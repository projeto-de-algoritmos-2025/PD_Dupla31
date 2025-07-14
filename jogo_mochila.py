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
        # Implementar na próxima etapa
        texto = self.font_titulo.render("Tela do Jogo - Em Desenvolvimento", True, PRETO)
        texto_rect = texto.get_rect(center=(LARGURA//2, ALTURA//2))
        self.tela.blit(texto, texto_rect)
    
    def desenhar_resultado(self):
        # Implementar na próxima etapa
        texto = self.font_titulo.render("Tela de Resultado - Em Desenvolvimento", True, PRETO)
        texto_rect = texto.get_rect(center=(LARGURA//2, ALTURA//2))
        self.tela.blit(texto, texto_rect)

if __name__ == "__main__":
    jogo = JogoMochila()
    jogo.executar() 