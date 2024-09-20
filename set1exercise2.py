#Squares Problem 

from math import floor
tiles = int(input("How many tiles do you have?: "))

answer = tiles ** 0.5
answer = floor(answer)

print(f"The maximum side length is {answer}")