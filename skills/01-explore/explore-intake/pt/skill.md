# Intake do Explorar

[Read in English](../en/skill.md)

Antes de desenhar qualquer coisa, o protótipo precisa de um plano: **qual pergunta ele responde, o que faria a ideia ser descartada, qual pedaço do PRD entra e quem aprova**. Esta skill lê o PRD com olhar de designer, encontra o que falta para prototipar, pergunta à pessoa só o que o PRD não responde e escreve o `prototype-plan.md`.

O intake não desenha telas nem propõe soluções. Ele prepara o terreno para as etapas seguintes (referências, conceitos, protótipo lo-fi).

## Quando usar

- Existe um PRD (ou um rascunho) e a pessoa quer prototipar uma ideia para aprovação.
- A pessoa quer saber o que falta no PRD antes de começar.
- A skill `explore` (orquestradora) chamou a etapa 1.
- Não serve para escrever o PRD do zero (isso é trabalho de produto; o template `prd` do BMAD Method serve para isso) nem para revisar o PRD para engenharia.

## Passos

### 1. Encontrar a exploração e o PRD

- Se a orquestradora passou a pasta `explore/<slug>/`, use-a. Se não, crie a pasta e o `README.md` com o quadro de status, como descrito em `gates.md` da skill `explore` (ou só a pasta e o plano, se a orquestradora não estiver instalada).
- Peça o caminho do PRD, ou procure `*prd*.md` no projeto e confirme com a pessoa qual é.
- Se já existe um `prototype-plan.md` na pasta, leia-o e continue de onde parou, em vez de começar de novo.

### 2. Ler o PRD inteiro e reconhecer o formato

Leia o PRD do começo ao fim antes de perguntar qualquer coisa.

- **PRD do BMAD Method**: o frontmatter tem `template: prd` ou `template: prd-light`. Use os IDs como estão: jornadas `UJ-N`, requisitos `FR-N`, regras `RULE-N`, métricas `SM-N`, perguntas abertas `OQ-N`.
- **PRD livre**: encontre o equivalente de cada seção (visão, usuários e jornadas, requisitos, não-objetivos, escopo, métricas, perguntas abertas). Se não houver IDs, numere jornadas e requisitos **no plano**, marcados como provisórios, e ofereça adicioná-los ao PRD. O PRD é de quem o escreveu: não edite sem pedir.

Faça um resumo de uso interno: a visão em uma frase, as jornadas (protagonista + clímax), os requisitos agrupados por jornada, os não-objetivos e as perguntas abertas. Não copie o PRD para o plano; o plano aponta para os IDs.

### 3. Encontrar as lacunas

Percorra [`referencias/lacunas-do-prd.md`](referencias/lacunas-do-prd.md). Só conta como lacuna o que afeta o **protótipo**; detalhes de engenharia, dados e operação ficam de fora.

Classifique cada lacuna:

- **bloqueante**: sem a resposta, não dá para saber o que prototipar. Precisa ser resolvida antes do gate.
- **vira suposição**: dá para seguir com uma hipótese razoável. Entra no plano com a marca `[SUPOSIÇÃO]`, e o protótipo serve para testá-la.
- **para produto**: não trava o protótipo, mas o PM precisa saber. Vai para a seção "Perguntas para produto" do plano.

### 4. Perguntar só o que o PRD não responde

Faça rodadas curtas, no máximo 4 perguntas por vez. Quando o PRD já sugere a resposta, **proponha e peça confirmação** em vez de perguntar do zero ("Pelo PRD, a jornada principal é a UJ-1. Fica só ela?").

Ordem das rodadas:

1. **Pergunta e critério de desistência.** O que o protótipo precisa responder, em uma frase? Que resultado faria você largar a ideia? O critério precisa ser observável e escrito antes de construir, porque um critério definido depois sempre favorece o resultado. Exemplos: "se 3 de 5 pessoas não encontrarem onde votar sem ajuda", "se o fluxo principal precisar de mais de 4 telas".
2. **Escopo.** Quais jornadas entram (de 1 a 3)? Qual é o formato (mobile, web, desktop)? Se a pessoa quiser o PRD inteiro, diga que um protótipo menor responde à pergunta mais rápido, sugira o que pode esperar e deixe a decisão com ela.
3. **Design system e aprovação.** Qual design system usar? Procure no projeto antes de perguntar (`DESIGN.md`, `tokens/*.json`, `dist/tokens.css`, um Storybook, um pacote com `dsPrefix`) e confirme com a pessoa; "nenhum" também é resposta, e aí o protótipo usa um wireframe neutro. Quem aprova, e como (reunião, link com comentários, teste com usuários)? Existe um limite de tempo?
4. **Lacunas bloqueantes.** Uma por vez, com a sua sugestão de resposta.

Quando a pessoa disser "pode seguir", pare de perguntar: marque o que sobrou como `[SUPOSIÇÃO]` e termine o plano.

### 5. Escrever o plano

Copie [`referencias/prototype-plan.md`](referencias/prototype-plan.md) para `explore/<slug>/prototype-plan.md` e preencha. O plano cabe em uma página, duas no máximo. As seções das etapas seguintes (Referências, Conceitos, Resultado) ficam com o marcador `(etapa N)`; as outras skills as preenchem.

### 6. Conferir o gate e pedir aprovação

Mostre o checklist do Gate 1 com ✓ ou ✗ em cada item, as suposições e as perguntas para produto. Se tudo passar, pergunte se pode marcar como `final`. Só com o sim da pessoa:

- mude o frontmatter para `status: final` e atualize `updated`;
- atualize o quadro de status do `README.md` da exploração;
- diga o próximo passo: etapa 2 (referências visuais, opcional) ou etapa 3 (conceitos).

## Regras

- Não invente requisito, jornada ou métrica. O que não está no PRD e não foi dito pela pessoa é `[SUPOSIÇÃO]` ou pergunta.
- O intake descreve o que o protótipo precisa mostrar, nunca como as telas são.
- Um protótipo, uma pergunta. Se aparecerem duas perguntas grandes, sugira duas explorações.
- O PRD não é editado sem pedido explícito.
- Use os nomes do glossário do PRD exatamente como estão escritos.

## Checklist (Gate 1)

- [ ] A pergunta do protótipo está escrita em uma frase
- [ ] O critério de desistência está escrito
- [ ] De 1 a 3 jornadas em escopo, com IDs, e os requisitos que elas usam
- [ ] O que fica fora do protótipo está listado
- [ ] Formato definido e design system apontado (ou "nenhum")
- [ ] Nenhuma lacuna bloqueante em aberto
- [ ] Quem aprova, e como, está definido
- [ ] A pessoa aprovou e o plano está `status: final`

## Exemplo

[`../examples/prd-clube-do-livro.md`](../examples/prd-clube-do-livro.md) é um PRD no formato prd-light do BMAD, com lacunas de propósito. Para testar: *"lê o PRD em examples/prd-clube-do-livro.md e planeja o protótipo"*.
