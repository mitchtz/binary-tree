class tree:
	def __init__(self):
		self.node_list = []
		self.node_num = 0

	#Insert new node, takes in value and node to start at, starts at root be default.
	def insert(self, value, check_node=0):
		#First node being inserted
		if self.node_num == 0:
			#Create root node
			self.node_list.append(node(value, None, None, None))
			#Increment the node num
			self.node_num = self.node_num + 1
			return True
		#Get value for current node, if value is less than the current node, recursively call left
		if value < self.node_list[check_node].get_value():
			#Check if left child exists, if not, create child
			if self.node_list[check_node].get_l_child() == None:
				#Create node
				self.node_list.append(node(value, check_node, None, None))
				#Update parent
				self.node_list[check_node].set_l_child(self.node_num)
				#Increment the node num
				self.node_num = self.node_num + 1
				return True
			else:
				#Call again with  left child as check_node
				return self.insert(value, self.node_list[check_node].get_l_child())
		#Else value is greater or equal and should go to right and be called again
		else:
			#Check if right child exists, if not, create child
			if self.node_list[check_node].get_r_child() == None:
				#Create node
				self.node_list.append(node(value, check_node, None, None))
				#Update parent
				self.node_list[check_node].set_r_child(self.node_num)
				#Increment the node num
				self.node_num = self.node_num + 1
				return True
			else:
				#Call again with left child as check_node
				return self.insert(value, self.node_list[check_node].get_r_child())
	#Finds the value in a tree, return True if found, Flase otherwise
	#Takes in value to find, and node to start checking at, which is 0 by default
	def find(self, value, check_node=0):
		#Check to see if the current node is the correct one
		if self.node_list[check_node].get_value() == value:
			return True
		#otherwise, check if value is less than current node. If so, call find with the left child
		elif value < self.node_list[check_node].get_value():
			#Check if left node exists, if not, return False
			if self.node_list[check_node].get_l_child() == None:
				return False
			#Else call find on left node
			else:
				return self.find(value, self.node_list[check_node].get_l_child())
		#Else value is greater or equal to current node, then check right node
		else:
			#Check if right node exists, if not, return False
			if self.node_list[check_node].get_r_child() == None:
				return False
			#Else call find on left node
			else:
				return self.find(value, self.node_list[check_node].get_r_child())

	#Prints all nodes in the tree in order of being added
	def print_all(self):
		for num, i in enumerate(self.node_list):
			print("----------------------------")
			
			print("NODE NUM:", num)
			print("Parent:", i.get_parent())
			print("Value:", i.get_value())
			print("Left Child:", i.get_l_child())
			print("Right Child:", i.get_r_child())
	'''
	TODO:
	delete function
	tree height function (possibly)
	tree width function (possibly)
	Make functions iterative instead of recursive (possibly)
	'''
			

#Helper class for tree class
class node:
	def __init__(self, value, parent, l_child, r_child):
		self.value = value
		#Num (index) of parent node
		self.parent = parent
		#Num (index) of left child
		self.l_child = l_child
		#Num (index) of right child
		self.r_child = r_child
	#Returns the value of the node
	def get_value(self):
		return self.value
	#Returns the parent node
	def get_parent(self):
		return self.parent
	#Returns left child
	def get_l_child(self):
		return self.l_child
	#Returns right child
	def get_r_child(self):
		return self.r_child
	#Sets the value for the node
	def set_value(self, value):
		self.value = value
	#Sets the parent for the node
	def set_parent(self, parent):
		self.parent = parent
	#Sets the left child for the node
	def set_l_child(self, l_child):
		self.l_child = l_child
	#Sets the right child for the node
	def set_r_child(self, r_child):
		self.r_child = r_child