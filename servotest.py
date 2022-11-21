#testing out basic servos (180 degree turning functionality
#using a tutorial ( https://www.youtube.com/watch?v=xHDT4CwjUQE )
#will create a pygame window, displaying both startservo and stopservo
#startservo will of course start the servo, and stopservo will stop all servos from moving.

#imported libraries neccesary for code
import RPi.GPIO as GPIO
import time
import pygame
import sys

#define colors for pygame to reference later
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
 
# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 32)
 
# create a text surface object,
# on which text is drawn on it.
text = font.render('Servos = On', True, green, blue)
 
# create a rectangular object for the
# text surface object
textRect = text.get_rect()
 
# set the center of the rectangular object.
textRect.center = (100 // 2, 100 // 2)

#pygame init, creates a pygame window to allow starting and stopping of servos by pressing keys
pygame.init()  

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pin 11 as an output, and set servo1 as pin 11 as PWM
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50) # Note 11 is pin, 50 = 50Hz pulse

#creates pygame window
# Define the dimensions of
# screen object(width,height)
screen = pygame.display.set_mode((500, 350))
  
# Set the caption of the screen
pygame.display.set_caption('Servo Control')
  
# Update the display using flip
pygame.display.flip()

#pygame things, creates a window titled "servo control" and if s is pressed stops servos
while True:
       
    # creating a loop to check events that
    # are occurring
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         
        # checking if keydown event happened or not
        if event.type == pygame.KEYDOWN:
               
            #stops active servos, exits pygame
            if event.key == pygame.K_a:
                servo1.stop()
                text = font.render('Servos = off', True, green, blue)
                print("Servos Off")
                GPIO.cleanup()
                print("Goodbye")
                exit()
                
                
               
           
               
            