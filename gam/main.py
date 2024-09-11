
#create a Maze game!
from pygame import *
# from pygame.sprite import Sprite, Group, spritecollide, groupcollide

class Gamesprite():
    def __init__(self, image_path, image_size, x, y, speed_x, speed_y):
        self.image = transform.scale(image.load(image_path), image_size)
        self.rect = self.image.get_rect(topleft=(x,y))
        self.speed_x = speed_x
        self.speed_y = speed_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Gamesprite):
    def l_stik(self):
        key_pressed=key.get_pressed()
        print(key_pressed[K_UP])
        if key_pressed[K_UP] and self.rect.y > 0:
            self.rect.y-=5 
        if key_pressed[K_DOWN] and self.rect.y < size[1]-stik_siz[1]:
            self.rect.y+=5
    def r_stik(self):
        key_pressed=key.get_pressed()
        print(key_pressed[K_UP])
        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.y-=5 
        if key_pressed[K_s] and self.rect.y < size[1]-stik_siz[1]:
            self.rect.y+=5

    def update(self):
        global missed_score_r
        global missed_score_l
        global inactive

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y


        if self.rect.x < 0:
            self.rect.y = size[1]/2
            self.rect.x = size[0]/2
            self.speed_x *= -1
            missed_score_l +=1
            # inactive = True
            
        elif self.rect.x > size[0] - self.image.get_width():
            self.rect.y = size[1]/2
            self.rect.x = size[0]/2
            self.speed_x *= -1
            missed_score_r +=1
            # inactive = True
            
        if self.rect.y > size[1] - self.image.get_height() or self.rect.y < 0:
            self.speed_y *= -1

        if self.rect.colliderect(left.rect) or self.rect.colliderect(right.rect):
            self.speed_x *= -1
        
        if self.rect.y > size[1]:
            self.rect.y = 0
            self.rect.x = randint(0, 635)
            missed_score +=1

        




        



num_size = (30, 50)
size = (600, 400)
ball_size = (20,20)
stik_siz= (15, 100)
wall = (10, 600)

window = display.set_mode(size)

display.set_caption("Atari style ping-pong(PONG)")

#back = transform.scale(image.load("background.jpg"), size)
#enemy = transform.scale(image.load("cyborg.png"), sprite)
#player = transform.scale(image.load("hero.png"), sprite)


x1 = 50
y1 = 300
x2 = 610
y2 = 300
#class define
ball = Player("square.png", ball_size, 200, 200, 4, 4)
right = Player("stik.png", stik_siz, 55 , 100, 4, 2)
left = Player("stik.png", stik_siz, 530, 100, 4, 2)
num_0r = Gamesprite("0.png", num_size, 160, 65, 0, 0)
num_1r = Gamesprite("1.png", num_size, 160, 65, 0, 0)
num_2r = Gamesprite("2.png", num_size, 160, 65, 0, 0)
num_3r = Gamesprite("3.png", num_size, 160, 65, 0, 0)
num_4r = Gamesprite("4.png", num_size, 160, 65, 0, 0)
num_5r = Gamesprite("5.png", num_size, 160, 65, 0, 0)
num_6r = Gamesprite("6.png", num_size, 160, 65, 0, 0)
num_7r = Gamesprite("7.png", num_size, 160, 65, 0, 0)
num_8r = Gamesprite("8.png", num_size, 160, 65, 0, 0)
num_9r = Gamesprite("9.png", num_size, 160, 65, 0, 0)

num_0l = Gamesprite("0.png", num_size, 410, 65, 0, 0)
num_1l = Gamesprite("1.png", num_size, 410, 65, 0, 0)
num_2l = Gamesprite("2.png", num_size, 410, 65, 0, 0)
num_3l = Gamesprite("3.png", num_size, 410, 65, 0, 0)
num_4l = Gamesprite("4.png", num_size, 410, 65, 0, 0)
num_5l = Gamesprite("5.png", num_size, 410, 65, 0, 0)
num_6l = Gamesprite("6.png", num_size, 410, 65, 0, 0)
num_7l = Gamesprite("7.png", num_size, 410, 65, 0, 0)
num_8l = Gamesprite("8.png", num_size, 410, 65, 0, 0)
num_9l = Gamesprite("9.png", num_size, 410, 65, 0, 0)

# wall1 = Gamesprite("wall.png", wall, 200, 200, 4, 4)

#group


missed_score_l = 0
missed_score_r = 0

clock =time.Clock()
FPS = 60



font.init()
font = font.Font(None, 70)
win = font.render("left wins ", True, (0, 255, 0))
lose = font.render("right wins", True, (255, 0, 0))

game = True
inactive = False
direction = "left"
while game:
    for e in event.get():
            if e.type == QUIT:
                game =False
    if not inactive:
        window.fill((0, 0, 0))
        left.reset()
        right.reset()
        ball.reset()
        

        


#    window.blit(back, (0,0))
#    window.blit(enemy, (x2, y2))
#    window.blit(player, (x1, y1))

        

    
    left.l_stik()
    ball.update()
    right.r_stik()
    
    # Missedl = font.render(f"{missed_score_r}", True, (255, 255, 255))
    # window.blit(Missedl, (160, 65))
    # Missedr = font.render(f"{missed_score_l}", True, (255, 255, 255))
    # window.blit(Missedr, (420, 65))



    if missed_score_l == 0:
        num_0l.reset()
    if missed_score_l == 1:
        num_1l.reset()
    if missed_score_l == 2:
        num_2l.reset()
    if missed_score_l == 3:
        num_3l.reset()
    if missed_score_l == 4:
        num_4l.reset()
    if missed_score_l == 5:
        num_5l.reset()
    if missed_score_l == 6:
        num_6l.reset()
    if missed_score_l == 7:
        num_7l.reset()
    if missed_score_l == 8:
        num_8l.reset()
    if missed_score_l == 9:
        num_9l.reset()
    
    if missed_score_r == 0:
        num_0r.reset()
    if missed_score_r == 1:
        num_1r.reset()
    if missed_score_r == 2:
        num_2r.reset()
    if missed_score_r == 3:
        num_3r.reset()
    if missed_score_r == 4:
        num_4r.reset()
    if missed_score_r == 5:
        num_5r.reset()
    if missed_score_r == 6:
        num_6r.reset()
    if missed_score_r == 7:
        num_7r.reset()
    if missed_score_r == 8:
        num_8r.reset()
    if missed_score_r == 9:
        num_9r.reset()

    if missed_score_l >9:
        left.rect.y = 100
        right.rect.y = 100
        missed_score_l = 0
        missed_score_r = 0
    elif missed_score_r >9:
        left.rect.y = 100
        right.rect.y = 100
        missed_score_r = 0
        missed_score_l = 0



    display.update()
    clock.tick(FPS)
    