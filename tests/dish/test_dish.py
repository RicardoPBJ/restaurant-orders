from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501
import pytest


# Req 2
def test_dish():
    dish1 = Dish('churrasco', 10.0)
    ingredient = Ingredient('carne')
    dish1.add_ingredient_dependency(ingredient, 2)

    dish2 = Dish('batata frita', 10.0)

    assert dish1.name == 'churrasco'
    assert repr(dish1) == "Dish('churrasco', R$10.00)"
    assert hash(dish1) == hash(dish1)
    assert dish1 == dish1

    assert hash(dish1) != hash(dish2)
    assert dish1 != dish2

    with pytest.raises(TypeError):
        Dish("churrasco", "10.0")

    with pytest.raises(ValueError):
        Dish("churrasco", 0.0)

    assert dish1.recipe.get(ingredient) == 2
    assert dish1.get_restrictions() == {
        Restriction.ANIMAL_MEAT, Restriction.ANIMAL_DERIVED
    }
    assert dish1.get_ingredients() == {ingredient}

    assert True
