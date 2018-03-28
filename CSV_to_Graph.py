#
# Programmer: Chris Blanks
# Purpose: This code is meant to extract point data
# from generated CSV files and plot the points.
#
# Last update: 3/28/2018
#


import numpy as np
import matplotlib.pyplot as plt

class Error_in_Input(Exception):
    pass

while True:
    try:
        print('Hello User.\n I recommend that you should use the graph that the sourcemeter created as a reference.\n')

        file_name = str(input('Please, enter the CSV file name. \n>'))
        file_name = file_name.strip()
        
        amp_range = int(input('Please, enter the lowest order of magnitude of the current readings. \n(ex: if it is mA then put -3)\n>'))
        key = int(input('Would you like to adjust the y-axis of your graph?\n Enter 1 for yes and 0 for no.\n'))

        if amp_range > -11 and amp_range <4: #bounds were selected due to typical range of current
            if '.csv' in file_name:
                if key == 1 or key == 0:
                    break
                else:
                    in_error = 0
                    in_error = key
                    raise Error_in_Input
            else:
                in_error = ''
                in_error = file_name
                raise Error_in_Input
        else:
            in_error = 0
            in_error = amp_range
            raise Error_in_Input
    except (Error_in_Input,ValueError):
        print('This is a wrong entry: {}.\nPlease, try again.\n'.format(in_error))

print("Successful entry!\n")

if key == 1:
    y_bound = int(input('Please, enter the range of the y-axis.\n (ex: an entry of 10 will make the axis -10 to 10)\n>'))
else:
    y_bound = 10

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

count2 = 0

for line in line_store:
    if count2 >= 8: #The line when the voltage and current can be extracted
        container = line.split(",")
        
        z = float(container[1])*10**(amp_range) #brings amp values to manageable range
        w = float(container[14])
        w = round(w,1) #shortens the decimals for the voltage
        
        x.append(w)
        y.append(z)
    count2+=1

new_array_x = x[::45] #Picks every 45th data point
new_array_y = y[::45]

plt.plot(new_array_x,new_array_y) #plots index by index

plt.xlabel('Voltage (V)', fontsize =18)
plt.ylabel('Current ($10^{}$ A)'.format(amp_orig), fontsize =16)
plt.axis([-11,11,-1*y_bound,y_bound])
plt.title('Current Vs Voltage')
plt.show()
