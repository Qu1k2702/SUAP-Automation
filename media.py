def converter_notas(nota: str):
    nota = nota.strip()

    if nota == "-":
        return None
    
    return float(nota.replace(",","."))