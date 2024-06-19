import jacobi
import ioj
import matplotlib.pyplot as plot
import numpy as np
import pandas as pd

sis = ioj.welcomeUser()
A, b, par, X0, sol = ioj.userInput(sis)
if sis != 1 and sis != 2:
	print()
X, E = jacobi.jacobi(A=A, b=b, X0=X0, k=par["iteration"], e=par["tol"])

Xx = []
sol0 = []
sol1 = []
sol2 = []
y0 = []
y1 = []
y2 = []
for i in range(0, len(X)):
	Xx.append(i)
	sol0.append(sol[0])
	sol1.append(sol[1])
	y0.append(X[i][0])
	y1.append(X[i][1])
	if sis == 2:
		sol2.append(sol[2])
		y2.append(X[i][2])

plot.plot(Xx, sol0, label="Exata x0")
plot.plot(Xx, sol1, label="Exata x1")
if sis == 2:
	plot.plot(Xx, sol2, label="Exata x2")
plot.plot(Xx, y0, label="Aprox. x0")
plot.plot(Xx, y1, label="Aprox. x1")
if sis == 2:
	plot.plot(Xx, y2, label="Aprox. x2")
plot.plot(Xx, np.absolute(np.subtract(y0, sol0)), label="Dif. x0")
plot.plot(Xx, np.absolute(np.subtract(y1, sol1)), label="Dif. x1")
if sis == 2:
	plot.plot(Xx, np.absolute(np.subtract(y2, sol2)), label="Dif. x2")

plot.legend()
plot.show()

# Gerar os dados da tabela
data = []
for i in range(1, len(X)):  # Itera a partir de 1 para evitar erro de diferença com X[-1]
    x1 = X[i][0]
    x2 = X[i][1]
    erro = np.linalg.norm(X[i] - X[i-1], ord=np.inf)
    if sis == 1:
        data.append(["", x1, x2, erro])
    elif sis == 2:
        x3 = X[i][2]
        data.append(["", x1, x2, x3, erro])

# Criação do DataFrame
if sis == 1:
    df = pd.DataFrame(data, columns=['Iteração', 'x1', 'x2', 'Erro'])
elif sis == 2:
    df = pd.DataFrame(data, columns=['Iteração', 'x1', 'x2', 'x3', 'Erro'])

print(df)