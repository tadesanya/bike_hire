Solution to Bike Hire Excercise

Please see the file "Bike Hire Exercise.pdf" for a proper description of
the challenge.

To run the solution, `cd` into the project directory and run the code:
`python bike_journey/journey_avg.py`

To Run tests:
`python -m unittest test_journey_avg`


Assumptions:
1. Each “data.csv” file represents a monthly reporting period. i.e May of 2015.
2. Reporting period for this program will be from 20150301T00:00:00 to 20150331T23:59:59. These represent REPORT_START_DATE and REPORT_END_DATE respectively.
3. Empty values for “Arrival Datetime” and “Departure Datetime” are substituted with the values of REPORT_START_DATE and REPORT_END_DATE respectively. This is done to account for the journey time of bikes that are still in transit at the beginning and end of each reporting period. (Also without this when sorting, rows with empty values are erroneously taken to the bottom of the sorting order.)
4. Output is displayed on screen.
