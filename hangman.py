import random, sys, pygame
from pygame.locals import *

# List of possible words that could be selected
WORD_BANK = ["apple", "banana", "carrot", "eggplant", "watermelon", "lemon", "pumpkin", "peaches", "corn", "strawberry","cherry", "orange", "onion", "pineapple", "kiwi", "lettuce", "peas", "spinach", "plum" ]

# This chooses the random word
random.shuffle(WORD_BANK)
WORD = WORD_BANK[0]

pygame.init()
# VARIABLES 
WIDTH = 600     # Width of game window
HEIGHT = 600    # Height of game window   
PADDING = 15    # Variable that creates a margin in the game window, also 
                # used for drawing lines
# Colors used 
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

LINE_WIDTH = 5      # Width of line for hanger
HEAD_RAD = int(HEIGHT / 25) # Radius of head 
BODY_LINE_WIDTH = 3       

# Assigns important colors

BACKGROUND_COLOR = WHITE
HANGER_COLOR = BLACK
WIN_COLOR = GREEN
INCORRECT_COLOR = RED

DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
# Hanger points

H_A = (PADDING + int(WIDTH/4),int(HEIGHT/2))
H_B = (H_A[0], int(HEIGHT/6))
H_C = (int(WIDTH/2), H_B[1])
H_D = (int(WIDTH/6), H_A[1])
H_E = (H_A[0] + (H_A[0] - H_D[0]), H_D[1])
H_F = (H_C[0], int(HEIGHT/25) + H_B[1])

# Body points
B_HEAD = (H_F[0], H_F[1] + HEAD_RAD)
B_BODY_1 = (H_F[0], H_F[1] + 2 * HEAD_RAD)
B_BODY_2 = (H_F[0], int(0.8 * H_A[1]))
B_R_ARM_1 = (H_F[0], int(0.6 * H_A[1]) )  # Body right arm point 1
B_R_ARM_2 = (int(H_F[0] * 1.1), int(0.7 * H_A[1])) # Body right arm point 2
B_L_ARM_1 = (H_F[0], int(0.6 * H_A[1]) )
B_L_ARM_2 = (int(H_F[0] * 0.9), int(0.7 * H_A[1]))
B_R_LEG_1 = (H_F[0],int(0.8 * H_A[1]))
B_R_LEG_2 = (int(H_F[0] * 1.1), int(0.9 * H_A[1]))
B_L_LEG_1 = (H_F[0],int(0.8 * H_A[1]))
B_L_LEG_2 = (int(H_F[0] * 0.9), int(0.9 * H_A[1]))


# Name:       drawHanger()
# Purpose:    Draws the hanger on the game window, in the color BLACK
# Parameters: None
# Returns:    Nothing 
def drawHanger():
    pygame.draw.line(DISPLAY, HANGER_COLOR, H_A,H_B, LINE_WIDTH)
    pygame.draw.line(DISPLAY, HANGER_COLOR, H_B,H_C, LINE_WIDTH)
    pygame.draw.line(DISPLAY, HANGER_COLOR, H_C,H_F, LINE_WIDTH)
    pygame.draw.line(DISPLAY, HANGER_COLOR, H_E,H_D, LINE_WIDTH)


# The following one line functions are used to draw individual body parts
# , so that we can draw the body parts in a sequential order, in the function
# drawBodyParts()
def drawHead():
    pygame.draw.circle(DISPLAY, BLACK, B_HEAD, HEAD_RAD, BODY_LINE_WIDTH)
def drawBody():
    pygame.draw.line(DISPLAY, BLACK, B_BODY_1, B_BODY_2, BODY_LINE_WIDTH)
def drawRightArm():
    pygame.draw.line(DISPLAY, BLACK, B_R_ARM_1, B_R_ARM_2, BODY_LINE_WIDTH)
def drawLeftArm():
    pygame.draw.line(DISPLAY, BLACK, B_L_ARM_1, B_L_ARM_2, BODY_LINE_WIDTH)
def drawRightLeg():
    pygame.draw.line(DISPLAY, BLACK, B_R_LEG_1, B_R_LEG_2, BODY_LINE_WIDTH)
def drawLeftLeg():
    pygame.draw.line(DISPLAY, BLACK, B_L_LEG_1, B_L_LEG_2, BODY_LINE_WIDTH)
    

PARTS = ['head', 'body', 'left arm', 'right arm', 'left leg', 'right leg']
# Name:       drawBodyPart()
# Purpose:    Draws body parts to DISPLAY in a sequential order, specified 
#             by the PARTS list
# Parameters: None
# Returns:    Nothing
def drawBodyPart():
    
        
    if PARTS[0] == 'head':
        drawHead()
    elif PARTS[0] == 'body':
        drawBody()
    elif PARTS[0] == 'left arm':
        drawLeftArm()
    elif PARTS[0] == 'right arm':
        drawRightArm()
    elif PARTS[0] == 'left leg':
        drawLeftLeg()
    elif PARTS[0] == 'right leg':
        drawRightLeg()

    del PARTS[0]

    if len(PARTS) == 0:
        pygame.display.update()
        pygame.quit()
        sys.exit()

# Name:       drawLines(letters)
# Purpose:    Draws a lines to DISPLAY corresponding to the number of letters in word
#             In addition, returns a list of graphic coordinates specifying where to 
#             draw the letters
# Parameters: letters <string>
# Returns:    <list> object of tuple points
def drawLines(letters):
    global lineSize # Size of each line to draw, made global because it is also the 
                    # font size of the letters to be drawn
    numLines = len(letters)
    lineSize = WIDTH / numLines
    lineSize = lineSize - 2 * PADDING
    x = PADDING     # Since the only part of the coordinates for the lines drawn is 
                    # the x part, we use x to specify the starting point of the lines
    letterSpots = [] # list object that will hold the points of where to draw
                     # the letters
    letterSpotY = int(HEIGHT * 0.75 - lineSize/2 - 4) # Y coordinate of letter objects

    for letter in letters:
        pygame.draw.line(DISPLAY, BLACK, (x, int(HEIGHT * 0.75)),\
                         (x + lineSize, int(HEIGHT*0.75)), BODY_LINE_WIDTH)
        letterSpots.append((x + lineSize/2, letterSpotY))
        x = x +lineSize + 2 * PADDING # update 

    return letterSpots

# Name:       makeLetters()
# Purpose:    Creates a list of letter objects, needed in order to actually make the 
#             correctly entered letters appear on the display
# Parameters: Nothing
# Returns:    <list> object of letter objects
def makeLetters():
    letterList = []
    fontObj = pygame.font.Font('freesansbold.ttf', int(lineSize))
    for letter in WORD:
        textObj = fontObj.render(letter, True, BLACK, WHITE)
        letterList.append(textObj)

    return letterList

# Name:       wrongLetter(letter)
# Purpose:    Called whenever the user enters an incorrect letter, draws it in RED
#             on the screen
# Parameters: letter <string>
# Returns:    Nothing, modifies the window
def wrongLetter(letter):
    wrongLetterX = 7 - len(PARTS)
    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    wrongLetterObj = fontObj.render(letter, True, INCORRECT_COLOR, BACKGROUND_COLOR)
    where = ((wrongLetterX * WIDTH/8), HEIGHT * 0.9)
    wrongLetterRect =  wrongLetterObj.get_rect()
    wrongLetterRect.center = where
    DISPLAY.blit(wrongLetterObj, wrongLetterRect)

# Name:       won(letters)
# Purpose:    Called after every turn, checks if each slot in the inputted 
#             letter object list is none. As letters from the letter object list
#             are drawn, their slot in the list is set to None, in order to 
#             signify that the letter has already been drawn
# Parameters: <list> of <letter> objects
# Returns:    Nothing, fills the window in GREEN, and writes "You Won!"
def won(letters):
    for letter in letters:
        if letter != None:
            return
    DISPLAY.fill(WIN_COLOR)
    fontObj = pygame.font.Font('freesansbold.ttf', 60)
    letterObj = fontObj.render("You won!", True, BLACK, GREEN)

    rect = letterObj.get_rect()
    rect.center = (300,300)
    
    DISPLAY.blit(letterObj, rect)

# Main code, ran when the game begins
DISPLAY.fill(BACKGROUND_COLOR)

drawHanger()
letterSpot = drawLines(WORD)
letterObject = makeLetters()
print(WORD)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            letterEntered = pygame.key.name(event.key)
            indices = []
            i = 0
            while i < len(WORD):
                if WORD[i] == letterEntered:
                    indices.append(i)
                i = i + 1

            if len(indices) > 0:
                for index in indices:
                    letterToDraw = letterObject[index]
                    if letterToDraw == None:
                        break
                    rectObj = letterToDraw.get_rect()
                    rectObj.center = letterSpot[index]
                    letterObject[index]= None
                    DISPLAY.blit(letterToDraw, rectObj)
            else:
                drawBodyPart()
                wrongLetter(letterEntered)

            won(letterObject)
                
                        
    pygame.display.update()



















    
