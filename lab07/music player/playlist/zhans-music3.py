import pygame as pg
import os
from random import choice
pg.init()
pg.mixer.init()
w, h, fps = 450, 600, 60
is_running = True
screen = pg.display.set_mode((w, h))
pg.display.set_caption('Music Player')
clock = pg.time.Clock()
is_sing, begin = False, False
background_img = pg.image.load("C:\\Users\\Lenovo\\OneDrive\\Рабочий стол\\PP II\\lab07\\music player\\img\\2.jpg")
image = pg.image.load("C:\\Users\\Lenovo\\OneDrive\\Рабочий стол\\PP II\\lab07\\music player\\img\\1.png")
image = pg.transform.scale(image, (450, 600))
surf_1 = pg.Surface((380, 55))
global i 
i, vol = 0, 1
global musics
 #playlist
def load_music():
    songs = []
    list_of_music = os.listdir(r'C:\\Users\\Lenovo\\OneDrive\\Рабочий стол\\PP II\\lab07\\music player\\playlist\\')
    for files in list_of_music:
        if files.endswith('.mp3'):
            songs.append(files)
    return songs

musics = load_music()
 #listening to music
while is_running:
    clock.tick(fps)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False

        if event.type == pg.KEYDOWN: # play music -> to start music player
            if event.key == pg.K_p:
                begin = True
                music = choice(musics)
                i = musics.index(music)
                pg.mixer.music.load(music)
                pg.mixer.music.play()

            if event.key == pg.K_SPACE: # pause or unpouse music
                if not is_sing:
                    pg.mixer.music.unpause()
                else:
                    pg.mixer.music.pause()

            if event.key == pg.K_RIGHT and is_sing: # play next music
                if i == len(musics) - 1:
                    i = 0
                else:
                    i += 1
                pg.mixer.music.load(musics[i])
                pg.mixer.music.play()

            if event.key == pg.K_LEFT and is_sing: # play previous music
                if i == 0:
                    i = len(musics) - 1
                else:
                    i -= 1
                pg.mixer.music.load(musics[i])
                pg.mixer.music.play()
                
            if event.key == pg.K_UP: # increase or decrease the music volume
                vol += 0.5
                pg.mixer.music.set_volume(vol)
            if event.key == pg.K_DOWN:
                vol -= 0.5
                pg.mixer.music.set_volume(vol)

            if event.key == pg.K_q: # stop music and exit player
                pg.mixer.music.stop()
                is_running = False
            
    font = pg.font.SysFont('Tahoma', 19, True) 
    font1 = pg.font.SysFont('Tahoma', 15, False) 
    screen.fill('white')
    screen.blit(background_img, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(surf_1, (33, 395)) 
    surf_1.blit(background_img, (0, 0))    

    if begin:
        s = font.render(musics[i][:-4], True, 'white') 
        t = font1.render('...is playing now', True, 'white') 
        screen.blit(s, (74, 400)) 
        screen.blit(t, (74, 420))  

    if pg.mixer.music.get_busy() == 1:
        is_sing = True
    else:
        is_sing = False

    pg.display.flip()
pg.quit()