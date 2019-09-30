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


def parse_compare_words_and_hints(words_list, skynet_guess, clue):
    # game mode where program is guessing, and where user is giving clues

    word_list = words_list
    word_list.remove(skynet_guess)

    new_list = find_related_words(word_list=words_list, robot_guess=skynet_guess,
                                  clue=int(clue))

    if len(new_list) > 0:
        r_word = random_list_element(new_list)
    else:
        r_word = ""
        new_list = []

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


