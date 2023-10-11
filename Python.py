import pygame
pygame.init()#initializes Pygame
pygame.display.set_caption("python piano program")#sets the window title
screen = pygame.display.set_mode((800, 800))#creates game screen
xpos = 0
ypos = 0
mousePos = (xpos, ypos) #variable mousePos stores TWO numbers
press = False

#audio stuff!
pygame.mixer.init()
k1 = pygame.mixer.Sound("key01.mp3")
k2 = pygame.mixer.Sound("key02.mp3")
k3 = pygame.mixer.Sound("key03.mp3")


#this holds onto what key the user has pressed
key = 0

class Key():
    def __init__(self,xpos, n):
        self.xpos = xpos
        self.num = n
        
    def click(self):
        pygame.draw.rect(screen, (150,150,150), (self.xpos,500,100,300))
        return self.num
            
    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), (self.xpos, 500, 100, 300))
        
        pygame.draw.rect(screen, (0, 0, 0), (self.xpos + 100, 500, 100, 300), 2)
        

    
        
painokey1 = Key(0, 1)
painokey2 = Key(100,2)
painokey3 = Key(200,3)
#gameloop###################################################
while True:
    print(mousePos) #this is just for testing so you can see the mouse coordinates on the screen!
    
    #event queue (bucket that holds stuff that happens in game and passes to one of the sections below)
    event = pygame.event.wait()
    
    #input section----------------------------------------------
    if event.type == pygame.QUIT: #close game window
        break

    if event.type == pygame.MOUSEBUTTONDOWN:
        press = True

    if event.type == pygame.MOUSEBUTTONUP:
        press = False

    if event.type == pygame.MOUSEMOTION:
        mousePos = event.pos
    
    
    painokey1.draw()
    painokey2.draw()
    painokey3.draw()
    if press == True:
        if mousePos[0] > 0 and mousePos[0] < 100 and mousePos[1] >500:
                key = painokey1.click()
                pygame.mixer.Sound.play(k1)
        elif mousePos[0] > 100 and mousePos[0] < 200 and mousePos[1] >500:
                key = painokey2.click()
                pygame.mixer.Sound.play(k2)
        elif mousePos[0] > 200 and mousePos[0] < 300 and mousePos[1] >500:
                key = painokey3.click()
                pygame.mixer.Sound.play(k3)
    
    
    
    
    


    #render section---------------------------------------------
    
    

    
    pygame.display.flip() #always needed at the end of every game loop!
    

#end game loop##############################################

pygame.quit()
