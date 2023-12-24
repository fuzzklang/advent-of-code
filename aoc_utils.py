import sys
from typing import List


def read_stdin() -> List[str]:
    lst = []
    for line in sys.stdin:
        line = line.strip()
        lst.append(line)
    return lst
