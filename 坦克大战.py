import pygame
import sys
from  pygame.locals import  *

class TaskMain():
    """坦克大战的主窗口"""

    def startMain(self):

        width = 600

        heigh = 500

        pygame.init()
        # 创建一个屏幕，屏幕的大小
        screen = pygame.display.set_mode((width,heigh),0,32)
        pygame.display.set_caption('坦克大战')

        while True:

            screen.fill((255,255,255))

            screen.blit(self.write_text(),(5,0))

            self.get_event()

            pygame.display.update()

    def stopGame(self):
        """关闭程序"""
        sys.exit()

    def get_event(self):

        for event in pygame.event.get():

            if event.type == QUIT:

                self.stopGame()


            if event.type == KEYDOWN:

                if event.key == K_LEFT:

                    pass

                if event.key == K_RIGHT:

                    pass

                if event.key == K_UP:

                    pass

                if event.key == K_DOWN:

                    pass

                if event.key == K_ESCAPE:

                    self.stopGame()

            # if event.type == MOUSEBUTTONDOWN


    def write_text(self):


        font = pygame.font.SysFont('abyssinicasil',20)

        text_sf = font.render('Welcome',True,(0,0,0))

        return text_sf

class BaseItem(pygame.sprite.Sprite):

    def __init__(self):

       pygame.sprite.Sprite.__init__(self)

class Tank(BaseItem):

    # 定义类属性，所有的坦克都一样的

    width = 50

    height = 50

    def __init__(self):

        super.__init__()

        self.direction = 'D'






if __name__ == '__main__':

    game =TaskMain()

    game.startMain()

