import pygame
import time

class Veiculo:
    def __init__(self, cor, modelo, ano, marca, velocidade = 0):
        self.cor = cor 
        self.modelo = modelo
        self.ano = ano
        self.marca = marca
        self.velocidade = velocidade
        print('Objeto do tipo Veiculo construido com sucesso!')

    def alterar_velocidade(self, valor):
        velocidade_atual = self.velocidade + valor
        
        if velocidade_atual < 0:
            print('Indisponivel!')
        else:
            self.velocidade = velocidade_atual
            
    def buzinar(self, tipo_buzina):
        if tipo_buzina == 1:
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load('fight-142564.mp3')
            pygame.mixer.music.play()
            time.sleep(0.5)
            
        elif tipo_buzina == 2:
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load('fight-142564.mp3')
            pygame.mixer.music.play()
            time.sleep(1)
            
        else:
            print('Buzina estragada!')