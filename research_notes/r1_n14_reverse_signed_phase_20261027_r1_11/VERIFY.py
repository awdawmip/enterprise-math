#!/usr/bin/env python3
"""Exact rational check of external finite two-law support formulas; not native X6."""
from fractions import Fraction as F
from itertools import product

ALPHA, BETA, GAMMA, DELTA = map(F, (68, 84, 7, -3))
BASE_R = {"":F(1),"a":F(3,2),"b":F(1,2),"ax":F(1),"ay":F(2),"bu":F(1),"bv":F(1,3)}
BASE_Q = {"":F(1),"a":F(1,2),"b":F(1,2),"ax":F(1,4),"ay":F(1,4),"bu":F(1,8),"bv":F(3,8)}
CH = {"":("a","b"),"a":("ax","ay"),"b":("bu","bv"),"ax":("axl","axm","axh"),
      "bu":("bul","bum","buh"),"ay":("aym",),"bv":("bvm",)}
def plus(x):
    return max(F(0),x)
def model(sa,sb):
    assert F(0)<sa<F(1,2) and F(0)<sb<F(1,2)
    r,q=dict(BASE_R),dict(BASE_Q)
    for h,s in (("ax",sa),("bu",sb)):
        for suf,ratio,w in (("l",F(1,2),s),("m",F(1),1-2*s),("h",F(3,2),s)):
            r[h+suf],q[h+suf]=ratio,q[h]*w
    for h in ("ay","bv"):
        r[h+"m"],q[h+"m"]=r[h],q[h]
    assert len(q)==15 and len([h for h in q if h not in CH])==8
    assert all(x>0 for x in q.values())
    for h,cs in CH.items():
        assert sum((q[c] for c in cs),F(0))==q[h]
        assert sum((q[c]*r[c] for c in cs),F(0))==q[h]*r[h]
    leaves=[h for h in q if h not in CH]
    assert sum((q[h] for h in leaves),F(0))==1
    assert sum((q[h]*r[h] for h in leaves),F(0))==1
    return r,q
def bellman(sa,sb,forced=None):
    r,q=model(sa,sb)
    def solve(h):
        rr=r[h]
        options={"P":BETA,"Q":ALPHA*rr}
        if h in CH:
            options["C"]=GAMMA*rr+DELTA+sum((q[c]/q[h]*solve(c) for c in CH[h]),F(0))
        if forced is not None and h in ("ax","bu"):
            return options[forced]
        return min(options.values())
    return solve("")
def closed(sa,sb):
    full=F(251,4)-plus(18*sa-4)/4-plus(18*sb-4)/8
    coarse=min(F(251,4),F(63)-plus(9*sa-F(3,2))/2-plus(F(9,2)*sb-1)/2)
    gap=min(plus(F(9,4)*sb-F(1,2)),plus(min(F(1,4),1-F(9,2)*sa)))
    return full,coarse,gap
grid=(F(1,100),F(1,10),F(1,6),F(1,5),F(2,9),
      F(1,4),F(5,18),F(1,3),F(2,5),F(49,100))
for sa,sb in product(grid,repeat=2):
    f=bellman(sa,sb)
    c=min(bellman(sa,sb,x) for x in ("P","Q","C"))
    assert (f,c,c-f)==closed(sa,sb),(sa,sb,f,c)
    assert (c>f)==(sa<F(2,9) and sb>F(2,9))
    assert F(0)<=c-f<=F(1,4)
assert closed(F(1,6),F(1,3))==(F(125,2),F(251,4),F(1,4))
assert [bellman(F(1,6),F(1,3),x) for x in ("P","Q","C")]==[F(63),F(251,4),F(251,4)]
assert closed(F(2,9),F(1,3))[2]==0
assert closed(F(1,6),F(2,9))[2]==0
assert closed(F(1,6),F(2,5))[2]==F(1,4)
print("PASS_EXACT_FRACTION")
print("NODES 15 POSITIVE_LEAVES 8 GRID 100 BOUNDARIES 1/6 2/9 1/3 5/18")
print("NORMAL (68,84,7,-3) OBS (P_decide_Q,Q_decide_P,E_P_tau,E_Q_tau)")
print("POINT sa=1/6 sb=1/3 FULL 125/2 COMPRESSED 251/4 GAP 1/4")
print("STRICT_REGION sa<2/9 AND sb>2/9")
print("GLOBAL_MAX 1/4 attained for sa<=1/6 AND sb>=1/3")
