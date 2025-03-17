import pygame as py
import random
py.init()
py.font.init()
py.font.get_init()
screen=py.display.set_mode((1000,800))
# loading images


class SpritSheet():
    def __init__(self,image):
        self.sheet=image
    def get_image(self,frame,width,height,scale,colour):
        image=py.Surface((width,height)).convert_alpha()
        image.blit(self.sheet,(0,0),((frame*width),0,width,height))
        image=py.transform.scale(image,(width*scale,height*scale))
        image.set_colorkey(colour)
        return image  






sprite_sheet_image=py.image.load("ufo.png")
sprite_sheet=SpritSheet(sprite_sheet_image)


animation_list= []
animation_steps=4
last_update=py.time.get_ticks()
animation_cooldown=10
frame=0

for i in range(animation_steps):
    animation_list.append(sprite_sheet.get_image(i,26,26,3,(0,0,0)))


current=py.time.set_timer(0,100)
print(current)
run=True
while run:
    screen.fill((255,255,255))
    print(current)

    n=80
    v=random.randrange(10,71,10)
    if n-v >= animation_cooldown:
        frame+=1
        if frame >= len(animation_list):
            frame=0
        screen.blit(animation_list[frame],(50,50))

   
   
    for i in py.event.get():
        if i.type==py.QUIT:
            run=False
    py.display.update()


