import torch
import numpy as np

data = [[1, 2], [3, 4]]
np_array = np.array(data)

print(data)
print(np_array)

x_data = torch.tensor(data)
x_np = torch.from_numpy(np_array)
print(x_data)
print(x_np)

print(x_data == x_np)
