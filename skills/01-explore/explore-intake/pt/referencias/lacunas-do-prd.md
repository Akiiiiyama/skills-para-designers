# Lacunas do PRD que afetam o protótipo

Percorra a lista com o PRD aberto. Para cada item que falhar, anote o ID envolvido e classifique: **bloqueante**, **vira suposição** ou **para produto**. A coluna "Normalmente" sugere a classificação mais comum; o contexto pode mudar isso.

## Jornadas

| Verificação | O que procurar | Normalmente |
|---|---|---|
| Jornada sem protagonista | "O usuário" em vez de uma pessoa com nome e contexto ("Ana, que organiza o clube e só tem o celular no ônibus"). Sem contexto, não dá para decidir formato nem densidade. | vira suposição |
| Jornada sem clímax | Não está claro em que momento o valor chega para a pessoa. É exatamente esse momento que o protótipo precisa mostrar. | bloqueante |
| Passo sem requisito | Um passo da jornada precisa do produto, mas nenhum `FR` o cobre. | vira suposição |
| Requisito sem jornada | Um `FR` que nenhuma jornada usa. Fica fora do protótipo, a não ser que a pessoa diga o contrário. | para produto |
| Estado de entrada indefinido | Não se sabe se a pessoa já está logada, se é a primeira vez ou se já tem dados. Muda a primeira tela. | vira suposição |

## Estados e conteúdo

| Verificação | O que procurar | Normalmente |
|---|---|---|
| Estado vazio | O que aparece quando ainda não há nada (primeira vez, lista vazia)? | vira suposição |
| Erro e falha | O PRD descreve pelo menos uma falha da jornada principal? | vira suposição |
| Forma do conteúdo | Quantos itens, tamanho dos textos, que dados aparecem? Sem isso, o protótipo cai no lorem ipsum. | vira suposição |
| Termos ambíguos | Uma palavra usada com dois sentidos, ou que não está no glossário ("rodada", "sessão", "grupo"). | bloqueante se for o centro da jornada |

## Escopo e decisão

| Verificação | O que procurar | Normalmente |
|---|---|---|
| Não-objetivos | Existe uma lista do que a feature não é? Sem ela, o protótipo tende a crescer. | para produto |
| Formato | Mobile, web, desktop ou vários? | bloqueante |
| Métrica de sucesso | Existe um `SM` ou outra forma de saber se funcionou? Ajuda a escrever o critério de desistência. | para produto |
| Perguntas abertas | Algum `OQ` muda o que o protótipo mostra? Esse vira bloqueante. | depende |
| Decisões já tomadas | Algo que o PRD já decidiu e que o protótipo não deve reabrir. Anote para não gastar conceitos com isso. | (não é lacuna) |

## Só a pessoa responde

Estes itens nunca estão no PRD. Pergunte sempre:

- a pergunta que o protótipo precisa responder;
- o critério de desistência;
- quem aprova, e como;
- o limite de tempo.
