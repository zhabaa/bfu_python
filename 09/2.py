import numpy as np

def run_length_encoding(x):
    if len(x) == 0:
        return (np.array([], dtype=x.dtype), np.array([], dtype=int))
    
    changes = np.where(x[:-1] != x[1:])[0] + 1
    starts = np.concatenate(([0], changes))
    ends = np.concatenate((changes, [len(x)]))
    
    values = x[starts]
    counts = ends - starts
    
    return (values, counts)


x = np.array([2, 2, 2, 3, 3, 3, 5])
values, counts = run_length_encoding(x)
print(values, counts)
