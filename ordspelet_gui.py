from appJar import gui as gui
import random
import ordspelet_file_handler as ofh
import ordspelet_game_funtions as ogf


# source: http://appjar.info/*


class OrdspelGUI:

    def __init__(self, word_list=None):
        # word_list=None, so we can use it if we have another words.txt file!
        # Otherwise, we will work with the one we have

        self.app = gui()
        self.word_list = word_list or ofh.file_reader("words.txt", encoding="ISO-8859-1")
        self.random_word = ogf.random_list_element(word_list=self.word_list)

    def go_gui(self):

        # CLASS / METHOD / FUNCTION - AREA
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

        # ------------------------------------- NEW TAB --------------------------------------

        # TAB NAME
        app.startTab("Program vs. User")

        app.addLabel("ti_pro_usr", f"saker med grejer", column=0, row=0)
        app.addEmptyLabel("empty_1_0", column=1, row=0)
        app.addAutoEntry("auto_entry", words=self.word_list, column=0, row=2)
        app.setAutoEntryNumRows("auto_entry", 3)

        app.stopTab()

        # ------------------------------------- STOP TAB -------------------------------------

        # ------------------------------------- NEW TAB --------------------------------------

        # TAB NAME
        app.startTab("User vs. Program")

        # LABEL COUNTER
        app.label_counter = 1

        # GUESS COUNTER
        app.guess_counter = 1

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

        # TAB FUNCTIONS
        def press(value):
            if value == "Submit":
                if app.getEntry('clue').isnumeric():
                    app.guess_counter += 1
                    # USES Y GROUP 2
                    app.setLabel(f"2_L1", f"Antal gissningar: {app.guess_counter}")

                    leader_return = ogf.leader_gui(self.word_list,
                                                   robot_guess=self.random_word,
                                                   clue=f"{app.getEntry('clue')}")
                    self.random_word = leader_return[0]
                    self.word_list = leader_return[1]

                    if len(self.word_list) > 1:
                        app.setTextArea("1_TA1", end=True, text=f"\n{app.guess_counter} - {self.random_word}")
                    else:
                        app.okBox(title="", message="Programmet har slut på ord i sin lista.")

                elif app.getEntry('clue').lower() == "rätt":
                    app.okBox(title="", message=f"Programmet gissade rätt ord. Ordet var {self.random_word}")
                    app.clearAllTextAreas()
            elif value == "Cancel":
                exit()
            elif value == "Restart":
                exit()
                lets_try_this_shhh()

        # Y GROUP 0
        app.addEmptyLabel("0_EL1", column=y_group0, row=x_group1)
        app.addEmptyLabel("0_EL2", column=y_group0, row=x_group2)
        app.addEmptyLabel("0_EL3", column=y_group0, row=x_group3)
        app.addEmptyLabel("0_EL4", column=y_group0, row=x_group4)

        # Y GROUP 1 // WORD GUESS HERE AND USER INPUT HERE
        auto_entry_word_suggestions = ["0", "1", "2", "3", "4", "5", "rätt"]
        button_names = ["Submit", "Cancel", "Restart"]
        info_text = "Skriv antal rätt bokstäver, eller om ordet är rätt."

        app.addLabel(title="1_L0", column=y_group1, row=x_group0, text=info_text)
        app.addLabel("1_L1", text="Programmets Gissnings Historik:", column=y_group1, row=x_group1)
        app.addScrolledTextArea("1_TA1", column=y_group1, row=x_group2)
        app.addAutoEntry(title="clue", words=auto_entry_word_suggestions, column=y_group1, row=x_group3)
        app.addButtons(names=button_names, funcs=press, column=y_group1, row=x_group4)

        # Settings
        app.setTextArea("1_TA1", text=f"{app.guess_counter} - {self.random_word}")

        # Y GROUP 2
        app.addLabel("2_L1", text="Antal gissningar:", column=y_group2, row=x_group1)
        app.addEmptyLabel("2_EL2", column=y_group2, row=x_group2)
        app.addEmptyLabel("2_EL3", column=y_group2, row=x_group3)
        app.addEmptyLabel("2_EL4", column=y_group2, row=x_group4)

        # Y GROUP 3 TODO DELETE?
        # app.addLabel("3_EL0", text="Historik:", column=y_group3, row=x_group0)
        # app.addEmptyLabel("3_EL1", column=y_group3, row=x_group1)
        # app.addEmptyLabel("3_EL2", column=y_group3, row=x_group2)
        # app.addEmptyLabel("3_EL3", column=y_group3, row=x_group3)
        # app.addEmptyLabel("3_EL4", column=y_group3, row=x_group4)

        app.stopTab()

        # ------------------------------------- STOP TAB -------------------------------------

        # \\\\\ STOP TABBED FRAMES /////
        app.stopTabbedFrame()

        # RUNS GUI APPLICATION
        app.go()


if __name__ == "__main__":
    # file_content = ofh.file_reader(read_file="words.txt", encoding='ISO-8859-1')  # returns list
    # generated_word = ogf.random_list_element(word_list=file_content)


    def lets_try_this_shhh():
        print("activated")
        x = OrdspelGUI()
        x.go_gui()


    lets_try_this_shhh()
