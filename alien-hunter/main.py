import random
import sys

import pygame
from pygame.locals import *

from sprites import Base, Player, PlayerBullet, Alien, AlienBullet

SCREENWIDTH, SCREENHEIGHT = 640, 360
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

while True:

    for event in pygame.event.get():
        esc_pressed = event.type == KEYDOWN and event.key == K_ESCAPE
        if event.type == QUIT or esc_pressed:
            pygame.quit()
            sys.exit()
