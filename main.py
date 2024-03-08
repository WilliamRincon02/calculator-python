def addition(num1, num2):
    return num1 + num2

def substract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if(num2 == 0):
        return "Error: Division entre 0"
    else:
        return num1/num2

print("Seleccione una opcion:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")

operation = input("Ingrese el numero de la operacion que desea realizar: ")

if(operation in ['1','2','3','4']):
    try:
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
    except:
        print("Entrada no valida los datos ingresados deben de ser valores numericos")
    else:
        if operation == '1':
            print(num1, "+", num2, "=", addition(num1, num2))
        elif operation == '2':
            print(num1, "-", num2, "=", substract(num1, num2))
        elif operation == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif operation == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Seleccione una operacion valida")