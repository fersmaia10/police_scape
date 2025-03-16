from code.Background import Background
from code.Const import  WIN_WIDTH

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'level1BG':
                list_BG = []
                for i in range(7):
                    list_BG.append(Background(f'level1BG{i}', (0, 0)))
                    list_BG.append(Background(f'level1BG{i}', (WIN_WIDTH, 0)))
                return list_BG

#classe que definirá o nível do jogo