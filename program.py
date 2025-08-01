# Versión 1 - Hola mundo
print("Versión 1: ¡Hola mundo!")

# Versión 2 - Suma de dos números
print("Versión 2: Suma de 5 + 3")
print("Resultado:", 5 + 3)

# Versión 3 - Saludo personalizado
nombre = input("¿Cómo te llamas? ")
print(f"Hola, {nombre} 👋")

# Versión 4 - Suma usando función
def sumar(a, b):
    return a + b

x = int(input("Ingresa un número: "))
y = int(input("Ingresa otro número: "))
print("La suma es:", sumar(x, y))
