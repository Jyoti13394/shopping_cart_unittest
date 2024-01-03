from shopping import ShoppingCart
import pytest

@pytest.fixture()
def cart():
    return ShoppingCart(5)


def test_item_in_cart(cart):
    cart.add("apple")
    assert cart.size_of_cart() == 1


def test_if_item_is_added_to_cart(cart):
    cart.add("apple")
    assert "apple" in cart.get_items()


def test_if_number_of_items_exceed_max_size(cart):
    for _ in range(5):
        cart.add("apple")
    with pytest.raises(OverflowError):
        cart.add("apple")


def test_can_get_total_price(cart):
    cart.add("apple")
    cart.add("orange")
    price_map = {
        "apple": 1.0,
        "orange": 3.0
    }
    assert cart.get_total_price(price_map) == 4.0



