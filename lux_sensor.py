import tkinter as tk
import random


def readSensors():
    output_1.set(random.choice([0, 1, 2, 3, 4, 5]))
    output_2.set(random.choice([0, 1, 2, 3, 4, 5]))
    output_3.set(random.choice([0, 1, 2, 3, 4, 5]))
    output_4.set(random.choice([0, 1, 2, 3, 4, 5]))
    win.after(1000, readSensors)


win = tk.Tk()
win.title('Lux Sensor Grid Readings')
win.geometry('825x600')
#win.configure(background='#CD5C5C')
win.configure(background='#4A7A8C')

output_1 = tk.StringVar()
output_2 = tk.StringVar()
output_3 = tk.StringVar()
output_4 = tk.StringVar()
output_4 = tk.StringVar()
output_5 = tk.StringVar()


measuredValues = [0, 1, 2, 3, 4, 5]
value0 = str(measuredValues[0])
value1 = str(measuredValues[1])
value2 = str(measuredValues[2])
value3 = str(measuredValues[3])
value4 = str(measuredValues[4])


output_1.set(value0)
output_2.set(value1)
output_3.set(value2)
output_4.set(value3)
output_5.set(value4)

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


#second column
output_1_label = tk.Label(win, textvariable=output_1, height=2, width=12)
output_1_label.place(x=200, y=100)

output_2_label = tk.Label(win, textvariable=output_2, height=2, width=12)
output_2_label.place(x=200, y=200)

output_3_label = tk.Label(win, textvariable=output_3, height=2, width=12)
output_3_label.place(x=200, y=300)

output_4_label = tk.Label(win, textvariable=output_4, height=2, width=12)
output_4_label.place(x=200, y=400)

output_5_label = tk.Label(win, textvariable=output_4, height=2, width=12)
output_5_label.place(x=200, y=500)

#third column
output_1_label = tk.Label(win, textvariable=output_1, height=2, width=12)
output_1_label.place(x=350, y=100)

output_2_label = tk.Label(win, textvariable=output_2, height=2, width=12)
output_2_label.place(x=350, y=200)

output_3_label = tk.Label(win, textvariable=output_3, height=2, width=12)
output_3_label.place(x=350, y=300)

output_4_label = tk.Label(win, textvariable=output_4, height=2, width=12)
output_4_label.place(x=350, y=400)

output_5_label = tk.Label(win, textvariable=output_4, height=2, width=12)
output_5_label.place(x=350, y=500)

#fifth column
output_1_label = tk.Label(win, textvariable=output_1, height=2, width=12)
output_1_label.place(x=500, y=100)

output_2_label = tk.Label(win, textvariable=output_2, height=2, width=12)
output_2_label.place(x=500, y=200)

output_3_label = tk.Label(win, textvariable=output_3, height=2, width=12)
output_3_label.place(x=500, y=300)

output_4_label = tk.Label(win, textvariable=output_4, height=2, width=12)
output_4_label.place(x=500, y=400)

output_5_label = tk.Label(win, textvariable=output_4, height=2, width=12)
output_5_label.place(x=500, y=500)

#fifth column
output_1_label = tk.Label(win, textvariable=output_1, height=2, width=12)
output_1_label.place(x=650, y=100)

output_2_label = tk.Label(win, textvariable=output_2, height=2, width=12)
output_2_label.place(x=650, y=200)

output_3_label = tk.Label(win, textvariable=output_3, height=2, width=12)
output_3_label.place(x=650, y=300)

output_4_label = tk.Label(win, textvariable=output_4, height=2, width=12)
output_4_label.place(x=650, y=400)

output_5_label = tk.Label(win, textvariable=output_4, height=2, width=12)
output_5_label.place(x=650, y=500)

win.after(1000, readSensors)
win.mainloop()
