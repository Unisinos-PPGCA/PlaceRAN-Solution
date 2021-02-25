import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon
from matplotlib.ticker import MaxNLocator
import numpy as np

i = 1
x = [1, 2, 3, 4]

rcs_lcr1 = [0, 112, 112, 112]
rcs_rcr1 = [106, 107, 108, 108]
rcs_hcr1 = [102, 102, 103, 103]

rcs_lcf1 = [0, 0, 128, 128]
rcs_rcf1 = [127, 128, 128, 128]
rcs_hcf1 = [127, 128, 128, 128]

agg_lcr1 = [0, 173, 207, 207]
agg_rcr1 = [271, 345, 346, 346]
agg_hcr1 = [489, 492, 498, 498]

agg_lcf1 = [0, 0, 238, 238]
agg_rcf1 = [332, 456, 457, 457]
agg_hcf1 = [606, 627, 641, 641]

fo_lcr1 = [0, 61, 95, 95]
fo_rcr1 = [165, 238, 238, 238]
fo_hcr1 = [387, 390, 395, 395]

fo_lcf1 = [0, 0, 110, 110]
fo_rcf1 = [205, 328, 329, 329]
fo_hcf1 = [479, 499, 513, 513]

n_rcs = 128

fo_max_r1 = 606
agg_max_r1 = 505

fo_max_f1 = 630
agg_max_f1 = 756

######################################## COMENTE ESTE CODIGO PARA GRAFICO DE R1 ########################################
# rcs_lcr1 = rcs_lcf1
# rcs_rcr1 = rcs_rcf1
# rcs_hcr1 = rcs_hcf1
#
# agg_lcr1 = agg_lcf1
# agg_rcr1 = agg_rcf1
# agg_hcr1 = agg_hcf1
#
# fo_lcr1 = fo_lcf1
# fo_rcr1 = fo_rcf1
# fo_hcr1 = fo_hcf1
#
# fo_max_r1 = fo_max_f1
# agg_max_r1 = agg_max_f1
########################################################################################################################

#transformar para %
for i in range(0, 4):
    rcs_lcr1[i] = (rcs_lcr1[i] * 100) / n_rcs
    rcs_rcr1[i] = (rcs_rcr1[i] * 100) / n_rcs
    rcs_hcr1[i] = (rcs_hcr1[i] * 100) / n_rcs

    agg_lcr1[i] = (agg_lcr1[i] * 100) / agg_max_r1
    agg_rcr1[i] = (agg_rcr1[i] * 100) / agg_max_r1
    agg_hcr1[i] = (agg_hcr1[i] * 100) / agg_max_r1

    fo_lcr1[i] = (fo_lcr1[i] * 100) / fo_max_r1
    fo_rcr1[i] = (fo_rcr1[i] * 100) / fo_max_r1
    fo_hcr1[i] = (fo_hcr1[i] * 100) / fo_max_r1

fig, (ax1, ax2, ax3) = plt.subplots(3)

labels = ['1', '2', '3', '4']

x = np.arange(len(labels))  # the label locations
width = 0.15  # the width of the bars

x1 = [1-width, 2-width, 3-width, 4-width]
x2 = [1, 2, 3, 4]
x3 = [1+width, 2+width, 3+width, 4+width]

ax1.bar(x1, fo_lcr1, width, label='Women', color='red')
ax1.bar(x2, fo_rcr1, width, label='FOLC', color='blue')
ax1.bar(x3, fo_hcr1, width, label='Women', color='green')

ax1.yaxis.grid(color='gray', linestyle='--', linewidth=0.5)

custom_lines = [Line2D([0], [0], color="white", lw=0)]

# ax1.legend(custom_lines, ['Objective Function (%)'], loc="upper center")
# ax2.legend(custom_lines, ['CRs (%)'], loc="upper center")
# ax3.legend(custom_lines, ['Aggregation Level (%)'], loc="upper center")

ax1.set_xticks([1, 2, 3, 4])
ax1.set_yticks([0, 20, 40, 60, 80, 100])

ax1.set_ylim(0, 120)
ax1.set_xlim(0.7, 4.3)
ax2.set_ylim(0, 125)
ax2.set_xlim(0.7, 4.3)
ax3.set_ylim(0, 120)
ax3.set_xlim(0.7, 4.3)

ax2.bar(x1, rcs_lcr1, width, label='Women', color='red')
ax2.bar(x2, rcs_rcr1, width, label='Men', color='blue')
ax2.bar(x3, rcs_hcr1, width, label='Women', color='green')

ax2.yaxis.grid(color='gray', linestyle='--', linewidth=0.5)

ax2.set_xticks([1, 2, 3, 4])
ax2.set_yticks([0, 20, 40, 60, 80, 100])

ax3.bar(x1, agg_lcr1, width, label='Women', color='red')
ax3.bar(x2, agg_rcr1, width, label='Men', color='blue')
ax3.bar(x3, agg_hcr1, width, label='Women', color='green')

ax3.yaxis.grid(color='gray', linestyle='--', linewidth=0.5)

ax3.set_xticks([1, 2, 3, 4])
ax3.set_yticks([0, 20, 40, 60, 80, 100])

for tick in ax1.yaxis.get_major_ticks():
    tick.label.set_fontsize(13)

for tick in ax2.yaxis.get_major_ticks():
    tick.label.set_fontsize(13)

for tick in ax3.yaxis.get_major_ticks():
    tick.label.set_fontsize(13)

ax1.errorbar(x1, fo_lcr1, yerr=[0, 0, 0, 0], fmt = 'd', color='black', ecolor="red", capsize=7)
ax1.errorbar(x2, fo_rcr1, yerr=[0, 0, 0, 0], fmt = 'd', color='black', ecolor="blue", capsize=6)
ax1.errorbar(x3, fo_hcr1, yerr=[0, 0, 0, 0], fmt = 'd', color='black', ecolor="green", capsize=6)

ax2.errorbar(x1, rcs_lcr1, yerr=[0, 0, 0, 0], fmt = 'd', color='black', ecolor="red", capsize=7)
ax2.errorbar(x2, rcs_rcr1, yerr=[0, 0, 0, 0], fmt = 'd', color='black', ecolor="blue", capsize=6)
ax2.errorbar(x3, rcs_hcr1, yerr=[0, 0, 0, 0], fmt = 'd', color='black', ecolor="green", capsize=6)

ax3.errorbar(x1, agg_lcr1, yerr=[0, 0, 0, 0], fmt = 'd', color='black', ecolor="red", capsize=7)
ax3.errorbar(x2, agg_rcr1, yerr=[0, 0, 0, 0], fmt = 'd', color='black', ecolor="blue", capsize=6)
ax3.errorbar(x3, agg_hcr1, yerr=[0, 0, 0, 0], fmt = 'd', color='black', ecolor="green", capsize=6)

plt.savefig("k_paths_TLF_R1.png")
plt.show()

