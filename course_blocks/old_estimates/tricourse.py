import pandas as pd
import numpy as np
from random import randint
from sklearn.utils.extmath import cartesian


def get_data():
    df = pd.read_csv("course_blocks/old_estimates/Most Common Courses Analysis.xlsx")

    col_list = list(df.columns)
    subject_index = col_list.index('MainSubject')
    course_num_index = col_list.index('MainCourse#')

    df['Main Course'] = pd.Series([row[subject_index] + ' ' + str(row[course_num_index]) for row in df.values])
    return df


def get_three_random_courses(courses):
    ci = np.random.permutation(len(courses))
    return [courses[i] for i in ci[:3]]


def array_to_real(array):
    return array[0] if len(array) > 0 else 0


def get_estimated_number_in_courses(network, courses, semester='Fall 2016'):
    n = network[network['Semester'] == semester]

    def n_in_course(course):
        array_result = n[n['Main Course'] == course]['Head Count'].values
        return array_to_real(array_result)
    n_in_courses = [n_in_course(course) for course in courses]

    def n_in_both(i):
        course1_df = n[n['Main Course'] == courses[i]]
        array_result = course1_df[courses[(i+1) % len(courses)]].values
        return array_to_real(array_result)
    n_in_boths = [n_in_both(i) for i in range(len(courses))]

    if len(courses) == 3:
        sums = [n_in_boths[i] * n_in_boths[(i-1)%len(n_in_boths)] / n_in_courses[i] for i in range(len(courses))]
    elif len(courses) == 4:
        sums = [n_in_boths[i] * n_in_boths[(i - 1) % len(n_in_boths)] * n_in_boths[(i - 2) % len(n_in_boths)] / n_in_courses[i]**2 for i in range(len(courses))]
    res = np.sum(sums) / len(courses)

    return res if not np.isnan(res) else 0


def all_distinct_groups(element_list, group_size=1):
    aux_list = list(element_list)
    for course in element_list:
        aux_list.remove(course)
        if group_size == 1:
            yield [course]
        else:
            for courses in all_distinct_groups(aux_list, group_size-1):
                yield [course] + courses


def largest_estimated_blocks(data, semester, block_size, n_save):
    best = []

    courses = list(np.unique(data['Main Course']))
    courses.remove('BIOL 1121')
    for test_courses in all_distinct_groups(list(courses), block_size):
        num = get_estimated_number_in_courses(data, test_courses, semester=semester)

        if len(best) < n_save or num > best[0][0]:
            best.append((num, test_courses))
            best.sort()
            best = best[-n_save:]

    return list(reversed(best))


def main():
    data = get_data()

    semesters = ['Fall 2016', 'Fall 2015', 'Fall 2014']
    temp = {}
    for sem in semesters:
        blocks = largest_estimated_blocks(data, sem, 4, 50)

        for (est, block) in blocks:
            block_name = '&'.join(block)
            if block_name not in temp:
                temp[block_name] = {}
            temp[block_name][sem] = est

    avg_blocks = []
    for block in temp:
        sum = 0
        for sem in temp[block]:
            sum += temp[block][sem]

        avg = sum / len(semesters)
        avg_blocks.append((avg, block))

    res = list(reversed(sorted(avg_blocks)))
    [print((round(a[0],1), a[1])) for a in res]


if __name__ == '__main__':
    main()