import solver


def test_solved():
    assert not solver.solver(1000)


def test_solver():
    assert solver.solver(12) == 60
