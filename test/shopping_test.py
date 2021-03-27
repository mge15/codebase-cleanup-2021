
# TODO: import some code

from app.shopping import format_usd

# TODO: test the code

def test_format_usd():
    assert format_usd(9.5) == "$9.50"

# TODO: import some code

from app.shopping import find_product

# TODO: test the code

def test_find_product():
    assert find_product(1) == "Aisle A"
    assert find_product(4) == None
    assert find_product(201) == "Aisle B"
    assert find_product(100) == None
