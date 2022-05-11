import tkinter as tk
import time
import board
import adafruit_bh1750
import adafruit_tca9548a
import random

# Create I2C bus as normal
i2c = board.I2C()  # uses board.SCL and board.SDA

# Create the TCA9548A object and give it the I2C bus
tca = adafruit_tca9548a.TCA9548A(i2c)
tca 
# For each sensor, create it using the TCA9548A channel instead of the I2C object
lux1 = adafruit_bh1750.BH1750(tca[0])
lux2 = adafruit_bh1750.BH1750(tca[1])
lux3 = adafruit_bh1750.BH1750(tca[2])
lux4 = adafruit_bh1750.BH1750(tca[3])
lux5 = adafruit_bh1750.BH1750(tca[4])

def readSensors():
    output_1.set(round(lux1.lux, 2))
    output_2.set(round(lux2.lux, 2))
    output_3.set(round(lux3.lux, 2))
    output_4.set(round(lux4.lux, 2))
    output_5.set(round(lux5.lux, 2))
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


#measuredValues = [0, 1, 2, 3, 4, 5]
value0 = str(lux1.lux)
value1 = str(lux2.lux)
value2 = str(lux3.lux)
value3 = str(lux4.lux)
value4 = str(lux5.lux)


output_1.set(value0)
output_2.set(value1)
output_3.set(value2)
output_4.set(value3)
output_5.set(value4)

print(output_1)

#first column
output_1_label = tk.Label(win, textvariable=output_1, height=2, width=12)
output_1_label.place(x=50, y=100)

output_2_label = tk.Label(win, textvariable=output_2, height=2, width=12)
output_2_label.place(x=50, y=200)

output_3_label = tk.Label(win, textvariable=output_3, height=2, width=12)
output_3_label.place(x=50, y=300)

output_4_label = tk.Label(win, textvariable=output_4, height=2, width=12)
output_4_label.place(x=50, y=400)

output_5_label = tk.Label(win, textvariable=output_5, height=2, width=12)
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
