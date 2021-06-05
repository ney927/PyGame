import pygame
import random
from car import Car
# paths = ['/Users/neyhabilling/Desktop/Hackathon/images/obstacleCar2.png', '/Users/neyhabilling/Desktop/Hackathon/images/obstacleCar.png']
class Obstacle (pygame.sprite.Sprite):
  def __init__(self, w, h):
    super().__init__()
    # self.image = pygame.image.load(paths[(int)(random.uniform(0, 2))]).convert_alpha()
    self.image = pygame.image.load('/Users/neyhabilling/Desktop/Hackathon/images/obstacleCar.png').convert_alpha()
    self.image = pygame.transform.smoothscale(self.image, (w, h))
    self.rect = self.image.get_rect()
    # self.moveUp = pygame.event.Event(self.move(5), 0)

  def moveUp(self, pixels):
    self.rect.y += pixels

  def update(self, x):
    self.moveUp((int)(x))

