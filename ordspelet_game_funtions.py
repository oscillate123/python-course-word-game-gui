import random
import ordspelet_parse_user_guess as pug
import ordspelet_input_functions as input_funcs


def find_related_words(word_list, robot_guess, clue):
    results = []

    for word in word_list:
        counter = 0
        for letter in word:
            if letter in robot_guess:
                counter += 1

        if counter >= clue:
            results.append(word)

    return results


def random_list_element(word_list):
    # generates a random word from the parameter word_list
    # source: https://docs.python.org/3/library/random.html
    # random.sample generates a list. Therefor we can point
    # out the value with index indication at the end.

    the_random_word = random.sample(word_list, 1)[0]

    return the_random_word


def leader(words_list):
    # game mode where program is guessing, and where user is giving clues
    counter_1 = 0
    word_list = words_list.copy()
    flag = True

    while flag:
        counter_1 += 1
        r_word = random_list_element(word_list)
        new_list = find_related_words(word_list=word_list, robot_guess=r_word, clue=input_funcs.leader_input(r_word))
        word_list = new_list
        new_list.remove(r_word)

        if len(new_list) == 0:
            print(f"Programmet ger upp.\n Programmet gissade {counter_1} gånger.")
            flag = False


def leader_gui(words_list, robot_guess, clue):
    # game mode where program is guessing, and where user is giving clues

    word_list = words_list
    print(len(word_list))
    word_list.remove(robot_guess)

    r_word = random_list_element(word_list)
    new_list = find_related_words(word_list=words_list, robot_guess=robot_guess,
                                  clue=int(clue))

    return [r_word, new_list]


def player(words_list):
    # game mode where user is guessing, and where program is giving clues
    counter_2 = 0
    flag = True
    random_word = random_list_element(word_list=words_list)

    while flag:
        counter_2 += 1
        user_guess = input_funcs.player_input(the_answer=random_word)
        run = pug.ParseGuess(guess=user_guess, word=random_word)
        run_done = run.run_game()

        if run_done:
            if counter_2 == 1:
                print(f"Du gissade bara {counter_2} gång!")
                flag = False
            else:
                print(f"Du gissade {counter_2} gånger.")
                flag = False
