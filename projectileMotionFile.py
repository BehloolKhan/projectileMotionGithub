#import all required libraries
import pygame #for rendering and display
import numpy #for physics/maths
import matplotlib #for graphs
import math #for projectile calculations

class Ball(pygame.sprite.Sprite):

    #down = positive, due to pygame co-ordinate system

    _mass = 10 #mass 10 KG
    _accelerationDueToWeight = 9.81

    def __init__(self, surfaceOfBall: pygame.Surface, colorOfBall:tuple, center:pygame.Vector2, radius, initialVelocity:int, angle:int, k=0):

        #invoke constructor method of parent class

        super().__init__()

        self.color = colorOfBall
        self.radius = radius
        self.center = center
        self.surface = surfaceOfBall
        self.K = k #by defualt, this value is 0
        self.verticalAcceleration = 9.81 #starting acceleration
        self.horizontalAcceleration = 0 #starting acceleration

        #need to convert angle value into radians
        angle = ((numpy.pi) / 180) * angle

        self.speed_horizontal = initialVelocity*math.cos(angle)
        self.speed_vertical = -initialVelocity*math.sin(angle)
        self.scale_factor = 10 #10 pixels = 1 meter

        self.line_scale_factor = 4 #4 pixels = one meter
        
        pygame.draw.circle(self.surface, self.color, self.center, self.radius)

    def getUpdatedAcceleration(self):
        
        overallAcceleration = (self.verticalAcceleration**2) + (self.horizontalAcceleration**2)
        overallAcceleration = math.sqrt(overallAcceleration)

        return overallAcceleration


    def update(self, time):
        #update the co-ordinates
        self.center.x += time*self.speed_horizontal*self.scale_factor
        self.center.y += self.speed_vertical*time*self.scale_factor
        
        #update the velocity:
        #need access to k value
        #need access to current velocity
        #F = -KV
        resistiveHorizontal = -self.K*self.speed_horizontal
        resistiveVertical = -self.K*self.speed_vertical

        #take into account weight now aswell
        resistiveVertical += (Ball._accelerationDueToWeight*Ball._mass)

        #now we need to update the respective vertical and horizontal components of speed
        self.horizontalAcceleration = resistiveHorizontal/Ball._mass
        self.verticalAcceleration = resistiveVertical/Ball._mass

        self.speed_horizontal += (self.horizontalAcceleration*time)
        self.speed_vertical += (self.verticalAcceleration*time) # That is now done

    def draw(self, surfaceOfBall):

        pygame.draw.circle(self.surface, self.color, self.center, self.radius)

        #we are going to draw a line
        #what will happen is that the starting point = center

        verticalVelocityVector = self.center + pygame.Vector2(0, self.speed_vertical*self.line_scale_factor)
        pygame.draw.line(self.surface, (255, 255, 255), self.center, verticalVelocityVector, 5)

        horizontalVelocityVector = self.center + pygame.Vector2(self.speed_horizontal*self.line_scale_factor, 0)
        pygame.draw.line(self.surface, (0, 255, 0), self.center, horizontalVelocityVector, 5)

        velocityVector = self.center + pygame.Vector2(self.speed_horizontal*self.line_scale_factor, self.speed_vertical*self.line_scale_factor)
        pygame.draw.line(self.surface, (255, 0, 0), self.center, velocityVector, 5)

        #draw the acceleration aswell

        accelerationVector = self.center + (pygame.Vector2(self.line_scale_factor*self.horizontalAcceleration, self.line_scale_factor*self.verticalAcceleration)) #scale the vector by a half
        pygame.draw.line(self.surface, (255, 0, 255), self.center, accelerationVector, 5)


#set up the dimensions of screen and everything

def displayProperties(destination: pygame.Surface, text:str, font:pygame.font.Font, textColor, topLeftX, topLeftY):

    ballProperites = font.render(text, True, textColor, (255, 255, 255)) # returns a surface, so need to blit on to another surface
    destination.blit(ballProperites, (topLeftX, topLeftY))

def mainGameLoop(initialVelocity, angle, k=0):

    pygame.init()

    bg_colour = (0, 0, 0) # Black
    BLUE_COLOUR = (0, 0, 255) # blue

    SCREEN_WIDTH = 1400
    SCREEN_HEIGHT = 800

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(bg_colour) #specify the color over here

    ball_radius = 20
    ball_centre = pygame.Vector2(20.0, SCREEN_HEIGHT/2)

    ball = Ball(screen, BLUE_COLOUR, ball_centre, ball_radius, initialVelocity, angle, k) #draw the circle
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
        textProperties = f"vertical velocity: {-ball.speed_vertical}"
        displayProperties(screen, textProperties, font, (0, 0, 0), 0, SCREEN_HEIGHT-70)
        textProperties = f"time: {cumulativeTime} seconds"
        displayProperties(screen, textProperties, font, (0, 0, 0), 0, SCREEN_HEIGHT-40)
        textProperties = f"overall maginitude of acceleration: {ball.getUpdatedAcceleration()} ms^-2"
        displayProperties(screen, textProperties, font, (0, 0, 0), 0, SCREEN_HEIGHT-130)


        pygame.display.flip() #update the display

        change_time = Clock.tick(100) #lets see what happens when u increase it
        change_time = change_time / 1000 #convert it to seconds
        ball.update(change_time)

        cumulativeTime+=change_time
    
    pygame.quit() #show down the pyagme window from here

if __name__ == "__main__":
    mainGameLoop(30, 30, 4)