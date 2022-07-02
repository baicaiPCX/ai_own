import pygame
import sys

class Scenes(object):
    def __init__(self,window_size=(600,400)):
        pygame.init()
        screen=pygame.display.set_mode(window_size)
        # pygame.display.set_caption("ai actor")

        # while True:
        #     for event in pygame.event.get():
        #         if event.type==pygame.QUIT:
        #             sys.exit()
        #     pygame.display.update()

if __name__ == "__main__":
    m_sce=Scenes()
    pass
