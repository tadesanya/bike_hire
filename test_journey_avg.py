import unittest
import pandas as pd

from bike_journey.journey_avg import time_formatter, calculate_mean_journey


class TestTimeFormatter(unittest.TestCase):
    def test_gives_correct_result(self):
        """
        Test time_formatter gives the right result
        """

        seconds = 12610
        result = time_formatter(seconds)
        self.assertEqual(result, '03:30:10')

    def test_result_datatype(self):
        """
        Test time_formatter returns a str
        """

        seconds = 483614
        result = time_formatter(seconds)
        self.assertIsInstance(result, str)


class TestCalculateMeanJourney(unittest.TestCase):
    def setUp(self):
        report_start_date = pd.to_datetime('20150301T00:00:00', format='%Y%m%dT%H:%M:%S')
        report_end_date = pd.to_datetime('20150331T23:59:59', format='%Y%m%dT%H:%M:%S')

        column_names = {
            'stationId': 'Station ID',
            'bikeId': 'Bike ID',
            'arrivalDatetime': 'Arrival Datetime',
            'departureDatetime': 'Departure Datetime',
        }
        
        raw_data = {
            'Station ID': [4, 22, 57, 2, 157, 32, 13, 157, 57],
            'Bike ID': [34, 102, 222, 34, 222, 102, 34, 222, 102],
            'Arrival Datetime': [None, '20150304T13:04:00', '20150305T07:00:00', '20150301T08:45:18', '20150306T14:20:14',
                                 '20150304T20:52:49', '20150311T06:10:07', '20150305T13:00:00', '20150305T12:00:31'],
            'Departure Datetime': ['20150301T05:15:08', '20150304T13:25:32', '20150305T12:30:59', '20150311T01:00:33',
                                    None, '20150305T08:15:00', '20150313T15:15:15', '20150306T11:30:19', None]
        }
        
        self.data = pd.DataFrame(raw_data)
        self.data[[column_names['arrivalDatetime']]] = self.data[[column_names['arrivalDatetime']]].fillna(
            report_start_date.strftime('%Y%m%dT%H:%M:%S'))
        self.data[[column_names['departureDatetime']]] = self.data[[column_names['departureDatetime']]].fillna(
            report_end_date.strftime('%Y%m%dT%H:%M:%S'))

        self.sorted_data = self.data.sort_values(column_names['arrivalDatetime'])
        self.grouped_data = self.sorted_data.groupby(column_names['bikeId'])

    def test_calculate_mean_journey_returns_right_result(self):
        """
        Test calculate_mean_journey returns the right result for its calculatons
        """
        data = self.grouped_data
        result = calculate_mean_journey(data)
        self.assertEqual(result, '78:28:33')

    def test_calculate_mean_journey_returns_right_datatype(self):
        """
        Test calculate_mean_journey returns the right result for its calculatons
        """
        data = self.grouped_data
        result = calculate_mean_journey(data)
        self.assertIsInstance(result, str)


if __name__ == '__main__':
    unittest.main()
