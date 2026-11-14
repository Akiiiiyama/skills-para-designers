# Design system a partir da identidade

[Read in English](en.md)

Um design system com a cara de alguém começa por **quem essa pessoa é**, não por uma lista de componentes. Esta skill percorre o mesmo caminho do IY Lotus (veja a skill `lotus-design-system`), mas para qualquer pessoa ou marca: descobrir a identidade, torná-la visível, conseguir a aprovação e só então transformá-la em tokens testados e prontos para publicar.

Quem decide a identidade é a pessoa. O Claude pergunta, propõe opções, mostra e constrói, mas nunca impõe um estilo. Toda escolha visual precisa vir de algo que a pessoa disse.

## Quando usar

- Alguém quer o próprio design system para um portfólio, marca pessoal, projeto paralelo ou produto pequeno.
- A pessoa tem uma identidade ainda vaga ("minimalista, mas acolhedor", "forte como o meu reel") e quer transformá-la em regras.
- Não serve para auditar um sistema grande que já existe (use uma auditoria de design system) nem para escolher um kit de UI pronto.

## Passos

### 1. Entrevista de identidade (pergunte, não suponha)

Pergunte em rodadas curtas, nunca mais de 4 perguntas por vez. Use [`references/identity-interview/pt.md`](references/identity-interview/pt.md). Cubra:

- **Propósito e público**: o que vai ser construído primeiro (site, app, apresentação)? Quem vai ver?
- **Valores**: 3 ou 4 palavras que o trabalho deve transmitir (no IY Lotus: crescimento, beleza, disciplina, sabedoria).
- **Escalas de personalidade**: calmo ↔ enérgico, minimalista ↔ expressivo, quente ↔ frio, clássico ↔ experimental, arredondado ↔ reto, light ↔ dark primeiro.
- **Referências**: 3 coisas que a pessoa ama (sites, cartazes, um vídeo, um lugar) e 1 com a qual ela não quer se parecer. Pergunte o porquê de cada uma.
- **O que já existe**: logo, cores, fontes, um reel, uma foto. O que a pessoa já aprovou vale mais do que ideias novas.
- **Restrições**: ferramentas e planos (o Figma Starter tem um modo de variável por coleção e não tem bibliotecas compartilhadas), stack (React, HTML puro), necessidades de acessibilidade, idiomas.

Devolva um **brief de identidade** em um parágrafo e espere um sim antes de seguir.

### 2. Duas ou três direções

A partir do brief, proponha 2 ou 3 direções diferentes. Para cada uma: um nome para a direção, os 4 valores ligados a decisões visuais, uma paleta (neutros + 1 destaque, no máximo 2), uma combinação tipográfica (uma família basta; os pesos dão a voz), forma (raio), densidade (base do espaçamento), sensação do movimento (easing, duração) e **um detalhe assinatura** (no IY Lotus, o ponto vermelho depois de uma palavra). Mostre o contraste do texto sobre o fundo em cada paleta. Recomende uma e explique o porquê com as palavras da própria pessoa.

### 3. Um nome com significado

Ofereça de 6 a 10 nomes ligados aos valores ou à pessoa (iniciais + um símbolo funciona bem). Depois da escolha, transforme a metáfora no **nome das camadas** do sistema, por exemplo Root / Stem / Petal / Bloom, Chão / Parede / Cômodo / Casa, Semente / Galho / Folha / Árvore. As camadas são sempre: valores brutos → significado por tema → componentes → páginas.

### 4. Página de proposta visual (portão de aprovação)

Construa uma página HTML já na direção escolhida, não uma ficha técnica neutra. Siga [`references/proposal-page/pt.md`](references/proposal-page/pt.md): hero com o nome e o slogan, valores, paleta com contraste, escala tipográfica, espaçamento, raios, botões/inputs/cards em todos os estados, light e dark lado a lado. Ajuste conforme o retorno, **mudando só o que a pessoa apontou**. Tenha uma aprovação explícita ("aprovado") antes de qualquer código.

### 5. Escolher o caminho

- **Code-first** (recomendado quando o Figma é Starter/View ou quando a pessoa programa): os tokens num repositório são a fonte da verdade; o Figma recebe tudo depois, por plugin ou importação.
- **Figma-first** (plano pago com bibliotecas e modos, equipe de designers): variáveis no Figma, exportadas para JSON DTCG.

Diga qual e por quê num parágrafo do README da pessoa.

### 6. Tokens a partir do starter

Copie [`templates/starter`](templates/starter) para o projeto da pessoa e troque os valores de exemplo pela direção aprovada:

- `tokens/primitives.json` — paleta bruta, espaçamento (base de 4 px), raios, durações, easing, famílias tipográficas.
- `tokens/typography.json` — a escala tipográfica.
- `tokens/theme/light.json` e `tokens/theme/dark.json` — **só apelidos** (`{color.neutral.0}`), com os mesmos nomes nos dois.
- Defina `"dsPrefix"` no `package.json` (por exemplo `lotus`, `mx`); ele dá nome às classes CSS.

Depois rode `npm run build` (tokens → `dist/tokens.json`, `dist/tokens.css`) e `npm test` (contraste nos dois temas). Se um par falhar, mude o **apelido do tema**, não o mínimo. Se a cor da marca não passar como texto em um dos temas, use um tom mais claro ou mais escuro para texto e mantenha a cor da marca para marcas e preenchimentos, e registre essa regra.

### 7. Crescer

Nesta ordem, cada passo com preview e aprovação antes do próximo:

1. Estilos base: body, classes de tipografia, o detalhe assinatura.
2. Os componentes que a primeira página precisa (normalmente Button, Link, TextField, Card), com todos os estados e usando só variáveis de tema. Props com os mesmos nomes das variantes do Figma.
3. Página de documentação: Primitives, Components, Layouts, Foundations, Theme, Typography.
4. Figma: variáveis (coleção Root + coleção de tema com os modos Light/Dark, ou duas coleções no Starter), estilos de texto e componentes com os mesmos nomes.
5. Versionamento (Changesets) e publicação, só quando a pessoa quiser pacotes.

## Regras

- A identidade é da pessoa: toda escolha cita o brief. Se ela discordar, a palavra final é dela.
- Componentes nunca usam primitives; temas são apelidos; light e dark têm os mesmos nomes.
- WCAG AA é um teste que falha, não uma recomendação.
- O mesmo nome em todo lugar: `color/action/accent` ↔ `--color-action-accent` ↔ variável do Figma.
- Em cada rodada, mude só o que foi pedido.

## Checklist

- [ ] Brief de identidade aprovado
- [ ] Direção escolhida, nome com significado, nomes das camadas definidos
- [ ] Proposta visual aprovada de forma explícita
- [ ] Tokens do starter preenchidos, `npm test` passando no light e no dark
- [ ] Detalhe assinatura definido e documentado
- [ ] Caminho (code-first ou Figma-first) explicado no README

## Exemplo

IY Lotus — veja a skill `lotus-design-system` e `github.com/Akiiiiyama/iylotus`.
