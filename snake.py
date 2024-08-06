import pygame
import random


class Snake:
    
    def __init__(self):
        self.size = 20
        self.body = [pygame.Rect(200,200, self.size, self.size)]
        self.dir = pygame.K_d
        self.score = 0
        
    def move(self):
        Xsnake, Ysnake = self.body[0].topleft

        if self.dir == pygame.K_w:
            newhead = pygame.Rect(Xsnake, Ysnake - self.size, self.size, self.size)

        elif  self.dir == pygame.K_s:
            newhead = pygame.Rect(Xsnake, Ysnake + self.size, self.size, self.size)

        elif  self.dir == pygame.K_d:
            newhead = pygame.Rect(Xsnake + self.size, Ysnake, self.size, self.size)

        elif  self.dir == pygame.K_a:
            newhead = pygame.Rect(Xsnake - self.size, Ysnake, self.size, self.size)

        self.body = [newhead] + self.body[:-1]


        
    def change_dir(self, dirr):
        if (dirr==pygame.K_w and self.dir != pygame.K_s ) or \
           (dirr==pygame.K_a and self.dir != pygame.K_d ) or \
           (dirr==pygame.K_s and self.dir != pygame.K_w ) or \
           (dirr==pygame.K_d and self.dir != pygame.K_a ):
            self.dir = dirr

    def check_collisions(self):
        head = self.body[0]
        if head[0] > 898 or head[0] < 92 or \
           head[1] > 698 or head[1] < 92:
                print("you lost")
                return False

        for snek in self.body[1:]:
            if head == snek:
                print("you lost")
                return False


    def grow(self):
        self.body.append(self.body[-1].copy())
        self.score = self.score + 1

    def checkscore(self):
        return self.score



class Snake2(Snake):
    def __init__(self):
        self.size = 20
        self.body = [pygame.Rect(300,200, self.size, self.size)]
        self.dir = pygame.K_RIGHT
        self.score = 0

    def move(self):
        Xsnake, Ysnake = self.body[0].topleft

        if self.dir == pygame.K_UP:
            newhead = pygame.Rect(Xsnake, Ysnake - self.size, self.size, self.size)

        elif  self.dir == pygame.K_DOWN:
            newhead = pygame.Rect(Xsnake, Ysnake + self.size, self.size, self.size)

        elif  self.dir == pygame.K_RIGHT:
            newhead = pygame.Rect(Xsnake + self.size, Ysnake, self.size, self.size)

        elif  self.dir == pygame.K_LEFT:
            newhead = pygame.Rect(Xsnake - self.size, Ysnake, self.size, self.size)

        self.body = [newhead] + self.body[:-1]


        
    def change_dir(self, dirr):
        if (dirr==pygame.K_UP and self.dir != pygame.K_DOWN ) or \
           (dirr==pygame.K_LEFT and self.dir != pygame.K_RIGHT ) or \
           (dirr==pygame.K_DOWN and self.dir != pygame.K_UP ) or \
           (dirr==pygame.K_RIGHT and self.dir != pygame.K_LEFT ):
            self.dir = dirr    





def drawsnake(screen, snake):
    for it in snake.body:
        pygame.draw.rect(screen, (0,0,0), it)
        
def drawsnake2(screen, snake):
    for it in snake.body:
        pygame.draw.rect(screen, (74,74,74), it)
    
def randompoint():
    return pygame.Rect(random.randrange(105, 795, 18), random.randrange(105, 595, 18), 20, 20)

def drawpoint(screen, point):
    pygame.draw.rect(screen, (176, 12,0), point)


def main():
    pygame.init()
    pygame.display.set_caption("SNAKE")
    screen = pygame.display.set_mode((1000, 800))
    clock = pygame.time.Clock()
    background = pygame.image.load('console_background.jpg')
    
    snake = Snake()

    point = randompoint()
    speed = 15
    

    #menu
    menu = True
    players = 0
    while menu:
        #screen.fill((250, 238, 180))
        
        #background
        screen.blit(background, (0,0))
        pygame.draw.rect(screen, (250, 238, 180), (100,100, 800, 600))

        #title 
        pygame.draw.rect(screen, (117, 103, 75), (293, 303, 388, 50))

        title = pygame.font.SysFont('Times New Roman', 50 ,bold = True)
        titlerender = title.render("SNAKE GAME", False, (255,255,255))
        screen.blit(titlerender, (319, 300))

        ins = pygame.font.SysFont('Times New Roman', 20)
        instruction = ins.render("Single player: press 1. Multi player: press 2", False, (0,0,0))
        screen.blit(instruction, (315, 400))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_1): 
                    players = 1 
                    menu = False
                elif(event.key == pygame.K_2):
                    players = 2
                    menu = False
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()

                
    if players == 2: snake2 = Snake2()
    
    #game
    run = True
    while run:
        clock.tick(speed)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                snake.change_dir(event.key)
                if players == 2: snake2.change_dir(event.key)


        snake.move()
        if players == 2: snake2.move()


        if snake.check_collisions() == False: run = False
            
        if players == 2:
             if snake2.check_collisions() == False: run = False
        
        if snake.body[0].colliderect(point):
            snake.grow()
            point = randompoint()
            if snake.checkscore() % 5 == 0 and snake.checkscore() != 0:
                speed = speed + 1
                print("speed+++")
        
        if players == 2:
            
            if snake2.body[0].colliderect(point):
                snake2.grow()
                point = randompoint()
                if snake2.checkscore() % 5 == 0 and snake2.checkscore() != 0:
                    speed = speed + 1
                    print("speed+++")
                    
        screen.blit(background, (0,0))     
        pygame.draw.rect(screen, (250, 238, 180), (100,100,800,600))
        drawpoint(screen, point)
        drawsnake(screen, snake)
        if players == 2: drawsnake2(screen, snake2)

        #score text
        text = pygame.font.SysFont('Times New Roman', 30)
        scorerender = text.render("Player 1: "+ str(snake.checkscore()), False, (0,0,0))
        screen.blit(scorerender, (120, 110))

        if players == 2:
            scorerender = text.render("Player 2: "+ str(snake2.checkscore()), False, (0,0,0))
            screen.blit(scorerender, (120, 160))

        pygame.display.update()

    iflost = True
    while iflost:
        #background
        screen.blit(background, (0,0))
        pygame.draw.rect(screen, (250, 238, 180), (100,100, 800, 600))
        
        #'you lost'
        loss = pygame.font.SysFont('Times New Roman', 35)
        lossrender = loss.render("You Lost!", False, (176, 12,0))
        
        print("1: lost at score: " + str(snake.checkscore()))
        if players == 2: print("2: lost at score: " + str(snake2.checkscore()))        

        screen.blit(lossrender, (423, 300))

        pygame.display.update()

        pygame.time.delay(1000)
        iflost = False

    
    pygame.quit()

if __name__ == "__main__":
    main()



