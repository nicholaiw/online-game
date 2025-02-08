from variables import *
import pathlib

def loadFont(font):
    currentFile = pathlib.Path(__file__)
    fontDirectory = currentFile.parent / "assets" / "fonts"
    fontPath = fontDirectory / f"{font}.ttf"
    return str(fontPath)


font = pygame.font.Font(loadFont('font'), 40)


def drawText(text, font, color, x , y):
    textSurface = font.render(text, True, color)
    screen.blit(textSurface, textSurface.get_rect(center=(x, y)))

class Button:
    def __init__(self, x, y, w, h, type, state=None):
        self.rect = pygame.Rect(x, y, w, h)
        self.type = type
        self.state = state
        self.pressed = False

    def actions(self, data=None):
        mousePressed = pygame.mouse.get_pressed()[0]
        mousePos = pygame.mouse.get_pos()

        if mousePressed and self.rect.collidepoint(mousePos) and not self.pressed:
            self.pressed = True

            if self.type == "changeState":
                activeStates.clear()
                activeStates.append(self.state)
            
            elif self.type == "addState":
                activeStates.append(self.state)

            elif self.type == "removeState":
                activeStates.remove(self.state)
            
            elif self.type == "createGame" or self.type == "joinGame":
                print(f"{self.type};{data}")
                network.sendData(f"{self.type};{data}")

        elif not mousePressed:
            self.pressed = False
                    

    def draw(self):
        pass
        pygame.draw.rect(screen, "#444477", self.rect)

class InputField:

    def __init__(self, x, y, w, h, text='', color="#ffffff", limit=False):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.text = text
        self.textSurface = font.render(text, True, self.color)
        self.active = False
        self.limit = limit
        self.pressedKeys = set()
        

    def actions(self):
        keys = pygame.key.get_pressed()

        if pygame.mouse.get_pressed()[0]:
            mousePos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mousePos):
                self.active = True
            else:
                self.active = False

        if self.active:
            if keys[pygame.K_RETURN] and pygame.K_RETURN not in self.pressedKeys:
                print(self.text)
                self.text = ''
                self.pressedKeys.add(pygame.K_RETURN)
            elif keys[pygame.K_BACKSPACE] and pygame.K_BACKSPACE not in self.pressedKeys:
                self.text = self.text[:-1]
                self.pressedKeys.add(pygame.K_BACKSPACE)
            else:
                for i in range(pygame.K_a, pygame.K_z + 1):
                    if keys[i] and i not in self.pressedKeys:
                        char = pygame.key.name(i)
                        if len(self.text) < self.limit or self.limit == False:
                            self.text += char
                        self.pressedKeys.add(i)

        for i in list(self.pressedKeys):
            if not keys[i]:
                self.pressedKeys.remove(i)

        self.textSurface = font.render(self.text, True,  self.color)


    def draw(self):
        screen.blit(self.textSurface, (self.rect.x + (self.rect.width - self.textSurface.get_width()) // 2,  
                                       self.rect.y + 4 + (self.rect.height - self.textSurface.get_height()) // 2))
       #pygame.draw.rect(screen, self.color, self.rect, 2)


