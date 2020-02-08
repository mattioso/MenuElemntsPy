
from menuAid import *

m = Menu(600, 600, (60, 60, 60))

m.text = Text(0, 0, "Text Example", "arial", 20, (255, 255, 255))

while 1:

  m.draw()

  m.screen.blit(m.text.getText(), m.text.getPos())

  m.update()