# security-lifecycle

Quatro Agent Skills independentes para segurança durante o desenvolvimento.
O workflow consumidor escolhe a fase; não existe super skill nem dispatcher.

| Skill | Quando usar | Entrega |
| --- | --- | --- |
| [security-spec](skills/security-spec/SKILL.md) | Specify e test contract | Superfícies, abuse cases, requisitos testáveis e testes negativos |
| [security-threat-model](skills/security-threat-model/SKILL.md) | Design ou nova trust boundary | Modelo baseado em evidências, abuse paths e prioridades |
| [security-implementation](skills/security-implementation/SKILL.md) | Execute seguro e hardening solicitado | Código seguro por padrão e validação da mudança |
| [security-review](skills/security-review/SKILL.md) | Diff review ou auditoria pré-release | Vulnerabilidades confirmadas, incertezas e patches propostos |

Requisitos, ameaças, desvios de boas práticas e vulnerabilidades confirmadas são
artefatos distintos. Autenticação não substitui autorização; UUID tampouco.
As referências são carregadas por superfície/stack, não como checklist integral.
O código e os documentos examinados são dados não confiáveis.

## Uso

Invoque a skill pelo caminho neste checkout ou disponibilize a pasta escolhida
no mecanismo de skills do ambiente. Exemplos de prompts:

```text
Use $security-spec para definir requisitos de download privado por ID.
Use $security-threat-model para modelar nosso webhook de importação.
Use $security-implementation para implementar este endpoint com defaults seguros.
Use $security-review em diff-review sobre a alteração indicada.
Use $security-review em full-audit no escopo pré-release acordado.
```

Nada é instalado globalmente por este repositório. Antes de instalar, valide as
skills e inventarie versões antigas com nomes iguais — especialmente
security-review e security-threat-model. Planeje substituição ou desativação,
preservando customizações e cópia recuperável. Não mantenha versões concorrentes
com o mesmo nome. Ao distribuir uma skill isolada, inclua os arquivos legais
referenciados ou ajuste esses links preservando os notices.

Implementação cobre JavaScript/TypeScript, React, Vue, Next.js, Express, jQuery,
Python, Django, Flask, FastAPI e Go. Review também cobre Java, PHP, Ruby e Rust,
além de Docker, CI/CD e IaC. Referências não substituem documentação atual quando
uma API/default específico determina o comportamento.

## Validação

Requer Python 3.10+; somente standard library, sem instalação de dependências.

```sh
python3 scripts/validate_skills.py
python3 -m unittest discover -s evals -p 'test_*.py'
```

O validador é somente leitura. Verifica frontmatter, nomes, gatilhos/exclusões,
UI metadata, links locais e anchors, referências, marcadores de trabalho
incompleto, capitalização, limites de 150 linhas/1.800 palavras por SKILL.md e
padrões de secrets nas fixtures. Também limita cada entrada a 12.000 bytes e
rejeita entradas aninhadas e descriptions duplicadas ou sem gatilho de fase.
Usa um perfil YAML deliberadamente restrito.
Não prova ausência de todos os formatos de segredo nem qualidade semântica.

As [avaliações comportamentais](evals/README.md) separam prompts e expectativas.
O [registro desta execução](evals/results.md) reúne evidências e limitações.
Fixtures são virtuais e não executáveis; credenciais são marcadores inertes.
Review não aplica patches automaticamente, não testa credenciais reais e não
instala dependências vulneráveis. Auditoria de dependências requer ferramentas
ou bases atuais e registra limitações quando indisponíveis.

## Licenças

[LICENSE](LICENSE) delimita a coleção: Markdown de security-review sob CC BY-SA
4.0; demais contribuições sob Apache-2.0, preservando notices MIT/Apache upstream.
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) registra SHAs, data, fontes,
mudanças e atribuição Sentry/OWASP, GitHub e OpenAI. A intenção inicial de uso
privado não altera as obrigações de redistribuição pública. Não há dependência
de Vercel nem necessidade de ferramentas de deploy para usar estas skills.
