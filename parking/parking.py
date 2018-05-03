import csv
import numpy as np
from matplotlib import pyplot as plt
from scipy import misc
from math import log


def main():
    buildings = []

    filename = 'input_data/building_location_enrollment.csv'
    with open(filename,'r') as csvfile:
        reader = csv.reader(csvfile)
        reader.__next__()  # Skip header
        for row in reader:
            [lat,long,enrollment] = row[1:]
            buildings.append([float(lat),float(long),float(enrollment)])

    lat_start = 35.2
    lat_stop = 35.215
    lat_step = .0005
    lat_steps = int((lat_stop - lat_start) // lat_step)

    long_start = -97.453
    long_stop = -97.435
    long_step = 0.0005
    long_steps = int((long_stop - long_start) // long_step)

    scale = 100
    log_offset = 500

    lats = []
    longs = []
    dists = []

    results = []
    for lat_i in range(lat_steps + 1):
        row_result = []
        lat = lat_start + lat_step*lat_i
        for long_i in range(long_steps + 1):
            long = long_start + long_step*long_i

            lats.append(lat)
            longs.append(long)

            weighted_distance = 0
            for building in buildings:
                distance = (lat-building[0])**2 + (long-building[1])**2
                weighted_distance += scale * distance * building[2]

            dists.append(weighted_distance)
            row_result.append(weighted_distance)
        results.append(row_result)

    img = misc.imread('/home/nick/Pictures/campus.png')

    max_dist = min(dists)
    log_dists = [-log(i-max_dist+log_offset) for i in dists]

    plt.imshow(img, extent=[long_start, long_stop, lat_start, lat_stop])
    plt.scatter(longs, lats, c=log_dists, alpha=0.8)
    plt.colorbar()
    plt.show()


if __name__ == '__main__':
    main()