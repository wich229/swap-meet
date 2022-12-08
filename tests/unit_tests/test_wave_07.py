import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

# ~~~~~ display_inventory Tests ~~~~~

# @pytest.mark.skip
def test_display_inventory_with_items_no_category(capfd):
    # Arrange
    item_a = Clothing(id=123, fabric="Striped")
    item_b = Electronics(id=456, type="Handheld Game")
    item_c = Decor(id=789, width=2, length=4)
    item_d = Item(id=100)
    vendor = Vendor(
        inventory=[item_a, item_b, item_c, item_d]
    )

    # Act
    vendor.display_inventory()

    # Assert
    captured = capfd.readouterr()
    expected_str = (
        "1. An object of type Clothing with id 123. It is made from Striped fabric.\n"
        "2. An object of type Electronics with id 456. This is a Handheld Game device.\n"
        "3. An object of type Decor with id 789. It takes up a 2 by 4 sized space.\n"
        "4. An object of type Item with id 100\n"
    )
    assert captured.out == expected_str

# @pytest.mark.skip
def test_display_inventory_with_items_and_category(capfd):
    # Arrange
    item_a = Decor(id=123, width=2, length=4)
    item_b = Electronics(id=456, type="Handheld Game")
    item_c = Decor(id=789, width=1, length=6)
    vendor = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # Act
    vendor.display_inventory(category="Decor")

    # Assert
    captured = capfd.readouterr()
    expected_str = (
        "1. An object of type Decor with id 123. It takes up a 2 by 4 sized space.\n"
        "2. An object of type Decor with id 789. It takes up a 1 by 6 sized space.\n"
    )
    assert captured.out == expected_str

# @pytest.mark.skip
def test_display_inventory_with_category_and_no_matching_items(capfd):
    # Arrange
    item_a = Decor(id=123, width=2, length=4)
    item_b = Electronics(id=456, type="Handheld Game")
    item_c = Decor(id=789, width=1, length=6)
    vendor = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # Act
    vendor.display_inventory(category="Clothing")

    # Assert
    captured = capfd.readouterr()
    expected_str = (
        "No inventory to display.\n"
    )
    assert captured.out == expected_str

# @pytest.mark.skip
def test_display_inventory_no_items_no_category(capfd):
    # Arrange
    vendor = Vendor(inventory=[])

    # Act
    vendor.display_inventory()

    # Assert
    captured = capfd.readouterr()
    expected_str = (
        "No inventory to display.\n"
    )
    assert captured.out == expected_str

# @pytest.mark.skip
def test_display_inventory_no_items_with_category(capfd):
    # Arrange
    vendor = Vendor(inventory=[])

    # Act
    vendor.display_inventory(category="Decor")

    # Assert
    captured = capfd.readouterr()
    expected_str = (
        "No inventory to display.\n"
    )
    assert captured.out == expected_str

# ~~~~~ swap_by_id Tests ~~~~~

# @pytest.mark.skip
def test_swap_by_id_success_returns_true():
    # Arrange
    item_a = Decor(id=123)
    item_b = Electronics(id=456)
    item_c = Decor(id=789)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(id=321)
    item_e = Decor(id=654)
    item_f = Clothing(id=987)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_id(
        other_vendor=jesse,
        my_item_id=456,
        their_item_id=321
    )

    # Assert
    assert result == True

    assert len(tai.inventory) == 3
    assert item_a in tai.inventory
    assert item_c in tai.inventory
    assert item_d in tai.inventory

    assert len(jesse.inventory) == 3
    assert item_b in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory

# @pytest.mark.skip
def test_swap_by_id_with_caller_empty_inventory_returns_false():
    # Arrange
    tai = Vendor(inventory=[])

    item_d = Clothing(id=321)
    item_e = Decor(id=654)
    item_f = Clothing(id=987)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_id(
        other_vendor=jesse,
        my_item_id=456,
        their_item_id=321
    )

    # Assert
    assert result == False
    assert len(tai.inventory) == 0

    assert len(jesse.inventory) == 3
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory

# @pytest.mark.skip
def test_swap_by_id_with_other_empty_inventory_returns_false():
    # Arrange
    item_a = Decor(id=123)
    item_b = Electronics(id=456)
    item_c = Decor(id=789)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jesse = Vendor(inventory=[])

    # Act
    result = tai.swap_by_id(
        other_vendor=jesse,
        my_item_id=456,
        their_item_id=321
    )

    # Assert
    assert result == False

    assert len(tai.inventory) == 3
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory

    assert len(jesse.inventory) == 0

# @pytest.mark.skip
def test_swap_by_id_fails_if_caller_missing_item():
    # Arrange
    item_a = Decor(id=123)
    item_b = Electronics(id=456)
    item_c = Decor(id=789)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(id=321)
    item_e = Decor(id=654)
    item_f = Clothing(id=987)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_id(
        other_vendor=jesse,
        my_item_id=213,
        their_item_id=654
    )

    # Assert
    assert result == False

    assert len(tai.inventory) == 3
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory

    assert len(jesse.inventory) == 3
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory

# @pytest.mark.skip
def test_swap_by_id_fails_if_other_missing_item():
    # Arrange
    item_a = Decor(id=123)
    item_b = Electronics(id=456)
    item_c = Decor(id=789)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(id=321)
    item_e = Decor(id=654)
    item_f = Clothing(id=987)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_id(
        other_vendor=jesse,
        my_item_id=123,
        their_item_id=564
    )

    # Assert
    assert result == False

    assert len(tai.inventory) == 3
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory

    assert len(jesse.inventory) == 3
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory

# ~~~~~ choose_and_swap_items Tests ~~~~~

# @pytest.mark.skip
def test_choose_and_swap_items_success(monkeypatch):
    # Arrange
    item_a = Decor(id=123)
    item_b = Electronics(id=456)
    item_c = Decor(id=789)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(id=321)
    item_e = Decor(id=654)
    item_f = Clothing(id=987)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Mock user input for picking item ids
    input_responses = iter(["123", "987"])
    monkeypatch.setattr('builtins.input', lambda msg: next(input_responses))

    # Act
    result = tai.choose_and_swap_items(other_vendor=jesse)

    # Assert
    assert result == True

    assert len(tai.inventory) == 3
    assert item_b in tai.inventory
    assert item_c in tai.inventory
    assert item_f in tai.inventory

    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory

# @pytest.mark.skip
def test_choose_and_swap_items_with_calling_inventory_empty(monkeypatch):
    # Arrange
    tai = Vendor(inventory=[])

    item_d = Clothing(id=321)
    item_e = Decor(id=654)
    item_f = Clothing(id=987)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Mock user input for picking item ids
    input_responses = iter(["123", "987"])
    monkeypatch.setattr('builtins.input', lambda msg: next(input_responses))

    # Act
    result = tai.choose_and_swap_items(other_vendor=jesse)

    # Assert
    assert result == False
    assert len(tai.inventory) == 0

    assert len(jesse.inventory) == 3
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory

# @pytest.mark.skip
def test_choose_and_swap_items_with_other_inventory_empty(monkeypatch):
    # Arrange
    item_a = Decor(id=123)
    item_b = Electronics(id=456)
    item_c = Decor(id=789)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jesse = Vendor(inventory=[])

    # Mock user input for picking item ids
    input_responses = iter(["123", "987"])
    monkeypatch.setattr('builtins.input', lambda msg: next(input_responses))

    # Act
    result = tai.choose_and_swap_items(other_vendor=jesse)

    # Assert
    assert result == False

    assert len(tai.inventory) == 3
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory

    assert len(jesse.inventory) == 0

# @pytest.mark.skip
def test_choose_and_swap_items_with_caller_missing_item(monkeypatch):
    # Arrange
    item_a = Decor(id=123)
    item_b = Electronics(id=456)
    item_c = Decor(id=789)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(id=321)
    item_e = Decor(id=654)
    item_f = Clothing(id=987)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Mock user input for picking item ids
    input_responses = iter(["231", "987"])
    monkeypatch.setattr('builtins.input', lambda msg: next(input_responses))

    # Act
    result = tai.choose_and_swap_items(other_vendor=jesse)

    # Assert
    assert result == False

    assert len(tai.inventory) == 3
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory

    assert len(jesse.inventory) == 3
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory

# @pytest.mark.skip
def test_choose_and_swap_items_with_other_vendor_missing_item(monkeypatch):
    # Arrange
    item_a = Decor(id=123)
    item_b = Electronics(id=456)
    item_c = Decor(id=789)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(id=321)
    item_e = Decor(id=654)
    item_f = Clothing(id=987)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Mock user input for picking item ids
    input_responses = iter(["123", "564"])
    monkeypatch.setattr('builtins.input', lambda msg: next(input_responses))

    # Act
    result = tai.choose_and_swap_items(other_vendor=jesse)

    # Assert
    assert result == False

    assert len(tai.inventory) == 3
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory

    assert len(jesse.inventory) == 3
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory