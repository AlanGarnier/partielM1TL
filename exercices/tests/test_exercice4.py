import pytest


def search_in_list(lst, item):
    return item in lst


@pytest.mark.parametrize(
    "lst, item, expected",
    [([1, 2, 3, 4, 5], 3, True), ([1, 2, 3, 4, 5], 10, False), ([], 6)],
)
def test_search_in_list(lst, item, expected):
    assert search_in_list(lst, item) == expected
