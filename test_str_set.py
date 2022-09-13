import pytest

def test_str_change():
    test_str = "abc"
    try:
        test_str[0] = "w"
        assert test_str == "wbc"
    except TypeError:
        pass

def test_str_sum():
    test_str_1 = "abc"
    test_str_2 = "def"
    assert "abcdef" == test_str_1 + test_str_2

def test_str_format():
    res = "value = abc"
    value = "abc"
    assert "value = {}".format(value) == res

@pytest.mark.parametrize('set_A, set_B, res', [({1,2}, {2,3}, {1,2,3}), ({1,2}, {3,4}, {1,2,3,4}), ({1,2}, set(), {1,2}), (set(), set(), set())])
def test_set_union(set_A, set_B, res):
    assert res == set_A.union(set_B)

def test_set_remove():
    set_A = {1,2}
    set_A.remove(1)
    assert 1 not in set_A

def test_set_clear():
    set_A = {1,2,3}
    set_A.clear()
    assert set() == set_A
