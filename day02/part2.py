from __future__ import annotations

import os.path

import pytest


_INPUT = os.path.join(os.path.dirname(__file__), 'input.txt')


_CHOICE_SCORES = {'X': 1, 'Y': 2, 'Z': 3}
_WINS = {'Y': 'A', 'X': 'C', 'Z': 'B'}
_WINS_CHOICE = {value: key for key, value in _WINS.items()}
_TIE = {'Y': 'B', 'X': 'A', 'Z': 'C'}
_TIE_CHOICE = {value: key for key, value in _TIE.items()}
_LOSE = {'Y': 'C', 'X': 'B', 'Z': 'A'}
_LOSS_CHOICE = {value: key for key, value in _LOSE.items()}
_TRANSLATE = {'X': 'A', 'Y': 'B', 'Z': 'C'}


def _solve(inp: str) -> int:
    ret = 0
    for line in inp.splitlines():
        opp_choice, our_choice = line.split()

        if our_choice == 'X':
            our_choice = _LOSS_CHOICE[opp_choice]
        elif our_choice == 'Y':
            our_choice = _TIE_CHOICE[opp_choice]
        elif our_choice == 'Z':
            our_choice = _WINS_CHOICE[opp_choice]
        ret += _CHOICE_SCORES[our_choice]
        if _WINS[our_choice] == opp_choice:
            ret += 6
        elif _TRANSLATE[our_choice] == opp_choice:
            ret += 3
        else:
            ret += 0

    return ret


_TESTS = """\
A Y
B X
C Z
"""
_EXPECTED = 12


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
