from __future__ import unicode_literals, annotations
import random
from string import ascii_uppercase
from threading import local
from tkinter import *

# Return a lsit of question Classes, easier to implement using tinker. 
# Go through the list to make tinker questions

# Constants
all_words = dict()  # A dictionary of Word: Word instance 
all_words_list = list(all_words)   # A list of all the words
tested_words = []   # Keep track of words user was tested on, shouldn't include words used for answers

# Classes
class Word:
    def __init__(self, spelling: str, meaning: str):
        self.spelling = spelling
        self.meaning = meaning
        if type(self) is Word:
            all_words[spelling] = self

    @property
    def spelling(self):
        return self._spelling

    @spelling.setter
    def spelling(self, value):
        self._spelling = value

    def __str__(self):
        return f"The word is {self.spelling}, meaing: {self.meaning}"

    def __repr__(self):
        return f"The word is {self.spelling}, meaing: {self.meaning}"

# Do I really need to inherit from word? Don't think so
class Question:
    def __init__(self):

        # initialising question attributes
        all_words_list = list(all_words)
        self.question_word = None
        self.question_words = []
        self.options = []
        self.correct_answer = None
        self.correct_asnwer_index = None

        # 4 total words, 1 question, 3 false answers
        while len(self.question_words) < 4:
            random_word = random.choice(all_words_list)
            if random_word not in self.question_words and random_word not in tested_words:
                self.question_words.append(random_word)
        # word tested on set and included
        self.question_word = self.question_words[0]
        tested_words.append(self.question_word)

        # setting the correct answer for the question
        self.correct_answer = all_words[self.question_word].meaning

        # Make a list of the answer options
        self.options = list(map(lambda word: all_words[word].meaning, self.question_words))

        # Shuffle the list of answers
        random.shuffle(self.options)

        # Setting correct answer index for tkinter later
        for index, answer in enumerate(self.options, 1):
            if answer == self.correct_answer:
                self.correct_asnwer_index = index
                break
        

class tkinterQuiz():
    def __init__(self, Questions:list, Options:list, Answers:list, notq): # List of strings, list of list of answers, list of ints of correct answer(index)
        # Boiler plate initialisation
        self.Win = Tk()
        self.Win.title("Quiz Game")

        self.root = Frame()
        self.root.pack()

        self.question = Label(self.root, width=60, font=("Arial", 15), text=Questions[0])
        self.question.pack()

        # constants
        self.Score = 0
        self.Total_No_Questions = notq
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
    

class Quiz:
    def __init__(self):
        self.modes = ["Lowest Mastery", None]
        self.notq = None
        self.list_of_questions = []
        self.questions = []
        self.options = []
        self.answers = []
        self.score = 0
        self.question_no = 1

    # Checking if correct modes
    def begin(self, notq, mode=None):
        if not verify_int(notq) or mode not in self.modes:
            print("Wrong usage")
            return

        # Generate Questions
        for _ in range(notq):
            self.notq = notq
            question = Question()
            self.list_of_questions.append(question)
            # print(*question.ask())
        
        # update class attributes 
        for question in self.list_of_questions:
            self.questions.append(question.question_word)
            self.options.append(question.options)
            self.answers.append(question.correct_asnwer_index)
        
        tkinterQuiz(self.questions, self.options, self.answers, self.notq)
    



##################
####FUNCTIONS#####
##################

def get_number_of_questions():
    while True:
        try:
            number = int(input("How many words would you like to be test on? "))
            return number
        except ValueError:
            continue


def verify_int(number):
    try:
        number = int(number)
        return True
    except ValueError:
        print("Invalid number of questions")
        raise ValueError


def get_asnwer(question):
    while True:
        user_answer = input(f"What is the meaning of {question}")
        if user_answer in ['A', 'B', 'C', 'D']:
            return user_answer