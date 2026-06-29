notas = {}

def converter_notas(nota: str):
    if nota == "-":
        return None
    
    return float(nota.replace(",","."))

    
def calcular_media_materia(materia: str):
    notas_por_bimestre = []
    nota_total = 0

    for i in notas[materia]:
        notas_por_bimestre.append(i)
        nota_total += i

    media = round(nota_total / len(notas_por_bimestre), 2)

    return f"Materia: {materia} \n Bimestres concluidos: {len(notas_por_bimestre)} \n  Media: {media}"

print(calcular_media_materia("BIO2"))
print("="*30)
print(calcular_media_materia("MAT3"))