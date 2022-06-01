from src.counter import count_ocurrences


def test_counter():
    assert count_ocurrences('src/jobs.csv', 'word') == 382
    assert count_ocurrences('src/jobs.csv', 'WoRd') == 382
    assert count_ocurrences('src/jobs.csv', 'abelha') == 0
    assert count_ocurrences('src/jobs.csv', 'michael') != 0
    try:
        assert count_ocurrences('src/jobs', 'notebook') != 0
    except FileNotFoundError:
        assert FileNotFoundError

