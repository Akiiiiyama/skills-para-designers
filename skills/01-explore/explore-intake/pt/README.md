# Intake do Explorar

Primeira etapa do Explorar. Lê o PRD da feature com olhar de designer, aponta o que falta para prototipar, pergunta só o que o PRD não responde e escreve o `prototype-plan.md`: a pergunta que o protótipo responde, o critério de desistência, as jornadas em escopo, o design system e quem aprova.

[Read in English](../en/README.md)

Funciona com PRDs no formato `prd` ou `prd-light` do [BMAD Method](https://github.com/bmad-code-org/BMAD-METHOD), usando os IDs deles (`UJ-N`, `FR-N`, `OQ-N`), e também com PRDs livres em Markdown.

## Instalar

```bash
git clone https://github.com/Akiiiiyama/skills-para-designers.git
cp -R skills-para-designers/skills/01-explore/explore-intake ~/.claude/skills/
```

Reinicie o Claude Code. Para ter o fluxo completo, com status e gates entre as etapas, instale também a [`explore`](../../explore/pt/README.md).

## Usar

Peça ao Claude: *"lê o PRD em docs/prd-votacao.md e planeja o protótipo"* ou *"o que falta nesse PRD antes de prototipar?"*. O Claude vai:

1. Ler o PRD inteiro e reconhecer o formato.
2. Encontrar as lacunas que afetam o protótipo ([lista](referencias/lacunas-do-prd.md)) e separar o que bloqueia, o que vira suposição e o que vai para o PM.
3. Perguntar em rodadas curtas: a pergunta e o critério de desistência, o escopo, o design system e a aprovação.
4. Escrever o plano a partir do [modelo](referencias/prototype-plan.md).
5. Mostrar o checklist do gate e marcar o plano como `final` só com o seu sim.

Para testar: [`examples/prd-clube-do-livro.md`](../examples/prd-clube-do-livro.md).

O modelo do plano é adaptado dos templates `prototype-plan` e `prd` do BMAD Method (licença MIT, © 2025 BMad Code, LLC).
