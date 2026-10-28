#!/usr/bin/env python3
"""Exact rational construction/checks for joint (TV_Q, TV_P) moment slice.

No floating point arithmetic, no external modules required.
Mathematical all-real proof is in RESEARCH.md; these are independent finite regression checks.
"""
from fractions import Fraction as F


def fsum(items):
    return sum(items, F(0))


def endpoint(s, m):
    assert s[0] <= m <= s[-1]
    den = s[-1] - s[0]
    ans = [F(0) for _ in s]
    ans[0] = (s[-1] - m)/den
    ans[-1] = (m - s[0])/den
    return ans


def positive_baseline(s, m):
    """Strict positive Q law of specified mean via uniform+extreme mixing."""
    assert s[0] < m < s[-1]
    mu_u = fsum(s)/len(s)
    eps = F(1, 2)
    while True:
        mu_0 = (m - eps * mu_u)/(1 - eps)
        if s[0] < mu_0 < s[-1]:
            break
        eps /= 2
    extreme = endpoint(s, mu_0)
    return [(1-eps)*x + eps/len(s) for x in extreme]


def tv(p, q):
    return fsum(abs(x-y) for x,y in zip(p, q))/2


def audit(s, r, q, qq, strict=False):
    n=len(s)
    assert all(x >= 0 for x in q+qq)
    if strict:
        assert all(x > 0 for x in q+qq)
    assert fsum(q)==fsum(qq)==1
    assert fsum(x*y for x,y in zip(s,q)) == r
    assert fsum(x*y for x,y in zip(s,qq)) == r
    p=[si*qi/r for si,qi in zip(s,q)]
    pp=[si*qi/r for si,qi in zip(s,qq)]
    assert fsum(p)==fsum(pp)==1
    if strict:
        assert all(x > 0 for x in p+pp)
    t, v=tv(q,qq),tv(p,pp)
    assert feasible(s,r,t,v,strict=strict)
    return (t,v)


def feasible(s,r,t,v,strict=False):
    if t<0 or v<0:
        return False
    if len(s)==2:
        return t==v==0
    wedge=(s[1]*t <= r*v <= s[-2]*t)
    if not wedge:
        return False
    if strict:
        return r*v-s[0]*t < r-s[0] and s[-1]*t-r*v < s[-1]-r
    return r*v-s[0]*t <= r-s[0] and s[-1]*t-r*v <= s[-1]-r


def max_t(s,r,m):
    return min(F(1), (r-s[0])/(m-s[0]), (s[-1]-r)/(s[-1]-m))


def construct(s,r,t,v,strict=False):
    """Construct q,qq for any feasible point; n>=3."""
    assert len(s)>=3 and feasible(s,r,t,v,strict=strict)
    if t==0:
        u=positive_baseline(s,r)
        return u,u[:]
    m=r*v/t
    n=len(s)
    a=endpoint(s,m)
    b=[F(0)]*n
    if n==3:
        assert m==s[1]
        b[1]=1
    else:
        den=s[-2]-s[1]
        b[1]=(s[-2]-m)/den
        b[-2]=(m-s[1])/den
    assert fsum(a)==fsum(b)==1
    assert fsum(x*si for x,si in zip(a,s))==m
    assert fsum(x*si for x,si in zip(b,s))==m
    assert all(x*y==0 for x,y in zip(a,b)), 'disjoint supports'
    if t==1:
        assert not strict and m==r
        c=[F(0)]*n
    else:
        mu=(r-t*m)/(1-t)
        common=positive_baseline(s,mu) if strict else endpoint(s,mu)
        c=[(1-t)*z for z in common]
    q=[c[i]+t*a[i] for i in range(n)]
    qq=[c[i]+t*b[i] for i in range(n)]
    assert audit(s,r,q,qq,strict=strict)==(t,v)
    return q,qq


def vertices(s,r):
    if len(s)==2:
        return [(F(0),F(0))]
    ms=[s[1],s[-2]]
    ans=[(F(0),F(0))]
    for m in ms:
        t=max_t(s,r,m)
        ans.append((t,t*m/r))
    if s[1]<=r<=s[-2]:
        ans.append((F(1),F(1)))
    return list(dict.fromkeys(ans))


def compositions(n,total):
    if n==1:
        yield (total,)
    else:
        for k in range(total+1):
            for rest in compositions(n-1,total-k):
                yield (k,)+rest


def check(s,r):
    n=len(s)
    print('CASE n=%d s=%s r=%s' % (n,','.join(map(str,s)),r))
    vs=vertices(s,r)
    print('  EXACT_POLYGON_VERTICES '+str(vs))
    for t,v in vs:
        assert feasible(s,r,t,v)
        q,qq=construct(s,r,t,v)
        audit(s,r,q,qq)
        if t>0:
            # Interior radial approximant keeps the same middle moment but
            # turns all common-overlap inequalities strict.
            tt=t*F(99,100)
            vv=v*F(99,100)
            assert feasible(s,r,tt,vv,strict=True)
            qp,qqp=construct(s,r,tt,vv,strict=True)
            assert audit(s,r,qp,qqp,strict=True)==(tt,vv)
    for i in range(21):
        m=s[1]+F(i,20)*(s[-2]-s[1]); ttop=max_t(s,r,m)
        for alpha in (F(1,17),F(1,2),F(99,100)):
            t=ttop*alpha
            v=t*m/r
            q,qq=construct(s,r,t,v,strict=True)
            assert audit(s,r,q,qq,strict=True)==(t,v)
    print('  EXACT_STRICT_POSITIVE_CONSTRUCTIONS %d' % (21*3))
    # Independent finite rational grid verification: not used for the theorem.
    den=12 if n<=4 else 8
    grid=[]
    for nums in compositions(n,den):
        q=[F(v,den) for v in nums]
        if fsum(si*qi for si,qi in zip(s,q))==r:
            grid.append(q)
    tests=0
    for i,q in enumerate(grid):
        for qq in grid[i:]:
            t,v=audit(s,r,q,qq)
            assert feasible(s,r,t,v)
            tests+=1
    print('  EXACT_RATIONAL_GRID q_count=%d pair_count=%d denominator=%d' %(len(grid),tests,den))
    return tests


def main():
    cases=[
        ([F(1,2),F(1),F(2)],F(1)),
        ([F(1,2),F(1),F(2),F(3)],F(3,4)),
        ([F(1,2),F(1),F(2),F(3)],F(3,2)),
        ([F(1,2),F(1),F(2),F(3)],F(5,2)),
        ([F(1,3),F(1,2),F(1),F(2),F(5,2)],F(1)),
        ([F(1,3),F(1,2),F(1),F(2),F(5,2),F(4)],F(3,2)),
    ]
    checked=sum(check(s,r) for s,r in cases)
    s=[F(1,2),F(1),F(2),F(3)]; r=F(3,2)
    assert vertices(s,r)==[(F(0),F(0)),(F(3,4),F(1,2)),(F(2,3),F(8,9)),(F(1),F(1))]
    # A naive intersection of independent sharp maxima and the ratio wedge
    # admits (TV_Q,TV_P)=(1,2/3), but it violates the exact last facet.
    assert not feasible(s,r,F(1),F(2,3))
    assert s[-1]*1-r*F(2,3)==F(2)>s[-1]-r==F(3,2)
    q=[F(12,25),F(1,10),F(1,10),F(8,25)]
    qq=[F(3,25),F(2,5),F(2,5),F(2,25)]
    assert audit(s,r,q,qq,strict=True)==(F(3,5),F(3,5))
    assert audit(s,r,*construct(s,r,F(3,5),F(3,5),strict=True),strict=True)==(F(3,5),F(3,5))
    print('COUNTEREXAMPLE naive_wedge_plus_caps contains (1,2/3); EXACT_FACET_EXCLUDES')
    print('STRICT_POSITIVE_WITNESS (t,v)=(3/5,3/5) q='+str(q)+' qprime='+str(qq))
    print('FINITE_GRID_PAIR_CHECKS', checked)
    print('ALL EXACT JOINT-TV-POLYGON CHECKS PASSED')


if __name__=='__main__':
    main()
