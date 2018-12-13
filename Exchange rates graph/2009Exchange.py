""" Exchange """
import matplotlib.pyplot as plt
def main():
    """ function """
    x = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN",\
     "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    y = [34.965, 36.175, 35.495, 35.28, 34.31, 34.06, 34.025, 34.02, 33.44, 33.455, 33.24, 33.36]#input rate exchange
    avg = sum(y)/12
    plt.plot(x, y, color="cyan", marker="o", label="Exchange Rate")
    plt.axhline(avg, linestyle="--", label="Average")
    plt.title("Exchange Rate 2009", color="magenta", fontsize=18)
    plt.ylabel("Rate")
    plt.xlabel("Month")
    plt.legend()
    plt.show()
main()
