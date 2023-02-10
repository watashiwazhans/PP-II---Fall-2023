def highScoreMov():
    for i in range(len(movies)):
        if movies[i]["imdb"] > 5.5:
            movss.append(movies[i])
    print(movss)

movss = []

highScoreMov()