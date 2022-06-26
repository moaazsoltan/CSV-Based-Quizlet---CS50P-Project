import random

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
        # setting up the question
        all_words_list = list(all_words)
        self.question_words = []
        while len(self.question_words) < 4:
            random_word = random.choice(all_words_list)
            if random_word not in self.question_words and random_word not in tested_words:
                self.question_words.append(random_word)

        self.question_word = self.question_words[0]
        tested_words.append(self.question_word)

        self.correct_answer = all_words[self.question_word].meaning
        list_of_wrong_answers = list(map(lambda word: all_words[word].meaning, self.question_words))
        print(list_of_wrong_answers)
        random.shuffle(list_of_wrong_answers)
        print(list_of_wrong_answers)

    def ask(self):
        print(f"What is the meaning of the word {self.question_word}?")
        [print(f"A: {self.question_words[i]}") for i in range(4)]


class Quiz:
    def __init__(self):
        self.modes = ["Lowest Mastery", None]

    # Checking if correct modes
    def begin(self, notq, mode=None):
        if not verify_int(notq) or mode not in self.modes:
            print("Wrong usage")
            return

        for _ in range(notq):
            question_instance = Question()
            question_instance.ask()



            # Prompt user for right answer


# Functions
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