#!/usr/bin/env python3
"""Certified rotation best-return risks for frozen S23/AV auxiliary observer.
All logical decisions use Fraction/integer arithmetic, never float.
Frozen science: enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
"""
from fractions import Fraction

B=79
Q=10**24
SCALE=10**18
MAX_SCAN=200000


def log_iv(a,b,n=160):
    x=Fraction(a-b,a+b)
    term=x
    lo=Fraction(0)
    for j in range(n):
        lo+=2*term/(2*j+1)
        term*=x*x
    return lo,lo+2*term/((2*n+1)*(1-x*x))


def certified_theta():
    l7,u7=log_iv(7,1)
    l107,u107=log_iv(10,7)
    den_l=79*l7-431*u107
    den_u=79*u7-431*l107
    num_l=2074774*l107-380295*u7
    num_u=2074774*u107-380295*l7
    assert 0<den_l<den_u and 0<num_l<num_u
    al,au=num_l/den_u,num_u/den_l
    assert Fraction(1,2)<al<au<Fraction(2,3)
    tl,tu=B*al-46,B*au-46
    assert Fraction(1,4)<tl<tu<Fraction(1,3)
    p=(tl*Q).__floor__()
    assert p==(tu*Q).__floor__()
    assert Fraction(p,Q)<tl<tu<Fraction(p+1,Q)
    return tl,tu,p


def cf_interval(lo,hi,count):
    partial=[]
    for _ in range(count):
        a=lo.numerator//lo.denominator
        assert a==hi.numerator//hi.denominator
        partial.append(a)
        lo,hi=1/(hi-a),1/(lo-a)
    return partial


def convergents(partial):
    pm2,pm1=0,1
    qm2,qm1=1,0
    out=[]
    for a in partial:
        p=a*pm1+pm2
        q=a*qm1+qm2
        out.append((p,q))
        pm2,pm1=pm1,p
        qm2,qm1=qm1,q
    return out


def norm_interval(d,p):
    assert d>=1
    low_d=d*p
    high_d=d*(p+1)
    f=low_d//Q
    assert f==high_d//Q, (d,'floor uncertified')
    lo=low_d-f*Q
    hi=high_d-f*Q
    assert 0<lo<=hi<Q
    if 2*hi<Q:
        return lo,hi
    if 2*lo>Q:
        return Q-hi,Q-lo
    raise AssertionError((d,'midpoint uncertified'))


def risk_bracket(q,theta_lo,theta_hi,pnumerator):
    """Exact 160-term logarithm bounds used for a tight 10^-18 bracket."""
    a,b=q*theta_lo,q*theta_hi
    n=a.numerator//a.denominator
    assert n==b.numerator//b.denominator
    a,b=a-n,b-n
    assert 0<a<b<1
    if 2*b<1:
        dl,du=a,b
    elif 2*a>1:
        dl,du=1-b,1-a
    else:
        raise AssertionError((q,'nearest-integer undecided'))
    v=(dl*SCALE).__floor__()
    assert v==(du*SCALE).__floor__()
    return v


def partition_risk_interval(m,p):
    """Independently reconstruct old partition neighbors via integer brackets."""
    def neg_phase(j):
        n=j*p//Q
        assert n==j*(p+1)//Q
        return ((n+1)*Q-j*(p+1),(n+1)*Q-j*p)
    old=[(0,0),(Q,Q)]+[neg_phase(j) for j in range(1,m)]
    old.sort(key=lambda t:t[0]+t[1])
    assert all(old[k][1]<old[k+1][0] for k in range(len(old)-1))
    zlo,zhi=neg_phase(m)
    idx=[k for k in range(len(old)-1) if old[k][1]<zlo and zhi<old[k+1][0]]
    assert len(idx)==1
    k=idx[0]
    left=(zlo-old[k][1],zhi-old[k][0])
    right=(old[k+1][0]-zhi,old[k+1][1]-zlo)
    if left[1]<right[0]:
        return left
    assert right[1]<left[0]
    return right


def main():
    tl,tu,p=certified_theta()
    partial=cf_interval(tl,tu,16)
    conver=convergents(partial)
    assert partial[:7]==[0,3,1,4,2,1,2]
    print('PASS_THETA_RATIONAL_INTERVAL theta_between',f'{p}/{Q}',f'{p+1}/{Q}',flush=True)
    print('PASS_CERTIFIED_CONTINUED_FRACTION',partial,flush=True)
    record_q=[]
    for i,(num,den) in enumerate(conver):
        v=risk_bracket(den,tl,tu,p)
        if den<=MAX_SCAN:
            record_q.append(den)
        print('PASS_CONVERGENT',f'j={i}',f'partial={partial[i]}',f'p={num}',f'q={den}',f'error_in=({v}/{SCALE},{v+1}/{SCALE})',flush=True)
    best=None
    detected=[]
    for d in range(1,MAX_SCAN+1):
        lb,ub=norm_interval(d,p)
        if best is None or ub<best[0]:
            best=(lb,ub)
            detected.append(d)
        else:
            assert lb>best[1],(d,'record-order uncertified')
    assert detected==record_q,(detected,record_q)
    print('PASS_ALL_INTEGERS_CERTIFIED',f'1..{MAX_SCAN}',f'records={detected}',flush=True)
    for m in [1,2,3,4,8,16,32,64,128,1000,10000,200000]:
        q=max(x for x in record_q if x<=m)
        error=risk_bracket(q,tl,tu,p)
        print('PASS_FINITE_MEMORY_RISK',f'm={m}',f'record_q={q}',f'error_in=({error}/{SCALE},{error+1}/{SCALE})',flush=True)
    for m in [1,2,3,4,8,16,32,64,128]:
        pl,pu=partition_risk_interval(m,p)
        q=max(x for x in record_q if x<=m)
        dl,du=norm_interval(q,p)
        assert max(pl,dl)<min(pu,du), (m,q,'independent methods disagree')
        assert (pl*SCALE//Q)==(pu*SCALE//Q)==risk_bracket(q,tl,tu,p)
        print('PASS_INDEPENDENT_PARTITION_CHECK',f'm={m}',f'best_return_q={q}',flush=True)
    print('PASS_S23_AV_DIOPHANTINE_FINITE_MEMORY_RISK',flush=True)


if __name__=='__main__':
    main()
