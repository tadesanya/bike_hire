from datetime import datetime
import pandas

REPORT_START_DATE = datetime(2015, 3, 1, 00, 00, 00)
REPORT_END_DATE = datetime(2015, 3, 31, 23, 59, 59)


def main():
    data = pandas.read_csv('data.csv',
                           delimiter=',',
                           names=['Station ID', 'Bike ID', 'Arrival Datetime', 'Departure Datetime'])

    # Fill empty values for Arrival Datetime and Departure Datetime with REPORT_START_DATE and REPORT_END_DATE
    # respectively.
    data[['Arrival Datetime']] = data[['Arrival Datetime']].fillna(REPORT_START_DATE.strftime('%Y%m%dT%H:%M:%S'))
    data[['Departure Datetime']] = data[['Departure Datetime']].fillna(REPORT_END_DATE.strftime('%Y%m%dT%H:%M:%S'))


if __name__ == '__main__':
    main()
