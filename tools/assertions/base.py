from typing import Any

def assert_status_code(actual:int, expected: int):
    assert actual == expected, f"Статус код некорректный. Ожидается {expected}, а получаем {actual}"

def assert_equal(actual: Any, expected: Any, name: str):
    assert actual == expected, f"Некорректное значение для {name}, Ожидаемое значение {expected}, Актуальное значение {actual}  "
