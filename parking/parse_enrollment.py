import csv
import numpy as np
import pandas as pd


DAYS = 'MTWRFSU'


def enrollment_parse():
    filename = 'input_data/enrollment_building.csv'
    with open(filename,'r') as csvfile:
        reader = csv.reader(csvfile)
        # Skip pull information
        header = next(reader)

        building_set = set()

        result = {}
        for row in reader:
            [term, building, crn, meeting_days, start, end, enrollment] = row

            building_set.add(building)

            start = int(start)
            end = int(end)
            enrollment = int(enrollment)

            if term not in result:
                result[term] = {}
                for day in DAYS:
                    result[term][day] = {}
                    for hour in range(24):
                        result[term][day][hour] = {}

            for meeting_day in meeting_days:
                day = result[term][meeting_day]
                for meeting_hour in range(start // 100, (end // 100) + 1):
                    if building not in day[meeting_hour]:
                        day[meeting_hour][building] = 0
                    day[meeting_hour][building] += enrollment

        building_list = sorted(list(building_set))
        print(list(enumerate(building_list)))

        data = []
        for term in result:
            for day_i, day in enumerate(DAYS):
                for hour in range(24):
                    for building_i, building_name in enumerate(building_list):
                        this_hour_data = result[term][day][hour]
                        enrollment = this_hour_data.get(building_name,0)
                        data.append([term, day_i,day,hour, building_i, building_name, enrollment])


        df = pd.DataFrame(data, columns=['term', 'day_index','day','hour','building_index', 'building','enrollment'])
        df.to_csv('cleaned_data/enrollment.pd')


if __name__ == '__main__':
    enrollment_parse()