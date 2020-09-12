from artistry import app
from flask import render_template, redirect, request
from artistry.core import find_lyrics


@app.route("/")
def index():
    return redirect("/search_artist/")


@app.route("/search_artist/", methods=["GET", "POST"])
def searchArtist():
    if request.method == "POST":
        artistLyrics = find_lyrics(request.form["artistName"])
        return render_template("artist_info.html",
                               artistLyrics=artistLyrics)
    return render_template("search_artist.html")
