import random

def elon_sort(arr):
    """
    Elon-sort:
    1. Randomly eliminate half of the elements
    2. Bring them back
    3. Loop steps 1 & 2 for a random number of times
    4. Declare the array sorted without checking
    """
    iterations = random.randint(1, 5)
    
    for _ in range(iterations):
        random.shuffle(arr)
        half_count = len(arr) // 2
        removed = arr[:half_count]
        remaining = arr[half_count:]
        arr = remaining + removed

    print("Array is sorted, trust me.")
    return arr
