import pygame
import time
from random import randrange, randint

black =(0,0,0)
red =(255,0,0)
white = (255,255,255)
sunset = (253, 72, 47)


greenyellow = (184, 255,0)
brightblue = (47, 228, 253)
orange = (255, 113, 0)
yellow = (255, 236, 0)
purpose = (252, 67, 255)

colorChoices = [greenyellow, brightblue, orange, yellow, purpose]



surfaceWidth = 800
surfaceHeight = 400

imageWidth = 100
imageHeight = 43

pygame.init()   # will start 
surface = pygame.display.set_mode((surfaceWidth, surfaceHeight))  # setting up the dimensions
pygame.display.set_caption('Helicopter')      # writing the captions for the screen
clock = pygame.time.Clock()
# will measure frames/second
img = pygame.image.load('Helicopter.png')

# the no of y co-ordinates you  will go down each time you leave your key unpressed or press down arrow key

def score(count):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render('Score:'+str(count), True ,white)
    surface.blit(text,[0,0]) # o,o signifies top left corner
    

def blocks(x_block,y_block,block_width,block_height,gap,colorChoice):
    pygame.draw.rect(surface,colorChoice,[x_block, y_block, block_width, block_height])   #pygame.draw.rect(where u want to draw, color of block, [x-position of block,y-pos of block,width of block , height of block])
    pygame.draw.rect(surface, colorChoice, [x_block, y_block + gap + block_height, block_width, surfaceHeight])   #we keep the x same because we want the blocks to be vertically up and down



def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN,pygame.KEYUP,pygame.QUIT]):
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type==pygame.KEYDOWN:
            continue
        return event.key
    return None


def makeTextObjs(text,font):
    textSurface = font.render(text,True,sunset) # it take 4 parameters text,aliasing,color,background-color set to none by default
    return textSurface,textSurface.get_rect()  # it allows us toget the rectangle box which will be used to highlight and  review the text

def msgSurface(text):
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    largeText = pygame.font.Font('freesansbold.ttf' ,150) # using bigger font size

    titleTextSurf, titleTextRect = makeTextObjs(text, largeText)
    titleTextRect.center = surfaceWidth/2, surfaceHeight/2
    surface.blit(titleTextSurf, titleTextRect)

    typTextSurf, typTextRect = makeTextObjs('press any key to continue', smallText)
    typTextRect.center = surfaceWidth/2, ((surfaceHeight/2)+100)
    surface.blit(typTextSurf,typTextRect)

    pygame.display.update()
    time.sleep(1)  # time for sleeping

    while replay_or_quit()==None:
        clock.tick() # updating clock
    main()



def gameOver():
    msgSurface('Kaboom!')


def helicopter(x,y, image):                # we are declaring image as pararmeter becoz we don't want that each time the function runs the helicopter image to be reloaded thus wasting memory
    surface.blit(img,(x,y))# surface.blit(img,(x,y)) it will be the position where helicopter will be placed x,y are the co-ordinates


def main(): 
    x = 150  # co-ordinates where we initially want to keep our helicopter
    y = 200
    y_move = 0


    x_block = surfaceWidth
    y_block = 4

    block_width = 75
    block_height = randint(0,surfaceHeight/2)
    gap = imageHeight *3
    block_move = 4

    current_score = 0


    game_over = False
    # looping for quiting the game

    blockColor = colorChoices[randrange(0,len(colorChoices))]

    while not game_over:                         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -5
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move = 5
        y += y_move

        surface.fill(black)  # filling the background color with black
        helicopter(x, y, img)

        
        blocks(x_block, y_block,block_width, block_height, gap,blockColor)
        score(current_score) # declaring a func for recording the scores

        x_block -=block_move
        
        if y > surfaceHeight-40 or y < 0:   # surfaceHeight-40 is for height-40 which is the height of the helicopter
            gameOver()

        if x_block < (-1*block_width):   # if x_block is less than -block_width this implies that the block went off screen 
            x_block = surfaceWidth # new block setting up
            block_height = randint(0,surfaceHeight/2)
            blockColor = colorChoices[randrange(0,len(colorChoices))]
            current_score+=1
             
        if x + imageWidth > x_block:
            if x < x_block + block_width:
                #print('possibly within boundary of x')
                if y < block_height:                         # its coding for upper boundaries when u hit the upper boundaris it quits
                    #print('y crossover upper!')
                    if x - imageWidth < block_width + x_block:
                        #print('game over hit upper')
                        gameOver()
    # setting the obstacle hit for lower
        if x  + imageWidth > x_block:

            if y + imageHeight > block_height + gap:
                #print('y cross-over lower')

                if x < block_width + x_block:
                    #print('game over lower')
                    gameOver()
        

        #if x_block < (x - block_width) < x_block + block_move:  # waiting that the helicopter crosses the block then only the score will be added  up
         #   current_score+=1

        if 3 <= current_score < 5:    # 
            block_move = 5
            gap = imageHeight * 2.9

        if 5 <= current_score < 8:
            block_move = 6
            gap = imageHeight * 2.8

        
        if 8 <= current_score < 14:
            block_move = 7
            gap = imageHeight * 2.7
            


        
        pygame.display.update()
        clock.tick(60)   # increasing the no in the bracket increases the frames/second which will make the screen to travel very fast
main()
pygame.quit()
quit()

