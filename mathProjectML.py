import tensorflow as tf
caliGasData2022 = [1.634, 1.626, 1.613, 1.614, 1.618, 1.641, 1.71, 1.729, 1.72, 1.712, 1.681, 1.666, 1.668, 1.667, 1.702, 1.79, 1.849, 1.832, 1.832, 1.832, 1.826, 1.809, 1.797, 1.796, 1.791, 1.777, 1.752, 1.744, 1.721, 1.688, 1.658, 1.647, 1.629, 1.627, 1.6, 1.582, 1.566, 1.59, 1.637, 1.66, 1.662, 1.694, 1.7, 1.695, 1.683, 1.716, 1.754, 1.798, 1.828, 1.867, 1.938, 1.954, 1.951, 1.947, 1.931, 1.946, 1.929, 1.901, 1.859, 1.824, 1.776, 1.722, 1.669, 1.616, 1.56, 1.523, 1.535, 1.643, 1.677, 1.672, 1.66, 1.624, 1.582, 1.55, 1.505, 1.469, 1.422, 1.379, 1.335, 1.293, 1.243, 1.197, 1.141, 1.109, 1.1, 1.129, 1.182, 1.206, 1.224, 1.251, 1.254, 1.286, 1.304, 1.331, 1.454, 1.498, 1.561, 1.592, 1.622, 1.617, 1.613, 1.607, 1.589, 1.571, 1.557, 1.554, 1.563, 1.563, 1.601, 1.618, 1.618, 1.613, 1.604, 1.591, 1.578, 1.593, 1.586, 1.581, 1.593, 1.599, 1.59, 1.58, 1.569, 1.559, 1.546, 1.534, 1.524, 1.521, 1.562, 1.592, 1.587, 1.57, 1.562, 1.54, 1.525, 1.52, 1.532, 1.577, 1.592, 1.634, 1.649, 1.683, 1.752, 1.862, 1.922, 2.012, 2.084, 2.145, 2.143, 2.13, 2.115, 2.077, 2.009, 1.977, 1.928, 1.867, 1.809, 1.763, 1.732, 1.696, 1.787, 1.805, 1.8, 1.785, 1.757, 1.725, 1.707, 1.703, 1.743, 1.92, 2.101, 2.1, 2.085, 2.034, 1.978, 1.912, 1.854, 1.805, 1.769, 1.737, 1.711, 1.685, 1.681, 1.691, 1.68, 1.652, 1.624, 1.615, 1.595, 1.617, 1.667, 1.69, 1.726, 1.753, 1.821, 1.868, 2.029, 2.109, 2.112, 2.097, 2.083, 2.079, 2.126, 2.157, 2.148, 2.124, 2.115, 2.223, 2.269, 2.324, 2.327, 2.316, 2.289, 2.259, 2.237, 2.204, 2.193, 2.186, 2.162, 2.128, 2.092, 2.055, 2.051, 2.1, 2.073, 2.053, 2.057, 2.094, 2.198, 2.327, 2.402, 2.394, 2.369, 2.341, 2.311, 2.263, 2.236, 2.192, 2.135, 2.049, 2.01, 1.982, 1.932, 1.932, 1.959, 2.034, 2.053, 2.091, 2.15, 2.176, 2.229, 2.287, 2.312, 2.376, 2.464, 2.592, 2.584, 2.565, 2.56, 2.516, 2.473, 2.434, 2.391, 2.36, 2.333, 2.352, 2.412, 2.457, 2.525, 2.538, 2.541, 2.549, 2.601, 2.716, 2.75, 2.77, 3.056, 3.004, 2.954, 2.947, 2.973, 2.964, 2.902, 2.827, 2.747, 2.659, 2.582, 2.453, 2.412, 2.335, 2.277, 2.249, 2.233, 2.213, 2.328, 2.417, 2.424, 2.513, 2.544, 2.522, 2.473, 2.439, 2.48, 2.532, 2.635, 2.669, 2.743, 2.811, 2.896, 3.068, 3.202, 3.332, 3.33, 3.323, 3.266, 3.269, 3.225, 3.198, 3.163, 3.189, 3.224, 3.24, 3.22, 3.198, 3.192, 3.211, 3.162, 3.098, 3.01, 2.949, 2.848, 2.76, 2.683, 2.601, 2.54, 2.481, 2.434, 2.396, 2.464, 2.495, 2.493, 2.496, 2.504, 2.561, 2.607, 2.61, 2.632, 2.583, 2.538, 2.491, 2.535, 2.632, 2.71, 2.796, 2.897, 3.068, 3.121, 3.152, 3.228, 3.252, 3.305, 3.316, 3.359, 3.461, 3.45, 3.436, 3.407, 3.374, 3.32, 3.236, 3.192, 3.157, 3.136, 3.158, 3.118, 3.06, 3.016, 2.928, 2.862, 2.791, 2.791, 2.839, 2.904, 2.961, 2.973, 2.996, 3.053, 3.143, 3.159, 3.231, 3.366, 3.395, 3.398, 3.361, 3.329, 3.285, 3.261, 3.298, 3.328, 3.29, 3.226, 3.148, 3.107, 3.108, 3.191, 3.328, 3.459, 3.537, 3.604, 3.602, 3.608, 3.685, 3.774, 3.846, 3.892, 3.903, 3.919, 3.952, 4.099, 4.242, 4.433, 4.588, 4.585, 4.573, 4.55, 4.52, 4.46, 4.317, 4.205, 4.118, 4.037, 3.955, 3.905, 3.859, 3.804, 3.725, 3.67, 3.601, 3.47, 3.355, 3.13, 2.783, 2.555, 2.374, 2.112, 1.955, 1.805, 1.738, 1.806, 1.81, 1.874, 1.988, 2.064, 2.095, 2.113, 2.215, 2.291, 2.261, 2.189, 2.196, 2.162, 2.154, 2.248, 2.308, 2.336, 2.34, 2.34, 2.355, 2.424, 2.524, 2.637, 2.756, 2.891, 2.979, 3.005, 2.984, 2.952, 2.88, 2.829, 2.829, 2.896, 3.04, 3.047, 3.031, 3.037, 3.099, 3.153, 3.14, 3.098, 3.069, 3.015, 2.988, 2.985, 2.987, 2.981, 2.961, 2.94, 2.921, 2.912, 2.903, 2.912, 2.933, 2.987, 3.046, 3.026, 3.008, 2.975, 2.961, 2.926, 2.918, 2.999, 3.046, 3.061, 3.091, 3.087, 3.088, 3.096, 3.09, 3.088, 3.118, 3.139, 3.118, 3.049, 3.024, 3.068, 3.053, 3.1, 3.126, 3.117, 3.113, 3.13, 3.134, 3.129, 3.172, 3.165, 3.14, 3.092, 3.041, 3.026, 3.005, 2.996, 3.013, 3.089, 3.147, 3.143, 3.145, 3.141, 3.175, 3.171, 3.152, 3.216, 3.25, 3.247, 3.287, 3.308, 3.332, 3.349, 3.357, 3.364, 3.397, 3.447, 3.555, 3.719, 3.874, 3.954, 3.966, 4.028, 4.057, 4.161, 4.205, 4.217, 4.257, 4.254, 4.218, 4.121, 4.056, 3.994, 3.94, 3.9, 3.839, 3.794, 3.778, 3.8, 3.818, 3.811, 3.798, 3.734, 3.734, 3.809, 3.944, 3.944, 3.923, 3.887, 3.835, 3.815, 3.864, 3.858, 3.846, 3.855, 3.84, 3.786, 3.718, 3.655, 3.611, 3.556, 3.576, 3.635, 3.707, 3.7, 3.714, 3.741, 3.758, 3.835, 4.035, 4.292, 4.358, 4.376, 4.375, 4.359, 4.322, 4.28, 4.235, 4.203, 4.186, 4.213, 4.367, 4.336, 4.312, 4.26, 4.164, 4.029, 3.887, 3.773, 3.733, 3.753, 3.808, 3.802, 3.868, 4.096, 4.129, 4.158, 4.176, 4.178, 4.155, 4.151, 4.176, 4.659, 4.623, 4.432, 4.169, 3.996, 3.858, 3.783, 3.747, 3.696, 3.619, 3.525, 3.506, 3.554, 3.605, 3.615, 3.63, 3.676, 3.904, 4.044, 4.154, 4.211, 4.212, 4.174, 4.12, 4.069, 4.053, 4.033, 3.992, 3.934, 3.905, 3.911, 4.04, 4.048, 4.022, 3.977, 3.969, 3.989, 4.075, 4.002, 3.985, 4.015, 4.036, 4.002, 3.95, 3.901, 3.83, 3.802, 3.822, 3.899, 4.051, 4.005, 3.932, 3.85, 3.791, 3.766, 3.718, 3.665, 3.603, 3.56, 3.547, 3.576, 3.58, 3.574, 3.594, 3.647, 3.667, 3.635, 3.589, 3.582, 3.59, 3.626, 3.697, 3.795, 3.855, 3.897, 3.958, 3.969, 3.997, 4.028, 4.156, 4.206, 4.254, 4.222, 4.169, 4.159, 4.135, 4.127, 4.106, 4.102, 4.102, 4.132, 4.128, 4.09, 4.034, 3.991, 3.948, 3.926, 3.898, 3.876, 3.843, 3.816, 3.786, 3.728, 3.693, 3.666, 3.598, 3.489, 3.39, 3.3, 3.217, 3.151, 3.072, 3.047, 2.979, 2.878, 2.75, 2.68, 2.671, 2.594, 2.484, 2.44, 2.441, 2.627, 2.798, 2.959, 3.418, 3.439, 3.356, 3.267, 3.209, 3.147, 3.102, 3.158, 3.433, 3.711, 3.732, 3.807, 3.757, 3.693, 3.591, 3.511, 3.48, 3.45, 3.432, 3.88, 3.897, 3.812, 3.724, 3.565, 3.584, 3.483, 3.342, 3.266, 3.155, 3.072, 2.994, 2.949, 2.914, 2.861, 2.847, 2.817, 2.824, 2.78, 2.716, 2.691, 2.679, 2.654, 2.736, 2.825, 2.875, 2.842, 2.712, 2.643, 2.551, 2.486, 2.378, 2.295, 2.406, 2.441, 2.596, 2.681, 2.782, 2.776, 2.75, 2.771, 2.775, 2.809, 2.786, 2.789, 2.804, 2.812, 2.84, 2.864, 2.866, 2.929, 2.91, 2.866, 2.858, 2.792, 2.725, 2.681, 2.643, 2.702, 2.709, 2.706, 2.753, 2.763, 2.764, 2.809, 2.799, 2.805, 2.798, 2.824, 2.809, 2.755, 2.69, 2.672, 2.682, 2.666, 2.67, 2.706, 2.779, 2.804, 2.794, 2.783, 2.791, 2.825, 2.874, 2.898, 2.956, 3, 3.005, 3.001, 2.998, 2.992, 3.008, 3.017, 3.017, 3.002, 2.986, 3.005, 3.094, 3.127, 3.104, 3.038, 2.996, 2.953, 2.946, 2.949, 2.934, 2.941, 2.981, 2.989, 3.014, 3.028, 3.035, 3.164, 3.186, 3.163, 3.143, 3.111, 3.083, 3.077, 3.064, 3.066, 3.243, 3.275, 3.222, 3.2, 3.16, 3.12, 3.106, 3.133, 3.148, 3.199, 3.196, 3.209, 3.296, 3.37, 3.358, 3.349, 3.36, 3.356, 3.392, 3.431, 3.487, 3.541, 3.522, 3.553, 3.567, 3.609, 3.632, 3.599, 3.618, 3.636, 3.632, 3.618, 3.591, 3.562, 3.546, 3.55, 3.535, 3.514, 3.505, 3.501, 3.491, 3.462, 3.471, 3.498, 3.513, 3.52, 3.527, 3.624, 3.707, 3.708, 3.709, 3.683, 3.644, 3.582, 3.526, 3.478, 3.399, 3.318, 3.271, 3.253, 3.219, 3.183, 3.161, 3.148, 3.13, 3.131, 3.155, 3.161, 3.184, 3.195, 3.223, 3.264, 3.389, 3.529, 3.718, 3.922, 3.948, 3.982, 4.006, 3.968, 3.934, 3.878, 3.83, 3.745, 3.678, 3.613, 3.621, 3.627, 3.605, 3.569, 3.551, 3.537, 3.487, 3.463, 3.44, 3.491, 3.494, 3.496, 3.613, 3.953, 4.091, 4.089, 4.03, 3.948, 3.953, 3.921, 3.847, 3.753, 3.674, 3.58, 3.508, 3.457, 3.438, 3.428, 3.419, 3.408, 3.388, 3.371, 3.366, 3.358, 3.36, 3.353, 3.325, 3.222, 3.066, 2.953, 2.872, 2.751, 2.7, 2.652, 2.635, 2.65, 2.688, 2.766, 2.798, 2.855, 2.891, 2.939, 2.963, 2.981, 3.022, 3.031, 3.049, 3.058, 3.054, 3.067, 3.092, 3.1, 3.106, 3.102, 3.086, 3.069, 3.061, 3.049, 3.047, 3.051, 3.033, 3.029, 3.027, 3.025, 3.032, 3.041, 3.04, 3.06, 3.085, 3.1, 3.145, 3.213, 3.245, 3.272, 3.316, 3.35, 3.451, 3.563, 3.638, 3.731, 3.76, 3.77, 3.787, 3.803, 3.835, 3.862, 3.906, 3.952, 3.981, 4.014, 4.057, 4.078, 4.086, 4.087, 4.126, 4.141, 4.165, 4.179, 4.174, 4.213, 4.234, 4.256, 4.232, 4.226, 4.227, 4.225, 4.217, 4.217, 4.241, 4.268, 4.339, 4.393, 4.439, 4.473, 4.532, 4.551, 4.554, 4.53, 4.513, 4.503, 4.485, 4.501, 4.503, 4.497, 4.486, 4.488, 4.507, 4.524, 4.57, 4.671, 5.187, 5.587, 5.71, 5.764, 5.714, 5.619, 5.545, 5.514, 5.526, 5.654, 5.793, 5.904, 5.993, 6.178, 6.271, 6.216, 6.138, 6.042, 5.903, 5.708, 5.573, 5.472, 5.298, 5.218, 5.146, 5.061, 5.053, 5.182, 5.239, 5.615, 6.213, 6.156, 5.847, 5.5, 5.311, 5.228, 5.21, 5.034, 4.813, 4.564, 4.352, 4.198, 4.155, 4.216, 4.228, 4.248, 4.276, 4.358, 4.414, 4.428, 4.518, 4.586, 4.704, 4.732, 4.656, 4.634, 4.625, 4.682, 4.725]

finalList = []
for i in range(len(caliGasData2022)-14):
  listA = []
  for j in range(15):
    listA.append(caliGasData2022[j+i] / 10)
    finalList.append(listA)

print(len(finalList))
print(len(finalList[0]))
predictLastK = 52
train = finalList[0: int(len(finalList)) - predictLastK]
test = finalList[int(len(finalList)) - predictLastK: int(len(finalList))]
print(len(test))
print(len(test[0]))
print(len(train))
print(len(train[0]))
print(train[0])
print(test[0])
train_x = []
train_y = []
test_x = []
test_y = []

for i in range(len(train)):
    train_x.append(train[i][0: len(train[0]) - 1])
    train_y.append(train[i][len(train[0]) - 1])
for i in range(len(test)):
    test_x.append(test[i][0: len(test[0]) - 1])
    test_y.append(test[i][len(train[0]) - 1])

print(test_x[0])
print(test_y[0])
print(train_x[0])
print(train_y[0])
model = tf.keras.models.Sequential([
    tf.keras.layers.Input(shape=(len(train_x[0]),)),
    tf.keras.layers.Dense(128, activation='relu'),
    #tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
print(model.input_shape, model.output_shape)
print(len(train_x[0]))
print(model.predict([test_x[0]]))
model.compile(optimizer='adam',
              loss='mean_squared_error')
model.fit(train_x, train_y, epochs=20)
model.evaluate(test_x, test_y)
print(10 * model.predict([test_x[0]]))
print(test_y[0])
sum = 0
max_error = 0
moneySpentIdeal = 0
moneySpentModel = 0
moneySpentWorst = 0
moneySaved = 0
for i in range(predictLastK - 2):
    prediction = 10 * model.predict([test_x[i]])
    day2 = [test_x[i + 1]]
    day2[len(day2) - 1] = prediction / 10
    if abs(prediction - 10 * test_y[i]) > max_error:
        max_error = abs(prediction - 10 * test_y[i])
    sum += abs(prediction - 10 * test_y[i])
print(sum / len(test_x))
print(max_error)
