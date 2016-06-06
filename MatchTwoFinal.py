import pygame
import math
import random


pygame.init()
gamedisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Match Two')

p = 0
cb = 0
click_count = []
dep = 0

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (174, 7, 164)
orange = (238, 103, 4)
cyan = (7, 230, 217)
yellow = (245, 245, 0)
chart = (86, 245, 0)
grey = (111, 111, 111)
brown = (160, 84, 3)
pink = (250, 180, 250)
magenta = (223, 30, 225)
dkgreen = (4, 122, 15)
dkred = (180, 3, 3)
navy = (2, 5, 142)
dkpurple = (81, 2, 108)
dkgrey = (56, 56, 56)

basicFont = pygame.font.SysFont(None, 24)
largefont = pygame.font.SysFont(None, 32)


def coorfind(x, y):
    xcord = int(((math.ceil(x / 100.0)) * 100) - 100)
    ycord = int(((math.ceil(y / 100.0)) * 100) - 100)
    return (xcord, ycord)




# number, chosen currently, used, random color, random number, x, y
rectprops = [[0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 100, 0],
             [2, 0, 0, 0, 0, 200, 0], [3, 0, 0, 0, 0, 300, 0],
             [4, 0, 0, 0, 0, 400, 0], [5, 0, 0, 0, 0, 500, 0],
             [6, 0, 0, 0, 0, 600, 0], [7, 0, 0, 0, 0, 700, 0],
             [8, 0, 0, 0, 0, 0, 100], [9, 0, 0, 0, 0, 100, 100],
             [10, 0, 0, 0, 0, 200, 100], [11, 0, 0, 0, 0, 300, 100],
             [12, 0, 0, 0, 0, 400, 100], [13, 0, 0, 0, 0, 500, 100],
             [14, 0, 0, 0, 0, 600, 100], [15, 0, 0, 0, 0, 700, 100],
             [16, 0, 0, 0, 0, 0, 200], [17, 0, 0, 0, 0, 100, 200],
             [18, 0, 0, 0, 0, 200, 200], [19, 0, 0, 0, 0, 300, 200],
             [20, 0, 0, 0, 0, 400, 200], [21, 0, 0, 0, 0, 500, 200],
             [22, 0, 0, 0, 0, 600, 200], [23, 0, 0, 0, 0, 700, 200],
             [24, 0, 0, 0, 0, 0, 300], [25, 0, 0, 0, 0, 100, 300],
             [26, 0, 0, 0, 0, 200, 300], [27, 0, 0, 0, 0, 300, 300],
             [28, 0, 0, 0, 0, 400, 300], [29, 0, 0, 0, 0, 500, 300],
             [30, 0, 0, 0, 0, 600, 300], [31, 0, 0, 0, 0, 700, 300],
             [32, 0, 0, 0, 0, 0, 400], [33, 0, 0, 0, 0, 100, 400],
             [34, 0, 0, 0, 0, 200, 400], [35, 0, 0, 0, 0, 300, 400],
             [36, 0, 0, 0, 0, 400, 400], [37, 0, 0, 0, 0, 500, 400],
             [38, 0, 0, 0, 0, 600, 400], [39, 0, 0, 0, 0, 700, 400],
             [40, 0, 0, 0, 0, 0, 500], [41, 0, 0, 0, 0, 100, 500],
             [42, 0, 0, 0, 0, 200, 500], [43, 0, 0, 0, 0, 300, 500],
             [44, 0, 0, 0, 0, 400, 500], [45, 0, 0, 0, 0, 500, 500],
             [46, 0, 0, 0, 0, 600, 500], [47, 0, 0, 0, 0, 700, 500]]
# number, chosen currently, used, random color, random number, x, y

numlist = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13',
           '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24',
           '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13',
           '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']

color_choice = [red, green, blue, purple, orange, cyan, yellow, chart, grey,
                brown, pink, magenta, dkgreen, dkred, navy, dkpurple, dkgrey]


def randassign():
    global rectprops
    global numlist
    global color_choice
    r = 0
    while numlist:
        num = random.choice(numlist)
        rectprops[r][4] = num
        color = random.choice(color_choice)
        rectprops[r][3] = color
        numlist.remove(num)
        r += 1


def throw():
    global rectprops
    c = 0
    while c < 48:
        color = rectprops[c][3]
        y = rectprops[c][6]
        x = rectprops[c][5]
        w = 100
        h = 100

        pygame.draw.rect(gamedisplay, color, (x, y, w, h))
        c += 1

    # vertical lines
    pygame.draw.line(gamedisplay, black, (0, 0), (0, 600), 3)
    pygame.draw.line(gamedisplay, black, (100, 0), (100, 600), 3)
    pygame.draw.line(gamedisplay, black, (200, 0), (200, 600), 3)
    pygame.draw.line(gamedisplay, black, (300, 0), (300, 600), 3)
    pygame.draw.line(gamedisplay, black, (400, 0), (400, 600), 3)
    pygame.draw.line(gamedisplay, black, (500, 0), (500, 600), 3)
    pygame.draw.line(gamedisplay, black, (600, 0), (600, 600), 3)
    pygame.draw.line(gamedisplay, black, (700, 0), (700, 600), 3)
    pygame.draw.line(gamedisplay, black, (799, 0), (799, 600), 2)
    # horizontal lines
    pygame.draw.line(gamedisplay, black, (0, 0), (0, 800), 3)
    pygame.draw.line(gamedisplay, black, (0, 100), (800, 100), 3)
    pygame.draw.line(gamedisplay, black, (0, 200), (800, 200), 3)
    pygame.draw.line(gamedisplay, black, (0, 300), (800, 300), 3)
    pygame.draw.line(gamedisplay, black, (0, 400), (800, 400), 3)
    pygame.draw.line(gamedisplay, black, (0, 500), (800, 500), 3)
    pygame.draw.line(gamedisplay, black, (0, 600), (800, 600), 3)
    pygame.draw.line(gamedisplay, black, (0, 700), (800, 700), 3)
    pygame.draw.line(gamedisplay, black, (0, 790), (800, 799), 2)

    pygame.display.update()



def main():
    global click_count
    global cb
    global coorfind
    global throw
    global dep
    global endgame
    throw()
    print(rectprops)
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                mx, my = event.pos
                click_count.append([mx, my])
                xcoord, ycoord = coorfind(mx, my)
                print('Number of clicks = ' + str(len(click_count)) + '.')
                dep += 1
                print('Dep = ' + str(dep) + '.')
                throw()
                z = 0
                check = 0
                if dep == 1:
                    countx = 0
                    county = 0
                    while rectprops[countx][5] != xcoord:
                        countx += 1
                        while rectprops[county][6] != ycoord:
                            county += 1
                    if ycoord == 100 and xcoord == 0:
                        countx += 8
                    elif ycoord == 200 and xcoord == 0:
                        countx += 16
                    elif ycoord == 300 and xcoord == 0:
                        countx += 24
                    elif ycoord == 400 and xcoord == 0:
                        countx += 32
                    elif ycoord == 500 and xcoord == 0:
                        countx += 40
                    gs = countx + county
                    if rectprops[gs][1] == 0 and rectprops[gs][2] == 0:
                        print('Squares grid number = ' + str(gs) + '.')
                        print('Squares random number: ' + str(rectprops[gs][4])
                              + '.')
                        print('Dep = ' + str(dep) + '.')
                        print()
                        print()
                        pygame.draw.rect(gamedisplay, black, (rectprops[gs][5],
                                         rectprops[gs][6], 100, 100))
                        text = basicFont.render(rectprops[gs][4], True, (255,
                                                                         255,
                                                                         255))
                        gamedisplay.blit(text, (rectprops[gs][5] + 50, rectprops
                                                [gs][6] + 50))
                        rectprops[gs][1] = 1
                        pygame.display.update()
                if dep == 2:
                    countx = 0
                    county = 0
                    while rectprops[countx][5] != xcoord:
                        countx += 1
                        while rectprops[county][6] != ycoord:
                            county += 1
                    if ycoord == 100 and xcoord == 0:
                        countx += 8
                    elif ycoord == 200 and xcoord == 0:
                        countx += 16
                    elif ycoord == 300 and xcoord == 0:
                        countx += 24
                    elif ycoord == 400 and xcoord == 0:
                        countx += 32
                    elif ycoord == 500 and xcoord == 0:
                        countx += 40
                    gs = countx + county
                    if rectprops[gs][1] == 0 and rectprops[gs][2] == 0:
                        cc = 0
                        while rectprops[cc][1] != 1:
                            cc += 1
                        if cc == gs and cc < 48:
                            cc += 1
                            while rectprops[cc][1] != 1:
                                cc += 1
                    if rectprops[gs][4] == rectprops[cc][4]:
                        rectprops[gs][3] = black
                        rectprops[cc][3] = black
                        rectprops[gs][2] = 1
                        rectprops[cc][2] = 1
                        rectprops[cc][1] = 0
                        rectprops[gs][1] = 0
                    if rectprops[gs][4] != rectprops[cc][4]:
                        rectprops[cc][1] = 0
                        rectprops[gs][1] = 0
                        throw()
                    print('Already clicked square = ' + str(cc) + '.')
                    print('Squares grid number = ' + str(gs) + '.')
                    print('Squares random number: ' + str(rectprops[gs][4])
                          + '.')
                    print('Dep = ' + str(dep) + '.')
                    print()
                    print()
                    pygame.draw.rect(gamedisplay, black, (rectprops[gs][5],
                                     rectprops[gs][6], 100, 100))
                    pygame.draw.rect(gamedisplay, black, (rectprops[cc][5],
                                     rectprops[cc][6], 100, 100))
                    text = basicFont.render(rectprops[gs][4], True, (255,
                                                                     255,
                                                                     255))
                    gamedisplay.blit(text, (rectprops[gs][5] + 50, rectprops
                                            [gs][6] + 50))
                    text2 = basicFont.render(rectprops[cc][4], True, (255,
                                                                      255,
                                                                      255))
                    gamedisplay.blit(text2, (rectprops[cc][5] + 50, rectprops
                                             [cc][6] + 50))
                    pygame.display.update()
                    while z < 48:
                        if rectprops[z][2] == 1:
                            check += 1
                        z += 1
                        print('Used Squares = ' + str(check) + '.')
                    if check == 48:
                        gamedisplay.fill((1, 27, 180))
                        gamedisplay.fill((1, 27, 180))
                        score = len(click_count)
                        text = largefont.render('Congratulations! You won!', True, (255, 255, 255))
                        gamedisplay.blit(text, (250, 10))
                        text = basicFont.render('You clicked ' + str(score) + ' boxes.', True, (255,
                                                255, 255))
                        gamedisplay.blit(text, (10, 150))
                        text = basicFont.render('That was ' + str((score - 48)) + ' more than the '
                                                'best possible score.', True, (255, 255, 255))
                        gamedisplay.blit(text, (10, 170))

                        if score <= 72:
                            text = basicFont.render('Wow, fantastic job!', True, (255, 255, 255))
                            gamedisplay.blit(text, (10, 190))
                        if score >= 73 and score <= 110:
                            text = basicFont.render('Not bad!', True, (255, 255, 255))
                            gamedisplay.blit(text, (10, 190))
                        if score >= 111 and score <= 170:
                            text = basicFont.render('Wasn\'t easy, was it?', True, (255, 255, 255))
                            gamedisplay.blit(text, (10, 190))
                        if score > 170:
                            text = basicFont.render('Ouch, that took a while. Practice your memory '
                                                    'skills...', True, (255, 255, 255))
                            gamedisplay.blit(text, (10, 190))
                            pygame.display.update()
                    dep = 0

randassign()
main()