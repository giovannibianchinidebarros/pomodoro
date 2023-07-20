'''Pomodoro APP

The Pomodoro Technique is a time management method based on 25-minute stretches 
of focused work broken by five-minute breaks. 
Longer breaks, typically 15 to 30 minutes, are taken after four consecutive 
work intervals. Each work interval is called a pomodoro, the Italian word for tomato.
'''

#  IMPORTS  #
import tkinter
import math

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
WORK_MIN = 0.2
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 1

CHECK_MARK = "✔"
loop_number = 0

#  TIMER RESET  #

#  TIMER MECHANISM  #


def start_timer():
    '''Start the count down, when the start button is clicked.'''

    global loop_number

    work_sec = int(WORK_MIN * 60)
    short_break_sec = int(SHORT_BREAK_MIN * 60)
    long_break_sec = int(LONG_BREAK_MIN * 60)

    loop_number += 1
    worked_times = math.ceil(loop_number / 2)

    if loop_number in [1, 3, 5, 7]:
        title_label.configure(text="Work")
        checkmark_label.configure(text=CHECK_MARK*worked_times)
        count_down(work_sec)

    elif loop_number in [2, 4, 6]:
        title_label.configure(text="Break")
        count_down(short_break_sec)

    elif loop_number >= 8:
        title_label.configure(text="Break")
        count_down(long_break_sec)
        loop_number = 0


#  COUNTDOWN MECHANISM  #
def count_down(count):
    '''
    Change the displayed time every 1 second.

    Args:
        count (int): starting number, in seconds.
    Returns:
        None.
    '''

    count_min = f"{count // 60}".zfill(2)
    count_sec = f"{count % 60}".zfill(2)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        window.after(1000, count_down, count-1)
    else:
        start_timer()


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
timer_text = canvas.create_text(
    100, 132, text="00:00", font=(FONT_NAME, FONT_SIZE, "bold"))

start_button = tkinter.Button(
    text="Start", highlightthickness=0, font=(BT_FONT_NAME, BT_FONT_SIZE, "bold"),
    command=start_timer)
reset_button = tkinter.Button(
    text="Reset", highlightthickness=0, font=(BT_FONT_NAME, BT_FONT_SIZE, "bold"))

checkmark_label = tkinter.Label(
    text="", bg=YELLOW, fg=GREEN, font=(CHK_FONT_NAME, CHK_FONT_SIZE, "bold"))


title_label.grid(row=0, column=1)
canvas.grid(row=1, column=1)
start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)
checkmark_label.grid(row=3, column=1)


window.mainloop()
