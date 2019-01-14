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

from dataclasses import dataclass
from typing import Dict, Generic, Iterable, Iterator, Optional, Tuple, TypeVar

__all__ = ["State", "Path"]


T = TypeVar("T")  # pylint: disable=invalid-name
O = TypeVar("O")  # pylint: disable=invalid-name


@dataclass
class Path(Generic[T, O]):  # pylint: disable=unsubscriptable-object
    """
    Path from one State to another.
    step: The entry to take.
    dest: The resulting State.
    value: The Paths output.
    """

    step: T
    dest: "State"
    value: O


@dataclass
class MealyResult(Generic[T, O]):  # pylint: disable=unsubscriptable-object
    """
    The result of changing the state of the Mealy Machine.
    step: The step that lead to this path.
    state: The new State resulting from this step.
    out: The output produced by walking on this path.
    """

    step: T
    state: "State"
    out: O

    def __str__(self) -> str:
        return f"{self.step} => {self.state} / {self.out}"


class State:
    """State of Mealy Machine."""

    def __init__(self, name: str, paths: Optional[Iterable[Path]] = None) -> None:
        PathDict = Dict[T, Tuple[State, O]]  # pylint: disable=invalid-name
        self.name = name
        self.paths: PathDict = {}
        if paths:
            self.set_paths(paths)

    def set_path(self, path: Path) -> None:
        """Sets the destination and value for this path"""
        self.paths[path.step] = (path.dest, path.value)

    def set_paths(self, paths: Iterable[Path]) -> None:
        """Sets the destination and value for these paths"""
        for path in paths:
            self.set_path(path)

    def step(self, step: T) -> Optional[MealyResult]:
        """If a Path exists for this step, return the Paths destination and output."""
        result = None
        try:
            state, out = self.paths[step]
            result = MealyResult(step, state, out)
        except KeyError:
            result = None
        return result

    def walk(self, steps: Iterable[T]) -> Iterator[MealyResult]:
        """Walk the given steps on the Mealy Machine and yield all steps and produced outputs."""
        state = self
        for step in steps:
            result: Optional[MealyResult] = state.step(step)
            if result:
                state = result.state
                yield result
            else:
                raise ValueError(
                    f"Can't take given steps. State {state.name} hasn't set a Path for Step {step}."
                )

    def __str__(self) -> str:
        return self.name
