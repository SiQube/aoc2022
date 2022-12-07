from __future__ import annotations

import os.path

import pytest


_INPUT = os.path.join(os.path.dirname(__file__), 'input.txt')


def _solve(inp: str) -> int:
    cwd = ['/']
    files: dict[str, int]
    files = dict()
    lines = inp.splitlines()[1:]
    disk_size = 70000000
    needed_space = 30000000
    min_del = 10000000000
    for lin_num, line in enumerate(lines):
        if line.startswith('$ cd'):
            _dir = line.split()[-1]
            if _dir.isalpha():
                cwd.append(_dir)
            elif _dir == '..':
                cwd.pop(-1)
        elif line.startswith('$ ls'):
            while True:
                lin_num += 1
                try:
                    cur_lin = lines[lin_num]
                except IndexError:
                    break
                first_elem = cur_lin.split()[0]
                if first_elem.isnumeric():
                    try:
                        files['/'.join(cwd[1:])] += int(first_elem)
                    except KeyError:
                        files['/'.join(cwd[1:])] = int(first_elem)
                elif not cur_lin.startswith('$'):
                    continue
                else:
                    break

    merge_dict: dict[str, int]
    merge_dict = {}
    for directory, size in sorted(files.items()):
        par_idx = 1
        try:
            merge_dict[directory] += size
        except KeyError:
            merge_dict[directory] = size
        while True:
            if directory == '':
                break
            parent_dir = '/'.join(directory.split('/')[:-par_idx])
            if parent_dir in merge_dict.keys():
                merge_dict[parent_dir] += size
            else:
                merge_dict[parent_dir] = size
            par_idx += 1
            if parent_dir == '/' or parent_dir == '':
                break

    space_left = disk_size - merge_dict['']
    for key, value in merge_dict.items():
        if (space_left+value) > needed_space:
            if value < min_del:
                min_del = value
    return min_del


_TESTS = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""
_EXPECTED = 24933642


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
