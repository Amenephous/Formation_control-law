#Below is a code to implement Control law of four robots in a particular formation (SWARM ROBOTICS)


import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

np.random.seed(0)

k = 1/25                                                                                             #k represents Time step
E = np.array([[1, 0, 0, 1, 1], 
              [-1, 1, 0, 0, 0], 
              [0, -1, 1, 0, -1], 
              [0, 0, -1, -1, 0]])                                                                   #E represents Incidence Matrix

D = np.array([[3, 0, 0, 0], 
              [0, 2, 0, 0], 
              [0, 0, 3, 0], 
              [0, 0, 0, 2]])                                                                        #D represents Degree Matrix

A = np.array([[0, 1, 1, 1], 
              [1, 0, 1, 0], 
              [1, 1, 0, 1], 
              [1, 0, 1, 0]])                                                                        #A represents Adjacency Matrix
L = D - A                                                                                           #L represents Laplacian Matrix

T = 3 * round(1 / k)                                                                                #T is the time it takes for the simulation
x = np.zeros((4, T))
y = np.zeros((4, T))
l = 5

x[:, 0] = np.array([np.random.randint(2 * 500 * l) / 500, 
                    np.random.randint(2 * 500 * l) / 500, 
                    np.random.randint(2 * 500 * l) / 500, 
                    np.random.randint(2 * 500 * l) / 500]) - l                                      #Random Intial x position
y[:, 0] = np.array([np.random.randint(2 * 500 * l) / 500, 
                    np.random.randint(2 * 500 * l) / 500, 
                    np.random.randint(2 * 500 * l) / 500, 
                    np.random.randint(2 * 500 * l) / 500]) - l                                      #Random Initial y position

x_pos = np.array([0, 1, 1, (1 - np.sqrt(3.5)) / 2])                                                 #Define x position in euclidean space
y_pos = np.array([0, 0, -1, (-1 - np.sqrt(3.5)) / 2])                                               #Define y position in euclidean space

for t in range(T - 1):
    z_xref = np.transpose(E) @ (x_pos)
    z_yref = np.transpose(E) @ (y_pos)
    u_x = k * (E @ z_xref - L @ (x[:, t]))                                                          #Realizing Control Law
    u_y = k * (E @ z_yref - L @ (y[:, t]))                              
    x[:, t+1] = u_x + x[:, t]                                     
    y[:, t+1] = u_y + y[:, t]                                     
    
    plt.clf()                                                                                       #Comment to see the the trajectory            
    plt.plot(x[:, t], y[:, t], ".", markersize=25,markeredgecolor = 'r',color='w',markeredgewidth=1.5)
    plt.xlim([-l, l])
    plt.ylim([-l, l])
    plt.pause(0.1)
plt.plot(x[:, -1], y[:, -1], '-', markersize=5, linewidth=1, color='black')                         #Join agents at final position           
plt.plot([x[0,-1], x[3,-1]], [y[0,-1], y[3,-1]], '-', markersize=5, linewidth=1, color='black')     #Join agents at final position
plt.plot([x[2,-1], x[0,-1]], [y[2,-1], y[0,-1]], '-', markersize=5, linewidth=1, color='black')     #Join agents at final position

for i in range(0,4):
    plt.plot(x[i, -1], y[i, -1], ".", markersize=21,markeredgecolor = 'w',color='w')            
    plt.text(x[i, -1], y[i, -1], str(i+1), fontsize=10, ha='center', va='center')                   #Label Agents from 1 to 4
plt.show()

'''
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(np.transpose(x), label=['Robot 1','Robot 2','Robot 3','Robot 4'])              #Position of x with respect to time
plt.ylabel("x position")       
plt.xlim([1, T])
plt.legend()
plt.subplot(2, 1, 2)
plt.plot(np.transpose(y), label=['Robot 1','Robot 2','Robot 3','Robot 4'])              #Position of y with respect to time
plt.ylabel("y position")
plt.xlim([1, T])
plt.xlabel("Time")
plt.legend()
plt.show()
'''