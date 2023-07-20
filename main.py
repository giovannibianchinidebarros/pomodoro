'''Pomodoro APP

The Pomodoro Technique is a time management method based on 25-minute stretches 
of focused work broken by five-minute breaks. 
Longer breaks, typically 15 to 30 minutes, are taken after four consecutive 
work intervals. Each work interval is called a pomodoro, the Italian word for tomato.
'''

#  IMPORTS  #
import tkinter

#  CONSTANTS  #
# colors
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
# fonts
FONT_NAME = "Courier"
FONT_SIZE = 32
BT_FONT_NAME = "Courier"
BT_FONT_SIZE = 18
CHK_FONT_NAME = "Courier"
CHK_FONT_SIZE = 24
# timer
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

CHECK_MARK = "✔"
check_mark_txt = ""

#  TIMER RESET  #

#  TIMER MECHANISM  #

#  COUNTDOWN MECHANISM  #

#  UI SETUP  #
window = tkinter.Tk()
window.title("Pomodoro")
window.minsize(width=420, height=400)
window.config(padx=20, pady=10, bg=YELLOW)

title_label = tkinter.Label(text="Timer", bg=YELLOW,
                            fg=GREEN, font=(FONT_NAME, FONT_SIZE, "bold"))

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 132, text="00:00", font=(FONT_NAME, FONT_SIZE, "bold"))

start_button = tkinter.Button(
    text="Start", font=(BT_FONT_NAME, BT_FONT_SIZE, "bold"))
reset_button = tkinter.Button(
    text="Reset", font=(BT_FONT_NAME, BT_FONT_SIZE, "bold"))

checkmark_label = tkinter.Label(
    text=f"{check_mark_txt}", bg=YELLOW, fg=GREEN, font=(CHK_FONT_NAME, CHK_FONT_SIZE, "bold"))


title_label.grid(row=0, column=1)
canvas.grid(row=1, column=1)
start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)
checkmark_label.grid(row=3, column=1)

window.mainloop()
