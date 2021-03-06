""" Exchange """
import matplotlib.pyplot as plt
def main():
    """ function """
    x = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN",\
     "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    y = [25.91, 25.892, 25.96, 26.125, 24.9, 24.7, 32.25, 34.25, 35.8, 40.3, 40.7, 47.05]#input rate exchange
    avg = sum(y)/12
    plt.plot(x, y, color="red", marker="o", label="Exchange Rates")
    plt.axhline(avg, linestyle="--", label="Average")
    plt.title("Exchange Rates 1997", color="red", fontsize=18)
    plt.ylabel("Rates")
    plt.xlabel("Months")
    plt.legend()
    plt.show()
main()
