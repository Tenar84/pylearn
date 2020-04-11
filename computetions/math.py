"""
Улитка ползет по вертикальному шесту высотой h метров, поднимаясь за день на a метров, а за ночь спускаясь на b
метров. На какой день улитка доползет до вершины шеста?
Программа получает на вход натуральные числа h, a, b
Программа должна вывести одно натуральное число. Гарантируется, что a>b
"""

from math import ceil

def pole_snail(pole_height, up_during_day, down_during_night):
    if down_during_night > up_during_day:
        print('snail during the day {} should go faster than go down at night {}', format(up_during_day, down_during_night))
        return
    way_per_day = up_during_day - down_during_night
    count_days = pole_height / way_per_day
    print('the way was lasting for long {} days'.format(ceil(count_days)))
pole_snail(740, 3, 2.5)

