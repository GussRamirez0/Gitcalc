# Versión 5 - Mini calculadora con menú
def sumar(a, b): return a + b
def restar(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b): return a / b if b != 0 else "No se puede dividir por cero"

print("Calculadora básica")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("Elige una opción: ")
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

if opcion == "1":
    print("Resultado:", sumar(a, b))
elif opcion == "2":
    print("Resultado:", restar(a, b))
elif opcion == "3":
    print("Resultado:", multiplicar(a, b))
elif opcion == "4":
    print("Resultado:", dividir(a, b))
else:
    print("Opción inválida.")
