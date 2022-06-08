from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, encoding="utf-8") as file:
        data = csv.DictReader(file, delimiter=",", quotechar='"')
        dataList = list(data)
    return dataList
