# Comb Sort in Python:
# Time Complexity: O(n^2)

def findNextGap(gap):
 
    # We set a shrink factor
    gap = (gap * 10)/13
    if gap < 1:
        return 1
    return gap
 
# Comb Sort:
def combSort(l):
 
    # We set the gap to the length of the array:
    gap = len(l)
 
    # We set swaps to True initially:
    swaps = True
 
    # We keep running this loop until the gap is 1 (no gap), or there are no more swaps:
    while gap != 1 or swaps == 1:
 
        # We find the next gap in numbers (change in numbers):
        gap = findNextGap(gap)
 
        # We set swaps as false before entering for loop:
        swaps = False
 
        # We compare all the several elements in the list with the current difference:
        for i in range(0, len(l)-gap):
            if l[i] > l[i + gap]:
                l[i], l[i + gap] = l[i + gap], l[i]
                swaps = True
            
#Example Array:
l = [2,7,19,30,83,29,50,28,58,23,-28,-29,-30,3,20,1,5,9]
combSort(l)
print ("Here is the sorted array:")
for i in arr:
    print(i)
