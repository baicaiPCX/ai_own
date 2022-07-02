import pygame
import sys

offset=lambda x,y:(x[0]+y,x[1]+y)
class GUI:
    def __init__(self,width,height):
        self.width=width
        self.height=height

        pygame.init()
        self.screen=pygame.display.set_mode(size=(width,height))
        pygame.display.set_caption("AI game")

        self.ship_icon=pygame.image.load("game/resources/img/spaceship.png").convert_alpha()
        self.bg_image=pygame.image.load("game/resources/img/background.jpeg").convert()
        self.bg_image=pygame.transform.scale(self.bg_image,(width,height)).convert_alpha()

        self._set_background()
        pygame.display.update()

    def update_frame(self,spaceships):
        self._set_background()
        if not isinstance(spaceships,(list,tuple)):
            spaceships=[spaceships]

        for ship in spaceships:
            spaceship_img=self._rot_center(self.ship_icon,ship.get_angle())
            ship_pos=offset(ship.get_xy(),-ship.radius)
            self.screen.blit(spaceship_img,ship_pos)

        pygame.display.update()
        pygame.time.wait(30)

    def back_events(self,engine):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    engine.left_down()
                if event.key == pygame.K_RIGHT:
                    engine.right_down()
                if event.key == pygame.K_UP:
                    engine.up_down()
                if event.key == pygame.K_DOWN:
                    engine.down_down()

    def _set_background(self):
        self.screen.blit(self.bg_image,[0,0])

    def _rot_center(self, image, angle):
        """
        rotate an image while keeping its center and size
        Thanks to https://www.pygame.org/wiki/RotateCenter?parent=CookBook
        """
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image

