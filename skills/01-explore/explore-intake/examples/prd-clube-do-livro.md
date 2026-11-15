---
title: "Votação do próximo livro"
template: prd-light
version: 1.1.0
status: draft
created: "2026-11-14"
updated: "2026-11-14"
---

<!-- PRD de exemplo para testar a skill explore-intake. Segue o formato prd-light do BMAD Method
     e tem lacunas de propósito: uma jornada sem protagonista nem clímax, um passo sem requisito,
     um requisito sem jornada, um termo ambíguo, formato não definido e uma pergunta aberta
     que muda a tela de resultado. -->

# Votação do próximo livro

## Vision

Clubes do livro pequenos (de 5 a 15 pessoas) escolhem o próximo livro numa conversa longa de grupo, que se perde entre outras mensagens e quase sempre termina com a organizadora decidindo sozinha. A Votação do próximo livro deixa a organizadora propor alguns títulos e os membros votarem em poucos toques, com um resultado que todo mundo vê e aceita.

## Users and journeys

**UJ-1. Ana abre a rodada do mês.** Ana organiza um clube de 12 pessoas e cuida de tudo sozinha, quase sempre pelo celular, no intervalo do trabalho. Ela escolhe 3 livros que estão na lista de sugestões, define até quando dá para votar e abre a rodada. Depois, compartilha o link no grupo do WhatsApp do clube. No dia seguinte, ela vê quantas pessoas já votaram e manda um lembrete para quem falta.

**UJ-2. O membro vota.** O usuário recebe o link, vê os livros propostos e vota no que prefere. Depois, pode mudar o voto até a votação fechar.

**UJ-3. Todos veem o resultado.** Quando o prazo acaba, a votação fecha e o livro vencedor aparece para todos, com o número de votos de cada título.

## Features and requirements

**Rodada de votação**

- FR-1: A organizadora pode criar uma rodada com 2 a 5 livros da lista de sugestões.
- FR-2: A organizadora pode definir a data e a hora em que a votação fecha.
- FR-3: A organizadora pode ver quantos membros já votaram e quem ainda não votou.
- FR-4: A organizadora pode enviar um lembrete para quem ainda não votou.

**Voto**

- FR-5: Um membro pode votar em um livro da rodada e mudar o voto até o fechamento.
- FR-6: Um membro pode comentar a sinopse de um livro proposto.

**Resultado**

- FR-7: Quando a votação fecha, todos os membros veem o livro vencedor e a contagem de votos.

**Lista de sugestões**

- FR-8: Qualquer membro pode sugerir um livro para a lista, com título, autor e capa.

## Non-goals

- Não é uma rede social de leitura: não há perfis públicos nem resenhas.
- Não controla o progresso de leitura dos membros.

## Technical approach

Web app simples, com login por link mágico enviado por e-mail. Os dados dos livros (capa, sinopse) vêm de uma API pública de livros. Hospedagem e banco ficam a critério de quem construir.

## Success

A organizadora não precisa mais decidir sozinha: na maioria das rodadas, pelo menos metade do clube vota antes do prazo.

## Open questions

- OQ-1: O que acontece em caso de empate? (responde: Ana, como organizadora)
- OQ-2: Membros novos que entram no meio da rodada podem votar? (responde: produto)
