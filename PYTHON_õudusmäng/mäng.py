#proov
import pygame, random, sys
from pygame.locals import *
import pygame_gui


pygame.init()

pygame.display.set_caption('The library nightmare')
aken = pygame.display.set_mode([1024, 768])
aken.fill([0,0,0])


taust1 = pygame.image.load("pildi_kaust/taust1.1.jpg")
aken.blit(taust1, (0,0))

#pildid
ufo_ruum = pygame.image.load("pildi_kaust/tulnukate ruum1.3.jpg")
ajaloo_ruum = pygame.image.load("pildi_kaust/ajaloo ruum1.1.jpg")
krimi_ruum = pygame.image.load("pildi_kaust/krimiruum1.3.jpg")
startpilt = pygame.image.load("pildi_kaust/start.jpg")
kaotuspilt = pygame.image.load("pildi_kaust/koletis.jpg")
võitpilt = pygame.image.load("pildi_kaust/voit2.jpg")
võti = pygame.image.load('pildi_kaust/voti.png')
võti_asukohtX = random.randint(1, 1024)
võti_asukohtY = random.randint(1, 768)
#tubade list
toad = [ufo_ruum, ajaloo_ruum, krimi_ruum]
suvaline_ruum = random.choice(toad)

#heli
tausta_heli = pygame.mixer.music.load("heli_kaust/oudusmangu_heli.mp3")
kaotus = pygame.mixer.Sound("heli_kaust/kaotus.wav")
võit = pygame.mixer.Sound("heli_kaust/voit.wav")
võit.set_volume(0.3)

mängu_algus = True
mäng_töötab = True
näita_nuppu = True
Click = False
kell = pygame.time.Clock()


while mängu_algus:
    aken.blit(startpilt, (0,0))
    pygame.display.flip()
    pygame.time.delay(5)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            mängu_algus = False
            mäng_töötab = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_RETURN:
                mängu_algus = False

tegelane = pygame.image.load("pildi_kaust/tydruk2.png")
tegelase_x = 500
tegelase_y = 20
tegelase_x_kiirus = 0 #kiirus x teljel e kui kiiresti lind liigub horisontaalselt
tegelase_y_kiirus = 0 #kiirus y teljel e kui kiiresti lind liigub vertikaalselt
tegelase_baaskiirus = 150



def vahetatausta(taust):
    aken.blit(taust, (0,0))
    
praegune_taust = taust1
pygame.mixer.music.play()
while mäng_töötab:
    MUSIC_END = pygame.USEREVENT+1
    pygame.mixer.music.set_endevent(MUSIC_END)
    dt = kell.tick() / 1000
    #sisendite kogumine ja töötlemine
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            mäng_töötab = False
        if e.type == MUSIC_END:
            print('music end event')
            aken.blit(kaotuspilt,(0,0))
            pygame.display.flip()
            kaotus.play()
            pygame.time.delay(9300)
            mäng_töötab = False
            
        if e.type == MOUSEBUTTONDOWN: 
            if e.button == 1: 
                Click = True 
#liikumine
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                tegelase_y_kiirus += -tegelase_baaskiirus
            if e.key == pygame.K_DOWN:
                tegelase_y_kiirus += tegelase_baaskiirus
            if e.key == pygame.K_LEFT:
                tegelase_x_kiirus += -tegelase_baaskiirus
            if e.key == pygame.K_RIGHT:
                tegelase_x_kiirus += tegelase_baaskiirus
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_UP:
                tegelase_y_kiirus -= -tegelase_baaskiirus
            if e.key == pygame.K_DOWN:
                tegelase_y_kiirus -= tegelase_baaskiirus
            if e.key == pygame.K_LEFT:
                tegelase_x_kiirus -= -tegelase_baaskiirus
            if e.key == pygame.K_RIGHT:
                tegelase_x_kiirus -= tegelase_baaskiirus
                

    #uuendame mängu olukorda
    tegelase_x += tegelase_x_kiirus * dt #asukoht x teljel muutub x telje kiiruse võrra
    tegelase_y += tegelase_y_kiirus * dt #asukoht y teljel muutub y telje kiiruse võrra
    #taUSTA VAHETUS
   # if näita_nuppu = True:
    if tegelase_y < 0 and praegune_taust == taust1:
        tegelase_y = tegelase_y + 5    
    if tegelase_x > 1024 and praegune_taust == taust1:
        tegelase_x = 0
        tegelase_y = 400
        praegune_taust = ajaloo_ruum
    elif tegelase_x < 0 and praegune_taust == ajaloo_ruum:
        tegelase_x = 1024
        tegelase_y = 300
        praegune_taust = taust1 
    elif tegelase_x > 1000 and praegune_taust == ajaloo_ruum:
        tegelase_x = tegelase_x - 5
    elif tegelase_y > 700 and praegune_taust == ajaloo_ruum:
        tegelase_y = tegelase_y - 5
    elif tegelase_y < 0 and praegune_taust == ajaloo_ruum:
        tegelase_y = tegelase_y + 5
        
    if tegelase_x < 0 and praegune_taust == taust1:
        tegelase_x = 1000
        tegelase_y = 400
        praegune_taust = ufo_ruum
    elif tegelase_x > 1024 and praegune_taust == ufo_ruum:
        tegelase_x = 0
        tegelase_y = 300
        praegune_taust = taust1
    elif tegelase_x < 0 and praegune_taust == ufo_ruum:
        tegelase_x = tegelase_x + 5
    elif tegelase_y > 700 and praegune_taust == ufo_ruum:
        tegelase_y = tegelase_y - 5
    elif tegelase_y < 0 and praegune_taust == ufo_ruum:
        tegelase_y = tegelase_y + 5
        
    if tegelase_y > 768 and praegune_taust == taust1:
        tegelase_x = 500
        tegelase_y = 450
        praegune_taust = krimi_ruum
    elif tegelase_y > 768 and praegune_taust == krimi_ruum:
        tegelase_x = 500
        tegelase_y = 450
        praegune_taust = taust1
    elif tegelase_x < 0 and praegune_taust == krimi_ruum:
        tegelase_x = tegelase_x + 5    
    elif tegelase_x > 1000 and praegune_taust == krimi_ruum:
        tegelase_x = tegelase_x - 5
    elif tegelase_y < 0 and praegune_taust == krimi_ruum:
        tegelase_y = tegelase_y + 5
          
    #joonistame uue olukorra 
    vahetatausta(praegune_taust)
    aken.blit(tegelane, [tegelase_x, tegelase_y])
    pygame.display.flip()
    pygame.time.delay(5)
    #võti asukoht
    if praegune_taust == suvaline_ruum:
        aken.blit(võti,(võti_asukohtX,võti_asukohtY))
               
        mx, my = pygame.mouse.get_pos() 
        MouseRect = pygame.Rect(mx,my,2,2)
        ButtonRect = pygame.Rect(võti_asukohtX,võti_asukohtY,30,30)  
        if MouseRect.colliderect(ButtonRect):
            if Click == True: 
                print('Somebody clicked me! :D')
                pygame.mixer.music.stop()
                aken.blit(võitpilt,(0,0))
                pygame.display.flip()
                võit.play()
                pygame.time.delay(9300)
                mäng_töötab = False
            
    pygame.display.update()
    pygame.display.flip()
    
pygame.quit()
sys.exit()