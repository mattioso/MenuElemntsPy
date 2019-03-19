
#Create a funtion that will return if a point is in a rectangle
#Parameters: int x, int y, int width, int heigh, touple/list pos)
def inBox(x, y, width, height, pos):
	#Returns True if the
	return x < pos[0] < x + width and y < pos[1] < y + height

class Menu(object):
		
	def createButton(self, name, x, y, imgList, buttonType=0):
		vars(self)[name] = Button(x, y, imgList, buttonType)
		
	def createDropdown(self, name, x, y, dropdownButton, buttonList):
		
		vars(self)[name] = DropdownMenu(x, y, dropdownButton, buttonList)

	def createInputTextBox(self, name, x, y, width, height, pygame, colourList, textSize):
		vars(self)[name] = InputTextbox(x, y, width, height, pygame, colourList, textSize)

	def createImage(self, name, imgLoc, x, y, pygame):
		vars(self)[name] = Image(imgLoc, x, y, pygame)

class DropdownMenu(object):
	
	def __init__(self, x, y, dropdownButtonImages, buttonImagesList):
		
		self.x = x
		self.y = y
		
		self.dropdownX = 0
		self.dropdownY = 0
		self.dropdownWidth = 0
		self.dropdownHeight = 0
		
		self.mainButton = Button(self.x, self.y, dropdownButtonImages, 1)
		
		self.buttonY = self.y + self.mainButton.height
		
		self.buttons = []
		
		for x in range(len(buttonImagesList)):
			
			self.buttons.append(Button(self.x, self.buttonY, buttonImagesList[x]))
			self.buttonY += self.buttons[x].height
			self.dropdownHeight += self.buttons[x].height
			
		self.dropdownWidth = self.buttons[0].width
		self.dropdownX = self.buttons[0].x
		self.dropdownY = self.buttons[0].y
		
		self.dropdownBox = [self.dropdownX, self.dropdownY, self.dropdownWidth, self.dropdownHeight]
			
		self.active = False
		
	def update(self, mousePos, pressedMouseButtons):
		
		self.mainButton.update(mousePos, 0, self.dropdownBox)
		
		self.active = self.mainButton.active
		
		if self.mainButton.active:
			for button in self.buttons:
				button.update(mousePos, pressedMouseButtons)

class Button(object):
	
	def __init__(self, x, y, imgList, buttonType=0):
		
		self.buttonType = buttonType
		
		self.x = x
		self.y = y
		
		if self.buttonType == 0:
			self.images = imgList
			self.currentImage = None
			
			self.isPressed = False
			
			if type(self.images) is list:
				if len(self.images) == 3:
					self.image = self.images[0]
					self.hoveredImage = self.images[1]
					self.pressedImage = self.images[2]
				else:
					raise ValueError('List does not have three elements')
			else:
				raise TypeError('Not a list for the images')
				
				
			self.width = self.images[0].get_width()
			self.height = self.images[0].get_height()
			
			self.currentImage = self.image
			
		elif self.buttonType == 1:
			
			self.images = imgList
			self.currentImage = None
			
			self.active = False
			
			if type(self.images) is list:
				if len(self.images) == 2:
					self.image = self.images[0]
					self.hoverImage = self.images[1]
					
				else:
					raise ValueError('Wrong type')
			else:
				raise TypeError('Not a list')
				
			self.width = self.images[0].get_width()
			self.height = self.images[0].get_height()
				
			self.currentImage = self.image
				
	def update(self, mousePos, pressedMouseButtons, dropdownBox=0):
		
		if self.buttonType == 0:
		
			if inBox(self.x, self.y, self.width, self.height, mousePos):
				if pressedMouseButtons[0] == 1:
					self.currentImage = self.pressedImage
					self.isPressed = True
				elif pressedMouseButtons[0] == 0:
					self.currentImage = self.hoveredImage
					self.isPressed = False
			else:
				self.currentImage = self.image
				self.isPressed = False
				
		elif self.buttonType == 1:
			
			self.active = False
			
			if inBox(self.x, self.y, self.width, self.height, mousePos) or inBox(dropdownBox[0], dropdownBox[1], dropdownBox[2], dropdownBox[3], mousePos):
				self.currentImage = self.hoverImage
				self.active = True
			else:
				self.currentImage = self.image
				self.acive = False

	def returnCords(self):
		return (self.x, self.y)

	def returnX(self):
		return self.x

	def returnY(self):
		return self.y

	def returnWidth(self):
		return self.currentImage.get_size()[0]

	def returnHeight(self):
		return self.currentImage.get_size()[1]

	def returnDimensions(self):
		return self.currentImage.get_size()

	def setCords(self, x, y):
		self.x = x
		self.y = y

class InputTextbox(object):

	def __init__(self, x, y, width, height, pygame, colourList, textSize):

		self.x = x
		self.y = y
		self.width = width
		self.height = height

		self.active = False

		self.input_box = pygame.Rect(x, y, width, height)

		self.text = ""

		self.colours = colourList
		self.colour = self.colours[0]

		self.textSize = textSize
		self.font = pygame.font.Font(None, textSize)

	def checkInput(self, event, mousePos, pygame):

		if event.type == pygame.MOUSEBUTTONDOWN:

			if inBox(self.x, self.y, self.width, self.height, mousePos):
				self.active = not self.active
			else:
				self.active = False

		if event.type == pygame.KEYDOWN:
			if self.active:
				if event.key == pygame.K_RETURN:
					pass
				elif event.key == pygame.K_BACKSPACE:
					self.text = self.text[:-1]
				else:
					self.text += event.unicode

	def draw(self, screen, pygame):

		if self.active:
			self.colour = self.colours[0]

		else:
			self.colour = self.colours[1]

		self.renderedText = self.font.render(self.text, True, self.colour)

		if self.renderedText.get_width() + 10 > self.width:
			self.text = self.text[:-1]

		self.input_box = pygame.Rect(self.x, self.y, self.width, self.height)
		self.input_box.w = self.width + 5

		screen.blit(self.renderedText, (self.input_box.x + 5, self.input_box.y + 5))

		pygame.draw.rect(screen, self.colour, self.input_box, 2)

	def returnString(self):

		if not self.active and self.text == "":
			return None
		elif self.active:
			return None
		else:
			return self.text

	def setPos(self, x, y):
		self.x = x
		self.y = y

class Image(object):

	def __init__(self, imgLoc, x, y, pygame):

		self.image = pygame.image.load(imgLoc)
		self.x = x
		self.y = y
		self.size = self.width, self.height = self.image.get_size()

	def draw(self, screen):

		screen.blit(self.image, (self.x, self.y))

	def setPos(self, x, y):

		self.x = x
		self.y = y

class Text(object):

	def __init__(self, text, x, y, colour, size, pygame):

		self.font = pygame.font.Font(None, size)
		self.x = x
		self.y = y
		self.colour = colour
		self.text = text
		self.renderedText = self.font.render(self.text, True, self.colour)
		self.width = self.renderedText.get_width()
		self.height = self.renderedText.get_height()

	def returnCords(self):

		return (self.x, self.y)

	def setPos(self, x, y):
		self.x = x
		self.y = y
