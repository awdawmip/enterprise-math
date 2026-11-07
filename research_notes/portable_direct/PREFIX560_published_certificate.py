"""PREFIX-560 exact observer symmetry certificate; frozen science f42f2906d77f24085c123f3ccfe9667d41caa96d.
Dependency: PREFIX550_shared_gauge_compact_certificate.py (native BRC edge implementation).
"""
from collections import Counter
import PREFIX550_shared_gauge_compact_certificate as x

PAIRS=((1,14),(3,17),(4,18),(6,32),(8,34),(9,23),(10,36),
       (11,25),(12,38),(20,44),(22,46),(24,48),(26,50),
       (28,40),(30,42),(35,47),(37,49))

def swap(w):
    w=list(w);w[4],w[5]=w[5],w[4];return tuple(w)
def merge(w):
    w=list(w);w[4]+=w[5];w[5]=0;return tuple(w)
def step(Q,v):
    out=[]
    for row in Q:
        acc=Counter()
        for (j,w),n in row.items():
            for m,a in v[j].items():acc[tuple(b+c for b,c in zip(m,w))]+=n*a
        out.append(acc)
    return out

def main():
    ids,growth=x.classes(x.ROOTS[0]);assert growth==[1,12,51]
    Q=x.quotient(ids,x.ZERO_ROOT);assert len(Q)==51 and sum(map(len,Q.values()))==165
    p=list(range(51))
    for a,b in PAIRS:p[a],p[b]=p[b],p[a]
    assert all(p[p[i]]==i for i in range(51))
    assert ids[9]==5 and p[5]==5
    assert {ids[i] for i in (7,29,31)}=={4,16,18}
    N=[];u=[Counter() for _ in range(51)]
    for i in range(51):
        assert Counter({(p[j],swap(w)):n for (j,w),n in Q[i].items()})==Q[p[i]]
        no=Counter()
        for (j,w),n in Q[i].items():
            if w[6]:
                assert w[6]==1 and j==5 and w[:6]==(1,0,0,0,0,0)
                u[i][w[:6]]+=n
            else:no[j,w[:6]]+=n
        N.append(no)
    assert {i for i in range(51) if u[i]}=={4,16,18}
    v=u
    monomials={}
    for d in range(18):
        assert all(a==v[5].get(swap(m),0) for m,a in v[5].items())
        if v[5]:monomials[d]=len(v[5])
        if d<17:v=step(N,v)
    assert monomials=={3:5,5:12,7:53,9:150,11:295,13:649,15:1205,17:1994}
    orbits=sorted({tuple(sorted({i,p[i]})) for i in range(51)})
    assert len(orbits)==34
    oid={i:j for j,o in enumerate(orbits) for i in o}
    Q51=[];Q34=[]
    for i in range(51):Q51.append(Counter({(j,merge(w)):n for (j,w),n in Q[i].items()}))
    for o in orbits:
        row=Counter()
        for (j,w),n in Q[o[0]].items():row[oid[j],merge(w)]+=n
        for i in o:
            check=Counter()
            for (j,w),n in Q[i].items():check[oid[j],merge(w)]+=n
            assert check==row
        Q34.append(row)
    a=[Counter({(0,)*7:1}) for _ in range(51)]
    b=[Counter({(0,)*7:1}) for _ in range(34)]
    for d in range(9):
        assert all(a[i]==b[oid[i]] for i in range(51))
        if d<8:a,b=step(Q51,a),step(Q34,b)
    print('ALL_CHECKS_PASS; 165 exact symbolic transitions; 17 swaps; 34 orbits; 459 full polynomial matches')

if __name__=='__main__':main()
