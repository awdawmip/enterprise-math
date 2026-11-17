#!/usr/bin/env python3
"""R259: exact 23-adic modular-period certificates, frozen science 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Pure standard library; independent fixed-parameter regression of the symbolic theorem.
"""
import json
from fractions import Fraction as F
from functools import reduce
from math import gcd, lcm
from pathlib import Path

P = 23
W = (144,576,1440,4320,17280,86400,518400)
CASES = (
    # s, t, T, J, K, r, valid modular period
    ('35597/90113','411/529',2238406920,28499307077,9732204000,2,12144),
    ('24911/60947','412/529',1513923480,4197801049,2194092000,2,12144),
    ('804575/2062139','9445/12167',1178141253480,15106173046037,5122353276000,3,22),
)

def pv(n, p=P):
    n=F(n)
    def vi(a):
        if not a: return 10**9
        k=0
        while a%p==0:
            a//=p;k+=1
        return k
    return vi(n.numerator)-vi(n.denominator)

def ids(m):
    return [0]+[j+1 for j in range(6) if m>>j&1]

def times_linear(poly,a):
    out=[F(0)]*(len(poly)+1)
    for i,v in enumerate(poly):
        out[i]-=a*v
        out[i+1]+=v
    return out

def characteristic(ix,a,b):
    f=[F(1)]
    for i in ix: f=times_linear(f,a[i])
    for i in ix:
        g=[F(1)]
        for j in ix:
            if j!=i: g=times_linear(g,a[j])
        for j,v in enumerate(g): f[j]-=b[i]*v
    return f

def source(s):
    t=(1691*s-2615)/(2615*s-3539)
    a=[F(1,5),F(1,4),F(3,10),F(9,20),s,F(2,3),t]
    b=[F(13,60)]+[F(5,18)*abs(F(1,2)-x) for x in a[1:]]
    pi=[b[i]/(1-a[i]) for i in range(7)]
    assert sum(pi)==1
    Z=sum(b[i]/(1-a[i])**2 for i in range(7))
    rho=[b[i]/(Z*(1-a[i])**2) for i in range(7)]
    return t,a,b,pi,rho

def next_states(states, polynomials):
    return [st[1:]+(-sum(c[j]*st[j] for j in range(len(st)))%P,)
            for st,c in zip(states,polynomials)]

def run_case(s_text,t_text,T,J,K,r,period):
    s=F(s_text);t,a,b,pi,rho=source(s)
    assert t==F(t_text) and pv(t)==-r and pv(s)>=0
    assert F(39,100)<s<F(41,100)
    E=lcm(*(x.denominator for x in a+b))
    assert E==23*T and pv(T)==r-1
    assert J==lcm(*((W[m.bit_count()]*rho[i]).denominator
                  for m in range(63) for i in ids(m)))
    assert J*T**3%K==0
    u=F(T)*(a[6]+b[6]);v=F(T*T)*a[6]
    assert u.denominator%P!=0
    u=int(u.numerator*pow(u.denominator,-1,P))%P
    v=0 if r>=3 else int(v.numerator*pow(v.denominator,-1,P))%P
    assert u!=0 and (r!=2 or v!=0)
    polys=[];bases=[]
    for m in range(63):
        ix=ids(m);d=len(ix)
        cf=characteristic(ix,a,b)
        scaled=[x*T**(d-j) for j,x in enumerate(cf)]
        assert all(x.denominator==1 for x in scaled)
        c=[int(x) for x in scaled]
        expected=[0]*(d+1); expected[d]=1
        if 6 in ix:
            expected[d-1]=-u%P
            if r==2:
                B=sum(b[i] for i in ix if i!=6)
                assert B.denominator%P!=0
                Bmod=B.numerator*pow(B.denominator,-1,P)%P
                expected[d-2]=v*Bmod%P
        assert [x%P for x in c]==expected, (m, c, expected)
        polys.append(c)
        state=[F(1)]*d; row=[]
        for k in range(d+3):
            if k>=3:
                h=W[m.bit_count()]*sum(rho[i]*state[j] for j,i in enumerate(ix))
                H=J*T**k*h
                assert H.denominator==1 and int(H)%K==0
                row.append(int(H)//K%P)
            total=sum(pi[i]*state[j] for j,i in enumerate(ix))
            state=[a[i]*state[j]+(1-a[i])*total for j,i in enumerate(ix)]
        bases.append(tuple(row))
    assert sum(map(len,bases))==249
    states=bases
    early=[]
    for k in range(3,9):
        if not any(st[0] for st in states):early.append(k)
        states=next_states(states,polys)
    # The state vectors now represent k=9,...,9+d-1.
    assert all(states[m][0]==0 for m in range(32))
    initial=list(states)
    late=[];minactive=63;minpositions=[]
    for k in range(9,9+period):
        count=sum(st[0]!=0 for st in states)
        if count==0:late.append(k)
        if count<minactive:
            minactive=count;minpositions=[k]
        elif count==minactive and len(minpositions)<10:minpositions.append(k)
        states=next_states(states,polys)
    assert states==initial, 'full state not periodic at the stated bound'
    assert not early and not late, 'this parameter actually has a 23-adic first-factor drop'
    return {'s':str(s),'t':str(t),'r':r,'T':str(T),'J':str(J),'K':str(K),
            'u_mod23':u,'v_mod23':v,'period_checked':period,
            'all_63_source_states_return':True,
            'early_k_3_to_8_common_zero_count':len(early),
            'period_k_9_through_end_common_zero_count':len(late),
            'minimum_active_masks_per_event':minactive,
            'minimum_occurs_first_at':minpositions[0],
            'no_23_dip_for_all_k_ge_3':True}

def main():
    rows=[run_case(*case) for case in CASES]
    data={
        'schema':'EM_R259_23ADIC_UNIFORM_PERIOD_V1',
        'science_pin':'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
        'symbolic_theorem':'At 23-adic t-poles of order r>=2, mod-23 scaled source characteristics are y^d without source6, y^(d-2)(y^2-u*y+v*B_R) with source6 and r=2, and y^(d-1)(y-u) with source6 and r>=3. Normalized 63-mask outputs are jointly periodic from k=9 with period dividing 12144 (r=2) or 22 (r>=3).',
        'proof':'Rank-one characteristic identity; valuations v23(T)=r-1; nilpotent companion part dimension<=6; exponent GL_2(F_23)=lcm(23*(23-1),23^2-1)=12144.',
        'cases':rows,
        'arithmetic':'Python fractions.Fraction exact; all 63 source masks preserved, mod 23 recurrence; no floating approximations',
        'limits':'Finite cases do not show absence of dips for all rational parameters; first-factor 23-divisibility only, not all 23-adic drop exponents.',
        'review':'AUTHOR_PROVED / EXACT_MODULAR_VERIFIED / NOT_REVIEWED',
        'pass':True}
    dest=Path(__file__).with_name('R259_23adic_uniform_period_verification.json')
    dest.write_text(json.dumps(data,sort_keys=True,indent=2,ensure_ascii=False)+'\n')
    print('PASS R259:',len(rows),'new exact rational samples; universal symbolic period bound; 63 source labels')
    for x in rows:
        print(x['s'],'r=',x['r'],'period=',x['period_checked'], 'minimum_active=',x['minimum_active_masks_per_event'])

if __name__=='__main__':main()
