from mealy import State, Path

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

    result = list(q0.walk("RDULD"))
    for r in result:
        print(r)

if __name__ == "__main__":
    test_mealy()
