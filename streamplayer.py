import streamlit as st 
import os
import random

s=0
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

def Play(i):
    global s
    s = i
    st.audio(f"./songs/{new_list[i]}",format = "audio/mp3")

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



