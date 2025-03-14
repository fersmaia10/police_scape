import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))

#checando a inicialização da janela
    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

#parei com 21min de aula
            #Checando todos os eventos
            #for event in pygame.event.get():
             #   if event.type == pygame.QUIT:
              #      pygame.quit()
               #     quit()




#Configurando a abertura da Janela
