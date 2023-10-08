from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = None


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="timer")
    check_mark.config(text="")
    global rep
    rep = 0


def start_timer():
    global rep
    rep += 1

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if rep % 8 == 0:
        count_down(long_break_seconds)
        title_label.config(text="break", fg=RED)
    elif rep % 2 == 0:
        count_down(short_break_seconds)
        title_label.config(text="break", fg=PINK)
    else:
        count_down(work_seconds)
        title_label.config(text="work", fg=GREEN)


def count_down(count):
    count_minutes = math.floor(count / 60)
    count_second = count % 60
    if count_second < 10:
        count_second = f"0{count_second}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(rep/2)
        for x in range(work_session):
            mark += "✔"
        check_mark.config(text=mark)


window = Tk()
window.title("Pomodoro timer")
window.config(padx=125, pady=50, bg=YELLOW)

title_label = Label(text="timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
title_label.grid(column=1, row=0)

canvas = Canvas(width=202, height=226, bg=YELLOW, highlightthickness=0)
tomato_picture = PhotoImage(file="tomato.png")
canvas.create_image(101, 113, image=tomato_picture)
timer_text = canvas.create_text(101, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
check_mark.grid(column=1, row=2)

window.mainloop()
