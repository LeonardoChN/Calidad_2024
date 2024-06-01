class calculo_iva ():
    def Pantalla():
        print ("Ingrese producto: ")
        Producto1 = input()
        print ("Ingrese producto valor sin iva del producto: ")
        Valor1 = int(input())
        print ("Ingrese cantidad del producto que lleva: ")
        Cantidad1 = int(input())
        return(Producto1, Valor1, Cantidad1)

    def Calcular_iva(Valor1, Cantidad1):
        Total_sin_iva = Valor1 * Cantidad1
        Iva = Total_sin_iva * 0.19  # Calcula el IVA 19%
        Total_con_iva = Total_sin_iva + Iva
        return (Total_sin_iva, Iva, Total_con_iva)

    def Mostrar_resultados(Producto1, Valor1, Cantidad1, Total_sin_iva, Iva, Total_con_iva):
        print("\nResumen del producto:")
        print("Producto:", Producto1)
        print("Cantidad:", Cantidad1)
        print("Valor:", Valor1)
        print("Total sin IVA:", Total_sin_iva)
        print("IVA:", Iva)
        print("Total con IVA:", Total_con_iva)

    producto, valor, cantidad = Pantalla()
    total_sin_iva, iva, total_con_iva = Calcular_iva(valor, cantidad)
    Mostrar_resultados(producto, cantidad, valor, total_sin_iva, iva, total_con_iva)

