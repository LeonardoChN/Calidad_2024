from ejercicio1 import CalculoIvaProductos
from ejercicio1 import ListaProductos


Calc=CalculoIvaProductos()

LstPrd=ListaProductos()

assert Calc.calculoIva(100)==19,"error en el iva"
assert Calc.calculoIva(200)==38,"error en el iva"
assert Calc.calculoIva(1000)==190,"error en el iva"

assert Calc.montoConIva(100)==119,"error en iva"

# -------------------------------
assert LstPrd.entradaDatos()==True,"Error en el proceso de entrada de datos"

#probaremos ingresando 5 productos
LstPrd.Pantalla()

assert LstPrd.getLista().count()==5