from __future__ import annotations

import os.path
from collections import deque

import pytest


_INPUT = os.path.join(os.path.dirname(__file__), 'input.txt')


def _solve(inp: str) -> int:
    deq: deque[str] = deque(maxlen=14)
    for idx, letter in enumerate(inp):
        deq.append(letter)
        if len(set(deq)) == deq.maxlen:
            return idx + 1
    raise NotImplementedError('no unique letter combination in string')


_TESTS = """\
mjqjpqmgbljsphdztnvjfqwrcgsmlb
"""
_EXPECTED = 19


@pytest.mark.parametrize(
    ('input_str', 'expected'),
    (
        (_TESTS, _EXPECTED),
    ),
)
def test(input_str: str, expected: int) -> None:
    assert _solve(input_str) == expected


def main() -> int:
    with open(_INPUT) as fp:
        print(_solve(fp.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
