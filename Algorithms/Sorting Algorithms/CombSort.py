# Time complexity: O(n^2)

def getGap(gap):
 
    # Reduce Gap by a factor
    gap = (gap * 10)/13
    if gap < 1:
        return 1
    return gap
 
# Comb Sort:
def combSort(arr):
    n = len(arr)
 
    # Set gap to n at beginning:
    gap = n
 
    # Set swapped to True so that while loop can run:
    swapped = True
 
    # We keep running the while loop when gap>1 and the most recent iteration makes a swap:
    while gap != 1 or swapped == 1:
 
        # Finding the coming gap:
        gap = getGap(gap)
 
        # We set swap as false so we can check during for loop if a swap is needed:
        swapped = False
 
        # Compare all elements with the current change in elements:
        for i in range(0, n-gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
 
 
# Example array:
arr = [8, 3, 1, 30, -44, 23, -6, -28, 0]
combSort(arr)
 
print ("Sorted array:")
for i in arr:
    print(i)
