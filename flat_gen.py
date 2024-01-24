import types


def flat_generator(list_of_lists):

    next_index = 0

    while next_index < len(list_of_lists):
        elements_ = list_of_lists[next_index]
        next_index += 1
        for element_ in elements_:
            yield element_

    # альтернативный вариант:
    # return (item for sublist in list_of_lists for item in sublist)


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
