"""Exact dual-law, two-coupled-time/LR-key stopped-tree certificate (Python stdlib)."""
from fractions import Fraction as F
from itertools import product

# All pairs are (P mass, Q mass), including source and conditional nature laws.
SOURCE = {"A1": (F(1, 8), F(1, 8)),
          "A2": (F(1, 8), F(1, 8)),
          "B": (F(1, 4), F(1, 8)),
          "C": (F(1, 2), F(5, 8))}
LOW = {"A1": (F(1, 2), F(1, 4)),
       "A2": (F(3, 4), F(3, 8))}


def terminal_flows(p1, p2, q1, q2, qb, r):
    p = {"A1": F(p1), "A2": F(p2)}
    q = {"A1": F(q1), "A2": F(q2), "B": F(qb)}
    out = []

    def emit(source, label, Pmass, Qmass, time, answer):
        assert answer in ("P", "Q")
        assert Pmass >= 0 and Qmass >= 0
        out.append((source, label, Pmass, Qmass, F(time), answer))

    for source in ("A1", "A2"):
        P, Q = SOURCE[source]
        Lp, Lq = LOW[source]
        a, b = p[source], q[source]
        emit(source, "I-stop", P*a, Q*a, 1, "Q")
        emit(source, "high-terminal", P*(1-a)*(1-Lp),
             Q*(1-a)*(1-Lq), 2, "P")
        emit(source, "J-stop", P*(1-a)*Lp*b,
             Q*(1-a)*Lq*b, 2, "Q")
        flowP, flowQ = P*(1-a)*Lp*(1-b), Q*(1-a)*Lq*(1-b)
        if source == "A1":
            # A terminal signal makes the fixed terminal response LR-measurable.
            emit(source, "J-final-X", flowP*F(3,5), flowQ*F(1,2), 3, "P")
            emit(source, "J-final-Y", flowP*F(2,5), flowQ*F(1,2), 3, "Q")
        else:
            emit(source, "J-final", flowP, flowQ, 3, "Q")
    P, Q = SOURCE["B"]
    emit("B", "J-stop", P*q["B"], Q*q["B"], 2, "Q")
    emit("B", "J-continue", P*(1-q["B"]), Q*(1-q["B"]), 3, "Q")
    P, Q = SOURCE["C"]
    emit("C", "private-stop", P*F(r), Q*F(r), 1, "P")
    emit("C", "private-continue", P*(1-F(r)), Q*(1-F(r)), 3, "Q")
    assert sum(x[2] for x in out) == sum(x[3] for x in out) == 1
    return out


def observe(p1, p2, q1, q2, qb, r):
    events = terminal_flows(p1, p2, q1, q2, qb, r)
    # eP = P(terminal answer Q); eQ = Q(terminal answer P).
    return (sum(x[2] for x in events if x[5] == "Q"),
            sum(x[3] for x in events if x[5] == "P"),
            sum(x[2]*x[4] for x in events),
            sum(x[3]*x[4] for x in events))


def LR(p, q, r):
    return observe(p, p, q, q, q, r)


def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def scale(s, a):
    return tuple(s*x for x in a)


def det4(columns):
    a = [[columns[j][i] for j in range(4)] for i in range(4)]
    d = F(1)
    for k in range(4):
        pivot = next((i for i in range(k, 4) if a[i][k]), None)
        if pivot is None:
            return F(0)
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            d = -d
        v = a[k][k]
        d *= v
        for i in range(k+1, 4):
            coeff = a[i][k]/v
            for j in range(k+1, 4):
                a[i][j] -= coeff*a[k][j]
            a[i][k] = 0
    return d


assert sum(v[0] for v in SOURCE.values()) == 1
assert sum(v[1] for v in SOURCE.values()) == 1
for source in LOW:
    lp, lq = LOW[source]
    assert 0 < lp < 1 and 0 < lq < 1
    assert SOURCE[source][0]/SOURCE[source][1] == 1
    assert (SOURCE[source][0]*lp)/(SOURCE[source][1]*lq) == 2
assert SOURCE["B"][0]/SOURCE["B"][1] == 2
assert SOURCE["C"][0]/SOURCE["C"][1] == F(4, 5)
# At all positive interior policies, terminal responses factor through
# each terminal (time, likelihood-ratio) key, even for differing sources.
terminal_keys = {}
interior = terminal_flows(*([F(1,2)]*6))
assert len(interior) == 13
for _, _, mp, mq, time, answer in interior:
    assert mp > 0 and mq > 0
    key = (time, mp/mq)
    if key in terminal_keys:
        assert terminal_keys[key] == answer
    terminal_keys[key] = answer
assert terminal_keys[(F(3), F(12,5))] == "P"
assert terminal_keys[(F(3), F(8,5))] == "Q"
for full_policy in product((F(1,4), F(1,2), F(3,4)), repeat=6):
    for _, _, mp, mq, time, answer in terminal_flows(*full_policy):
        assert mp > 0 and mq > 0
        assert terminal_keys[(time, mp/mq)] == answer

O = LR(0, 0, 0)
B = sub(LR(1, 0, 0), O)
C = sub(LR(0, 1, 0), O)
D = sub(sub(sub(LR(1, 1, 0), O), B), C)
E = sub(LR(0, 0, 1), O)
expected = ((F(139,160),F(3,16),F(93,32),F(181,64)),
            (F(21,160),-F(3,16),-F(13,32),-F(21,64)),
            (F(3,80),-F(1,64),-F(13,32),-F(13,64)),
            (-F(3,80),F(1,64),F(5,32),F(5,64)),
            (-F(1,2),F(5,8),-F(1),-F(5,4)))
assert (O, B, C, D, E) == expected
assert det4((B, C, D, E)) == F(233, 163840)

# A source/port-preserving exact finite check of an identity that holds
# algebraically because each path has monomials 1,p,q,pq,r only.
GRID = (F(0), F(1,4), F(1,2), F(3,4), F(1))
for p, q, r in product(GRID, repeat=3):
    formula = add(add(add(add(O, scale(p, B)), scale(q, C)),
                      scale(p*q, D)), scale(r, E))
    assert LR(p, q, r) == formula

lr_vertices = list(product((0, 1), repeat=3))
full_vertices = list(product((0, 1), repeat=6))
# Each full decision parameter appears at most once on each path:
# exact midpoint checks for every parameter and every Boolean setting of the others.
for varying in range(6):
    for other in product((0, 1), repeat=5):
        a = list(other)
        a.insert(varying, F(0))
        zero = observe(*a)
        a[varying] = F(1)
        one = observe(*a)
        a[varying] = F(1,2)
        assert observe(*a) == scale(F(1,2), add(zero, one))
H = lambda v: v[0] + v[3]  # dimensionless time in integer ticks
max_lr = max(H(LR(*a)) for a in lr_vertices)
max_full = max(H(observe(*a)) for a in full_vertices)
assert max_lr == F(1183, 320)
assert max_full == F(237, 64)
assert max_full-max_lr == F(1, 160)
witness_policy = (0,0,1,0,0,0)
witness = observe(*witness_policy)
assert witness == (F(29,32), F(11,64), F(91,32), F(179,64))
assert H(witness)-max_lr == F(1, 160)
assert all(H(LR(p,q,r)) <= max_lr for p,q,r in product(GRID,repeat=3))

# The LR image is an invertible affine image of (p,q,pq,r).
# Endpoints have (p,q,pq,r)=(0,0,0,0),(1,1,1,0),
# and the midpoint would require (1/2,1/2,1/2,0),
# violating pq=1/4. This is an all-real nonmembership proof.
midpoint = scale(F(1,2), add(LR(0,0,0), LR(1,1,0)))
assert midpoint == (F(299,320),F(3,32),F(165,64),F(333,128))
assert midpoint == add(O, add(scale(F(1,2), B),
                      add(scale(F(1,2), C), scale(F(1,2), D))))
assert F(1,2)*F(1,2) != F(1,2)

print("P/Q initial source probabilities: OK")
print("key I=(time 1, P/Q 1), key J=(time 2, P/Q 2): OK")
print("terminal response is a function of (time, P/Q):", len(terminal_keys), "keys")
print("strictly interior FULL policies checked:", 3**6)
print("FULL multiaffinity checks:", 6*(2**5))
print("LR policy grid checked:", len(GRID)**3)
print("FULL/LR deterministic strategies:", len(full_vertices), len(lr_vertices))
print("O0,B,C,D,E:", *(str(v) for v in (O,B,C,D,E)), sep="\n")
print("LR affine-rank determinant:", det4((B,C,D,E)))
print("LR nonconvex midpoint:", midpoint)
print("H=eP+TQ: LR maximum",max_lr,"FULL maximum",max_full,"gap",max_full-max_lr)
print("FULL witness policy (p1,p2,q1,q2,qB,r):", witness_policy)
print("FULL witness (eP,eQ,TP,TQ):", witness)
print("Linfty distance to conv(LR) >=", F(1,320))
print("PASS_EXACT_R5_TWO_COUPLED_KEYS_PERFECT_RECALL_OBSTRUCTION")
