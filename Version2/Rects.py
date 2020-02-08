
from menuAid import *

def clickFunction():
  m.button.x += 10

m = Menu(600, 600, (60, 60, 60))

m.rect1 = OutlineRect(0, 0, 49, 49, (255, 0, 0))
m.rect2 = FilledRect(50, 0, 50, 50, (0, 255, 0))
m.button = Button(100, 0, 50, 50, (0, 0, 255), "Button", (0, 0, 0), "arial", 20)

while 1:

  m.rect1.update()
  m.rect2.update()
  m.button.update()

  m.button.onPress(clickFunction, m.getMousePos(), m.getMouseButtons())

  m.draw()

  m.rect1.draw(m.screen)
  m.rect2.draw(m.screen)
  m.button.draw(m.screen)

  m.update()