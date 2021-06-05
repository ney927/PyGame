import pygame
from racingGame import racingGame
from main import game
import snake_game

# race = racingGame()
# race.playGame()


pygame.init()
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (61, 191, 52)
GRAY = (148, 148, 148)
DARKGRAY = (87, 87, 87)
width = 700
height = 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Break Time!")
play = True
clock = pygame.time.Clock() 

display_surface = pygame.display.set_mode((width, height)) #display surface object for text
def show_text(text, fontsize, textColour, xPos, yPos): #background will be none
  #displaying text
  font = pygame.font.Font('freesansbold.ttf', fontsize) #set font
  textSurf = font.render(text, True, textColour) #text surface object for test
  textSurf = font.render(text, True, textColour) #text surface object for test
  textRect = textSurf.get_rect() #rect obj for surface
  textRect.center = (xPos, yPos) # set the center placement for obj
  display_surface.blit(textSurf, textRect)


while play:
  width = 700
  height = 700
  screen = pygame.display.set_mode((width, height))
  pygame.display.set_caption("Break Time!") 
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        play = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_s:
        snake_game.main()
      elif event.key == pygame.K_r:
        game()
  screen.fill((200,150,150))
  show_text('Congrats!', 32, BLACK, width/2, height/2-100)
  show_text('You finished 20 minutes of hard work', 32, BLACK, width/2, height/2-50)
  show_text('Which game would you like to play?', 32, BLACK, width/2, height/2)
  show_text('S for Snake or R for Racing?', 32, BLACK, width/2, height/2+50)
  pygame.display.flip()
  clock.tick(60)
pygame.quit()
