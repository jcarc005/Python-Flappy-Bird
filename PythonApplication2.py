
#we first import pygamee library
import pygame

#initialize pygame
pygame.init()

#define colors
black = (0,0,0)
white = (255,255,255)

#define screen size
size = (500,700)
screen = pygame.display.set_mode(size)

#define screen title 
pygame.display.set_caption("Flappy bird")

#boolean T/F to control game logic
done = False
#clock to control game refresh speed
clock = pygame.time.Clock()

#while logic to keep game running
while not done:
    #capture input events so we act upon them
    for event in pygame.event.get():
        #if user select 'ESC' key or presses windows 'X' top right button
        if event.type == pygame.QUIT:
            done = True
    #fill screen with color defined above
    screen.fill(white)
    #refresh screen by flipping like a flipbook new animation
    pygame.display.flip()
    #define times per second this will happen via clock defined above
    clock.tick(60)


            #once logic loop end exit game 
pygame.quit()
