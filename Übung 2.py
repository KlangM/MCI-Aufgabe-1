# %% Import der nötigen Pakete
import numpy as np
import matplotlib.pyplot as plt

# %%
for i in range(3):
    m = str(i + 1)
    x = ('PÜ2\input_data\power_data_'+m +'.txt')
    power_data_watts = open(x).read().split("\n")
    y = np.array(power_data_watts)
print(y)
# %%


# %%
