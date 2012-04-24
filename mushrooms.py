def transpose(ls):
    return zip(*ls)

def make_input_list(filename):
    return [line.strip().split(",") for line in open(filename)]

def collect_groups(input_list):
    return [list(sorted(set(group)))
            for group in transpose(input_list)]

def get_singleton_indices(ls):
    return [i
            for i, each in enumerate(ls)
            if len(each) < 2]

def get_options_count(groups):
    return map(len, groups)

def indices(input_list, groups):
    return [[group.index(word)
             for group, word in zip(groups, row)]
            for row in input_list]

def test_running():
    input_list = [[1, 2, 3, 4, 5, 4, 6],
                  [2, 1, 2, 4, 3, 6, 4],
                  [3, 1, 1, 4, 2, 4, 3]]
    groups = collect_groups(input_list)
    assert groups == [[1, 2, 3],
                      [1, 2],
                      [1, 2, 3],
                      [4],
                      [2, 3, 5],
                      [4, 6],
                      [3, 4, 6]]
    assert len(input_list[0]) == len(groups)
    old_length = len(input_list[0])
    for i in reversed(get_singleton_indices(groups)):
        for row in input_list + [groups]:
            row.pop(i)
    assert len(input_list[0]) == len(groups) == old_length - 1
    ixs = indices(input_list, groups)
    assert ixs == [[0, 1, 2, 2, 0, 2],
                   [1, 0, 1, 1, 1, 1],
                   [2, 0, 0, 0, 0, 0]]

def test_get_singleton_indices():
    assert get_singleton_indices([[1, 2], [3], [4, 5, 4], [6]]) == [1, 3]

def test():
    test_get_singleton_indices()
    test_running()

test()
