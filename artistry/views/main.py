from artistry import app
from flask import render_template, redirect, request, send_file
from artistry.core.lyrics import find_lyrics
import networkx as nx
import matplotlib.pyplot as plt
from io import BytesIO
import base64


@app.route("/")
def index():
    return redirect("/search_artist/")


@app.route("/search_artist/", methods=["GET", "POST"])
def searchArtist():
    if request.method == "POST":
        # artistLyrics = find_lyrics(request.form["artistName"])
        # return render_template("artist_info.html",
        #                        artistLyrics=artistLyrics)
        G = nx.Graph()
        G.add_edge("Eminem", "Sang3o")
        G.add_edge("Eminem", "50 Cent")
        G.add_edge("Eminem", "2 Pac")
        nx.draw(G, with_labels=True)
        img = BytesIO()
        plt.savefig(img)
        pngImageB64String = "data:image/png;base64,"
        pngImageB64String += base64.b64encode(img.getvalue()).decode('utf8')
        img.seek(0)
        plt.clf()
        return render_template("artist_info.html", img=pngImageB64String)

    return render_template("search_artist.html")
