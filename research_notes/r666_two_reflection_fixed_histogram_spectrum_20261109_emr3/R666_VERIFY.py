#!/usr/bin/env python3
"""R666 exact fixed-multiplicity spectra; pure standard-library integers."""
from itertools import combinations
from math import gcd
from pathlib import Path
import json
IDENT=(0,1,2)
A=(0,2,1); B=(2,1,0)
def perm(a,b): return tuple(a[b[i]] for i in range(3))
def power(a,n):
    x=IDENT
    for _ in range(n):x=perm(x,a)
    return x
R=perm(A,B)
assert R==(1,2,0) and power(R,3)==IDENT
def product(x,y,p):
    e,f=x; d,g=y
    return ((e+(-1 if f else 1)*d)%p,f^g)
def formula(m,n,p):
    N=m+n
    lo=max(0,n-N//2);hi=min(n,(N+1)//2)
    assert hi-lo+1==min(m,n)+1
    return {((n-2*x)%p,N%2) for x in range(lo,hi+1)}
def dp(m,n,p):
    mat=[[set() for _ in range(n+1)] for _ in range(m+1)]
    mat[0][0].add((0,0))
    for i in range(m+1):
        for j in range(n+1):
            if i:mat[i][j]|={product(t,(0,1),p) for t in mat[i-1][j]}
            if j:mat[i][j]|={product(t,(-1%p,1),p) for t in mat[i][j-1]}
    return mat[m][n]
def words(m,n):
    N=m+n
    for chosen in combinations(range(N),n):
        pick=set(chosen)
        yield ''.join('B' if i in pick else 'A' for i in range(N))
def evaluate(w,p):
    t=(0,0)
    for c in w:t=product(t,(0,1) if c=='A' else (-1%p,1),p)
    return t
def frame(w):
    f=IDENT
    for c in w:f=perm(f,A if c=='A' else B)
    return f
def native_step(u,v,f):
    assert len(set(u)&set(v))==2
    leaving=next(iter(set(u)-set(v))); entering=next(iter(set(v)-set(u)))
    d=dict(zip(u,f));d[entering]=d[leaving]
    return tuple(d[t] for t in v)
o=(0,1,2)
loop_a=(o,(0,1,3),(0,2,3),o)
loop_b=(o,(0,1,3),(1,2,3),o)
def native_loop(w):
    f=IDENT
    for c in w:
        t=loop_a if c=='A' else loop_b
        for u,v in zip(t,t[1:]):f=native_step(u,v,f)
    return f
assert native_loop('A')==A and native_loop('B')==B
dp_cases=0
for p in range(2,20):
    for m in range(23):
        for n in range(23):
            d=dp(m,n,p); assert d==formula(m,n,p)
            assert len(d)==min(p//gcd(p,2),min(m,n)+1)
            dp_cases+=1
word_count=0
for p in range(2,11):
    for m in range(8):
        for n in range(8):
            got=set()
            for w in words(m,n):
                x=evaluate(w,p);got.add(x);word_count+=1
                if p==3:
                    e,f=x
                    assert frame(w)==perm(power(R,e),A if f else IDENT)
            assert got==formula(m,n,p)
witness={}
for m,n in [(1,1),(2,1),(2,2),(3,3)]:
    vals={}
    for w in words(m,n):
        h=native_loop(w)
        assert h==frame(w)
        vals.setdefault(str(h),w)
    assert len(vals)==min(3,min(m,n)+1)
    witness[f'A{m}B{n}']={'count':len(vals),'examples':vals}
assert dp_cases==9522 and word_count==115821
result={'marker':'R666_TWO_REFLECTION_FIXED_HISTOGRAM_DIHEDRAL_SPECTRUM_PASS',
'R462_frozen':'18783e01e3646c72b7aab3b16d3f565e83e6446f',
'previous_R665':'c28925c3c0881894111a7049e16216fb2656cd60',
'dp_cases':dp_cases,'dp_p':'2..19','dp_m_n':'0..22',
'word_instances':word_count,'word_cases':576,'word_p':'2..10','word_m_n':'0..7',
'formula':'min(p/gcd(p,2),min(m,n)+1)',
'loop_A':[list(x) for x in loop_a],'loop_B':[list(x) for x in loop_b],
'witnesses':witness,'independent_review':'NOT_DONE','native_V29_license':'NOT_CHECKED'}
Path(__file__).with_name('R666_EVIDENCE.json').write_text(json.dumps(result,indent=2,ensure_ascii=False,sort_keys=True)+'\n',encoding='utf8')
print(result['marker'],dp_cases,word_count,[(k,v['count']) for k,v in witness.items()])
