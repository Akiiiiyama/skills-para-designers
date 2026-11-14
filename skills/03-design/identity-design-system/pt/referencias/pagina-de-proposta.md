# Página de proposta visual

[Read in English](../../en/references/proposal-page.md)

Um único arquivo HTML, construído **já na direção escolhida** (as cores, a tipografia e o detalhe assinatura dela), para a pessoa julgar o visual e não uma tabela. Uma página só, com rolagem.

## Seções, nesta ordem

1. **Hero** — o nome do sistema com o detalhe assinatura, o slogan (os valores) e uma linha sobre para que ele serve. Só palavras inteiras: nunca quebre uma palavra entre linhas na primeira dobra.
2. **Valores → decisões** — cada valor com a regra visual que ele virou.
3. **Paleta** — neutros e destaque como amostras com nome, hex e o contraste do texto sobre cada uma; marque os pares que passam no AA.
4. **Tipografia** — a escala (display → legenda) com frases reais do trabalho da pessoa, não lorem ipsum.
5. **Espaçamento, raios, elevação, movimento** — réguas visuais pequenas; uma demonstração do easing no hover.
6. **Componentes** — Button (variantes × tamanhos × padrão/hover/foco/desabilitado), TextField (padrão/foco/erro/desabilitado), Card. Pode ser estático; estados lado a lado.
7. **Light e dark** — o mesmo bloco nos dois temas, lado a lado.
8. **Camadas** — a metáfora (por exemplo Root / Stem / Petal / Bloom) com um exemplo por camada.

## Regras

- Cores como variáveis CSS em `:root`, redefinidas para o dark em `[data-theme="dark"]` e em `prefers-color-scheme`; o `body` tem um fundo explícito.
- Funciona na largura de celular (margens de 16 px, sem rolagem horizontal).
- Sem datas, números de versão ou "rascunho" no hero, a não ser que a pessoa peça.
- Depois de um retorno, mude só o que foi apontado e diga o que mudou.
- Mais tarde, a página vira a documentação (Primitives, Components, Layouts, Foundations, Theme, Typography).
