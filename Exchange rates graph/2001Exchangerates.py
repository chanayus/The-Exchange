""" Exchange """
import matplotlib.pyplot as plt
def main():
    """ function """
    x = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN",\
     "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    y = [42.5, 43.1, 45.025, 45.65, 45.375, 45.3, 45.72, 44.05, 44.45, 44.71, 43.935, 44.235]#input rate exchange
    avg = sum(y)/12
    plt.plot(x, y, color="blue", marker="o", label="Exchange Rates")
    plt.axhline(avg, color="red", linestyle="--", label="Average")
    plt.title("Exchange Rates 2001", color="black", fontsize=18)
    plt.ylabel("Rates")
    plt.xlabel("Months")
    plt.legend()
    plt.show()
main()
