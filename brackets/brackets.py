import re


def split_group(line: str):
    try:
        last_index = line.rindex(')') + 1
        if last_index < len(line):
            return split_group(line[:last_index])
    except ValueError:
        return line
    return line


def re_split_group(line):
    return re.sub(r'[^)]+$', '', line)
