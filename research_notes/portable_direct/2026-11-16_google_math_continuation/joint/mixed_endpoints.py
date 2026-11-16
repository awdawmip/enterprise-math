"""Check for isolated additional active corners at ALL critical abscissas."""
from itertools import combinations
import sympy as s
from mixed_envelope import fun, g, roots, P0, cut, unique_intervals, winner, v, u

def make_poly(f):
    return s.Poly(f,v,domain=s.QQ)

def factor_for(f,l,r):
    factors=make_poly(f).factor_list()[1]
    return next(p for p,m in factors if p.count_roots(l,r))

def sign_at(f,I,root):
    p=make_poly(f)
    if p.is_zero:return 0
    l,r=I
    if l==r:return s.sign(p.eval(l))
    if p.rem(root).is_zero:return 0
    while p.count_roots(l,r):
        l,r=root.refine_root(l,r,steps=4)
    return s.sign(p.eval((l+r)/2))

def test():
    polys={s.cancel(f).as_numer_denom()[0] for f in [P0.subs(v,-v),*fun.values()]}
    for f in fun.values():
        polys.add(f.as_numer_denom()[1])
        polys.add(s.diff(f,v).cancel().as_numer_denom()[0])
    for f,w in combinations(fun.values(),2):
        polys.add(s.cancel(f-w).as_numer_denom()[0])
    by={}
    for f in polys-{0}:
        for interval in roots(f):by[interval]=f
    cuts=unique_intervals([(0,0),*by.keys(),(cut,cut)])
    stop=roots(P0.subs(v,-v))[0]
    for j,I in enumerate(cuts):
        if I[0]>stop[1]:break
        if j==0:
            # sign(v) corresponds to the same point when V=0.
            assert set(winner(0)[1])=={(0,-1,-1),(0,-1,1)}
            continue
        rightcl=I[0]>=stop[0] and I[1]<=stop[1]
        prevs=winner((cuts[j-1][1]+I[0])/2)[1]
        nexts=() if rightcl else winner((I[1]+cuts[j+1][0])/2)[1]
        expected=set(prevs)|set(nexts)
        p=next(f for (l,r),f in by.items() if max(l,I[0])<=min(r,I[1]))
        root=factor_for(p,*I) if I[0]!=I[1] else None
        base=fun[prevs[0]]
        # Take the safe-side active radius and test each signed margin there.
        # A vanishing u coefficient with vanishing offset also appears here.
        actual=set()
        for key in fun:
            m,su,sv=key
            M=s.cancel(g[m].subs({u:su*base,v:sv*v},simultaneous=True))
            n,d=M.as_numer_denom()
            sig=sign_at(n,I,root)*sign_at(d,I,root)
            assert sig>=0,(I,key,'invalid branch')
            if sig==0:actual.add(key)
        if rightcl:
            expected|={(m,-su,sv) for m,su,sv in expected}
        assert actual==expected,(I,actual,expected)
        if len(actual)>1:print(float(sum(I)/2),sorted(actual))
    D=6*v**5+176*v**4+776*v**3+256*v**2+51*v-15
    r=roots(D)[0]
    assert s.Rational(14373,100000)<r[0]<r[1]<s.Rational(14375,100000)
    assert s.cancel(fun[3,1,-1]-v).as_numer_denom()[0]==-D
    x,keys=winner(s.Rational(1,10))
    assert x==s.Rational(1125301,3086500) and keys==((1,-1,-1),)
    print('diagonal isolator',r,'V=1/10',x)
    print('endpoint masks confirmed')
if __name__=='__main__':test()
