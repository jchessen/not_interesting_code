import numpy as np
import matplotlib.pyplot as plt

# Define the function that we wish to integrate
def f(x):
    return np.sin(x)  # Example function

# Implementation of the trapezoid rule
def trapezoid_rule(func, a, b, n):
    # Compute the width of each trapezoid
    h = (b - a) / n
    
    # Compute the x values (endpoints of each trapezoid)
    x = np.linspace(a, b, n+1)
    
    # Compute the y values (function values at the x endpoints)
    y = func(x)
    
    # The integral approximation using the trapezoid rule
    integral = h * (0.5*y[0] + 0.5*y[-1] + np.sum(y[1:-1]))
    
    return integral, x, y

# Interval bounds and number of trapezoids
a = 0     # Lower bound of the interval
b = np.pi # Upper bound of the interval
n = 10    # Number of trapezoids

# Use the trapezoid rule to approximate the integral
integral, x, y = trapezoid_rule(f, a, b, n)
print("Integral approximation:", integral)

# Plotting the function and the trapezoids
x_vals = np.linspace(a, b, 1000)
y_vals = f(x_vals)

# Plot the function
plt.plot(x_vals, y_vals, label='Function f(x)')

# Plot the trapezoids
for i in range(n):
    plt.fill_between([x[i], x[i+1]], [y[i], y[i+1]], color='gray', alpha=0.5)

# Add labels, legend, and show the plot
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Trapezoid Rule Approximation')
plt.legend()
plt.grid(True)
plt.show()
