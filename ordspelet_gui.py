from appJar import gui as gui
import ordspelet_file_handler as handler
import ordspelet_game_funtions as functions

# source: https://it-ord.idg.se/
# source: http://appjar.info/


class OrdspelGUI:
    # TABLE OF CONTENTS
    """
    The program is a word game application. In User vs. Skynet, the Skynet has chosen a word,
    and the user is going to try to find out which word it is. In Skynet vs. User, the user
    thinks of a word, and the Skynet is going to try to find out which word it is. The Skynet's
    word dictionary is from a text file, called "words.txt" in the repository.



    1. INIT
    2. GUI METHOD - This runs the whole show
        2.1 TAB 1 - Has its own Table of Contents
        2.2 TAB 2 - Has its own Table of Contents
        2.3 Method functions, used for saving space in the GUI code
        2.4 Starts the GUI
    """

    def __init__(self, word_list=None):
        # word_list=None, so we can use it if we have another words.txt file!
        # Otherwise, we will work with the one we have

        self.app = gui()
        self.word_list = word_list or handler.file_reader("words.txt", encoding="ISO-8859-1")
        self.random_word = functions.random_from_list(word_list=self.word_list)

    def gui_application(self):

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

        # TERMS AND CONDITIONS OF USING APPLICATION
        terms_n_cond_msg = "Det går inte att spela båda spelen samtidigt. Om du vill byta spelläge," \
                           " måste du klicka på återställ innan du kan påbörja ett nytt spel."
        app.errorBox(title="Villkor", message=terms_n_cond_msg)

        # ///// START TABBED FRAMES \\\\\
        app.startTabbedFrame("TabbedFrame")
        app.setTabbedFrameTabExpand("TabbedFrame", expand=True)

        #  ------------------------------- START TAB 1 -------------------------------------

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
                if control_input(usr_guess):
                    ran_wrd = self.random_word
                    tab1_control_if_correct(random_word=ran_wrd, user_guess=usr_guess)
                    app.guess_counter += 1
                else:
                    incorrect_input_msg()
            elif button_name == " Avbryt":
                exit()
            elif button_name == " Återställ":
                clean_up()

        def tab1_control_if_correct(random_word, user_guess):
            app.clearEntry(name='tab1_guess')
            response = functions.compare_random_with_guess(word=random_word, guess=user_guess)

            if response == "Rätt gissning!":
                ok_box(title="", msg=response)
                clean_up()
            else:
                app.setTextArea("tab1_1_TA1", text=f"\n{app.guess_counter} - {user_guess}\n")
                app.setTextArea("tab1_1_TA1", text=f"{response}\n")
                app.setLabel(f"tab1_2_L1", f"Antal gissningar: {app.guess_counter}")

        def control_input(user_guess):
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

        # 4. TAB 1 LOCAL GROUPS
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

        #  ------------------------------- START TAB 2 -------------------------------------

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
                tab2_control_if_correct(user_input=app.getEntry('clue'))
            elif button_name == "Avbryt":
                exit()
            elif button_name == "Återställ":
                app.guess_counter = 1  # TAB LOCAL VARIABLE resets to default button_name
                clean_up()  # the clean_up function restores balance to the universe.
                app.setLabel(f"2_L1", f"Antal gissningar: {app.guess_counter}")  # reset gui

        def tab2_control_if_correct(user_input):
            # DATA IS USER INPUT

            if user_input.lower() == "rätt":
                ok_box(title="", msg=f"Programmet gissade rätt ord. Ordet var {self.random_word}")
                app.guess_counter = 1
                clean_up()

            elif len(user_input) == 2 and any(char.isdigit() for char in user_input if 0 <= int(char) <= 5):
                get_new_random_and_list(data=user_input)

            else:
                tab2_error_box()
                app.clearAllEntries()

        def get_new_random_and_list(data):
            # USES Y GROUP 2
            app.guess_counter += 1
            app.setLabel(f"2_L1", f"Antal gissningar: {app.guess_counter}")

            self.random_word, self.word_list = functions.new_random_and_list(words_list=self.word_list,
                                                                             skynet_guess=self.random_word,
                                                                             clue=data)

            control_if_list_empty(check_list=self.word_list)

        def control_if_list_empty(check_list):
            if len(check_list) > 0:
                # USES Y GROUP 1
                app.setTextArea("1_TA1", end=True, text=f"\n{app.guess_counter} - {self.random_word}")
                # app.setLabel(name=f"tab1_2_L1", text=f"Antal gissningar: {app.guess_counter}")
                app.clearEntry(name="clue")

            else:
                ok_box(title="", msg="Programmet har slut på ord i sin lista.")
                clean_up()

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
            self.word_list = handler.file_reader("words.txt", encoding="ISO-8859-1")  # restore to its default content
            self.random_word = functions.random_from_list(word_list=self.word_list)  # random from restored word_list
            app.clearAllTextAreas()
            app.clearAllEntries()
            app.setTextArea("1_TA1", text=f"\n{app.guess_counter} - {self.random_word}")
            app.setLabel(name=f"tab1_2_L1", text=f"Antal gissningar: 0")
            app.setLabel(name=f"2_L1", text=f"Antal gissningar: {app.guess_counter}")

        def ok_box(title, msg):
            app.okBox(title=f"{title}", message=f"{msg}")

        def tab2_error_box():
            err_msg = 'Skriv antalet bokstäver som är på rätt plats ' \
                      'följt av en siffra som indikerar hur många bokstäver som är rätt ' \
                      'men på fel plats. T.ex. "13" - betyder att en bokstav är på rätt plats,' \
                      ' och tre bokstäver är rätt men på fel plats.' \
                      ' Om ordet är rätt, så skriv rätt.'
            ok_box(title="Ogiltig indata", msg=err_msg)

        # RUNS GUI APPLICATION
        app.go()
