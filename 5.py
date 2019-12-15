import datetime
import numpy


def working_days(y1, m1, d1, y2, m2, d2):
    start_date = datetime.date(y1, m1, d1)
    end_date = datetime.date(y2, m2, d2)
    print('Working days during thi period:', numpy.busday_count(start_date, end_date))


first_string, second_string = '2019_7_2', '2019_7_11'
first_string_spl = first_string.split('_')
second_string_spl = second_string.split('_')
working_days(int(first_string_spl[0]), int(first_string_spl[1]), int(first_string_spl[2]),
             int(second_string_spl[0]), int(second_string_spl[1]), int(second_string_spl[2]) + 1)
