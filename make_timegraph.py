#using numpy and matplotlib library, plot a png file
#if ordering = True switches on the ordering of legends in graph as maximum to minimum

#import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#####################
filename = 'Flat_MSD.csv'
ordering = True
xlabel = "x_label"
ylabel = "y_label"
title = "title"
###################

#read file
df = pd.read_csv(filename)
print(df.head())

num_arrays = len(df.columns.values)
arrays = [[] for _ in range(num_arrays)]

final_time_array = []

for i in range(len(df.columns.values)):
    arrays[i] = df[df.columns.values[i]].to_numpy()
    final_time_array.append(arrays[i][-1])

time_scale = arrays[0]


arrays_2 = arrays[1:]     #copy of the main arrays without the timescale column
final_time_array_2 = final_time_array[1:]

print(final_time_array_2)


##Plotting###
for i in range(len(arrays_2)):
    plt.plot(time_scale, arrays_2[i], label = df.columns.values[i+1])



if ordering:                           #legends ordered in numerical order
    order_array = []
    sorted_array = sorted(final_time_array_2, reverse = True)
    for i in sorted_array:
        index = final_time_array_2.index(i)
        order_array.append(index)
    
    handles, labels = plt.gca().get_legend_handles_labels()
    print(handles)
    print(labels)
    plt.legend([handles[idx] for idx in order_array],[labels[idx] for idx in order_array], bbox_to_anchor= [1,1])
    print(final_time_array_2)
    print(sorted_array)            
    print(order_array)

else:
    plt.legend(bbox_to_anchor = [1,1])    #fix the location of the legend
#print(arrays)

plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title(title)
plt.savefig(filename.replace('csv','png'), dpi=600, bbox_inches='tight')
plt.show()
