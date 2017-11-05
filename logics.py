"""
Filename: operation_logic.py
Author: zhuangr
date: 05/04/2017
"""
"""
This file is about the logic of operations in the game of 2048.
It is based on some concepts of matrix in the operations. The 
operations will be interpret in the method of a class
"""
import random
import interfaces

def matrix(n):
	"""create an n*n matrix"""

class Oper:
	"""A class that initial the matrix and interpret the operations
	of the game of 2048"""

	def __init__(self,rows = 4):
		"""Constructor: initialize the matrix"""
		self.mat = []

		for i in range(rows):
			row = []
			for i in range(rows):
				row.append(0)
			self.mat.append(row)

	def matrix(self, n):
		"""create an n*n zero matrix"""
		matrix = []
		for i in range(n):
			row=[]
			for i in range(n):
				row.append(0)
			matrix.append(row)
		return matrix

	def random_update(self):
		"""randomly assigned one empty cell with number 2 or 4"""
		a = random.randrange(0, len(self.mat))
		b = random.randrange(0, len(self.mat))
		while self.mat[a][b] != 0:
			a = random.randrange(0, len(self.mat))
			b = random.randrange(0, len(self.mat))

		c = random.random()
		if c < 0.90:
			self.mat[a][b] = 2
		else:
			self.mat[a][b] = 4


	def add(self):
		"""add the two cells horizontally toward the left side if the 
		two cells are identical"""
		for r in range(len(self.mat)):
			for c in range(len(self.mat)-1):
				if self.mat[r][c] != 0 and self.mat[r][c] == self.mat[r][c+1]:
					self.mat[r][c] = 2 * self.mat[r][c]
					self.mat[r][c+1] = 0

	def compress(self):
		"eliminate zeros between cells which have values"
		l = len(self.mat)
		new_mat = self.matrix(l)
		for r in range(l):
			count = 0
			for c in range(l):
				if self.mat[r][c] != 0:
					new_mat[r][count] = self.mat[r][c]
					count += 1
		return new_mat


	def identify_offsets(self,row,column):
		"""identify if there are identical cell in the surrounding of a given
		cell"""
		l = len(self.mat)
		mat = self.mat[row][column]
		offsets = [    (-1, 0),    
				(0,-1),      (0, 1),
				      (1, 0)        ]
		for offset in offsets:
			r = row + offset[0]
			c = column + offset[1]
			if (r >= 0 and r < l) and (c >= 0 and c < l):
				if self.mat[r][c] == mat:
					return True
		return False

	def game_state(self):
		"""check all the cells and return 1 as win, -1 as lose, 0 as keep
		going"""
		l = len(self.mat)
		for r in range(l):
			for c in range(l):
				if self.mat[r][c] == 2048:
					return 1

		count = 0
		for r in range(l):
			for c in range(l):
				if self.identify_offsets(r, c) == True:
					count += 1
				if self.mat[r][c] == 0:
					count += 1
		if count == 0:
			return -1
		else:
			return 0

	def transpose(self):
		"""transpose the matrix"""
		l = len(self.mat)
		newlist = []
		for r in range(l):
			alist = []
			for c in range(l):
				alist.append(self.mat[c][r])
			newlist.append(alist)
		return newlist

	def reverse(self):
		"""reverse the matrix which means flip the entries around"""
		l = len(self.mat)
		newlist = []
		for r in range(l):
			alist = []
			for c in range(l):
				alist.append(self.mat[r][-c - 1])
			newlist.append(alist)
		return newlist

	def leftward(self):
		"""update the matrix if the user's command is toward left"""
		self.mat = self.compress()
		self.add()
		self.mat = self.compress()

	def rightward(self):
		"""update the matrix if the user's command is toward right"""
		self.mat = self.reverse()
		self.mat = self.compress()
		self.add()
		self.mat = self.compress()
		self.mat = self.reverse()

	def upward(self):
		"""update the matrix if the user wants to move upward"""
		self.mat = self.transpose()
		self.mat = self.compress()
		self.add()
		self.mat = self.compress()
		self.mat = self.transpose()

	def downward(self):
		"""update the matrix if the user wants to move downward"""
		self.mat = self.transpose()
		self.mat = self.reverse()
		self.mat = self.compress()
		self.add()
		self.mat = self.compress()
		self.mat = self.reverse()
		self.mat = self.transpose()

	def checker(self):
		"Check if there are entries in all the cells"
		l = len(self.mat)
		count = 0
		for r in range(l):
			for c in range(l):
				if self.mat[r][c] != 0:
					count += 1
		return count





def main():
    m = Oper()
    m.random_update()
    k = interfaces.Graphics()
    k.update_cells(m.mat)

    k.startmainloop(m)
    
    
if __name__ == '__main__':
    main()
