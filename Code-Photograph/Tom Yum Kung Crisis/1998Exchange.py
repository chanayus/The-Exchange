""" Exchange """
import matplotlib.pyplot as plt
def main():
    """ function """
    x = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN",\
     "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    y = [52.95, 43.05, 39.125, 38.55, 40.39, 42.2, 40.8, 41.9, 39.55, 36.8, 36.15, 36.35]#input rate exchange
    avg = sum(y)/12
    plt.plot(x, y, color="orange", marker="o", label="Exchange Rate")
    plt.axhline(avg, linestyle="--", label="Average")
    plt.title("Exchange Rate 1998", color="red", fontsize=18)
    plt.ylabel("Rate")
    plt.xlabel("Month")
    plt.legend()
    plt.show()
main()
