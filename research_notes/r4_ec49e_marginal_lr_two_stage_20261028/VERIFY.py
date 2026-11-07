#!/usr/bin/env python3
"""EC49E exact integer exhaustive verifier; auxiliary positive BRC observer only."""
from __future__ import annotations
import itertools
import json
from fractions import Fraction

# Order of y1,y2 is (1,1), (1,0), (0,1), (0,0).
# Unconditional source masses are integer numerators with common denominator 40.
P = ((14, 1, 1, 4), (11, 4, 4, 1))
Q = ((4, 1, 1, 14), (1, 4, 4, 11))
LABELS = ((1, 1), (1, 0), (0, 1), (0, 0))
LEAVES = []
for w in range(2):
    for i, (y1, y2) in enumerate(LABELS):
        p, q = P[w][i], Q[w][i]
        LEAVES.append((w, y1, y2, p, q, Fraction(p, q)))
assert sum(z[3] for z in LEAVES) == sum(z[4] for z in LEAVES) == 40
assert all(p > 0 and q > 0 for _, _, _, p, q, _ in LEAVES)
assert all(sum(P[w]) == sum(Q[w]) == 20 for w in range(2))

# Every W-fiber has the same one-step *marginal* LR spectrum for both Y1 and Y2.
def marginal_spectrum(w, which):
    ans = {}
    for value in (0, 1):
        chosen = [z for z in LEAVES if z[0] == w and z[which] == value]
        p, q = sum(z[3] for z in chosen), sum(z[4] for z in chosen)
        ans[str(Fraction(p, q))] = Fraction(q, 20)
    return ans

for i in (1, 2):
    assert marginal_spectrum(0, i) == marginal_spectrum(1, i)
    assert marginal_spectrum(0, i) == {'1/3': Fraction(3, 4), '3': Fraction(1, 4)}

# Joint source LRs: (W=0) 7/2,1,1,2/7 and (W=1) 11,1,1,1/11.
assert [str(z[5]) for z in LEAVES] == ['7/2','1','1','2/7','11','1','1','1/11']
# At T=2 the accessible complete prefix LR is 3 for Y1=1, else 1/3.
assert all(Fraction(sum(z[3] for z in LEAVES if z[0]==w and z[1]==y),
                    sum(z[4] for z in LEAVES if z[0]==w and z[1]==y)) == (Fraction(3) if y else Fraction(1,3))
           for w in (0,1) for y in (0,1))

# Deterministic policy: 0 reject, 1 accept, 2 continue. At T=3 no continue.
# Coarse states: T1 singleton; T2 L1 in {3,1/3}; T3 full joint LR in five states.
# Refined states: T1 W; T2 (W,L1); T3 (W,L2).
COARSE_LR3 = tuple(sorted(set(z[5] for z in LEAVES)))
FINE_LR3 = tuple((w, r) for w in (0, 1) for r in sorted(set(z[5] for z in LEAVES if z[0]==w)))
assert len(COARSE_LR3) == 5 and len(FINE_LR3) == 6 # W+LR merges two off-diagonal leaves for each W

def deterministic_observations(refined):
    stage1_states = (0,1) if refined else (0,)
    stage2_states = tuple((w,y) for w in (0,1) for y in (0,1)) if refined else (0,1)
    stage3_states = FINE_LR3 if refined else COARSE_LR3
    for a in itertools.product((0,1,2), repeat=len(stage1_states)):
        first = dict(zip(stage1_states, a))
        for b in itertools.product((0,1,2), repeat=len(stage2_states)):
            second = dict(zip(stage2_states, b))
            for t in itertools.product((0,1), repeat=len(stage3_states)):
                terminal = dict(zip(stage3_states, t))
                pa=qa=pt=qt=0
                for w, y1, y2, p, q, lr in LEAVES:
                    act1 = first[w if refined else 0]
                    if act1 == 2:
                        act2 = second[(w,y1) if refined else y1]
                        if act2 == 2:
                            act3 = terminal[(w,lr) if refined else lr]
                            time = 3
                            accepted = act3
                        else:
                            time = 2
                            accepted = act2
                    else:
                        time = 1
                        accepted = act1
                    pa += p*accepted
                    qa += q*accepted
                    pt += p*time
                    qt += q*time
                yield pa,qa,pt,qt

GRID=[Fraction(0), Fraction(1,40), Fraction(1,20), Fraction(3,40),
      Fraction(1,10),Fraction(1,8),Fraction(2,15),Fraction(7,50),
      Fraction(3,20),Fraction(1,5),Fraction(1,3)]

def predicted(refined,c):
    d=Fraction(1,4)
    gains=(Fraction(1,20),Fraction(1,5))
    plus=lambda x:max(Fraction(0),x)
    if refined:
        return sum((plus(d-2*c+plus(g-c)) for g in gains),Fraction(0))/2
    return plus(d-2*c+plus(Fraction(1,8)-c))

results={}
for refined in (False,True):
    count=0
    best={c:None for c in GRID}
    maximizer={}
    for pa,qa,pt,qt in deterministic_observations(refined):
        count+=1
        for c in GRID:
            val = Fraction(pa-2*qa,40)-c*Fraction(pt+qt-80,40)
            if best[c] is None or val>best[c]:
                best[c]=val
                maximizer[c]=(pa,qa,pt,qt)
    assert all(best[c]==predicted(refined,c) for c in GRID), (refined,best)
    results['refined' if refined else 'coarse']={
        'deterministic_policies':count,
        'support_by_cost':{str(c):str(best[c]) for c in GRID},
        'witness_at_c_1_over_8':list(map(str,maximizer[Fraction(1,8)]))
    }
assert results['coarse']['deterministic_policies']==3*(3**2)*(2**5)==864
assert results['refined']['deterministic_policies']==(3**2)*(3**4)*(2**6)==46656
# Both optimize over all behaviorally randomized policies: each randomized node
# is a convex combination of deterministic local actions, and finite expansion
# is a mixture of global deterministic policies. Hence support is exhaustive.
assert predicted(False,Fraction(1,8)) == 0
assert predicted(True,Fraction(1,8)) == Fraction(3,80)

# Explicit fine policy: reject at T1 for W=0, buy Y1 for W=1; when
# W=1,Y1=1 buy Y2 and accept exactly when complete terminal LR=11.
def witness():
    pa=qa=pt=qt=0
    for w,y1,y2,p,q,lr in LEAVES:
        if w==0:
            t,a=1,0
        elif y1==0:
            t,a=2,0
        else:
            t,a=3,int(lr==11)
        pa+=p*a;qa+=q*a;pt+=p*t;qt+=q*t
    return pa,qa,pt,qt
assert witness()==(11,1,75,65)
assert Fraction(11,40)-2*Fraction(1,40)-Fraction(1,8)*(Fraction(75+65,40)-2)==Fraction(3,80)

# Sharp gap: positive exactly for 1/20<c<3/20. Boundary values checked.
def explicit_gap(c):
    if c<=Fraction(1,20) or c>=Fraction(3,20): return Fraction(0)
    if c<=Fraction(1,8): return c/2-Fraction(1,40)
    return Fraction(9,40)-3*c/2
assert all(predicted(True,c)-predicted(False,c)==explicit_gap(c) for c in GRID)
assert all(v>0 for v in [explicit_gap(Fraction(3,40)),explicit_gap(Fraction(1,8)),explicit_gap(Fraction(7,50))])

out={
 'model':'EC49E_8_LEAF_TWO_FUTURE_INFORMATIVE_SIGNALS',
 'leaves':[{ 'w':w,'y1':y1,'y2':y2,'P':str(Fraction(p,40)),'Q':str(Fraction(q,40)),'full_LR':str(lr)} for w,y1,y2,p,q,lr in LEAVES],
 'one_step_marginal_LR_Q_law':{ 'Y1':{k:str(v) for k,v in marginal_spectrum(0,1).items()},'Y2':{k:str(v) for k,v in marginal_spectrum(0,2).items()}},
 'results':results,
 'support_gap_at_c_1_over_8':'3/80',
 'sharp_positive_gap_interval':'1/20 < c < 3/20',
 'explicit_fine_witness_raw_four_vector':['11/40','1/40','15/8','13/8'],
 'all_deterministic_policies_enumerated':results['coarse']['deterministic_policies']+results['refined']['deterministic_policies'],
 'verification':'PASS_EXACT_INTEGER_AND_FRACTION'
}
print(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
