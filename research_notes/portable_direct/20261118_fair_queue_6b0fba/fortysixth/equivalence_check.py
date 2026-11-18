#!/usr/bin/env python3
"""Sharp two-alloy composition bounds and prospective design; exact rationals."""
from fractions import Fraction as F
from itertools import combinations, product
import json

NAMES = ('Ti','Al','V','Pt','Rh')
A = (F(9,10),F(3,50),F(1,25),F(0),F(0))
B = (F(0),F(0),F(0),F(9,10),F(1,10))
PURE = [tuple(F(i==j) for j in range(5)) for i in range(5)]


def dot(x,y):
    return sum(a*b for a,b in zip(x,y))


def eta(R):
    return F(2)*(R-1)/(R+1)


def ratio(e):
    return (2+e)/(2-e)


def rays(R,d=5):
    for i in range(3):
        for j in range(3,5):
            v = [F(0)]*d
            v[i],v[j] = R/A[i],1/B[j]
            yield v
    for i in range(5,d):
        yield [F(i==j) for j in range(d)]


def evaluate(R,P,Q,factor=F(1)):
    finite = []
    infinity = False
    skipped = 0
    for v in rays(R,len(P)):
        num,den = factor*dot(P,v),dot(Q,v)
        if den:
            finite.append(num/den)
        elif num:
            infinity = True
        else:
            skipped += 1
    return min(finite),None if infinity else max(finite),skipped


def interval(P,Q,Rbox,err=None,pid='P',qid='Q'):
    roles = ('A','B',pid,qid)
    labels = sorted(set(roles))
    if err is None:
        err = {k:(F(1),) for k in labels}
    lows,highs = [],[]
    for R_obs in Rbox:
        for corner in product(*(err[k] for k in labels)):
            mult = dict(zip(labels,corner))
            R = R_obs*mult['B']/mult['A']
            lo,hi,_ = evaluate(R,P,Q,mult[pid]/mult[qid])
            lows.append(lo)
            highs.append(hi)
    return min(lows), None if None in highs else max(highs)


def rank(A):
    rows = [list(r) for r in A]
    d = 0
    for col in range(len(rows[0])):
        i = next((i for i in range(d,len(rows)) if rows[i][col]),None)
        if i is None:
            continue
        rows[d],rows[i] = rows[i],rows[d]
        for i in range(d+1,len(rows)):
            t = rows[i][col]/rows[d][col]
            rows[i] = [a-t*b for a,b in zip(rows[i],rows[d])]
        d += 1
    return d


def design():
    options = []
    for measured in combinations(range(5),3):
        r = rank([A,B]+[PURE[i] for i in measured])
        if r<5:
            continue
        u = next(i for i in range(3) if i not in measured)
        v = next(j for j in range(3,5) if j not in measured)
        gain = max(1,(2-A[u])/A[u],(1-B[v])/B[v])
        gains = []
        for e0,*es in product((-1,1),repeat=4):
            errors = dict(zip(measured,es))
            errors[u] = (e0-sum(A[i]*errors[i] for i in measured))/A[u]
            errors[v] = -sum(B[i]*errors[i] for i in measured)/B[v]
            gains.append(max(abs(z) for z in errors.values()))
        assert gain == max(gains)
        options.append(dict(measured=[NAMES[i] for i in measured],gain=gain))
    winner = min(options,key=lambda v:v['gain'])
    assert winner == dict(measured=['Al','V','Rh'],gain=F(11,9))
    return options


def main():
    lo,hi=(F(-53,10**16),F(23,10**16))  # 1 stated statistical sigma plus stated systematic bound.
    Rbox = ratio(lo),ratio(hi)
    assert (eta(Rbox[0]),eta(Rbox[1])) == (lo,hi)
    assert interval(A,B,Rbox) == Rbox
    new = (F(89,100),F(7,100),F(4,100),F(0),F(0))
    assert evaluate(F(1),new,B)[:2] == (F(89,90),F(7,6))
    assert tuple(eta(z) for z in evaluate(F(1),new,B)[:2]) == (F(-2,179),F(2,13))
    assert evaluate(F(1),PURE[0],B)[:2] == (0,F(10,9))
    assert evaluate(F(1),PURE[0],PURE[3]) == (0,None,2)
    P6,Q6 = (0,0,0,0,0,1),(*B,0)
    assert evaluate(F(1),P6,Q6)[:2] == (0,None)
    err = {k:(F(99,100),F(101,100)) for k in ['A','B','Ti']}
    assert interval(A,B,Rbox,err,'A','B') == Rbox
    assert interval(PURE[0],B,[F(1)],err,'Ti','B') == (0,F(1010,891))
    # Different positive component vectors, exactly identical calibration outputs.
    g1 = [F(1)]*5
    g2 = [F(19,18),F(1,2),F(1,2),F(1),F(1)]
    assert dot(A,g1) == dot(B,g1) == dot(A,g2) == dot(B,g2) == 1
    # Strictly positive parameters provide independent interior checks.
    count = 0
    targets = [(A,B),(PURE[0],B),(PURE[0],PURE[3]),(new,B),(PURE[1],PURE[2])]
    for R in [F(1,2),F(1),F(3,2)]:
        for w1,w2,w3 in product(range(1,7),repeat=3):
            if w1+w2 >= 8:
                continue
            x,y = [F(w1,8),F(w2,8),F(8-w1-w2,8)],[F(w3,8),F(8-w3,8)]
            g = [R*z/a for z,a in zip(x,A)]+[z/b for z,b in zip(y,B[3:])]
            assert dot(B,g) == 1 and dot(A,g) == R
            for P,Q in targets:
                l,h,_ = evaluate(R,P,Q)
                result = dot(P,g)/dot(Q,g)
                assert l <= result and (h is None or result <= h)
                count += 1
    # Directly test correlated discrepancies for distinct/read-again materials.
    nerr = 0
    for a,b,c in product((F(99,100),F(1),F(101,100)),repeat=3):
        for R in [Rbox[0],sum(Rbox)/2,Rbox[1]]:
            rul = R*b/a
            for P,Q,pid,qid,mul in [(A,B,'A','B',a/b),(PURE[0],B,'Ti','B',c/b),
                                      (B,PURE[0],'B','Ti',b/c)]:
                l,h,_ = evaluate(rul,P,Q,mul)
                L,H = interval(P,Q,Rbox,err,pid,qid)
                assert L <= l and (H is None or (h is not None and h<=H))
                nerr += 1
    out=dict(component_order=NAMES,nominal_mass_fractions=[A,B],conditional_eta_window=[lo,hi],
             equivalent_R_window=Rbox,exact_null_enrichment_eta=[F(-2,179),F(2,13)],
             exact_null_pure_Ti_vs_reference_ratio=[0,F(10,9)],
             pure_Ti_vs_pure_Pt_ratio_closure=[0,'infinity'],
             pure_Ti_with_shared_reference_error_upper=F(1010,891),
             equal_calibration_witnesses=[g1,g2],strict_interior_target_checks=count,
             shared_error_calibration_checks=nerr,pure_designs=design())
    print(json.dumps(out,default=str,sort_keys=True,indent=2))


if __name__ == '__main__':
    main()
