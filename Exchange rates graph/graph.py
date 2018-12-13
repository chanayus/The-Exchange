""" Exchange """
import matplotlib.pyplot as plt
def main():
    """ function """
    x = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN",\
     "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    y = [42.5, 43.1, 45.025, 45.65, 45.375, 45.3, 45.72, 44.45, 44.71, 43.935, 44.235]#input rate exchange
    avg = sum(y)/12
    plt.plot(x, y, color="blue", marker="o", label="Exchange Rates")
    plt.axhline(avg, linestyle="--",color ="orange", label="Average")
    plt.title("Exchange Rates", color="black", fontsize=26)
    plt.ylabel("Rate", color="red", fontsize=18)
    plt.xlabel("Month", color="green", fontsize=18)
    plt.legend()
    plt.show()
main()
