#%% #importieren von nötigen Bibliotheken
import numpy as np
import matplotlib.pyplot as plt

#%% #schleife zum importieren der Daten
for i in range(3):                         
     m = str(i + 1)
     x = ('PÜ2\input_data\power_data_'+str(i +1) +'.txt')
     power_data_watts = open(x).read().split("\n")
     y = np.array(power_data_watts)
     plt.title("Line graph" +str(i+1))
     plt.plot(y, color="green")
     plt.show()
# %%
