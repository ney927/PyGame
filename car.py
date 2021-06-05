import pygame

class Car (pygame.sprite.Sprite):
  def __init__(self, w, h):
    super().__init__()
    self.image = pygame.image.load('/Users/neyhabilling/Desktop/Hackathon/images/mainCar.png').convert_alpha()
    self.image = pygame.transform.smoothscale(self.image, (w, h))
    self.rect = self.image.get_rect()

  def moveLeft(self, pixels):
    self.rect.x -= pixels
  
  def moveRight(self, pixels):
    self.rect.x += pixels