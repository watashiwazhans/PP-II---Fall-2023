from itertools import permutations 
def Perm(n):
    newlist = [n[i] for i in range(0, len(n))]
    newlist.sort()
    perm = permutations(newlist)
    for permutation in perm:
        print(permutation)
n = str(input())
Perm(n)   
