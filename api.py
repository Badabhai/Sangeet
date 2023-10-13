from flask import Flask ,request,jsonify
import player as p

app = Flask(__name__)

@app.route('/')
def home():
    p.loadSong(0)
    p.playSong()
    return "Home"

@app.route("/pause")
def pause():
    p.pauseSong()
    return "Song Paused"

@app.route("/resume")
def resume():
    p.resume()
    return "Song Resumed"

@app.route("/next")
def next():
    p.nextSong()
    return "Next Song"

@app.route("/prev")
def prev():
    p.previousSong()
    return "Previous Song"


if __name__ == '__main__':
    app.run(debug=True)