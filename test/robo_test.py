
# TODO: import some code

from app.robo import request_data

# TODO: test the code

def test_request_data():
    keys = list(request_data("GOOGL").keys())
    assert "Meta Data" in keys
    assert "Time Series (Daily)" in keys
