# initial configs
import pygame
import random

pygame.init()
pygame.display.set_caption("Snake Game on Python")

width, height = 900, 600
screen=pygame.display.set_mode((width,height))

clock=pygame.time.Clock()

#colors RGB
background_color=(0,0,0)
snake_color=(255,255,255)
food_color=(0,255,0)
score_color=(255,0,255)

#snake paramns
square_size=20
snake_speed=10

# draw objects
##score
##snake


##food
def generate_food():
    x=round(random.randrange(0,900-square_size)/square_size)*square_size
    y=round(random.randrange(0,600-square_size)/square_size)*square_size
    return x, y

def draw_food(size,x,y):
    pygame.draw.rect(screen, food_color, [x,y,size,size])
    
def draw_snake(size, pixels):
    for pixel in pixels:
        pygame.draw.rect(screen, snake_color,[pixel[0], pixel[1], size, size])

def draw_score(score):
    font=pygame.font.SysFont("comicsans", 25)
    text=font.render(f"Score : {score}", True, score_color)
    screen.blit(text,[400,10])
    
def select_speed(key):
    if key ==pygame.K_DOWN:
        speed_x=0
        speed_y=square_size
    elif key ==pygame.K_UP:
        speed_x=0
        speed_y=-square_size
    elif key ==pygame.K_LEFT:
        speed_x=-square_size
        speed_y=0
    elif key ==pygame.K_RIGHT:
        speed_x=square_size
        speed_y=0
    return speed_x, speed_y

# create infinity loop (game running)
def run_game():
    game_over=False
    
    x=width/2
    y=height/2
    
    speed_x=0
    speed_y=0
    
    snake_size=1
    pixels=[]
    
    food_x, food_y = generate_food()
    

    
    while not game_over:
        screen.fill(background_color)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over=True
            elif event.type == pygame.KEYDOWN:
                speed_x, speed_y = select_speed(event.key)
                
        draw_food(square_size,food_x,food_y)
        
        #update snake position
        x+=speed_x
        y+=speed_y
        
        #draw snake
        pixels.append([x,y])
        if len(pixels)>snake_size:
            del pixels[0]
        
        #if snake hits itself
        for pixel in pixels[:-1]:
            if pixel==[x,y]:
                game_over=True
            
    
        
        draw_snake(square_size, pixels)
                      
        draw_score(snake_size - 1)   
                      
        pygame.display.update()
        
        #create new food
        if x == food_x and y==food_y:
            snake_size+=1
            food_x,food_y=generate_food()
            
        clock.tick(snake_speed)
            




# finish when?
##snake hits wall
##snake hits snake

# get inputs
##keyboard
##close game

run_game()