# IY Lotus — como o design system foi construído

[Read in English](../en/skill.md)

*Crescimento, beleza, disciplina e sabedoria.*

O IY Lotus é o design system por trás do isabelayukari.com. Ele não foi desenhado primeiro e codado depois: começou num vídeo de motion, virou uma proposta escrita e visual, foi aprovado e só então foi construído **com o código primeiro** (code-first). Os tokens num repositório são a fonte da verdade, e o Figma recebe tudo por um plugin. Esta skill conta essa história em ordem, com as decisões e os erros, para que ela possa ser recontada ou continuada.

Repositório: `github.com/Akiiiiyama/iylotus` (público, MIT). Site: `apps/site` no mesmo repositório, publicado na Vercel.

Dois modos:

- **Recontar** (case, palestra, post no LinkedIn, resposta de entrevista): siga [O processo](#o-processo) e os aprendizados; [`referencias/linha-do-tempo.md`](referencias/linha-do-tempo.md) tem o passo a passo com os artefatos.
- **Evoluir** (token, cor, componente ou página nova): siga [Evoluindo o IY Lotus](#evoluindo-o-iy-lotus). Nunca edite `dist/`.

## O processo

### 1. Começar de algo que já tem identidade

O sistema nasceu do reel da skill `brand-motion-intro` (Design Engineer → Product Designer, preto e um vermelho, tipografia light e bold em palavras inteiras). O visual já estava aprovado pela dona, então o sistema **extraiu** regras dele em vez de inventar um estilo: tinta quase preta, papel e superfície um passo acima, um vermelho de destaque em ~10% da tela, DM Sans em light (300) e bold (700) em palavras inteiras, e um ponto vermelho como assinatura (`IY.`).

### 2. Dar um nome com significado

Foram propostas dez opções de nome; a escolhida foi **IY Lotus 🌺 — Crescimento, beleza, disciplina e sabedoria**. A metáfora virou a arquitetura, então o nome não é enfeite:

| Camada | Significado | Conteúdo |
|---|---|---|
| **Root** (raiz) | primitives, valores brutos | `color/red/600 = #C8102E`, espaçamento de 4 px |
| **Stem** (caule) | tema, o significado no light e no dark | `color/action/accent` |
| **Petal** (pétala) | componentes | `<Button variant="accent" />` |
| **Bloom** (flor) | layouts e páginas | o site |

Os quatro valores viraram regras: **disciplina** (escala de 4 px, todos os estados de todo componente, o mesmo nome no Figma, no CSS e no React), **sabedoria** (WCAG AA como teste que falha), **beleza** (light + bold, um único destaque), **crescimento** (pacotes versionados, changesets).

### 3. Propor antes de construir: por escrito e depois visualmente

1. Uma proposta escrita: tokens, inputs, botões, cards, nomenclatura e como seria publicado (`@iylotus/tokens`, `@iylotus/styles`, `@iylotus/react`).
2. Uma **proposta visual em HTML** no estilo do reel, para a dona julgar o visual e não uma lista. Ajustada até a aprovação: equilíbrio entre light e dark, primeira dobra com palavras inteiras, sem datas nem rótulos de versão no hero.
3. Uma **página de documentação** separada (`docs/index.html`) com as seções Primitives, Components, Layouts, Foundations, Theme e Typography, e um header flutuante como o do site.

A aprovação foi explícita ("Design system aprovado") antes de existir qualquer pacote.

### 4. Escolher o caminho pelas restrições reais

O Figma estava no **plano Starter com assento View**: sem bibliotecas compartilhadas e com um modo de variável por coleção. Por isso o **caminho A, code-first**: o repositório é a fonte da verdade, e o Figma recebe variáveis, estilos e componentes de um plugin de desenvolvimento construído com os mesmos tokens. A alternativa (desenhar no Figma e exportar) dependeria de recursos pagos.

### 5. Tokens (Root + Stem)

- JSON no formato **DTCG** do W3C em `packages/tokens/src`: `primitives.json`, `typography.json`, `theme/light.json`, `theme/dark.json`.
- Os tokens de tema são **apelidos** (`{color.neutral.0}`); componentes nunca usam primitives.
- Um `scripts/build.mjs` sem dependências achata a árvore, resolve as referências (com checagem de referência circular ou inexistente), confere se light e dark têm **os mesmos nomes de token** e gera `dist/tokens.json`, `index.js` e `index.d.ts`.
- `test/contrast.test.mjs` (node:test) quebra o build se algum par de texto ficar abaixo de 4.5:1 ou de ícone/foco abaixo de 3:1, nos dois temas.

Decisão importante: no dark, o destaque de **texto** é `red/300` (#E4637A), porque `red/600` sobre o quase preto não passa 4.5:1 para texto. A marca (o ponto do `IY.` e dos títulos) é decorativa, então o site mantém `red/600` em todo lugar. É uma regra do site, não uma mudança de token.

### 6. CSS (`@iylotus/styles`)

Um segundo script transforma os tokens em variáveis CSS: primitives em `:root`, o tema light como padrão, o dark por `prefers-color-scheme` **e** por `[data-theme="dark"]` (para um bloco poder forçar um tema), uma classe por estilo de tipografia (`.iy-type-h2`) e as classes base `.iy-lt`, `.iy-bd` e `.iy-dot`. As variáveis de tema apontam para os primitives (`var(--color-neutral-950)`), então a camada Stem continua legível no devtools.

### 7. Componentes (Petal)

`@iylotus/react`, React + TypeScript compilado com `tsc`, CSS por componente reunido em `dist/styles.css`. v1: Button, TextField, TextArea, Select, Checkbox, Radio, Switch, Card, Tag, Badge, Avatar, Link e Divider. Storybook 8 com o addon de acessibilidade e uma barra para trocar o tema; testes de markup com `renderToStaticMarkup`. As props usam as mesmas palavras das variantes do Figma (`variant=accent, size=md`).

### 8. O Figma, a partir do código

`packages/figma-plugin`: os tokens entram no plugin no build, sem acesso à rede. Os comandos criam as coleções `IY Lotus · Root` e `IY Lotus · Stem` (Light/Dark), estilos de texto e de efeito, uma página Root com amostras ligadas às variáveis e conjuntos de componentes para todos os componentes da v1. No Starter (um modo só), o dark vai para uma segunda coleção e o plugin avisa. Testado em node com uma API do Figma simulada antes de a dona rodar no Figma de verdade.

### 9. Publicar e aplicar (Bloom)

Monorepo com npm workspaces, **Changesets** com versões fixas, CI no GitHub Actions nos PRs e um workflow de release que só publica quando existe o `NPM_TOKEN`. Depois o site (`apps/site`, Next.js) usou o sistema de verdade: hero, cards, um notebook mostrando a documentação no dark, motion de abertura. Toda mudança visual passou por um preview local aprovado pela dona antes do merge.

## Aprendizados (guarde estes)

- **Mude só o que foi pedido.** Refazer partes aprovadas "já que estava ali" custou um revert.
- **Mostre, depois construa.** Uma proposta visual no estilo da própria marca foi aprovada mais rápido do que qualquer tabela de tokens.
- **As restrições escolhem a arquitetura.** O plano do Figma decidiu o code-first; explique o porquê no README.
- **Torne os valores executáveis.** "Sabedoria = acessibilidade" só ficou real quando o contraste virou um teste que falha.
- **Separe o destaque de texto da marca.** A cor acessível para texto e a cor da marca podem mudar por tema; decida onde cada uma vale.
- **O mesmo nome em todo lugar.** `color/action/accent` ↔ `--color-action-accent` ↔ `themes.light.color.action.accent` ↔ variável do Figma.
- **Preview, aprovação, depois publicação.** Deploy em produção só depois que a dona disser que pode.

## Evoluindo o IY Lotus

1. Edite só `packages/tokens/src/*.json` (ou o componente em `packages/react/src/<Nome>`).
2. Cor nova: crie o primitive no Root; se os componentes precisarem dela, crie um apelido **Stem** em `light.json` **e** em `dark.json` (o build falha se forem diferentes).
3. Se for uma cor de texto, ícone ou foco, acrescente o par em `PAIRS` no `test/contrast.test.mjs`.
4. `npm run build && npm test` na raiz do repositório.
5. Componente novo: o CSS usa só variáveis de tema; crie uma story com todos os estados; crie um teste SSR; inclua no plugin do Figma com os mesmos nomes de variante.
6. `npm run changeset` (patch, minor ou major), abra um PR, faça o preview e espere a aprovação.

## Checklist

- [ ] Nenhum primitive usado direto num componente
- [ ] Light e dark com os mesmos tokens
- [ ] Testes de contraste passando nos dois temas
- [ ] O mesmo nome no JSON, no CSS, nas props do React e no Figma
- [ ] Todos os estados interativos existem (padrão, hover, foco, desabilitado e erro quando fizer sentido)
- [ ] Changeset criado; nada em `dist/` editado à mão
