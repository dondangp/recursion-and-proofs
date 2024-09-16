# Function to merge two sorted arrays
def merge_two_sorted_arrays(arr1, arr2):
    merged = []
    i, j = 0, 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    
    # Append the remaining elements
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    
    return merged

# Function to merge K sorted arrays
def merge_k_sorted_arrays(arrays):
    if not arrays:
        return []

    while len(arrays) > 1:
        merged_arrays = []

        # Merge pairs of arrays
        for i in range(0, len(arrays), 2):
            if i + 1 < len(arrays):
                merged_arrays.append(merge_two_sorted_arrays(arrays[i], arrays[i+1]))
            else:
                merged_arrays.append(arrays[i])
        
        arrays = merged_arrays
    
    return arrays[0]

# Example usage
array1 = [1, 3, 5, 7]
array2 = [2, 4, 6, 8]
array3 = [0, 9, 10, 11]
result = merge_k_sorted_arrays([array1, array2, array3])
print(f"Merged array: {result}")
