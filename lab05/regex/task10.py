import re 
def camel_to_snake(text):
    res = ""
    pattern = re.compile(r"[A-Z][a-z]+")
    words = pattern.findall(text)
    for i, word in enumerate(words):
        if i == 0:
            res += word.casefold()
        else:
            res += "_" + word.casefold()
    return res


def main():
    print("Task 1")
    print(pattern_1.search("fdskfldkflddsdsab"))

    print("Task 2")
    print(pattern_2.search("gjdfkabbbbfkkliu"))

    print("Task 3")
    print(pattern_3.findall("fdsfd_ fdjskfjdsk_ fdsf4ds_"))

    print("Task 4")
    print(pattern_4.findall("Ffdsf GGfgrhr ImknkJtr"))

    print("Task 5")
    print(pattern_5.search("kktngtag423b"))
    print(pattern_5.search("fjdjgfdb"))
    print(pattern_5.search("fdifafgnjgr3"))

    print("Task 6")
    text = "gfdjf,fhdsjh..fdskjf fjhgerj,. fds"
    print(pattern_6.sub(":", text))

    print("Task 7")

    print(snakeToCamel("hello_world_wordle"))

    print("Task 8")
    print(modify("OneTwoThree"))
    
    print("Task 9")
    print(spaces("HelloWordlOneMoreTime"))

    print("Task 10")
    print(camel_to_snake("SnakeCaseVar"))





if __name__ == "__main__":
    main()