#
# Programmer: Chris Blanks
# Purpose: This code is meant to extract point data
# from generated CSV files and plot the points.
#


import numpy as np
import matplotlib.pyplot as plt

file_name = str(input('Hello. Please, enter the CSV file name. \n>'))
amp_range = int(input('Please, enter the lowest order of magnitude of the current readings(ex: if it is mA then put -3)\n>'))

amp_orig = amp_range  #Used for units on graph label

if amp_range < 0:
    amp_range = abs(amp_range)
else:
    amp_range = -1*amp_range


f = open(file_name ,'r')
line_store = f.readlines()
f.close()

container = []
x = [] #voltage
y = [] #current
z = 0
count = 0

for line in line_store:
    if count >= 8: #The line when the voltage and current can be extracted
        container = line.split(",")
        
        z = float(container[1])*10**(amp_range) #brings amp values to manageable range
        w = float(container[14])
        w = round(w,1) #shortens the decimals for the voltage
        
        x.append(w)
        y.append(z)
    count+=1

new_array_x = x[::45] #Picks every 45th data point
new_array_y = y[::45]

plt.plot(new_array_x,new_array_y,'--') #plots index by index

plt.xlabel('Voltage (V)', fontsize =18)
plt.ylabel('Current ($10^{}$ A)'.format(amp_orig), fontsize =16)
plt.axis([-11,11,-20,20])
plt.title('Current Vs Voltage')
plt.show()





