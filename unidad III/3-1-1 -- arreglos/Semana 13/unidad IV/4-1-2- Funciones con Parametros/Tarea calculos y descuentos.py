####
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento/100)
    return descuento

if __name__ == "__main__":
    vivienda1 = 2380
    moto2 = 1845

    ##llamada
    descuento = calcular_descuento(vivienda1)
    print(f"monto de mi compra es {vivienda1}, el descuento es {descuento}")

##### llamada 2
    descuento2 = calcular_descuento(moto2,)
    print(f"monto de mi compra es {moto2}, el descuento es {descuento2}")