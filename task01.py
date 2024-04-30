from time import perf_counter_ns
from functools import wraps
import random


# Декоратор для замера скорости работы функции
def timer(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start = perf_counter_ns()
        result = function(*args, **kwargs)
        end = perf_counter_ns()
        time_taken = end - start
        wrapper.executed_time.append(time_taken)
        print(f'Функция {function.__name__} с аргументом {args[0]} отработала за {time_taken} наносекунд')
        return result

    wrapper.executed_time = []
    return wrapper


# Обычная реализация, когда мы смотрим на остаток от деления на 2
# Плюсы: легко читается -> сразу понятно, что проверяется четность числа
# Минусы: может долго работать
@timer
def isEven(value) -> bool:
    return value % 2 == 0


# Реализация, через побитовое И с единицей. Если при этой операции получается 0,
# то в младшем бите стоит 0, значит число четное.
# Плюсы: чаще работает быстро из-за быстрых побитовых операций
# Минусы: не сразу очевидно, что проверяется четность числа -> не так легко читается, как предыдущий метод
@timer
def anotherIsEven(value) -> bool:
    return value & 1 == 0


def main():
    # Результаты сравнения производительностей двух функций
    results = {'isEven': 0, 'anotherIsEven': 0}
    tests_num = 100

    for i in range(tests_num):
        not_big_value = random.randint(0, 1 << 42)
        big_value = random.randint(1 << 42, 1 << 100)

        assert isEven(not_big_value) == anotherIsEven(not_big_value)
        assert isEven(big_value) == anotherIsEven(big_value)

    for i in range(2 * tests_num):
        if isEven.executed_time[i] == anotherIsEven.executed_time[i]:
            results['isEven'] += 1
            results['anotherIsEven'] += 1
        elif isEven.executed_time[i] < anotherIsEven.executed_time[i]:
            results['isEven'] += 1
        else:
            results['anotherIsEven'] += 1

    print(results)


if __name__ == '__main__':
    main()
