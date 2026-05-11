import math
import statistics

def media(data: list[float]) -> float:
    if not data:
        raise ValueError("La lista no puede estar vacía")
    return statistics.mean(data)

def mediana(data: list[float]) -> float:
    if not data:
        raise ValueError("La lista no puede estar vacía")
    return statistics.median(data)

def desviacion_estandar(data: list[float]) -> float:
    if not data:
        raise ValueError("La lista no puede estar vacía")
    return statistics.pstdev(data)