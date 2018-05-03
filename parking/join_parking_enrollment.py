from datetime import datetime
import numpy as np
import pandas as pd

building_index = [(0, '655 Research Parkway'), (1, '825 Research Parkway'), (2, '865 Research Parkway'), (3, 'Academic Center'), (4, 'Adams Center Dorm'), (5, 'Adams Hall'), (6, 'Archeological Survey Building'), (7, 'Armory'), (8, 'Bizzell Library'), (9, 'Buchanan Hall'), (10, 'Burton Hall'), (11, 'Carnegie Building'), (12, 'Carpenter Hall'), (13, 'Carson Engr Ctr'), (14, 'Cate Center One'), (15, 'Cate Center Two'), (16, 'Cate Dorm #4'), (17, 'Catlett Music Ctr'), (18, 'Ceramics Studio'), (19, 'Chem Bldg Annex'), (20, 'Chemistry Building'), (21, 'College of Allied Health'), (22, 'Collings Hall'), (23, 'Collums Building'), (24, 'Comp Wind Tunnel'), (25, 'Copeland Hall'), (26, 'Cross Center A'), (27, 'Dale Hall'), (28, 'Dale Hall Tower'), (29, 'Devon Energy Hall'), (30, 'Dunham Residential College'), (31, 'Engineering Lab'), (32, 'Evans Hall'), (33, 'Farzaneh Hall'), (34, 'Fears Structural Engr Lab'), (35, 'Felgar Hall'), (36, 'Fine Arts Center'), (37, 'Five Partners Place'), (38, 'Fred Jones Art Ctr'), (39, 'Fred Jones Art Museum'), (40, 'Fredrick Douglass Center'), (41, 'G L Cross Hall'), (42, 'Gaylord Hall'), (43, 'Gould Hall'), (44, 'HSC Conference Center'), (45, 'Headington Hall'), (46, 'Headington Residential College'), (47, 'Honors #5'), (48, 'Huston Huffman Center'), (49, 'Intramural Soccer Field'), (50, 'Kaufman Hall'), (51, 'Law Center'), (52, 'Lawton Eisenhower High School'), (53, 'Lawton MacArthur High School'), (54, 'Lissa and Cy Wagner Hall'), (55, 'Lloyd Noble Center'), (56, 'Main Building - Texoma'), (57, 'Michael F. Price Hall'), (58, 'Model Shop'), (59, 'Monnet Hall'), (60, 'Moore Public Schools'), (61, 'N.C. Bldg 101'), (62, 'N.C. Bldg 104'), (63, 'N.C. Bldg 210'), (64, 'National Weather Center'), (65, 'Nielsen Hall'), (66, 'Noble Microscopy'), (67, 'Norman High School'), (68, 'Norman North High School'), (69, 'North Campus Aviation Complex'), (70, 'OU HSC Bird Library'), (71, 'Oklahoma City Design Center'), (72, 'Oklahoma Memorial Stadium'), (73, 'Oklahoma Memorial Union'), (74, 'Old Faculty Club'), (75, 'Parkways'), (76, 'Physical Science Ctr'), (77, 'Putnam City School Admin Off'), (78, 'Radar Innovations Lab'), (79, 'Rawls Engr Practice Facility'), (80, 'Reynolds Performing Arts Ctr'), (81, 'Richards Hall'), (82, 'Richards Hall Add'), (83, 'Robertson Hall'), (84, 'S.C. Building 134'), (85, 'SJ Sarkeys Complex'), (86, 'Sam Noble OK Museum Nat Hist'), (87, 'Sarkeys Energy Ctr'), (88, 'Science Hall'), (89, 'Southmoore Hish School'), (90, 'Stephenson Life Sci Research'), (91, 'Stephenson Res and Tech. Cntr'), (92, 'Sutton Hall'), (93, 'Three Partners Place'), (94, 'Zarrow Hall')]
CAP = {
    'Boyd House': 194,
    'Duck Pond': 840,
    'Jenkins': 177,
    'Monett Lot - North': 238
}
_headers = []
_headers.extend([building_name + "BEFORE" for (i, building_name) in building_index])
_headers.extend([building_name + "NOW" for (i, building_name) in building_index])
_headers.extend([building_name + "AFTER" for (i, building_name) in building_index])

def no_school(date):
    if date.year == 2017:
        if date.month == 9 and date.day == 4 and date.year == 2017:
            return 1  # Labor Day
        if date.month == 11 and 22 <= date.day <= 26:
            return 1
    if date.year == 2018:
        if date.month == 1:
            if date.day < 16:
                return 1
        if date.month == 2:
            if 21 <= date.day <= 22:
                return 1  # Snow days
        if date.month == 3:
            if 17 <= date.day <= 25:
                return 1
    return 0


def home_gameday(date):
    if date.year == 2017:
        if date.month == 9:
            if date.day == 2:
                return 1
            if date.day == 16:
                return 1
        if date.month == 10:
            if date.day == 7:
                return 1

    return 0


spring_2018_start = datetime(2018, 1, 16)
fall_2017_start = datetime(2017, 8, 21)


def days_into_semester(date):
    if date > spring_2018_start:
        return (date - spring_2018_start).days
    if date > fall_2017_start:
        return (date - fall_2017_start).days
    return 0


def fall(date):
    return date.month >= 8


def spring(date):
    return date.month <= 5


def get_semester(date):
    result = ' '

    if fall(date):
        result = 'Fall'
    elif spring(date):
        result = 'Spring'
    else:
        result = 'Summer'

    return result + ' ' + str(date.year)


def get_building_enrollment(enrollment_data, date):
    term = get_semester(date)
    day_i = date.weekday()
    hour = date.hour

    enrollment = enrollment_data.query('term == @term and day_index == @day_i')
    # enrollment = enrollment_data[enrollment_data['term'] == term][enrollment_data['day_index'] == day_i]
    enrollment_info_before = enrollment[enrollment['hour'] == hour - 1]
    enrollment_info_now = enrollment[enrollment['hour'] == hour]
    enrollment_info_after = enrollment[enrollment['hour'] == hour + 1]

    before = enrollment_info_before['enrollment'].T
    now = enrollment_info_now['enrollment'].T
    after = enrollment_info_after['enrollment'].T

    return before, now, after


def assemble_data(enrollment_data, parking_data):
    a_data = augmented_data(enrollment_data, parking_data)
    merged_df = pd.merge(parking_data, a_data,on='datetime')

    return merged_df


def augmented_data(enrollment_data, parking_data):
    data = []
    for date_string in parking_data['datetime'].unique():
        date = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S')
        date_info = [date_string, date.year, fall(date), spring(date), days_into_semester(date), date.weekday(), date.hour,
                     no_school(date), home_gameday(date)]

        enrollment_info_before, enrollment_info_now, enrollment_info_after = get_building_enrollment(
            enrollment_data, date)

        row = np.hstack(
            [date_info, enrollment_info_before, enrollment_info_now, enrollment_info_after])
        data.append(row)
    return pd.DataFrame(data, columns=['datetime', 'year', 'fall', 'spring', 'days_into_semester', 'weekday_index', 'hour', 'no_school', 'home_gameday'] + _headers)



def get_headers():
    headers = ['lot_name', 'lot_capacity', 'year', 'fall', 'spring', 'days_into_semester', 'weekday_index',
               'hour', 'no_school', 'home_gameday']

    headers.extend([building_name + "BEFORE" for (i, building_name) in building_index])
    headers.extend([building_name + "NOW" for (i, building_name) in building_index])
    headers.extend([building_name + "AFTER" for (i, building_name) in building_index])

    headers.append('occupancy')

    return headers


def main():
    enrollment_file = 'enrollment.pd'
    parking_file = 'parking.pd'
    enrollment_data = pd.read_csv(enrollment_file)
    parking_data = pd.read_csv(parking_file)

    data = assemble_data(enrollment_data, parking_data)

    data.to_csv('cleaned_data/parking_enrollment.pd')


if __name__ == '__main__':
    main()