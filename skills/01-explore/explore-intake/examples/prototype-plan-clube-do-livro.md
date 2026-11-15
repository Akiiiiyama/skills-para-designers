---
title: "Votação do próximo livro"
template: prototype-plan
adapted_from: "BMAD Method prototype-plan 1.1.0 (MIT, © 2025 BMad Code, LLC)"
stage: 1-intake
status: final
prd: "examples/prd-clube-do-livro.md"
design_system: "iylotus/packages/tokens/dist/tokens.json"
form_factor: "mobile web"
created: "2026-11-14"
updated: "2026-11-14"
---

<!-- Saída de exemplo da skill explore-intake rodada sobre prd-clube-do-livro.md.
     As respostas da designer foram simuladas no teste; numa exploração real elas vêm da pessoa. -->

# Votação do próximo livro · plano do protótipo

## Pergunta e critério de desistência

**Pergunta:** Um membro que chega pelo link do grupo do WhatsApp consegue votar sem ajuda e sem desistir no login?

**Critério de desistência:** Se 2 de 5 pessoas no teste desistirem ou pedirem ajuda antes de ver o voto confirmado, ou se o caminho do link até o voto confirmado precisar de mais de 3 telas.

## Escopo

**Jornadas em escopo:**

- `UJ-2` · membro do clube que abre o link no celular · clímax: ver que o voto foi contado · usa `FR-5`
- `UJ-3` · o mesmo membro, depois do prazo · clímax: ver o livro vencedor · usa `FR-7`

**Fora do protótipo:**

- `UJ-1` (Ana abre a rodada): a pergunta é sobre quem vota; a rodada aparece já criada, com 3 livros.
- `FR-3`, `FR-4` (acompanhar e lembrar quem falta votar): fazem parte da `UJ-1`.
- `FR-6` (comentar sinopse) e `FR-8` (sugerir livro): nenhuma jornada usa.

## Formato e design system

- **Formato:** mobile web (os membros chegam pelo WhatsApp; o PRD diz só "web app").
- **Design system:** IY Lotus, `iylotus/packages/tokens/dist/tokens.json`. O Lotus ainda não tem um `DESIGN.md`.
- **Saída:** protótipo HTML de baixa fidelidade com o design system no tema wireframe.

## Suposições

- [SUPOSIÇÃO] A `UJ-2` não tem protagonista: usamos "Bia, membro do clube há 2 meses, que abre o link no ônibus". (jornada sem protagonista)
- [SUPOSIÇÃO] O clímax da `UJ-2` é uma confirmação clara de que o voto foi contado, com a opção de mudar. (jornada sem clímax)
- [SUPOSIÇÃO] Quem chega pelo link vota primeiro e confirma o e-mail do link mágico depois; o voto fica pendente até a confirmação. É justamente o que o protótipo testa. (estado de entrada indefinido)
- [SUPOSIÇÃO] Se o link for aberto depois do prazo, a pessoa vai direto para o resultado. (falha não descrita)

## Perguntas para produto

- "Rodada" e "votação" aparecem como sinônimos no PRD. Sugestão: rodada é o ciclo do mês; votação é o período em que dá para votar dentro dela. Vale entrar num glossário.
- O passo "compartilha o link no grupo do WhatsApp" da `UJ-1` não tem requisito. Falta um `FR` para copiar ou compartilhar o link.
- `FR-6` e `FR-8` não estão em nenhuma jornada: entram no MVP?
- `OQ-2` (membro novo no meio da rodada) continua aberta e não afeta este protótipo.

## Aprovação

- **Quem aprova:** a designer, depois de testar com 5 membros de clubes do livro.
- **Como:** link do protótipo aberto no celular de cada pessoa, com a tarefa "vote no livro que você prefere".
- **Limite de tempo:** 2 dias até o protótipo estar pronto para teste.

## Referências

(etapa 2)

## Conceitos

(etapa 3)

## Decisões

- O escopo ficou em `UJ-2` + `UJ-3`, porque a pergunta é sobre quem vota, não sobre quem organiza.
- O formato é mobile web, porque o link chega pelo WhatsApp.
- `OQ-1` foi resolvida para o protótipo: em empate, aparece "empate entre A e B, a Ana decide" até a organizadora escolher. Era bloqueante porque mudava a tela de resultado da `UJ-3`.

## Resultado

(etapa 5)
