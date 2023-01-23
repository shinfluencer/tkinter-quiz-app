import tkinter
from quiz_brain import QuizBrain

# Constants
THEME_COLOR = "#375362"


class UserInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        # Window Setup
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        icon = tkinter.PhotoImage(file="images/icon.png")
        self.window.iconphoto(False, icon)
        
        # Widgets
        self.score_label = tkinter.Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        
        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Question.", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        true_image = tkinter.PhotoImage(file="images/true.png")
        self.true_button = tkinter.Button(image=true_image, highlightthickness=0, command=self.choose_true)
        self.true_button.grid(column=0, row=2)
        
        false_image = tkinter.PhotoImage(file="images/false.png")
        self.false_button = tkinter.Button(image=false_image, highlightthickness=0, command=self.choose_false)
        self.false_button.grid(column=1, row=2)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        
    def choose_true(self):
        self.give_feedback(self.quiz.check_answer("True"))
        
    def choose_false(self):
        self.give_feedback(self.quiz.check_answer("False"))
    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        
        self.window.after(1000, self.get_next_question)
