#!/anaconda3/bin/python3

import math
import argparse

# For now only MERGE slides ch 2 -- Im defining q q and ar WITHIN the function
# But for MERGE_SORT p,q and r are defined as parameters!

def merge(ar):
    '''
    Takes as input an array. When splitting the array into half, the left
    part will be longer by one if not divisible by 2. These subarrays will be
    called left and right. Each of the subarrays is sorted. Merge then merges
    These sorted arrays into one sorted array. The sorted array is returned.
    '''
    print(ar)
    p=0 # for now defining always as 0
    if len(ar)%2==0:
        q=len(ar)//2-1
    else:
        q=len(ar)//2 # BS: indexing starts at 0 math.ceil(ar/2) # Gausche aufrundungsfunktion
    r=len(ar)
    print('p', p, 'q', q, 'r', r)

#############################################################################################################################
# Adding parser
#############################################################################################################################
parser = argparse.ArgumentParser(description='MERGE algorithm from ch 2')
parser.add_argument('-a', '--array', type=str, metavar='', required=True, help='One List of integers composed of 2 sorted halves. Sorting must start from smallest to largest for each of the halves.')
args = parser.parse_args()
args_list_st=args.array.split(',') # list of strings
args_list_int=[]
for i in args_list_st:
    args_list_int.append(int(i))
    
if __name__ == "__main__":
    merge(args_list_int)

