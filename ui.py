from tkinter import *
from data import question, question_data, answer_data
import html

THEME_COLOR = "#375362"

class QuizInterface:


    def end_game(self):
        self.question_label.config(bg="white",text=f"Final score is: \n{self.score}/10")

    def get_next_question(self):
        if self.index == 10:
            self.end_game()
        else:
            self.question_label.config(bg="white",text=f"Q.{self.index}: {html.unescape(question_data[self.index])}")
    def update_ui(self,answer):
        if self.index == 10:
            self.end_game()

        if answer == answer_data[self.index]:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.question_label.config(bg="green")
            print("correct setting bg to green")

        else:

            print(question_data[self.index])
            print(answer_data[self.index])
            self.question_label.config(bg="red")
            print("wrong setting bg to red")

        self.question_label.after(1000,self.get_next_question)
        self.index += 1

    def __init__(self):
        def false_button_pressed():

            self.update_ui("False")

        def true_button_pressed():

            self.update_ui("True")

        self.index = 1
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,pady=20,padx=20)

        self.score = 0
        self.score_label = Label(text= f"Score: {self.score}",fg="white",bg=THEME_COLOR,font=("Arial",12))
        self.score_label.grid(column=1,row=0)

        #q_text = html.unescape(question)
        q_text=f"Q.{self.index}: {html.unescape(question_data[self.index])}"
        self.question_label = Label(text=q_text, bg="white",fg=THEME_COLOR,font=("Arial",20,"italic"),wraplength=300)
        self.question_label.grid(column=0,row=1,columnspan=2)
        self.question_label.config(width=26,height=12,pady=20,padx=20)

        self.true_button_image = PhotoImage(file="images/true.png")
        self.false_button_image = PhotoImage(file="images/false.png")

        self.true_button = Button(image=self.true_button_image,command=true_button_pressed)
        self.true_button.grid(column=0,row=2)
        self.true_button.config(width=100, height=97,padx=20,pady=20)

        self.false_button = Button(image=self.false_button_image,command=false_button_pressed)
        self.false_button.grid(column=1,row=2)
        self.false_button.config(width=100,height=97)

        self.window.mainloop()


