import csv
import json, requests


def main():
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    my_key = 'AIzaSyBR3G6ut8ft8zSaAmt69ss9dMxYpuaNFgk'
    with open('/home/nick/Downloads/building_enrollment.csv','r') as csvfile:
        reader = csv.reader(csvfile)

        reader.__next__() # Skip header

        with open('/home/nick/Downloads/building_enrollment_coord.csv','w') as outfile:
            writer = csv.writer(outfile)

            for row in reader:
                building = row[0]

                params = dict(
                    address=building + 'University of Oklahoma',
                    key=my_key
                )

                resp = requests.get(url=url, params=params)
                data = json.loads(resp.text)
                location = data['results'][0]['geometry']['location']
                lat = location['lat']
                lng = location['lng']

                writer.writerow(row + [lat, lng])


def m2():
    with open('/home/nick/Downloads/building_enrollment_coord.csv','r') as csvfile:
        reader = csv.reader(csvfile)

        reader.__next__() # Skip header

        with open('/home/nick/Downloads/builds.csv','w') as outfile:
            writer = csv.writer(outfile)

            for row in reader:
                if len(row) == 4 or len(row[4]) == 0:
                    writer.writerow(row)
                else:
                    loc = row[4].split(", ")
                    writer.writerow(row[:2] + loc)


def m3():
    code_to_coord = {}
    with open('/home/nick/Downloads/building_coordinates.csv','r') as csvfile:
        reader = csv.reader(csvfile)
        reader.__next__()  # Skip header
        for row in reader:
            code = row[0]
            loc = row[2:]
            code_to_coord[code] = loc

    with open('/home/nick/Downloads/sections.csv','r') as csvfile:
        reader = csv.reader(csvfile)

        header = reader.__next__() # Skip header

        i = 0
        with open('/home/nick/Downloads/section_coord.csv','w') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(header + ['Building_Latitude','Building_Longitude'])

            for row in reader:
                i += 1
                if i % 500:
                    print(i)
                    
                code = row[0]
                writer.writerow(row + code_to_coord[code])


if __name__ == '__main__':
    m3()