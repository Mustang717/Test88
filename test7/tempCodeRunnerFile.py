import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import time

file = 'Data.csv'  
x_data = []
y_data = []
z_data = []

with open(file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  
    for row in csv_reader:
        x_data.append(float(row[1]))  
        y_data.append(float(row[2]))
        z_data.append(float(row[3]))   

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_data, y_data, z_data)
