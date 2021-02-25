import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['LCR1', 'RCR1', 'HCR1', 'LCF1', 'RCF1', 'HCF1']
RCs = [81, 63, 33, 100, 100, 71]
Agg = [20, 46, 68, 19, 51, 42]
AG1 = [27, 19, 59, 51, 93, 80]
AG2 = [11, 0, 11, 31, 8, 21]
AC1 = [63, 82, 31, 19, 0, 0]

x = [1, 2.4, 3.8, 5.2, 6.6, 8.0]
width1 = 0.5  # the width of the bars
width2 = 0.3  # the width of the bars

x1 = [0.3, 2.1, 4.1, 6.1, 8.1, 10.1]
x2 = [0.7, 2.5, 4.5, 6.5, 8.5, 10.5]
x3 = [1.0, 2.8, 4.8, 6.8, 8.8, 10.8]
x4 = [1.2, 3.0, 5.0, 7.0, 9.0, 11.0]
x5 = [1.4, 3.2, 5.2, 7.2, 9.2, 11.2]

fig, ax = plt.subplots()
rects1 = ax.bar(x1, RCs, width1, label='RCs', color="brown")
rects2 = ax.bar(x2, Agg, width1, label='Agg', color="darkgreen")
rects3 = ax.bar(x3, AG1, width2, label='AG1', color="navy")
rects4 = ax.bar(x4, AG2, width2, label='AG2', color="blue")
rects5 = ax.bar(x5, AC1, width2, label='AC1', color="royalblue")

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel("Information (%)", fontsize=20)
plt.yticks(fontsize=18)

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

fig.tight_layout()

plt.savefig("barras_RC_agg.png")

plt.show()
