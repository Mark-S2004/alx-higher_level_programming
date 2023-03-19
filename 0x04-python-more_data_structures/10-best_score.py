#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_student = list(a_dictionary)[0]
    for student in list(a_dictionary)[1:]:
        if a_dictionary[student] > a_dictionary[max_student]:
            max_student = student
    return max_student
