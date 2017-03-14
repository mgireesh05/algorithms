
def mergesort(arr):

	if len(arr) <= 1:
		return arr

	left = arr[:len(arr)/2]
	right = arr[len(arr)/2:]
	ret = []

	if len(arr) == 1 and len(right) == 1:
		if left[0] < right[0]:
			ret.append(left[0])
			ret.append(right[0])
		else:
			ret.append(right[0])
			ret.append(left[0])
		return ret

	if(len(left) != 0):
		left = mergesort(left)

	if(len(right) != 0):
		right = mergesort(right)

	return merge(left, right)

def merge(left, right):	
	ret = []
	i = 0
	j = 0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			ret.append(left[i])
			i = i + 1
		else:
			ret.append(right[j])
			j = j + 1

	while i < len(left):
		ret.append(left[i])
		i = i + 1

	while j < len(right):
		ret.append(right[j])
		j = j + 1

	return ret

arr = []
for i in range(0, 100):
	arr.append(99-i)
print(arr)

arr = mergesort(arr)
print("Sorted: ",  arr)