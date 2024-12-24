import pandas as pd
import matplotlib.pyplot as plt

def analyze_csv(filename):
    try:

        data = pd.read_csv

        print("dentest review")
        print(data.head(), "\n")

        print("Destriptive Statistics")
        print(data.describe())

        data.hist(figsize = (10, 8), bins = 10, edgecolor = "black")
        plt.suptitle("Box Plts")
        plt.show()

    except FileNotFoundError:
        print("File does not exist")
    except pd.errors.EmptyDataError:
        print("File is empty")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    filename = input("Enter name of the csv file: ")
    analyze_csv(filename)