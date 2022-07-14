from tkinter import *

# variables
Questions_test = ["What technology is used to record cryptocurrency transactions?",
             "What tool would you use to reduce the digital image size?",
             "Which computer language is the most widely used?",
             "Is Moaaz Awesome?"]
Options_test = [["Digital wallet", "Mining", "Blockchain", "tomato"],
           ["Filter", "Crop", "Rotate", "potato"],
           ["C++", "Python", "Javascript", "vegetable"],
           ["Yes", "fuck yes", "No", "not cool fam"]]

Answers_test = [3, 2, 3, 2]


class tkinterQuiz():
    def __init__(self, Questions, Options, Answers):
        # Boiler plate initialisation
        self.Win = Tk()
        self.Win.title("Quiz Game")

        self.root = Frame()
        self.root.pack()

        self.question = Label(self.root, width=60, font=("Arial", 15), text=Questions[0])
        self.question.pack()

        # constants
        self.Score = 0
        self.Total_No_Questions = 4
        self.Question_no = 1

        # Quiz Constants
        self.Questions = Questions
        self.Options = Options
        self.Answers = Answers

        # Options
        self.val1 = IntVar()
        self.val2 = IntVar()
        self.val3 = IntVar()
        self.val4 = IntVar()

        self.option1 = Checkbutton(self.root, variable=self.val1, text=self.Options[0][0], command=lambda: self.check(1))
        self.option1.pack()

        self.option2 = Checkbutton(self.root, variable=self.val2, text=self.Options[0][1], command=lambda: self.check(2))
        self.option2.pack()

        self.option3 = Checkbutton(self.root, variable=self.val3, text=self.Options[0][2], command=lambda: self.check(3))
        self.option3.pack()

        self.option4 = Checkbutton(self.root, variable=self.val4, text=self.Options[0][3], command=lambda: self.check(4))
        self.option4.pack()

        self.next_b = Button(self.root, text="next", command=self.next)
        self.next_b.pack()

        self.score = Label(self.Win)
        self.score.place_forget()

        self.Win.mainloop()

    def check(self, option):
        if option == 1:
            self.val2.set(0)
            self.val3.set(0)
            self.val4.set(0)
        elif option == 2:
            self.val1.set(0)
            self.val3.set(0)
            self.val4.set(0)
        elif option == 3:
            self.val1.set(0)
            self.val2.set(0)
            self.val4.set(0)
        elif option == 4:
            self.val1.set(0)
            self.val2.set(0)
            self.val3.set(0)
        



    def next(self):
        if self.val1.get() == 1:
            selected_option = 1
        elif self.val2.get() == 1:
            selected_option = 2
        elif self.val3.get() == 1:
            selected_option = 3
        elif self.val4.get() == 1:
            selected_option = 4
        else:
            selected_option = -1

        if self.Answers[self.Question_no-1] == selected_option :
            self.Score += 1

        self.Question_no += 1

        if self.Question_no > self.Total_No_Questions:
            self.root.pack_forget()
            self.score.place(relx=.40, rely=.40)
            self.score.config(text="Score:"+str(self.Score), font=("Arial", 15))

        else:
            self.val1.set(0)
            self.val2.set(0)
            self.val3.set(0)
            self.val4.set(0)
            self.question.config(text=self.Questions[self.Question_no-1])
            self.option1.config(text=self.Options[self.Question_no-1][0])
            self.option2.config(text=self.Options[self.Question_no-1][1])
            self.option3.config(text=self.Options[self.Question_no-1][2])
            self.option4.config(text=self.Options[self.Question_no-1][3])
    


tkinterQuiz(Questions_test, Options_test, Answers_test)