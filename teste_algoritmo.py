#!/usr/bin/env python3
"""
Teste para validar o algoritmo knapsack implementado no jogo
"""

def knapsack_otimo(itens, capacidade):
    """Resolve o problema da mochila usando programação dinâmica"""
    n = len(itens)
    W = capacidade
    
    # Criar tabela DP
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    # Preencher tabela DP
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            peso_item = itens[i-1]["peso"]
            valor_item = itens[i-1]["valor"]
            
            if peso_item <= w:
                dp[i][w] = max(valor_item + dp[i-1][w-peso_item], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    # Recuperar itens da solução ótima
    valor_otimo = dp[n][W]
    itens_otimos = []
    
    w = W
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            itens_otimos.append(i-1)
            w -= itens[i-1]["peso"]
    
    return valor_otimo, itens_otimos

def testar_algoritmo():
    """Executa testes do algoritmo knapsack"""
    print("=== TESTE DO ALGORITMO KNAPSACK ===\n")
    
    # Itens do jogo
    itens = [
        {"nome": "Comida Enlatada", "peso": 3, "valor": 8},
        {"nome": "Água Potável", "peso": 2, "valor": 10},
        {"nome": "Ferramenta Multiuso", "peso": 1, "valor": 6},
        {"nome": "Kit Primeiros Socorros", "peso": 2, "valor": 9},
        {"nome": "Tesouro Antigo", "peso": 5, "valor": 15},
        {"nome": "Mapa da Ilha", "peso": 1, "valor": 7},
        {"nome": "Lanterna", "peso": 1, "valor": 5},
        {"nome": "Corda Resistente", "peso": 2, "valor": 6},
        {"nome": "Bússola", "peso": 1, "valor": 8},
        {"nome": "Cristal Mágico", "peso": 4, "valor": 12}
    ]
    
    capacidade = 15
    
    # Executar algoritmo
    valor_otimo, itens_otimos = knapsack_otimo(itens, capacidade)
    
    print(f"Capacidade da mochila: {capacidade}kg")
    print(f"Total de itens disponíveis: {len(itens)}")
    print(f"\nSOLUÇÃO ÓTIMA:")
    print(f"Valor máximo: {valor_otimo}")
    print(f"Itens selecionados: {len(itens_otimos)}")
    
    peso_total = 0
    print("\nItens na solução ótima:")
    for i in itens_otimos:
        item = itens[i]
        peso_total += item["peso"]
        relacao_vp = item["valor"] / item["peso"]
        print(f"  - {item['nome']}: {item['peso']}kg, valor {item['valor']} (V/P: {relacao_vp:.1f})")
    
    print(f"\nPeso total usado: {peso_total}kg / {capacidade}kg")
    print(f"Capacidade restante: {capacidade - peso_total}kg")
    
    # Verificar se a solução é válida
    if peso_total <= capacidade:
        print("\n✅ Solução válida! Peso dentro da capacidade.")
    else:
        print("\n❌ Erro: Solução inválida! Peso excede a capacidade.")
    
    # Mostrar análise dos itens
    print("\n=== ANÁLISE DOS ITENS ===")
    print("Itens ordenados por relação valor/peso:")
    
    # Ordenar itens por relação valor/peso
    itens_ordenados = [(i, item, item["valor"]/item["peso"]) 
                       for i, item in enumerate(itens)]
    itens_ordenados.sort(key=lambda x: x[2], reverse=True)
    
    for i, (indice, item, relacao) in enumerate(itens_ordenados):
        status = "✓ SELECIONADO" if indice in itens_otimos else "✗ Não selecionado"
        print(f"{i+1:2d}. {item['nome']:20s} (V/P: {relacao:4.1f}) - {status}")

if __name__ == "__main__":
    testar_algoritmo() 