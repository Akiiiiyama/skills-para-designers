# Explorar (orquestradora)

[Read in English](../en/skill.md)

A etapa Explorar transforma um PRD num protótipo de baixa fidelidade que alguém aprova, ajusta ou descarta. Ela é feita por várias skills pequenas, cada uma com um único trabalho. Esta skill não faz nenhum desses trabalhos: ela **monta a pasta, sabe a ordem, confere os gates e chama a próxima skill**.

Um gate é a condição para avançar. Cada etapa grava um artefato com `status: draft` ou `status: final` no frontmatter e um checklist de pronto. A próxima etapa só começa quando o artefato da anterior está `final` e o checklist passa. Quem marca `final` é sempre a pessoa, nunca o Claude sozinho.

## Quando usar

- Uma feature tem PRD (ou um rascunho de PRD) e a pessoa quer chegar rápido numa ideia visível para aprovar.
- A pessoa abre uma pasta de exploração e pergunta em que pé está ou qual é o próximo passo.
- Não serve para implementar a feature de verdade (isso é a etapa Prototipar) nem para refinar um design já aprovado (Refinar).

## As etapas

| # | Skill | Produz | Obrigatória? |
|---|---|---|---|
| 1 | `explore-intake` | `prototype-plan.md` | Sim |
| 2 | `explore-refs` | `refs/` + `patterns.md` | Não: pode pular, com o motivo registrado |
| 3 | `explore-concepts` | `concepts.md` | Sim |
| 4 | `explore-lofi` | `prototype/index.html` | Sim |
| 5 | `explore-review` | `review.html` + seção Resultado no plano | Sim |

Os gates de cada etapa estão em [`referencias/gates.md`](referencias/gates.md). Leia esse arquivo sempre que for conferir um gate.

## Passos

### 1. Encontrar ou criar a exploração

- Se a pessoa está numa pasta `explore/<slug>/`, ou cita uma, use essa.
- Se não, procure `explore/*/README.md` no projeto. Se houver uma exploração com etapas em aberto, pergunte se é para continuar nela.
- Se for nova: pergunte o nome curto da feature (vira o `<slug>` em kebab-case) e onde está o PRD. Crie `explore/<slug>/` na raiz do projeto, a não ser que a pessoa indique outro lugar, e escreva o `README.md` da exploração com o quadro de status (modelo em [`referencias/gates.md`](referencias/gates.md#quadro-de-status)).

O PRD fica onde está. A exploração guarda só o caminho dele.

### 2. Ler o estado

Para cada etapa, leia o frontmatter do artefato (`status`, `updated`) e classifique:

- **não iniciada**: o arquivo não existe;
- **em andamento**: existe com `status: draft`;
- **concluída**: `status: final` e o checklist do gate passa;
- **pulada**: só a etapa 2, com `skipped: true` e um motivo no README.

Se um artefato diz `final` mas o checklist não passa (alguém editou à mão, por exemplo), trate como **em andamento** e diga qual item falhou.

Atualize o quadro de status do `README.md` da exploração com o que encontrou.

### 3. Dizer onde está e qual é o próximo passo

Responda em poucas linhas: a etapa atual, o que falta para o gate dela passar e qual skill vem depois. Exemplo:

> Etapa 1 (intake) em andamento. Falta o critério de desistência e a definição de quem aprova. Depois disso vem a etapa 2 (referências visuais), que dá para pular se você já tem referências.

### 4. Chamar a próxima skill

- Se o gate da etapa atual passou, chame a skill da próxima etapa e passe para ela o caminho da exploração.
- Se a skill da etapa não está instalada, diga isso e ofereça fazer a etapa à mão, seguindo o que o gate pede. O artefato precisa sair com o mesmo nome e o mesmo frontmatter, para o gate continuar funcionando.
- Se a pessoa pedir para pular uma etapa obrigatória, explique o que se perde (por exemplo: sem `concepts.md`, o protótipo não tem alternativa para comparar) e só siga se ela confirmar. Registre a decisão no README da exploração.

### 5. Voltar uma etapa

Se uma etapa mais à frente mostra que uma anterior estava errada (o protótipo revela que a jornada escolhida não responde à pergunta, por exemplo), volte o artefato anterior para `status: draft`, registre o motivo no README e refaça dali. Os artefatos depois dele também voltam para `draft`.

## Regras

- Uma etapa por vez. Nunca rode duas skills de etapa no mesmo passo.
- Só a pessoa marca `final`. O Claude mostra o checklist e pergunta.
- O quadro de status no README é um resumo; a verdade está no frontmatter de cada artefato.
- Toda decisão de pular, voltar ou forçar uma etapa vai para a seção Decisões do README, com data e motivo.
- Os nomes dos arquivos e as chaves do frontmatter são os mesmos em português e em inglês, para que explorações dos dois idiomas funcionem com as mesmas skills.

## Checklist

- [ ] A exploração tem pasta, `README.md` e o caminho do PRD
- [ ] O quadro de status bate com o frontmatter dos artefatos
- [ ] A pessoa sabe a etapa atual, o que falta e qual é a próxima
- [ ] Nenhuma etapa começou com o gate da anterior aberto (ou a exceção está registrada)
