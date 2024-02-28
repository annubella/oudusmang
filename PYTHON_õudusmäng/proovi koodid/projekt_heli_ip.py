#mängu heli kood
import pygame, sys

pygame.init()
aken = pygame.display.set_mode([1024,768])

tausta_heli = pygame.mixer.music.load("oudusmangu_heli.mp3")
pygame.mixer.music.play(-1)

kaotus = pygame.mixer.Sound("kaotus.wav")
võit = pygame.mixer.Sound("voit.wav")

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #Järgmine koodijupp on vaid võidu ja kaotuse testimiseks, kuna need peaksid võidu/kaotuse koodi minema!
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_f:
                kaotus.play()
            if i.key == pygame.K_g:
                võit.play()
