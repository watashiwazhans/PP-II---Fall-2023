def getCateg():
    for i in range(len(movies)):
        if movies[i]["category"] == "Thriller":
            print(movies[i])

getCateg()