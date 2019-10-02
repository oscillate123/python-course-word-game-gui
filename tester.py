import ordspelet_game_funtions as ogf
import ordspelet_file_handler as ofh

word_list = ofh.file_reader("words.txt", encoding="ISO-8859-1")
random_word = ogf.random_from_list(word_list=word_list)

print(len(word_list))
print(random_word)

x = ogf.filter_word_list(word_list=word_list, robot_guess="alträ", clue="12")

print(x)
print(len(x))
