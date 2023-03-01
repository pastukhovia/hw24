import re
from typing import Union, List, Iterator, Any


def query_handler(query: str, value:  Any, data: Any, file_name: str) -> Union[map, filter, List[str], set, None]:
    if data is None:
        file_data = read_file(file_name)
    else:
        file_data = data

    if query == 'filter':
        return filter(lambda v: value in v, file_data)
    elif query == 'map':
        return map(lambda v: v.split(' ')[int(value)], file_data)
    elif query == 'unique':
        return set(file_data)
    elif query == 'sort':
        if value == 'asc':
            return sorted(file_data, reverse=False)
        elif value == 'desc':
            return sorted(file_data, reverse=True)
    elif query == 'limit':
        return list(file_data)[:int(value)]
    elif query == 'regex':
        result: list = []
        for string in file_data:
            if re.search(value, string):
                result.append(string)

        return result

    # Запрос для поиска images/....png
    # {
    #     "cmd1": "regex",
    #     "cmd2": "sort",
    #     "val1": "images/[\\w-]+\\.png",
    #     "val2": "asc",
    #     "file_name": "apache_logs.txt"
    # }
    return None


def read_file(file_name: str) -> Iterator[str]:
    with open(file_name) as f:
        for line in f:
            yield line
