from random import randint

def quicksort(arr):

	if len(arr) <= 1:
		return arr

	if len(arr) == 2:
		ret = []
		ret.append(min(arr[0], arr[1]))
		ret.append(max(arr[0], arr[1]))
		return ret

	left = []
	right = []
	pivot, left, right = partition(arr)

	left = quicksort(left)
	right = quicksort(right)

	left.append(pivot)
	return left + right

def partition(arr):
	left = []
	right = []
	pivot = arr[len(arr)/2]
	arr.pop(len(arr)/2)

	for item in arr:
		if item < pivot:
			left.append(item)
		else:
			right.append(item)
	
	return pivot, left, right

arr = []
sum = 0
for i in range(0, 100):
	val = randint(0,100)
	arr.append(val)
	sum = sum + val
print(len(arr), sum, arr)


arr = quicksort(arr)
sum = 0
for i in arr:
	sum = sum + i
print(len(arr), sum, arr)