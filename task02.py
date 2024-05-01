from time import perf_counter_ns

class FIFOArray:
    """
    Циклический буфер FIFO на массиве
    """
    def __init__(self, capacity=42):
        """
        Конструктор очереди
        :param capacity: емкость очереди
        """
        self.capacity = capacity
        self.head = 0
        self.tail = 0
        self._size = 0
        self.buffer = []

    def empty(self):
        """
        Проверка на пустоту
        :return: `True`, если очередь пуста
        """
        return self._size == 0

    def size(self):
        """
        Узнать текущий размер
        :return: размер очереди
        """
        return self._size

    def front(self):
        """
        Вернуть первый элемент
        :return: первый элемент очереди
        """
        if self._size > 0:
            return self.buffer[self.head]
        return None

    def back(self):
        """
        Вернуть последний элемент
        :return: последний элемент очереди
        """
        if self._size > 0:
            return self.buffer[(self.tail - 1) % self.capacity]
        return None

    def push_back(self, obj):
        """
        Добавить элемент в конец
        :param obj: добавляемый элемент
        :return: `None`
        """
        if len(self.buffer) < self.capacity:
            self.buffer.append(obj)
        else:
            self.buffer[self.tail] = obj

        self.tail = (self.tail + 1) % self.capacity

        if self._size == self.capacity:
            self.head = (self.head + 1) % self.capacity
        else:
            self._size += 1

    def pop_front(self):
        """
        Удалить элемент из начала очереди
        :return: `None`
        """
        if self._size != 0:
            self.head = (self.head + 1) % self.capacity
            self._size -= 1


class FIFOLinkedList:
    """
    Циклический буфер FIFO на связном списке
    """
    class Node:
        """
        Вспомогательный класс для узлов связного списка
        """
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self, capacity=42):
        """
        Конструктор очереди
        :param capacity: емкость очереди
        """
        self.capacity = capacity
        self.head = self.Node(None)
        self.head.next = self.head
        self.tail = self.head
        self._size = 0

    def empty(self):
        """
        Проверка на пустоту
        :return: `True`, если очередь пуста
        """
        return self._size == 0

    def size(self):
        """
        Узнать текущий размер
        :return: размер очереди
        """
        return self._size

    def front(self):
        """
        Вернуть первый элемент
        :return: первый элемент очереди
        """
        if self._size > 0:
            return self.head.value
        return None

    def back(self):
        """
        Вернуть последний элемент
        :return: последний элемент очереди
        """
        if self._size > 0:
            return self.tail.value
        return None

    def push_back(self, obj):
        """
        Добавить элемент в конец
        :param obj: добавляемый элемент
        :return: `None`
        """
        if self._size == 0:
            self.head.value = obj
            self._size += 1
        elif self._size < self.capacity:
            tmp = self.Node(obj)
            tmp.next = self.head
            self.tail.next = tmp
            self.tail = tmp
            self._size += 1
        else:
            self.tail = self.tail.next
            self.head = self.head.next
            self.tail.value = obj

    def pop_front(self):
        """
        Удалить элемент из начала очереди
        :return: `None`
        """
        if self._size != 0:
            self.head = self.head.next
            self._size -= 1


# Ниже проводятся тесты по добавлению в очередь и удалению из нее для разных реализаций.
# Удаление работает примерно за одинаковое время, но добавление всегда работает
# быстрее для связного списка, поэтому его лучше применять для реализации очереди.
# Это связано с быстрой работой с указателями.
def main():
    tests_num = 10000

    fifo_array = FIFOArray()

    start_FIFOArray_pb = perf_counter_ns()
    for i in range(tests_num):
        fifo_array.push_back(i)
    end_FIFOArray_pb = perf_counter_ns()

    start_FIFOArray_pf = perf_counter_ns()
    for i in range(tests_num):
        fifo_array.pop_front()
    end_FIFOArray_pf = perf_counter_ns()


    fifo_linked_list = FIFOLinkedList()

    start_FIFOLinkedList_pb = perf_counter_ns()
    for i in range(tests_num):
        fifo_linked_list.push_back(i)
    end_FIFOLinkedList_pb = perf_counter_ns()

    start_FIFOLinkedList_pf = perf_counter_ns()
    for i in range(tests_num):
        fifo_linked_list.pop_front()
    end_FIFOLinkedList_pf = perf_counter_ns()

    print(f'Время работы добавления в очередь для реализации на массиве: \
     {end_FIFOArray_pb - start_FIFOArray_pb} наносекунд')
    print(f'Время работы добавления в очередь для реализации на связном списке: \
     {end_FIFOLinkedList_pb - start_FIFOLinkedList_pb} наносекунд')

    print(f'Время работы удаления из очереди для реализации на массиве: \
     {end_FIFOArray_pf - start_FIFOArray_pf} наносекунд')
    print(f'Время работы удаления из очереди для реализации на связном списке: \
     {end_FIFOLinkedList_pf - start_FIFOLinkedList_pf} наносекунд')


if __name__ == '__main__':
    main()
