from __future__ import annotations

import os.path

import pytest


_INPUT = os.path.join(os.path.dirname(__file__), 'input.txt')


def _solve(inp: str) -> int:
    lines = inp.splitlines()
    len_lines = len(lines)
    len_elems = len(lines[0])
    trees = dict()
    for idy, line in enumerate(lines):
        for idx, val in enumerate(line):
            trees[idx, idy] = int(val)

    view = -1

    def help_solve(x: int, y: int) -> int:
        height = trees[(y, x)]

        up = 0
        for y_coord in range(y - 1, -1, -1):
            up += 1
            if trees[(y_coord, x)] >= height:
                break

        down = 0
        for y_coord in range(y + 1, len_lines):
            down += 1
            if trees[(y_coord, x)] >= height:
                break

        left = 0
        for x_coord in range(x - 1, -1, -1):
            left += 1
            if trees[(y, x_coord)] >= height:
                break

        right = 0
        for x_coord in range(x + 1, len_elems):
            right += 1
            if trees[(y, x_coord)] >= height:
                break

        return up * down * left * right

    for y in range(0, len_lines):
        for x in range(0, len_elems):
            view = max(help_solve(x, y), view)
    return view


_TESTS = """\
30373
25512
65332
33549
35390
"""
_EXPECTED = 8


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
