import pygame as pyg 
import pygame.freetype as pyfree 


class NLO:
    def __init__(self, xy, speed, pick, damage, shield): 
        self.xy = xy 
        self.speed = speed
        self.pick = pick 
        self.rect = pick.get_rect(center = xy)  
        self.check = 0
        self.ship_life = 4
        self.ship_shield = 0
        self.damage = damage 
        self.shield = shield
        self.shield_rect = shield[0].get_rect() 
        self.engine_piks = []
        self.number = 0
        for i in range(11,18):
            pik_engine = pyg.image.load(f'assets/PNG/Effects/fire{i}.png')
            self.engine_piks.append(pik_engine) 
    def draw(self, displey):
        displey.blit(self.pick, self.rect) 
        if self.ship_life == 3:
            displey.blit(self.damage[0], self.rect) 
        if self.ship_life == 2:
            displey.blit(self.damage[1], self.rect) 
        if self.ship_life == 1:
            displey.blit(self.damage[2], self.rect) 
        if self.ship_shield == 3:
            displey.blit(self.shield[2], self.shield_rect)
        if self.ship_shield == 2:
            displey.blit(self.shield[1], self.shield_rect)
        if self.ship_shield == 1:
            displey.blit(self.shield[0], self.shield_rect) 
        displey.blit(self.engine_piks[int(self.number)], (self.rect.x+40, self.rect.y+75))   
    def update(self, speed):
        keys = pyg.key.get_pressed()
        if keys [pyg.K_RIGHT] == True:
            self.rect.x = self.rect.x + self.speed 
        if keys [pyg.K_LEFT] == True:
            self.rect.x = self.rect.x - self.speed 
        if keys [pyg.K_UP] == True:
            self.rect.y = self.rect.y - self.speed
        if keys [pyg.K_DOWN] == True:
            self.rect.y = self.rect.y + self.speed 
        self.shield_rect.x = self.rect.x-23
        self.shield_rect.y = self.rect.y-25
        self.number = self.number + speed 
        if self.number > 6:
             self.number = 0 
    def life(self):
        if self.ship_life < 4:
            self.ship_life = self.ship_life + 1
    def life_minus(self):
        if self.ship_shield > 0:
            self.ship_shield = self.ship_shield - 1 
        elif self.ship_shield == 0: 
            self.ship_life = self.ship_life - 1



class meteorite:
    def __init__(self, xy, speed_y, speed_x, pick):
        self.xy = xy 
        self.speed_y = speed_y
        self.speed_x = speed_x 
        self.pick = pick 
        self.rect = pick.get_rect(center = xy)   
    def draw(self, display):
        display.blit(self.pick, self.rect) 
    def update(self):
        self.rect.y = self.rect.y + self.speed_y
        self.rect.x = self.rect.x + self.speed_x 


class Laser:
    def __init__(self, xy, pick):
        self.xy = xy
        self.pick = pick
        self.speed = 3
        self.rect = pick.get_rect(center = xy) 
        self.laser_piks = []
        self.number = 0
        for i in range(1,8):
            pik_las = pyg.image.load(f'assets/PNG/Lasers/laserBlue0{i}.png')
            self.laser_piks.append(pik_las)  
    def update(self, speed):
        self.rect.y = self.rect.y - self.speed 
        self.number = self.number + speed 
        if self.number > 6:
            self.number = 0 
    def draw(self, display):
        display.blit(self.laser_piks[int(self.number)], self.rect)  


class Upgrade:
    def __init__(self, xy, pick, type):
        self.xy = xy
        self.speed = 2
        self.pick = pick
        self.type = type 
        self.rect = pick.get_rect(center = xy) 
    def update(self):
        self.rect.y = self.rect.y + self.speed 
    def draw(self, display):
        display.blit(self.pick, self.rect) 


class Button:
    def __init__(self, xy, pick, text):
        self.xy = xy
        self.pick = pick
        self.text = text
        self.rect = pick.get_rect(center = xy) 
        self.font =  pyfree.Font('Bonus/kenvector_future.ttf', 30)
    def draw(self, display):
        display.blit(self.pick, self.rect,)
        self.font.render_to(display, (self.rect.x+20, self.rect.y+10), self.text)  