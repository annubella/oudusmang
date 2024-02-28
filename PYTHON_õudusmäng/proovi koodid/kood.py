#proov
import pygame, random, sys

pygame.init()

aken = pygame.display.set_mode([1024, 768])
aken.fill([255,0,0])

startpilt = pygame.image.load("start.jpg")

#heli
tausta_heli = pygame.mixer.music.load("oudusmangu_heli.mp3")
kaotus = pygame.mixer.Sound("kaotus.wav")
võit = pygame.mixer.Sound("voit.wav")


###
mängu_algus = True
mäng_töötab = True
mangulopp = False
manguvoit = False
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
    

taust1 = pygame.image.load("taust1.1.jpg")
aken.blit(taust1, (0,0))

ufo_ruum = pygame.image.load("tulnukate ruum1.3.jpg")
ajaloo_ruum = pygame.image.load("ajaloo ruum1.1.jpg")
krimi_ruum = pygame.image.load("krimiruum1.3.jpg")

tegelane = pygame.image.load("tydruk.png")
tegelase_x = 500
tegelase_y = 20
tegelase_x_kiirus = 0 
tegelase_y_kiirus = 0 
tegelase_baaskiirus = 150

def vahetatausta(taust):
    aken.blit(taust, (0,0))
praegune_taust = taust1

kaotus = pygame.image.load("koletis.jpg")

pygame.mixer.music.play()
while mäng_töötab:
    dt = kell.tick() / 1000
    #sisendite kogumine ja töötlemine
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            mäng_töötab = False
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
    
    #liikumine ajaloo tuppa
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
    
    #liikumine sci-fi tuppa
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
    
    #liikumine krimi tuppa
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

pygame.quit()
