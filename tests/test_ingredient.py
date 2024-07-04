import pytest
from praktikum.ingredient import Ingredient

class TestIngredient:
    @pytest.mark.parametrize("ingredient_type, name, price", [
        ('Соус', 'Соус фирменный Space Sauce', 80),
        ('Соус', 'Соус Spicy-X', 90),
        ('Начинка', 'Мясо бессмертных моллюсков Protostomia', 1337),
    ])
    def test_ingredient_attributes(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price


