import pytest
from app.calculator import calculator


class TestCalc:
    def setup (self):
        self.calc = calculator


    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 4, 2) == 2

    def test_subtraction_calculate_failed(self):
        assert self.calc.subtraction(self, 4, 2) == 3

