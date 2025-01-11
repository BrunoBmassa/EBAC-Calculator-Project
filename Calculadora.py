#Exercício Calculadora com condicional

num1 = float(input('Digite o primeiro valor'))
num2 = float(input('Digite o segundo valor'))
opr = input('Escolha qual operação deseja realizar : Soma, Subtração, Multiplicação ou Divisão').lower()
resultado = 0

if opr == 'soma':
  resultado = num1 + num2
  print("A soma de", num1,"+", num2, "é", resultado)
elif opr == 'subtração':
  resultado = num1 - num2
  print("A subtração de", num1,"-", num2, "é", resultado)
elif opr == 'multiplicação':
  resultado = num1 * num2
  print("A multiplicação de", num1,"*", num2, "é", resultado)
else:
  resultado = num1 / num2
  print("A divisão de", num1,"/", num2, "é", resultado)
