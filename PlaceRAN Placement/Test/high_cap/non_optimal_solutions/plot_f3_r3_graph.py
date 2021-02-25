import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import json

with open("solution_f3.json") as json_file:

    data = json.load(json_file)

    steps = data["steps"]

    i = 1
    x = []
    rcs = []
    aggs = []
    gap = []
    for item in steps:
        rcs.append((item["RCs"]*100)/51)
        aggs.append((item["Agg"]*100)/918)
        gap.append(item["gap"])
        x.append(i)
        i += 1

    plt.plot(x, rcs, color="maroon")
    plt.plot(x, aggs, color="red")
    plt.plot(x, gap, color="coral")

    fig, ax = plt.subplots()

    ax.xaxis.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.ylim(0, 105)
    plt.xlim(0, 33)

with open("solution_f3.json") as json_file:

    data = json.load(json_file)

    steps = data["steps"]

    i = 1
    x = []
    rcs = []
    aggs = []
    gap = []
    for item in steps:
        rcs.append((item["RCs"] * 100) / 51)
        aggs.append((item["Agg"] * 100) / 918) #480 for R3
        gap.append(item["gap"])
        x.append(i)
        i += 1

    best_bound = []

    for i in range(len(x)):
        best_bound.append((800*100)/918) # 480 for R3

    plt.plot(x, rcs, color="navy", linewidth=2.5)
    plt.plot(x, aggs, color="darkgreen", linewidth=2.5)
    plt.plot(x, gap, color="gray", linewidth=2.5)
    plt.plot(x, best_bound, color="red", linewidth=2.5)

    legend_elements = [Line2D([0], [0], color='navy', lw=4, label='RCs'),
                       Line2D([0], [0], color='darkgreen', lw=4, label='Aggregation level'),
                       Line2D([0], [0], color='gray', lw=4, label='Gap'),
                       Line2D([0], [0], color='red', lw=4, label='Best Bound')]

    plt.legend(handles=legend_elements, loc="lower left")

    plt.savefig("f3_non_optimal.png")

    plt.ylabel('Solutions informations (%)')
    plt.show()