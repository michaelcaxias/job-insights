from src.jobs import read


def get_unique_job_types(path):
    all_jobs = read(path)

    no_repeated_jobs = set()

    for row in all_jobs:
        no_repeated_jobs.add(row["job_type"])

    return no_repeated_jobs


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []
    for job in jobs:
        if job_type == job['job_type']:
            filtered_jobs.append(job)
    return filtered_jobs


def get_unique_industries(path):
    all_jobs = read(path)

    no_repeated_industries = set()

    for row in all_jobs:
        if row["industry"] != '':
            no_repeated_industries.add(row["industry"])

    return no_repeated_industries


def filter_by_industry(jobs, industry):
    filtered_industry = []
    for job in jobs:
        if industry == job['industry']:
            filtered_industry.append(job)
    return filtered_industry


def get_max_salary(path):
    all_jobs = read(path)

    max_salary = []

    for row in all_jobs:
        # https://www.delftstack.com/howto/python/python-check-if-character-is-number/#:~:text=the%20conditional%20statement.-,Use%20the%20isdigit()%20Method%20to%20Check%20if%20a%20Given,in%20the%20scope%20of%20digits.
        if row["max_salary"] != '' and row["max_salary"].isdigit():
            max_salary.append(int(row["max_salary"]))

    return max(max_salary)


def get_min_salary(path):
    all_jobs = read(path)

    min_salary = []

    for row in all_jobs:
        # https://www.delftstack.com/howto/python/python-check-if-character-is-number/#:~:text=the%20conditional%20statement.-,Use%20the%20isdigit()%20Method%20to%20Check%20if%20a%20Given,in%20the%20scope%20of%20digits.
        if row["min_salary"] != '' and row["min_salary"].isdigit():
            min_salary.append(int(row["min_salary"]))

    return min(min_salary)


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
