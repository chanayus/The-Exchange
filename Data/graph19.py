""" Exchange """
import matplotlib.pyplot as plt
def main():
    """ function """
    x = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN",\
     "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]#input rate exchange
    avg = sum(y)/12
    plt.plot(x, y, color="black", marker="o", label="exchange rate")
    plt.axhline(avg, linestyle="--", label="average")
    plt.title("Exchange Rate", color="orange", fontsize=18)
    plt.ylabel("Rate")
    plt.xlabel("Month")
    plt.legend("")
    plt.show()
main()
