#using numpy and matplotlib library, plot a png file

#import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#####################
filename = '1FmigrationResultsData.csv'
xlabel = "x_label"
ylabel = "y_label"
title = "title"
###################

#read file
df = pd.read_csv(filename)
print(df.head())


title_names = []
for i in df.columns.values:
    if ".csv" in i:
        title_names.append(i.replace(".csv",""))
print(title_names)
        
print("\ntotal of " + str(len(title_names)) + " data are plotted.")
print("Please verify with your csv files if these are the number of columns in your original dataset.\n")

x_array = []
y_array = []

i = 0
while i< (len(df.columns.values)):
    x_array_i = df[df.columns.values[i]].to_numpy()
    y_array_i = df[df.columns.values[i+1]].to_numpy()
    x_array_i = np.array(x_array_i[2:],dtype='d')
    y_array_i = np.array(y_array_i[2:],dtype='d')
    #print(x_array_i)
    #print(y_array_i)
    x_array.append(x_array_i)
    y_array.append(y_array_i)
    
    i+=2

for index in range(len(title_names)):   #(len(title_names)):
    title_index = title_names[index]
    #print(title_index)
    plt.plot(x_array[index], y_array[index], label = title_index ,linewidth = 1)

plt.title(title)
plt.legend(bbox_to_anchor = [1,1])
plt.savefig(fname=filename.replace(".csv",".png"), dpi=600, bbox_inches='tight')
plt.show()
