#!/usr/bin/env python3
"""Exact rational regression for a stochastic C->L detour in the R5 two-merger model.

This is an auxiliary finite, positive-weight Q/P BRC path model, NOT native-X6
arithmetic or a formal admission checker. Universal statements are proved in
RESEARCH.md; finite enumerations below check the specified rational witnesses.
"""
from fractions import Fraction as F
from itertools import product

ONE, ZERO, HALF = F(1), F(0), F(1, 2)


def observe(a0, a1, k, policy, lr=False):
    """Return TP,TQ and exact total P,Q masses from terminal paths.

    FULL policy order: A0,A1,D0,D1,Y0,Y1,L0C,L0D,L0Y,L1C,L1D,L1Y
    LR policy order: A,D,Y,L (all origins and L-entry routes share action).
    Bit zero means STOP, one CONTINUE; C splits naturally, not by policy.
    """
    TP = TQ = PP = QQ = ZERO

    def terminal(q, lam, t):
        nonlocal TP, TQ, PP, QQ
        p = q * lam
        TP += p * t
        TQ += q * t
        PP += p
        QQ += q

    def act(i, key):
        if lr:
            return policy[{"A": 0, "D": 1, "Y": 2, "L": 3}[key[0]]]
        base = {"A": i, "D": 2+i, "Y": 4+i}
        return policy[base[key]] if key in base else policy[6 + 3*i + {"LC":0, "LD":1, "LY":2}[key]]

    for i, a in enumerate((a0, a1)):
        q = HALF
        if not act(i, "A"):
            terminal(q, ONE, 1)
            continue
        d = q*a
        c = q*(ONE - 2*a)
        y = q*a
        if not act(i, "D"):
            terminal(d, HALF, 2)
        else:
            terminal(d*F(2,3), F(1,4), 3)
            terminal(d*F(1,3), ONE, 3 + act(i,"LD"))
        # C makes a nature-driven terminal/pass split, both branches positive.
        terminal(c*(ONE-k), ONE, 2)
        terminal(c*k, ONE, 3 + act(i,"LC"))
        if not act(i, "Y"):
            terminal(y, F(3,2), 2)
        else:
            terminal(y*HALF, F(2), 3)
            terminal(y*HALF, ONE, 3 + act(i,"LY"))
    return TP, TQ, PP, QQ


def tuned_direction(a0,a1,k):
    s=(a0+a1)/2
    u=2*(ONE+k-s*(2*k-ONE))
    v=-u-s
    assert u>0 and u/2-s>0 and -s<0
    return u,v


def gap_formula(a0,a1,k):
    return (ONE+k)*abs(a0-a1)/4


def cross(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def hull(points):
    pts=sorted(set(points))
    if len(pts)<=1: return pts
    lo=[]
    for p in pts:
        while len(lo)>1 and cross(lo[-2],lo[-1],p)<=0:lo.pop()
        lo.append(p)
    up=[]
    for p in reversed(pts):
        while len(up)>1 and cross(up[-2],up[-1],p)<=0:up.pop()
        up.append(p)
    return lo[:-1]+up[:-1]


def inside(poly,p):
    if len(poly)==1:return p==poly[0]
    if len(poly)==2:return cross(poly[0],poly[1],p)==0 and min(poly[0][0],poly[1][0])<=p[0]<=max(poly[0][0],poly[1][0]) and min(poly[0][1],poly[1][1])<=p[1]<=max(poly[0][1],poly[1][1])
    return all(cross(poly[i],poly[(i+1)%len(poly)],p)>=0 for i in range(len(poly)))


def run(a0,a1,k,check_hull=False):
    assert ZERO<a0<HALF and ZERO<a1<HALF and ZERO<k<ONE
    u,v=tuned_direction(a0,a1,k)
    full_max=None; lr_max=None; witness=None; full_points=[]; lr_points=[]
    for bits in product((0,1),repeat=4):
        tp,tq,pm,qm=observe(a0,a1,k,bits,True)
        assert (pm,qm)==(ONE,ONE)
        score=u*tp+v*tq
        lr_max=score if lr_max is None or score>lr_max else lr_max
        lr_points.append((tp,tq))
    for bits in product((0,1),repeat=12):
        tp,tq,pm,qm=observe(a0,a1,k,bits,False)
        assert (pm,qm)==(ONE,ONE)
        score=u*tp+v*tq
        if full_max is None or score>full_max:
            full_max=score;witness=(bits,tp,tq)
        if check_hull:full_points.append((tp,tq))
    expected=gap_formula(a0,a1,k)
    assert lr_max==-(a0+a1)/2, (lr_max,-(a0+a1)/2)
    assert full_max-lr_max==expected,(a0,a1,k,full_max,lr_max,expected)
    if check_hull:
        poly=hull(lr_points)
        assert all(inside(poly,p) for p in full_points),"FULL vertex outside LR time hull"
        assert len(poly)>=3
    return full_max,lr_max,expected,witness,(u,v),len(hull(lr_points))


def main():
    # Stress tests include the old H kink-exit regime k>3/4.
    cases=[
        (F(1,4),F(1,8),F(1,20)),
        (F(1,4),F(1,8),F(1,4)),
        (F(1,4),F(1,8),F(3,4)),
        (F(1,4),F(1,8),F(9,10)),
        (F(1,8),F(1,4),F(9,10)),
        (F(1,3),F(1,5),F(2,3)),
        (F(1,7),F(1,9),F(7,8)),
        (F(1,4),F(1,4),F(1,4)),
        (F(1,8),F(1,8),F(9,10)),
    ]
    for j,(a0,a1,k) in enumerate(cases,1):
        fm,lm,g,w,uv,n=run(a0,a1,k,check_hull=a0==a1)
        print(f"case{j:02d} a0={a0} a1={a1} k={k} H={uv} LR={lm} FULL={fm} gap={g} LR_hull_vertices={n}")
    a0,a1,k=F(1,4),F(1,8),F(1,4)
    fm,lm,g,_,(u,v),_=run(a0,a1,k)
    # Explicit FULL maximizer: A0 CONTINUE, A1 STOP; D STOP, Y CONTINUE;
    # all L STOP. This tests a concrete witness without relying on argmax search.
    p=(1,0,0,0,1,0,0,0,0,0,0,0)
    tp,tq,pm,qm=observe(a0,a1,k,p)
    assert (tp,tq,pm,qm)==(F(7,4),F(27,16),ONE,ONE)
    assert (16*u,16*v)==(F(43),F(-46))
    assert 43*tp-46*tq==F(-19,8)
    assert 16*lm==F(-3) and 16*fm==F(-19,8)
    assert 16*g==F(5,8)
    # L_inf separation by dual Hölder bound for all real LR behavioral policies.
    assert (16*g)/(abs(16*u)+abs(16*v))==F(5,712)
    print("fixed_witness: O_time=(7/4,27/16), J=43 T_P - 46 T_Q, support_FULL=-19/8, support_LR=-3")
    print("exact_L_infinity_distance_lower_bound=5/712")
    print("FULL_policies_per_case=4096 LR_policies_per_case=16 cases=9")
    print("PASS_EXACT_R5_C_TO_L_DETOUR_TIME_HULL_RIGIDITY")


if __name__=='__main__':main()
