import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

if(len(sys.argv) != 3):
    print('Usage: python graph.py <Path to csv file> <Plot title>')
    print('Example: python graph.py ../data/merge.csv \'Merge sort\'')
    sys.exit()

df = pd.read_csv(sys.argv[1])
input_size = df.iloc[:, 1].values
sort_time = df.iloc[:, 2].values

plt.figure()
plt.plot(input_size, sort_time, marker='s', color='b')
plt.xlabel('Input size')
plt.ylabel('Sort time (s)')
plt.title(sys.argv[2])
plt.show()
