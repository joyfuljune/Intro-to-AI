import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Create color maps for the plot
cmap_light = ListedColormap(['#FFAAAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#0000FF'])

# Plot the decision boundary by assigning a color to each point in the mesh [x_min, x_max] x [y_min, y_max].
# Increase step size to increase the resolution of the plot
h = 0.02
x_min, x_max = x[:, 0].min() - 0.5, x[:, 0].max() + 0.5
y_min, y_max = x[:, 1].min() - 0.5, x[:, 1].max() + 0.5
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.figure(figsize=(10, 6))
plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

# Plot the training points and testing points
plt.scatter(x_train[:, 0], x_train[:, 1], c=y_train, cmap=cmap_bold, edgecolor='k')
# plt.scatter(x_test[:, 0], x_test[:, 1], c=y_test, cmap=cmap_bold, marker='x', s=80, linewidth=2)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title("KNN (k = %i) classification" % knn.n_neighbors)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
