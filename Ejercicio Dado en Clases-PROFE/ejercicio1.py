'''
   implemente un codigo en python usando POO o Metodos que permitan
   realizar un pequeño programa
   que, ingresando una lista de productos (nombres,precios sin iva y cantidades)
   calcule:
   - los ivas de cada producto
   - los totales con iva
   - los totales sin iva
   - use el iva del 19%
   usando una clase de unittest, valide que sus metodos estan bien implementados

   Cuantos productos va a ingresar: _1
   ingrese el producto #1
   Nombre del producto: _Manzanas
   precio sin iva del producto: _1000
   cantidad del producto: 10_
   ...
   el iva de la manzana es 190
   los totales con iva son 11900
   los totales sin iva son 10000
   FIN
'''

class CalculoIvaProductos:

    def calculoIva(self,monto):
        return float(monto)*float(0.19)
    
    def montoConIva(self,monto):
        return float(monto)+self.calculoIva(monto)


class ListaProductos:

    def __init__(self):
        self.lista=[]


    def getLista(self):
        return self.lista

    def entradaDatos(self):
        try:
            prd=CalculoIvaProductos()
            nombre=input("ingrese nombre del producto:")
            precio=int(input("ingrese su precio sin iva:"))
            cantidad=int(input("ingrese la cantidad:"))

            dato={'nombre':nombre,'precio':precio,'cantidad':cantidad,'iva':prd.calculoIva(precio)}
            self.lista.append(dato)
            return True
        
        except:
            return False

    def Pantalla(self):
        print("Bienvenidos al Mercadillo")
        print("-------------------------")
        cuantos=int(input("cuantos productos va a ingresar:"))
        for i in range(cuantos):
            self.entradaDatos()


    def salida(self):
        totales=0
        totalsiniva=0
        prd=CalculoIvaProductos()
        for articulo in self.lista:
            print("el iva de la {} es {}".format(articulo["nombre"],articulo["iva"]))

            totales+=prd.montoConIva(articulo["precio"]*articulo["cantidad"])
            totalsiniva=articulo["precio"]*articulo["cantidad"]

        print("los totales con iva son {}".format(totales))
        print("los totales sin iva son {}".format(totalsiniva))