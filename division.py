import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_division_calculate_correctly(self):
        assert self.calc.multiply(self, 4, 2)==2

    def test_division_calculation_failed(self):
        assert self.calc.multiply(self, 4, 4)==0