import pytest

def test_status_code(get_req):
    assert get_req == 200