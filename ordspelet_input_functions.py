import ordspelet_game_explaination as game_exp


def player_input(the_answer):
    # user input_funcs, stored as a "guess" in the game
    # source: top comment https://stackoverflow.com/questions/19859282/check-if-a-string-contains-a-number/31861306
    # source: any section https://docs.python.org/3/library/functions.html#any

    while True:
        player_guess = input("\nGissa vilket ord det är: ")

        if player_guess == "ge upp" or player_guess == "surrender":
            print("Du har valt att avsluta spelet.")
            print(f"Ordet var: {the_answer}")
            exit()
        elif any(char.isdigit() for char in player_guess):
            print("Får enbart innehålla bokstäver.")
        elif len(player_guess) is not 5:
            print("Får enbart vara 5 bokstäver.")
        else:
            return player_guess.lower()  # no break or False point, because return jumps out of function.


def leader_input(random_word):
    # user input_funcs, returns an integer as a hint or a clue.
    # source: https://www.geeksforgeeks.org/python-string-isnumeric-application/

    print(f"Programmet gissar på att ordet är {random_word}")

    while True:
        correct_letter_amount = input("Hur många bokstäver är rätt?")

        if not any(char.isnumeric() for char in correct_letter_amount):
            print("Det får endast vara en siffra.")
        elif len(correct_letter_amount) > 1:
            print(f"Det får endast vara en siffra.")
        else:
            correct_letter_amount = int(correct_letter_amount)
            if correct_letter_amount == 5:
                is_it_right = input(f"Är {random_word} rätt ord?").lower()
                if is_it_right == "ja":
                    print(f"Programmet har gissat rätt ord. Ordet var {random_word}")
                    exit()
                return correct_letter_amount
            elif 5 > correct_letter_amount >= 0:
                return correct_letter_amount
            else:
                print("Det kan endast vara ett värde mellan 0-5")


def console_input():
    # user input_funcs, used for receiving commands, like starting the game etc
    # TODO - Ändra alternativen och kontrollera output
    commands = ["ge upp", "surrender", "leader", "player", "spelregler", "rules", "exit"]

    while True:
        print("\n ## Skriv 'cmd' om du vill se kommando-alternativen. ##")
        user_input = input("\nVill du vara leader eller player?\n")

        if user_input == "cmd":
            print(commands)

        elif user_input == "spelregler" or user_input == "rules":
            game_exp.get_game_description(boolean=True)

        elif user_input == "leader":
            return user_input

        elif user_input == "player":
            return user_input

        elif user_input == "exit":
            exit()
