"""Usage: python check_gated.py /path/to/the/pinned/check_nonabelian_multicircuit.py."""
import hashlib
import importlib.util
import itertools
import sys
from collections import Counter
from contextlib import redirect_stdout
from fractions import Fraction as F
from io import StringIO
from pathlib import Path

src = Path(sys.argv[1])
data = src.read_bytes()
assert hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest() == '328c328d76e5766261f590afa710671b0a81f0cb'
spec = importlib.util.spec_from_file_location("v38",src)
v38 = importlib.util.module_from_spec(spec)
with redirect_stdout(StringIO()):
    spec.loader.exec_module(v38)

axes = set(range(6))
supports = list(itertools.combinations(sorted(axes),3))
edges = [(s,t) for s in supports for t in supports if len(set(s)&set(t))==2]
mid = {(s,t):[u for u in supports if len(set(s)&set(u))==len(set(t)&set(u))==2] for s,t in edges}


def direct(s,t):
    result=v38.transport_slots({a:a for a in s},s,t)
    return tuple(result[a] for a in t)


def join(left,right,u):
    result=Counter()
    for l,weight in left.items():
        for r,mass in right.items():
            result[tuple(l[u.index(a)] for a in r)] += weight*mass
    return result


def rel_frame(s,t,frame):
    a,b=sorted(set(s)&set(t))
    c,=set(s)-set(t)
    basis=(a,b,c)
    h=direct(s,t)
    return tuple(basis.index(frame[h.index(axis)]) for axis in basis)


def gate_census():
    tested=0
    for start in itertools.permutations(sorted(axes),3):
        s=tuple(sorted(start))
        for k in (1,2,3):
            for enabled in itertools.combinations(range(3),k):
                after_one=[]
                for p in enabled:
                    for y in axes-set(start):
                        u=tuple(sorted(set(start)-{start[p]}|{y}))
                        slots=v38.transport_slots({a:i for i,a in enumerate(start)},s,u)
                        after_one.append((u,slots))
                for p in enabled:
                    for d in axes-set(start):
                        t=tuple(sorted(set(start)-{start[p]}|{d}))
                        h=v38.transport_slots({a:i for i,a in enumerate(start)},s,t)
                        ends=[]
                        for u,slots in after_one:
                            leave=set(u)-set(t)
                            if len(leave)==1 and slots[next(iter(leave))] in enabled:
                                dest=v38.transport_slots(slots,u,t)
                                ends.append(tuple(dest[a] for a in t))
                        target=tuple(h[a] for a in t)
                        assert len(ends)==k+1 and ends.count(target)==2
                        for signs in itertools.product((-1,1),repeat=3):
                            ell=sum(signs[j]==signs[p] for j in enabled)
                            signed=[tuple(signs[i] for i in frame) for frame in ends]
                            assert signed.count(tuple(signs[i] for i in target))==ell+1
                            tested+=1
    assert tested==34560
    return tested


def recurse_coeff(x,y,p):
    flat=p
    bend=1-p
    return (flat*x*x + bend*(x*x+6*x*y-3*y*y)/8,
            flat*y*y + bend*(3*x*x-6*x*y-y*y)/8)


def predictions(x,y,s):
    return {(0,1,2):(1+s+2*x+2*y)/6,
            (1,2,0):(1+s-x-y)/6, (2,0,1):(1+s-x-y)/6,
            (1,0,2):(1-s-2*x+2*y)/6,
            (2,1,0):(1-s+x-y)/6, (0,2,1):(1-s+x-y)/6}


def weighted_census():
    for p in map(F,['0','1','1/2','1/3','2/3','2/5']):
        table={(s,t):Counter({direct(s,t):1}) for s,t in edges}
        x=y=F(1)
        for n in range(1,6):
            out={}
            x,y=recurse_coeff(x,y,p)
            expected=predictions(x,y,(2*p-1)**(2**n-1))
            denominator=(2*p.denominator)**(2**n-1)
            for s,t in edges:
                counts=Counter()
                for u in mid[s,t]:
                    flat=len(set(s)&set(t)&set(u))==2
                    weight=p.numerator if flat else p.denominator-p.numerator
                    if weight:
                        for f,m in join(table[s,u],table[u,t],u).items():
                            counts[f]+=weight*m
                got={rel_frame(s,t,f):F(v,denominator) for f,v in counts.items()}
                assert all(got.get(f,0)==v for f,v in expected.items())
                out[s,t]=counts
            table=out
            if p==0 and n>=2:
                assert expected[1,0,2]==(1+2*F(1,2)**(2**(n-1)))/3


def conditional_probe(tau):
    s,t=(0,1,2),(0,1,3)
    output={}
    for u in mid[s,t]:
        bins=Counter()
        for a,b in itertools.product(mid[s,u],mid[u,t]):
            left_weight=F(1,4)
            if u==(0,1,4):
                left_weight=(1-tau)/4+tau*int(a==(1,2,4))
            slots={v:v for v in s}
            path=(s,a,u,b,t)
            for left,right in zip(path,path[1:]):
                slots=v38.transport_slots(slots,left,right)
            bins[tuple(slots[v] for v in t)] += left_weight/4
        output[u]=bins
    return output


def probe_checks():
    order=[(0,1,4),(0,1,5),(0,2,3),(1,2,3)]
    for tau in (F(0),F(1,4),F(1,2),F(1),F(2,3)):
        cols=conditional_probe(tau)
        probabilities=[sum(v for w,v in cols[u].items() if w[0]==2) for u in order]
        assert probabilities==[(5+7*tau)/16,F(5,16),F(3,16),F(7,16)]
        total_variation=sum(abs(cols[order[0]][w]-cols[order[1]][w])
                            for w in itertools.permutations(range(3)))/2
        assert total_variation==7*tau/16
        weights=[F(1,10),F(2,10),F(3,10),F(4,10)]
        if tau:
            obs=sum(x*y for x,y in zip(weights,probabilities))
            assert (16*obs-5*sum(weights[:2])-3*weights[2]-7*weights[3])/(7*tau)==weights[0]


print("candidate gate / named target / sign checks:",gate_census())
weighted_census()
probe_checks()
print("180 edges x 5 recursive depths x 6 exact weights: PASS")
print("two-level probes, all child paths and five mark strengths: PASS")
