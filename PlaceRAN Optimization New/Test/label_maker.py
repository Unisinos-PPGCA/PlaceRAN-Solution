import matplotlib.pyplot as plt
import matplotlib
from matplotlib.lines import Line2D

fig, ax = plt.subplots()

#ax.set_title('Scores by group and gender')

plt.rcParams.update({'font.size': 20})

legend_elements = [Line2D([0], [0], color='royalblue', lw=4, label='LC R1'),
                       #Line2D([0], [0], color='red', lw=4, label='NG-RAN (2)'),
                       Line2D([0], [0], color='darkorange', lw=4, label='RC R1'),
                       #Line2D([0], [0], color='blueviolet', lw=4, label='D-RAN (1)'),
                       Line2D([0], [0], color='green', lw=4, label='HC R1')]
                       #Line2D([0], [0], color='saddlebrown', lw=4, label='D-RAN (1)')]

ax.legend(handles=legend_elements, loc='lower center')
plt.savefig("label.png")
plt.show()
