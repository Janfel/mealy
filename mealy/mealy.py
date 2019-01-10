# region License

# Copyright (C) 2019 Jan Felix Langenbach
#
# This file is part of mealy.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http: //www.gnu.org/licenses/>.

# endregion

"""Main module for mealy."""

from collections import namedtuple
from typing import Dict, Iterable, Iterator, Optional, Tuple, TypeVar

T = TypeVar("T")  # pylint: disable=invalid-name
O = TypeVar("O")  # pylint: disable=invalid-name

Path = namedtuple("Path", ["name", "dest", "value"])


class State:
    """State of Mealy Machine"""

    def __init__(self, name: str, paths: Optional[Iterable[Path]]) -> None:
        self.name = name

        PathDict = Dict[T, Tuple[State, O]]  # pylint: disable=invalid-name
        self.paths: PathDict = {}
        if paths:
            self.set_paths(paths)

    def set_path(self, path: Path) -> None:
        """Sets the destination and value for this path"""
        self.paths[path.name] = (path.dest, path.value)

    def set_paths(self, paths: Iterable[Path]) -> None:
        """Sets the destination and value for these paths"""
        for path in paths:
            self.set_path(path)

    def walk(self, step: T) -> Optional[Tuple[State, O]]:
        """If a Path exists for this step, return the Paths destination and output."""
        result = None
        try:
            result = self.paths[step]
        except KeyError:
            result = None
        return result


def mealy(state: State, steps: Iterable[T]) -> Iterator[O]:
    """Walk the given steps on the Mealy Machine and yield all produced outputs."""
    for step in steps:
        tup: Optional[Tuple[State, O]] = state.walk(step)
        if tup:
            state, out = tup
            yield out
        else:
            raise ValueError(
                f"Can't take given steps. State {state.name} hasn't set a Path for Step {step}."
            )
