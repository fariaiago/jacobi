def welcomeUser():
	print("Olá, bem vindo!\n")
	print("Primeiramente, você pode escolher resolver um sistema 2x2 ou 3x3\n")
	print("Lembre-se que, sistemas 2x2 são:\n a11x1 + a12x2 = b1\n a21x1 + a22x2 = b2")
	print("\nJá sistemas 3x3: \n a11x1 + a12x2 + a13x3 = b1 \n a21x1 + a22x2 + a23x3 = b2 \n a31x1 + a32x2 + a33x3 = b3")
	choice = int(input("\nDigite [1] para sistema 2x2 ou [2] para sistema 3x3: "))
	return choice

def userInput(choice):
	if choice == 1:
		a1 = input("Digite o valor de a11 e a12 separados por um espaço: ")
		a11, a12 = map(float, a1.split())
		a2 = input("Digite o valor de a21 e a22, separados por um espaço: ")
		a21, a22 = map(float, a2.split())

		b1 = float(input("Digite o valor de b1: "))
		b2 = float(input("Digite o valor de b2: "))

		tolIteration = input("Defina a tolerância e o número máximo de interações, separados por um espaço: ")
		tol, iteration = tolIteration.split()
		tol = float(tol)
		iteration = int(iteration)

		x = input("Digite os valores iniciais de X, separados por um espaço: ")
		x10, x20 = map(float, x.split())

		s = input("Digite os valores da solução exata, separados por um espaço: ")
		s1, s2 = map(float, s.split())

		fatores = [[a11, a12], [a21, a22]]
		b = [b1, b2]
		parametros = {"tol": tol, "iteration": iteration}
		X0 = [x10, x20]
		solucaoExata = [s1, s2]
	elif choice == 2:
		a1 = input("Digite o valor de a11, a12 e a13, separados por um espaço: ")
		a11, a12, a13 = map(float, a1.split())
		a2 = input("Digite o valor de a21, a22 e a23 separados por um espaço: ")
		a21, a22, a23 = map(float, a2.split())
		a3 = input("Digite o valor de a31, a32 e a33 separados por um espaço: ")
		a31, a32, a33 = map(float, a3.split())

		b1 = float(input("Digite o valor de b1: "))
		b2 = float(input("Digite o valor de b2: "))
		b3 = float(input("Digite o valor de b3: "))

		tolIteration = input("Defina a tolerância e o número máximo de interações, separados por um espaço: ")
		tol, iteration = tolIteration.split()
		tol = float(tol)
		iteration = int(iteration)
		
		x = input("Digite os valores iniciais de X, separados por um espaço: ")
		x10, x20, x30 = map(float, x.split())

		s = input("Digite os valores da solução exata, separados por um espaço: ")
		s1, s2, s3 = map(float, s.split())

		fatores = [[a11, a12, a13], [a21, a22, a23],[a31, a32, a33]]
		b = [b1, b2, b3]
		parametros = {"tol": tol, "iteration": iteration}
		X0 = [x10, x20, x30]
		solucaoExata = [s1, s2, s3]
	else:
		print("Somente dígitos 1 ou 2 são aceitos, por favor tente novamente.")
		return [], [], {}, [], []
	return fatores, b, parametros, X0, solucaoExata

# choice = welcomeUser()
# fatores, parametros, solucao = userInput(choice)
#
# print(fatores)
# print(parametros)
# print(solucao)