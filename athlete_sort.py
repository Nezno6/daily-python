#!/bin/python3

import math
import os
import random
import re
import sys

def print_list(sorted_athletes_data: list):
    print("\n".join(sorted_athletes_data))

def list_to_str(sorted_athletes_data: list):
    return [" ".join(map(str, athlete_data)) for athlete_data in sorted_athletes_data]

def to_int_tuple(athlete_data: str):
    return tuple(map(int, athlete_data.split()))

def athlete_sort(input_data: list):
    sort_by = int(input_data[-1])
    athletes_data = [to_int_tuple(athlete_data) for athlete_data in input_data[1:-1]]
    sorted_athletes_data = sorted(athletes_data, key=lambda x: x[sort_by])
    return list_to_str(sorted_athletes_data)

if __name__ == '__main__':
    n,m = map(int, input().split())

    arr = ["n m"]

    for _ in range(n):
        arr.append(input())

    arr.append(input())
    print_list(athlete_sort(arr))

