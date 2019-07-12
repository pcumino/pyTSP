import numpy as np, random, operator, pandas as pd, matplotlib.pyplot as plt

from City import City
from Fitness import Fitness

def initialPopulation(popSize, cityList):
	population = []

	for i in range(0, popSize):
		population.append(createRoute(cityList))
	return population

def createRoute(cityList):
	route = random.sample(cityList, len(cityList))
	return route

def rankRoutes(population):
	fitnessResults = {}
	for i in range(0,len(population)):
		fitnessResults[i] = Fitness(population[i]).routeFitness()
	return sorted(fitnessResults.items(), key = operator.itemgetter(1), reverse = True)


def selection(popRanked, eliteSize):
	selectionResults = []
	df = pd.DataFrame(np.array(popRanked), columns=["Index","Fitness"])
	df['cum_sum'] = df.Fitness.cumsum()
	df['cum_perc'] = 100*df.cum_sum/df.Fitness.sum()

	for i in range(0, eliteSize):
		selectionResults.append(popRanked[i][0])
	for i in range(0, len(popRanked) - eliteSize):
		pick = 100*random.random()
		for i in range(0, len(popRanked)):
			if pick <= df.iat[i,3]:
				selectionResults.append(popRanked[i][0])
				break
	return selectionResults

def matingPool(population, selectionResults):
	matingpool = []
	for i in range(0, len(selectionResults)):
		index = selectionResults[i]
		matingpool.append(population[index])
	return matingpool

def main():
	numberCities = 5
	cityList = [ City(np.random.randint(0,30),np.random.randint(0,30)) for e in range(0,numberCities)]
	pop = initialPopulation(3, cityList)
	[print(city) for city in pop]
	print()
	
	rankRoutes(pop)
	
	[print(city) for city in pop]



if __name__ == '__main__':
	main()