import sys, pygame
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

  def getMousePos(self):
    return pygame.mouse.get_pos()

  def getMouseButtons(self):
    return pygame.mouse.get_pressed()

class Element(object):

  def __init__(self, x, y, width, height):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.drawable = True

  def inBox(self, pos):
    return self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height

  def setPos(self, x, y):
    self.x = x
    self.y = y
  def setX(self, x):
    self.x = x
  def setY(self, y):
    self.y = y

  def getPos(self):
    return self.x, self.y

  def draw(self):
    raise Exception("Draw not implimented")

class Text(Element):

  def __init__(self, x, y, text, fontName, size, colour):
    
    self.text = text
    self.fontName = fontName
    self.size = size
    self.colour = colour

    self.render()

    super().__init__(x, y, self.renderedText.get_width(), self.renderedText.get_height())

  def getText(self):
    return self.renderedText

  def render(self):
    self.font = pygame.font.SysFont(self.fontName, self.size)
    self.renderedText = self.font.render(self.text, True, self.colour)

  def draw(self, screen):
    screen.blit(self.renderedText, self.getPos())

class Rect(Element):

  def __init__(self, x, y, width, height, colour):
    super().__init__(x, y, width, height)
    self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    self.colour = colour
    
  def update(self):
    self.rect.x = self.x
    self.rect.y = self.y
    self.rect.width = self.width
    self.rect.height = self.height

class OutlineRect(Rect):
  def draw(self, screen):
    pygame.draw.rect(screen, self.colour, self.rect, 2)

class FilledRect(Rect):  
  def draw(self, screen):
    pygame.draw.rect(screen, self.colour, self.rect, 0)

class Button(FilledRect):

  def __init__(self, x, y, width, height, colour, text, textColour, fontName, size, cooldownCounter=10):
    super().__init__(x, y, width, height, colour)
    self.onCooldown = False
    self.cooldownCounter = cooldownCounter
    self.maxCount = cooldownCounter

    self.text = Text(self.x, self.y, text, fontName, size, textColour)
    self.text.setPos(
      self.x + (self.width / 2 - self.text.width / 2),
      self.y + (self.height / 2 - self.text.height / 2)
    )

    if self.text.width > self.width:
      self.width = self.text.width + 2

  def onPress(self, function, mousePos, mouseButtons):
    if (self.inBox(mousePos) and mouseButtons[0] and not self.onCooldown):
      function()
      self.onCooldown = True
      self.cooldownCounter = self.maxCount

    if self.onCooldown:
      self.cooldownCounter -= 1
      if self.cooldownCounter == 0:
        self.onCooldown = False

  def draw(self, screen):
    pygame.draw.rect(screen, self.colour, self.rect, 0)
    self.text.draw(screen)

  def update(self):
    super().update()
    self.text.setPos(
      self.x + (self.width / 2 - self.text.width / 2),
      self.y + (self.height / 2 - self.text.height / 2)
    )

