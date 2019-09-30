# In this class, we compare the user guess with the random generated word.
# We return True if the guess is the same as the random generated word.


class ParseGuess:
    def __init__(self, guess, word):
        self.guess = guess
        self.word = word

    def words_analyzer(self):
        # here we analyze/parse the two class attributes guess and word
        # source: https://qph.fs.quoracdn.net/main-qimg-dbe0252936d6b28a6644faa17953f9ef

        print_correct_pos = 0
        print_correct = 0

        for g_idx, g_char in enumerate(self.guess):
            if g_char in self.word and g_idx == self.word.index(g_char):
                # if the characters and character indexes are matching.
                print_correct_pos += 1

            elif g_char in self.word:
                print_correct += 1

        # Here we return the number of correct positions, and the number of correct letters
        return print_correct_pos, print_correct

    def run_parse(self):
        # compares the user guess with the chosen word

        if self.guess == self.word:
            return "Rätt gissning!"

        else:
            print_correct_pos, print_correct_letter = ParseGuess.words_analyzer(self)

            return_pos = f"{print_correct_pos} är rätt och är på rätt plats, "
            return_letter = f"och {print_correct_letter} är rätt men på fel plats."

            return return_pos + return_letter
