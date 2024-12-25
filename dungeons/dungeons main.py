import pygame
pygame.init()
pygame.font.init()
pygame.font.get_init()


screen=pygame.display.set_mode((1472,832))
clock=pygame.time.Clock()
color=(255,255,85)

play_image=pygame.image.load('start_btn.png')
bg_image=pygame.image.load('dun_bg.png')

quit_image=pygame.image.load('exit_btn.png')
char_image=pygame.image.load('hg.png')



font1=pygame.font.Font('ork-slayer.ttf',80)
text1=font1.render('DUNGEONS',True,(255,255,255))
text1rec=text1.get_rect()
text1rec.center=((500,250)) 

run=True



def play():
    run=True
    
    while run:
        screen.fill((0,0,0))


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
        pygame.display.update()

def menu():
    
    while run:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
        pygame.display.update()


class button():


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

play_button=button(100,100,play_image,0.7)

quit_button=button(100,200,quit_image,0.7)
run = True




while run:
    
    
  
    screen.fill(color)
    screen.blit(bg_image,dest=(0,0))
    screen.blit(text1,text1rec.center)
    
    if play_button.draw():
        play()
        pygame.quit()
    if quit_button.draw():
        run=False
    
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
    pygame. display.update()
pygame.display.update()
