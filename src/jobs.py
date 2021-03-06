from functools import lru_cache
import csv


@lru_cache
def read(path):
    all_jobs = []
    with open(path, encoding="UTF-8") as jobs:
        jobs_list = csv.DictReader(jobs)
        for row in jobs_list:
            all_jobs.append(row)
    return all_jobs
