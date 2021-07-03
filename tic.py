import pygame
import sys
turn = 1
squares = ['', '', '', '', '', '', '', '', '']
#possible values: playing, playerxW, playeroW, tie
score = 'playing'


def logic():
    global score
    global turn
    d = 188
    r = 40
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP and score == 'playing':
            x, y = pygame.mouse.get_pos()
            print('x', x, 'y', y)
            if x >= r:
                indx_x = ((x - r) // d)
            else:
                indx_x = 0
            if y >= r:
                indx_y = ((y - r) // d) * 3
            else:
                indx_y = 0
            print('indx_x', indx_x, 'indx_y',indx_y)
            indx = indx_x + indx_y
            print(indx)
            if squares[indx] == '':
                if turn == 1:
                    turn = 2
                    squares[indx] = 'x'
                elif turn == 2:
                    turn = 1  
                    squares[indx] = 'o' 
            else:
                pass
        if event.type == pygame.QUIT:
            sys.exit()
    if score != 'playing':
        return
    if squares[0] == 'x' and squares[1] == 'x'and squares[2] == 'x':
        score = 'playerxW'
    if squares[3] == 'x' and squares[4] == 'x'and squares[5] == 'x':
        score = 'playerxW'
    if squares[6] == 'x' and squares[7] == 'x'and squares[8] == 'x':
        score = 'playerxW'
    if squares[0] == 'x' and squares[3] == 'x'and squares[6] == 'x':
        score = 'playerxW'
    if squares[1] == 'x' and squares[4] == 'x'and squares[7] == 'x':
        score = 'playerxW'
    if squares[2] == 'x' and squares[5] == 'x'and squares[8] == 'x':
        score = 'playerxW'
    if squares[0] == 'x' and squares[4] == 'x'and squares[8] == 'x':
        score = 'playerxW'
    if squares[2] == 'x' and squares[4] == 'x'and squares[6] == 'x':
        score = 'playerxW'
    if squares[0] == 'o' and squares[1] == 'o'and squares[2] == 'o':
        score = 'playeroW'
    if squares[3] == 'o' and squares[4] == 'o'and squares[5] == 'o':
        score = 'playeroW'
    if squares[6] == 'o' and squares[7] == 'o'and squares[8] == 'o':
        score = 'playeroW'
    if squares[0] == 'o' and squares[3] == 'o'and squares[6] == 'o':
        score = 'playeroW'
    if squares[1] == 'o' and squares[4] == 'o'and squares[7] == 'o':
        score = 'playeroW'
    if squares[2] == 'o' and squares[5] == 'o'and squares[8] == 'o':
        score = 'playeroW'
    if squares[0] == 'o' and squares[4] == 'o'and squares[8] == 'o':
        score = 'playeroW'
    if squares[2] == 'o' and squares[4] == 'o'and squares[6] == 'o':
        score = 'playeroW' 
    if not '' in squares:
        if score == 'playing':
            score = 'tie'
            

def scene():
    global turn
    global score
    d = 187
    screen.fill(black)
    screen.blit(bkrnd, bkrndrect)
    if turn == 1:
        screen.blit(player_1, (400, 5))
    if turn == 2:
        screen.blit(player_2, (400, 5))
    indx = 0
    while indx < len(squares):
        if squares[indx] == '':
            pass
        if squares[indx] == 'x':
            screen.blit(x, ((indx%3) * d + 25, (indx // 3) * d + 25))
        if squares[indx] == 'o':
            screen.blit(o, ((indx%3) * d + 25, (indx // 3) * d + 25))
        indx += 1
    if score == 'playerxW':
        screen.blit(trophy, (200,100))
        screen.blit(xwin, (250,350))
    elif score == 'playeroW':
        screen.blit(trophy, (200,100))
        screen.blit(owin,(250,350))
    elif score == 'tie':
        screen.blit(tie, (100, 50))
    pygame.display.flip()


pygame.init()
size = width, height = 600, 600
black = (0, 0, 0)
owin = pygame.image.load('owin.png')
xwin = pygame.image.load('xwin.png')
trophy = pygame.image.load('trophy.jpg')
player_1 = pygame.image.load('player_1.png')
player_2 = pygame.image.load('player_2.png')
o = pygame.image.load('o.png')
x = pygame.image.load('x.png')
bkrnd = pygame.image.load('background.png')
tie = pygame.image.load('tie.gif')
bkrndrect = bkrnd.get_rect()
screen = pygame.display.set_mode(size)
while True:
    logic()
    scene()

