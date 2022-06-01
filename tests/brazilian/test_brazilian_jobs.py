from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    mock_path = 'tests/mocks/brazilians_jobs.csv'
    mock_jobs = read_brazilian_file(mock_path)[0]
    assert ('title' and 'salary' and 'type') in list(mock_jobs)
    assert ('titulo' and 'salario' and 'tipo') not in list(mock_jobs)
