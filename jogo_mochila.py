import pygame
import sys
from typing import List, Dict, Tuple

# Inicializar pygame
pygame.init()

# Constantes
LARGURA = 1200
ALTURA = 800
FPS = 60

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (70, 130, 180)
VERDE = (34, 139, 34)
VERMELHO = (220, 20, 60)
AMARELO = (255, 215, 0)
CINZA = (128, 128, 128)
CINZA_CLARO = (211, 211, 211)

class JogoMochila:
    def __init__(self):
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("Aventura do Mochileiro: O Desafio dos Recursos Limitados")
        self.clock = pygame.time.Clock()
        self.font_titulo = pygame.font.Font(None, 48)
        self.font_normal = pygame.font.Font(None, 24)
        self.font_pequena = pygame.font.Font(None, 18)
        
        # Estado do jogo
        self.executando = True
        self.tela_atual = "menu"  # menu, jogo, resultado
        
        # Capacidade da mochila
        self.capacidade_mochila = 15
        
        # Itens disponíveis (nome, peso, valor)
        self.itens = [
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
        
        # Itens selecionados pelo jogador
        self.itens_selecionados = []
        
        # Resultados
        self.valor_jogador = 0
        self.peso_jogador = 0
        self.valor_otimo = 0
        self.itens_otimos = []
        
    def executar(self):
        while self.executando:
            self.processar_eventos()
            self.atualizar()
            self.desenhar()
            self.clock.tick(FPS)
            
        pygame.quit()
        sys.exit()
    
    def processar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.executando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.executando = False
                elif evento.key == pygame.K_SPACE:
                    if self.tela_atual == "menu":
                        self.tela_atual = "jogo"
                        self.itens_selecionados = []
                elif evento.key == pygame.K_RETURN:
                    if self.tela_atual == "jogo":
                        self.calcular_resultado()
                        self.tela_atual = "resultado"
                elif evento.key == pygame.K_r:
                    if self.tela_atual == "resultado":
                        self.tela_atual = "menu"
                        self.itens_selecionados = []
                # Teclas numéricas para selecionar itens
                elif self.tela_atual == "jogo" and evento.key >= pygame.K_1 and evento.key <= pygame.K_9:
                    indice = evento.key - pygame.K_1
                    if indice < len(self.itens):
                        self.alternar_item(indice)
                elif self.tela_atual == "jogo" and evento.key == pygame.K_0:
                    if len(self.itens) > 9:
                        self.alternar_item(9)
    
    def atualizar(self):
        pass
    
    def desenhar(self):
        self.tela.fill(BRANCO)
        
        if self.tela_atual == "menu":
            self.desenhar_menu()
        elif self.tela_atual == "jogo":
            self.desenhar_jogo()
        elif self.tela_atual == "resultado":
            self.desenhar_resultado()
            
        pygame.display.flip()
    
    def desenhar_menu(self):
        # Título
        titulo = self.font_titulo.render("Aventura do Mochileiro", True, AZUL)
        subtitulo = self.font_normal.render("O Desafio dos Recursos Limitados", True, AZUL)
        
        titulo_rect = titulo.get_rect(center=(LARGURA//2, 150))
        subtitulo_rect = subtitulo.get_rect(center=(LARGURA//2, 200))
        
        self.tela.blit(titulo, titulo_rect)
        self.tela.blit(subtitulo, subtitulo_rect)
        
        # Instruções
        instrucoes = [
            "Você é um aventureiro se preparando para uma expedição.",
            "Escolha sabiamente os itens para sua mochila!",
            "Capacidade máxima: 15kg",
            "",
            "Pressione ESPAÇO para começar",
            "Pressione ESC para sair"
        ]
        
        y_pos = 300
        for instrucao in instrucoes:
            texto = self.font_normal.render(instrucao, True, PRETO)
            texto_rect = texto.get_rect(center=(LARGURA//2, y_pos))
            self.tela.blit(texto, texto_rect)
            y_pos += 40
    
    def desenhar_jogo(self):
        # Título
        titulo = self.font_titulo.render("Escolha seus itens para a aventura!", True, AZUL)
        titulo_rect = titulo.get_rect(center=(LARGURA//2, 50))
        self.tela.blit(titulo, titulo_rect)
        
        # Informações da mochila
        peso_atual = sum(self.itens[i]["peso"] for i in self.itens_selecionados)
        info_mochila = f"Capacidade da mochila: {peso_atual}kg / {self.capacidade_mochila}kg"
        
        cor_peso = VERMELHO if peso_atual > self.capacidade_mochila else VERDE
        texto_mochila = self.font_normal.render(info_mochila, True, cor_peso)
        texto_mochila_rect = texto_mochila.get_rect(center=(LARGURA//2, 100))
        self.tela.blit(texto_mochila, texto_mochila_rect)
        
        # Desenhar barra de progresso da capacidade
        barra_largura = 300
        barra_altura = 20
        barra_x = (LARGURA - barra_largura) // 2
        barra_y = 120
        
        # Barra de fundo
        pygame.draw.rect(self.tela, CINZA_CLARO, (barra_x, barra_y, barra_largura, barra_altura))
        
        # Barra de progresso
        progresso = min(peso_atual / self.capacidade_mochila, 1.0)
        cor_barra = VERMELHO if progresso > 1.0 else VERDE if progresso < 0.8 else AMARELO
        pygame.draw.rect(self.tela, cor_barra, (barra_x, barra_y, int(barra_largura * progresso), barra_altura))
        
        # Contorno da barra
        pygame.draw.rect(self.tela, PRETO, (barra_x, barra_y, barra_largura, barra_altura), 2)
        
        # Lista de itens
        y_inicial = 180
        for i, item in enumerate(self.itens):
            y_pos = y_inicial + i * 50
            
            # Cor do item (selecionado ou não)
            cor_fundo = VERDE if i in self.itens_selecionados else CINZA_CLARO
            
            # Retângulo do item
            item_rect = pygame.Rect(100, y_pos, 1000, 40)
            pygame.draw.rect(self.tela, cor_fundo, item_rect)
            pygame.draw.rect(self.tela, PRETO, item_rect, 2)
            
            # Número do item
            numero = self.font_normal.render(f"{i+1}", True, PRETO)
            numero_rect = numero.get_rect(center=(130, y_pos + 20))
            self.tela.blit(numero, numero_rect)
            
            # Nome do item
            nome = self.font_normal.render(item["nome"], True, PRETO)
            self.tela.blit(nome, (170, y_pos + 10))
            
            # Peso do item
            peso = self.font_normal.render(f"Peso: {item['peso']}kg", True, PRETO)
            self.tela.blit(peso, (600, y_pos + 10))
            
            # Valor do item
            valor = self.font_normal.render(f"Valor: {item['valor']}", True, PRETO)
            self.tela.blit(valor, (800, y_pos + 10))
            
            # Indicador de seleção
            if i in self.itens_selecionados:
                check = self.font_normal.render("✓", True, VERDE)
                self.tela.blit(check, (1050, y_pos + 10))
        
        # Instruções
        instrucoes = [
            "Pressione as teclas numéricas (1-9, 0) para selecionar/desselecionar itens",
            "Pressione ENTER para confirmar sua escolha",
            "Pressione ESC para sair"
        ]
        
        y_instrucao = 700
        for instrucao in instrucoes:
            texto = self.font_pequena.render(instrucao, True, PRETO)
            texto_rect = texto.get_rect(center=(LARGURA//2, y_instrucao))
            self.tela.blit(texto, texto_rect)
            y_instrucao += 25
    
    def desenhar_resultado(self):
        # Título
        titulo = self.font_titulo.render("Resultado da Aventura", True, AZUL)
        titulo_rect = titulo.get_rect(center=(LARGURA//2, 50))
        self.tela.blit(titulo, titulo_rect)
        
        # Calcular porcentagem de eficiência
        if self.valor_otimo > 0:
            eficiencia = (self.valor_jogador / self.valor_otimo) * 100
        else:
            eficiencia = 0
        
        # Sua escolha (lado esquerdo)
        pygame.draw.rect(self.tela, CINZA_CLARO, (50, 120, 500, 400))
        pygame.draw.rect(self.tela, PRETO, (50, 120, 500, 400), 2)
        
        titulo_jogador = self.font_normal.render("SUA ESCOLHA", True, PRETO)
        titulo_jogador_rect = titulo_jogador.get_rect(center=(300, 140))
        self.tela.blit(titulo_jogador, titulo_jogador_rect)
        
        # Estatísticas do jogador
        stats_jogador = [
            f"Valor Total: {self.valor_jogador}",
            f"Peso Total: {self.peso_jogador}kg / {self.capacidade_mochila}kg",
            f"Itens Selecionados: {len(self.itens_selecionados)}"
        ]
        
        y_pos = 170
        for stat in stats_jogador:
            texto = self.font_normal.render(stat, True, PRETO)
            self.tela.blit(texto, (70, y_pos))
            y_pos += 30
        
        # Lista de itens do jogador
        y_pos = 280
        texto_itens = self.font_normal.render("Itens escolhidos:", True, PRETO)
        self.tela.blit(texto_itens, (70, y_pos))
        y_pos += 30
        
        for i in self.itens_selecionados:
            item = self.itens[i]
            item_texto = f"• {item['nome']} (Peso: {item['peso']}kg, Valor: {item['valor']})"
            texto = self.font_pequena.render(item_texto, True, PRETO)
            self.tela.blit(texto, (70, y_pos))
            y_pos += 20
        
        # Solução ótima (lado direito)
        pygame.draw.rect(self.tela, CINZA_CLARO, (650, 120, 500, 400))
        pygame.draw.rect(self.tela, PRETO, (650, 120, 500, 400), 2)
        
        titulo_otimo = self.font_normal.render("SOLUÇÃO ÓTIMA", True, PRETO)
        titulo_otimo_rect = titulo_otimo.get_rect(center=(900, 140))
        self.tela.blit(titulo_otimo, titulo_otimo_rect)
        
        # Estatísticas da solução ótima
        peso_otimo = sum(self.itens[i]["peso"] for i in self.itens_otimos)
        stats_otimo = [
            f"Valor Total: {self.valor_otimo}",
            f"Peso Total: {peso_otimo}kg / {self.capacidade_mochila}kg",
            f"Itens Selecionados: {len(self.itens_otimos)}"
        ]
        
        y_pos = 170
        for stat in stats_otimo:
            texto = self.font_normal.render(stat, True, PRETO)
            self.tela.blit(texto, (670, y_pos))
            y_pos += 30
        
        # Lista de itens da solução ótima
        y_pos = 280
        texto_itens = self.font_normal.render("Itens da solução ótima:", True, PRETO)
        self.tela.blit(texto_itens, (670, y_pos))
        y_pos += 30
        
        for i in self.itens_otimos:
            item = self.itens[i]
            item_texto = f"• {item['nome']} (Peso: {item['peso']}kg, Valor: {item['valor']})"
            texto = self.font_pequena.render(item_texto, True, PRETO)
            self.tela.blit(texto, (670, y_pos))
            y_pos += 20
        
        # Avaliação de desempenho
        y_pos = 550
        
        # Eficiência
        eficiencia_texto = f"Eficiência: {eficiencia:.1f}%"
        cor_eficiencia = VERDE if eficiencia >= 90 else AMARELO if eficiencia >= 70 else VERMELHO
        texto_eficiencia = self.font_normal.render(eficiencia_texto, True, cor_eficiencia)
        texto_eficiencia_rect = texto_eficiencia.get_rect(center=(LARGURA//2, y_pos))
        self.tela.blit(texto_eficiencia, texto_eficiencia_rect)
        
        # Feedback baseado na eficiência
        y_pos += 40
        if eficiencia >= 95:
            feedback = "🎉 Perfeito! Você encontrou a solução ótima!"
            cor_feedback = VERDE
        elif eficiencia >= 85:
            feedback = "👍 Excelente! Você chegou muito perto da solução ótima!"
            cor_feedback = VERDE
        elif eficiencia >= 70:
            feedback = "✅ Bom trabalho! Você fez escolhas razoáveis."
            cor_feedback = AMARELO
        elif eficiencia >= 50:
            feedback = "⚠️ Pode melhorar. Analise o valor vs peso dos itens."
            cor_feedback = VERMELHO
        else:
            feedback = "❌ Tente novamente! Foque em itens com melhor relação valor/peso."
            cor_feedback = VERMELHO
        
        texto_feedback = self.font_normal.render(feedback, True, cor_feedback)
        texto_feedback_rect = texto_feedback.get_rect(center=(LARGURA//2, y_pos))
        self.tela.blit(texto_feedback, texto_feedback_rect)
        
        # Barra de progresso da eficiência
        y_pos += 60
        barra_largura = 400
        barra_altura = 20
        barra_x = (LARGURA - barra_largura) // 2
        
        # Barra de fundo
        pygame.draw.rect(self.tela, CINZA_CLARO, (barra_x, y_pos, barra_largura, barra_altura))
        
        # Barra de progresso
        progresso_eficiencia = min(eficiencia / 100, 1.0)
        cor_barra = VERDE if eficiencia >= 85 else AMARELO if eficiencia >= 70 else VERMELHO
        pygame.draw.rect(self.tela, cor_barra, (barra_x, y_pos, int(barra_largura * progresso_eficiencia), barra_altura))
        
        # Contorno da barra
        pygame.draw.rect(self.tela, PRETO, (barra_x, y_pos, barra_largura, barra_altura), 2)
        
        # Instruções
        instrucoes = [
            "Pressione R para jogar novamente",
            "Pressione ESC para sair"
        ]
        
        y_instrucao = 720
        for instrucao in instrucoes:
            texto = self.font_pequena.render(instrucao, True, PRETO)
            texto_rect = texto.get_rect(center=(LARGURA//2, y_instrucao))
            self.tela.blit(texto, texto_rect)
            y_instrucao += 25
    
    def alternar_item(self, indice):
        """Alterna a seleção de um item"""
        if indice in self.itens_selecionados:
            self.itens_selecionados.remove(indice)
        else:
            # Verificar se adicionar o item não ultrapassa a capacidade
            peso_atual = sum(self.itens[i]["peso"] for i in self.itens_selecionados)
            if peso_atual + self.itens[indice]["peso"] <= self.capacidade_mochila:
                self.itens_selecionados.append(indice)
    
    def calcular_resultado(self):
        """Calcula o valor da escolha do jogador e a solução ótima"""
        # Calcular valor e peso da escolha do jogador
        self.valor_jogador = sum(self.itens[i]["valor"] for i in self.itens_selecionados)
        self.peso_jogador = sum(self.itens[i]["peso"] for i in self.itens_selecionados)
        
        # Calcular solução ótima usando programação dinâmica
        self.valor_otimo, self.itens_otimos = self.knapsack_otimo()
    
    def knapsack_otimo(self):
        """Resolve o problema da mochila usando programação dinâmica"""
        n = len(self.itens)
        W = self.capacidade_mochila
        
        # Criar tabela DP
        dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
        
        # Preencher tabela DP
        for i in range(1, n + 1):
            for w in range(1, W + 1):
                peso_item = self.itens[i-1]["peso"]
                valor_item = self.itens[i-1]["valor"]
                
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
                w -= self.itens[i-1]["peso"]
        
        return valor_otimo, itens_otimos

if __name__ == "__main__":
    jogo = JogoMochila()
    jogo.executar() 