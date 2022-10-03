"""rapsDaily test views

testviews docstring
"""
# test_views.py
#pylint: disable=missing-function-docstring

def test_index_ok(client):
    # Make a GET request to / and store the response object
    # using the Django test client.
    response = client.get('/')
    # Assert that the status_code is 200 (OK)
    assert response.status_code == 200
