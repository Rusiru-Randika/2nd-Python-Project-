yeslist=["Y","y"]

lines = ["Mind Reading Project(Funny Project)",
        "This Phython Project By Rusiru Randika.",]

from time import sleep
import sys

for line in lines:
    for a in line:
        print(a, end='')
        sys.stdout.flush()
        sleep(0.1)
    print('')

print(" ")

def main():

    lines2 = ["Think of a Number                  :After Press Enter"]

    for line in lines2:
        for b in line:
            print(b, end='')
            sys.stdout.flush()
            sleep(0.1)
        input('')

    lines3 = ["Multiply by x2                     :After Press Enter"]

    for line in lines3:
        for c in line:
            print(c, end='')
            sys.stdout.flush()
            sleep(0.1)
        input('')

    import random

    test_list = [2, 4, 6, 8]

    n = random.choice(test_list)


    lines4 = [f"Add +{n}                             :After Press Enter"]

    for line in lines4: 
        for d in line:
            print(d, end='')
            sys.stdout.flush()
            sleep(0.1)
        input('')

    lines5 = ["Dvide by /2                        :After Press Enter"]

    for line in lines5:
        for e in line:
            print(e, end='')
            sys.stdout.flush()
            sleep(0.1)
        input('')


    lines6 = ["Reduce your first thought Number   :After Press Enter"]

    for line in lines6:
        for f in line:
            print(f, end='')
            sys.stdout.flush()
            sleep(0.1)
        input('')

    print('')

    lines7 = [f"Answer is {n/2}"]

    for line in lines7:
        for g in line:
            print(g, end='')
            sys.stdout.flush()
            sleep(0.1)
        print('')


    print("I think I read your Mind")

    restart=input("Do You Want to Start Again ?(Y/N) : ")

    print("")
    if restart in yeslist:
        main()
        print("")

    else:
        input("Goodbye...!!!")
        exit()

main()







