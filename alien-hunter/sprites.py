import pygame


class Base(pygame.sprite.Sprite):

    List = pygame.sprite.Group()

    def __init__(self, x, y):
        pygame.sprite.Sprite(self)
        Base.List.add(self)


class Player(Base):

    List = pygame.sprite.Group()

    def __init__(self, x, y):
        Base.__init__(self, x, y)
        Player.List.add(self)


class PlayerBullet(Base):

    List = pygame.sprite.Group()

    def __init__(self, x, y):
        Base.__init__(self, x, y)
        PlayerBullet.List.add(self)


class Alien(Base):

    List = pygame.sprite.Group()

    def __init__(self, x, y):
        Base.__init__(self, x, y)
        Alien.List.add(self)


class AlienBullet(Base):

    List = pygame.sprite.Group()

    def __init__(self, x, y):
        Base.__init__(self, x, y)
        AlienBullet.List.add(self)
