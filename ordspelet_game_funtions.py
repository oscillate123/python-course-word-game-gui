import random
import ordspelet_parse_user_guess as parse


def filter_word_list(word_list, robot_guess, clue):
    # source: find_related_words_source.jpg
    # The picture originates from a discussion with my teacher,
    # regarding how to improve/optimize my function.

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


def random_from_list(word_list):
    # generates a random word from the parameter word_list
    # source: https://docs.python.org/3/library/random.html
    # random.sample generates a list. Therefor we can point
    # out the value with index indication at the end.

    the_random_word = random.sample(word_list, 1)[0]

    return the_random_word


def new_random_and_list(words_list, skynet_guess, clue):
    # game mode where program is guessing, and where user is giving clues

    word_list = words_list
    word_list.remove(skynet_guess)

    new_list = filter_word_list(word_list=words_list, robot_guess=skynet_guess,
                                clue=clue)

    if len(new_list) > 0:
        r_word = random_from_list(new_list)
    else:
        r_word = ""
        new_list = []

    return [r_word, new_list]


def compare_random_with_guess(word, guess):
    parse_run = parse.StringChecker(guess=guess, word=word)
    response = parse_run.check_if_correct()
    return response
