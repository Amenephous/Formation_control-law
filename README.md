# Formation-_control-law

This is a Python implementation of the control law on four robots to a particular formation using swarm robotics techniques. The robots move in a coordinated manner to achieve a desired formation, and the code simulates their movements over time.

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

The code uses the numpy package for numerical computations, matplotlib for plotting the trajectories, and networkx for computing the Laplacian matrix.

License
This code is licensed under the MIT License. Feel free to use and modify it for your own purposes.
