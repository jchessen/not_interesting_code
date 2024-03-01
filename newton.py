import numpy as np
import matplotlib.pyplot as plt

# Define the function whose root we are trying to find
def f(x):
    return x**3-2*x**2 - 1

# Define the derivative of the function
def f_prime(x):
    return 3*x**2 -4*x

# Newton's method implementation
def newtons_method(func, func_prime, x0, tol=1e-7, max_iter=1000):
    # Set initial guess
    x = x0
    # List to store the sequence of approximations
    sequence = [x]

    for _ in range(max_iter):
        # Calculate the function value and derivative
        f_x = func(x)
        f_prime_x = func_prime(x)
        
        # Check if the derivative is zero to avoid division by zero
        if f_prime_x == 0:
            print("Zero derivative. No solution found.")
            return None, sequence
        
        # Newton's method formula
        x_new = x - f_x / f_prime_x
        sequence.append(x_new)
        
        # Check if the process is within tolerance
        if abs(x_new - x) < tol:
            return x_new, sequence
        
        # Update the estimate
        x = x_new
    
    # Maximum iteration reached without convergence
    print("Max iterations reached without convergence.")
    return None, sequence

# Use Newton's method to find the root
initial_guess = 1.0
root, sequence = newtons_method(f, f_prime, initial_guess)

# Output the result
if root is not None:
    print("Root is approximately:", root)
    print("Number of iterations:", len(sequence) - 1)
else:
    print("No root found.")

# Plotting
x_vals = np.linspace(min(sequence) - 1, max(sequence) + 1, 400)
y_vals = f(x_vals)

# Plot the function
plt.plot(x_vals, y_vals, label='Function f(x)')

# Plot the root if found
if root is not None:
    plt.plot(root, f(root), 'ro', label='Root')

# Plot the initial guess
plt.plot(initial_guess, f(initial_guess), 'go', label='Initial guess')

# Add the iterations (estimates)
plt.plot(sequence, f(np.array(sequence)), 'x', label='Estimates')

# Add labels, legend, and show the plot
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Newton\'s Method')
plt.legend()
plt.grid(True)
plt.show()
