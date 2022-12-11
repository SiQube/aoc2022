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

    visible_trees = set()
    for y in range(0, len_lines):

        down_height = trees[(y, 0)]
        visible_trees.add((y, 0))
        for x in range(1, len_elems):
            coords = (y, x)
            if trees[coords] > down_height:
                visible_trees.add(coords)
                down_height = trees[coords]

        up_height = trees[(y, len_elems - 1)]
        visible_trees.add((y, len_elems - 1))
        for x in range(len_elems-1, -1, -1):
            coords = (y, x)
            if trees[coords] > up_height:
                visible_trees.add(coords)
                up_height = trees[coords]

    for x in range(0, len_elems):

        left_height = trees[(0, x)]
        visible_trees.add((0, x))
        for y in range(1, len_lines):
            coords = (y, x)
            if trees[coords] > left_height:
                visible_trees.add(coords)
                left_height = trees[coords]

        right_height = trees[(len_lines - 1, x)]
        visible_trees.add((len_lines - 1, x))
        for y in range(len_lines-1, -1, -1):
            coords = (y, x)
            if trees[coords] > right_height:
                visible_trees.add(coords)
                right_height = trees[coords]

    return len(visible_trees)


_TESTS = """\
30373
25512
65332
33549
35390
"""
_EXPECTED = 21


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
