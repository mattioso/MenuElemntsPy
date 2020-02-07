
from menuAid import *

m = Menu(600, 600, (60, 60, 60))

m.testText = Text(0, 0, "Test", "arial", 20, (255, 255, 255))

while 1:
  m.draw()

  m.screen.blit(m.testText.getText(), m.testText.getPos())

  m.update()