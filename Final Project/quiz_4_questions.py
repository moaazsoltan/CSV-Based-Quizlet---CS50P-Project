from tkinter import *

Questions = ["What technology is used to record cryptocurrency transactions?",
             "What tool would you use to reduce the digital image size?",
             "Which computer language is the most widely used?",
             "Is Moaaz Awesome?"]
Options = [["Digital wallet", "Mining", "Blockchain", "tomato"],
           ["Filter", "Crop", "Rotate", "potato"],
           ["C++", "Python", "Javascript", "vegetable"],
           ["Yes", "fuck yes", "No", "not cool fam"]]

Answers = [3, 2, 3, 2]

Score = 0
Total_No_Questions = 4
Question_no = 1


def next():
    global Score, Question_no
    if val1.get() == 1:
        selected_option = 1
    elif val2.get() == 1:
        selected_option = 2
    elif val3.get() == 1:
        selected_option = 3
    elif val4.get() == 1:
        selected_option = 4
    else:
        selected_option = -1

    if Answers[Question_no-1] == selected_option :
        Score += 1

    Question_no += 1

    if Question_no > Total_No_Questions:
        root.pack_forget()
        score.place(relx=.40, rely=.40)
        score.config(text="Score:"+str(Score), font=("Arial", 15))

    else:
        val1.set(0)
        val2.set(0)
        val3.set(0)
        val4.set(0)
        question.config(text=Questions[Question_no-1])
        option1.config(text=Options[Question_no-1][0])
        option2.config(text=Options[Question_no-1][1])
        option3.config(text=Options[Question_no-1][2])
        option4.config(text=Options[Question_no-1][3])


def check(option):
    if option == 1:
        val2.set(0)
        val3.set(0)
        val4.set(0)
    elif option == 2:
        val1.set(0)
        val3.set(0)
        val4.set(0)
    elif option == 3:
        val1.set(0)
        val2.set(0)
        val4.set(0)
    elif option == 4:
        val1.set(0)
        val2.set(0)
        val3.set(0)
        


Win = Tk()
Win.title("Quiz Game")

root = Frame()
root.pack()

question = Label(root, width=60, font=("Arial", 15), text=Questions[0])
question.pack()

val1 = IntVar()
val2 = IntVar()
val3 = IntVar()
val4 = IntVar()

option1 = Checkbutton(root, variable=val1, text=Options[0][0], command=lambda: check(1))
option1.pack()

option2 = Checkbutton(root, variable=val2, text=Options[0][1], command=lambda: check(2))
option2.pack()

option3 = Checkbutton(root, variable=val3, text=Options[0][2], command=lambda: check(3))
option3.pack()

option4 = Checkbutton(root, variable=val4, text=Options[0][3], command=lambda: check(4))
option4.pack()

next_b = Button(root, text="next", command=next)
next_b.pack()

score = Label(Win)
score.place_forget()

Win.mainloop()