#!/usr/bin/env python3
"""R255: exact 13/23-adic spectral-scaling exceptions for the frozen 63-mask positive observer."""
from fractions import Fraction as F
from math import lcm
import hashlib, json
from pathlib import Path

PIN = "43ec6098b1330ae86d0a7863be336c5d97f6ef34"

def sources(s):
    t = (1691*s-2615)/(2615*s-3539)
    a = [F(1,5),F(1,4),F(3,10),F(9,20),s,F(2,3),t]
    b = [F(13,60)] + [F(5,18)*abs(F(1,2)-a[i]) for i in range(1,7)]
    assert F(39,100) <= s <= F(41,100)
    assert a[4] < F(1,2) and a[6] > F(1,2)
    return a,b

def mask(m):
    return [0]+[i+1 for i in range(6) if (m>>i)&1]

def times_linear(pol,a):
    q=[F(0)]*(len(pol)+1)
    for i,c in enumerate(pol):
        q[i]-=c*a
        q[i+1]+=c
    return q

def charpoly(a,b,ids):
    p=[F(1)]
    for i in ids:p=times_linear(p,a[i])
    for i in ids:
        q=[F(1)]
        for j in ids:
            if j!=i:q=times_linear(q,a[j])
        for k,c in enumerate(q):p[k]-=b[i]*c
    assert p[-1]==1
    return p

def v(q,p):
    q=F(q); n,d=q.numerator,q.denominator; e=0
    if n==0:return None
    while n%p==0:n//=p;e+=1
    while d%p==0:d//=p;e-=1
    return e

def factors(n):
    result=[];p=2
    while p*p<=n:
        if n%p==0:
            result.append(p)
            while n%p==0:n//=p
        p=3 if p==2 else p+2
    if n>1:result.append(n)
    return result

def integral_all(T, polys):
    return all((c*T**(d-j)).denominator==1 for poly in polys for d in [len(poly)-1]
               for j,c in enumerate(poly) if j<d)

def spectral_scale(a,b):
    polys=[charpoly(a,b,mask(m)) for m in range(63)]
    E=lcm(*(q.denominator for q in a+b))
    assert integral_all(E,polys)
    T=E
    for p in factors(E):
        while T%p==0 and integral_all(T//p,polys):T//=p
    assert integral_all(T,polys)
    assert all(not integral_all(T//p,polys) for p in factors(T))
    return E,T,polys

def main():
    examples=[F(2,5),F(46,117),F(66,169),F(67,169),F(857,2197),F(770,1973),F(767,1966)]
    rows=[]
    for s in examples:
        a,b=sources(s);E,T,polys=spectral_scale(a,b)
        assert len(polys)==63 and sum(len(p)-1 for p in polys)==249
        assert polys[9][-3] == F(11,18)*s+F(13,72)
        assert polys[32][0] == F(17,36)*a[6]-F(1,36)
        r13=-v(s,13) if v(s,13)<0 else 0
        r23=-v(a[6],23) if v(a[6],23)<0 else 0
        if r13:
            assert v(a[6],13)>=0
            assert v(F(13,18)*s+F(5,36),13)==1-r13
            assert v(T,13)==max(1,r13-1)
            assert v(E,13)==r13
            assert v(polys[9][-3],13)==-r13
        if r23:
            assert v(s,23)>=0
            assert v(F(23,18)*a[6]-F(5,36),23)==1-r23
            assert v(T,23)==max(1,r23-1)
            assert v(E,23)==r23
            assert v(polys[32][0],23)==-r23
        rows.append({'s':str(s),'t':str(a[6]),'E':str(E),'T_min':str(T),
                     'E_div_T':str(E//T),'v13_s':v(s,13),'v23_t':v(a[6],23),
                     'v13_T':v(T,13),'v23_T':v(T,23),'scaled_coefficients':249})
    grid=[]
    for j in range(390,411):
        a,b=sources(F(j,1000));E,T,_=spectral_scale(a,b)
        grid.append({'j':j,'T_min':str(T),'E_div_T':str(E//T)})
    assert all(x['E_div_T']=='1' for x in grid)
    assert next(x for x in rows if x['s']=='67/169')['E_div_T']=='13'
    assert next(x for x in rows if x['s']=='770/1973')['E_div_T']=='23'
    result={'schema':'EM_R255_PADIC_SPECTRAL_SCALING_EXCEPTIONS_V1',
            'frozen_science_pin':PIN,'arithmetic':'Fraction exact, no floats',
            'p_adic_theorem':'If v_13(s)=-r<0 or v_23(t)=-r<0, then v_p(T_min)=max(1,r-1), v_p(E)=r',
            'theorem_domain':'r>=1; rational 39/100 < s < 41/100; t(s)=(1691s-2615)/(2615s-3539)',
            'masks':63,'coefficient_positions':249,'exact_examples':rows,
            'grid_21_all_E_equal_T':True,'grid_21_results':grid,
            'mathematical_status':'AUTHOR_PROVED / EXACT_COMPUTATION / NOT_REVIEWED',
            'pass':True}
    raw=json.dumps(result,indent=2,sort_keys=True,ensure_ascii=False)+'\n'
    dest=Path(__file__).with_name('R255_verification.json')
    dest.write_text(raw)
    print('PASS exact samples',len(rows),'grid',len(grid),'SHA256',hashlib.sha256(raw.encode()).hexdigest())
    for row in rows:print(row['s'],row['T_min'],row['E_div_T'],row['v13_s'],row['v23_t'])
if __name__=='__main__':main()
