import os
from datetime import datetime
from functools import reduce

# Utilizing higher-order functions for side-effect free programming
def date_control(val, dateformat="%d-%m-%Y"):
    try:
        return datetime.strptime(val, dateformat) if isinstance(val, str) else val
    except ValueError:
        return val

def read_csv(file_path, encoding="ISO-8859-1", delimiter=";", dateformat="%d-%m-%Y"):
    if not (os.path.isfile(file_path) and file_path.endswith(".csv")):
        print("File does not exist or is not a CSV")
        return []
    
    with open(file_path, "r", encoding=encoding) as f:
        lines = f.readlines()
    headers = lines[0].strip().split(delimiter)
    
    return [
        {headers[i]: date_control(col, dateformat) for i, col in enumerate(row.split(delimiter))}
        for row in lines[1:]
    ]

def remove_duplicates(collection):
    return reduce(lambda acc, x: acc + [x] if x not in acc else acc, collection, [])

def merge_lists(list1, list2, deduplicate=True):
    combined = list1 + list2
    return remove_duplicates(combined) if deduplicate else combined

def change_column_name(data, old_column, new_column):
    return [
        {new_column if k == old_column else k: v for k, v in row.items()}
        for row in data
    ]

def change_float(val, decimal="."):
    return float(val.replace(",", decimal)) if isinstance(val, str) and "," in val else val

def column_sum(data, cols_list, cols_multip, new_column):
    return [
        {**row, new_column: sum(change_float(row[col]) * cols_multip[i] for i, col in enumerate(cols_list))}
        for row in data
    ]
