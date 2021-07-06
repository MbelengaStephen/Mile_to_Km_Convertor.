from tkinter import *


def miles_to_km():
    miles = float(miles_entry.get())
    km = round(miles * 1.609)
    km_result_label.config(text=f"{km}")


window = Tk()
window.title("Miles To Km Converter.")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

miles_label = Label(text="Miles", font="italic")
miles_label.grid(row=4, column=5)

km_label = Label(text="Km", font="italic")
km_label.grid(row=6, column=5)

km_result_label = Label(text="0")
km_result_label.grid(row=6, column=4)

is_equal_label = Label(text="is equal to", font="bold")
is_equal_label.grid(row=6, column=0)

miles_entry = Entry(width=10)
miles_entry.grid(row=4, column=4)

button = Button(text="Calculate.", command=miles_to_km)
button.grid(row=8, column=4)


window.mainloop()