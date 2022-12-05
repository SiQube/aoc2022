from __future__ import annotations

import os.path

import pytest


_INPUT = os.path.join(os.path.dirname(__file__), 'input.txt')


def _solve(inp: str) -> str:
    _input = inp.split('\n\n')
    stack_dict: dict[str, list[str]] = dict()
    cols = [4*idx + 1 for idx in range(10)]
    for line in reversed(_input[0].splitlines()):
        if len(line) != 39:
            line = 4*' ' + line
        for idx, col in enumerate(cols):
            try:
                stack = line[col]
                if stack.isnumeric():
                    stack_dict[f'{(col-1) // 4}'] = []
                elif stack.isalpha():
                    stack_dict[f'{(col-1) // 4}'].append(stack)
            except IndexError:
                continue

    for line in _input[1].splitlines():
        split_line = line.split()
        _items_to_move = int(split_line[1])
        _from = split_line[3]
        _to = split_line[5]
        try:
            stack_dict[_to].extend(stack_dict[_from][-_items_to_move:])
            stack_dict[_from] = stack_dict[_from][:-_items_to_move]
        except IndexError:
            continue

    ret = ''
    for key, value in stack_dict.items():
        try:
            ret += value[-1]
        except IndexError:
            continue

    return ret


_TESTS = """\
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

 move 1 from 2 to 1
 move 3 from 1 to 3
 move 2 from 2 to 1
 move 1 from 1 to 2
"""
_EXPECTED = 'MCD'


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
