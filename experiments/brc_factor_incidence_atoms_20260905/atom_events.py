"""Regular-parameter guard from SUPPLIED monic polynomial-in-t atoms.

This is not a Q(t)[x] gcd-factorization engine or a complete CAD compiler.
Persistent endpoint roots and invalid generic atoms are explicitly refused.
"""
from fractions import Fraction as Q
import factor_atoms as fa


def event_guard(atoms, left, right, rg):
    if not Q(left) < Q(right):
        raise ValueError("invalid interval")
    normalized = tuple(rg.x_trim(p) for p in atoms)
    if any(len(p) < 2 or p[-1] != rg.ONE for p in normalized):
        raise ValueError("supplied atoms must be nonconstant and monic in x")
    event = rg.ONE
    slots = 0
    for i, p in enumerate(normalized):
        factors = [rg.resultant_event_factor(p), rg.x_eval(p, Q(left)), rg.x_eval(p, Q(right))]
        factors += [rg.sylvester_resultant(p, q) for q in normalized[:i]]
        for f in factors:
            if f == rg.ZERO:
                raise ValueError("nonregular supplied atoms or persistent endpoint: refine the typed input")
            event = rg.t_mul(event, f)
            slots += 1
    event = fa.K._p_monic(event)
    common = fa.K._p_gcd(event, fa.K._p_derivative(event))
    return fa.K._p_div_exact(event, common), slots


def specialize(poly, t, rg):
    return fa.K._trim(tuple(rg.t_eval(c, Q(t)) for c in poly))
