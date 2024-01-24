class FlatIterator:

    def __init__(self, list_of_lists):

        self.flat_list = self.flatten_list(list_of_lists)
        self.index = 0

    def __iter__(self):

        return self

    def __next__(self):

        if self.index < len(self.flat_list):
            result = self.flat_list[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

    def flatten_list(self, list_):

        flat = []

        for element_ in list_:
            if isinstance(element_, list):
                flat.extend(self.flatten_list(element_))
            else:
                flat.append(element_)

        return flat


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
