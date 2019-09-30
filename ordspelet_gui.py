from appJar import gui as gui
import ordspelet_file_handler as ofh
import ordspelet_game_funtions as ogf

# source: https://it-ord.idg.se/
# source: http://appjar.info/


class OrdspelGUI:

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

        # ///// START TABBED FRAMES \\\\\
        app.startTabbedFrame("TabbedFrame")
        app.setTabbedFrameTabExpand("TabbedFrame", expand=True)

        # TODO -------------------------------- NEW TAB --------------------------------------

        # TAB VARIABLES

        # LABEL COUNTER
        # app.label_counter = 1

        # TAB FUNCTIONS

        # FUNCTION FOR AUTO-GENERATE A NUMBER - OLD FUNCTION TODO DELETE?
        def label_picker():
            if app.label_counter == 1:
                app.label_counter += 1
                return 1
            elif app.label_counter == 2:
                app.label_counter += 1
                return 2
            elif app.label_counter == 3:
                app.label_counter += 1
                return 3
            elif app.label_counter == 4:
                app.label_counter = 1
                return 4

        # TAB NAME
        app.startTab("Skynet vs. Användaren")

        app.addLabel("ti_pro_usr", f"saker med grejer", column=0, row=0)
        app.addEmptyLabel("empty_1_0", column=1, row=0)
        app.addAutoEntry("auto_entry", words=self.word_list, column=0, row=2)
        app.setAutoEntryNumRows("auto_entry", 3)

        app.stopTab()

        # TODO -------------------------------- STOP TAB -------------------------------------

        # TODO -------------------------------- NEW TAB --------------------------------------

        # TABLE OF CONTENTS - CURRENT TAB
        """
        Current tab is for "Part 2" in the assignment. Where the User plays against the program.
        The Program is trying to figure out which word the User is thinking of. The Programs 
        guesses are based on a random word from the self.word_list class attribute.
        
        TODO markings indicates critical gui and functional code parts
        
        1. TAB LOCAL SETTINGS - Configures the settings of current tab
        2. TAB LOCAL VARIABLES - Local tab variables
        3. TAB LOCAL FUNCTIONS - 
        4. TAB LOCAL GROUPS
        5. TAB LOCAL STOP
        """

        # 1. TAB LOCAL SETTINGS
        # 1.1 INIT TAB & TAB NAME
        app.startTab("Användaren vs. Skynet")

        # 2. TAB LOCAL VARIABLES
        # 2.1 GUESS COUNTER
        app.guess_counter = 1  # used in the 'press'-function

        # 3. TAB LOCAL FUNCTIONS
        # 3.1 PRESS FUNCTION
        def press(value):
            if value == "Submit":
                send_data_to_backend(data=f"{app.getEntry('clue')}")
                # if app.getEntry('clue').isdigit() and 0 <= int(app.getEntry('clue')) <= 5:
                #     # USES Y GROUP 2
                #     app.setLabel(f"2_L1", f"Antal gissningar: {app.guess_counter}")
                #     app.guess_counter += 1
                #
                #     parse_return = ogf.parse_compare_words_and_hints(words_list=self.word_list,
                #                                                      skynet_guess=self.random_word,
                #                                                      clue=f"{app.getEntry('clue')}")
                #     self.random_word = parse_return[0]
                #     self.word_list = parse_return[1]
                #
                #     # if the wordlist contains one item or above, we take the random word and print it
                #     if len(self.word_list) > 0:
                #         # USES Y GROUP 1
                #         app.setTextArea("1_TA1", end=True, text=f"\n{app.guess_counter} - {self.random_word}")
                #
                #     # otherwise we tell the User that the Program has run out of guesses (in its word list)
                #     else:
                #         app.okBox(title="", message="Programmet har slut på ord i sin lista.")
                #         clean_up()
                #
                # # if the User tell the Program that the word guess was right, we will notify the user and clean up
                # elif app.getEntry('clue').lower() == "rätt":
                #     app.okBox(title="", message=f"Programmet gissade rätt ord. Ordet var {self.random_word}")
                #     clean_up()  # the clean_up function restores balance to the universe.
                #     app.guess_counter = 1  # TAB LOCAL VARIABLE resets to default value
                #
                # # if the User provides incorrect input
                # else:
                #     app.warningBox(title="!", message='Skriv antal rätt bokstäver med en siffra,'
                #                                       ' eller "rätt" om ordet är rätt.')
            elif value == "Cancel":
                exit()
            elif value == "Restart":
                clean_up()  # the clean_up function restores balance to the universe.
                app.guess_counter = 1  # TAB LOCAL VARIABLE resets to default value

        def send_data_to_backend(data):
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
                clean_up()  # the clean_up function restores balance to the universe.
                app.guess_counter = 1  # TAB LOCAL VARIABLE resets to default value

            else:
                err_msg = 'Skriv antal rätt bokstäver med en siffra, eller "rätt" om ordet är rätt.'
                ok_box(title="Ogiltig indata", msg=err_msg)
                app.clearAllEntries()

        # 4 TAB LOCAL GROUPS
        # 4.0 Y GROUP 0 // EMPTY SPACE
        # 4.0 - GUI WIDGETS
        app.addEmptyLabel("0_EL1", column=y_group0, row=x_group1)
        app.addEmptyLabel("0_EL2", column=y_group0, row=x_group2)
        app.addEmptyLabel("0_EL3", column=y_group0, row=x_group3)
        app.addEmptyLabel("0_EL4", column=y_group0, row=x_group4)

        # 4.1 Y GROUP 1 // WORD GUESS OUTPUT AND USER INPUT
        # 4.1 - VARIABLES
        # auto_entry_word_suggestions = ["0", "1", "2", "3", "4", "5", "rätt"]
        button_names = ["Submit", "Cancel", "Restart"]
        info_text = "Skriv antal rätt bokstäver, eller om ordet är rätt."

        # 4.1 - GUI WIDGETS
        app.addLabel(title="1_L0", column=y_group1, row=x_group0, text=info_text)
        app.addLabel("1_L1", text="Programmets Gissnings Historik:", column=y_group1, row=x_group1)
        app.addScrolledTextArea("1_TA1", column=y_group1, row=x_group2)
        app.addEntry(title="clue", column=y_group1, row=x_group3)
        app.addButtons(names=button_names, funcs=press, column=y_group1, row=x_group4)

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

        # 5 TAB LOCAL STOP
        app.stopTab()

        # TODO -------------------------------- STOP TAB -------------------------------------

        # \\\\\ STOP TABBED FRAMES /////
        app.stopTabbedFrame()

        # METHOD FUNCTIONS:
        def clean_up():
            self.word_list = ofh.file_reader("words.txt", encoding="ISO-8859-1")  # restore to its default
            self.random_word = ogf.random_list_element(word_list=self.word_list)  # random from default word_list
            app.clearAllTextAreas()
            app.clearAllEntries()

        def ok_box(title, msg):
            app.okBox(title=f"{title}", message=f"{msg}")

        # RUNS GUI APPLICATION
        app.go()


if __name__ == "__main__":
    # file_content = ofh.file_reader(read_file="words.txt", encoding='ISO-8859-1')  # returns list
    # generated_word = ogf.random_list_element(word_list=file_content)


    def lets_try_this_shhh():
        print("activated")
        x = OrdspelGUI()
        x.go_gui()

    try:
        print("activated")
        x = OrdspelGUI()
        x.go_gui()
    except ValueError:
        gui.okBox(title="ValueError", message="", parent=x.go_gui())