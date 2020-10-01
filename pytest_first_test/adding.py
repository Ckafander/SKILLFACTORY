import pytest
from app.calculator import calculator


class TestCalc:
    def setup (self):
        self.calc = calculator


    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 2, 2) == 4

    def test_adding_calculate_failed(self):
        assert self.calc.adding(self, 2, 2) == 5
