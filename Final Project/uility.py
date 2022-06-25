# Constants
all_words = dict()

# Classes
class Word:
    def __init__(self, spelling: str, meaning:str):
        self.spelling = spelling
        self.meaning = meaning
        all_words[spelling] = self

    def __str__(self):
        return f"The word is {self.spelling}, meaing: {self.meaning}"

    def __repr__(self):
        return f"The word is {self.spelling}, meaing: {self.meaning}"



class Quiz:
    ...



# Functions
def get_number_of_questions():
    while True:
        try:
            number = int(input("How many words would you like to be test on?" ))
            return number
        except ValueError:
            continue





