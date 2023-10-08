from tkinter import *


def miles_conversion():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to kilometer converter.")
window.config(padx=25, pady=25)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="0")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="miles")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="km")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="calculate", command=miles_conversion)
calculate_button.grid(column=1, row=2)

window.mainloop()
