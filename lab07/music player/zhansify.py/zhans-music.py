import pygame as pg
import os
pg.init()
screen = pg.display.set_mode((600,600))
clock = pg.time.Clock()
player_icon = pg.transform.scale(pg.image.load("C:\\Users\\Lenovo\\OneDrive\\Рабочий стол\\PP II\\lab07\\music player\\img\\player_mp3.jpg"), (600,600))
game = False
current = 0
paused = True
musics = []
for i in os.listdir("C:\\Users\\Lenovo\\OneDrive\\Рабочий стол\\PP II\\lab07\\music player\\playlist"):
    music = pg.mixer.Sound( "C:\\Users\\Lenovo\\OneDrive\\Рабочий стол\\PP II\\lab07\\music player\\playlist\\" + str(i))
    musics.append(music)
    

while not game:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = True

        pressed = pg.key.get_pressed()   
          # start play music
        if pressed[pg.K_UP]:
            musics[current].play()
            paused = False
        #pause and unpause
        if pressed[pg.K_DOWN]:
            if paused == True:
                pg.mixer.unpause()
                paused = False
            elif paused == False:
                pg.mixer.pause()
                paused = True
            #next music
        if pressed[pg.K_RIGHT]:
            musics[current].stop()
            current += 1
            if current == len(musics) :
                current = 0
            musics[current].play()
        #prev music
        if pressed[pg.K_LEFT]:
            musics[current].stop()
            current -= 1
            if current <= -1:
                current = len(musics) - 1
            musics[current].play()

        # draw screen
        screen.blit(player_icon, (0,0))

        # display
        pg.display.flip()
        clock.tick(60)
        #close the window
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
pg.quit()
        
