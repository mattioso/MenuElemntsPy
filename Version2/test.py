
from menuAid import *

m = Menu(600, 600, (60, 60, 60))

m.testText = Text(0, 0, "Test", "arial", 20, (255, 255, 255))
m.testOutlineRect = OutlineRect(50, 0, 50, 50, (0, 0, 0))
m.testFilledRect = FilledRect(100, 0, 50, 50, (0, 0, 0))

while 1:
  m.draw()

  m.screen.blit(m.testText.getText(), m.testText.getPos())
  m.testOutlineRect.draw(m.screen)
  m.testFilledRect.draw(m.screen)

  m.update()