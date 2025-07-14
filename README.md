# Aventura do Mochileiro: O Desafio dos Recursos Limitados

Um jogo educativo em Python que simula o problema da mochila 0/1 (0-1 Knapsack Problem) de forma interativa e divertida.

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 22/2021933  |  William Bernardo da Silva |
| 22/2015195  |  Mateus de Castro Santos |

## Requisitos

- Python 3.8+
- pygame 2.5.2+

## Instalação

1. Clone o repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Como Executar

```bash
python jogo_mochila.py
```

## Como Usar

### Objetivo
Você é um aventureiro se preparando para uma expedição. Escolha sabiamente os itens para sua mochila (capacidade máxima: 15kg) para maximizar o valor total dos itens carregados.

### Controles

**Tela do Menu:**
- ESPAÇO: Começar o jogo
- ESC: Sair do jogo

**Tela do Jogo:**
- Teclas 1-9 e 0: Selecionar/desselecionar itens
- ENTER: Confirmar seleção e ver resultado
- ESC: Sair do jogo

**Tela de Resultado:**
- R: Jogar novamente
- ESC: Sair do jogo

### Funcionalidades

- **Lista de Itens**: 10 itens disponíveis com diferentes pesos e valores
- **Seleção Interativa**: Interface visual para selecionar itens
- **Validação de Peso**: Não permite exceder a capacidade da mochila
- **Algoritmo Knapsack**: Calcula automaticamente a solução ótima usando programação dinâmica
- **Sistema de Pontuação**: Compara sua escolha com a solução ótima
- **Feedback Visual**: Barras de progresso e indicadores coloridos

## Observações

- O jogo implementa o algoritmo de programação dinâmica para resolver o problema da mochila 0/1
- A eficiência do jogador é calculada como: (valor_jogador / valor_otimo) * 100%
- O jogo oferece feedback educativo baseado na performance do jogador

## Screenshots

*Screenshots serão adicionados em breve*

## Outros

Este projeto foi desenvolvido como parte da disciplina de Programação Avançada, focando na implementação prática do algoritmo de programação dinâmica para o problema da mochila 0/1.

[Video Apresentação](link)
