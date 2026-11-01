import pytest
from src.inventory import Inventory


def test_add_stock():
    inv = Inventory()
    inv.add_stock('apple', 10)
    assert inv.stock['apple'] == 10
    inv.add_stock('apple', 5)
    assert inv.stock['apple'] == 15


def test_remove_stock():
    inv = Inventory()
    inv.add_stock('apple', 10)
    inv.remove_stock('apple', 4)
    assert inv.stock['apple'] == 6


def test_remove_stock_insufficient():
    inv = Inventory()
    inv.add_stock('apple', 3)
    with pytest.raises(ValueError, match='not enough stock'):
        inv.remove_stock('apple', 5)
