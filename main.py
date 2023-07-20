'''Pomodoro APP

The Pomodoro Technique is a time management method based on 25-minute stretches 
of focused work broken by five-minute breaks. 
Longer breaks, typically 15 to 30 minutes, are taken after four consecutive 
work intervals. Each work interval is called a pomodoro, the Italian word for tomato.
'''

#  IMPORTS  #
import tkinter

#  CONSTANTS  #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
FONT_SIZE = 32
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

#  TIMER RESET  #

#  TIMER MECHANISM  #

#  COUNTDOWN MECHANISM  #

#  UI SETUP  #
window = tkinter.Tk()
window.title("Pomodoro")
window.minsize(width=300, height=300)
window.config(padx=20, pady=20, bg=YELLOW)

canvas = tkinter.Canvas(width=204, height=226, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(102, 113, image=tomato_img)
canvas.create_text(102, 133, text="00:00", font=(FONT_NAME, FONT_SIZE, "bold"))
canvas.pack()

window.mainloop()
