#proov
import pygame, random

pygame.init()

aken = pygame.display.set_mode([1024, 768])
aken.fill([0,0,0])

taust1 = pygame.image.load("taust1.1.jpg")
aken.blit(taust1, (0,0))

ufo_ruum = pygame.image.load("tulnukate ruum1.3.jpg")
ajaloo_ruum = pygame.image.load("ajaloo ruum1.1.jpg")
krimi_ruum = pygame.image.load("krimiruum1.3.jpg")

mäng_töötab = True

tegelane = pygame.image.load("tydruk.png")
tegelase_x = 500
tegelase_y = 20
tegelase_x_kiirus = 0 #kiirus x teljel e kui kiiresti lind liigub horisontaalselt
tegelase_y_kiirus = 0 #kiirus y teljel e kui kiiresti lind liigub vertikaalselt
tegelase_baaskiirus = 150

kell = pygame.time.Clock()

def vahetatausta(taust):
    aken.blit(taust, (0,0))
praegune_taust = taust1
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
    
pygame.quit()
