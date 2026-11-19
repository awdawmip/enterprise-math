"""Integral harmonic measurements on the frozen W59A three-token history."""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, combinations_with_replacement, product
from math import gcd, lcm, prod
from pathlib import Path
import argparse
import contextlib
import io
import json
import runpy
import sys

PINS={
    "path":("experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py","6f0d79a519c53fed1300b3fabf500c34e30aa46cdd63b409fa6ecc115071ecb4"),
    "frame":("experiments/x6_cell_internal_state_v1_20260906/check_triadic_port_frame.py","34058e33af5d8e325e3804bdbcf92f06918d48817b3ba5f8ded02e34c337a964"),
    "brc":("src/enterprise_math/brc_weighted.py","4f3e356227a1c964d33a3ddae94922463ba28097a43b8d1b8f6cd9ca5615fc9f")}


def observer(repo,weights):
    for path,h in PINS.values():
        assert sha256((repo/path).read_bytes()).hexdigest()==h
    with contextlib.redirect_stdout(io.StringIO()):
        spatial=runpy.run_path(str(repo/PINS["path"][0]))
        frames=runpy.run_path(str(repo/PINS["frame"][0]))
    sys.path.insert(0,str(repo/'src'))
    from enterprise_math import brc_weighted as brc
    assert Path(brc.__file__).resolve()==repo/PINS["brc"][0]
    dim=len(weights)-1
    pos=[[brc.CWM_ZERO for _ in range(dim)] for _ in range(dim)]
    neg=[[brc.CWM_ZERO for _ in range(dim)] for _ in range(dim)]
    def unit(port):
        return tuple(((1 if port>0 else -1) if i==abs(port) else 0) for i in range(1,7))
    state=((1,-2,3),0)
    original=state
    events=[]
    zero=(0,)*6
    for layer,weight in enumerate(weights):
        f,mode=state
        target=frames['R'](f)
        next_state=frames['F'](state)
        assert next_state==((f,1) if mode==0 else (target,0))
        for token,(a,b) in enumerate(zip(f,target)):
            u,v=unit(a),unit(b)
            delta=tuple(y-x for x,y in zip(u,v))
            assert spatial['shortest_event_count'](delta)==2 and spatial['shortest_path_multiplicity'](delta)==2
            source,end=(u,zero) if not mode else (zero,v)
            assert spatial['shortest_event_count'](tuple(y-x for x,y in zip(source,end)))==1
            edge=brc.cwm_edge(Fraction(weight,3))
            for j,sgn in ((layer,-1),(layer+1,1)):
                for k,sgn2 in ((layer,-1),(layer+1,1)):
                    if 0<j<=dim and 0<k<=dim:
                        ledger=pos if sgn==sgn2 else neg
                        ledger[j-1][k-1]=brc.cwm_recoalesce(ledger[j-1][k-1],edge)
            events.append((layer,token,mode,a,b,source,end))
        state=next_state
    L=[[pos[i][j].total-neg[i][j].total for j in range(dim)] for i in range(dim)]
    assert all(x.denominator==1 for row in L for x in row)
    return [[int(x) for x in row] for row in L],events,state==original


def lap(weights):
    n=len(weights)-1
    return [[weights[i]+weights[i+1] if i==j else -weights[max(i,j)] if abs(i-j)==1 else 0
             for j in range(n)] for i in range(n)]


def smith(weights):
    previous=1; entries=[]
    for k in range(1,len(weights)-1):
        delta=gcd(*(prod(t) for t in combinations(weights,k)))
        entries.append(delta//previous);previous=delta
    entries.append(sum(prod(weights)//v for v in weights)//previous)
    assert all(v%u==0 for u,v in zip(entries,entries[1:]))
    return entries


def det(a):
    if len(a)==0:return 1
    if len(a)==1:return a[0][0]
    pivot=a[0][0]
    if not pivot:
        i=next((j for j in range(1,len(a)) if a[j][0]),None)
        if i is None:return 0
        b=[r[:] for r in a];b[0],b[i]=b[i],b[0]
        return -det(b)
    b=[[a[i][j]*pivot-a[i][0]*a[0][j] for j in range(1,len(a))] for i in range(1,len(a))]
    return det(b)//pivot**max(0,len(a)-2)


def all_minors(weights):
    a=lap(weights);n=len(a);delta=1;entries=[]
    for k in range(1,n+1):
        d=0
        for r in combinations(range(n),k):
            for c in combinations(range(n),k):
                d=gcd(d,det([[a[i][j] for j in c] for i in r]))
        entries.append(d//delta);delta=d
    return entries


def current_formula(w,m):
    es=[gcd(a,m) for a in w]
    l=lcm(*es);v=m//l
    c=sum((l//e)*pow(a//e,-1,v) for a,e in zip(w,es))%v
    g=gcd(c,v)
    fiber=prod(es)//l
    return {i*(m//g):fiber for i in range(g)}


def image_size(w,m):
    largest=lcm(*w)
    penultimate=lcm(*(gcd(x,y) for x,y in combinations(w,2)))
    response=sum(largest//wi for wi in w)
    return gcd(m,penultimate*response)//gcd(m,penultimate)


def flow_dp(w,m):
    rows={}
    # Sum of all increments must be zero. Only this congruence identifies
    # both zero boundary values after the first initial value is pinned.
    for j in range(m):
        dp={0:1}
        for weight in w:
            choices=[e for e in range(m) if weight*e%m==j]
            following=Counter()
            for x,multiplicity in dp.items():
                for e in choices:
                    following[(x+e)%m] += multiplicity
            dp=following
        if dp.get(0,0):rows[j]=dp[0]
    return rows


def site_enumeration(w,m):
    L=lap(w);out=Counter()
    for f in product(range(m),repeat=len(L)):
        if all(sum(u*x for u,x in zip(row,f))%m==0 for row in L):
            out[w[0]*f[0]%m]+=1
    return dict(out)


def specific(a,b,n):
    if n==1:return [a+b]
    d=gcd(a,b);A=a//d;B=b//d
    return [d]*n+[d*A*B]*(n-2)+[n*d*A*B*(A+B)]


def run(repo):
    st=Counter(); cases=[]
    for M in range(2,7):
        for w in combinations_with_replacement(range(1,5),M):
            assert all_minors(w)==smith(w); st["exact_all_minor_matrices"]+=1
            for m in range(2,10):
                f=current_formula(w,m); dp=flow_dp(w,m)
                assert len(f)==image_size(w,m)
                assert f==dp and sum(f.values())==prod(gcd(m,s) for s in smith(w))
                st["complete_current_histograms"]+=1
    for n in range(1,5):
        for a,b in combinations_with_replacement(range(1,10),2):
            assert smith((a,b)*n)==specific(a,b,n)
            st["integer_alternating_matrices"]+=1
    for a,b,n in ((1,4,1),(2,3,1),(1,5,2),(2,3,2),(1,5,3),(2,3,3),(4,4,6),(3,6,6)):
        w=(a,b)*n
        L,events,loop=observer(repo,w)
        assert L==lap(w)
        s=smith(w);assert s==specific(a,b,n)
        readings={}
        for m in (2,3,4,5,6,8,9,12,16,18,24,27,36,48,60):
            counts=flow_dp(w,m)
            assert counts==current_formula(w,m) and len(counts)==image_size(w,m)
            assert sum(counts.values())==prod(gcd(x,m) for x in s)
            if n<=3 and m<=4:
                assert site_enumeration(w,m)==counts;st["exhaustive_interior_site_checks"]+=1
            readings[m]=[sum(counts.values()),len(counts),counts[0]]
        cases.append(dict(a=a,b=b,n=n,closed_C12=loop,primitive_token_occurrences=len(events),
                     token_history_sha256=sha256(json.dumps(events,separators=(',',':')).encode()).hexdigest(),
                     smith=s,readings_count_image_and_zero_current_fiber=readings))
    for M in range(2,6):
        for w in product(range(1,6),repeat=M):
            for m in range(1,61):
                assert len(current_formula(w,m))==image_size(w,m)
                st["closed_image_counts"]+=1
    for h in range(1,41):
        exps={x*y*(x+y)//gcd(x,y)**2 for x in range(1,h+1) for y in range(1,h+1)}
        assert lcm(*exps)==lcm(*range(1,2*h+1));st["uniform_exponents"]+=1
    return dict(frozen_sha256={k:v[1] for k,v in PINS.items()},cases=cases,checks=dict(st))

if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo",type=Path,required=True)
    print(json.dumps(run(p.parse_args().repo.resolve()),sort_keys=True,indent=2))
