import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimHei'

# Define the given points
points = np.random.rand(5, 2) * 10


# Define the least squares fit line equation
def least_squares_fit(points):
    x = points[:, 0]
    y = points[:, 1]
    A = np.vstack([x, np.ones(len(x))]).T
    b_fit, a_fit = np.linalg.lstsq(A, y, rcond=None)[0]
    return a_fit, b_fit


# Given values of a and b
a = a_slider.value
b = b_slider.value

# Calculate the least squares fit line coefficients
a_fit, b_fit = least_squares_fit(points)

# Calculate the least squares fit error
x = points[:, 0]
y = points[:, 1]
y_predicted = a_fit + b_fit * x
least_squares_fit_error = np.sum(np.square(y - y_predicted))

# Calculate the predicted line coefficients and plot it
y_predicted_line = a + b * x
plt.plot(x, y_predicted_line, '--', label='预测线')

# Plot the given points and the least squares fit line
x_range = np.linspace(0, 10, 100)
y_range = a_fit + b_fit * x_range
plt.plot(points[:, 0], points[:, 1], 'o', label='数据点')
plt.plot(x_range, y_range, label='最小二乘法预测线')
plt.xlabel('x')
plt.ylabel('y')
plt.title('最小二乘法 vs 一般预测')
plt.legend()
plt.show()

# Output the results
print(f'预测线: y = {a:.2f} + {b:.2f}x')
print(f'预测线误差: {np.sum(np.square(y - y_predicted_line)):.2f}')
print(f'最小二乘法: y = {a_fit:.2f} + {b_fit:.2f}x')
print(f'最小二乘法误差: {least_squares_fit_error:.2f}')
