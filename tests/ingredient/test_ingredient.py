from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient1 = Ingredient('frango')
    ingredient2 = Ingredient('arroz')

    assert isinstance(ingredient1, Ingredient)
    assert ingredient1.name == 'frango'
    assert ingredient1.restrictions == {
        Restriction.ANIMAL_MEAT, Restriction.ANIMAL_DERIVED
    }

    assert hash(ingredient1) == hash(ingredient1)
    assert ingredient1 == ingredient1

    assert repr(ingredient1) == "Ingredient('frango')"
    assert hash(ingredient1) != hash(ingredient2)
    assert ingredient1 != ingredient2
