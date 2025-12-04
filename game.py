import pygame
import random

pygame.init()
screen = pygame.display.set_mode((700, 820))
pygame.display.set_caption("Snakes & Ladders")
font = pygame.font.SysFont(None, 30)

RED = (220, 50, 47)
BLUE = (52, 152, 219)

ladders = {2: 38, 7: 14, 21: 42, 28: 84, 51: 67, 71: 91}
snakes = {16: 6, 46: 25, 62: 19, 89: 68, 95: 75, 99: 80}

p1 = 1
p2 = 1
turn = 1
dice = 0
won = 0

def draw():
    screen.fill((220, 220, 200))
    
    for i in range(1, 101):
        row = (i-1) // 10
        col = (i-1) % 10

        if row%2 == 0: #changed x coordinate , y coordinate won't change 
            x = col*70
        else:
            x = (9-col)*70
        y = (9-row) * 70
        if row%2 == 0:
            if (row + col) % 2 == 0:
                pygame.draw.rect(screen, (240, 240, 220), (x, y, 70, 70))
            else:
                pygame.draw.rect(screen, (200, 220, 240), (x, y, 70, 70))
        else:
            if (row + col) % 2 == 0:
                pygame.draw.rect(screen, (200, 220, 240), (x, y, 70, 70))
            else:
                pygame.draw.rect(screen, (240, 240, 220), (x, y, 70, 70))
        pygame.draw.rect(screen, (100, 100, 100), (x, y, 70, 70), 1)
        txt = font.render(str(i), True, (0, 0, 0))
        screen.blit(txt, (x+5, y+5))
    
    #ladders
    for start, end in ladders.items():
        r1 = (start-1) // 10
        c1 = (start-1) % 10

        if r1%2==0:
            x1 = c1*70+35
        else:
            x1 = (9-c1)*70+35    
        y1 = (9-r1)*70+35
        
        r2 = (end-1) // 10
        c2 = (end-1) % 10
        if r2%2 == 0:
            x2 = c2 * 70 + 35
        else:
            x2 = (9 - c2) * 70 + 35
        y2 = (9-r2)*70+35
        
        pygame.draw.line(screen, (0, 150, 0), (x1, y1), (x2, y2), 5)
    
    #Snakes
    for start, end in snakes.items():
        r1 = (start-1) // 10
        c1 = (start-1) % 10
        if r1%2==0:
            x1 = c1*70+35
        else:
            x1 = (9-c1)*70+35
        y1 = (9-r1)*70+35
        
        r2 = (end-1) // 10
        c2 = (end-1) % 10
        if r2%2==0:
            x2 = c2 * 70 + 35
        else:
            x2 = (9 - c2) * 70 + 35
        y2 = (9-r2)*70+35
        
        pygame.draw.line(screen, (200, 0, 0), (x1, y1), (x2, y2), 5)
        pygame.draw.circle(screen, (200, 0, 0), (x1, y1), 8)
    
    # Players
    r1 = (p1-1) // 10
    c1 = (p1-1) % 10
    if r1%2==0:
        pygame.draw.circle(screen, RED, (c1*70+25, (9-r1)*70+35), 12)
    else:
        pygame.draw.circle(screen, RED, ((9-c1)*70+25, (9-r1)*70+35), 12)

    r2 = (p2-1) // 10
    c2 = (p2-1) % 10
    if r2%2==0:
        pygame.draw.circle(screen, BLUE, (c2*70+45, (9-r2)*70+35), 12)
    else:
        pygame.draw.circle(screen, BLUE, ((9-c2)*70+45, (9-r2)*70+35), 12)
    pygame.draw.rect(screen, (100, 100, 120), (0, 700, 700, 120))
    
    if won == 0:
        msg = font.render(f"Player {turn} - Press SPACE to roll", True, (255, 255, 255))
        screen.blit(msg, (20, 720))
        d = font.render(f"Dice: {dice}", True, (255, 255, 255))
        screen.blit(d, (20, 760))
    else:
        msg = font.render(f"Player {won} WINS! Press R to restart", True, (255, 255, 0))
        screen.blit(msg, (150, 740))
    
    pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                p1 = 1
                p2 = 1
                turn = 1
                dice = 0
                won = 0
            
            if event.key == pygame.K_SPACE and won == 0:
                dice = random.randint(1, 6)
                
                if turn == 1:
                    p1 = p1 + dice
                    if p1 > 100:
                        p1 = p1 - dice
                    if p1 in ladders:
                        p1 = ladders[p1]
                    if p1 in snakes:
                        p1 = snakes[p1]
                    if p1 == 100:
                        won = 1
                    else:
                        turn = 2
                else:
                    p2 = p2 + dice
                    if p2 > 100:
                        p2 = p2 - dice
                    if p2 in ladders:
                        p2 = ladders[p2]
                    if p2 in snakes:
                        p2 = snakes[p2]
                    if p2 == 100:
                        won = 2
                    else:
                        turn = 1
    
    draw()

pygame.quit()