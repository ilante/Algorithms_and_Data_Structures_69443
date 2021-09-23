#!/usr/bin/python3

import argparse

def insertion_sort(arr):
    '''
    Takes any array as parameter and sorts it **in place**: 
    It rearranges the numbers within the array. Returns the
    sorted array.
    '''
    for j in range(1, len(arr)):
        curr_key = arr[j]
        # inserting arr[j] into sorted sequence arr[1..j-1]
        i = j - 1
        while i > -1 and arr[i] > curr_key:
            arr[i+1] = arr[i]
            i = i - 1
            print('the new i')
            print(i)
        arr[i+1] = curr_key
        print(arr)
    return(arr)

# Parser:

parser = argparse.ArgumentParser(description='Insertion Sort Algorithm as described in ch 1 page 18')
parser.add_argument('-a', '--array', '--nargs-int-type', nargs='+', type=int, metavar='', required=True, help='Please insert an array as a list of integers for sorting.')
args = parser.parse_args()

if __name__ == '__main__':
    my_arr = args.array
    insertion_sort(my_arr)
