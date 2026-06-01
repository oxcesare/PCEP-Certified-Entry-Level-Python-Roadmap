#Practica de control de Ventas semanales

#Debes controlar las ventas de 3 productos durante los primeros 3 días de la semana (Lunes, Martes y Miércoles).

#Vectores: Declara un vector que contenga los nombres: "Laptop", "Smartphone", "Tablet".
#Matrices: Declara una matriz de 3x3 (3 productos x 3 días) inicializada en cero.

#Captura de datos
def calcualrVentas():
    #Vector de productos
    productos = ["Laptop", "Smartphone", "Tablet"]
    #matriz de  3x3 Declara una matriz de 3x3 (3 productos x 3 días) inicializada en cero.
    ventas = [[0] * 3 for _ in range(3)]

    # Lectura de datos
    for i in range(3):
        print(f"--- Registro para {productos[i]} ---")
        for j in range(3):
            ventas[i][j] = int(input(f"Ventas del día {j + 1}: "))

    # Escritura y Reporte
    print("\nRESUMEN DE VENTAS")
    total_general = 0
    totales_por_producto = []

    for i in range(3):
        suma_producto = sum(ventas[i])
        print(f"ventas[i]: i:  {i}  {ventas[i]}")# suma los 3 días del producto i
        totales_por_producto.append(suma_producto)
        total_general += suma_producto
        print(f"{productos[i]}: {ventas[i]} | Total: {suma_producto}")

    print(f"\nEl total de ventas de la semana es: {total_general}")
    print(f"El promedio de ventas es: {total_general / 9:.2f}")

    # Producto más vendido usando el total de los 3 días
    indice_max = totales_por_producto.index(max(totales_por_producto))
    print(f"El producto más vendido de la semana es: {productos[indice_max]} con {totales_por_producto[indice_max]} ventas")

def main():
    calcualrVentas()

if __name__ == "__main__":
    main()