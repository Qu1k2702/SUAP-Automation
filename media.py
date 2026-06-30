def converter_notas(nota: str):
    nota = nota.strip()

    if nota == "-":
        return None
    
    return float(nota.replace(",","."))

    
def calcular_media(materia: str, notas: dict):
    notas_validas = [n for n in notas[materia] if n is not None]

    if not notas_validas:
        return f"{materia}: Sem notas"
    
    media = round(sum(notas_validas) / len(notas_validas), 2)

    return f"Materia: {materia} \n Bimestres concluidos: {len(notas_validas)} \n  Media: {media}"