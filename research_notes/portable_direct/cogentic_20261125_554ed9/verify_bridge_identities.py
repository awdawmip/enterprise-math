"""Exact examples for the finite-window multiscale identity derived in REPORT.md.

The algebraic proof is in the report. These examples verify boundary accounting
and the supplied rational implementation; they do not audit the ten source papers.
Run: python3 verify_bridge_identities.py
"""
from fractions import Fraction as F
from pathlib import Path
import json


def discrete_energy(h, rhos, initial, weights=None):
    h, rhos, initial = list(map(F, h)), list(map(F, rhos)), list(map(F, initial))
    if not rhos or len(rhos) != len(initial) or any(not 0 <= r < 1 for r in rhos):
        raise ValueError("Use a nonempty bank with matching initial values and 0 <= rho < 1")
    count = len(rhos)
    weights = [F(1)]*len(h) if weights is None else list(map(F, weights))
    if len(weights) != len(h) or any(w < 0 for w in weights) or not h:
        raise ValueError("Use a nonempty input with nonnegative weights of the same length")
    paths = []
    for rho, start in zip(rhos, initial):
        ys = [start]
        for x in h:
            ys.append(rho * ys[-1] + (1-rho) * x)
        paths.append(ys)
    means = [sum(ys[t] for ys in paths)/count for t in range(1, len(h)+1)]
    lhs = sum(w*(x*y-y*y) for w,x,y in zip(weights,h,means))
    variance = sum(weights[t-1]*(ys[t]-means[t-1])**2 for ys in paths for t in range(1,len(h)+1))/count
    terminal = sum(rho/(2*(1-rho))*(weights[-1]*ys[-1]**2-weights[0]*ys[0]**2)
                   for rho,ys in zip(rhos,paths))/count
    weight_drop = sum(rho/(2*(1-rho))*sum((weights[t-1]-weights[t])*ys[t]**2
                                          for t in range(1,len(h)))
                      for rho,ys in zip(rhos,paths))/count
    increments = sum(rho/(2*(1-rho))*sum(weights[t-1]*(ys[t]-ys[t-1])**2 for t in range(1,len(ys)))
                     for rho,ys in zip(rhos,paths))/count
    assert lhs == variance+terminal+weight_drop+increments
    return {
        "input": [str(x) for x in h], "rho": [str(x) for x in rhos],
        "initial": [str(x) for x in initial], "terminal_values": [str(ys[-1]) for ys in paths],
        "weights": [str(w) for w in weights],
        "lhs": str(lhs), "variance": str(variance), "boundary": str(terminal),
        "weight_drop": str(weight_drop),
        "increment_energy": str(increments), "identity_exact": True,
    }


def riesel_preservation():
    a, modulus, q, target = 7, 3*5*13, 17, 4
    t = ((target-a)*pow(modulus,-1,q)) % q
    changed = a+t*modulus
    rows = []
    for n in range(16):
        old, new = a*a*(1 << n)-1, changed*changed*(1 << n)-1
        assert new-old == (1 << n)*(2*a*t*modulus+t*t*modulus*modulus)
        assert all(old % p == new % p for p in [3,5,13])
        rows.append({"n":n,"old_mod_195":old%modulus,"new_mod_195":new%modulus})
    assert changed % q == target
    return {"a":a,"M":modulus,"q":q,"target_root_mod_q":target,"t":t,
            "changed_a":changed,"checked_n":list(range(16)),"all_old_channels_preserved":True,
            "new_root_condition_met":True,"rows":rows,
            "scope":"Finite examples of an all-n algebraic identity, not a new Riesel covering result"}


def sign_residual():
    # Pointwise S^2=1 supplies a checkable closure residual for any candidate A.
    matrices = []
    S = [[F(1 if i != j else -1) for j in range(4)] for i in range(4)]
    for name, A in [("rank_one_mean", [[F(1,2) for _ in range(4)] for _ in range(4)]),
                    ("uniform_shrink", [[F(3,4)*x for x in row] for row in S])]:
        R = [[S[i][j]-A[i][j] for j in range(4)] for i in range(4)]
        for i in range(4):
            for j in range(4):
                assert A[i][j]**2-1 == -2*S[i][j]*R[i][j]+R[i][j]**2
        avg_abs = sum(abs(x) for row in R for x in row)/16
        avg_square = sum(x*x for row in R for x in row)/16
        defect = sum(abs(x*x-1) for row in A for x in row)/16
        assert defect <= 2*avg_abs+avg_square
        matrices.append({"name":name,"mean_abs_residual":str(avg_abs),
                         "mean_square_residual":str(avg_square),"Boolean_closure_defect":str(defect),
                         "exact_bound":str(2*avg_abs+avg_square),"passed":True})
    return matrices


def main():
    result = {
        "scope":"Exact rational examples and algebra checks; paper headline theorems remain unreviewed",
        "discrete_energy": [
            discrete_energy([3,-1,2,-2,F(1,3)], [0,F(1,2),F(3,4)], [0,0,0]),
            discrete_energy([0,0,0], [F(1,2),F(3,4)], [2,-3]),
            discrete_energy([3,-1,2,-2,F(1,3)], [0,F(1,2),F(3,4)], [0,0,0],
                            [F(1,n*n) for n in range(4,9)]),
        ],
        "riesel":riesel_preservation(), "Boolean_closure":sign_residual(),
    }
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
