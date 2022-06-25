# Constants
all_words = dict()

# Classes
class Word:
    def __init__(self, spelling: str, meaning:str):
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
    all_words_list = all_words.items()
    modes = ["Lowest Mastery", None]

    # Checking if correct modes
    def begin(self, notq, mode=None):
        if not verify_int(notq) or mode not in modes:
            print("Wrong usage")
            return
    
        for _ in range(notq):
            question_words = []
            [question_words.append(random.choice(all_words_list)) for _ in range(4)]
            question = question_words[1]
            correct_answer = None
            list_of_wrong_answers = None


        

    



# Functions
def get_number_of_questions():
    while True:
        try:
            number = int(input("How many words would you like to be test on?" ))
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




