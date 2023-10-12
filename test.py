import streamlit as st
import os
import random
import player as p

Home, Player, Search, Settings = st.tabs(["Home", "Player", "Search", "Settings"])

with Home:
    songs = p.get_songs()
    for i in range(len(songs)):
        if st.button(songs[i])==True:
            p.Play(i)
    

with Player:
    st.header("Player")

    Previous,Play,Next = st.columns(3)
    with Previous:
        if st.button("Previous"):
            p.previousSong()

    with Play:
        if st.button("Play"):
            state = p.getState()
            start = p.Started()
            if state == True:
                p.pauseSong()
            if(state == False) and (start == True):
                p.resume()
            if(state == False) and (start == False):
                p.Play(0)

    with Next:
        if st.button("Next"):
            p.nextSong()


    # pos = st.slider(five[i],0,value =p.getPos())

    volume = st.slider("Volume",0.0,1.0,value=p.getVolume())
    p.setVolume(volume)
    

with Settings:
    st.header("Settings")

with Search:
    st.header("Search")

