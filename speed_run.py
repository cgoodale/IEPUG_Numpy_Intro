import copy
import numpy as np

TEST_CYCLES = 100

"""
GOAL:  Take a 100 x 100 grid and square all values to the power of 2 and Test
several difference approaches to completing this task, with python lists and
numpy arrays.
"""

def make_2d_grid(x,y):
	list_based_2d_grid = []
	for i in range(x):
		list_based_2d_grid.append(range(y))

	return list_based_2d_grid

default_array = np.array(make_2d_grid(100,100))

PYTHON_GRID = make_2d_grid(100,100)

def square_2d_list(input_grid=PYTHON_GRID):
	""" This will raise each element in a 2d grid to the power of 2.

	Input:
		input_grid <list> List of lists whos elements will be squared to a power of 2.

	Return:
		power_grid <list> The input list elements square to the power of 2.
	"""
	# Must do this since Lists are mutable
	power_grid = copy.deepcopy(input_grid)

	for ix, x in enumerate(input_grid):
		for iy, y in enumerate(x):
			# Final assignment should be to the copied grid
			power_grid[ix][iy] = pow(y, 2)

	return power_grid

def square_2d_list_w_map(input_grid=PYTHON_GRID):
	""" This will square each element in a 2d grid to the power of 2.

	Input:
		input_grid <list> List of lists whos elements will be squared to a power of 2.

	Return:
		power_grid <list> The input list elements square to the power of 2.
	"""
	# Must do this since Lists are mutable
	power_grid = copy.deepcopy(input_grid)

	for ix, x in enumerate(power_grid):
		power_grid[ix] = map(lambda element: pow(element, 2), x)

	return power_grid

def square_2d_list_w_list_comp(input_grid=PYTHON_GRID):
	""" This will square each element in a 2d grid to the power of 2.

	Input:
		input_grid <list> List of lists whos elements will be squared to a power of 2.

	Return:
		power_grid <list> The input list elements square to the power of 2.
	"""
	# Must do this since Lists are mutable
	power_grid = copy.deepcopy(input_grid)

	grid = [[pow(y,2) for y in x] for x in power_grid]

	return grid

def square_2d_array_slow_looping(input_array=default_array):
	""" This will square each element in a 2d array to the power of 2, using a 
	typical pythonic FOR LOOP approach.

	Input:
		input_grid <numpy.ndarray> 2d Array whos elements will be squared to a power of two.

	Return:
		power_grid <numpy.ndarray> The input array elements square to the power of 2.
	"""
	power_grid = input_array.copy()

	for ix, x in enumerate(input_array):
		for iy, y in enumerate(x):
			# Final assignment should be to the copied grid
			power_grid[ix][iy] = y**2

	return power_grid

def square_2d_array_vectorized(input_array=default_array):
	""" This will square each element in a 2d array to the power of 2, using the 
	numpy vectorize approach.

	Input:
		input_grid <numpy.ndarray> 2d Array whos elements will be squared to a power of two.

	Return:
		power_grid <numpy.ndarray> The input array elements square to the power of 2.
	"""
	# Keeping the copy function in here to compare fairly
	power_grid_copy = input_array.copy()

	power_grid = input_array**2

	return power_grid






if __name__ == '__main__':
	import timeit
	print("Python List Based Test")
	print(timeit.timeit("square_2d_list()", setup="from __main__ import square_2d_list", number=TEST_CYCLES))

	print("Python List Test Using map built-in function")
	print(timeit.timeit("square_2d_list_w_map()", setup="from __main__ import square_2d_list_w_map", number=TEST_CYCLES))

	print("Python List Test Using List Comprehension")
	print(timeit.timeit("square_2d_list_w_list_comp()", setup="from __main__ import square_2d_list_w_list_comp", number=TEST_CYCLES))

	print("Numpy Array using Pythonic Looping")
	print(timeit.timeit("square_2d_array_slow_looping()", setup="from __main__ import square_2d_array_slow_looping", number=TEST_CYCLES))

	print("Numpy Array using Numpy Vectorize")
	print(timeit.timeit("square_2d_array_vectorized()", setup="from __main__ import square_2d_array_vectorized", number=TEST_CYCLES))

