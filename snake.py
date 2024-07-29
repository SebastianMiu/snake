import pygame
import random


class Snake:
    
    def __init__(self):
        self.size = 18
        self.body = [pygame.Rect(100,100, self.size, self.size)]
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
        if head[0] > 800 or head[0] < 0 or \
           head[1] > 600 or head[1] < 0:
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



def drawsnake(screen, snake):
    for it in snake.body:
        pygame.draw.rect(screen, (0,0,0), it)
    
def randompoint():
    return pygame.Rect(random.randrange(0, 800, 18), random.randrange(0, 600, 18), 18, 18)

def drawpoint(screen, point):
    pygame.draw.rect(screen, (176, 12,0), point)


def main():
    pygame.init()
    pygame.display.set_caption("SNAKE")
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    
    snake = Snake()
    point = randompoint()
    speed = 15

    #menu
    menu = True
    while menu:
        screen.fill((250, 238, 180))

        pygame.draw.rect(screen, (117, 103, 75), (204, 203, 388, 50))

        title = pygame.font.SysFont('Times New Roman', 50 ,bold = True)
        titlerender = title.render("SNAKE GAME", False, (255,255,255))
        screen.blit(titlerender, (228, 200))

        ins = pygame.font.SysFont('Times New Roman', 20)
        instruction = ins.render("Press any key to start", False, (0,0,0))
        screen.blit(instruction, (306, 300))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                menu = False
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()
                
    
    run = True
    while run:
        clock.tick(speed)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                snake.change_dir(event.key)


        snake.move()


        if snake.check_collisions() == False:    

            run = False
        
        if snake.body[0].colliderect(point):
            snake.grow()
            point = randompoint()
            if snake.checkscore() % 5 == 0 and snake.checkscore() != 0:
                speed = speed + 1
                print("speed+++")
            
     
        screen.fill((250, 238, 180))
        drawpoint(screen, point)
        drawsnake(screen, snake)

        text = pygame.font.SysFont('Times New Roman', 30)

        scorerender = text.render("Score: "+ str(snake.checkscore()), False, (0,0,0))
        screen.blit(scorerender, (20, 20))

        pygame.display.update()

    iflost = True
    while iflost:
        screen.fill((250, 238, 180))
        loss = pygame.font.SysFont('Times New Roman', 35)
        lossrender = loss.render("You Lost!", False, (176, 12,0))

        screen.blit(lossrender, (328, 250))

        pygame.display.update()

        pygame.time.delay(1000)
        iflost = False

    
    pygame.quit()

if __name__ == "__main__":
    main()



