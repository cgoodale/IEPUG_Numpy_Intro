import unittest

import numpy as np

import speed_run as sr

class TestPythonLists(unittest.TestCase):
	def setUp(self):
		self.python_list = [[0,1,2],
							[0,1,2],
							[0,1,2]]

		self.power_list = [[0,1,4],
						   [0,1,4],
						   [0,1,4]]

	def test_python_looping(self):
		self.output_grid = sr.square_2d_list(self.python_list)
		self.assertEquals(self.power_list, self.output_grid)

	def test_python_map(self):
		self.output_grid = sr.square_2d_list_w_map(self.python_list)
		self.assertEquals(self.power_list, self.output_grid)

	def test_list_comp(self):
		self.output_grid = sr.square_2d_list_w_list_comp(self.python_list)
		self.assertEquals(self.power_list, self.output_grid)


class TestNumpyArrays(unittest.TestCase):
	def setUp(self):
		self.numpy_array = np.array([[0,1,2],
									 [0,1,2],
									 [0,1,2]])

		self.power_array = np.array([[0,1,4],
						   			 [0,1,4],
						   			 [0,1,4]])

	def test_numpy_with_python_looping(self):
		self.output_grid = sr.square_2d_array_slow_looping(self.numpy_array)
		np.testing.assert_array_equal(self.power_array, self.output_grid)

	def test_numpy_with_vectorization(self):
		self.output_grid = sr.square_2d_array_vectorized(self.numpy_array)
		np.testing.assert_array_equal(self.power_array, self.output_grid)

if __name__ == "__main__":

	unittest.main()