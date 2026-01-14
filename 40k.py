def main():
    while True:
        print("Welcome to the Space marine info files") #Mr passini will do number 60: Exorcists
        print("Here you'll learn about the basic information about every space marine chapter")
        print("Just choose a nummber that we have listed here")

        print("Space marine chapter profiles") #Streling will number 33:  Brazen Claws
        print("1. Imperial Fists")
        print("2. Black Templars")
        print("3. Exit")

        choice = input("Pick a number:")

        if choice == "1": #Carlos you are gonna be number 7: Angels of Defiance
            print("Imperial Fists info:")
            print("Primarch: Rogal Dorn")
            print("Codex: They follow it")
            print("Colors: Yellow")
            print("Known for: Fortifications")


        elif choice == "2": #Caden you will be number 57: Storm Giants
            print("Black Templars info:")
            print("Primarch: From Rogal Dorn")
            print("Codex: They don't follow it")
            print("Colors: Black/White")
            print("Known for: Crusades")


        elif choice == "3": #Jonas you will be number 71: Minotaurs
            print("For the Emperor")
            break

        else:
            print("Just pick 1, 2, or 3")



if __name__ == "__main__":
    main()