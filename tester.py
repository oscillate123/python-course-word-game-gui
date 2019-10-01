import ordspelet_game_funtions as ogf
import ordspelet_file_handler as ofh

word_list = ofh.file_reader("words.txt", encoding="ISO-8859-1")
random_word = ogf.random_list_element(word_list=word_list)

print(len(word_list))
print(random_word)

x = ogf.find_related_words_v2(word_list=word_list, robot_guess="alträ", clue="12")

print(x)
print(len(x))
