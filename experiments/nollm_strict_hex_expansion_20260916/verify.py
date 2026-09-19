"""Rebuild the first-style straight hexagon expansion. Integer geometry only.
Usage: python verify.py [output] [--full]
--full requires NumPy and visits every selected site through k=12.
No Actions, network, source writes, label deletion or mathematical promotion.
"""
from collections import Counter, defaultdict
from pathlib import Path
import csv, hashlib, json, math, sys


def h(q,r):return max(abs(2*q+r),abs(q+2*r),abs(q-r))
def threshold(k):return 3*((2**k-1)//3)
def row_bounds(t,q):
    return max(-t-2*q,-((t+q)//2),q-t),min(t-2*q,(t-q)//2,q+t)
def rows(t):
    for q in range(-(2*t//3),2*t//3+1):
        lo,hi=row_bounds(t,q)
        if lo<=hi:yield q,lo,hi

def decode(q,r,k):
    n=0
    for i in range(k):
        a,b=q%2,r%2;n+=(a+2*b)*4**i
        u,v=(q-a)//2,(r-b)//2
        q,r=u+v,-u
    return n

def encode(n):
    q=r=0;digits=[]
    while n:digits.append(n%4);n//=4
    for d in reversed(digits):q,r=-2*r+d%2,2*q+2*r+d//2
    return q,r

def excluded(k):
    m=2**k;t=threshold(k);out=defaultdict(list)
    for level in range(t+1,m+1):
        for q,lo,hi in rows(level):
            for r in sorted({lo,hi}):
                if h(q,r)==level:
                    n=decode(q,r,k);a,b=encode(n)
                    assert (a%m,b%m)==(q%m,r%m)
                    out[n].append([q,r])
    assert len(out)==m*m-(t*t+t+1)
    return dict(sorted(out.items()))

def factors(n):
    result=[];p=2
    while p*p<=n:
        e=0
        while n%p==0:n//=p;e+=1
        if e:result.append([p,e])
        p=3 if p==2 else p+2
    if n>1:result.append([n,1])
    return result

def full_check(k,expected):
    import numpy as np
    m=2**k;N=m*m;t=threshold(k);seen=np.zeros(N,dtype=bool)
    qs=[];rs=[];size=0;visited=0
    def flush():
        nonlocal size,visited
        if not qs:return
        q=np.concatenate(qs);r=np.concatenate(rs);u=q.copy();v=r.copy();n=np.zeros_like(q)
        for j in range(k):
            a,b=u%2,v%2;n+=(a+2*b)*4**j
            x,y=(u-a)//2,(v-b)//2;u,v=x+y,-x
        assert len(np.unique(n))==len(n) and not np.any(seen[n])
        x=np.zeros_like(q);y=np.zeros_like(r)
        for j in range(k-1,-1,-1):
            d=(n//4**j)%4;x,y=-2*y+d%2,2*x+2*y+d//2
        assert np.all(x%m==q%m) and np.all(y%m==r%m)
        def heights(a,b):return np.maximum.reduce([abs(2*a+b),abs(a+2*b),abs(a-b)])
        z=heights(q,r)
        assert np.all(z<=t) and np.array_equal(z,heights(-r,q+r))
        assert np.array_equal(z,heights(q+r,-r))
        seen[n]=True;visited+=len(n);qs.clear();rs.clear();size=0
    for q,lo,hi in rows(t):
        qs.append(np.full(hi-lo+1,q,dtype=np.int64));rs.append(np.arange(lo,hi+1,dtype=np.int64));size+=hi-lo+1
        if size>=262144:flush()
    flush()
    assert visited==t*t+t+1
    assert np.flatnonzero(~seen).tolist()==list(expected)
    return {'all_selected_sites':visited,'full_id_bitset':N,'duplicates':0,'inverse_failures':0,'holes':0}

def main(out,full=False):
    out=Path(out);out.mkdir(parents=True,exist_ok=True);result=[];sets={}
    for k in [8,9,10,11,12,14,16]:
        m=2**k;t=threshold(k);ex=excluded(k);sets[k]=set(ex)
        kept=sum(hi-lo+1 for q,lo,hi in rows(t));assert kept==t*t+t+1
        a=t//3;v=[[-2*a,a],[-a,-a],[a,-2*a],[2*a,-a],[a,a],[-a,2*a]]
        a2=abs(sum(q*y-r*x for (q,r),(x,y)in zip(v,v[1:]+v[:1])))
        b=sum(math.gcd(abs(q-x),abs(r-y))for(q,r),(x,y)in zip(v,v[1:]+v[:1]))
        assert (a2+b+2)//2==kept
        fs={n:factors(n) for n in ex} if k<=12 else {}
        for n,f in fs.items():assert math.prod(p**e for p,e in f)==n
        primes=[n for n,f in fs.items() if f==[[n,1]]] if fs else None
        p=out/f'excluded_k{k}.csv'
        with p.open('w',encoding='utf-8',newline='') as f:
            w=csv.writer(f);w.writerow(['n','factors','is_prime','candidate_qr'])
            for n,pts in ex.items():w.writerow([n,json.dumps(fs.get(n)),n in primes if primes is not None else '',json.dumps(pts)])
        entry={'k':k,'population':m*m,'period':m,'threshold':t,'kept':kept,'excluded':len(ex),
               'excluded_primes':len(primes)if primes is not None else None,'sides':6,'fill':'1',
               'vertices':v,'boundary_candidates':sum(map(len,ex.values())),
               'first_excluded':list(ex)[:8],'csv_sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
        if full and k<=12:entry['full_check']=full_check(k,ex)
        else:entry['method']='complete boundary plus integer row count; not all interior IDs enumerated'
        result.append(entry);print(k,kept,len(ex),entry['excluded_primes'],flush=True)
    for k in [8,10,12,14]:
        assert {n//16 for n in sets[k+2] if n%16==0}==sets[k]
        assert not sets[k]&sets[k+2]
        assert all(h(*encode(n))<=threshold(k+2)for n in sets[k])
    assert 128 not in sets[8] and 128*128 in sets[8]
    report={'schema':'NOLLM_STRAIGHT_HEX_VERIFIER_V1','source_encoding':'F(4n+d)=2W F(n)+(d%2,d//2)',
            'source_ref':'19fbd134f2dcb09263c5c65c674211e01d03e078','scales':result,
            'exact_divisible_16_recurrence':True,'old_boundary_labels_readmitted':True,
            'raw_ids_deleted':False,'mathematical_admission':False,'Actions_used':False}
    (out/'summary.json').write_text(json.dumps(report,indent=2)+'\n')
    return report
if __name__=='__main__':
    args=[s for s in sys.argv[1:] if s!='--full']
    main(args[0] if args else Path(__file__).parent/'verified','--full' in sys.argv)
