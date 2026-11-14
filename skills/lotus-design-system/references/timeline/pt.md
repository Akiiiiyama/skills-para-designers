# IY Lotus — linha do tempo com artefatos

[Read in English](en.md)

Use ao recontar a história (case, palestra, post). Cada etapa mostra o que foi produzido e o que a dona decidiu.

| # | Etapa | Artefato | Decisão |
|---|---|---|---|
| 1 | Reel de marca | reel da `brand-motion-intro`, 9:16 e 16:9 em 4K | Preto e um vermelho, palavras inteiras em light/bold, ponto vermelho como assinatura |
| 2 | Ideia do site | — | Construir o portfólio em React, que também serve de material de estudo |
| 3 | Nome | 10 opções de nome | **IY Lotus 🌺 — Crescimento, beleza, disciplina e sabedoria** |
| 4 | Proposta escrita | tokens, inputs, botões, cards, nomes dos pacotes | Direção aprovada; escopo npm `@iylotus/*` |
| 5 | Proposta visual | página HTML no estilo do reel | Ajustes: equilíbrio light/dark, palavras inteiras na primeira dobra, sem datas |
| 6 | Página de documentação | `docs/index.html`, seções 1 a 6, header flutuante, sem grid | "Design system aprovado" |
| 7 | Escolha do caminho | — | Caminho A, code-first (Figma Starter, assento View) |
| 8 | Tokens | `@iylotus/tokens`: JSON DTCG, script de build, testes de contraste | Apelidos Root → Stem; destaque de texto no dark = red/300 |
| 9 | Estilos | `@iylotus/styles`: variáveis CSS, temas, classes de tipografia | `[data-theme]` + `prefers-color-scheme` |
| 10 | Componentes | `@iylotus/react`: 13 componentes, Storybook, testes SSR | Props = nomes das variantes do Figma |
| 11 | Plugin do Figma | plugin de desenvolvimento: variáveis, estilos e componentes | No Starter, o dark vai para uma segunda coleção; conferido no Figma de verdade |
| 12 | Preparação do release | Changesets (versões fixas), CI, workflow de release com `NPM_TOKEN` | 0.1.0 pronta; a publicação espera a organização no npm |
| 13 | Site | `apps/site` (Next.js) na Vercel, domínio isabelayukari.com | Toda mudança com preview local e aprovação antes do merge |

## Versão em um parágrafo

O IY Lotus começou de um reel de motion que já tinha uma cara: preto, um vermelho, tipografia light e bold. Dei a ele o nome do que eu quero que o meu trabalho tenha (crescimento, beleza, disciplina e sabedoria) e transformei a flor de lótus na arquitetura: Root (valores brutos), Stem (temas), Petal (componentes), Bloom (páginas). Propus por escrito e depois como uma página no estilo do próprio reel, aprovei e construí com o código primeiro, porque o meu plano do Figma não comportava uma biblioteca compartilhada: tokens DTCG com um script de build, variáveis CSS para light e dark, componentes React com Storybook, contraste como um teste que falha e um plugin do Figma que recria as mesmas variáveis e componentes a partir do código. Depois usei tudo isso para construir o meu site.
