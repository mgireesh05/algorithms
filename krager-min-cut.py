import random
import copy


class Vertex:
	def __init__(self, vid, adjacencies):
		self.vid = vid
		self.adjacencies = adjacencies

	def fix_links(self, vertex_to_stay, vertex_to_go):
		if self.vid in vertex_to_go.adjacencies:
			if vertex_to_stay.vid in self.adjacencies:
				self.adjacencies[vertex_to_stay.vid] = self.adjacencies[vertex_to_stay.vid] + vertex_to_go.adjacencies[self.vid]
			else:
				self.adjacencies[vertex_to_stay.vid] = self.adjacencies[vertex_to_go.vid]

		if self.vid == vertex_to_stay.vid:
			for vid in vertex_to_go.adjacencies:
				if vid in self.adjacencies:
					self.adjacencies[vid] = self.adjacencies[vid] + vertex_to_go.adjacencies[vid]
				else:
					self.adjacencies[vid] = vertex_to_go.adjacencies[vid]

		if vertex_to_go.vid in self.adjacencies:
			self.adjacencies.pop(vertex_to_go.vid)

		if self.vid in self.adjacencies:
			self.adjacencies.pop(self.vid)


class Graph:
	def __init__(self, name):
		self.name = name
		self.orig_vertices = []
		self.vertices = []
		self.orig_len = 0
	
	def add_vertices(self, vid, adjacencies):
		adj = {}
		for item in adjacencies:
			if item in adj:
				adj[item] = adj[item] + 1
			else:
				adj[item] = 1

		vertex = Vertex(vid, adj)		
		self.vertices.append(vertex)
		self.orig_vertices.append(copy.deepcopy(vertex))
		self.orig_len = self.orig_len + 1

	def contract_edge(self, vertex_to_stay, vertex_to_go):
		for item in self.vertices:
			item.fix_links(vertex_to_stay, vertex_to_go)

		self.vertices.remove(vertex_to_go)

	def get_random(self):
		random_vertex = random.choice(self.vertices)
		edge = []
		for item in random_vertex.adjacencies:
			edge.append(item)
			break
		edge.append(random_vertex.vid)
		
		ret = []
		for item in self.vertices:
			if item.vid == edge[0]:
				ret.append(item)

		for item in self.vertices:
			if item.vid == edge[1]:
				ret.append(item)

		return ret

	def validate_cut(self):
		if(len(self.vertices) != 2):
			print "Final vertices not equal to 2; not a valid cut"
			return False

		v1 = self.vertices[0]
		v2 = self.vertices[1]

		if(len(v1.adjacencies) != 1):
			print "V1 adjacencies not equal to 1; not a valid cut"
			return False

		if(len(v2.adjacencies) != 1):
			print "V1 adjacencies not equal to 1; not a valid cut"
			return False

		if v1.vid not in v2.adjacencies:
			print "V1 not in V2 adjacencies; not a valid cut"
			return False

		if v2.vid not in v1.adjacencies:
			print "V2 not in V1 adjacencies; not a valid cut"
			return False

		if v1.adjacencies[v2.vid] != v2.adjacencies[v1.vid]:
			print "V1 <-> V2 links are not same; not a valid cut"
			return False

		return True

	def find_cut(self):
		if len(self.vertices) == 2:
			# Copy the graph for the next run
			self.vertices = copy.deepcopy(self.orig_vertices)			

		while len(self.vertices) != 2:
			random_edge = self.get_random()
			self.contract_edge(random_edge[0], random_edge[1])
			
		if (self.validate_cut()):
			cut = self.vertices[0].adjacencies[self.vertices[1].vid]
			#print ("Cut = ", cut, ", V1 <-> V2 links are same; so a valid cut")
			return cut

	def find_min_cut(self):
		min_cut = self.find_cut()
		for i in range(0, 50000):
			cut = self.find_cut()
			if cut < min_cut:
				min_cut = cut
				print ("Got a smaller cut", cut)
		return min_cut

	def convert_to_adjacency_matrix(self):
		adj_matrix = []
		for i in range(0, self.orig_len):
			row = []
			for j in range(0, self.orig_len):
				row.append(0)
			adj_matrix.append(row)

		for item in self.vertices:
			for key in item.adjacencies:				
				adj_matrix[key-1][item.vid-1] = item.adjacencies[key]

		print "====Start===="
		for item in adj_matrix:
			print item
		print "====End======"


	def print_graph(self):
		print "----Start----"
		for item in self.vertices:
			print (str(item.vid) + " -> " + str(item.adjacencies))
		print "----End------"

	def print_orig_graph(self):
		print "----Start----"
		for item in self.orig_vertices:
			print (str(item.vid) + " -> " + str(item.adjacencies))
		print "----End------"


## --------- Tests --------- ##
input_file = open("kragerMinCut-tc1.txt")
lines = input_file.readlines()
graph = Graph("Graph")

for line in lines:
	item = line.split()
	item = [int(x.strip()) for x in item]
	vertex = item[0]
	adjacencies = item[1:]
	graph.add_vertices(vertex, adjacencies)

min_cut = graph.find_min_cut()
assert (min_cut == 2), "Min cut not correct!"

input_file = open("kragerMinCut-tc2.txt")
lines = input_file.readlines()
graph = Graph("Graph")

for line in lines:
	item = line.split()
	item = [int(x.strip()) for x in item]
	vertex = item[0]
	adjacencies = item[1:]
	graph.add_vertices(vertex, adjacencies)

min_cut = graph.find_min_cut()
assert (min_cut == 2), "Min cut not correct!"

input_file = open("kragerMinCut-tc3.txt")
lines = input_file.readlines()
graph = Graph("Graph")

for line in lines:
	item = line.split()
	item = [int(x.strip()) for x in item]
	vertex = item[0]
	adjacencies = item[1:]
	graph.add_vertices(vertex, adjacencies)

min_cut = graph.find_min_cut()
assert (min_cut == 1), "Min cut not correct!"

input_file = open("kragerMinCut-tc4.txt")
lines = input_file.readlines()
graph = Graph("Graph")

for line in lines:
	item = line.split()
	item = [int(x.strip()) for x in item]
	vertex = item[0]
	adjacencies = item[1:]
	graph.add_vertices(vertex, adjacencies)

min_cut = graph.find_min_cut()
assert (min_cut == 1), "Min cut not correct!"

input_file = open("kragerMinCut-tc5.txt")
lines = input_file.readlines()
graph = Graph("Graph")

for line in lines:
	item = line.split()
	item = [int(x.strip()) for x in item]
	vertex = item[0]
	adjacencies = item[1:]
	graph.add_vertices(vertex, adjacencies)

min_cut = graph.find_min_cut()
assert (min_cut == 3), "Min cut not correct!"

input_file = open("kragerMinCut-tc6.txt")
lines = input_file.readlines()
graph = Graph("Graph")

for line in lines:
	item = line.split()
	item = [int(x.strip()) for x in item]
	vertex = item[0]
	adjacencies = item[1:]
	graph.add_vertices(vertex, adjacencies)

min_cut = graph.find_min_cut()
assert (min_cut == 2), "Min cut not correct!"

input_file = open("kragerMinCut.txt")
lines = input_file.readlines()
graph = Graph("Graph")

for line in lines:
	item = line.split()
	item = [int(x.strip()) for x in item]
	vertex = item[0]
	adjacencies = item[1:]
	graph.add_vertices(vertex, adjacencies)

min_cut = graph.find_min_cut()
assert (min_cut == 17), "Min cut not correct!"

print "All tests pass!"

