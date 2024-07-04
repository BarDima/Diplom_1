from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger

class TestBurger:
    def setup_method(self):
        self.bun_mock = Mock(spec=Bun)
        self.bun_mock.get_price.return_value = 988
        self.bun_mock.get_name.return_value = 'Флюоресцентная булка R2-D3'

        self.filling_mock = Mock(spec=Ingredient)
        self.filling_mock.get_price.return_value = 1337
        self.filling_mock.get_name.return_value = 'Мясо бессмертных моллюсков Protostomia'
        self.filling_mock.get_type.return_value = 'Начинка'

        self.sauce_mock = Mock(spec=Ingredient)
        self.sauce_mock.get_price.return_value = 90
        self.sauce_mock.get_name.return_value = 'Соус Spicy-X'
        self.sauce_mock.get_type.return_value = 'Соус'

    def test_add_ingredient(self):
        burger = Burger()
        burger.set_buns(self.bun_mock)
        burger.add_ingredient(self.filling_mock)
        burger.add_ingredient(self.sauce_mock)
        assert burger.ingredients == [self.filling_mock, self.sauce_mock]

    def test_get_price(self):
        burger = Burger()
        burger.set_buns(self.bun_mock)
        burger.add_ingredient(self.filling_mock)
        burger.add_ingredient(self.sauce_mock)
        assert burger.get_price() == 3403

    def test_get_receipt(self):
        burger = Burger()
        burger.set_buns(self.bun_mock)
        burger.add_ingredient(self.filling_mock)
        burger.add_ingredient(self.sauce_mock)  # Add the sauce
        expected_receipt = "(==== Флюоресцентная булка R2-D3 ====)\n= начинка Мясо бессмертных моллюсков Protostomia =\n= соус Соус Spicy-X =\n(==== Флюоресцентная булка R2-D3 ====)\n\nPrice: 3403"
        assert burger.get_receipt() == expected_receipt

    def test_remove_ingredient(self):
        burger = Burger()
        burger.set_buns(self.bun_mock)
        burger.add_ingredient(self.filling_mock)
        burger.add_ingredient(self.sauce_mock)
        burger.remove_ingredient(0)
        assert burger.ingredients == [self.sauce_mock]
