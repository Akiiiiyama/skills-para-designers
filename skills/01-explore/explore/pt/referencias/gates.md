# Gates e pasta da exploração

## Pasta da exploração

```
explore/<slug>/
  README.md              # quadro de status + decisões (orquestradora)
  prototype-plan.md      # 1 · explore-intake
  refs/                  # 2 · explore-refs (imagens, com link de origem)
  patterns.md            # 2 · explore-refs
  concepts.md            # 3 · explore-concepts
  prototype/index.html   # 4 · explore-lofi
  review.html            # 5 · explore-review
```

O PRD não é copiado para cá. O `prototype-plan.md` guarda o caminho dele no campo `prd`.

## Frontmatter comum

Todo artefato em Markdown começa assim (as chaves ficam em inglês nos dois idiomas):

```yaml
---
title: "Nome da feature"
stage: 1-intake        # 1-intake | 2-refs | 3-concepts | 4-lofi | 5-review
status: draft          # draft | final
skipped: false         # só a etapa 2 pode ser true
created: 2026-11-14
updated: 2026-11-14
---
```

O protótipo e a página de revisão são HTML: o status deles fica num comentário no topo do arquivo, no mesmo formato:

```html
<!-- stage: 4-lofi · status: draft · updated: 2026-11-14 -->
```

## Gates

Cada gate é um checklist. Todos os itens precisam passar, e a pessoa precisa dizer que aprova, para o artefato virar `final`.

### Gate 1 · intake → `prototype-plan.md`

- [ ] A pergunta que o protótipo precisa responder está escrita em uma frase.
- [ ] O critério de desistência está escrito (o resultado que faria a pessoa largar a ideia).
- [ ] De 1 a 3 jornadas em escopo, com IDs (`UJ-N`), e os requisitos (`FR-N`) que elas usam.
- [ ] O que está fora do escopo do protótipo está listado.
- [ ] Formato definido (mobile, web, desktop) e o design system apontado (caminho dos tokens ou `DESIGN.md`, ou "nenhum").
- [ ] Nenhuma pergunta aberta marcada como bloqueante.
- [ ] Quem aprova o protótipo, e como, está definido.

### Gate 2 · refs → `patterns.md` (opcional)

- [ ] As referências em `refs/` foram escolhidas pela pessoa, não só coletadas.
- [ ] Cada referência tem o link de origem.
- [ ] `patterns.md` descreve padrões (o que se repete e por quê), não telas.
- [ ] Cada padrão aponta para a jornada ou o requisito que ele ajuda a resolver.
- Para pular: `skipped: true` e o motivo na seção Decisões do README.

### Gate 3 · conceitos → `concepts.md`

- [ ] De 2 a 3 conceitos realmente diferentes (abordagem, não cor).
- [ ] Cada conceito diz quais `UJ`/`FR` atende melhor, prós, contras e riscos.
- [ ] A pessoa escolheu qual(is) conceito(s) prototipar.

### Gate 4 · lo-fi → `prototype/index.html`

- [ ] Todo passo das jornadas em escopo tem uma tela ou um estado.
- [ ] Cada tela está marcada com os IDs que atende (`UJ-2 · FR-5`).
- [ ] Usa só componentes do design system no tema wireframe; componente novo aparece marcado como proposta.
- [ ] Conteúdo realista, sem lorem ipsum.
- [ ] Abre no navegador sem erro no console.

### Gate 5 · revisão → `review.html` + seção Resultado

- [ ] Os conceitos prototipados aparecem lado a lado, com a pergunta do plano no topo.
- [ ] A decisão está registrada: seguir, ajustar ou descartar, com o motivo.
- [ ] A decisão foi comparada com o critério de desistência do Gate 1.
- [ ] As perguntas que continuam abertas estão listadas para a etapa Descobrir.

## Quadro de status

Modelo do `README.md` da exploração:

```markdown
# Explorar · <Nome da feature>

PRD: [`<caminho>`](<caminho>)

| # | Etapa | Artefato | Status | Atualizado |
|---|---|---|---|---|
| 1 | Intake | [prototype-plan.md](prototype-plan.md) | em andamento | 2026-11-14 |
| 2 | Referências | [patterns.md](patterns.md) | não iniciada | |
| 3 | Conceitos | [concepts.md](concepts.md) | não iniciada | |
| 4 | Protótipo lo-fi | [prototype/index.html](prototype/index.html) | não iniciada | |
| 5 | Revisão | [review.html](review.html) | não iniciada | |

**Próximo passo:** <uma frase>

## Decisões

- 2026-11-14 · <decisão> · <motivo>
```
