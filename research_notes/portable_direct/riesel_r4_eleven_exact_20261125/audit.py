import json,re,itertools
from fractions import Fraction as Q
from math import gcd,prod
from pathlib import Path
def read(f):
    return json.loads(Path(f).read_text())
m=read('minimum.json'); d=read('density.json'); t=read('templates.json')
a=int(m['minimum']); base=int(m['minimuma4']); step=int(m['step'])
E10=read('ten-density.json')['E10']
N,D=map(int,(E10['numerator'],E10['denominator']))
ds=Path('density.js').read_text()
assert all(int(re.search(fr't{v}=BigInt\("(\d+)"\)',ds).group(1))==x for v,x in zip('ND',(N,D)))
all_h={}
for row in d['inventory'].values():
    all_h.setdefault(row['h'],[]).append(row)
def hits(a,key):
    h,b=map(int,key.split(':'))
    return any(gcd(int(row['carrier']), (a*a*pow(2,32+36*b,int(row['carrier']))-1)%int(row['carrier']))>1 for row in all_h[h])
keyhit={s:hits(a,s) for s in set(itertools.chain.from_iterable(t))}
winning=[xs for xs in t if all(keyhit[s] for s in xs)]
assert winning==[['12:0','15:5','15:8','15:11']],winning
def inv_options(b):
    opts=[]
    for row in all_h[20]:
        for q in map(int,row['factors']):
            r=pow(2,-16-18*b,q)
            opts.extend((q, ((z-base)*pow(step,-1,q))%q) for z in (r,-r))
    return opts
bounds=[u+p*((v-u)*pow(p,-1,q)%q) for (p,u),(q,v) in itertools.product(inv_options(0),inv_options(8)) if p!=q]
assert min(bounds)==int(m['pairBound']['best'])
c=list(map(int,d['symbolicCoefficients']))
known=list(map(int,d['known140']))
def eval_formula(extra):
    qs=known+extra
    return sum(Q(cj,int(d['denominator']))*prod(Q(q-2*j,q) for q in qs) for j,cj in enumerate(c))-Q(N,D)
L=eval_formula([]); U=eval_formula([int(d['firstAbove'])]*(d['primeInterval'][1]-142))
assert L==Q(int(d['lower']['n']),int(d['lower']['d']))
assert U==Q(int(d['upper']['n']),int(d['upper']['d']))
assert Q('2.4892508568010196e-14')<=L<U<=Q('2.4892508568010290e-14')
assert 0<U-L<Q('9.224e-29')
print('Full-carrier gcd unique winner:',winning)
print('Independent pair CRT:',len(bounds),min(bounds))
print('Symbolic exact fractions match both endpoints and E10 pinned snapshot')
