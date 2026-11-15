"""R171 independent exact checks: signed-axis prefix-integral context quotient.
Only finite exact integer/residue algebra; no BRC amplitude or physical evolution.
"""
from collections import deque
from itertools import product
import json


def directions(d):
    for i in range(d):
        for sign in (-1, 1):
            yield (i, sign)


def K(word, q, d):
    displacement = [0] * d
    integral = [0] * d
    for i, sign in word:
        displacement[i] += sign
        for j in range(d):
            integral[j] += displacement[j]
    return (len(word) % q,
            tuple(x % q for x in displacement),
            tuple(x % q for x in integral))


def K_integer(word, d):
    displacement = [0] * d
    integral = [0] * d
    for i, sign in word:
        displacement[i] += sign
        for j in range(d):
            integral[j] += displacement[j]
    return (len(word), tuple(displacement), tuple(integral))


def mul(x, y, q, d):
    a, b, c = x
    n, e, f = y
    return ((a + n) % q,
            tuple((b[i] + e[i]) % q for i in range(d)),
            tuple((c[i] + f[i] + n * b[i]) % q for i in range(d)))


def reachability(q, d):
    identity = (0, (0,) * d, (0,) * d)
    generators = [K((v,), q, d) for v in directions(d)]
    seen = {identity}
    todo = deque([identity])
    while todo:
        state = todo.popleft()
        for g in generators:
            next_state = mul(state, g, q, d)
            if next_state not in seen:
                seen.add(next_state)
                todo.append(next_state)
    return len(seen)


def main():
    q, d = 3, 2
    alphabet = list(directions(d))
    short = [w for n in range(4) for w in product(alphabet, repeat=n)]
    medium = [w for n in range(5) for w in product(alphabet, repeat=n)]
    checks = 0
    for u in medium:
        ku = K(u, q, d)
        for v in medium:
            assert K(u + v, q, d) == mul(ku, K(v, q, d), q, d)
            checks += 1
    context_tests = 0
    # Three contexts constitute a complete separating basis for any two words.
    contexts = [((), ()), (((0, 1),), ()), ((), ((0, 1),))]
    for u in short:
        for v in short:
            equivalent = all(K(x + u + y, q, d)[2] ==
                             K(x + v + y, q, d)[2] for x, y in contexts)
            assert equivalent == (K(u, q, d) == K(v, q, d))
            context_tests += 1
    # Exact endpoint-return counterexample: binary sign projection is 10 for both.
    p = ((0, 1), (0, -1))
    r = ((1, 1), (1, -1))
    assert K_integer(p, 6)[:2] == K_integer(r, 6)[:2]
    assert K_integer(p, 6)[2] != K_integer(r, 6)[2]
    reach = {}
    for qq, dd in ((2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)):
        reach[f"q{qq}_d{dd}"] = reachability(qq, dd)
        if qq % 2 == 1:
            assert reach[f"q{qq}_d{dd}"] == qq ** (2 * dd + 1)
    assert reach["q2_d2"] == 16
    result = {
        "marker": "R171_SIGNED_X6_CONTEXT_COCYCLE_EXACT_PASS",
        "arithmetic": "exact integers and reductions modulo q; no floats",
        "concatenation_pairs": checks,
        "three_context_pair_tests": context_tests,
        "reachability_counts": reach,
        "q3_d6_group_order_symbolically_proved": 3 ** 13,
        "counterexample": {
            "P": ["+E1", "-E1"], "Q": ["+E2", "-E2"],
            "binary_sign_projection_both": "10",
            "integer_K_P": K_integer(p, 6),
            "integer_K_Q": K_integer(r, 6)
        },
        "limitations": "finite enumeration checks algebra and selected reachability; universal statements use symbolic proofs in R171 note",
        "independent_review": "NOT_REVIEWED"
    }
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
