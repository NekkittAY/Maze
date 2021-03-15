import pygame
import random
class Cell(pygame.sprite.Sprite):
    def __init__(self,x,y,color):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.surface.Surface((10,10))
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.rect.centerx=x
        self.rect.centery=y

def shum():
    x=540
    y=240
    mass=[]
    for i in range(0,10):
        mass1=[]
        for j in range(0,10):
            gen=random.randint(0,1)
            mass1.append(gen)
            if gen==1:
                cell=Cell(x+10*i,y+10*j,(0,0,0))
            else:
                cell=Cell(x+10*i,y+10*j,(255,255,255))
            all_sprites.add(cell)
        mass.append(mass1)
    return mass
    
pygame.init()
screen=pygame.display.set_mode((1200,600))
running=True
clock=pygame.time.Clock()
all_sprites=pygame.sprite.Group()
world = []
for i in range(0,10):
    gen = shum()
    world.append(gen)
print(world)
gen=shum()
print(gen)
while running:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    screen.fill((150,150,150))
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
