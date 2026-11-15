# Explorar (orquestradora)

Conduz a etapa Explorar de uma feature, do PRD até um protótipo de baixa fidelidade aprovado. A etapa é feita por várias skills pequenas, e esta é a que sabe a ordem: ela monta a pasta da exploração, confere o gate de cada etapa e chama a próxima.

[Read in English](../en/README.md)

## As etapas

1. **`explore-intake`**: lê o PRD, aponta as lacunas e escreve o plano do protótipo.
2. **`explore-refs`** *(planejada)*: referências visuais e os padrões que elas mostram. Opcional.
3. **`explore-concepts`** *(planejada)*: 2 ou 3 conceitos diferentes, ligados às jornadas do PRD.
4. **`explore-lofi`** *(planejada)*: protótipo HTML de baixa fidelidade com o design system no tema wireframe.
5. **`explore-review`** *(planejada)*: comparação dos conceitos e registro da decisão.

Enquanto uma skill está planejada, a orquestradora oferece fazer a etapa à mão, com o mesmo artefato e o mesmo gate.

## Instalar

```bash
git clone https://github.com/Akiiiiyama/skills-para-designers.git
cp -R skills-para-designers/skills/01-explore/explore ~/.claude/skills/
cp -R skills-para-designers/skills/01-explore/explore-intake ~/.claude/skills/
```

Reinicie o Claude Code.

## Usar

Peça ao Claude: *"vamos explorar a feature de votação, o PRD está em docs/prd-votacao.md"*. Depois, a qualquer momento: *"em que pé está a exploração?"* ou *"qual o próximo passo?"*.

Tudo fica em `explore/<feature>/`, com um `README.md` que mostra o status de cada etapa e as decisões tomadas no caminho. Os gates estão em [`referencias/gates.md`](referencias/gates.md).
