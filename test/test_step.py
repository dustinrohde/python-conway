from conway import ToroidalArray, step

def test_rule_1():
    '''Any live cell with fewer than 2 live neighbors dies.'''
    t = ToroidalArray([
        [0, 0, 0],
        [0, 1, 1],
        [0, 0, 0]
    ], recursive=True)

    t2 = step(t)
    assert 1 not in t2


def test_rule_2():
    '''Any live cell with 2 or 3 neighbors lives on.'''
    t = ToroidalArray([
        [0, 1, 0],
        [0, 1, 1],
        [0, 0, 0]
    ], recursive=True)

    t2 = step(t)
    assert t2[0][1] == 1
    assert t2[1][1] == 1
    assert t2[1][2] == 1


def test_rule_3():
    '''Any live cell with more than 3 live neighbors dies.'''
    t = ToroidalArray([
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 1],
        [0, 0, 0, 0]
    ], recursive=True)

    t2 = step(t)
    assert t2[1][2] == 0
    assert t2[2][2] == 0


def test_rule_4():
    '''Any dead cell with exactly three live neighbors becomees a live cell.'''
    t = ToroidalArray([
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 1],
    ], recursive=True)

    t2 = step(t)
    assert t2[1][1] == 1