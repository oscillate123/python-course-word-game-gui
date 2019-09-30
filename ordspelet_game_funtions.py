import random
import ordspelet_parse_user_guess as pug


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


def parase_compare_random_and_guess(word, guess):
    run = pug.ParseGuess(guess=guess, word=word)
    response = run.run_parse()
    return response
