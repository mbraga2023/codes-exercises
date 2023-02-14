# TODO
from cs50 import get_int

while True:
    altura = get_int ("Altura da piramide: ")
    if altura >= 1 and altura <= 8:
        break

for i in range(altura):
    for j in range(altura):
        if(i+j>= altura-1):
            print("#", end="")
        else:
            print(" ", end="")
    print()