#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math, random
from collections import Counter, defaultdict
from functools import lru_cache

CORPUS_SEED=0x5A17C0DE
PUBLIC_SEEDS=tuple(range(64))

def is_prime(n:int)->bool:
    if n<2:return False
    for p in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n==p:return True
        if n%p==0:return False
    d=n-1;s=0
    while d%2==0:s+=1;d//=2
    for a in (2,325,9375,28178,450775,9780504,1795265022):
        if a%n==0:continue
        x=pow(a,d,n)
        if x in (1,n-1):continue
        for _ in range(s-1):
            x=x*x%n
            if x==n-1:break
        else:return False
    return True

def next_prime(n:int)->int:
    n=max(2,n)
    if n==2:return 2
    if n%2==0:n+=1
    while not is_prime(n):n+=2
    return n

def factor_small(n:int)->tuple[int,...]:
    out=[];x=n;d=2
    while d*d<=x:
        while x%d==0:out.append(d);x//=d
        d=3 if d==2 else d+2
    if x>1:out.append(x)
    return tuple(out)

def spsp2(n:int)->bool:
    if n<3 or n%2==0 or is_prime(n):return False
    d=n-1;s=0
    while d%2==0:s+=1;d//=2
    x=pow(2,d,n)
    if x in (1,n-1):return True
    for _ in range(s-1):
        x=x*x%n
        if x==n-1:return True
    return False

def band(bits:int)->str:
    return 'B05_12' if bits<=12 else ('B13_16' if bits<=16 else ('B17_20' if bits<=20 else 'B21_PLUS'))

def build_corpus():
    rng=random.Random(CORPUS_SEED);out=[];seen=set();case_i=0
    def add(cid,n,family,factors):
        if n in seen or n<=3 or len(factors)<2:return
        assert math.prod(factors)==n
        seen.add(n);out.append({'case_id':cid,'n':n,'family':family,'bit_length':n.bit_length(),'band':band(n.bit_length()),'factors':tuple(sorted(factors))})
    for bits in (10,12,14,16,18,20):
        half=bits//2
        for k in range(4):
            base=(1<<(half-1))+rng.randrange(1,max(3,1<<max(1,half-2)))
            p=next_prime(base);q=next_prime(p+2+2*k)
            if p==q:q=next_prime(q+2)
            case_i+=1;add(f'C{case_i:04d}',p*q,'balanced_semiprime',(p,q))
        for k in range(3):
            pb=max(3,bits//4);qb=max(4,bits-pb)
            p=next_prime((1<<(pb-1))+2*k+1)
            q=next_prime((1<<(qb-1))+rng.randrange(1,1<<max(1,qb-3)))
            if p==q:q=next_prime(q+2)
            case_i+=1;add(f'C{case_i:04d}',p*q,'unbalanced_semiprime',(p,q))
        for k in range(3):
            center=(1<<(half-1))+rng.randrange(5,max(7,1<<max(2,half-2)))
            p=next_prime(center);q=next_prime(p+2)
            case_i+=1;add(f'C{case_i:04d}',p*q,'near_twin_semiprime',(p,q))
        p=next_prime((1<<max(2,bits//3-1))+1);e=2
        while (p**(e+1)).bit_length()<=bits:e+=1
        case_i+=1;add(f'C{case_i:04d}',p**e,'prime_power',(p,)*e)
        p=next_prime((1<<max(2,bits//5-1))+1);q=next_prime(p+4);r=next_prime((1<<max(3,bits//2-1))+rng.randrange(1,8))
        case_i+=1;add(f'C{case_i:04d}',p*q*r,'multi_prime',(p,q,r))
    for n in (561,1105,1729,2465,2821,6601,8911,10585,15841,29341):
        case_i+=1;add(f'C{case_i:04d}',n,'carmichael',factor_small(n))
    for n in (2047,3277,4033,4681,8321,15841,29341,42799,49141,52633):
        if spsp2(n):case_i+=1;add(f'C{case_i:04d}',n,'strong_pseudoprime_base2',factor_small(n))
    collision=[]
    for s in PUBLIC_SEEDS:
        if s<2:continue
        for v in (s*s+1,s*s+s+1,s**6-1,s**6+1):
            if v>3:
                fac=factor_small(abs(v))
                if len(fac)>=2 and abs(v)%2==1 and abs(v).bit_length()<=22:collision.append(abs(v))
        if len(set(collision))>=12:break
    for n in sorted(set(collision))[:12]:
        case_i+=1;add(f'C{case_i:04d}',n,'coordinate_collision',factor_small(n))
    return out

@lru_cache(maxsize=None)
def A(s:int)->int:
    a=1
    for k in range(s):
        num=a*6*(2*k+1)*(3*k+1)*(3*k+2);den=(k+1)**3
        assert num%den==0;a=num//den
    return a

def wall_vector(n:int,s:int):
    a=A(s);d=[1]
    for k in (1,2,3):d.append(math.gcd(a,n**k))
    return {'D':d[1:],'H':[d[k]//d[k-1] for k in (1,2,3)]}

def split_n_only(n:int):
    d=math.gcd(n,6)
    if 1<d<n:return {'factor':d,'class':'SMALL_PRIME_PRECHECK','s':None,'H':None,'u':None}
    s=1
    while s<=math.isqrt(n):
        w=wall_vector(n,s);g=w['D'][0]
        if g==1:s*=2;continue
        if 1<g<n:return {'factor':g,'class':'DIRECT_W1_SEPARATOR','s':s,'H':w['H'],'u':None}
        h2=w['H'][1]
        if 1<h2<n:return {'factor':h2,'class':'W1_SYNC_W2_SEPARATOR','s':s,'H':w['H'],'u':None}
        if h2==1:cl='FULL_SYNC_HIGH_BIN_2S_3S'
        elif h2==n:cl='FULL_SYNC_LOW_BIN_3S2_2S'
        else:raise AssertionError(('bad H2',n,s,w))
        assert w['H'][2]==1
        u=math.isqrt(n)//3+1;g2=math.gcd(A(u),n)
        return {'factor':g2,'class':cl,'s':s,'H':w['H'],'u':u}
    raise AssertionError(('no dyadic wall',n))

def poly_probe(n:int,sixth:bool):
    for s in PUBLIC_SEEDS:
        vals=(s**6-1,s**6+1) if sixth else (s*s+1,s*s+s+1)
        for v in vals:
            g=math.gcd(abs(v),n)
            if 1<g<n:return True
    return False

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out');args=ap.parse_args()
    corpus=build_corpus();assert len(corpus)==89
    assert sum(poly_probe(c['n'],False) for c in corpus)==74
    assert sum(poly_probe(c['n'],True) for c in corpus)==84
    rows=[];classes=Counter();family=defaultdict(Counter)
    for c in corpus:
        fac=c['factors'];domain=len(fac)==2 and fac[0]!=fac[1] and all(x%2 and is_prime(x) for x in fac)
        if not domain:continue
        p,q=fac;res=split_n_only(c['n']);d=res['factor']
        assert 1<d<c['n'] and c['n']%d==0
        if res['s'] is not None:
            s=res['s'];assert s<p
            vp=(2*s)//p+(3*s)//p;vq=(2*s)//q+(3*s)//q
            assert 0<=vq<=vp<=3
            h=res['H']
            for j in (1,2,3):
                expected=(p if vp>=j else 1)*(q if vq>=j else 1);assert h[j-1]==expected
            if res['class'].startswith('FULL_SYNC'):
                u=res['u'];assert u<p and p<3*u<q and math.gcd(A(u),c['n'])==p
        classes[res['class']]+=1;family[c['family']][res['class']]+=1
        rows.append({'case_id':c['case_id'],'family':c['family'],'n':c['n'],'proof_factors':[p,q],'class':res['class'],'first_wall_seed':res['s'],'wall_quotients':res['H'],'fallback_u':res['u']})
    assert len(rows)==61
    evidence={'schema':'PCF3_HIDDEN_FACTOR_SEPARATION_SPECTRUM_EVIDENCE_V1','pcf2_corpus_cases':89,'semiprime_theorem_domain_cases':61,'pcf2_probe_regression':{'quadratic_successes':74,'sixth_power_successes':84},'kernel_spectrum_classes':dict(sorted(classes.items())),'family_classes':{k:dict(sorted(v.items())) for k,v in sorted(family.items())},'theorem_checks':{'candidate_input':'N only','all_61_split':True,'single_fallback_inequality_checked':True,'wall_projection_formula_checked':True},'collision_registry':rows}
    txt=json.dumps(evidence,sort_keys=True,indent=2)+'\n'
    if args.out:open(args.out,'w').write(txt)
    print('PCF3_SPECTRUM_CHECK_PASS corpus=89 theorem_domain=61 splits=61 classes='+json.dumps(dict(sorted(classes.items())),sort_keys=True))
if __name__=='__main__':main()
