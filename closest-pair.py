from math import sqrt
import sys

def find_distance(P1, P2):
	return sqrt(((P1[0] - P2[0])**2) + (P1[1] - P2[1])**2)

def naive_implementation(points):
	min_dist = sys.maxint
	pair = [(0,0), (0,0)]
	points = list(points)
	for i in range(0, len(points)-1):
		j = i + 1
		for j in range(j, len(points)):
			dist = find_distance(points[i], points[j])
			if dist < min_dist:
				min_dist = dist
				pair = [points[i], points[j]]

	return min_dist, pair


def mergesort(arr, index):

	if len(arr) <= 1:
		return arr

	left = arr[:len(arr)/2]
	right = arr[len(arr)/2:]
	ret = []

	if len(left) == 1 and len(right) == 1:
		if left[0][index] < right[0][index]:
			ret.append(left[0])
			ret.append(right[0])
		else:
			ret.append(right[0])
			ret.append(left[0])
		return ret

	if(len(left) != 0):
		left = mergesort(left, index)

	if(len(right) != 0):
		right = mergesort(right, index)

	return merge(left, right, index)

def merge(left, right, index):	
	ret = []
	i = 0
	j = 0
	while i < len(left) and j < len(right):
		if left[i][index] < right[j][index]:
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

def find_closest_pair(points):
	Px = mergesort(points, 0)
	Py = mergesort(points, 1)

	return find_pairs(Px, Py)

def find_split_pairs(Px, Py, d):

	Xbar = Px[len(Px)/2]

	Sy = []
	for P in Py:
		if (P[0] >= Xbar[0] - d) and (P[1] <= Xbar[1] + d):
			Sy.append(P)

	best = d
	best_pair = []

	for i in range(0, len(Sy)-1):
		for j in range(1, min(7, len(Sy) - i)):
			dist = find_distance(Sy[i], Sy[j])
			if dist < best:
				best_pair = [Sy[i], Sy[j]]
	
	return best, best_pair

def find_pairs(Px, Py):

	if len(Px) <= 3 or len(Py) <= 3:
		points = set(Px) | set(Py)
		return naive_implementation(points)

	Qx = Px[:len(Px)/2]
	Rx = Px[len(Px)/2:]

	Qy = Py[:len(Py)/2]
	Ry = Py[len(Py)/2:]

	d1, pair1 = find_pairs(Qx, Qy)
	d2, pair2 = find_pairs(Rx, Ry)
	d = min(d1, d2)
	d3, pair3 = find_split_pairs(Px, Py, d)

	if d3 < d:		
		return d3, pair3
	else:
		if d1 < d2:
			return d1, pair1
		else:
			return d2, pair2


points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
pair = find_closest_pair(points)
print(pair)
pair = naive_implementation(points)
print(pair)

points = [(1, 1), (4, 1), (1, 5), (1000, 1000)]
pair = find_closest_pair(points)
print(pair)
pair = naive_implementation(points)
print(pair)

points = [(100000, 200000), (200000, 200000), (150000, 286603), (60000, 140000), (240000, 140000), (150000, 340000), (1, 340000), (300000, 340000), (150000, 87087)]
pair = find_closest_pair(points)
print(pair)
pair = naive_implementation(points)
print(pair)

points = [(0, 0), (-4, 1), (-7, -2), (4, 5), (1, 1)]
pair = find_closest_pair(points)
print(pair)
pair = naive_implementation(points)
print(pair)

points = [(0, 0), (0, 1), (100, 45), (2, 3), (9, 9)]
pair = find_closest_pair(points)
print(pair)
pair = naive_implementation(points)
print(pair)
