from asteval import Interpreter
import numpy as np

aeval = Interpreter()

def jacobi(k):
	for i in range(0,k - 1):
		aeval("")
