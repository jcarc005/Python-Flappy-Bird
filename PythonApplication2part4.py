
#we first import pygamee library
import pygame
import random 

#initialize pygame
pygame.init()

#define colors
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)

#define screen size
size = (700,500)
screen = pygame.display.set_mode(size)

#define screen title 
pygame.display.set_caption("Flappy bird")

#boolean T/F to control game logic
done = False
#clock to control game refresh speed
clock = pygame.time.Clock()

x = 350
y = 250

#define global variables to control speed
x_speed = 0
y_speed = 0

#define global variable position for the ground
#sinde vertical "size' equals 500, defined above, and
#ball size is 20 as defined in 'ball' defining function
#and -3 pixel correction
ground = 477

#x axis location of obstacle
xloc=700
#y axis location of obstacle
yloc=0
#how wide we want obstacle
xsize = 70
#how randomly tall it is
ysize = random.randint(0,350)
#space between two blocks
space = 150
#the speed of the obstacle as they move across the screen
#pixels per frame/flip
obspeed = 2.5
score = 0

#we proceed to define our obstacles
def obstacles(xloc,yloc,xsize,ysize):
    pygame.draw.rect(screen, green, [xloc,yloc,xsize,ysize])
    pygame.draw.rect(screen, green, [xloc, int(yloc+ysize+space), xsize, ysize+500])


#define function to draw circle
def ball(x,y):
    pygame.draw.circle(screen,black,(x,y),20)

#define function to handle game over event
def gameover():
    font = pygame.font.SysFont(None,75)
    text = font.render("Game Over", True, red)
    screen.blit(text, [150,250])

def Score(score):
    font = pygame.font.SysFont(None,75)
    #we use str to convert score value to string for display
    text = font.render("Score: " + str(score), True,black)
    #top left corner coordinates
    screen.blit(text,[0,0])

#while logic to keep game running
while not done:
    #capture input events so we act upon them
    for event in pygame.event.get():
        #if user select 'ESC' key or presses windows 'X' top right button
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_speed = -10

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                y_speed = 5

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x_speed = 2

    #fill screen with color defined above
    screen.fill(white)
    #time to draw obstacles
    obstacles(xloc,yloc,xsize,ysize)
    #call function to draw the ball
    ball(x,y)
    #if the ball is between to obstacles
    Score(score)
    #adjust vertical y position
    y += y_speed
    #time to redefine per refresh new x location
    xloc -= obspeed
    #adjust horizontal x position
    x += x_speed
    #once 'y' is changes check if ground is touches hence game over
    if y > ground:
        gameover()
        #to stop the ball
        y_speed = 0
        #if we hit the ground obstacles stops
        obspeed = 0
    #if we hit obstacles in the top block
    if x+20 > xloc and y-20 < ysize and x-15 < xsize+xloc:
        gameover()
        obspeed = 0
        y_speed = -2
    #if we hit obstacles in the the bottom block
    if x+20 > xloc and y+20 > ysize+space and x-15 < xsize+xloc:
        gameover()
        obspeed = 0
        y_speed = -2
    #if obstacle location x is
    if xloc < -80:
        xloc = 700
        ysize = random.randint(0,350)
    #check if obstacle was passed adding to score
    if x > xloc and x < xloc+3:
        score = (score +1)
    #refresh screen by flipping like a flipbook new animation
    pygame.display.flip()
    #define times per second this will happen via clock defined above
    clock.tick(60)


            #once logic loop end exit game 
pygame.quit()
