"""EC49AJ exact rational certificate. python3 VERIFY.py
Auxiliary P/Q positive observer; not native signed or phase BRC.
"""
from fractions import Fraction as F
import json

Z, O = F(0), F(1)
eta, k, lam = F(3,10), F(177,172), F(49,860)
C1, C20 = F(43,48), F(7,8)
knots = [Z, F(3,128), F(179,2592), F(3,32)]

def t(w,u):
    return F(1,2)+(2*u-1)*(1-w)*eta
def P(w,u,z):
    return t(w,u)*(F(1,6) if w==z else F(1,12))
def Q(w,u,z):
    return t(w,u)/9
def mass(x,c,u):
    return sum(x[w][c]*t(w,u) for w in range(3))/3
def d(x,c,u,z):
    return sum(x[w][c]*(P(w,u,z)-k*Q(w,u,z)) for w in range(3))
def phi(x,c,u):
    return sum(max(Z,d(x,c,u,z)) for z in range(3))
def H(x):
    return sum(phi(x,c,u) for c in range(4) for u in range(2))
def dual(x,e):
    return lam*(C20-e)+sum(max(Z,phi(x,c,u)-lam*mass(x,c,u))
                             for c in range(4) for u in range(2))
def Y(e):
    return [[F(9,16)-6*e,Z,F(1,16)+3*e,Z],[Z,O,Z,Z],[O,Z,Z,Z]]
def vertices(e):
    B=F(1,16)+3*e
    for b in (Z,B):
        for i in range(3):
            for j in range(3):
                for labels in range(8):
                    for blabel in range(2):
                        x=[[Z,Z,Z,Z] for _ in range(3)]
                        for w in range(3):
                            s=F(5,16)+b if w==i else Z
                            bb=b if w==j else Z
                            x[w][(labels>>w)&1]=O-s-bb
                            x[w][2+blabel]+=bb
                        yield x
def costs(x,e,all_buy=False):
    assert all(min(row)>=Z and sum(row)<=O for row in x)
    c1=sum(row[0]+row[1]+2*(row[2]+row[3]) for row in x)/3
    q=sum(mass(x,c,u) for c in range(4) for u in range(2))
    assert c1==C1 and q>=C20-e
    if all_buy: assert q==C20-e
def mask(e):
    return frozenset((c,u,z) for c in range(4) for u in range(2)
                     for z in range(3) if d(Y(e),c,u,z)>0)
def ab(x,accepted):
    a=sum(x[w][c]*P(w,u,z) for c,u,z in accepted for w in range(3))
    b=sum(x[w][c]*Q(w,u,z) for c,u,z in accepted for w in range(3))
    return a,b
def coeff(f,a,b):
    m=(f(b)-f(a))/(b-a)
    return f(a)-m*a,m

def run():
    ps=qs=Z
    for w in range(3):
        for u in range(2):
            assert sum(P(w,u,z) for z in range(3))==t(w,u)/3
            assert sum(Q(w,u,z) for z in range(3))==t(w,u)/3
            for z in range(3):
                p,q=P(w,u,z),Q(w,u,z)
                assert p>0 and q>0
                ps+=p; qs+=q
    assert ps==qs==O
    roots=set()
    for c in range(4):
        for u in range(2):
            for z in range(3):
                a=d(Y(Z),c,u,z)
                slope=d(Y(O),c,u,z)-a
                if slope:
                    r=-a/slope
                    if Z<r<knots[-1]: roots.add(r)
    assert sorted(roots)==knots[1:-1]
    endpoints=[]
    for e in knots:
        y=Y(e); costs(y,e,True)
        target=H(y)
        vv=list(vertices(e))
        assert len(vv)==288
        distinct=len({tuple(j for row in x for j in row) for x in vv})
        assert distinct==(144 if e==knots[-1] else 168)
        vals=[]
        for x in vv:
            costs(x,e)
            v=dual(x,e)
            assert v<=target,(e,x,v,target)
            vals.append(v)
        assert max(vals)==target
        endpoints.append(dict(epsilon=str(e),C2=str(C20-e),
          support=str(target),dual_min=str(min(vals)),
          dual_max=str(max(vals)),indexed=len(vv),distinct=distinct,
          equalities=sum(v==target for v in vals)))
    pieces=[]
    for a,b in zip(knots[:-1],knots[1:]):
        m=mask((a+b)/2)
        for c in range(4):
            for u in range(2):
                for z in range(3):
                    j=(c,u,z)
                    if j in m:
                        assert d(Y(a),*j)>=0 and d(Y(b),*j)>=0
                    else:
                        assert d(Y(a),*j)<=0 and d(Y(b),*j)<=0
        h0,h1=coeff(lambda e:H(Y(e)),a,b)
        aa0,aa1=coeff(lambda e:ab(Y(e),m)[0],a,b)
        bb0,bb1=coeff(lambda e:ab(Y(e),m)[1],a,b)
        assert h0==aa0-k*bb0 and h1==aa1-k*bb1
        assert H(Y((a+b)/2))==h0+h1*(a+b)/2
        pieces.append(dict(epsilon_start=str(a),epsilon_end=str(b),
           support_intercept=str(h0),support_slope=str(h1),
           alpha_intercept=str(aa0),alpha_slope=str(aa1),
           beta_intercept=str(bb0),beta_slope=str(bb1),
           acceptance_atoms=list(map(list,sorted(m)))))
    assert [(F(p["support_intercept"]),F(p["support_slope"])) for p in pieces]==[
      (F(919,8256),-F(49,860)),
      (F(4451,41280),F(79,860)),
      (F(249,2752),F(59,172))]
    assert Y(knots[-1])[0][0]==Z
    assert F(5,16)+2*(F(1,16)+3*knots[-1])==O
    return dict(schema="EC49AJ_SHARP_COST_KINKS_V1",
       scope="all real causal fresh coin policies; eta=3/10;k=177/172;C1=43/48;0<=epsilon<=3/32",
       source_P=str(ps),source_Q=str(qs),lambda_dual=str(lam),
       sign_roots=[str(x) for x in sorted(roots)],
       endpoint_certificates=endpoints,pieces=pieces,
       indexed_endpoint_checks=288*len(knots),
       distinct_endpoint_checks=sum(v["distinct"] for v in endpoints),
       result="PASS_EXACT_FRACTION_AUTHOR_UNREVIEWED",
       native_BRC_transfer="NOT_CLAIMED",formal_proof="NOT_PERFORMED")
if __name__=="__main__":
    print(json.dumps(run(),ensure_ascii=False,indent=2))
