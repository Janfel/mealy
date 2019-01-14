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

"""Tests for mealy.mealy."""

from mealy.mealy import *  # pylint: disable=wildcard-import, unused-wildcard-import


def test_state():
    """
    Test for State.
    Imagine a rectangle like this:

    q0−−−−−q1
     |     |
     |     |
    q2−−−−−q3
    """

    # pylint: disable=invalid-name

    q0 = State("q0")
    q1 = State("q1")
    q2 = State("q2")
    q3 = State("q3")

    q0.set_paths([Path("R", q1, "0°"), Path("D", q2, "90°")])
    q1.set_paths([Path("L", q0, "180°"), Path("D", q3, "90°")])
    q2.set_paths([Path("R", q3, "0°"), Path("U", q0, "270°")])
    q3.set_paths([Path("L", q2, "180°"), Path("U", q1, "270°")])


def test_mealy():
    """
    Test for mealy().
    Imagine a rectangle like this:

    q0−−−−−q1
     |     |
     |     |
    q2−−−−−q3
    """

    # pylint: disable=invalid-name

    q0 = State("q0")
    q1 = State("q1")
    q2 = State("q2")
    q3 = State("q3")

    q0.set_paths([Path("R", q1, "0°"), Path("D", q2, "90°")])
    q1.set_paths([Path("L", q0, "180°"), Path("D", q3, "90°")])
    q2.set_paths([Path("R", q3, "0°"), Path("U", q0, "270°")])
    q3.set_paths([Path("L", q2, "180°"), Path("U", q1, "270°")])

    expected = [
        MealyResult("R", q1, "0°"),
        MealyResult("D", q3, "90°"),
        MealyResult("U", q1, "270°"),
        MealyResult("L", q0, "180°"),
        MealyResult("D", q2, "90°"),
    ]
    result = list(q0.walk("RDULD"))
    assert result == expected
