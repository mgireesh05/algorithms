from random import randint

def quicksort(arr, option):
	comparisons = [0] #sending as an array so as to preserve the values across recursion levels
	do_quicksort(arr, 0, len(arr), comparisons, option)
	return comparisons[0]

def do_quicksort(arr, start, end, comparisons, option):
	if start >= end:
		return

	if len(arr) == 2 or end - start == 1: #base case
		if arr[end-1] < arr[start]:
			temp = arr[start]
			arr[start] = arr[end-1]
			arr[end-1] = temp
		return

	# count the swaps in reach recursion step (for coursera assignment)
	m = end - start - 1
	comparisons[0] = comparisons[0] + m

	#partition the arrary - in place
	pivot_index = partition(arr, start, end, option)

	#sort the left sub array
	do_quicksort(arr, start, pivot_index, comparisons, option)
	#sort the right sub array
	do_quicksort(arr, pivot_index + 1, end, comparisons, option)

	return

def median_of_three(a, idx_a, b, idx_b, c, idx_c):
    if a <= b <= c or c <= b <= a:
		return idx_b
    elif b <= a <= c or c <= a <= b:
		return idx_a
    else:
		return idx_c

def choose_pivot(arr, start, end, option):
	if option == "first":
		#just return the first element
		pivot = arr[start]
	elif option == "last":
		#swap the last and first and then return the first
		temp = arr[start]
		arr[start] = arr[end-1]
		arr[end-1] = temp
		pivot = arr[start]
	elif option == "median":
		#find the median value of first, middle, and last and then swap that with the first and then return the first
		first = arr[start]
		last = arr[end-1]	
		if (end - start) % 2 == 0:
			mid_offset = ((end - start) / 2) - 1
		else: 
			mid_offset = (end - start)/2
		middle_index = start + mid_offset #note: the offset must be added to the start to point to the correct index
		middle = arr[middle_index]

		median_index = median_of_three(first, start, middle, middle_index, last, end-1)
		temp = arr[start]
		arr[start] = arr[median_index]
		arr[median_index] = temp
		pivot = arr[start]
	else:
		pivot = arr[start]

	return pivot

def partition(arr, start, end, option):
	pivot = choose_pivot(arr, start, end, option)
	i = start + 1 #index of the array where the elements to the left are partitioned and elements to the right are not
	j = start + 1 #index of the partitioned array where elements to the left are less than or equal to the pivot and elements to the right are greater
	
	for i in range(start + 1, end):
		if arr[i] > pivot:
			i = i + 1 #value is greater than the pivot, just move on by incrementing "i"
		else:
			#value is less than or equal to the pivot,
			#swap the values so as to move the greater values to the right of "j" and lesser values to the left of "j"
			temp = arr[i]
			arr[i] = arr[j]
			arr[j] = temp
			#move "i" and "j"
			j = j + 1 
			i = i + 1
			
	#finally, swap the pivot to order the arrary in the form <p <-> p <-> >p
	arr[start] = arr[j-1]
	arr[j-1] = pivot

	#return the pivot to be used to split the array for the next recursive step
	return j-1

def check(arr):
	cur = 0
	prev = 0
	for val in arr:
		cur = val
		assert (prev <= cur), "Not sorted correctly!"
		prev = cur
	return

arr = [70, 83, 79]
quicksort(arr, "first")
check(arr)
print(arr)

arr = [3, 8, 2, 5, 1, 4, 7, 6]
quicksort(arr, "first")
check(arr)
print(arr)

arr = [95, 38, 70, 26, 42, 100, 0, 24, 20, 76]
quicksort(arr, "first")
check(arr)
print(arr)

arr = []
for i in range(0, 50):
	val = randint(0,100)
	arr.append(val)

quicksort(arr, "first")
check(arr)
print(arr)
arr = []
max_range = randint(0,10000)
for i in range(0, max_range):
	val = randint(0,100)
	arr.append(val)

quicksort(arr, "first")
check(arr)

input_file = open("input.txt")
arr = input_file.readlines()
arr = [int(x.strip()) for x in arr] #Make sure to convert the read line to int, otherwise the answer won't be correct
comparisons = quicksort(arr, "first")
check(arr)
assert (comparisons == 565), "Comparisons are not correct!"

input_file = open("input.txt")
arr = input_file.readlines()
arr = [int(x.strip()) for x in arr] #Make sure to convert the read line to int, otherwise the answer won't be correct
comparisons = quicksort(arr, "last")
check(arr)
assert (comparisons == 588), "Comparisons are not correct!"

input_file = open("input.txt")
arr = input_file.readlines()
arr = [int(x.strip()) for x in arr] #Make sure to convert the read line to int, otherwise the answer won't be correct
comparisons = quicksort(arr, "median")
check(arr)
assert (comparisons == 530), "Comparisons are not correct!"

print "All tests passed!!!"
