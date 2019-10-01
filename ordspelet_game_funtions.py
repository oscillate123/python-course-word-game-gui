import random
import ordspelet_parse_user_guess as pug


def find_related_words_v2(word_list, robot_guess, clue):
    # source: find_related_words_source.jpg
    # The picture originates from a discussion with my teacher,
    # regarding how to improve/optimize my function. Therefor v2

    results = []
    clue_p = clue[0]  # correct position
    clue_r = clue[1]  # correct letter, but not correct position

    for word in word_list:
        counter_p = 0  # correct position
        counter_r = 0  # correct letter, but not correct position
        for letter in word:
            if letter == robot_guess[word.index(letter)]:
                counter_p += 1
            elif letter in robot_guess:
                counter_r += 1
            else:
                pass

        if counter_r >= int(clue_r) and counter_p == int(clue_p):
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

    new_list = find_related_words_v2(word_list=words_list, robot_guess=skynet_guess,
                                     clue=clue)

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
