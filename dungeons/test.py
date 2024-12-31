import pygame,random
pygame.init()
screen=pygame.display.set_mode((1900,1000))

image= pygame.image.load('closing screen.png')

class SpritSheet():
    def __init__(self,image):
        self.sheet=image
    def get_image(self,frame,width,height,scale,colour):
        image=pygame.Surface((width,height)).convert_alpha()
        image.blit(self.sheet,(0,0),((frame*width),0,width,height))
        image=pygame.transform.scale(image,(width*scale,height*scale))
        image.set_colorkey(colour)
        return image  
    
sprite_sheet_image=pygame.image.load('closing screen.png')
sprite_sheet=SpritSheet(sprite_sheet_image)


animation_list= []
animation_steps=22
last_update=pygame.time.get_ticks()
animation_cooldown=560
frame=0


for i in range(animation_steps):
    animation_list.append(sprite_sheet.get_image(i,1000,790,1.7,(0,0,0)))
run =True
while run:
    screen.fill((0,0,0))
    n=random.randrange(1,850)
    v=random.randrange(1,850)
    if n-v >= animation_cooldown:
        frame+=1
        if frame >= len(animation_list):
            frame=0
    screen.blit(animation_list[frame],(60,20))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.display.update()
