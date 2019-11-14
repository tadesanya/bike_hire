from datetime import datetime
import pandas

REPORT_START_DATE = datetime(2015, 3, 1, 00, 00, 00)
REPORT_END_DATE = datetime(2015, 3, 31, 23, 59, 59)


def main():
    data = pandas.read_csv('data.csv',
                           delimiter=',',
                           names=['Station ID', 'Bike ID', 'Arrival Datetime', 'Departure Datetime'])


if __name__=='__main__':
    main()
