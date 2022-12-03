from __future__ import annotations

import os.path

import pytest


_INPUT = os.path.join(os.path.dirname(__file__), 'input.txt')


def _solve(inp: str) -> int:
    score = 0
    rlist = []
    for idx, line in enumerate(inp.splitlines()):
        rlist.append(line)
        if idx % 3 == 2:
            first_intersect = set(rlist[0]).intersection(set(rlist[1]))
            final_intersect = first_intersect.intersection(set(rlist[2]))
            letter = list(final_intersect)[0]
            if letter == letter.capitalize():
                letter_score = ord(letter) - 38
            else:
                letter_score = ord(letter) - 96
            score += letter_score
            rlist = []

    return score


_TESTS = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""
_EXPECTED = 70


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
