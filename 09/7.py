import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

species = iris[:, -1]

unique_species, counts = np.unique(species, return_counts=True)

print("Уникальные виды и их количество:")
for s, c in zip(unique_species, counts):
    print(s.decode('utf-8'), c)
