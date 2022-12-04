from __future__ import annotations

import os.path

import pytest


_INPUT = os.path.join(os.path.dirname(__file__), 'input.txt')


def _solve(inp: str) -> int:
    score = 0
    for line in inp.splitlines():
        first_elf, second_elf = line.split(',')
        fe_1, fe_2 = first_elf.split('-')
        se_1, se_2 = second_elf.split('-')
        fe_1_int, fe_2_int = int(fe_1), int(fe_2)
        se_1_int, se_2_int = int(se_1), int(se_2)
        if fe_1_int <= se_1_int <= fe_2_int:
            score += 1
        elif se_1_int <= fe_1_int <= se_2_int:
            score += 1
        else:
            continue

    return score


_TESTS = """\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""
_EXPECTED = 2


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
