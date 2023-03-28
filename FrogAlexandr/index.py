import pygame as p


class Frog:
    def __init__(self): 
        self.frog_piks = [] 
        for i in range(1,11):
            pik = p.image.load(f'FrogAlexandr/attack_{i}.png')
            self.frog_piks.append(pik) 
        self.rect = pik.get_rect() 
        self.rect.center = 150, 150 
        self.number = 0
    def animate(self):
        pass

    def draw(self, target_surf):
        target_surf.blit(self.frog_piks [int(self.number)], self.rect)
       

    def update(self, speed):
        self.number = self.number + speed   
        if self.number > 9:
            self.number = 0 

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300

p.init()
clock = p.time.Clock()
screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
p.display.set_caption('Frog')

frog = Frog()

running = True
while running:
    for event in p.event.get():
        if event.type == p.QUIT or (event.type == p.KEYDOWN
                                    and event.key == p.K_ESCAPE):
            running = False


    screen.fill((255, 255, 255))

    frog.update(0.25)
    frog.draw(screen)

    clock.tick(60)
    p.display.flip()

