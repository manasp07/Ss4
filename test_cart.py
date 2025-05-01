import pytest
from cart import Cart

def test_add_item():
    cart = Cart()
    cart.add_item("Apple", 3)
    cart.add_item("Apple", 2)
    assert cart.get_quantity("Apple") == 5
    print("✅ Apple added with total quantity 5")

def test_update_item():
    cart = Cart()
    cart.add_item("Banana", 2)
    cart.update_item("Banana", 6)
    assert cart.get_quantity("Banana") == 6
    print("✅ Banana updated to quantity 6")

def test_remove_item():
    cart = Cart()
    cart.add_item("Orange", 4)
    cart.remove_item("Orange")
    assert not cart.contains_product("Orange")
    print("✅ Orange removed from cart")

def test_get_quantity_when_product_not_present():
    cart = Cart()
    assert cart.get_quantity("Milk") == 0
    print("✅ Milk not in cart, quantity is 0")

def test_contains_product():
    cart = Cart()
    cart.add_item("Bread", 1)
    assert cart.contains_product("Bread")
    assert not cart.contains_product("Butter")
    print("✅ Bread present, Butter not present")

# ❌ A test case designed to fail
def test_failure_case():
    cart = Cart()
    cart.add_item("FailItem", 1)
    assert cart.get_quantity("FailItem") == 99  # Incorrect on purpose
    print("❌ This test should fail")
