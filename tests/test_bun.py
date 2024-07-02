import pytest
from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize("name, price", [
        ('Флюоресцентная булка R2-D3', 988),
        ('Краторная булка N-200i', 1255),
    ])
    def test_bun_parameters(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price
