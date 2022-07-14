from tkinter import *

class Window(Tk):

    def __init__(self):
        super().__init__()
        self.title = 'Hello World'
        self.geometry('300x300')
        FancyButton(text='Press Me').pack()
        FancyButton(text='Press Me').pack()
        FancyButton(text='Press Me').pack()
        self.mainloop()

class FancyButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self['background'] = 'red'

Window()
 
# If you try running this
# I've made a custom button class (all it does is colour the button red)
# this is great if you want to re-use a button style all over your UI
# instead of modifying the settings of every new button you make
# you can contain it all in a class


# from tkinter import *
# class Window(Tk):

#     def __init__(self):
#         super().__init__()
#         self.title = 'Hello World'
#         self.geometry('300x300')
#         Button(text='Press Me').pack()

#     def show(self):
#         self.mainloop()

# win = Window()
# win.show()