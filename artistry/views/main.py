from artistry import app
from flask import render_template, redirect, request
from artistry.core.lyrics import find_lyrics
import networkx as nx
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from io import BytesIO
import base64


def getImg(artistName):
    G = nx.Graph()
    G.add_edge(artistName, "Sang3o")
    G.add_edge(artistName, "50 Cent")
    G.add_edge(artistName, "2 Pac")
    nx.draw(G, with_labels=True)
    img = BytesIO()
    plt.savefig(img)
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(img.getvalue()).decode('utf8')
    img.seek(0)
    plt.clf()
    return pngImageB64String


@app.route("/")
def index():
    return redirect("/search_artist/")


@app.route("/search_artist/", methods=["GET", "POST"])
def searchArtist():
    if request.method == "POST":
        # artistLyrics = find_lyrics(request.form["artistName"])
        # return render_template("artist_info.html",
        #                        artistLyrics=artistLyrics)
        return render_template("artist_info.html",
                               img=getImg(request.form["artistName"]))

    return render_template("search_artist.html")
