precio = 49
txt = "El precio es de  {} pesos"
print(txt.format(precio))

precio = 49
txt = "El precio es de {:.2f} pesos"

print(txt.format(precio))

cantidad= 3
numprod= 567
precio= 49
miorden= "Deseo {} piezas del producto {} de {:.2f} pesos."
print(miorden.format(cantidad, numprod, precio))

cantidad= 3
numprod= 567
precio= 49
miorden= "Deseo {0} piezas del producto {1} de ${2:.2f} pesos."
print(miorden.format(cantidad, numprod, precio))

edad= 36
nombre= "John"
txt = "Su nombre es  {1}. {1} tiene {0} años."
print(txt.format(edad, nombre))