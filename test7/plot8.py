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



#def update(frame):
    #ax.view_init(elev=100, azim=frame)  
    #return scatter

#ani = FuncAnimation(fig, update, frames=range(0, 360, 5), blit=True)

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Data Animation')

plt.show()


#plt.plot(x_data, y_data)
#plt.xlabel('X-axis')
#plt.ylabel('Y-axis')
#plt.title('CSV Data Plot')
#plt.show()