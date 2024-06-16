import numpy as np

def jacobi(A: np.ndarray, b: np.ndarray, X0: np.ndarray, k: int, e: float) -> tuple[np.ndarray, np.ndarray]:
	"""
	A : Matriz de fatores
	b : Vetor de resultados
	X0 : Vetor de valores iniciais de X
	k : Número máximo de iterações
	e : Epsilon, desvio mínimo

	Retorna
	-------
	(X, E) : Tupla, X é lista de vetores de Xn, E é lista de epsilons
	"""
	F = np.repeat(A, repeats=1, axis=1)
	np.fill_diagonal(F, 0)
	F = F / -np.diagonal(A)
	d = b / np.diagonal(A)
	Xn = np.repeat(X0, repeats=1, axis=0)
	E = []
	X = []
	for i in range(0,k):
		X.append(Xn)
		Xn_old = np.repeat(Xn, repeats=1, axis=0)
		Xn = F @ Xn + d
		E.append(np.amax(np.absolute(Xn - Xn_old), axis=0))
		if E[-1] < e:
			break
	X.append(Xn)
	return (X, E)
#print(jacobi(A=np.array([[2., -1.],[1., 2.]]), b=np.array([1., 3.]), X0=np.array([0., 0.]), k=10, e=1e-2))