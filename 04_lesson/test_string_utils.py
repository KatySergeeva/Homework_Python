import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# Принимает на вход текст, делает первую букву заглавной
# и возвращает этот же текст


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("Hello world", "Hello world"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# Принимает на вход текст и удаляет пробелы в начале, если они есть


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),
    (" 456", "456"),
    ("   python", "python"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    (" 1 2 3 ", "1 2 3 "),
    ("", ""),
    (" ", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# Возвращает `True`, если строка содержит искомый символ и `False` - если нет

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol ", [
    (" skypro", "s"),
    (" 12345", "3"),
    (" !@#$%", "$"),

])
def test_contains_positive(input_str, symbol):
    assert string_utils.contains(input_str, symbol)


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol", [
    ("skypro", "w"),
    ("", " "),
    ("", "a"),

])
def test_contains_negative(input_str, symbol):
    assert string_utils.contains(input_str, symbol) is False


# Удаляет все подстроки из переданной строки

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("21 june 2025", "21 ", "june 2025"),

])
def test_delete_symbols_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "a", "SkyPro"),
    ("   ", "", "   "),
    ("SkyPro", "!", "SkyPro"),
    ("", " ", ""),

])
def test_delete_symbols_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected