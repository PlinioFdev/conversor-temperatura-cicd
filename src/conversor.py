"""Conversor de temperatura entre Celsius, Fahrenheit e Kelvin."""

ZERO_KELVIN_EM_CELSIUS = -273.15


def celsius_para_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32


def fahrenheit_para_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


def celsius_para_kelvin(celsius: float) -> float:
    if celsius < ZERO_KELVIN_EM_CELSIUS:
        raise ValueError("Temperatura abaixo do zero absoluto")
    return celsius - ZERO_KELVIN_EM_CELSIUS


def kelvin_para_celsius(kelvin: float) -> float:
    if kelvin < 0:
        raise ValueError("Kelvin não pode ser negativo")
    return kelvin + ZERO_KELVIN_EM_CELSIUS


def celsius_para_rankine(celsius: float) -> float:
    return celsius_para_kelvin(celsius) * 9 / 5


def converter(valor: float, origem: str, destino: str) -> float:
    origem = origem.upper()
    destino = destino.upper()
    unidades = ("C", "F", "K")
    if origem not in unidades or destino not in unidades:
        raise ValueError("Unidade inválida. Use C, F ou K")

    if origem == destino:
        return valor

    # normaliza tudo para Celsius primeiro, depois converte para o destino
    if origem == "F":
        celsius = fahrenheit_para_celsius(valor)
    elif origem == "K":
        celsius = kelvin_para_celsius(valor)
    else:
        celsius = valor

    if destino == "F":
        return celsius_para_fahrenheit(celsius)
    if destino == "K":
        return celsius_para_kelvin(celsius)
    return celsius


if __name__ == "__main__":
    print(converter(100, "C", "F"))
