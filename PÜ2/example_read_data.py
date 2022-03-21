# %% Import der nötigen Pakete
import numpy as np
import matplotlib.pyplot as plt

# %% Öffnen der Datei und konvertieren zu numpy-Array
file_name =  'input_data/power_data_1.txt'
power_data_watts = open(file_name).read().split("\n")
x = np.array(power_data_watts)

# %% Erstellen des Plots
plt.title("Line graph")
plt.plot(x, color="red")
plt.show()


# %%
for i in range(3):
     m = str(i + 1)
     x = ('input_data/power_data_'+m +'.txt')
     power_data_watts = open(x).read().split("\n")
     y = np.array(power_data_watts)
     print(y)
     print(x)
# %%
for i in range(3):
    plt.title("Line graph"+str(i +1))
    plt.plot(y, color="green")
    plt.show()
# %%
