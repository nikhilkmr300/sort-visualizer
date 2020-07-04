import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import sys

if(len(sys.argv) <= 1):
    print('Usage: python compare.py <csv_file_1> <csv_file_2> ...')
    sys.exit()

fig, ax = plt.subplots(1, 1)
ax.set_xlabel('Input size')
ax.set_ylabel('Sort time (s)')
for i in range(1, len(sys.argv)):
    df = pd.read_csv(sys.argv[i])

    input_size = df.iloc[:, 1].values
    sort_time = df.iloc[:, 2].values

    # Cropping for small_compare
    """
    mask = input_size <= 150
    input_size = input_size[mask]
    sort_time = sort_time[mask]
    """

    label = (sys.argv[i].split('/'))[-1][:-4].capitalize()

    ax.plot(input_size, sort_time, label=label)
ax.legend()
plt.show()
