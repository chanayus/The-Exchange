""" Exchange """
import matplotlib.pyplot as plt
def main():
    """ function """
    x = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN",\
     "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    y = [34.75, 34.025, 32.325, 32.85, 32.9, 31.7, 29.95, 32.535, 31.9, 31.675, 30.7, 30.05]#input rate exchange
    avg = sum(y)/12
    plt.plot(x, y, color="purple", marker="o", label="Exchange Rate")
    plt.axhline(avg, linestyle="--", label="Average")
    plt.title("Exchange Rate 2007", color="blue", fontsize=18)
    plt.ylabel("Rate")
    plt.xlabel("Month")
    plt.legend()
    plt.show()
main()
