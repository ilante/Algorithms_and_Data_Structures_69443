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
    r=len(ar)-1
    print('p', p, 'q', q, 'r', r)

    # lets check if n1 and n2 check outA
    n_1 = q-p+1 # describes the lenght of the left subarray 
    n_2 = r-q # len of right subarray
    print('n1 is: ', n_1)
    print('n2 is: ', n_2)
    left = [0]*(n_1+1) # initiating zero list of lenght n1
    right=[0]*(n_2+1)
    print(left, len(left))
    print(right, len(right))

    # filling left and right
    for i in range(n_1):# because last value will always be infinity
        left[i] = ar[p+i]
    for j in range(n_2):
        right[j] = ar[q+j+1]
        #print(ar[q+j+1])
        #print(right[j])
    # inserting infinity at last index for each subarray
    left[n_1]=math.inf
    right[n_2]=math.inf
    print(left)
    print(right)
    # merging: initiating indeces at 0
    i=0
    j=0
    print('p', p)
    print('r', r)
    for k in range(p,r+1):
        if left[i] <= right[j]:
            ar[k]=left[i]
            # increase i
            i += 1
        else:
            ar[k]=right[j]
            #increase j
            j += 1
            print('preliminary',ar)
    print(ar)
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

