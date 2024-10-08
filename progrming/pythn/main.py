import os
from time import sleep

money = []


def main():
    os.system("clear")
    menu = input("kiadás hozzáadása: 1 || Pénz megtekintése: 2 || kilép: 3: ")
    if menu == "1":
        kiadas()
    elif menu == "2":
        lookmoney()
    elif menu == "3":
        pass
"""
3.10-es python-tól
match menu:
    switch 1:
        kiadas()
    switch 2:
        lookmoney()
"""


def kiadas():
    menu = input("Vissza: 1 || pénz hozzáadása: 2 || pénz torlése: 3: ")
    if menu == 1:
        main()
    elif menu == 2:
        money_ammount = input("Mennyi pénz szeretnél hozzáadni?: ")
        money.append(money_ammount)
        kiadas()
    elif menu == 3:
        print("Egyenlőre nem működik térj vissza később")
        sleep(10)
        kiadas()



def lookmoney():
    menu = input("Vissza: 1 || pénz megtekintése: 2: ")
    if menu == 1:
        main()
    elif menu == 2:
        print(f"\n-----------------\n{money}\n-------------------")


if __name__ == "__main__":
    main()