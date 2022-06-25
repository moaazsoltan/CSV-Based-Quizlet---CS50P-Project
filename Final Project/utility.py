import random

# Constants
all_words = dict()

# Classes
class Word:
    def __init__(self, spelling: str, meaning: str):
        self.spelling = spelling
        self.meaning = meaning
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


class Quiz:
    def __init__(self):
        self.all_words_list = list(all_words)
        self.modes = ["Lowest Mastery", None]

    # Checking if correct modes
    def begin(self, notq, mode=None):
        if not verify_int(notq) or mode not in self.modes:
            print("Wrong usage")
            return

        tested_words = []
        for _ in range(notq):
            question_words = []
            while len(question_words) < 4:
                random_word = random.choice(self.all_words_list)
                if random_word not in question_words and random_word not in tested_words:
                    question_words.append(random_word)
                    tested_words.append(random_word)

            question = question_words[0]
            correct_answer = all_words[question].meaning
            list_of_wrong_answers = list(map(lambda word: all_words[word].meaning, question_words))
            print(list_of_wrong_answers)
            random.shuffle(list_of_wrong_answers)
            print(list_of_wrong_answers)


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