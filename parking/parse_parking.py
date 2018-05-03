import csv
import numpy as np
from datetime import datetime
import pandas as pd


'''

x = enrollment at that time in all buildings, maybe weather?, maybe day into semester, day of week
y = occupancy for that lot
'''

lots = ['Boyd House', 'Duck Pond', 'Jenkins', 'Monett Lot - North']

CAP = {
    'Boyd House': 194,
    'Duck Pond': 840,
    'Jenkins': 177,
    'Monett Lot - North': 238
}

DAYS = 'MTWRFSU'
DAYS_LONG = {
    'Mon': 0,
    'Tue': 1,
    'Wed': 2,
    'Thu': 3,
    'Fri': 4,
    'Sat': 5,
    'Sun': 6
}


def get_parking_data(filename):
    results = {}

    with open(filename,'r') as csvfile:
        reader = csv.reader(csvfile)
        # Skip pull information
        for _ in range(13):
            next(reader)
        header = next(reader)

        lot = None

        for i, row in enumerate(reader):
            if len(row[0]) > 1:
                lot = row[0]
            elif 'Page' in row[14]:
                pass
            elif lot is not None and len(''.join(row)) > 0:
                date = datetime.strptime(row[7] + ' ' + row[9], '%m/%d/%Y %I:%M:%S %p')
                date_string = date.isoformat()
                day = row[12]
                occ = int(row[15])
                occ_type = row[2]

                if date_string not in results:
                    results[date_string] = {}
                if lot in results[date_string]:
                    print("Duplicate times found")
                    print(row)
                    print(date_string, results[date_string])

                results[date_string][lot] = [day, occ_type, CAP[lot], occ]

    return results


def building_parking_data(parking_dir, parking_filenames):
    parking_results = {}

    for parking_filename in parking_filenames:
        file_results = get_parking_data(parking_dir + parking_filename)
        parking_results.update(file_results)

    results = []
    for date_string in parking_results:
        for lot in parking_results[date_string]:
            row = [date_string, lot] + parking_results[date_string][lot]
            results.append(row)

    return pd.DataFrame(results, columns=['datetime','lot','weekday','occ_type', 'capacity','occ'])


def create_parking_dataframe():
    parking_dir = 'input_data/'
    parking_filenames = ['T2OccupancyCount9_22_17.csv', 'T2OccupancyCount3_9_18.csv']
    parking = building_parking_data(parking_dir, parking_filenames)

    parking.to_csv('cleaned_data/parking.pd')


if __name__ == '__main__':
    create_parking_dataframe()