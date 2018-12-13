""" Exchange """
import matplotlib.pyplot as plt
def main():
    """ function """
    x = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN",\
     "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    y = []#input rate exchange
    avg = sum(y)/12
    plt.plot(x, y, color="black", marker="o", label="exchange rate")
    plt.axhline(avg, linestyle="--", label="average")
    plt.title("Exchange Rate", color="orange", fontsize=18)
    plt.ylabel("Rate")
    plt.xlabel("Month")
    plt.legend("")
    plt.show()
main()
