"""Exact Gaussian rational arithmetic: public finite no-wrap Fourier model."""
from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations_with_replacement, product
import argparse
import json
from pathlib import Path
from random import Random


@dataclass(frozen=True)
class Z:
    re: int | F = 0
    im: int | F = 0

    def __add__(self, other):
        if not isinstance(other,Z): other=Z(other)
        return Z(self.re+other.re,self.im+other.im)
    __radd__=__add__

    def __neg__(self):
        return Z(-self.re,-self.im)

    def __sub__(self,other):
        return self+(-other)

    def __mul__(self, other):
        if not isinstance(other,Z):return Z(self.re*other,self.im*other)
        return Z(self.re*other.re-self.im*other.im,self.re*other.im+self.im*other.re)
    __rmul__=__mul__

    def conj(self):
        return Z(self.re,-self.im)


I=Z(0,1)
UNITS=(Z(1),I,Z(-1),-I)
ZERO3=(Z(),)*3
ZERO4=(Z(),)*4


def dot(v,w):
    return sum(x*y for x,y in zip(v,w))


def add(v,w):
    return tuple(x+y for x,y in zip(v,w))


def minus(v,w):
    return tuple(x-y for x,y in zip(v,w))


def scale(a,v):
    return tuple(a*x for x in v)


def cross(v,w):
    return tuple(v[(j+1)%3]*w[(j+2)%3]-v[(j+2)%3]*w[(j+1)%3] for j in range(3))


def rect(v):
    return sum(abs(z.re)+abs(z.im) for z in v)


def norm2(v):
    return sum(z.re*z.re+z.im*z.im for z in v)


def observe(k,v):
    m=dot(k,k)
    s=dot(k,v)*F(1,m) if m else Z()
    return minus(v,scale(s,k))+(s,)


def field(randomized=False, swap=False):
    rng=Random(7189);u={};tags={}
    for j,(b,t) in enumerate(zip((5,-4,-3,1,1),(1,1,3,3,2)),1):
        p=(4*j,1,0);q=(1-4*j,-1,0)
        a1=tuple(map(Z,(-1,4*j,0) if j<5 else (0,0,1)))
        a2=tuple(map(Z,(0,0,b)))
        if randomized:
            def arbitrary(k):
                x=Z(F(rng.randint(-3,3),2),rng.randint(-3,3))
                z=Z(rng.randint(-2,2),F(rng.randint(-2,2),3))
                return (x*(-k[1]),x*k[0],z)
            a1,a2=arbitrary(p),arbitrary(q)
        for mode,a,tag in ((p,a1,0),(q,a2,t)):
            if swap: mode=(mode[1],mode[0],mode[2]);a=(a[1],a[0],a[2])
            neg=tuple(-x for x in mode)
            assert mode not in u and neg not in u and dot(mode,a)==Z()
            u[mode]=a;u[neg]=tuple(z.conj() for z in a)
            tags[mode]=tag;tags[neg]=-tag%4
    return u,tags


def direct(u,h,tags,only=None):
    """Ordered raw rotational convolution, via curl and cross, independent of swap pairing."""
    phased={p:scale(UNITS[h*tags[p]%4],a) for p,a in u.items()}
    raw=defaultdict(lambda:ZERO3)
    for p,q in product(phased,repeat=2):
        k=add(p,q)
        if max(map(abs,k))<=20 and (only is None or (p,q) in only):
            curl=scale(I,cross(q,phased[q]))
            raw[k]=add(raw[k],cross(phased[p],curl))
    return {k:observe(k,v) for k,v in raw.items()}


def branches(u,tags):
    ledger=[];counts=Counter()
    for p,q in combinations_with_replacement(u,2):
        counts['unordered_candidates']+=1
        k=add(p,q)
        if max(map(abs,k))>20: continue
        counts['retained_unordered']+=1
        a,b=u[p],u[q]
        vec=minus(scale(dot(a,b),q if p==q else k),scale(dot(q,a),b))
        if p!=q: vec=minus(vec,scale(dot(p,b),a))
        c=observe(k,scale(I,vec))
        if rect(c):
            counts['nonzero_branches']+=1
            g=(tags[p]+tags[q])%4
            if g:
                ledger.append((k,g,c))
    counts['nonconstant_nonzero_branches']=len(ledger)
    return ledger,counts


def summary(randomized=False,swap=False):
    u,tags=field(randomized,swap)
    ledger,counts=branches(u,tags)
    bins={}
    for k,g,c in ledger:
        if (k,g) in bins: bins[k,g]=add(bins[k,g],c)
        else: bins[k,g]=c
    counts['touched_bins']=len(bins)
    counts['build_vector_adds']=len(ledger)-len(bins)
    bins={key:v for key,v in bins.items() if rect(v)}
    counts['nonzero_bins']=len(bins)
    base=direct(u,0,tags);energy=defaultdict(F);total=defaultdict(lambda:ZERO4)
    for (k,g),v in bins.items():
        total[k]=add(total[k],v);energy[k]+=norm2(v)
    counts['distinct_active_output_modes']=len(total)
    counts['distinct_ordered_output_modes_including_zeros']=len(base)
    counts['ordered_retained_per_oracle']=sum(max(map(abs,add(p,q)))<=20 for p,q in product(u,repeat=2))
    energy={k:norm2(total[k])+e for k,e in energy.items()}
    mean=defaultdict(F); rows=[];signed=None
    for h in range(4):
        oracle=direct(u,h,tags)
        x={k:minus(oracle[k],v) for k,v in base.items()}
        projected=defaultdict(lambda:ZERO4)
        t1=defaultdict(F);g1=defaultdict(F);nb=ng=0
        for k,g,c in ledger:
            factor=UNITS[(h*g)%4]-Z(1)
            if factor!=Z():
                nb+=1;t1[k]+=rect(scale(factor,c))
        for (k,g),v in bins.items():
            factor=UNITS[h*g%4]-Z(1)
            if factor!=Z():
                ng+=1;contribution=scale(factor,v)
                projected[k]=add(projected[k],contribution);g1[k]+=rect(contribution)
        assert all(projected[k]==v and rect(v)<=g1[k]<=t1[k] for k,v in x.items())
        for k,v in x.items():
            assert x[tuple(-z for z in k)]==tuple(z.conj() for z in v[:3])+(-v[3].conj(),)
            mean[k]+=norm2(v)*F(1,4)
        if h==2:signed=x
        if not randomized and not swap and h==1:
            assert x[(1,0,0)]==(Z(),Z(),Z(-3,1),Z(0,-2))
        k=(1,0,0)
        rows.append(dict(h=h,base_phase_scales=nb,group_phase_scales=ng,
                         joint=[str(sum(t1.values())),str(sum(g1.values())),str(sum(map(rect,x.values())))],
                         k1=[str(t1[k]),str(g1[k]),str(rect(x.get(k,ZERO4)))]))
    assert all(mean[k]==energy.get(k,0) for k in mean)
    return counts,rows,signed,energy


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--json',type=Path)
    args=ap.parse_args()
    counts,rows,signed,e=summary();k=(1,0,0);l=(0,1,0)
    assert rows[2]['k1']==['26','6','2'] and signed[k]==(Z(),Z(),Z(0,2),Z()) and e[k]==8
    _,_,swapped,_=summary(swap=True)
    assert signed.get(l,ZERO4)==ZERO4 and swapped.get(k,ZERO4)==ZERO4 and swapped[l]==signed[k]
    # Quarters 1 and 3 agree on h=0,2. Their distinction returns at an odd h.
    assert all(UNITS[h%4]==UNITS[3*h%4] for h in (0,2))
    assert UNITS[1]!=UNITS[3]
    # A fixed, conjugate-closed omitted mask. Evaluate its defect independently
    # using every ordered term that the masked callback would have discarded.
    u,tags=field()
    mask=set()
    for j in range(1,5):
        p,q=(4*j,1,0),(1-4*j,-1,0)
        for a,b in ((p,q),(q,p)):
            mask.add((a,b));mask.add((tuple(-x for x in a),tuple(-x for x in b)))
    omitted=[]
    for h in range(4):
        raw=direct(u,h,tags,mask)
        assert set(raw)=={k,(-1,0,0)}
        expect=I*(UNITS[h]-2*UNITS[3*h%4])
        assert raw[k]==(Z(),Z(),expect,Z())
        omitted.append(sum(map(rect,raw.values())))
    assert omitted==[2,6,2,6]
    assert sum(x*x for x in omitted)==16*5  # one-output mean square
    random_counts,_,_,_=summary(randomized=True)
    report={"retained_max_abs":20,"signed_inputs":20,"ordered_candidates_per_oracle":400,
            "base_counts":dict(counts),"scenarios":rows,"k1_average_squares":str(e[k]),
            "full_average_squares":str(sum(e.values())),"fixed_omission_l1_over_full_box":[str(x) for x in omitted],"randomized_counts":dict(random_counts)}
    text=json.dumps(report,indent=2,sort_keys=True)+'\n'
    if args.json:args.json.write_text(text)
    print(text,end='')


if __name__=='__main__':main()
