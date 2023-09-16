# Insertion sort
import numpy as np

# Set the random seed to a specific value e.g.42
np.random.seed(42)

# create a array of 5 random integers between 0 to 9
random_integers = np.random.randint(0, 10, 6)

print("Original array:", random_integers)


# Define a function to perform insertion sort operation
def insert_sort(arr):
    # loop starts from the second elements(index 1)
    for i in range(1, len(arr)):
        # Store the current element as 'key'
        key = arr[i]
        # Initilize the 'j' as the element before 'i'
        j = i - 1

        # Move elements that are greater than the 'key' to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Place the 'key' to its correct position
        arr[j + 1] = key

# Sort the array using the insertion_sort function
insert_sort(random_integers)

print("Sorted array:", random_integers)

# results    
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j] = key