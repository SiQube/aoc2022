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
    tail = dict()
    for idx in range(1, 10):
        tail[idx] = Knot(0, 0)

    visited = {(head.x, head.y)}
    for line in inp.splitlines():
        move_dir, move_number = line.split()
        number_moves = int(move_number)
        for move_index in range(number_moves):
            head = Knot(*head.move(move_dir))
            last_knot = head
            for idx in range(1, 10):
                if (
                    abs(last_knot.x - tail[idx].x) == 2 and
                    abs(last_knot.y - tail[idx].y) == 2
                ):
                    tail[idx] = Knot(
                        (last_knot.x + tail[idx].x)//2,
                        (last_knot.y + tail[idx].y)//2,
                    )
                elif abs(last_knot.x - tail[idx].x) == 2:
                    tail[idx] = Knot(
                        (last_knot.x + tail[idx].x)//2,
                        last_knot.y,
                    )
                elif abs(last_knot.y - tail[idx].y) == 2:
                    tail[idx] = Knot(
                        last_knot.x,
                        (last_knot.y + tail[idx].y)//2,
                    )
                last_knot = Knot(tail[idx].x, tail[idx].y)
            visited.add((tail[9].x, tail[9].y))
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
_EXPECTED = 1

_SECOND_TESTS = """\
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""

_SECOND_EXPECTED = 36


@pytest.mark.parametrize(
    ('input_str', 'expected'),
    (
        (_TESTS, _EXPECTED),
        (_SECOND_TESTS, _SECOND_EXPECTED),
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
