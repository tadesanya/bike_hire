import csv


def main():
    with open('data.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            pass


if __name__=='__main__':
    main()
