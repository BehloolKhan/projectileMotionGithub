#import all required libraries
import pygame #for rendering and display
import numpy #for physics/maths
import matplotlib #for graphs
import math #for projectile calculations

class Ball(pygame.sprite.Sprite):

    #down = positive, due to pygame co-ordinate system

    acc = -9.81

    def __init__(self, surfaceOfBall: pygame.Surface, colorOfBall:tuple, center:pygame.Vector2, radius, initialVelocity:int, angle:int):

        #invoke constructor method of parent class

        super().__init__()
        self.color = colorOfBall
        self.radius = radius
        self.center = center
        self.surface = surfaceOfBall

        #need to convert angle value into radians
        angle = ((numpy.pi) / 180) * angle

        self.speed_horizontal = initialVelocity*math.cos(angle)
        self.speed_vertical = initialVelocity*math.sin(angle)
        self.scale_factor = 10 #10 pixels = 1 meter

        self.line_scale_factor = 4
        
        pygame.draw.circle(self.surface, self.color, self.center, self.radius)


    def update(self, time):
        #update the co-ordinates
        self.center.x += time*self.speed_horizontal*self.scale_factor
        self.center.y += -self.speed_vertical*time*self.scale_factor
        
        #update the velocity:
        #horizontal remains the same
        #vertical changes
        self.speed_vertical = (self.speed_vertical) + Ball.acc*time

    def draw(self, surfaceOfBall):

        pygame.draw.circle(self.surface, self.color, self.center, self.radius)

        #we are going to draw a line
        #what will happen is that the starting point = center

        verticalVelocityVector = self.center + pygame.Vector2(0, -self.speed_vertical*self.line_scale_factor)
        pygame.draw.line(self.surface, (255, 255, 255), self.center, verticalVelocityVector, 5)

        horizontalVelocityVector = self.center + pygame.Vector2(self.speed_horizontal*self.line_scale_factor, 0)
        pygame.draw.line(self.surface, (0, 255, 0), self.center, horizontalVelocityVector, 5)

        velocityVector = self.center + pygame.Vector2(self.speed_horizontal*self.line_scale_factor, -self.speed_vertical*self.line_scale_factor)
        pygame.draw.line(self.surface, (255, 0, 0), self.center, velocityVector, 5)

        #draw the acceleration aswell

        accelerationVector = self.center + (pygame.Vector2(0, -Ball.acc)) #scale the vector by a half
        pygame.draw.line(self.surface, (255, 0, 255), self.center, accelerationVector, 5)


#set up the dimensions of screen and everything

def displayProperties(destination: pygame.Surface, text:str, font:pygame.font.Font, textColor, topLeftX, topLeftY):

    ballProperites = font.render(text, True, textColor, (255, 255, 255)) # returns a surface, so need to blit on to another surface
    destination.blit(ballProperites, (topLeftX, topLeftY))

def mainGameLoop(initialVelocity, angle):

    pygame.init()

    bg_colour = (0, 0, 0) # Black
    BLUE_COLOUR = (0, 0, 255) # blue

    SCREEN_WIDTH = 1400
    SCREEN_HEIGHT = 800

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(bg_colour) #specify the color over here

    ball_radius = 20
    ball_centre = pygame.Vector2(20.0, SCREEN_HEIGHT/2)

    ball = Ball(screen, BLUE_COLOUR, ball_centre, ball_radius, initialVelocity, angle) #draw the circle
    Clock = pygame.time.Clock()

    cumulativeTime = 0 #keeps track of total seconds passed so far in seconds

    running = True

    while running:

        screen.fill(bg_colour) #it will get wiped out by this

        for event in pygame.event.get():

            if (event.type == pygame.QUIT):

                running = False

            elif (event.type == pygame.KEYDOWN):

                if (event.key == pygame.K_ESCAPE):

                    running = False

        
        ball.draw(screen) #draw the ball
        font = pygame.font.SysFont("Ariel", 30)
        textProperties = f"horizontal velocity: {ball.speed_horizontal} "
        displayProperties(screen, textProperties, font, (0, 0, 0), 0, SCREEN_HEIGHT-100)
        textProperties = f"vertical velocity: {ball.speed_vertical}"
        displayProperties(screen, textProperties, font, (0, 0, 0), 0, SCREEN_HEIGHT-70)
        textProperties = f"time: {cumulativeTime} seconds"
        displayProperties(screen, textProperties, font, (0, 0, 0), 0, SCREEN_HEIGHT-40)

        pygame.display.flip() #update the display

        change_time = Clock.tick(100) #lets see what happens when u increase it
        change_time = change_time / 1000 #convert it to seconds
        ball.update(change_time)

        cumulativeTime+=change_time
    
    pygame.quit() #show down the pyagme window from here

if __name__ == "__main__":
    mainGameLoop(30, 30)