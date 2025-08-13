import pytest
from _pytest.fixtures import SubRequest

@pytest.mark.parametrize("number_1, number_2" ,[(1,0),(2,0),(2,7)])
def test_1(number_1: int,number_2: int):
    assert number_1>number_2


@pytest.fixture(params=["dev", "stage", "prod"])
def host(request: SubRequest)->str:
    return request.param

def test_host(host:str):
    print(host)