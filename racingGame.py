import random
import pygame
from car import Car
from obstacle import Obstacle
class racingGame():

  def __init__(self):
    import random
    import pygame
    from car import Car
    from obstacle import Obstacle
    pygame.init()
    self.BLACK = ( 0, 0, 0)
    self.WHITE = (255, 255, 255)
    self.GREEN = (61, 191, 52)
    self.GRAY = (148, 148, 148)
    self.DARKGRAY = (87, 87, 87)
    self.width = 700
    self.height = 700
    self.screen = pygame.display.set_mode((self.width, self.height))
    pygame.display.set_caption("Racing Game")

    self.display_surface = pygame.display.set_mode((self.width, self.height)) #display surface object for text

    self.MC = pygame.sprite.Group()
    self.player = Car(50, 100)
    self.player.rect.x = 330
    self.player.rect.y = self.height/2+100
    self.MC.add(self.player)

    self.speed = 5.0
    self.often = 1000
    self.pygame.time.set_timer(pygame.USEREVENT+1, often)
    self.pygame.time.set_timer(pygame.USEREVENT+2, 3500)

    self.obstacle_positions = [480, 200, 330]
    self.obstacles_list = pygame.sprite.Group()
    self.obst = Obstacle(50, 100)
    self.obst.rect.x = obstacle_positions[(int)(random.uniform(0, 3))]
    self.obstacles_list.add(obst)
    
    self.clock = pygame.time.Clock() 
    self.carryOn = True
    self.startGame = False
    self.lives = 3

  def show_text(text, fontsize, textColour, xPos, yPos): #background will be none
    #displaying text
    font = pygame.font.Font('freesansbold.ttf', fontsize) #set font
    textSurf = font.render(text, True, textColour) #text surface object for test
    textSurf = font.render(text, True, textColour) #text surface object for test
    textRect = textSurf.get_rect() #rect obj for surface
    textRect.center = (xPos, yPos) # set the center placement for obj
    display_surface.blit(textSurf, textRect)

  def drawLanes(pixels):
    for x in range(10):
      pygame.draw.rect(screen, WHITE, [270, x*100-pixels, 10, 50],0)
    for x in range(10):
      pygame.draw.rect(screen, WHITE, [420, x*100-pixels, 10, 50],0)

  def playGame(self):
    # -------- Main Program Loop -----------
    while self.carryOn:
      # --- Main event loop
      if self.lives > 0:
        if self.startGame:
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
              self.carryOn = False
            elif event.type == pygame.KEYDOWN:
              if event.key == pygame.K_x: #if x key is pressed, exit game
                self.carryOn = False
            if event.type == pygame.USEREVENT+1:
              rand = (int)(random.uniform(0, 3))
              obst2 = Obstacle(50, 100)
              obst2.rect.x = obstacle_positions[rand]
              obstacles_list.add(obst2)

              speed += 0.1
              print(speed)

              if (speed > 8):
                newRand = (int)(random.uniform(0, 3))
                while newRand == rand:
                  newRand = (int)(random.uniform(0, 3))
                obst2 = Obstacle(50, 100)
                obst2.rect.x = obstacle_positions[newRand]
                obstacles_list.add(obst2)

            if event.type == pygame.USEREVENT+2 and speed > 9.8:
              rand = (int)(random.uniform(0, 3))
              obst2 = Obstacle(50, 100)
              obst2.rect.x = obstacle_positions[rand]
              obstacles_list.add(obst2)
              speed = 9

          keys = pygame.key.get_pressed()
          if keys[pygame.K_RIGHT] and player.rect.x < 540 - player.rect.width:
            player.moveRight(7)
            startGame = True
          if keys[pygame.K_LEFT] and player.rect.x > 150 + 10:
            player.moveLeft(7)
            startGame = True

          obstacles_list.update(speed)
          # obstacles_list.update((int)(abs(x-5000)/1000)+1)
          
          for obstacle in obstacles_list:
            if obstacle.rect.colliderect(player):
              obstacles_list.remove(obstacle)
              lives -= 1

        # --- Drawing code should go here
        screen.fill(GREEN)
        # pygam.draw.rec(location, colour, [x-coordinate, y-corrdinate, width, length], idk)
        pygame.draw.rect(screen, GRAY, [150, 0, 400, height],0)
        pygame.draw.rect(screen, DARKGRAY, [150, 0, 10, height],0)
        pygame.draw.rect(screen, DARKGRAY, [540, 0, 10, height],0)
        drawLanes(20) 
        #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
        obstacles_list.draw(screen)
        MC.draw(screen)
        show_text(f'Lives: {lives}', 25, BLACK, 50, 25)
        if not startGame:
          show_text('Use the arrow keys to move', 32, BLACK, width/2, height/2-50)
          show_text('You have 3 lives, Good Luck!', 32, BLACK, width/2, height/2 + 50)
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
              carryOn = False
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_x: #if x key is pressed, exit game
                carryOn = False
              if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                startGame = True
                print(startGame)
      else:
        screen.fill(WHITE)
        show_text('Game Over!', 32, BLACK, width/2, height/2-50)
        show_text('press ESC to exit', 25, BLACK, width/2, height/2-50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              carryOn = False
            elif event.type == pygame.KEYDOWN:
              if event.key == pygame.K_x: #if x key is pressed, exit game
                carryOn = False

      # --- Go ahead and update the screen with what we've drawn.
      pygame.display.flip()

      # --- Limit to 60 frames per second
      clock.tick(60)

#Once we have exited the main program loop we can stop the game engine:
  # pygame.quit()
