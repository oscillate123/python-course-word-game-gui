from appJar import gui as gui
import random
import ordspelet_file_handler as ofh
import ordspelet_game_funtions as ogf

# source: http://appjar.info/*


class ordspel_gui:


    def __init__(self, random_word):
        self.random_word = random_word
        self.app = gui()

    def go_gui(self):

        # CLASS / METHOD / FUNCTION - AREA
        random_word = self.random_word
        app = self.app

        # BODY SETTINGS
        app.setSize(300, 400)
        app.setLocation(0, 200)

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
        app.addAutoEntry("auto_entry", words=file_content, column=0, row=2)
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
            if value == "SUBMIT":
                app.guess_counter += 1
                # USES Y GROUP 3
                app.setLabel(f"2_L1", f"Guesses: {app.guess_counter}")
                app.setTextArea("1_L1", end=True, text=f"\n{app.guess_counter} - {random_word}")

        # Y GROUP 0
        app.addEmptyLabel("0_EL0", column=y_group0, row=x_group0)
        app.addEmptyLabel("0_EL1", column=y_group0, row=x_group1)
        app.addEmptyLabel("0_EL2", column=y_group0, row=x_group2)
        app.addEmptyLabel("0_EL3", column=y_group0, row=x_group3)

        # Y GROUP 1 // WORD GUESS HERE AND USER INPUT HERE
        app.addLabel("1_L0", text="Program Guess History:", column=y_group1, row=x_group0)

        app.addScrolledTextArea("1_L1", column=y_group1, row=x_group1)
        app.setTextArea("1_L1", text=f"{app.guess_counter} - {self.random_word}")

        app.addNumericEntry("clue", column=y_group1, row=x_group2)
        app.addButton("SUBMIT", press, column=y_group1, row=x_group3)

        # Y GROUP 2
        app.addLabel("2_L1", text="Guesses:", column=y_group2, row=x_group0)
        app.addEmptyLabel("2_EL1", column=y_group2, row=x_group1)
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

    file_content = ofh.file_reader(read_file="words.txt", encoding='ISO-8859-1')  # returns list
    generated_word = ogf.random_list_element(word_list=file_content)


    def lets_try_this_shhh():
        print("mehe")
        x = ordspel_gui(generated_word)
        x.go_gui()


    lets_try_this_shhh()