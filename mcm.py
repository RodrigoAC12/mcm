class CalculadoraMCM:
    def __init__(self):
        pass

    # Método para calcular el MCD (Máximo Común Divisor) usando el algoritmo de Euclides
    def mcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Método para calcular el MCM
    def mcm(self, a, b):
        return abs(a * b) // self.mcd(a, b)

    # Método para calcular el MCM de una lista de números
    def mcm_lista(self, lista):
        mcm_resultado = lista[0]
        for num in lista[1:]:
            mcm_resultado = self.mcm(mcm_resultado, num)
        return mcm_resultado


# Crear una instancia de la clase
calculadora = CalculadoraMCM()

# Bucle para permitir realizar múltiples cálculos
while True:
    try:
        # Solicitar 3 números al usuario
        numero1 = int(input("Ingresa el primer número: "))
        numero2 = int(input("Ingresa el segundo número: "))
        numero3 = int(input("Ingresa el tercer número: "))

        # MCM de los tres números
        resultado = calculadora.mcm_lista([numero1, numero2, numero3])
        print(f"El MCM de {numero1}, {numero2} y {numero3} es: {resultado}")

        # Preguntar al usuario si desea realizar otro cálculo
        repetir = input("¿Quieres calcular otro MCM? (sí/no): ").lower()
        if repetir != "sí":
            print("¡Hasta luego!")
            break
    except ValueError:
        print("Por favor, ingresa solo números válidos.")

