#
# Стандартные алгоритмы сортировки за `n⋅log(n)` могут на некоторых входных данных работать медленно.
# Невыгодно запускать такие сортировки, например, на маленьких входных данных.
# На мой взгляд, лучшим решением данной проблемы является предварительный анализ входных данных,
# на основе которого уже и запускать конкретный алгоритм. На маленьких входных данных быстрее всего
# отработает `insertion sort`. Если глубина рекурсии становится слишком большой, то нужно переходить
# на `heap sort`. Также еще необходимо знать, нужна стабильная сортировка или нет.
# Но в любом случае, кажется, что лучшим вариантом будет обратиться к научным исследованиям из этой
# области. А именно воспользоваться готовыми алгоритмами, которые как раз и проводят "оценку"
# входных данных и сортируют уже на ее основе. Ресерч по этой теме показал, что на данный момент
# наиболее успешные алгоритмы -- это `Timsort` и `Powersort`.
#
def main():
    return


if __name__ == '__main__':
    main()
