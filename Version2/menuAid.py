import pygame
import pygame.locals

class Menu(object):

  def __init__(self, width, height, colour):

    self.size = self.width, self.height = width, height
    self.clock = pygame.time.Clock()

    pygame.init()
    self.screen = pygame.display.set_mode(self.size)
    self.colour = colour
  
  def draw(self):
    self.screen.fill(self.colour)

    
  def update(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    self.clock.tick(60)
    pygame.display.update()


class Element(object):

  def __init__(self, x, y, width, height):
    self.x = x
    self.y = y
    self.width = width
    self.height = height

  def inBox(self, x, y, width, height, mousePos):
    return self.x < mousePos[0] < self.x + self.width and self.y < mousePos[1] < self.y + self.height