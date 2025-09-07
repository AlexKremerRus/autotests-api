from typing import Any, Sized

import allure
from tools.logger import get_logger  # Импортируем функцию для создания логгера

logger = get_logger("BASE_ASSERTIONS")


@allure.step("Проверка что статус ответа эквивалентен {expected}")
def assert_status_code(actual:int, expected: int):
    logger.info(f"Проверка статуса кода ответа {expected}")
    assert actual == expected, f"Статус код некорректный. Ожидается {expected}, а получаем {actual}"

@allure.step("Проверка что {name} эквивалентна {expected}")
def assert_equal(actual: Any, expected: Any, name: str):
    logger.info(f'Проверка что {name} эквивалентна {expected}')  # Логируем проверку
    assert actual == expected, f"Некорректное значение для {name}, Ожидаемое значение {expected}, Актуальное значение {actual}  "

@allure.step("Проверка что {name} это верно")
def assert_is_true(actual: Any, name: str):
    """
    Проверяет, что фактическое значение является истинным.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :raises AssertionError: Если фактическое значение ложно.
    """
    logger.info(f'Проверка что {name} это верно')
    assert actual, (
        f'Incorrect value: "{name}". '
        f'Expected true value but got: {actual}'
    )


def assert_length(actual: Sized, expected: Sized, name:str):
    with allure.step(f"Проверка что длина {name} эквивалентна {len(expected)}"):
        logger.info(f'Проверка что длина {name} эквивалентна {len(expected)}')
        assert len(actual) == len(expected), f"Некорректная длина объекта {name}, Ожидаемая длина {len(expected)}, Фактическая длина {len(actual)} "