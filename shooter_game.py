#Создай собственный Шутер!
win_width = 700
a,b=0,0
from pygame import *
from random import randint
from time import sleep
mixer.init()
kuk=list()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('shoot.ogg')
kill_sound = mixer.Sound('kill.ogg')
lose_sound = mixer.Sound('lose.ogg')
window = display.set_mode((700,500))
background = transform.scale(image.load('galaxy.jpg'),(700,500))
clock = time.Clock()
run = True
display.set_caption('shuter')
health = 10
score = 0
max_bullets=30
bullets_count=max_bullets
asteroid_health=10
kok=60
trun=180
field_active=None
kuk.append(transform.scale(image.load('asteroid16bit.png'),(100,100)))
kuk.append(transform.scale(image.load('asteroid16bit1.png'),(100,100)))
kuk.append(transform.scale(image.load('asteroid16bit2.png'),(100,100)))
kuk.append(transform.scale(image.load('asteroid16bit3.png'),(100,100)))
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_speed,player_y,a,b,):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(a,b))
        self.speed = player_speed
        self.rect =self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
        
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update(self):
        global bullets_count,kek,field_active,trun

        keys=key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x-=self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x+=self.speed
        if keys[K_SPACE]:
            if kek <= 0:
                self.Fire() 
                fire_sound.play()
                kek=5
        if field_active and trun>0:
            self.image=transform.scale(image.load('rocket16bit_force_field.png'),(80,80))
        else:
            self.image=transform.scale(image.load('rocket16bit.png'),(65,65))
            trun=1000
            field_active=False
    def Fire(self):
        global bullets_count
        bullet=Bullet('bullet16bit.png',self.rect.centerx-12,10,self.rect.top,25,25)
        bullets.add(bullet)
        bullets_count-=1
g=0

class Asteroid(GameSprite): 
    def update(self):
            self.rect.y+=self.speed
            global health, asteroid_health,g,kuk,field_active
            if g==40:
                g=0
            puk=int(g/10-1)
            self.image=kuk[puk]
            
            

            if sprite.collide_rect(player,self):    
                self.Colide()
                if field_active!= True:
                    health-=10
            if self.rect.y >=500:
                self.Colide()
            
            if asteroid_health<=0:
                self.Colide()
                
    def Colide(self):
        global kok
        global asteroid_health
        self.rect.y=0
        self.rect.x=randint(100,550)
        self.speed=randint(1,3)
        kok=600 
        asteroid_health=10
        
i =list()
class Enemy(GameSprite):
    def update(self):
        self.rect.y+=self.speed
        global health,score,jpek,field_active,nock,что

        if self.rect.y >=500 or sprite.collide_rect(player,self):
            
            self.Colide()
            if field_active!= True:
                health-=1
   
        if self in lol:
            
            score+=1
            jpek+=1
            kill_sound.play() 
            if nock == score:
                boost.rect.x,boost.rect.y=self.rect.x,self.rect.y
                nock=randint(score+30,score+70) 
                что=True  
            self.Colide()
        
    def Colide(self):
        self.rect.y=0
        self.rect.x=randint(100,550)
        self.speed=randint(3,5)      
e1= Enemy('ufo16bit.png', randint(100,600),randint(3,5),0,70,65)
e2= Enemy('ufo16bit.png', randint(100,600),randint(3,5),0,70,65)
e3= Enemy('ufo16bit.png', randint(100,600),randint(3,5),0,70,65)
e4= Enemy('ufo16bit.png', randint(100,600),randint(3,5),0,70,65)
e5= Enemy('ufo16bit.png', randint(100,600),randint(3,5),0,70,65)
nock = randint(30,50)
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        global asteroid_health
        if sprite.collide_rect(self,a) and kok<=0:
            asteroid_health-=1
            self.kill()
class boost(GameSprite):
    def update(self):
        global field_active,что
        self.rect.y+=self.speed
        if sprite.collide_rect(player,self):
            field_active=True
            что=False
lol=list() 
player = Player('rocket16bit.png',285,10,win_width-280,80,80)
bullets=sprite.Group()
font.init()
font1 = font.Font(None,36)
enemies= sprite.Group()
enemies.add(e1)
enemies.add(e2)
enemies.add(e3)
enemies.add(e4)
enemies.add(e5)
a= Asteroid('asteroid16bit.png', randint(100,600),randint(1,3),0,100,100)
kek = 0
jpek=0
boost=boost('force_field.png', randint(100,600),randint(1,3),0,65,65)
что=None
while run:
    if health>0:
        kek-=1
        kok-=1
        trun-=1
        window.blit(background,(0,0))
        player.update()
        player.reset()
        enemies.draw(window)
        bullets.draw(window)
        enemies.update()
        bullets.update()
        
        
        if kok <=1:
            
            a.reset()
            a.update()
            g+=1
        text_health = font1.render('Жизни: '+str(health),False,(255,255,255))
        window.blit(text_health,(0,30))
        text_score = font1.render('Очки: '+str(score),False,(255,255,255))
        window.blit(text_score,(0,0))
        text_bullets = font1.render('Пуль: '+str(bullets_count)+'/'+str(max_bullets),False,(255,255,255))
        window.blit(text_bullets,(0,60))
        
        if что:
            boost.reset()
            boost.update()
        if jpek >= 10:
            health+=1
            jpek=0
        if bullets_count==0:
            kek=60
            bullets_count=max_bullets
        lol = sprite.groupcollide(enemies,bullets,False,True)
        display.update()    
        clock.tick(60)
        print(nock)
    else:
        lose = font1.render('YOU LOSE',False,(255,0,0)) 
        window.fill((255,255,255))
        window.blit(lose,(300,100)) 

        
        text_score = font1.render('Очки: '+str(score),False,(0,0,0))
        
        window.blit(text_score,(300,250))
        lose_sound.play()
        display.update()    
        sleep(2)
        run=False
        
    for e in event.get():
        if e.type == QUIT:
            run =False
    
    