def imdbAvg():
    for i in movies:
        avg = sum(j["imdb"] for j in movies)/len(movies)
    print(avgg)

avgg = 0
imdbAvg()