import os

def main():
    os.system("clear")
    menu = input("kiadás hozzáadása: 1 || Pénz megtekintése: 2 || kilép: 3: ")
    if menu != "1" or menu != "2" or menu != "3":
        main()
    else:
        if menu == "1":
            kiadas()
    
def kiadas():
    os.system("clear")
    print("Kiadás hozzáadása")



if __name__ == "__main__":
    main()