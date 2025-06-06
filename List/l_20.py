def reverse_array_in_place(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

my_array = [10, 2, 3, 4, 5]
reverse_array_in_place(my_array)
print(my_array)  # Output: [5, 4, 3, 2, 10]