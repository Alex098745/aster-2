import pygame as py 
import setting as sett
import sprites as spri 
import os 
import random 
import pygame.freetype as pyfree 

def destroyd_ship():
    for i in more_meteors:
        if i.rect.colliderect(space_ship.rect):
            more_meteors.remove(i) 
            space_ship.life_minus()

        

def destroyd_meteors():
    for i in more_lasers:
        for a in more_meteors:
            if a.rect.colliderect(i.rect):
                more_meteors.remove(a)
                more_lasers.remove(i) 
                space_ship.check = space_ship.check + 1
            

def destroyd_upgrade():
    for i in more_up:
        if i.rect.colliderect(space_ship.rect):
            if i.type == 0: 
                space_ship.life() 
            if i.type == 1:
                space_ship.ship_shield = 3
                
            more_up.remove(i) 




py.init() 

font = pyfree.Font('Bonus/kenvector_future.ttf', 20)  
pick_button = py.image.load('assets/PNG/UI/buttonBlue.png') 
pick_button_two = py.image.load('assets/PNG/UI/buttonRed.png')
button = spri.Button((250,450), pick_button, 'start') 
button_2 = spri.Button((250,550), pick_button_two, 'exit') 



wind = py.display.set_mode((sett.SIZE_X, sett.SIZE_Y))

clock = py.time.Clock()

stop = True

damage_piks = []
for i in range(1,4): 
    damage_piks.append (py.image.load(f'assets/PNG/Damage/playerShip3_damage{i}.png')) 

shield_piks = []
for i in range(1,4):
    shield_piks.append(py.image.load(f'assets/PNG/Effects/shield{i}.png')) 

pik = py.image.load('assets/Backgrounds/darkPurple.png') 
pik = py.transform.scale(pik, (sett.SIZE_X, sett.SIZE_Y))
pik_new = py.image.load('assets/PNG/UI/playerLife3_blue.png')
pik_menu = py.image.load('assets/Backgrounds/blue.png') 
pik_menu = py.transform.scale(pik_menu, (sett.SIZE_X, sett.SIZE_Y))

pik_ship = py.image.load('assets/PNG/playerShip3_blue.png') 
space_ship = spri.NLO((250,400), 2,  pik_ship, damage_piks, shield_piks)  

name_meteors = os.listdir('assets/PNG/Meteors')
pik_meteors = []

for i in name_meteors:
    pik_meteor = py.image.load(f'assets/PNG/Meteors/{i}') 
    pik_meteors.append(pik_meteor)  
       

pik_las = py.image.load('assets/PNG/Lasers/laserBlue01.png') 

pik_up = py.image.load('assets/PNG/Power-ups/pill_blue.png')
pik_up_2 = py.image.load('assets/PNG/Power-ups/powerupYellow_shield.png') 

more_lasers = [] 
more_meteors = [] 
more_up = [] 
pik_ups = [pik_up, pik_up_2] 


menu = 'меню'
moment = 0


METEOR_EVENT = py.USEREVENT 
py.time.set_timer(METEOR_EVENT, 2000) 
UPGRADE_EVENT = py.USEREVENT + 1
py.time.set_timer(UPGRADE_EVENT, 7000) 
while stop:
    sob = py.event.get()
    for i in sob:
        if i.type == py.QUIT:
            stop = False 
        if i.type == py.KEYDOWN:
            if i.key ==  py.K_w and py.time.get_ticks() - moment > 2000:  
                moment = py.time.get_ticks()
                laser = spri.Laser(space_ship.rect.center, pik_las) 
                more_lasers.append(laser) 
        
        if i.type == METEOR_EVENT:
            meteors = spri.meteorite((random.randint(0, sett.SIZE_X), 0), (random.randint(1,2)), random.randint(-1,1) , pik_meteors[random.randint(0,len(pik_meteors)- 1)])
            more_meteors.append(meteors)   
        

        if i.type == UPGRADE_EVENT:
            rand = random.randint(0,1) 
            upgrade = spri.Upgrade((random.randint(0 , sett.SIZE_X-2), 0), pik_ups[rand], rand)   
            more_up.append(upgrade) 

        if i.type == py.MOUSEBUTTONDOWN:
            if button.rect.collidepoint(i.pos):
                menu = 'игра'  
                space_ship.ship_life = 4  
                space_ship.check = 0
                space_ship.rect.center = 250, 500 
                more_meteors = []
                more_lasers = []
                more_up = [] 
            if button_2.rect.collidepoint(i.pos):
                stop = False
                

                

    if space_ship.ship_life == 0:
        menu = 'меню' 

    
        
        
    


    if menu == 'игра':
        wind.blit(pik, (0, 0)) 
        wind.blit(pik_new,(450,8)) 
        for i in more_lasers:
            i.draw(wind)
            i.update(0.25)  
            if i.rect.bottom <= 0: 
                more_lasers.remove(i) 
        space_ship.draw(wind) 
        space_ship.update(0.25) 
        font.render_to(wind, (8,8), str (space_ship.check)) 
        font.render_to(wind, (480, 8), str (space_ship.ship_life)) 
        for i in more_meteors:
            i.draw(wind)
            i.update() 
        destroyd_ship() 
        destroyd_meteors()
        for i in more_up:
            i.draw(wind) 
            i.update() 
        destroyd_upgrade()
    else:
        wind.blit(pik_menu,(0,0)) 
        button.draw(wind)
        button_2.draw(wind) 

    py.display.update()
   

    clock.tick(sett.FPS) 
