'''def solve(numheads, numlegs):
    all_heads = 35;
    all_legs = 94;
    #4x + 2y = 94
    #x + y = 35
    second_step = all_legs - 2 * all_heads
    #2x = 24
    third_step = second_step // 2
    #here we have the number of rabbits = 12
    fourth_step = 35 - third_step
    #here we have the number of chickens = 23
    print(numheads, third_step)
    print(numlegs, fourth_step)
solve("The number of rabbits :", "The number of chickens :")
'''
def solve(numheads, numlegs):

    rabbits = int((numlegs - 35 * 2) / 2)
    chickens = int(numheads - rabbits)

    return rabbits, chickens

numheads = int(input())
numlegs = int(input())

print(solve(numheads, numlegs))