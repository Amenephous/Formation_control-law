# Formation_control-law

This is a Python implementation of the control law on four robots to a particular formation using swarm robotics techniques. The robots move in a coordinated manner to achieve a desired formation, and the code simulates their movements over time.

![Formation](https://github.com/Amenephous/Formation-_control-law/assets/48127920/38dd7efe-988b-4e4d-aa7b-92f219cbb3ae)

Desired Formation with distance between the bots.


Requirements
To run this code, you need the following Python packages:

numpy
matplotlib
networkx
You can install them using pip:

bash
Copy code
pip install numpy matplotlib networkx
Usage
To run the code, simply execute the control_law.py file:

bash
Copy code
python Formation control Swarm.py
This will run the simulation and display the trajectories of the four robots in a formation. You can also uncomment the code at the end to display the position of each robot over time.


Explanation
The code implements the control law for four robots in a particular formation. The robots are modeled as points in a two-dimensional space, and their movements are governed by a control law that keeps them in a desired formation. The control law is based on the Laplacian matrix of the robot network, which determines the interaction between the robots.

The code uses the incidence matrix, degree matrix, and adjacency matrix to compute the Laplacian matrix. It then uses this matrix to calculate the control input for each robot, which is based on the difference between the robot's current position and the desired position in the formation.

Assuming each agent has state space dynamics ui with ui in R^2 and u = [u1,u2,u3,u4], the second order linear control law can be implemented using the equation:

u = -k * L * x + k * E * z_ref

where:

k is a positive gain
L is the Laplacian matrix
E is the incidence matrix 
z_ref is the reference input vector

This control law is designed to control the system dynamics and stabilize the system around a desired reference input z_ref. By tuning the controller gain matrix k and the state feedback matrix L, the stability and performance of the system can be improved.

The code uses the numpy package for numerical computations, matplotlib for plotting the trajectories, and networkx for computing the Laplacian matrix.


https://github.com/Amenephous/Formation-_control-law/assets/48127920/9d7e5012-b8fc-4ccf-bb79-e873081235e1

Simulation of Formation Control for 4 bots randomly placed in space.


