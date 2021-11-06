from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#F7DBF0"
PURPLE = "#BEAEE2"
MINT = "#CDF0EA"
WHITE = "#F9F9F9"
YELLOW = "#FFF5DA"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        timer_title.config(timer_title, text="♡YAYYY long break♡", fg=PINK)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_title.config(text="time for a short break~♡♡♡", fg=PINK)
    else:
        timer_title.config(text="time to work Q-Q", fg=YELLOW, bg=MINT)
        count_down(work_sec)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("s t u d y ~ !")
window.config(padx=25, pady=10, bg=PINK)

canvas = Canvas(width=259, height=263, highlightthickness=0)
froggy = PhotoImage(file="C:/Users/Rebekah Alecci/Downloads/babyfroggy2.png")
canvas.create_image(129, 132, image=froggy)
timer_text = canvas.create_text(138, 150, text="00:00", fill=PURPLE, font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        global reps
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✓"
            checkmarks.config(text=marks)


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_title.config(text="Timer", fg=PURPLE, bg=WHITE)
    global reps
    reps = 0
    global marks
    marks = ""



start = Button(text="Start", bg=WHITE, fg=PURPLE, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", bg=WHITE, fg=PURPLE, command=reset_timer)
reset.grid(column=2, row=2)

timer_title = Label(text="Timer", fg=PURPLE, font=(FONT_NAME, 30, "bold"))
timer_title.grid(column=1, row=0)

checkmarks = Label(text="", bg=WHITE, fg=PURPLE)
checkmarks.config(padx=10, pady=5)
checkmarks.grid(column=1, row=3)


window.mainloop()