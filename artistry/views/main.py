from artistry import app
from flask import render_template, redirect, request
from artistry.core.graph import getGraph


@app.route("/")
def index():
    return redirect("/search_artist/")


@app.route("/search_artist/", methods=["GET", "POST"])
def searchArtist():
    if request.method == "POST":
        referenceCount = {"Donald Trump": 3, "2Pac": 5, "Snoop Dogg": 11}
        img = getGraph(request.form["artistName"], referenceCount)
        return render_template("artist_info.html", img=img)

    return render_template("search_artist.html")
