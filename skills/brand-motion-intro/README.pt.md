# brand-motion-intro: como usar

*[Read in English](README.md)*

Uma skill do Claude Code que transforma uma frase, o seu design system e uma música num vídeo de motion de 10 a 20 segundos (MP4), com cada transição na batida. Esta página é para **quem vai usar a skill**. O [`SKILL.md`](SKILL.md) é o que o Claude lê.

## 1. Requisitos

| Você precisa de | Como conferir |
|---|---|
| [Claude Code](https://claude.com/claude-code) (terminal, app de desktop ou extensão de IDE) | `claude --version` |
| Node.js 20 ou mais novo | `node -v` |
| Python 3.9 ou mais novo (sem pacotes extras) | `python3 --version` |
| Google Chrome (usado em segundo plano para gravar os quadros) | Caminho padrão do macOS, ou defina `CHROME=/caminho/do/chrome` |
| ffmpeg | Instalado no passo 2, ou o seu próprio no `PATH` |

## 2. Instalar

**a. Deixe a skill disponível para o Claude Code.** Copie (ou crie um link para) a pasta da skill na sua pasta pessoal de skills:

```bash
mkdir -p ~/.claude/skills
```

```bash
cp -R skills/brand-motion-intro ~/.claude/skills/
```

Para usar só em um projeto, copie para `<projeto>/.claude/skills/`. Para ficar sempre igual à versão deste repositório, use um link simbólico: `ln -s "$PWD/skills/brand-motion-intro" ~/.claude/skills/brand-motion-intro`.

**b. Instale as dependências dos scripts de render** (puppeteer-core e ffmpeg-static):

```bash
cd ~/.claude/skills/brand-motion-intro/scripts && npm install
```

Se o npm bloquear os scripts de instalação e o arquivo `node_modules/ffmpeg-static/ffmpeg` não existir, baixe o binário uma vez:

```bash
cd ~/.claude/skills/brand-motion-intro/scripts/node_modules/ffmpeg-static && node install.js
```

**c. Reinicie o Claude Code** (ou abra uma sessão nova) para ele reconhecer a skill.

## 3. Prepare o material

1. **Sua mensagem numa frase com vírgulas.** Cada vírgula vira uma transição. Exemplo: `Hi, I'm IY., Isabela Yukari, Design Engineer`.
2. **Uma referência** do estilo de motion que você gosta (link, prints ou descrição).
3. **Sua marca**: um repositório com seu site ou design system, um arquivo do Figma, ou pelo menos as cores em hex, as fontes e o logo.
4. **Formato e duração**: 16:9 (feed, YouTube, portfólio) ou 9:16 (Stories e Reels), de 12 a 20 segundos.
5. **Um arquivo de música com licença** (MP3 ou WAV), salvo no seu computador.

## 4. Use

Abra o Claude Code em qualquer pasta (de preferência no repositório do seu design system) e peça com suas palavras. A skill é ativada por pedidos como "faz um vídeo de motion como esta referência". Você também pode chamá-la pelo nome: `/brand-motion-intro`.

Exemplo de pedido:

> Faz um vídeo de motion de 20s, 16:9, no estilo desta referência: <link>. Texto: "Hi, I'm IY., Isabela Yukari, Design Engineer". Cada vírgula é uma transição. Use o design system de ~/Portfolio. Clima: futurista com glassmorfismo, mas doce. Música: ~/Downloads/musica.mp3.

O que acontece depois:

1. **Briefing**: o Claude pergunta só o que falta (formato, clima, música, claro ou escuro).
2. **Estratégia**: ele propõe o arco narrativo e um objeto-herói que fecha o ciclo no seu logo. Você aprova ou redireciona.
3. **Quadros**: você recebe uma prancha com 9 a 12 quadros-chave. É o momento mais barato para mudar a direção.
4. **Ajustes**: peça em texto, por exemplo "paleta mais clara", "palavras mais devagar", "no final a bola vira o ponto do logo".
5. **Música**: o Claude encontra o andamento, a entrada da batida e os trechos com voz, emenda a faixa na batida e prende cada transição num golpe.
6. **Render**: MP4 a 60 quadros por segundo. Grava cerca de 3 quadros por segundo, então um vídeo de 20s leva uns 7 minutos. Depois vem a varredura automática de quadros com defeito.
7. **Entrega**: o MP4 numa pasta que você escolher (por exemplo `~/Movies`), com o que foi e o que não foi conferido.

Pedidos úteis depois: "faz também a versão para Stories (9:16)", "renderiza em 4K" (`SCALE=2`), "exporta uma versão só com efeitos sonoros para eu colocar a música no Instagram".

## 5. Rodar os scripts você mesmo (opcional)

Dentro de `scripts/`:

```bash
node render.cjs ../templates/scene.html stills 1 2 3 4
```

```bash
python3 analyze_beats.py ~/Downloads/musica.mp3 --from 50 --to 100
```

```bash
python3 splice_audio.py ~/Downloads/musica.mp3 audio.wav 64.28:79.78 133.80:end --dur 20
```

```bash
WARP=1 DUR=20 node render.cjs ../templates/scene.html video silent.mp4
```

```bash
python3 scan_flicker.py silent.mp4
```

Depois, junte vídeo e áudio: `ffmpeg -i silent.mp4 -i audio.wav -map 0:v -map 1:a -c:v copy -c:a aac -shortest final.mp4`.

## 6. Dicas e problemas comuns

| Situação | O que fazer |
|---|---|
| A referência é um post do Instagram | Mande prints ou descreva. O Claude geralmente não consegue assistir sem login. |
| Você não consegue baixar a música | Peça uma versão só com efeitos sonoros e adicione a música pela biblioteca do Instagram. |
| O vídeo parece rápido demais | Peça pelo menos 1,5s por frase. A curva de tempo estica as cenas sem refazer a animação. |
| Uma piscada de um quadro no vídeo | Peça para o Claude rodar o `scan_flicker.py` e corrigir os quadros marcados antes da entrega. |
| Voz cantada por cima do texto | Peça um trecho instrumental e ouça para confirmar. |
| `Chrome not found` | Defina `CHROME` com o caminho do seu Chrome. |
| `ffmpeg: not found` | Rode o passo 2b, ou instale o ffmpeg e confira se ele está no `PATH`. |

**Direitos da música:** para publicar, a licença precisa cobrir a plataforma. A skill nunca baixa músicas de bancos por você.
