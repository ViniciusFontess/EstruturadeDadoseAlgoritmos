def binary_search (nums, n, l=0, r= None):
    if r is None:
        r = len(nums)-1
        
    while l < r:
        mid = int((l+r)/2)

        if nums[mid] == n:
            return mid
        elif nums[mid] < n:
            l = mid+1
        else:
            r = mid
    return -1        

def exponential_search(arr,target):
    if arr[0] == target:
        return 0
    n = len(arr)
    i = 1

    while i < n and arr[i] > target:
        i *= 2

    if arr[i] == target:
        return i
    
    return binary_search(arr, target, i//2, min(i,n))


    
target = 32
d = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
result = exponential_search(d,target)
print(f"Element found at index {result}")



