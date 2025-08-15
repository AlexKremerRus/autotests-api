from typing import Any, Sized

def assert_status_code(actual:int, expected: int):
    assert actual == expected, f"Статус код некорректный. Ожидается {expected}, а получаем {actual}"

def assert_equal(actual: Any, expected: Any, name: str):
    assert actual == expected, f"Некорректное значение для {name}, Ожидаемое значение {expected}, Актуальное значение {actual}  "

def assert_is_true(actual: Any, name: str):
    """
    Проверяет, что фактическое значение является истинным.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :raises AssertionError: Если фактическое значение ложно.
    """
    assert actual, (
        f'Incorrect value: "{name}". '
        f'Expected true value but got: {actual}'
    )


def assert_length(actual: Sized, expected: Sized, name:str):
    assert len(actual) == len(expected), f"Некорректная длина объекта {name}, Ожидаемая длина {len(expected)}, Фактическая длина {len(actual)} "