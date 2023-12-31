import pygame as pg
import os
import random

pg.mixer.init()
pg.mixer.music.set_volume(0.5)

s=0
start = 0
songs =[]
new_list = []
for song in os.listdir("./songs/"):
    songs.append(song)
for i in range(len(songs)):
    ran = random.choice(songs)
    new_list.append(ran)
    songs.remove(ran)

def get_songs():
    return new_list

def queueSong(i):
    n=i+1
    while(n<len(new_list)):
        pg.mixer.music.queue(f"./songs/{new_list[n]}")
        n=n+1

def loadSong(i):
    if(i>=len(new_list)):
        i=0
    global s
    s = i
    pg.mixer.music.load(f"./songs/{new_list[i]}")
    global start
    start=1
    queueSong(i)

def playSong():
    pg.mixer.music.play()

def pauseSong():
    pg.mixer.music.pause()

def resume():
    pg.mixer.music.unpause()

def previousSong():
    global s
    if(s!=0):
        s = s-1
        Play(s)
    else:
        Play(0)


def nextSong():
    global s
    if(s!=len(new_list)):
        s=s+1
        Play(s)
    else:
        Play(0)


def getVolume():
    return pg.mixer.music.get_volume()

def setVolume(volume):
    pg.mixer.music.set_volume(volume)

def getPos():
    return pg.mixer.music.get_pos()

def getState():
    return pg.mixer.music.get_busy()

def Started():
    if start == 0:
        Start = False
    if start == 1:
        Start = True
    return Start

def Play(song):
    loadSong(song)
    playSong()