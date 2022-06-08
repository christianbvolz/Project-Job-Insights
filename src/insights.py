from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    job_types = []
    for job in jobs:
        if not job["job_type"] in job_types:
            job_types.append(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)
    return filtered_jobs


def get_unique_industries(path):
    jobs = read(path)
    industries = []
    for job in jobs:
        if job["industry"] != "" and not job["industry"] in industries:
            industries.append(job["industry"])
    return industries


def filter_by_industry(jobs, industry):
    filtered_jobs = []
    for job in jobs:
        if job["industry"] == industry:
            filtered_jobs.append(job)
    return filtered_jobs


def get_max_salary(path):
    jobs = read(path)
    max_salary = 0
    for job in jobs:
        if job["max_salary"].isnumeric():
            job_salary = float(job["max_salary"])
            if job_salary > max_salary:
                max_salary = job_salary
    return max_salary


def get_min_salary(path):
    jobs = read(path)
    min_salary = 0
    for job in jobs:
        if job["min_salary"].isnumeric():
            job_salary = float(job["min_salary"])
            if job_salary < min_salary or min_salary == 0:
                min_salary = job_salary
    return min_salary


def matches_salary_range(job, salary):
    try:
        if int(job["min_salary"]) > int(job["max_salary"]):
            raise ValueError("max_salary less than min_salary")
        range = int(job["min_salary"]) <= salary <= int(job["max_salary"])
        return range
    except(TypeError, KeyError):
        raise ValueError


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
