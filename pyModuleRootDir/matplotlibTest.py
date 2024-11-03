import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define your points
a = (1, 2, 3)  # Replace these with your actual coordinates
b = (4, 5, 6)

# Create a figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the points
ax.scatter(*a, color='r', label='Point A')
ax.scatter(*b, color='b', label='Point B')

# Add labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

# Display the plot
plt.show()
