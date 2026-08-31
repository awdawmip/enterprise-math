#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,math
from pathlib import Path
STATES=((0,0,0,0),(0,0,1,0),(0,1,1,0),(1,0,0,1),(0,0,0,1));NAMES=('Z','C','B3','A4','D12')
EXPECTED={1:(4,2,2,4),5:(2,0,2,0),7:(4,2,0,0),11:(2,0,0,0)}
def vals(x):return (x*x+1,x*x+x+1,x**6-1,x**6+1)
def sig(x,p):return tuple(int(v%p==0) for v in vals(x))
def prime(n):
    if n<2:return False
    d=2
    while d*d<=n:
        if n%d==0:return False
        d=3 if d==2 else d+2
    return True
def counts(p):
    out={name:0 for name in NAMES}
    for x in range(p):
        s=sig(x,p);assert s in STATES,(p,x,s);out[NAMES[STATES.index(s)]]+=1
    return out
def expected(p):
    if p==3:return {'Z':1,'C':1,'B3':1,'A4':0,'D12':0}
    c=p%12;v=EXPECTED[c];r=sum(v);return {'Z':p-r,'C':v[0],'B3':v[1],'A4':v[2],'D12':v[3]}
def verify(path):
    r=json.loads(Path(path).read_text());assert r['schema']=='PCF3_HIDDEN_FACTOR_SEPARATION_SPECTRUM_V1'
    ps=[p for p in range(3,200) if p%2 and prime(p)]
    for p in ps:assert counts(p)==expected(p),(p,counts(p),expected(p))
    pair=0
    for i,p in enumerate(ps[:16]):
        for q in ps[i+1:16]:
            cp,cq=counts(p),counts(q);coll=sum(cp[k]*cq[k] for k in NAMES);direct=sum(1 for xp in range(p) for xq in range(q) if sig(xp,p)==sig(xq,q));assert coll==direct;pair+=1
    ce=r['fixed_prefix_64_counterexample'];N=int(ce['N']);p=int(ce['p']);q=int(ce['q']);assert p*q==N and prime(p) and prime(q)
    for x in range(64):
        for v in vals(x):assert math.gcd(N,v) in (1,N)
    b=r['benchmark_replay'];assert (b['cases'],b['successes'],b['semiprime_cases'],b['semiprime_successes'])==(89,84,48,43)
    fam=b['by_family'];assert fam['balanced_semiprime']=={'cases':23,'successes':21};assert fam['unbalanced_semiprime']=={'cases':18,'successes':18};assert fam['near_twin_semiprime']=={'cases':7,'successes':4}
    print(f"PCF3_INDEPENDENT_CHECK_PASS primes={len(ps)} pairs={pair} fixed64={N} aggregate=84/89")
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--verify-report',required=True);a=ap.parse_args();verify(a.verify_report)
if __name__=='__main__':main()
