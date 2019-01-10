from enum import Enum
from typing import Set, List, Dict

# class Sigma(Enum):
#     A = "A"
#     B = "B"

# class Omega(Enum):
#     S = "S"
#     N = "N"

# class Q(Enum):
#     q0 = q0

# def q0(sig: Sigma) -> (Q, Omega):
#     return (Omega.N, Q.q1 if sig == Sigma.A else Q.q3)

#def mealy(Q, s, Sig, Omg):


#mealy(["q0,", "q2"], "q0", , "")

Q_test = {"q0", "q1", "q2", "q3", "q4", "q5", "q6"}

Sigm_test = {"A", "B"}

Omg_test = {"N", "S"}

table_test = {
    "q0":{
        "A":("q1", "N"),
        "B":("q3", "N")
    },
    "q1":{
        "A":("q3", "N"),
        "B":("q2", "N")
    },
    "q2":{
        "A":("q3", "N"),
        "B":("q1", "N")
    },
    "q3":{
        "A":("q0", "N"),
        "B":("q4", "N")
    },
    "q4":{
        "A":("q5", "N"),
        "B":("q2", "N")
    },
    "q5":{
        "A":("q0", "N"),
        "B":("q6", "S")
    },
    "q6":{
        "A":(None, "N"),
        "B":(None, "N")
    },
}

class MealyAutomat:
    # Q = Zustände
    # Sigm = Eingabealphabet (mögliche Aktionen)
    # Omg = Ausgabealphabet (mögliche Ausgaben)
    # table = Definition der Zusammenhänge
    def __init__(self, Q: Set, Sigm: Set, Omg: Set, table):
        self.Q = Q
        self.Sigm = Sigm
        self.Omg = Omg
        self.table = table
    
    def run(self, s, path: List[self.Sigm]) -> self.Omg:
        result = None
        for step in path:
            s, result = self.table[s][step]
        return result

mein_automat = MealyAutomat(Q_test, Sigm_test, Omg_test, table_test)
print(mein_automat.run("q0", "AAA"))