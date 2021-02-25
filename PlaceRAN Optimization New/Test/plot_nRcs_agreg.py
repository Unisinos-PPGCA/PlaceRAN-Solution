import matplotlib.pyplot as plt
import matplotlib
from matplotlib.lines import Line2D

if __name__ == '__main__':
    const_label = 5.5
    # plot low_capacity solutions [ru1, ru_0_1]
    x = [100, 80.4, 4]
    y = [18.4, 19.7, 27]
    n = ["F1", "R1", "AG1"]

    plt.plot(x[0], y[0], 'o', color="red", markersize=22)
    plt.plot(x[1], y[1], '^', color="red", markersize=22)
    plt.plot(x[2], y[2], "H", color="salmon", markersize=16)
    plt.rcParams.update({'font.size': 22})

    for i, txt in enumerate(n):
        if i < 2:
            plt.annotate(txt, (x[i] - const_label / 2, y[i] + const_label))
        else:
            plt.annotate(txt, (x[i], y[i] + const_label))

    # plot rdn_capacity solutions [ru1, ru_0_1]
    x = [100, 62.7]
    y = [51.1, 45.3]
    n = ["F1", "R1"]

    plt.plot(x[0], y[0], 'o', color="blue", markersize=22)
    plt.plot(x[1], y[1], '^', color="blue", markersize=22)
    plt.rcParams.update({'font.size': 22})

    for i, txt in enumerate(n):
        plt.annotate(txt, (x[i] - const_label / 2, y[i] + const_label))

    # plot high_capacity solutions [ru1, ru_0_1]
    x = [41.1, 32.7]
    y = [70.8, 68.0]
    n = ["F1", "R1"]

    plt.plot(x[0], y[0], 'o', color="green", markersize=22)
    plt.plot(x[1], y[1], '^', color="green", markersize=22)
    plt.rcParams.update({'font.size': 22})
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)

    plt.rcParams.update({'font.size': 20})

    legend_elements = [Line2D([0], [0], color='red', lw=4, label='LC'),
                       Line2D([0], [0], color='blue', lw=4, label='RC'),
                       Line2D([0], [0], color='green', lw=4, label='HC')]

    plt.legend(handles=legend_elements, loc="upper right")

    plt.grid(color='gray', linestyle='--', linewidth=0.5)

    plt.ylim(0, 115)
    plt.xlim(0, 103)

    # plt.legend(labels=['Low Capacity (LC)', 'Random Capacity (RC)', 'High Capacity (HC)'], bbox_to_anchor=(1, 1),
    #            bbox_transform=plt.gcf().transFigure)

    for i, txt in enumerate(n):
        plt.annotate(txt, (x[i] - const_label / 2, y[i] + const_label))

    #plt.plot(75, 30, 'o', color="white")
    #plt.plot(75, 104, 'o', color="white")

    #plt.xlabel("Percentage of CR's (%)", fontsize=16)
    #plt.ylabel("Aggregation Level (%)", fontsize=18)
    # plt.title("Random Capacity - Total")
    plt.savefig("nRCs_aggr.png")
    plt.show()
