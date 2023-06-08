def print2largest(arr, arr_size):

	if (arr_size < 2):
	
		print(" Invalid Input ")
		return
	

	first = second = -2147483648
	for i in range(arr_size):
	
		if (arr[i] > first):
		
			second = first
			first = arr[i]
      
		elif (arr[i] > second and arr[i] != first):
			second = arr[i]
	
	if (second == -2147483648):
		print("There is no second largest element")
	else:
		print("The second largest element is", second)


# Driver program
arr = [12, 35, 1, 10, 34, 1]
n = len(arr)

print2largest(arr, n)


# Output

# The second largest element is 34
# Complexity Analysis:

# Time Complexity: O(n). 
# Only one traversal of the array is needed.
# Auxiliary space: O(1). 
# As no extra space is required.
