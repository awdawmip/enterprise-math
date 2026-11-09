#!/usr/bin/env python3
"""Exact finite-horizon Bayes risk on frozen S23/AV circle rotation.
Relies on independently certified enclosure P/Q < theta < (P+1)/Q
from the predecessor proof at enterprise-math@3d1e430b8590cbcb08be3dc626ac73940444c33e.
All classification and comparisons use integers; no floating-point decisions.
"""
P = 262204504569236716045286
Q = 10**24


def bounds(a, b):
    """Bounds in Q units of affine a+b*theta."""
    x, y = a*Q+b*P, a*Q+b*(P+1)
    return min(x,y), max(x,y)


def phase(j):
    if j == 0:
        return (0, 0)
    assert j*P//Q == j*(P+1)//Q
    floor = j*P//Q
    expr = (floor+1, -j)
    lo, hi = bounds(*expr)
    assert 0 < lo <= hi < Q
    return expr


def subtract(v,u,wrap=False):
    return (v[0]-u[0]+int(wrap),v[1]-u[1])


def certify(m, horizon):
    count = m+horizon
    cuts = [(phase(j),j) for j in range(count)]
    cuts.sort(key=lambda row: bounds(*row[0])[0])
    assert all(bounds(*cuts[i][0])[1]<bounds(*cuts[i+1][0])[0]
               for i in range(count-1))
    old_indices = [i for i,(_,j) in enumerate(cuts) if j<m]
    best_total=(0,0)
    branch_lengths=[]
    for oldpos, start in enumerate(old_indices):
        following = old_indices[(oldpos+1)%m]
        end=following if following>start else following+count
        gaps=[]
        for z in range(start,end):
            (start_e,_),(end_e,_) = cuts[z%count], cuts[(z+1)%count]
            gaps.append(subtract(end_e,start_e,(z+1)>=count))
        winners=[g for g in gaps if all(bounds(*g)[0]>bounds(*h)[1]
                    for h in gaps if h is not g)]
        if len(gaps)==1:
            winner=gaps[0]
        else:
            assert len(winners)==1, (m,horizon,start,'uncertified winner',gaps)
            winner=winners[0]
        best_total=(best_total[0]+winner[0],best_total[1]+winner[1])
        if len(gaps)>1:
            branch_lengths.append((cuts[start][1],tuple(cuts[z%count][1]
                                               for z in range(start+1,end)),gaps))
    risk=subtract((1,0),best_total)
    lo,hi=bounds(*risk)
    assert 0<=lo<=hi<=Q
    return risk,(lo,hi),branch_lengths


def main():
    delta=(16,-61)
    lam=(-43,164)
    for m in (4,19,61,128,717):
        r,iv,_=certify(m,1)
        print('CERT_SINGLE',m,r,iv,flush=True)
    for L in range(1,37):
        expr,iv,_=certify(128,L)
        assert expr==(L*delta[0],L*delta[1]),(L,expr)
    print('CERT_LINEAR_HORIZON m=128 L=1..36 risk=L*(16-61*theta)',flush=True)
    expr,iv,detail=certify(128,37)
    expect=(36*delta[0]+lam[0],36*delta[1]+lam[1])
    assert expr==expect==(533,-2032)
    assert lam[0]*Q+lam[1]*P>0
    exceptional=[d for d in detail if 164 in d[1]]
    assert len(exceptional)==1 and exceptional[0][0]==103
    print('CERT_FIRST_DEVIATION m=128 L=37 risk=533-2032*theta',flush=True)
    for m,L in ((61,8),(128,36),(128,37),(717,16)):
        expr,(lo,hi),_ = certify(m,L)
        print('CERT_RISK',f'm={m}',f'L={L}',f'affine={expr}',
              f'interval=({lo}/{Q},{hi}/{Q})',flush=True)
    print('PASS_S23_AV_FINITE_HORIZON_CERTIFIED',flush=True)


if __name__=='__main__':
    main()
