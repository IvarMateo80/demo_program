#define class 'game'
#__init__ methodo initializer 
#methods are special functions defined 
import pygame

class Game: 
    #__init__ is initialization only. MUST not contain an infinite loop
    def __init__(self, caption="My First Game", screen_width=640, screen_height=480):
        print('initializing game attributes')
        pygame.init()
        #create the game window (screen)
        pygame.display.set_caption(caption)
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.screen_width = screen_width
        self.screen_height = screen_height

        #this is the start position (self.circle_x = self.screen_height // 2, self.circle_y = self.screen_width // 2)
        self.circle_x = self.screen_height // 2
        self.circle_y = self.screen_width // 2
        
        self.circle_x_factor = 5
        self.circle_y_factor = 5
        self.circle_radius = 20
        
        self.keep_screen_open = True

    #this methos has the GAME SCREEN OPEN > "GAME LOOP = while true"
    def run(self):
        print("this is the game run method")
        while self.keep_screen_open: 
            print("the game is running")
            self.capture_event()
            self.update()
            self.draw()
        else:
            print("quit game because self.keep_screen_open is", self.keep_screen_open)
            pygame.quit() #cleaning pygame 
    
    def capture_event(self):
        #get events from pygame, and loop to get each event
        for event in pygame.event.get():
            #ask pygame if event ocurred
            if event.type == pygame.QUIT:
                print("received.event.type", event.type, "that indicates close screen")
                self.keep_screen_open = False
    
    #cambiar el estado interno del juego basado en el input del jugador, logica interna del juego, etc
    def update(self):
        user_input = pygame.key.get_pressed()
        if user_input[pygame.K_SPACE]:
            self.circle_x = self.screen_height // 2
            self.circle_y = self.screen_width // 2
            self.circle_x_factor = 0
            self.circle_y_factor = 0
        

    def draw_circle(self):
        #user_input = pygame.key.get_pressed()
        #if user_input[pygame.K_SPACE]:
            #self.circle_x = self.screen_height // 2
            #self.circle_y = self.screen_width // 2
            #self.circle_x_factor = 0
            #self.circle_y_factor = 0
        #move the circle before drwaing it
        #else:
        self.circle_x += self.circle_x_factor
        self.circle_y += self.circle_y_factor

        #verify if circle i inside the screen limits (top, button, left, rigth)
        #and make decision to avoid falling outside the limits
        if self.circle_x - self.circle_radius < 0 or self.circle_x + self.circle_radius > self.screen_width:
            self.circle_x_factor = -self.circle_x_factor

        if self.circle_y - self.circle_radius < 0 or self.circle_y + self.circle_radius > self.screen_height:
            self.circle_y_factor = -self.circle_y_factor

        #draw the circle
        circle_color = (255, 0, 0)
        pygame.draw.circle(self.screen, circle_color, (self.circle_x, self.circle_y), self.circle_radius)
    
    #renderizar (dibujaro hacer que la pantalla se actualize) el caambio de pantalla
    def draw(self):
        #change the screen panel to white
        self.screen.fill((255, 255, 255))
        
        
        self.draw_circle()
        pygame.display.flip()
        #20 miliseconds equivale mas o menos a 50 refresh de pantalla
        pygame.time.delay(20) #nos dormimos durante 20 milisegundos antes de hacer el siguiente ciclo