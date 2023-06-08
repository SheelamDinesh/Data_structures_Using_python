def arraySortedOrNot(arr, n):

	# Array has one or no element
	if (n == 0 or n == 1):
		return True

	for i in range(1, n):

		# Unsorted pair found
		if (arr[i-1] > arr[i]):
			return False

	# No unsorted pair found
	return True


# Driver code
arr = [20, 23, 23, 45, 78, 88]
n = len(arr)
if (arraySortedOrNot(arr, n)):
	print("Yes")
else:
	print("No")
	

 

# Output

# Yes
# Time Complexity: O(n) 
# Auxiliary Space: O(1)
