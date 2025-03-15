import pygame

<<<<<<< HEAD
=======
from code.Menu import Menu


>>>>>>> 8ee638a (Adicionando a janela com o background do menu)
class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))

<<<<<<< HEAD
#checando a inicialização da janela
=======
>>>>>>> 8ee638a (Adicionando a janela com o background do menu)
    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
<<<<<<< HEAD
            pass

#parei com 21min de aula
            #Checando todos os eventos
=======

>>>>>>> 8ee638a (Adicionando a janela com o background do menu)
            #for event in pygame.event.get():
             #   if event.type == pygame.QUIT:
              #      pygame.quit()
               #     quit()
<<<<<<< HEAD




#Configurando a abertura da Janela
=======
>>>>>>> 8ee638a (Adicionando a janela com o background do menu)
