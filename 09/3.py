import numpy as np

arr = np.random.normal(size=(10, 4))

min_val = np.min(arr)
max_val = np.max(arr)
mean_val = np.mean(arr)
std_val = np.std(arr)

print(f"Min: {min_val}, Max: {max_val}, Mean: {mean_val}, Std: {std_val}")

first_5_rows = arr[:5]