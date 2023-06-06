# Python code to split into even and odd lists
# Function to split
def Split(mix):
	ev_li = []
	od_li = []
	for i in mix:
		if (i % 2 == 0):
			ev_li.append(i)
		else:
			od_li.append(i)
	print("Even lists:", ev_li)
	print("Odd lists:", od_li)

# Driver Code
mix = [2, 5, 13, 17, 51, 62, 73, 84, 95]
Split(mix)
