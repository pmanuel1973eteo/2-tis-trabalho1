def lerFloat():
    while True:
        user_input = input("Escreva um numero: ")
        try:
            float_value = float(user_input)
            #print("Entered number as float:", float_value)
            break # Exit the loop if the conversion was successful
        except ValueError:
            print("Por favor escreva um número válido.(ex: 10 ou 2.56)")
            # The loop continues to prompt for valid input
    return float_value

print("CALCULADORA TIS")
num1 = lerFloat()

num2 = lerFloat()

op = input ('indica uma operacao (+, -, *, :):')
print("")

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1-num2)
elif op == '*':
    print(num1 * num2)
elif op == ':':    
    print(num1/num2)
else:
    print('ERRO')
