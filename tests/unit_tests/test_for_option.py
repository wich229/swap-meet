import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics


def test_swap_clothing_items_by_fabric():
    # Arrange
    item_a = Clothing(id=321, fabric="strip")
    item_b = Decor(id=654)
    tai = Vendor(
        inventory=[item_a, item_b]
    )

    item_d = Clothing(id=323, fabric="strip")
    item_e = Decor(id=654)
    jesse = Vendor(
        inventory=[item_d, item_e]
    )

    # Act
    result = tai.swap_clothing_items_by_fabric(jesse, item_a, item_d)

    # Assert
    assert result == True
    assert len(tai.inventory) == 2
    assert len(jesse.inventory) == 2
    assert item_d in tai.inventory
    assert item_a in jesse.inventory
    
def test_swap_electronics_items_by_type():
    # Arrange
    item_a = Electronics(id=456, type="phone")
    item_b = Decor(id=654)
    tai = Vendor(
        inventory=[item_a, item_b]
    )

    item_d = Electronics(id=789, type="camera")
    item_e = Decor(id=654)
    jesse = Vendor(
        inventory=[item_d, item_e]
    )

    # Act
    result = tai.swap_electronics_items_by_type(jesse, item_a, item_d)

    # Assert
    assert result == False
    assert len(tai.inventory) == 2
    assert len(jesse.inventory) == 2
    assert item_d not in tai.inventory
    assert item_a not in jesse.inventory
    
    
def test_correct_space_for_decor_product():
    # Arrange
    item = Decor(id=889, width = 5, length = 5)

    # Act
    result = item.get_space()

    # Assert
    assert result == 25.00

def test_swap_electronics_items_by_type():
    # Arrange
    item_b = Decor(id=897, width = 5, length = 5)
    tai = Vendor(
        inventory=[item_b]
    )
    
    item_e = Decor(id=5678, width = 5, length = 5)
    jesse = Vendor(
        inventory=[item_e]
    )

    # Act
    result = tai.swap_decor_items_by_space(jesse, item_b, item_e)

    # Assert
    assert result == True
    assert len(tai.inventory) == 1
    assert len(jesse.inventory) == 1
    assert item_e in tai.inventory
    assert item_b in jesse.inventory
