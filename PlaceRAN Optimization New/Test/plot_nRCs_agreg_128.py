import matplotlib.pyplot as plt
import matplotlib
from matplotlib.lines import Line2D

if __name__ == '__main__':
    const_label = 5.5
    # plot low_capacity solutions [ru1, ru_0_1]
    x = [100, 87.5]
    y = [31.5, 34.2]
    n = ["F1", "R1"]

    plt.plot(x[0], y[0], 'o', color="red", markersize=22)
    plt.plot(x[1], y[1], '^', color="red", markersize=22)
    plt.rcParams.update({'font.size': 22})

    for i, txt in enumerate(n):
        plt.annotate(txt, (x[i] - const_label / 2, y[i] + const_label))

    # plot rdn_capacity solutions [ru1, ru_0_1]
    x = [71.1, 64.1]
    y = [60.5, 57.1]
    n = ["F1", "R1"]

    plt.plot(x[0], y[0], 'o', color="blue", markersize=22)
    plt.plot(x[1], y[1], '^', color="blue", markersize=22)
    plt.rcParams.update({'font.size': 22})

    for i, txt in enumerate(n):
        plt.annotate(txt, (x[i] - const_label / 2, y[i] + const_label))

    # plot high_capacity solutions [ru1, ru_0_1]
    x = [21.1, 21.1]
    y = [84.8, 82.2]
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

    plt.ylim(0, 105)
    plt.xlim(15, 105)

    # plt.legend(labels=['Low Capacity (LC)', 'Random Capacity (RC)', 'High Capacity (HC)'], bbox_to_anchor=(1, 1),
    #            bbox_transform=plt.gcf().transFigure)

    for i, txt in enumerate(n):
        if i:
            plt.annotate(txt, (x[i] + 3, y[i] - 4))
        else:
            plt.annotate(txt, (x[i]+3, y[i] + 2))

    plt.plot(75, 30, 'o', color="white")
    plt.plot(75, 100, 'o', color="white")

    #plt.xlabel("CRs (%)", fontsize=16)
    #plt.ylabel("Aggregation Level (%)", fontsize=18)
    # plt.title("Random Capacity - Total")
    plt.savefig("nRCs_aggr_128.png")
    plt.show()
