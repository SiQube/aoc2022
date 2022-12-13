from __future__ import annotations

import os.path

import pytest


_INPUT = os.path.join(os.path.dirname(__file__), 'input.txt')


def draw(pixel_to_draw: set[tuple[int, int]]) -> str:
    min_x, min_y = min(pixel_to_draw)
    max_x, max_y = max(pixel_to_draw)
    return '\n'.join(''.join('#' if (x, y) in pixel_to_draw else '.' for x in range(min_x, max_x + 1)) for y in range(min_y, max_y + 1))  # noqa: E501


def _solve(inp: str) -> str:
    X = [1]
    cycle_counter = 0
    to_draw = set()
    for line in inp.splitlines():
        try:
            addx, value = line.split()
        except ValueError:
            cycle_counter += 1
            if sum(X) - 1 <= ((cycle_counter - 1) % 40) <= sum(X) + 1:
                to_draw.add((
                    (cycle_counter - 1) % 40, (cycle_counter - 1) // 40,
                ))
            if cycle_counter >= 240:
                break
            continue
        int_val = int(value)
        for _ in range(2):
            cycle_counter += 1
            if sum(X) - 1 <= ((cycle_counter - 1) % 40) <= sum(X) + 1:
                to_draw.add((
                    (cycle_counter - 1) % 40, (cycle_counter - 1) // 40,
                ))
        if cycle_counter >= 240:
            break
        X.append(int_val)

    return draw(to_draw)


_TESTS = """\
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""
_EXPECTED = '''\
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
'''.rstrip()


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
