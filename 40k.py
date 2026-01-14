while True:
    print("Space marine chapter profiles")
    print("1. Imperial Fists")
    print("2. Black Templars")
    print("3. Exit")

    choice = input("Pick (1-3): ")

    if choice == "1":
        print("Imperial Fists info:")
        print("Primarch: Rogal Dorn")
        print("Codex: They follow it")
        print("Colors: Yellow")
        print("Known for: Fortifications")

    elif choice == "2":
        print("Black Templars info:")
        print("1Primarch: From Rogal Dorn")
        print("Codex: They don't follow it")
        print("Colors: Black/White")
        print("Known for: Crusades")

    elif choice == "3":
        print("For the Emperor")
        break

    else:
        print("Just pick 1, 2, or 3")