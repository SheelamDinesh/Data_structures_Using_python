
def print2largest(arr, arr_size):

	if (arr_size < 2):
		print(" Invalid Input ");
		return;

	largest = second = -2454635434;

	# Find the largest element
	for i in range(0, arr_size):
		largest = max(largest, arr[i]);
    
	for i in range(0, arr_size):
		if (arr[i] != largest):
			second = max(second, arr[i]);

	if (second == -2454635434):
		print("There is no second " +
			"largest element");
	else:
		print("The second largest " +
			"element is \n", second);

# Driver code
if __name__ == '__main__':

	arr = [12, 35, 1,
		10, 34, 1];
	n = len(arr);
	print2largest(arr, n);


 

# Output

# Second largest : 12
# Complexity Analysis:

# Time Complexity: O(n). 
# Two traversals of the array is needed.
# Auxiliary space: O(1). 
# As no extra space is required.
