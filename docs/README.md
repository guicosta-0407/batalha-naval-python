# Batalha Naval — GPTech Games

Trabalho individual da disciplina de Programação em Python (Engenharia de
Computação, CEFET-MG — Campus Divinópolis, Prof. Guido Pantuza).

Autor: Guilherme Marra

## Requisitos

- Python 3.10 ou superior
- Nenhuma biblioteca externa é necessária (apenas biblioteca padrão:
  `random`, `time`, `json`, `os`, `pathlib`)

## Como executar

```bash
python3 menu.py
```

O menu principal é o ponto de entrada do sistema. Rodar `python3 main.py`
também funciona (ele chama o menu internamente).

## Como jogar

- As coordenadas seguem o formato **letra + numero** (ex.: `C5`), com
  colunas de `A` a `J` e linhas de `1` a `10`.
- Legenda do tabuleiro: `~` agua nao jogada, `N` navio (so visivel no seu
  proprio tabuleiro), `X` acerto, `O` agua ja jogada, `#` navio afundado
  (visivel mesmo no tabuleiro do adversario, ja que nao ha mais segredo).
- No inicio de cada partida, cada jogador ve sua frota sorteada e pode:
  - `[1]` Confirmar a frota;
  - `[2]` Sortear tudo novamente;
  - `[3]` Mover um navio especifico para outra posicao (funcionalidade
    extra alem do RF10).
- **Acertar um tiro (ou afundar um navio) da direito a jogar novamente.**
  Um tiro n'agua passa a vez para o adversario.
- No modo **Dois Jogadores**, a tela e limpa entre os turnos e o programa
  pede confirmacao antes de mostrar o tabuleiro de cada um, para o outro
  jogador nao ver a frota alheia.
- No modo **Jogador x Computador**, o tabuleiro do computador nao e
  mostrado (para nao revelar a posicao dos navios dele antes da hora);
  a tela indica apenas de quem e a vez e o resultado de cada tiro.

## Estrutura do projeto

```
BatalhaNaval/
|-- main.py           # laco de uma partida (turnos, fim de jogo)
|-- menu.py           # menus, telas e conferencia de posicionamento
|-- tabuleiro.py      # matriz 10x10, tiros, posicionamento
|-- navios.py         # classe Navio
|-- jogador.py        # jogador humano
|-- computador.py     # jogador controlado pelo computador (IA)
|-- estatisticas.py   # calculo e persistencia de estatisticas
|-- replay.py         # gravacao e reproducao da ultima partida
|-- utils.py          # constantes e funcoes auxiliares
|-- data/             # estatisticas.json e ultima_partida.json (gerados
|                        em tempo de execucao; nao versionados)
|-- docs/             # video de demonstracao e diario de desenvolvimento
`-- README.md
```

## Requisitos funcionais e regras de negocio implementados

| ID | Descricao | Onde |
|----|-----------|------|
| RF01 | Menu principal | `menu.exibir_menu_principal` |
| RF02 | Tabuleiro 10x10 | `Tabuleiro.__init__` |
| RF03 | Navios pequeno/grande | `navios.py`, `TAMANHO_NAVIO` |
| RF04 | Posicionamento automatico sem sobreposicao | `Tabuleiro.posicionar_navio_aleatorio` / `posicionar_frota` |
| RF05 | Validacao de jogadas | `utils.converter_coordenada`, `Jogador.escolher_jogada` |
| RF06 | Mensagens de agua/acerto/afundado | `main.jogar_partida` |
| RF07 | Fim de jogo (vencedor, jogadas, tempo) | `main.jogar_partida` |
| RF08 | Nova partida a qualquer momento pelo menu | `menu.iniciar` |
| RF09 | Dois modos de jogo | `Jogador` / `Computador` |
| RF10 | Posicionamento e conferencia dos navios | `menu.confirmar_posicionamento` |
| RF11 | Historico de jogadas | lista `historico` em `main.jogar_partida` |
| RF12 | Estatisticas de desempenho | `estatisticas.py` |
| RF13 | Modo replay | `replay.py` |
| RN01 | Formato letra + numero | `utils.converter_coordenada` |
| RN02 | Jogada repetida rejeitada, sem consumir rodada | `Tabuleiro.ja_jogada` |
| RN03 | Navio afundado quando todas as casas atingidas | `Navio.esta_afundado` |
| RN04 | Fim de jogo quando toda a frota adversaria afunda | `Tabuleiro.todos_afundados` |
| RN05 | Computador joga de forma autonoma | `computador.py` |

## Decisoes de projeto

Como o enunciado deixa alguns pontos em aberto, as decisoes tomadas foram:

- **Frota padrao:** 2 navios grandes (4 casas) + 3 navios pequenos
  (2 casas) = 14 casas por jogador. Configuravel em `TAMANHO_FROTA`,
  no `utils.py`.
- **Turno extra:** acertar um tiro (inclusive afundar um navio) mantem a
  vez do mesmo jogador; so errar (agua) passa a vez.
- **Visibilidade do tabuleiro:** o jogador ve seu proprio tabuleiro (com
  navios) e o do adversario sem navios, lado a lado. No modo contra o
  computador, o tabuleiro do computador nunca e mostrado, para preservar
  a imersao — apenas as mensagens de resultado aparecem.
- **Navio afundado:** passa a ser exibido com o simbolo `#` mesmo no
  tabuleiro "escondido" do adversario, ja que a partir do afundamento
  aquela informacao deixa de ser segredo.
- **RF10 (conferencia):** alem de confirmar ou sortear tudo de novo, o
  jogador pode mover um navio especifico para outra posicao, mantendo o
  tamanho e a orientacao originais (funcionalidade extra).
- **Nomes dos jogadores:** pedidos por `input()` no inicio de cada
  partida. Se o campo for deixado em branco, usa-se um nome padrao
  ("Jogador 1", "Jogador 2").
- **Estatisticas (RF12):** guardadas por nome de jogador em
  `data/estatisticas.json`, permitindo varios jogadores no mesmo
  computador. So o vencedor de cada partida tem suas estatisticas
  atualizadas (partidas, vitorias, tiros, acertos, aproveitamento).
- **Persistencia:** os arquivos `data/estatisticas.json` e
  `data/ultima_partida.json` sao gerados/atualizados automaticamente
  durante a execucao e nao sao versionados no repositorio (ver
  `.gitignore`). Se o arquivo nao existir ou estiver corrompido, o
  programa usa valores padrao em vez de travar (RNF05).

## Funcionalidades extras (bonus)

- **IA caca-e-alvo do computador:** apos um acerto, o computador guarda
  as posicoes vizinhas (cima, baixo, esquerda, direita) numa fila e
  testa-as antes de voltar a sortear aleatoriamente, de forma
  semelhante a uma estrategia real de Batalha Naval.
- **Reposicionamento manual de navios** na tela de conferencia (RF10),
  alem do sorteio automatico exigido pelo RF04.

## README
- Feito por IA.