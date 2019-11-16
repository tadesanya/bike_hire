import pandas
import numpy as np

# These assume the report start and end date are 20150301T00:00:00 and 20150331T23:59:59 respectively
REPORT_START_DATE = pandas.to_datetime('20150301T00:00:00', format='%Y%m%dT%H:%M:%S')
REPORT_END_DATE = pandas.to_datetime('20150331T23:59:59', format='%Y%m%dT%H:%M:%S')

COLUMN_NAMES = {
    'stationId': 'Station ID',
    'bikeId': 'Bike ID',
    'arrivalDatetime': 'Arrival Datetime',
    'departureDatetime': 'Departure Datetime',
}


def time_formatter(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))


def calculate_mean_journey(grouped_data):
    all_mean_journey_durations = []
    date_parser = lambda x: pandas.to_datetime(x, format='%Y%m%dT%H:%M:%S')

    for name_of_the_group, group in grouped_data:
        group = group.reset_index(drop=True)
        bike_journey_duration = []
        group_length = len(group)
        first_row = None
        last_row = None

        for row_index, row in group.iterrows():
            if row_index == 0:
                first_row = row
                continue
            else:
                if row_index == group_length - 1:
                    last_row = row

                duration = date_parser(row[COLUMN_NAMES['arrivalDatetime']]) - date_parser(group.iloc[row_index - 1, 3])
                bike_journey_duration.append(duration.total_seconds())

        # Get the duration of the bike's current journey that is still ongoing
        # reporting period till it arrived at the first station.
        if date_parser(first_row[COLUMN_NAMES['arrivalDatetime']]) != REPORT_START_DATE:
            first_journey_duration = date_parser(row[COLUMN_NAMES['arrivalDatetime']]) - REPORT_START_DATE
            bike_journey_duration.insert(0, first_journey_duration.total_seconds())

        # Get duration of bike journey by getting the time difference between departure time from
        # as at the end of the reporting period.
        if date_parser(last_row[COLUMN_NAMES['departureDatetime']]) != REPORT_END_DATE:
            last_journey_duration = REPORT_END_DATE - date_parser(row[COLUMN_NAMES['departureDatetime']])
            bike_journey_duration.append(last_journey_duration.total_seconds())

        # Calculate the mean journey of bike for the reporting period
        mean_bike_journey = np.mean(bike_journey_duration)
        print('Bike {} journey during reporting period (in seconds) {}'.format(name_of_the_group, bike_journey_duration))
        print('Mean journey for Bike {}: {}\n'.format(name_of_the_group, time_formatter(mean_bike_journey)))
        all_mean_journey_durations.append(mean_bike_journey)

    overall_mean_journey = np.mean(all_mean_journey_durations)
    print('\nTotal Journeys:', all_mean_journey_durations)
    return time_formatter(overall_mean_journey)


def main():
    data = pandas.read_csv('data.csv',
                           delimiter=',',
                           names=[COLUMN_NAMES['stationId'],
                                  COLUMN_NAMES['bikeId'],
                                  COLUMN_NAMES['arrivalDatetime'],
                                  COLUMN_NAMES['departureDatetime']])

    # Fill empty values for Arrival Datetime and Departure Datetime with REPORT_START_DATE and REPORT_END_DATE
    # respectively. Without this when sorting, rows with NaN are erroneously taken to the bottom of the sorting order.
    data[[COLUMN_NAMES['arrivalDatetime']]] = data[[COLUMN_NAMES['arrivalDatetime']]].fillna(REPORT_START_DATE.strftime('%Y%m%dT%H:%M:%S'))
    data[[COLUMN_NAMES['departureDatetime']]] = data[[COLUMN_NAMES['departureDatetime']]].fillna(REPORT_END_DATE.strftime('%Y%m%dT%H:%M:%S'))

    sorted_data = data.sort_values(COLUMN_NAMES['arrivalDatetime'])
    grouped_data = sorted_data.groupby(COLUMN_NAMES['bikeId'])

    mean_journey = calculate_mean_journey(grouped_data)
    print('\nOverall mean journey of all bikes: {}'.format(mean_journey))


if __name__ == '__main__':
    main()
