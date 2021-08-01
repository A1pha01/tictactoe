import pygame
import sys
import random
import time
class Game:
    def __init__(self):
        pygame.init()
        self.squares = ['', '', '', '', '', '', '', '', '']
        self.turn = 1
        #possible values: menu, playing, playerxW, playeroW, tie
        self.score = 'menu'
        self.size = (600, 600)
        self.menubkrnd = pygame.image.load('menu.jpg')
        self.owin = pygame.image.load('owin.png')
        self.xwin = pygame.image.load('xwin.png')
        self.trophy = pygame.image.load('trophy.jpg')
        self.player_1 = pygame.image.load('player_1.png')
        self.player_2 = pygame.image.load('player_2.png')
        self.o = pygame.image.load('o.png')
        self.x = pygame.image.load('x.png')
        self.bkrnd = pygame.image.load('background.png')
        self.tie = pygame.image.load('tie.gif')
        self.screen = pygame.display.set_mode(self.size)
        self.ai = pygame.image.load('ai.png')
        self.p2 = pygame.image.load('p2.png')
        #possible values: cv, irl
        self.mode = None
    def logic_menu(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                if x >= 200 and x <= 406:
                    if y >= 300 and y <= 371:
                        self.score = 'playing'
                        self.mode = 'irl'
                if x >= 200 and x <= 406:
                    if y >= 100 and y <= 171:
                        self.score = 'playing'
                        self.mode = 'cv'

    def logic_playing(self, events):
        d = 188
        r = 40
        if self.turn == 2 and self.mode == 'cv' and self.score == 'playing':
            time.sleep(0.5)
            x = 0
            indxs = []
            while x < len(self.squares):
                if self.squares[x] == '':
                     indxs.append(x)
                x += 1
            indx = random.choice(indxs)
            self.squares[indx] = 'o'
            self.turn = 1
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP and self.score == 'playing':
                x, y = pygame.mouse.get_pos()
                if x >= r:
                    indx_x = ((x - r) // d)
                else:
                    indx_x = 0
                if y >= r:
                    indx_y = ((y - r) // d) * 3
                else:
                    indx_y = 0
                indx = indx_x + indx_y
                if self.squares[indx] == '':
                    if self.turn == 1:
                        self.turn = 2
                        self.squares[indx] = 'x'
                    elif self.mode == 'irl':    
                        if self.turn == 2:
                            self.turn = 1  
                            self.squares[indx] = 'o'
        if self.score != 'playing':
            return
        if self.squares[0] == 'x' and self.squares[1] == 'x'and self.squares[2] == 'x':
            self.score = 'playerxW'
        if self.squares[3] == 'x' and self.squares[4] == 'x'and self.squares[5] == 'x':
            self.score = 'playerxW'
        if self.squares[6] == 'x' and self.squares[7] == 'x'and self.squares[8] == 'x':
            self.score = 'playerxW'
        if self.squares[0] == 'x' and self.squares[3] == 'x'and self.squares[6] == 'x':
            self.score = 'playerxW'
        if self.squares[1] == 'x' and self.squares[4] == 'x'and self.squares[7] == 'x':
            self.score = 'playerxW'
        if self.squares[2] == 'x' and self.squares[5] == 'x'and self.squares[8] == 'x':
            self.score = 'playerxW'
        if self.squares[0] == 'x' and self.squares[4] == 'x'and self.squares[8] == 'x':
            self.score = 'playerxW'
        if self.squares[2] == 'x' and self.squares[4] == 'x'and self.squares[6] == 'x':
            self.score = 'playerxW'
        if self.squares[0] == 'o' and self.squares[1] == 'o'and self.squares[2] == 'o':
            self.score = 'playeroW'
        if self.squares[3] == 'o' and self.squares[4] == 'o'and self.squares[5] == 'o':
            self.score = 'playeroW'
        if self.squares[6] == 'o' and self.squares[7] == 'o'and self.squares[8] == 'o':
            self.score = 'playeroW'
        if self.squares[0] == 'o' and self.squares[3] == 'o'and self.squares[6] == 'o':
            self.score = 'playeroW'
        if self.squares[1] == 'o' and self.squares[4] == 'o'and self.squares[7] == 'o':
            self.score = 'playeroW'
        if self.squares[2] == 'o' and self.squares[5] == 'o'and self.squares[8] == 'o':
            self.score = 'playeroW'
        if self.squares[0] == 'o' and self.squares[4] == 'o'and self.squares[8] == 'o':
            self.score = 'playeroW'
        if self.squares[2] == 'o' and self.squares[4] == 'o'and self.squares[6] == 'o':
            self.score = 'playeroW' 
        if not '' in self.squares:
            if self.score == 'playing':
                self.score = 'tie'

    def logic(self):
        events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            else:
                events.append(event)
        if self.score == 'menu':
            self.logic_menu(events)
        else:
            self.logic_playing(events)

    def scene(self):
        if self.score == 'menu':
            self.scene_menu()
        else:
            self.scene_playing()
        pygame.display.flip()

    def scene_menu(self):
        self.screen.blit(self.menubkrnd, (0, 0))
        self.screen.blit(self.ai, (200, 100))
        self.screen.blit(self.p2, (200, 300))
    
    def scene_playing(self):
        d = 187
        black = (0, 0, 0)
        self.screen.fill(black)
        self.screen.blit(self.bkrnd, (0, 0))
        if self.turn == 1:
            self.screen.blit(self.player_1, (400, 5))
        if self.turn == 2:
            self.screen.blit(self.player_2, (400, 5))
        indx = 0
        while indx < len(self.squares):
            if self.squares[indx] == '':
                pass
            if self.squares[indx] == 'x':
                self.screen.blit(self.x, ((indx%3) * d + 25, (indx // 3) * d + 25))
            if self.squares[indx] == 'o':
                self.screen.blit(self.o, ((indx%3) * d + 25, (indx // 3) * d + 25))
            indx += 1
        if self.score == 'playerxW':
            self.screen.blit(self.trophy, (200,100))
            self.screen.blit(self.xwin, (250,350))
        elif self.score == 'playeroW':
            self.screen.blit(self.trophy, (200,100))
            self.screen.blit(self.owin,(250,350))
        elif self.score == 'tie':
            self.screen.blit(self.tie, (100, 50))
    

game = Game()
while True:
    game.logic()
    game.scene()

