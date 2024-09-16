# Function to remove duplicates from a sorted array
def remove_duplicates(arr):
    if not arr:
        return arr
    
    index = 1  # Start from the second element
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[index] = arr[i]
            index += 1
    
    return arr[:index]

# Example usage
array = [1, 2, 2, 3, 4, 4, 4, 5, 5]
result = remove_duplicates(array)
print(f"Array after removing duplicates: {result}")
