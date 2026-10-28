import pytest

from src.conversor import (
    celsius_para_fahrenheit,
    fahrenheit_para_celsius,
    celsius_para_kelvin,
    kelvin_para_celsius,
    converter,
)


def test_celsius_para_fahrenheit():
    assert celsius_para_fahrenheit(0) == 32
    assert celsius_para_fahrenheit(100) == 212


def test_fahrenheit_para_celsius():
    assert fahrenheit_para_celsius(32) == 0
    assert fahrenheit_para_celsius(212) == 100


def test_celsius_para_kelvin():
    assert celsius_para_kelvin(0) == pytest.approx(273.15)


def test_kelvin_para_celsius():
    assert kelvin_para_celsius(273.15) == pytest.approx(0)


def test_kelvin_negativo_gera_erro():
    with pytest.raises(ValueError):
        kelvin_para_celsius(-1)


def test_celsius_abaixo_zero_absoluto_gera_erro():
    with pytest.raises(ValueError):
        celsius_para_kelvin(-300)


def test_converter_mesma_unidade():
    assert converter(25, "C", "C") == 25


def test_converter_celsius_para_fahrenheit():
    assert converter(0, "C", "F") == 32


def test_converter_fahrenheit_para_kelvin():
    assert converter(32, "F", "K") == pytest.approx(273.15)


def test_converter_unidade_invalida_gera_erro():
    with pytest.raises(ValueError):
        converter(10, "C", "X")
