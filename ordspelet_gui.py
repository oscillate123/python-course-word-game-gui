from appJar import gui as gui
import ordspelet_file_handler as ofh
import ordspelet_game_funtions as ogf

# source: https://it-ord.idg.se/
# source: http://appjar.info/


class OrdspelGUI:
    # TABLE OF CONTENTS - CURRENT TAB
    """
    Current tab is for "Part 2" in the assignment. Where the User plays against the program.
    The Program is trying to figure out which word the User is thinking of. The Programs
    guesses are based on a random word from the self.word_list class attribute.

    Lines through the code indicates tab code areas


    """

    def __init__(self, word_list=None):
        # word_list=None, so we can use it if we have another words.txt file!
        # Otherwise, we will work with the one we have

        self.app = gui()
        self.word_list = word_list or ofh.file_reader("words.txt", encoding="ISO-8859-1")
        self.random_word = ogf.random_list_element(word_list=self.word_list)

    def go_gui(self):

        # CLASS VARIABLES
        app = self.app

        # BODY SETTINGS
        app.setSize(350, 400)
        app.setLocation(0, 200)
        app.setTitle("Ordspelet")

        # Y COORDINATE GROUPS (used for mass controlling column groups)
        y_group0 = 0
        y_group1 = 1
        y_group2 = 2
        y_group3 = 3

        # X COORDINATE GROUPS (used for mass controlling row groups)
        x_group0 = 0
        x_group1 = 1
        x_group2 = 2
        x_group3 = 3
        x_group4 = 4
        x_group5 = 5

        # TERMS AND CONDITIONS OF USING APPLICATION
        terms_n_cond_msg = "Det går inte att spela båda spelen samtidigt. Om du vill byta spelläge," \
                           " måste du klicka på återställ innan du kan påbörja ett nytt spel."
        app.errorBox(title="Villkor", message=terms_n_cond_msg)

        # ///// START TABBED FRAMES \\\\\
        app.startTabbedFrame("TabbedFrame")
        app.setTabbedFrameTabExpand("TabbedFrame", expand=True)

        #  ----------------------------------- TAB 1 ---------------------------------------

        # TABLE OF CONTENTS - TAB 1
        """
        Current tab is for "Part 1" in the assignment (Ordspelet.pdf). Where the Program plays against the User.
        The User is trying to figure out which word the Program chose. The User 
        guesses are based on the clues generated by the Program. The User will get suggestions on words

        1. TAB LOCAL SETTINGS - Configures settings of current tab
        2. TAB LOCAL VARIABLES - Local tab variables
        3. TAB LOCAL FUNCTIONS - Local tab functions, such as button presses & back end contact
        4. TAB LOCAL GROUPS - Gui widget groups, sorted by Y coordinated groups (vertical)
        5. TAB STOP - Where code for the current tab stops
        """

        # 1. TAB 1 LOCAL SETTINGS
        # 1.1 INIT TAB & TAB NAME
        app.startTab("Skynet vs. Användaren")

        # 2. TAB 1 LOCAL VARIABLES
        # 2.1 GUESS COUNTER
        app.guess_counter = 0  # used in the 'press'-function

        # 3. TAB 1 LOCAL FUNCTIONS
        # 3.1 PRESS FUNCTION
        def tab1_press(button_name):
            if button_name == " Skicka":
                usr_guess = app.getEntry('tab1_guess')
                if check_correct_input(usr_guess):
                    ran_wrd = self.random_word
                    gui_middleman_backend_gamemode1(random_word=ran_wrd, user_guess=usr_guess)
                    app.guess_counter += 1
                else:
                    incorrect_input_msg()
            elif button_name == " Avbryt":
                exit()
            elif button_name == " Återställ":
                clean_up()

        def gui_middleman_backend_gamemode1(random_word, user_guess):
            app.clearEntry(name='tab1_guess')
            response = ogf.parase_compare_random_and_guess(word=random_word, guess=user_guess)

            if response == "Rätt gissning!":
                ok_box(title="", msg=response)
                clean_up()
            else:
                app.setTextArea("tab1_1_TA1", text=f"\n{app.guess_counter} - {user_guess}\n")
                app.setTextArea("tab1_1_TA1", text=f"{response}\n")
                app.setLabel(f"tab1_2_L1", f"Antal gissningar: {app.guess_counter}")

        def check_correct_input(user_guess):
            if user_guess.isalpha():
                if len(user_guess) == 5:
                    return True
                else:
                    incorrect_input_msg()
                    return False
            else:
                incorrect_input_msg()
                return False

        def incorrect_input_msg():
            ok_box(title='Ogiltig indata', msg="Vänligen skriv ett ord med 5 unika bokstäver.")

        # 4 TAB 1 LOCAL GROUPS
        # 4.0 Y GROUP 0 // EMPTY SPACE
        # 4.0 - VARIABLES
        info_text = "Här ska du gissa vilket ord programmet har valt."

        # 4.0 - GUI WIDGETS
        app.addLabel(title="tab1_0_L0", column=y_group0, row=x_group0, colspan=3, text=info_text)
        app.addEmptyLabel("tab1_0_EL1", column=y_group0, row=x_group1)
        app.addEmptyLabel("tab1_0_EL2", column=y_group0, row=x_group2)
        app.addEmptyLabel("tab1_0_EL3", column=y_group0, row=x_group3)
        app.addEmptyLabel("tab1_0_EL4", column=y_group0, row=x_group4)

        # 4.1 Y GROUP 1 // WORD GUESS INPUT AND PROGRAM OUTPUT
        # 4.1 - VARIABLES
        tab1_button_names = [" Skicka", " Avbryt", " Återställ"]

        # 4.1 - GUI WIDGETS
        app.addLabel("tab1_1_L1", text="Användarens Gissnings Historik:", column=y_group1, row=x_group1)
        app.addScrolledTextArea("tab1_1_TA1", column=y_group1, row=x_group2)
        app.addAutoEntry(title="tab1_guess", words=self.word_list, column=y_group1, row=x_group3)
        app.addButtons(names=tab1_button_names, funcs=tab1_press, column=y_group1, row=x_group4)

        # 4.2 Y GROUP 2 // DISPLAY NUMBER OF GUESSES
        # 4.2 - GUI WIDGETS
        app.addLabel("tab1_2_L1", text=f"Antal gissningar: {app.guess_counter}", column=y_group2, row=x_group1)
        app.addEmptyLabel("tab1_2_EL2", column=y_group2, row=x_group2)
        app.addEmptyLabel("tab1_2_EL3", column=y_group2, row=x_group3)
        app.addEmptyLabel("tab1_2_EL4", column=y_group2, row=x_group4)

        # 4.3 Y GROUP 3 // EMPTY SPACE
        # 4.3 - GUI WIDGETS
        app.addEmptyLabel("tab1_3_EL0", column=y_group3, row=x_group0)
        app.addEmptyLabel("tab1_3_EL1", column=y_group3, row=x_group1)
        app.addEmptyLabel("tab1_3_EL2", column=y_group3, row=x_group2)
        app.addEmptyLabel("tab1_3_EL3", column=y_group3, row=x_group3)
        app.addEmptyLabel("tab1_3_EL4", column=y_group3, row=x_group4)

        # 5. TAB 1 STOP
        app.stopTab()

        #  -------------------------------- STOP TAB 1 -------------------------------------

        #  ----------------------------------- TAB 2 ---------------------------------------

        # TABLE OF CONTENTS - TAB 2
        """
        Current tab is for "Part 2" in the assignment (Ordspelet.pdf). Where the User plays against the program.
        The Program is trying to figure out which word the User is thinking of. The Programs 
        guesses are based on a random word from the self.word_list class attribute.
        
        1. TAB LOCAL SETTINGS - Configures settings of current tab
        2. TAB LOCAL VARIABLES - Local tab variables
        3. TAB LOCAL FUNCTIONS - Local tab functions, such as button presses & back end contact
        4. TAB LOCAL GROUPS - Gui widget groups, sorted by Y coordinated groups (vertical)
        5. TAB STOP - Where code for the current tab stops
        """

        # 1. TAB LOCAL SETTINGS
        # 1.1 INIT TAB & TAB NAME
        app.startTab("Användaren vs. Skynet")

        # 2. TAB LOCAL VARIABLES
        # 2.1 GUESS COUNTER
        app.guess_counter = 1  # used in the 'press'-function

        # 3. TAB LOCAL FUNCTIONS
        # 3.1 PRESS FUNCTION
        def tab2_press(button_name):
            if button_name == "Skicka":
                gui_middleman_backend_gamemode2(data=app.getEntry('clue'))
            elif button_name == "Avbryt":
                exit()
            elif button_name == "Återställ":
                app.guess_counter = 1  # TAB LOCAL VARIABLE resets to default button_name
                clean_up()  # the clean_up function restores balance to the universe.
                app.setLabel(f"2_L1", f"Antal gissningar: {app.guess_counter}")  # reset gui

        def gui_middleman_backend_gamemode2(data):
            # DATA IS USER INPUT
            if data.isdigit() and 0 <= int(data) <= 5:
                # USES Y GROUP 2
                app.setLabel(f"2_L1", f"Antal gissningar: {app.guess_counter}")
                app.guess_counter += 1

                parse_return = ogf.parse_compare_words_and_hints(words_list=self.word_list,
                                                                 skynet_guess=self.random_word,
                                                                 clue=data)
                self.random_word = parse_return[0]
                self.word_list = parse_return[1]

                if len(self.word_list) > 0:
                    # USES Y GROUP 1
                    app.setTextArea("1_TA1", end=True, text=f"\n{app.guess_counter} - {self.random_word}")
                    app.clearEntry(name="clue")

                else:
                    ok_box(title="", msg="Programmet har slut på ord i sin lista.")
                    clean_up()

            elif data.lower() == "rätt":
                ok_box(title="", msg=f"Programmet gissade rätt ord. Ordet var {self.random_word}")
                clean_up()
                app.guess_counter = 1

            else:
                err_msg = 'Skriv antal rätt bokstäver med en siffra, eller "rätt" om ordet är rätt.'
                ok_box(title="Ogiltig indata", msg=err_msg)
                app.clearAllEntries()

        # 4 TAB LOCAL GROUPS
        # 4.0 Y GROUP 0 // EMPTY SPACE
        # 4.0 - VARIABLES
        info_text = "Tänk på ett ord. Skriv antal rätt bokstäver, eller om ordet är rätt."

        # 4.0 - GUI WIDGETS
        app.addLabel(title="0_L0", column=y_group0, row=x_group0, colspan=3, text=info_text)
        app.addEmptyLabel("0_EL1", column=y_group0, row=x_group1)
        app.addEmptyLabel("0_EL2", column=y_group0, row=x_group2)
        app.addEmptyLabel("0_EL3", column=y_group0, row=x_group3)
        app.addEmptyLabel("0_EL4", column=y_group0, row=x_group4)

        # 4.1 Y GROUP 1 // WORD GUESS OUTPUT AND USER INPUT
        # 4.1 - VARIABLES
        button_names = ["Skicka", "Avbryt", "Återställ"]
        info_text = "Tänk på ett ord. Skriv antal rätt bokstäver, eller om ordet är rätt."

        # 4.1 - GUI WIDGETS
        app.addLabel("1_L1", text="Programmets Gissnings Historik:", column=y_group1, row=x_group1)
        app.addScrolledTextArea("1_TA1", column=y_group1, row=x_group2)
        app.addEntry(title="clue", column=y_group1, row=x_group3)
        app.addButtons(names=button_names, funcs=tab2_press, column=y_group1, row=x_group4)

        # 4.1 - SETTINGS
        app.setTextArea("1_TA1", text=f"{app.guess_counter} - {self.random_word}")

        # 4.2 Y GROUP 2 // DISPLAY NUMBER OF GUESSES
        # 4.2 - GUI WIDGETS
        app.addLabel("2_L1", text=f"Antal gissningar: {app.guess_counter}", column=y_group2, row=x_group1)
        app.addEmptyLabel("2_EL2", column=y_group2, row=x_group2)
        app.addEmptyLabel("2_EL3", column=y_group2, row=x_group3)
        app.addEmptyLabel("2_EL4", column=y_group2, row=x_group4)

        # 4.3 Y GROUP 3 // EMPTY SPACE
        # 4.3 - GUI WIDGETS
        app.addEmptyLabel("3_EL0", column=y_group3, row=x_group0)
        app.addEmptyLabel("3_EL1", column=y_group3, row=x_group1)
        app.addEmptyLabel("3_EL2", column=y_group3, row=x_group2)
        app.addEmptyLabel("3_EL3", column=y_group3, row=x_group3)
        app.addEmptyLabel("3_EL4", column=y_group3, row=x_group4)

        # 5 TAB 2 STOP
        app.stopTab()

        #  -------------------------------- STOP TAB 2 -------------------------------------

        # \\\\\ STOP TABBED FRAMES /////
        app.stopTabbedFrame()

        # VERSITILE LOCAL FUNCTIONS:
        def clean_up():
            app.guess_counter = 1
            self.word_list = ofh.file_reader("words.txt", encoding="ISO-8859-1")  # restore to its default content
            self.random_word = ogf.random_list_element(word_list=self.word_list)  # random from restored word_list
            app.clearAllTextAreas()
            app.clearAllEntries()
            app.setTextArea("1_TA1", text=f"\n{app.guess_counter} - {self.random_word}")
            app.setLabel(name=f"tab1_2_L1", text=f"Antal gissningar: 0")

        def ok_box(title, msg):
            app.okBox(title=f"{title}", message=f"{msg}")

        # RUNS GUI APPLICATION
        app.go()


if __name__ == "__main__":
    # file_content = ofh.file_reader(read_file="words.txt", encoding='ISO-8859-1')  # returns list
    # generated_word = ogf.random_list_element(word_list=file_content)

    print("activated")
    x = OrdspelGUI()
    x.go_gui()
