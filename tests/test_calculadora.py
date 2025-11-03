import pytest
from calculadora_organizada import Calculadora


def test_sum():
    app = Calculadora()
    # Configura uma expressao simples de soma
    app.expressao = "2+3"
    app.calcular()
    assert app.valor_texto.get() == "5"


def test_division_by_zero():
    app = Calculadora()
    # Configura divisao por zero para testar tratamento de erro
    app.expressao = "5/0"
    app.calcular()
    assert "Erro" in app.valor_texto.get()
