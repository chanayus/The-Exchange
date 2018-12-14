"""Exchange Rate Years"""
import csv
import matplotlib.pyplot as plt
def main():
    """function"""
    text = input("Choose exchange rates years(1997-2016)\n")
    url = open(r'Exchange1997-2016.csv')
    reader = csv.reader(url)
    for i in reader:
        if i[0] == text:
            graph([float(i[j]) for j in range(1, 13)])

def graph(y):
    """ plot graph input years """
    x = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN",\
     "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    avg = sum(y)/12
    plt.plot(x, y, color="black", marker="o", label="exchange rate")
    plt.axhline(avg, color="red", linestyle="--", label="average")
    plt.title("Exchange Rate", color="orange", fontsize=18)
    plt.ylabel("Rate")
    plt.xlabel("Month")
    plt.legend()
    plt.show()
main()
