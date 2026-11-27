"""Necessary seven-moment and prime residue conditions for the variable tail."""
from fractions import Fraction
from heapq import heappop, heappush

from exact import WEIGHTS, enumerate_ball, model, signed_mass

HEIGHT = 9600
POLYNOMIALS = {
    9152: (1320, -100462, 1092526, -4787885, 10000000, -9841088, 3635592),
    9569: (-4827586, 10000000, -5172414),
}


def h6_tail(u, v, bound, polynomial):
    positive, negative = signed_mass(v)
    a, b = bound - positive, bound - negative
    target = [
        -sum(Fraction(x, (17*j)**k) for j, x in enumerate(u, 1))
        for k in range(7)
    ]
    observed = sum(c * 2**k * target[k] for k, c in enumerate(polynomial))
    value = {
        d: sum(Fraction(c * 2**k, d**k) for k, c in enumerate(polynomial))
        for d in range(2, max(a, b) + 2) if d % 17
    }
    upper_positive = max([Fraction()] + [f / (d-1) for d, f in value.items() if d-1 <= a])
    upper_negative = max([Fraction()] + [-f / (d-1) for d, f in value.items() if d-1 <= b])
    slack = a * upper_positive + b * upper_negative - observed
    result = {"tail_caps": (a, b), "polynomial_on_2_over_a": polynomial,
              "unit_max": (str(upper_positive), str(upper_negative)),
              "dual_slack": str(slack)}
    if slack < 0:
        return result | {"status": "NEGATIVE_SLACK"}

    # These are the minimum denominator divisibilities implied by the exact M6.
    required = (16, 9, 5, 7)
    primes = (2, 3, 5, 7)
    for d, q in zip(required, primes):
        power = target[6].denominator
        exponent = 0
        while power % q == 0:
            exponent += 1
            power //= q
        assert (d//q)**6 < q**exponent <= d**6

    q1, q2 = 11, 13
    m1, m2 = q1*q1, q2*q2
    goal = []
    for q, m in ((q1, m1), (q2, m2)):
        scaled = target[6] * q**6
        goal.append(scaled.numerator * pow(scaled.denominator, -1, m) % m)

    # State: first four bits track compulsory power divisors. The next two
    # record an atom divisible by q^2, which relaxes that q's residue check.
    actions = {}
    for d, f in value.items():
        mask = sum(1 << i for i, power in enumerate((*required, m1, m2)) if d % power == 0)
        r1 = pow(d//q1, -6, m1) if d % q1 == 0 and d % m1 else 0
        r2 = pow(d//q2, -6, m2) if d % q2 == 0 and d % m2 else 0
        for sign, cap, maximum in ((1, a, upper_positive), (-1, b, upper_negative)):
            if d-1 > cap:
                continue
            penalty = (d-1)*maximum - sign*f
            assert penalty >= 0
            if penalty > slack:
                continue
            action = (mask, (sign*r1) % m1, (sign*r2) % m2)
            if any(action) and (action not in actions or penalty < actions[action]):
                actions[action] = penalty

    initial = (0, 0, 0)
    costs = {initial: Fraction()}
    pending = [(Fraction(), initial)]
    checked = 0
    best = None
    while pending:
        cost, state = heappop(pending)
        if cost != costs[state]:
            continue
        checked += 1
        mask, r1, r2 = state
        if mask & 15 == 15 and (mask & 16 or r1 == goal[0]) and (mask & 32 or r2 == goal[1]):
            best = cost
            break
        for (add, d1, d2), penalty in actions.items():
            total = cost + penalty
            if total > slack:
                continue
            successor = (mask | add, (r1+d1) % m1, (r2+d2) % m2)
            if total < costs.get(successor, slack+1):
                costs[successor] = total
                heappush(pending, (total, successor))
    return result | {"prime_residue_target": goal, "required": required, "actions": len(actions),
                     "checked_states": checked, "status": "EXCLUDED" if best is None else "RELAXATION_FEASIBLE",
                     "min_penalty": None if best is None else str(best)}


def verify_variable_tail(weighted):
    census, vectors = enumerate_ball(model(weighted, True), HEIGHT)
    assert [h for h, _, _ in vectors] == [9152, 9569]
    rows = []
    for h, v, _ in vectors:
        u = tuple(x//w for x, w in zip(v, WEIGHTS))
        assert tuple(w*x for w, x in zip(WEIGHTS, u)) == v
        proof = h6_tail(u, v, HEIGHT, POLYNOMIALS[h])
        assert proof["status"] in ("EXCLUDED", "NEGATIVE_SLACK")
        rows.append({"threshold": h, "u": u, "masses": signed_mass(v), "proof": proof})
    next_relaxation = h6_tail(rows[0]["u"], vectors[0][1], HEIGHT+1, POLYNOMIALS[9152])
    assert next_relaxation["status"] == "RELAXATION_FEASIBLE"
    return {"census": census, "tested_vectors": rows, "first_uncleared_relaxation": next_relaxation}
