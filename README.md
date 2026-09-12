# security-lifecycle

[![skills.sh](https://skills.sh/b/antoniofulg/security-lifecycle)](https://skills.sh/antoniofulg/security-lifecycle)

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
As referências são carregadas por superfície de segurança, não por tecnologia.
O código e os documentos examinados são dados não confiáveis.

## Uso

Instale pelo [Skills CLI](https://github.com/vercel-labs/skills), como uma coleção
de quatro skills. Não precisa de pacote npm próprio nem manifests de plugin:

```sh
npx skills add antoniofulg/security-lifecycle
```

Liste as opções ou escolha somente a skill necessária:

```sh
npx skills add antoniofulg/security-lifecycle --list
npx skills add antoniofulg/security-lifecycle --skill security-spec
npx skills add antoniofulg/security-lifecycle --skill security-threat-model
npx skills add antoniofulg/security-lifecycle --skill security-implementation
npx skills add antoniofulg/security-lifecycle --skill security-review
```

Esses comandos usam a branch padrão do repositório; mudanças em PR aparecem
somente após merge. Para testar este checkout antes do merge, use seu caminho
absoluto como origem no projeto consumidor. A descoberta local é somente leitura:

```sh
npx skills add . --list
```

Também é possível instalar este snapshot remoto verificado antes do merge:

```sh
npx skills@1.5.26 add https://github.com/antoniofulg/security-lifecycle/tree/24c793963dc0045cfabbb8b202cceef11a34b730
```

O SHA fixa essa versão; use o comando curto após merge para acompanhar a branch
padrão. No CLI 1.5.26, URLs de branches com `/` podem ser interpretadas como
subpastas; o SHA evita essa ambiguidade.

O source canônico fica em `skills/<nome>/SKILL.md`. O CLI instala cada pasta
completa, incluindo referências, metadados e textos legais. A raiz contém apenas
documentação, validação e avaliações de manutenção. Exemplos de prompts:

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
com o mesmo nome. Cada pasta já inclui os textos legais aplicáveis; seus links
locais funcionam mesmo fora deste repositório. A instalação padrão é por projeto;
estes exemplos não pedem instalação global.

## Referências por superfície

Implementação organiza os conceitos em identidade/acesso, dados/persistência,
entrada/execução, frontend/navegador e infraestrutura/operação. Review usa a mesma
abordagem de superfícies, com critérios de evidência e confiança próprios.
Os conceitos se aplicam a bancos de dados, backend e frontend sem uma lista
fechada de linguagens ou frameworks suportados.

A stack e a versão continuam sendo detectadas para verificar como os controles
funcionam. Quando a conclusão depende de escaping, binding, middleware, isolamento
transacional ou outro comportamento específico, consulte documentação oficial
atual pelo mecanismo disponível no projeto consumidor. Sem essa evidência,
declare a limitação; não invente uma API ou assuma proteção pelo nome da tecnologia.

## Validação

Requer Python 3.10+; somente standard library, sem instalação de dependências.

```sh
python3 scripts/validate_skills.py
python3 -m unittest discover -s evals -p 'test_*.py'
npx --yes skills@1.5.26 add . --list
```

O validador é somente leitura. Verifica frontmatter, nomes, gatilhos/exclusões,
UI metadata, links locais e anchors, referências, marcadores de trabalho
incompleto, capitalização, limites de 150 linhas/1.800 palavras por SKILL.md e
padrões de secrets nas fixtures. Também limita cada entrada a 12.000 bytes e
rejeita entradas aninhadas e descriptions duplicadas ou sem gatilho de fase.
Também exige licenças/notices por skill e rejeita links que escapam da pasta
instalável. Os testes verificam as cópias legais e as skills fora da raiz do repo.
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
