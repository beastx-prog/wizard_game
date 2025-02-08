import pygame
import random

pygame.init()
pygame.font.init()
pygame.font.get_init()

clock=pygame.time.Clock()

screen=pygame.display.set_mode((1472,832))
white_color=(255,255,255)


#loading images
strt_btn=pygame.image.load('start_btn.png')
bg_image=pygame.image.load('dun_bg.png')
exit_btn=pygame.image.load('exit_btn.png')
yes_btn=pygame.image.load('yes.png')
stone_image=pygame.image.load('stone.png')


#text
font1=pygame.font.Font('ork-slayer.ttf',80)
text1=font1.render('DUNGEONS',True,(255,255,255))
text1rec=text1.get_rect()
text1rec.center=((500,250)) 



class SpritSheet():
    def __init__(self,image):
        self.sheet=image
    def get_image(self,frame,width,height,scale,colour):
        image=pygame.Surface((width,height)).convert_alpha()
        image.blit(self.sheet,(0,0),((frame*width),0,width,height))
        image=pygame.transform.scale(image,(width*scale,height*scale))
        image.set_colorkey(colour)
        return image  
        
class Button():
    def __init__(self,x,y,image,scale):
        width=image.get_width()
        height=image.get_height()
        self.image=pygame.transform.scale(image,(int(width*scale),int(height*scale)))
        self.rect=self.image.get_rect() 
        self.rect.topleft=(x,y) 
        self.clicked=False

    def draw(self):
        action=False
        pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(pos): 
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                self.clicked=True 
                action=True
        if pygame.mouse.get_pressed()[0]==0:
            self.clicked=False                          

                               
        screen.blit(self.image,(self.rect.x,self.rect.y))
        return action

#creating an image controller

class image_controller():
    def __init__(self,x,y,image,scale):
        width=image.get_width()
        height=image.get_height()
        self.image=pygame.transform.scale(image,(int(width*scale),int(height*scale)))
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
    def draw(self):
        screen.blit(self.image,(self.rect.x,self.rect.y))

def yes():
    pygame.init()
    global SpritSheet
    sprite_sheet_image=pygame.image.load('closing screen.png')
    sprite_sheet=SpritSheet(sprite_sheet_image)
    


    animation_list= []
    animation_steps=22
    last_update=pygame.time.get_ticks()
    animation_cooldown=560
    frame=0


    screen3=pygame.display.set_mode((1500,900))

    def player_screen():
        global run
        #definig stones
        stone_img=image_controller(0,0,stone_image,2.5)
        screen4=pygame.display.set_mode((1000,800))
        while run:
            screen4.fill((255,255,255))
            stone_img.draw()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
                    exit()
            pygame.display.update()
        pygame.display.update() 


    for i in range(animation_steps):
        animation_list.append(sprite_sheet.get_image(i,1000,790,1.3,(0,0,0)))
    run=True
    while run:
        screen3.fill((0,0,0))
        n=random.randrange(1,1050)
        v=random.randrange(1,1050)
        if n-v >= animation_cooldown:
            frame+=1
            if frame >= len(animation_list):
                frame=0
                if frame==0:
                    player_screen()
        screen3.blit(animation_list[frame],dest=(20,5))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()

#retrieving images from sprite sheet

sprite_sheet_image=pygame.image.load('wiz nimation.png')
sprite_sheet=SpritSheet(sprite_sheet_image)


animation_list= []
animation_steps=18
last_update=pygame.time.get_ticks()
animation_cooldown=560


for i in range(animation_steps):
    animation_list.append(sprite_sheet.get_image(i,150,150,5,(0,0,0)))

#defining play function
def play():
    global white_color
    screen2=pygame.display.set_mode((1472,900))
    font2=pygame.font.Font('ork-slayer.ttf',35)
    text2=font2.render('Come forth warrior',True,(white_color))
    text2rec=text2.get_rect()
    text2rec.center=((200,300))
    font3=pygame.font.Font('ork-slayer.ttf',35)
    text3=font3.render('do you wish to go forward',True,white_color)
    text3rec=text3.get_rect()
    text3rec.center=((200,400))

    frame=0
    run=True
    while run:
        screen2.fill((0,0,0))
        screen2.blit(text2,text2rec.center)
        screen2.blit(text3,text3rec.center)
        if yes_button.draw()==True:
            yes()
            exit()
        
        n=random.randrange(1,850)
        v=random.randrange(1,850)
        if n-v >= animation_cooldown:
            frame+=1
            if frame >= len(animation_list):
                frame=0
        screen.blit(animation_list[frame],(950,50))
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run=False
                
        pygame.display.update()
        
    

#defining buttons
play_button=Button(50,100,strt_btn,0.7)
exit_button=Button(50,200,exit_btn,0.7)
yes_button=Button(300,430,yes_btn,2.0)

#main screen/loop
run=True
while run:

    screen.fill(white_color)
    screen.blit(bg_image,dest=(0,0))
    screen.blit(text1,text1rec.center)
    if play_button.draw():
        play()
        exit()
       
    if exit_button.draw():
        run=False
        exit()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.display.update()
    