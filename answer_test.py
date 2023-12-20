import answer


def test_answered():
    assert not answer.answer()


def test_answer():
    assert answer.answer() == 31875000
