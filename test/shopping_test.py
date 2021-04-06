
# TODO: import some code

import os
from pandas import read_csv
from app.shopping import find_product
from app.number_decorators import format_usd

# TODO: test the code

def test_format_usd():
    assert format_usd(9.5) == "$9.50"


mock_products_filepath = os.path.join(os.path.dirname(__file__), "..", "test", "mock_data", "mock_products.csv")
mock_products_df = read_csv(mock_products_filepath)
mock_products = mock_products_df.to_dict("records")

def test_find_product():
    # if the product id is valid, return product information
    valid_result = find_product("8", mock_products)
    assert valid_result == {
        'aisle': 'Aisle C',
        'department': 'snacks',
        'id': 8,
        'name': 'Product 8',
        'price': 10.0
    }

    # if the product id is invalid, return None
    invalid_result = find_product("189", mock_products)
    assert invalid_result == None
