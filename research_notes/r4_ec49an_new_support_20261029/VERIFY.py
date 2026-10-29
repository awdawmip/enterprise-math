"""EC49AN author-side exact rational certificate (Python stdlib only).
Full real-strategy theorem follows separately from the analytic vertex/convexity proof.
"""
from fractions import Fraction as F
from itertools import product, combinations
import json

K=F(177,172); A=F(27,172); C=(1,1,2,2,0)
E0=F(41,1106); E1=F(1,20); LOW=F(25,32); HIGH=F(43,48)
Z=F(0); O=F(1)

def vertices():
    out=set()
    for m in range(3):
        others=[w for w in range(3) if w!=m]
        for i,j in product(range(5), repeat=2):
            needed=F(43,16)-C[i]-C[j]
            for a,b in combinations(range(5),2):
                if not min(C[a],C[b]) < needed < max(C[a],C[b]):
                    continue
                p=(needed-C[b])/F(C[a]-C[b]); x=[[Z]*5 for _ in range(3)]
                x[others[0]][i]=x[others[1]][j]=O
                x[m][a]=p; x[m][b]=O-p
                key=tuple(tuple(row) for row in x)
                assert all(sum(row)==O for row in key)
                assert sum(C[c]*key[w][c] for w,c in product(range(3),range(5))) == F(43,16)
                out.add(key)
    assert len(out)==168
    return sorted(out)

def leaf(w,u,z,eta):
    t=F(1,2)+(2*u-1)*(1-w)*eta
    P=t*(F(1,6) if z==w else F(1,12))
    Q=t/F(9)
    return P,Q

def fibers(x,eta):
    for c,u in product(range(4),range(2)):
        q=[x[w][c]*(F(1,2)+(2*u-1)*(1-w)*eta)/3 for w in range(3)]
        T=sum(q); V=sum(max(Z,43*qw-16*T) for qw in q)
        yield T,V

def full(x,eta):
    f=list(fibers(x,eta))
    return sum((t for t,v in f),Z),sum((v/F(172) for t,v in f),Z)

def lam(eta): return F(553,946)*eta-F(152,473)
def bound(eta): return F(22625,60544)-F(13825,30272)*eta

def D(x,eta):
    la=lam(eta)
    assert la<0
    return sum((v/F(172)-la*t for t,v in fibers(x,eta)),Z)

def mix(x,y):
    return tuple(tuple((a+b)/2 for a,b in zip(row1,row2)) for row1,row2 in zip(x,y))

def actual(x,eta,accept):
    alpha=beta=Z
    for w,u,z,c in product(range(3),range(2),range(3),range(5)):
        p,q=leaf(w,u,z,eta)
        if c<4 and accept(c,u,z):
            alpha+=p*x[w][c]
            beta+=q*x[w][c]
    return alpha,beta,alpha-K*beta

sat=((O,Z,Z,Z,Z),(Z,O,Z,Z,Z),(Z,Z,F(11,32),Z,F(21,32)))
swap=((Z,F(11,16),Z,Z,F(5,16)),(O,Z,Z,Z,Z),(Z,O,Z,Z,Z))

def acc_sat(c,u,z): return (c==0 and z==0) or (c==1 and z==1) or (c==2 and z==2)
def acc_swap(c,u,z): return (c==0 and z==1) or (c==1 and ((u==0 and z==2) or (u==1 and z in (0,2))))

vs=vertices(); results={}
for eta in (E0,E1):
    ps=[];qs=[]
    for w,u,z in product(range(3),range(2),range(3)):
        p,q=leaf(w,u,z,eta);assert p>0 and q>0
        ps.append(p);qs.append(q)
    assert len(ps)==len(qs)==18 and sum(ps)==sum(qs)==O
    vals=[D(x,eta) for x in vs]
    assert max(vals)==bound(eta) and all(v<=bound(eta) for v in vals)
    n=sum(v==bound(eta) for v in vals)
    assert n==(24 if eta==E0 else 16)
    for x,acc,c2,h in ((sat,acc_sat,LOW,A*LOW),(swap,acc_swap,HIGH,F(1417,16512)+F(553,8256)*eta)):
        assert full(x,eta)==(c2,h)
        alpha,beta,H=actual(x,eta,acc)
        assert H==h and h-lam(eta)*c2==bound(eta)
    results[str(eta)]={"lambda":str(lam(eta)),"B":str(bound(eta)),"max_D":str(max(vals)),"tight_vertices":n,"strict_vertices":168-n,
                       "smallest_strict_margin":str(min((bound(eta)-d for d in vals if d<bound(eta))))}

# All exact-support vertices at the critical endpoint: 12 low, 12 high.
def tight_classes(eta):
    lo=[];hi=[]
    for i,x in enumerate(vs):
        if D(x,eta)==bound(eta):
            c2,_=full(x,eta)
            assert c2 in (LOW,HIGH)
            (lo if c2==LOW else hi).append((i,x))
    return lo,hi
lo0,hi0=tight_classes(E0); lo1,hi1=tight_classes(E1)
assert (len(lo0),len(hi0),len(lo1),len(hi1))==(12,12,12,4)
assert [i for i,x in lo0]==[i for i,x in lo1]
assert set(i for i,x in hi1).issubset(set(i for i,x in hi0))
pair_results={}
for eta,lows,highs in ((E0,lo0,hi0),(E1,lo1,hi1)):
    gaps=[bound(eta)-D(mix(x,y),eta) for i,x in lows for j,y in highs]
    assert all(g>0 for g in gaps)
    pair_results[str(eta)]={"pairs":len(gaps),"minimum_midpoint_gap":str(min(gaps))}

# Independent exact spot check of endpoint formulae inside the certified interval.
for eta in (F(1,26),F(1,25),F(1,22)):
    assert E0<eta<E1
    assert D(sat,eta)==D(swap,eta)==bound(eta)
    assert full(swap,eta)[1]==F(1417,16512)+F(553,8256)*eta
assert lam(E0)==F(-567,1892) and lam(E1)==F(-5527,18920)
assert bound(E0)==F(675,1892) and bound(E1)==F(42485,121088)

print(json.dumps({"schema":"EC49AN_EXACT_FRACTION_V1","status":"PASS_EXACT_AUTHOR_UNREVIEWED",
    "source_model":"18+18 positive-probability BRC leaf observer, C1=43/48",
    "eta_interval":[str(E0),str(E1)],"lambda_formula":"(553/946)*eta-152/473",
    "intercept_formula":"22625/60544-(13825/30272)*eta",
    "certification":"168 distinct first-stage vertices at two eta endpoints; convexity in x and eta",
    "vertex_checks":336,"fiber_evaluations":2688,
    "endpoints":results,"strict_nonattainment_endpoint_midpoints":pair_results,
    "witness_costs":[str(LOW),str(HIGH)],
    "fixed_cost_interiors":"support strictly unattained for any eta in certified interval and LOW<C2<HIGH",
    "formal_independence":"AUTHOR_SIDE_ONLY; UNREVIEWED; NOT_ADMITTED"},indent=2))
