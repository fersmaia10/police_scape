import pygame

#Configurando a abertura da Janela
print ('Setup Start')
pygame.init()
window = pygame.display.set_mode(size=(600,480))
print('Setup End')

print('Loop Start')
while True:
    #Checando todos os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Saindo...')
            pygame.quit()
            quit()
