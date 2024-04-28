from pygame import *
'''Необходимые классы'''


#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        elif keys[K_s] and self.rect.y < 395:
            self.rect.y += self.speed 
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        elif keys[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed 

class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__(player_image, player_x, player_y, player_speed, wight, height)
        self.speed_x = player_speed
        self.speed_y = player_speed

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y < 5:
            self.speed_y = self.speed_y * -1
        elif self.rect.y > 495:
            self.speed_y *= -1

#игровая сцена:
back = (200, 255, 255) #цвет фона (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
#флаги, отвечающие за состояние игры
game = True
finish = False
clock = time.Clock()
FPS = 60

racket1 = Player('clipart.png', 20, 200, 4, 50, 150)
racket2 = Player('clipart.png', 540, 200, 4, 50, 150)
ball = Ball('ball.png', 300, 250, 2, 50, 50)

player_score1 = 0
player_score2 = 0

font.init()
font = font.SysFont('Aria', 45)

win1 = font.render('Player 1 win!!!', True, (0, 255, 0))
win2 = font.render('Player 2 win!!!', True, (0, 255, 0))




while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        raund_text = font.render('Текущий счёт'+str(player_score1)+':'+str(player_score2), True, (0,0,0))
        # отрисовка объектов : фон, ракетка1, ракетка2, мяч
        # перемещение: ракетка1, ракетка2, мяч
        window.fill(back)
        window.blit(raund_text, (140, 30))
        window.fill(back)
        racket1.reset()
        racket2.reset()
        ball.reset()
        racket1.update_l()
        racket2.update_r()
        ball.update()
        # условия соприкосновения ракеток и мяча
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(ball, racket2):
            ball.speed *= -1

        # условия проигрыша
        if ball.rect.x > 550:
            player_score1+= 1
            ball.rect.x = 300
            ball.rect.y = 250
            ball.speed_x *= -1

        elif ball.rect.x < 10:
            player_score1+= 1
            ball.rect.x = 300
            ball.rect.y = 250
            ball.speed_x *= -1
            ball.speed_x *= -1

        if player_score1 >= 11:
            finish = True
            window.blit(win1, (150, 200))
        elif player_score2 >= 11:
            finish= True
            window.blit(win2, (150, 200))

    clock.tick(FPS)
    display.update()