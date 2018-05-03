import pandas as pd
import numpy as np
from collections import Counter
import glob

# Those are semesters in Banner.
# 201630 – Summer 2017
# 201710 – Fall 2017
# 201720 – Spring 2018
#
# 201711 and  201721 are special terms for CCE advanced programs.You can ignore them in this project.

SEP = '\\'
def get_data(dir='.' + SEP + 'course_blocks' + SEP + 'data'):
    rollss = []
    for roll_file in glob.iglob(dir + SEP + 'course_rolls?.csv'):
        rollss.append(pd.read_csv(roll_file))
    rolls = pd.concat(rollss, axis=0)

    sus = []
    for su_file in glob.iglob(dir + SEP + 'student_details?.csv'):
        sus.append(pd.read_csv(su_file))
    student_details = pd.concat(sus, axis=0)

    return rolls, student_details


def largest_courses(rolls, n=None, min_size=None):
    count = Counter(rolls.COURSE_IDENTIFICATION)

    size_sorted = sorted([(count[name], name) for name in count], reverse=True)
    if n is not None:
        size_sorted = size_sorted[:n]
    if min_size is not None:
        split = 0
        size = size_sorted[0][0]
        while size >= min_size:
            split += 1
            size = size_sorted[split][0]
        size_sorted = size_sorted[:split]
    return size_sorted


def course_rolls(rolls, course_s):
    if type(course_s) == type([]):
        return [course_rolls(rolls, c) for c in course_s]
    else:
        return rolls[rolls.COURSE_IDENTIFICATION == course_s].PERSON_UID_


def main():
    rolls, student_details = get_data()

    sem = 201710 # Fall 2017
    rolls = rolls[rolls.ACADEMIC_PERIOD == sem]
    student_details = student_details[student_details.ACADEMIC_PERIOD == sem]

    # Get largest courses (instead of checking all)
    n_courses = 100
    large_courses = [name for (size, name) in largest_courses(rolls, min_size=100)]
    large_courses.remove('BIOL1121') # Remove lab because it is highly correlated with its class
    large_course_rolls = course_rolls(rolls, large_courses)

    # Find largest blocks
    min_size = 50
    n_classes_per_block = 3
    largest = []
    for classes in permutations(len(large_courses), n_classes_per_block):
        courses = [large_courses[i] for i in classes]

        students_in_all_classes = large_course_rolls[classes[0]]
        students_in_one_class  = large_course_rolls[classes[0]]
        for i in classes[1:]:
            if students_in_all_classes.size < min_size:
                break
            students_in_all_classes = np.intersect1d(students_in_all_classes, large_course_rolls[i])
            students_in_one_class = np.union1d(students_in_all_classes, large_course_rolls[i])

        if students_in_all_classes.size >= min_size:
            correlation = students_in_all_classes.size / students_in_one_class.size
            largest.append((students_in_all_classes.size, courses, students_in_all_classes, correlation))

    # Print results
    for size, courses, students_in_all_classes, correlation in sorted(largest, reverse=True):
        all_student_details = student_details[student_details.PERSON_UID_.isin(students_in_all_classes)]

        classes, class_counts = np.unique(all_student_details['IRR_DEMO_CLASS'], return_counts=True)
        max_ind = np.argmax(class_counts)
        class_mode = classes[max_ind]
        class_perc = round(class_counts[max_ind] / np.size(all_student_details['IRR_DEMO_CLASS']), 2)

        majors, major_counts = np.unique(all_student_details['MAJOR_DESC'], return_counts=True)
        max_ind = np.argmax(major_counts)
        major_mode = majors[max_ind]
        major_perc = round(major_counts[max_ind] / np.size(all_student_details['MAJOR_DESC']), 2)

        print(round(correlation,2), size, courses, '\t', class_perc, class_mode, '\t', major_perc, major_mode)


def permutations(n, size, start=0):
    if size > n - start:
        return None

    total = []

    for i in range(start, n):
        if size > 1:
            other = permutations(n, size-1, start=i+1)
            if other is not None:
                new = np.array([i] * len(other)).reshape(-1,1)
                res = np.hstack([new, other])
                total.append(res)
        elif size == 1:
            total.append([i])

    return np.unique(np.vstack(total), axis=0)


if __name__ == '__main__':
    main()
