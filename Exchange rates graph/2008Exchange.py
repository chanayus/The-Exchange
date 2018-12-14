""" Exchange """
import matplotlib.pyplot as plt
def main():
    """ function """
    x = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN",\
     "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    y = [31.3, 31.075, 31.47, 31.655, 32.489, 33.43, 33.52, 34.225, 33.855, 35.05, 35.47, 34.785]#input rate exchange
    avg = sum(y)/12
    plt.plot(x, y, color="purple", marker="o", label="Exchange Rates")
    plt.axhline(avg, color="orange", linestyle="--", label="Average")
    plt.title("Exchange Rates 2008", color="blue", fontsize=18)
    plt.ylabel("Rates")
    plt.xlabel("Months")
    plt.legend()
    plt.show()
main()
