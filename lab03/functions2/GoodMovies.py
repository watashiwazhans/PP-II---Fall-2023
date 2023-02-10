from Movies import movies 
def highScoreMov():
    for i in range(len(movies)):
        if movies[i]["imdb"] > 5.5:
            return print(movies[i])
        
highScoreMov()