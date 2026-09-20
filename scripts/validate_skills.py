#!/usr/bin/env python3
"""Read-only structural validation; Python standard library only.

The repository deliberately uses a small YAML profile: name/description are
single-line plain or JSON-quoted strings. This is not a general YAML parser.
Markdown supports inline links, reference links and GitHub heading anchors.
Secret detection is heuristic, not proof of absence of every possible credential.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


NAMES = {
    "security-audit-coordinator",
    "security-implementation",
    "security-review",
    "security-spec",
    "security-threat-model",
}
SECRET_MARKER = "[REDACTED_TEST_SECRET]"
UNFINISHED_PATTERN = re.compile(r"\b(?:" + "|".join(
    ("TO" + "DO", "TB" + "D", "FIX" + "ME", "PLACE" + "HOLDER", "YOUR_" + "[A-Z_]+")
) + r")\b|\[(?i:insert)\b")
TOKEN = re.compile(
    r"(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|"
    r"AKIA[A-Z0-9]{16}|xox[baprs]-[A-Za-z0-9-]{20,}|sk-(?:live-|proj-)?[A-Za-z0-9_-]{20,}|"
    r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|"
    r"eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+|"
    r"[a-z]+://[^\s/:]+:[^\s/@]+@)"
)
ASSIGNED_SECRET = re.compile(
    r'''(?im)["']?\b(?:[A-Z_]*(?:SECRET|TOKEN|PASSWORD|API_KEY|PRIVATE_KEY|ACCESS_KEY)[A-Z_]*)["']?\s*[:=]\s*["']([^"'\n]+)["']'''
)


def scalar(value):
    if value.startswith('"'):
        result = json.loads(value)
        if not isinstance(result, str):
            raise ValueError("expected string")
        return result
    if not value or value[0] in "'|>{[&*!":
        raise ValueError("use a plain or JSON-quoted single-line string")
    return value


def metadata(text):
    lines = text.splitlines()
    if not lines or lines[0] != "---" or "---" not in lines[1:]:
        raise ValueError("missing frontmatter delimiters")
    end = lines.index("---", 1)
    fields = {}
    for line in lines[1:end]:
        key, sep, value = line.partition(":")
        if not sep or key not in {"name", "description"} or key in fields:
            raise ValueError("expected unique name/description fields")
        fields[key] = scalar(value.strip())
    if set(fields) != {"name", "description"}:
        raise ValueError("name and description required")
    return fields


def without_fences(text):
    lines, fence = [], None
    for line in text.splitlines():
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence) and not marker[2].strip():
                fence = None
        elif marker:
            fence = marker[1]
        else:
            lines.append(line)
    return "\n".join(lines)


def anchors(text):
    text = without_fences(text)
    result, counts = set(), {}
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", text, re.M):
        slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        result.add(slug + (f"-{count}" if count else ""))
    result.update(re.findall(r'(?:id|name)=["\']([^"\']+)', text))
    return result


def links(text):
    # Fenced examples are data, not rendered Markdown links.
    rendered = without_fences(text)
    refs = dict((k.casefold(), v.strip("<>")) for k, v in re.findall(
        r"^\s*\[([^\]]+)\]:\s*(<[^>\n]+>|[^\s]+)", rendered, re.M))
    targets = [v.strip("<>") for v in re.findall(
        r"\[[^\]\n]*\]\((<[^>\n]+>|[^\s)>]+)(?:\s+\"[^\"]*\")?\)", rendered)]
    missing = []
    for label, key in re.findall(r"\[([^\]\n]+)\]\[([^\]\n]*)\]", rendered):
        key = (key or label).casefold()
        if key in refs:
            targets.append(refs[key])
        else:
            missing.append(key)
    targets.extend(refs.values())
    # Bare code-form reference pointers must also exist.
    targets.extend(re.findall(r"`((?:\.{1,2}/)*(?:references|agents|scripts)/[^`\s*]+)`", rendered))
    return targets, missing


def fixture_texts(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for item in value.values():
            yield from fixture_texts(item)
    elif isinstance(value, list):
        for item in value:
            yield from fixture_texts(item)


def validate(root):
    root = Path(root).resolve()
    errors, names, descriptions = [], set(), set()

    def fail(path, message):
        errors.append(f"{path.relative_to(root)}: {message}")

    files = [p for p in root.rglob("*") if p.is_file()
             and not any(part in {".git", "__pycache__"} for part in p.relative_to(root).parts)]
    for path in files:
        if path.name.lower() == "skill.md" and path.name != "SKILL.md":
            fail(path, "entrypoint must be capitalized SKILL.md")
    skill_root = root / "skills"
    if not skill_root.is_dir():
        return ["skills/: missing directory"]
    expected = {skill_root / name / "SKILL.md" for name in NAMES}
    if {p for p in files if p.name == "SKILL.md"} != expected:
        errors.append("skills/: expected exactly five entrypoints, without nested SKILL.md files")
    dirs = {p.name for p in skill_root.iterdir() if p.is_dir()}
    if dirs != NAMES:
        errors.append("skills/: expected exactly the five security-lifecycle directories")
    for directory in sorted(skill_root.iterdir()):
        if not directory.is_dir():
            continue
        path = directory / "SKILL.md"
        for bundled in ("LICENSE", "THIRD_PARTY_NOTICES.md"):
            if not (directory / bundled).is_file():
                fail(directory / bundled, "missing bundled license or provenance")
        if not path.is_file():
            fail(path, "missing SKILL.md")
            continue
        text = path.read_text(encoding="utf-8")
        try:
            fields = metadata(text)
            name, description = fields["name"], fields["description"]
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
                fail(path, "invalid name")
            if name in names:
                fail(path, "duplicate skill name")
            names.add(name)
            if name != directory.name:
                fail(path, "name must match directory")
            if not description.strip() or len(description) > 1024:
                fail(path, "description must be nonblank and at most 1024 characters")
            if description.strip().casefold() in descriptions:
                fail(path, "duplicate description")
            descriptions.add(description.strip().casefold())
        except (ValueError, json.JSONDecodeError) as exc:
            fail(path, f"invalid frontmatter: {exc}")
        if len(text.splitlines()) > 150 or len(text.split()) > 1800 or len(text.encode()) > 12000:
            fail(path, "SKILL.md exceeds 150 lines, 1800 words or 12000 bytes")
        ui = directory / "agents" / "openai.yaml"
        if not ui.is_file():
            fail(ui, "missing UI metadata")
        else:
            try:
                ui_lines = ui.read_text().splitlines()
                if not ui_lines or ui_lines[0] != "interface:":
                    raise ValueError("interface mapping required")
                values = {}
                for line in ui_lines[1:]:
                    key, sep, value = line.strip().partition(":")
                    if not sep or key in values or not value.strip().startswith('"'):
                        raise ValueError("unique quoted interface fields required")
                    values[key] = scalar(value.strip())
                if set(values) != {"display_name", "short_description", "default_prompt"}:
                    raise ValueError("three interface fields required")
                if not 25 <= len(values["short_description"]) <= 64:
                    raise ValueError("short_description must be 25–64 characters")
                if "$" + directory.name not in values["default_prompt"]:
                    raise ValueError("default_prompt must invoke its skill")
            except (ValueError, json.JSONDecodeError) as exc:
                fail(ui, str(exc))

    for path in files:
        if "evals" in path.relative_to(root).parts:
            try:
                fixture = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                fail(path, "binary fixture cannot be checked for secrets")
                continue
            try:
                values = fixture_texts(json.loads(fixture)) if path.suffix == ".json" else [fixture]
                for value in values:
                    if TOKEN.search(value) or any(m != SECRET_MARKER for m in ASSIGNED_SECRET.findall(value)):
                        fail(path, "possible secret value in fixture (value suppressed)")
                        break
            except json.JSONDecodeError:
                fail(path, "invalid JSON")
        if path.suffix not in {".md", ".yaml", ".json", ".py", ".env", ".ts", ".js", ".txt"}:
            continue
        if "licenses" in path.relative_to(root).parts:
            continue  # Verbatim legal appendices contain example copyright fields.
        text = path.read_text(encoding="utf-8")
        if UNFINISHED_PATTERN.search(text):
            fail(path, "unfinished placeholder")
        if path.suffix == ".md":
            targets, missing = links(text)
            for key in missing:
                fail(path, f"undefined link reference: {key}")
            for target in targets:
                url = urlsplit(target)
                if url.scheme or url.netloc:
                    continue
                dest = (path.parent / unquote(url.path)).resolve() if url.path else path
                if path.is_relative_to(skill_root) and not dest.is_relative_to(
                    skill_root / path.relative_to(skill_root).parts[0]
                ):
                    fail(path, "local link escapes installable skill")
                elif not dest.is_relative_to(root):
                    fail(path, "local link escapes repository")
                elif not dest.exists():
                    fail(path, f"broken local link: {target}")
                elif url.fragment and dest.is_file() and dest.suffix == ".md":
                    if unquote(url.fragment) not in anchors(dest.read_text(encoding="utf-8")):
                        fail(path, f"broken heading anchor: {target}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate(args.root)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("PASS: five skills; metadata, references, links, placeholders, fixture secrets and size limits")
    return 0


if __name__ == "__main__":
    sys.exit(main())
