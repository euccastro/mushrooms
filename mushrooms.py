from itertools import chain

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

def remove_indices(ls, ixs):
    for i in sorted(ixs, reverse=True):
        ls.pop(i)

def get_options_count(groups):
    return map(len, groups)

def indices(input_list, groups):
    return [[group.index(word)
             for group, word in zip(groups, row)]
            for row in input_list]

def one_to_many(row, group_counts):
    return list(chain.from_iterable(
        [int(index==row_index)
         for index in xrange(gc)]
        for row_index, gc in zip(row, group_counts)))

def prep(filename):
    input_list = make_input_list(filename)
    groups = collect_groups(input_list)
    singleton_indices = get_singleton_indices(groups)
    for row in input_list + [groups]:
        remove_indices(row, singleton_indices)
    ixs = indices(input_list, groups)
    gc = get_options_count(groups)
    return [one_to_many(row, gc)
            for row in ixs]

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
    singleton_indices = get_singleton_indices(groups)
    for row in input_list + [groups]:
        remove_indices(row, singleton_indices)
    assert len(input_list[0]) == len(groups) == old_length - 1
    ixs = indices(input_list, groups)
    assert ixs == [[0, 1, 2, 2, 0, 2],
                   [1, 0, 1, 1, 1, 1],
                   [2, 0, 0, 0, 0, 0]]
    gc = get_options_count(groups)
    assert gc == [3, 2, 3, 3, 2, 3]
    otm = [one_to_many(row, gc)
           for row in ixs]
    assert otm == [[1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1],
                   [0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0],
                   [0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0]]

def test_get_singleton_indices():
    assert get_singleton_indices([[1, 2], [3], [4, 5, 4], [6]]) == [1, 3]

def test():
    test_get_singleton_indices()
    test_running()
    print "All OK."

test()
