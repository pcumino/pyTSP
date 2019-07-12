import numpy as np, random, operator, pandas as pd, matplotlib.pyplot as plt

class City():
	"""docstring for City"""
	def __init__(self, x, y):
		super(City, self).__init__()
		self.x = x
		self.y = y

	def distance(self, city):
		xDis = abs(self.x - city.x)
		yDis = abs(self.y - city.y)
		dist = np.sqrt((xDis ** 2) + (yDis ** 2))
		return dist

	def __repr__(self):
		return "(" + str(self.x) + "," + str(self.y) + ")"