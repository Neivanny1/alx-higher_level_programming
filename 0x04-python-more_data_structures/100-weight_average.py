#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    else:
        T_score = 0
        T_weight = 0
        for score, weight in my_list:
            T_score += score * weight
            T_weight += weight
        avg_weight = T_score / T_weight
        return avg_weight
