def imdbCatAvg():
    for i in range(len(movies)):
        if movies[i]["category"] == catt:
            movss.append(movies[i])
    avge = sum(j["imdb"] for j in movss)/len(movss)
    print(avge)

catt = input()
movss = []
avge = 0
imdbCatAvg()