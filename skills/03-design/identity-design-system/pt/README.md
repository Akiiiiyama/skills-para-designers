# Design system a partir da sua identidade

Crie o seu próprio design system a partir da identidade que **você** quer: uma entrevista sobre seus valores, personalidade e referências, duas ou três direções, um nome com significado, uma página de proposta visual para aprovar e, depois, tokens funcionando (CSS light/dark + testes de contraste) a partir de um kit inicial.

[Read in English](../en/README.md)

## Instalar

```bash
git clone https://github.com/Akiiiiyama/skills-para-designers.git
cp -R skills-para-designers/skills/03-design/identity-design-system ~/.claude/skills/
```

Reinicie o Claude Code.

## Usar

Peça ao Claude: *"quero criar meu próprio design system"* ou *"me ajuda a transformar minha identidade visual em tokens"*. O Claude vai:

1. Entrevistar você em rodadas curtas (propósito, valores, escalas de personalidade, referências, restrições) e escrever um brief de identidade para você aprovar.
2. Propor 2 ou 3 direções com paleta, tipografia, forma, movimento e um detalhe assinatura, com o contraste de cada cor.
3. Sugerir nomes e transformar a metáfora no nome das camadas (valores brutos → tema → componentes → páginas).
4. Montar uma página de proposta na sua direção e ajustar até você aprovar.
5. Preencher o [`templates/starter`](../templates/starter) com os seus tokens: `npm run build && npm test`.
6. Crescer para componentes, página de documentação e Figma, um passo aprovado de cada vez.

A identidade é sempre sua: cada escolha cita algo que você disse.

Exemplo real: [IY Lotus](https://github.com/Akiiiiyama/iylotus) e a skill [`lotus-design-system`](../../../02-discover/lotus-design-system/pt/skill.md).
