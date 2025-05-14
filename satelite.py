altitud_inicial = float(input("Ingresa la altitud inicial del satelite en kilometros: "))
coeficiente_arrastre = float(input("Ingresa el coeficiente de arrastre inicial (un numero decimal muy pequeño): "))
altitud_min_seg = float(input("Ingresa la altitud minima de seguridad en kilometros: "))

altitud_actual = altitud_inicial
orbita = 0

print("Simulando la desintegración orbital...")

while altitud_actual > altitud_min_seg:
    altitud_perdida = coeficiente_arrastre * altitud_actual
    altitud_actual = altitud_actual - altitud_perdida
    coeficiente_arrastre += 0.0001
    orbita += 1
    print("orbita: ", orbita, "Altitud actual =", round(altitud_actual,4), "km", "Coeficiente de arrastre =", round(coeficiente_arrastre,4),altitud_perdida)
    if altitud_perdida < 0.01:
        break

print(f"El satélite ha reingresado en la atmósfera terrestre después de {orbita} órbitas.")