#!/usr/bin/env python3
"""Exact Fraction regression for a source-blind merged LR node (R5)."""
from collections import defaultdict
from fractions import Fraction as F
from json import dumps
from random import Random

S = (F(1, 2), F(1), F(3, 2), F(5, 2))
mu = {
    "A": (F(7, 50), F(11, 75), F(1, 2), F(16, 75)),
    "B": (F(17, 200), F(23, 150), F(3, 5), F(97, 600)),
}
nu = {
    ("A", "L"): (F(1, 2), F(1, 6), F(1, 4), F(1, 12)),
    ("B", "L"): (F(5, 12), F(1, 3), F(1, 6), F(1, 12)),
    ("A", "R"): (F(17, 100), F(23, 75), F(1, 5), F(97, 300)),
    ("B", "R"): (F(31, 120), F(5, 18), F(1, 15), F(143, 360)),
}
eta = (F(1, 8), F(1, 4), F(3, 8), F(1, 4))
assert all(sum(a) == 1 for a in (eta, *mu.values(), *nu.values()))
assert all(sum(s*w for s,w in zip(S, mu[o])) == F(3, 2) for o in mu)
assert all(sum(s*w for s,w in zip(S, nu[o, b])) == (F(1) if b == "L" else F(3, 2)) for o,b in nu)
assert sum(s*w for s,w in zip(S, eta)) == F(3, 2)


def distribution(p, q, gamma, a=F(1)):
    """Q terminal (t,s)-cell masses, 0 <= p,q <= root survival a <= 1."""
    assert F(0) <= p <= a <= F(1) and F(0) <= q <= a and F(0) <= gamma <= F(1)
    W = defaultdict(F)
    W[(1, F(1, 2))] += F(1, 2)
    W[(1, F(3, 2))] += F(1, 2) * (1-a)
    source_x = defaultdict(F)
    source_y = defaultdict(F)
    for origin in ("A", "B"):
        for ratio, weight in zip(S, mu[origin]):
            mass = F(1, 4) * weight
            if ratio not in (F(1), F(3, 2)):
                W[(2, ratio)] += mass * a
                continue
            flow = p if ratio == F(1) else q
            W[(2, ratio)] += mass * (a - flow)
            label = "L" if ratio == F(1) else "R"
            for next_ratio, second_weight in zip(S, nu[origin, label]):
                qmass = mass * flow * second_weight
                if next_ratio == F(3, 2):
                    source_x[origin] += qmass
                    source_y[origin] += qmass * gamma
                    W[(3, next_ratio)] += qmass * (1 - gamma)
                    for final_ratio, final_weight in zip(S, eta):
                        W[(4, final_ratio)] += qmass * gamma * final_weight
                else:
                    W[(3, next_ratio)] += qmass
    assert sum(W.values()) == 1
    assert sum(s*w for (t,s),w in W.items()) == 1
    return dict(W), dict(source_x), dict(source_y)


def terminal_decision(W, variant):
    index={s:i+1 for i,s in enumerate(S)}
    return {cell: mass * (F((cell[0]+index[cell[1]]) if variant == "F" else (2*cell[0]+index[cell[1]]), (12 if variant == "F" else 13))) for cell,mass in W.items()}


def obs(W, m):
    return (
        F(1)-sum(s*m.get((t,s), F(0)) for t,s in W),
        sum(m.values()),
        sum(t*s*weight for (t,s),weight in W.items()),
        sum(t*weight for (t,s),weight in W.items()),
    )

W_F, x_F, y_F = distribution(F(1), F(0), F(1))
W_G, x_G, y_G = distribution(F(0), F(1), F(0))
v=sum(x_F.values()); w=sum(x_G.values())
gamma_mid=v/(v+w)
assert gamma_mid==F(4, 13)
W_H, x_H, y_H = distribution(F(1,2), F(1,2), gamma_mid)
keys = set(W_F)|set(W_G)|set(W_H)
assert all(W_H.get(k, F(0)) == (W_F.get(k,F(0))+W_G.get(k,F(0)))/2 for k in keys)

# Wedges differ at the source-vector level, but agree after observer quotient.
x_target={o:(x_F.get(o,F(0))+x_G.get(o,F(0)))/2 for o in ("A","B")}
y_target={o:(y_F.get(o,F(0))+y_G.get(o,F(0)))/2 for o in ("A","B")}
assert x_H == x_target
assert y_H != y_target
wedge=y_target["A"]*x_target["B"] - y_target["B"]*x_target["A"]
assert wedge==F(-49, 2880000), wedge
assert sum(y_H.values()) == sum(y_target.values())

mF=terminal_decision(W_F,"F"); mG=terminal_decision(W_G,"G")
mH={k:(mF.get(k,F(0))+mG.get(k,F(0)))/2 for k in keys}
assert all(0<=mH[k]<=W_H.get(k,F(0)) for k in keys)
O_F=obs(W_F,mF); O_G=obs(W_G,mG); O_H=obs(W_H,mH)
assert all(a==(b+c)/2 for a,b,c in zip(O_H,O_F,O_G))

# Independent exact-rational stress: interpolate two behavioral policies by
# their prefix survivals and the scalar postmerge continued mass.
rng=Random(41029)
for _ in range(240):
    def r(): return F(rng.randrange(1, 19), 20)
    a1,a2=r(),r()
    p1,q1=a1*r(),a1*r()
    p2,q2=a2*r(),a2*r()
    g1,g2=r(),r()
    lam=r()
    U1,_,_=distribution(p1,q1,g1,a1)
    U2,_,_=distribution(p2,q2,g2,a2)
    x1=v*p1+w*q1
    x2=v*p2+w*q2
    xmix=lam*x1+(1-lam)*x2
    zmix=lam*g1*x1+(1-lam)*g2*x2
    amid=lam*a1+(1-lam)*a2
    pmid=lam*p1+(1-lam)*p2
    qmid=lam*q1+(1-lam)*q2
    gmid=zmix/xmix if xmix else F(0)
    Umid,_,_=distribution(pmid,qmid,gmid,amid)
    cells=set(U1)|set(U2)|set(Umid)
    assert all(Umid.get(k,F(0)) == lam*U1.get(k,F(0))+(1-lam)*U2.get(k,F(0)) for k in cells)
    d1=terminal_decision(U1,'F')
    d2=terminal_decision(U2,'G')
    dmid={k:lam*d1.get(k,F(0))+(1-lam)*d2.get(k,F(0)) for k in cells}
    assert all(F(0)<=dmid[k]<=Umid.get(k,F(0)) for k in cells)
    omid=obs(Umid,dmid)
    o1=obs(U1,d1);o2=obs(U2,d2)
    assert all(m==lam*u+(1-lam)*z for m,u,z in zip(omid,o1,o2))

result={
 "status":"PASS_EXACT_R5_SOURCE_BLIND_DIAMOND_OBSERVER_QUOTIENT",
 "checks":{"mean_normalizations":True,"terminal_mass_normalization_both_laws":True,"full_terminal_Q_law_midpoint":True,"randomized_declaration_midpoint":True,"four_observer_midpoint":True,"source_resolved_midpoint_infeasible":True,"exact_rational_policy_mixture_stress_240":True},
 "input":{"source_vectors_v":{o:str(x_F[o]) for o in ("A","B")},"source_vectors_w":{o:str(x_G[o]) for o in ("A","B")},"policy_F":["1","0","1"],"policy_G":["0","1","0"],"policy_H":["1/2","1/2",str(gamma_mid)]},
 "source_wedge":str(wedge),
 "positive_terminal_cell_count":sum(W_H.get(k,F(0))>0 for k in keys),
 "four_observations":{"F":[str(v) for v in O_F],"G":[str(v) for v in O_G],"midpoint_H":[str(v) for v in O_H]},
 "scientific_scope":"finite two-measure LR diamond; common source-blind final kernel eta; no native X6 or canonical review",
 "formal_admission":"NOT_ADMITTED",
}
print(dumps(result,indent=2,ensure_ascii=False))
