#%% Impoertier Numpy und Matplotlib
import numpy as np
import matplotlib.pyplot as plt

#%% Schleife für alle 3 Inputdaten
for i in range(3):                         
     x=str(i+1)
     y=("input_data/power_data_"+x+".txt")
     power_data_watts=open(y).read().split("\n")
     z=np.array(power_data_watts)
     plt.title("Line graph "+str(i+1))
     plt.plot(z,color="green")
     plt.show()

# Gut, aber eine flexible Zahl an Dateien wäre noch besser -YS 
# %%
