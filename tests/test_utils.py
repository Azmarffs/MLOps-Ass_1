from src.utils.helpers import normalize_list


def test_normalize_list_empty():
    assert normalize_list([]) == []


def test_normalize_list_constant():
    assert normalize_list([5, 5, 5]) == [0.0, 0.0, 0.0]


def test_normalize_list_varied():
    assert normalize_list([0, 5, 10]) == [0.0, 0.5, 1.0]

