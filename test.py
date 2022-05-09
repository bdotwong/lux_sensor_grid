import tkinter as tk
import random

def assign_sensor(x):
    print(x)

win = tk.Tk()

win.geometry('825x600')
win.configure(background='#CD5C5C')

def readSensors(i):
    output = output_+str(i)
    output.set(random.choice([0, 1, 2, 3, 4, 5]))
    win.after(1000, readSensors)
    output = tk.StringVar()

    measuredValues=[0, 1, 2, 3, 4, 5]
    value = value+str(i)
    value=str(measuredValues[0])
    output.set(value)

#first column
output_1_label = tk.Label(win, textvariable=output_1, height=2, width=12)
output_1_label.place(x=50, y=100)

output_2_label = tk.Label(win, textvariable=output_2, height=2, width=12)
output_2_label.place(x=50, y=200)

output_3_label = tk.Label(win, textvariable=output_3, height=2, width=12)
output_3_label.place(x=50, y=300)

output_4_label = tk.Label(win, textvariable=output_4, height=2, width=12)
output_4_label.place(x=50, y=400)

output_5_label = tk.Label(win, textvariable=output_4, height=2, width=12)
output_5_label.place(x=50, y=500)
for i in range(0,5):
    assign_sensor(i)
