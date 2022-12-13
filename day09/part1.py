from __future__ import annotations

import os.path

import pytest


_INPUT = os.path.join(os.path.dirname(__file__), 'input.txt')


class Knot:
    def __init__(self, x: int, y: int):
        self.x, self.y = x, y
        self.dirs = {
            'R': (1, 0),
            'L': (-1, 0),
            'D': (0, 1),
            'U': (0, -1),
        }

    def move(self, move) -> tuple[int, int]:
        return self.x + self.dirs[move][0],  self.y + self.dirs[move][1]

    def move_tail(self, move) -> tuple[int, int]:
        if move == 'R':
            move = 'L'
        elif move == 'L':
            move = 'R'
        elif move == 'U':
            move = 'D'
        elif move == 'D':
            move = 'U'
        return self.x + self.dirs[move][0],  self.y + self.dirs[move][1]


def _solve(inp: str) -> int:
    head = Knot(0, 0)
    tail = Knot(0, 0)
    visited = {(tail.x, tail.y)}
    for line in inp.splitlines():
        move_dir, move_number = line.split()
        number_moves = int(move_number)
        for _ in range(number_moves):
            head = Knot(*head.move(move_dir))
            if abs(head.x - tail.x) >= 2 or abs(head.y - tail.y) >= 2:
                tail = Knot(*head.move_tail(move_dir))
                visited.add((tail.x, tail.y))

    return len(visited)


_TESTS = """\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""
_EXPECTED = 13


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
