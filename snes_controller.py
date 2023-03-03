import sys
import pygame
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

clk = pygame.time.Clock()

if pygame.joystick.get_count() == 0:
    raise IOError("No joystick detected")
joy = pygame.joystick.Joystick(0)
joy.init()


def buttonX(boton):
    if(boton == 0):
        return 374+70
    elif(boton == 1):
        return 418+70
    elif(boton == 2):
        return 330+70
    elif(boton == 3):
        return 374+70
    elif(boton == 4):
        return 105+70
    elif(boton == 5):
        return 374+70
    elif(boton == 8):
        return 154+70
    elif(boton == 9):
        return 195+70


def buttonY(boton):
    if(boton == 0):
        return 166-30
    elif(boton == 1):
        return 133-30
    elif(boton == 2):
        return 133-30
    elif(boton == 3):
        return 100-30
    elif(boton == 4 or boton == 5):
        return 25-30
    elif(boton == 8):
        return 108-30
    elif(boton == 9):
        return 110-30


size = width, height = 566, 250
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Joystick Tester")
background_image = pygame.image.load("control.png").convert()
frameRect = pygame.Rect((0, 0), (width, height))

crosshair = pygame.surface.Surface((10, 10))
crosshair.fill(pygame.Color("magenta"))
pygame.draw.circle(crosshair, pygame.Color("black"), (5, 5), 5, 0)
crosshair.set_colorkey(pygame.Color("magenta"))

crosshairb = pygame.surface.Surface((20, 20))
crosshairb.fill(pygame.Color("magenta"))
pygame.draw.circle(crosshairb, pygame.Color("red"), (5, 5), 5, 0)
crosshairb.set_colorkey(pygame.Color("magenta"))

# triangulo azul = 3
# cuadrado verde = 2
# x amarillo = 0
# o rojo = 1
# L1 flecha arriba = 9
# click derecho flecha abajo = 8
# ps ? = 5
# pair flecha izq = 4
buttons = {}
for b in range(joy.get_numbuttons()):
    # print(b)
    buttons[b] = [
        crosshair,
        (buttonX(b), buttonY(b))
    ]
    # print(buttons)


while True:
    pygame.event.pump()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(background_image, (0, 0))

    x = joy.get_axis(0)
    y = joy.get_axis(1)
    screen.blit(crosshairb, ((x*20)+123-5, (y*20)+125-5))

    for b in range(joy.get_numbuttons()):
        if joy.get_button(b):
            print(buttons[b][0], buttons[b][1], b)
            screen.blit(buttons[b][0], buttons[b][1])

    pygame.display.flip()
    clk.tick(40)
