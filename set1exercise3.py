#Planked Fence 

from math import ceil 

section1 = input("How many fences in section 1? ")
section2 = input("How many fences in section 2? ")
section3 = input("How many fences in section 3? ")

cans = len(section1) + len(section2) + len(section3)
boxes = ceil(cans/12)
cost = boxes * 14.95

print(f"You need {cans} cans aka {boxes} box(es).\nThis will cost ${cost}.")