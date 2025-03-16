import pygame
from code.Const import COLOR_ORANGE, COLOR_YELLOW, MENU_OPTION, WIN_WIDTH, WIN_HEIGHT


class Menu:
    def __init__(self, window):
        #definindo imagens
        self.window = window
        self.surf = pygame.image.load('./asset/menuBG.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            #definindo os textos
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Police", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Scape", COLOR_ORANGE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, ((WIN_WIDTH / 2), 260 + 30 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_ORANGE, ((WIN_WIDTH / 2), 260 + 30 * i))
            pygame.display.flip()


            #evento para fechamento de janela
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            #evento de seleção do menu com a tecla para baixo
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
            #tecla para cima
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha().convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
