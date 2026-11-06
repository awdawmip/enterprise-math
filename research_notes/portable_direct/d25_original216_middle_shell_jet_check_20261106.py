#!/usr/bin/env python3
"""Exact modular checker: original 216 low + first-order middle and gap shells.
No external dependencies. All fractions have denominators prime to p.
"""
from math import isqrt, comb

def primes_leq(N):
    sv=bytearray(b'\x01')*(N+1)
    sv[0:2]=b'\x00\x00'
    for d in range(2,isqrt(N)+1):
        if sv[d]:
            sv[d*d::d]=b'\x00'*((N-d*d)//d+1)
    return [d for d in range(7,N+1) if sv[d] and d%6==1]

def study(p):
    m=(p-1)//6
    mod=p**3
    mod2=p**2
    a=[1]
    for k in range(1,p):
        n=k
        numer=(2*n-1)*(3*n-2)*(3*n-1)
        denom=36*n**3
        a.append(a[-1]*numer*pow(denom,-1,mod)%mod)
    if p in (7,13,19,31,67,373,997):
        for n in range(p):
            gamma=comb(2*n,n)**2*comb(3*n,n)
            independent=gamma*pow(216,-n,mod)%mod
            assert a[n]==independent,(p,n,'independent factorial mismatch')
    weighted=lambda k: (6*k+1)*a[k]
    direct=sum(weighted(k) for k in range(p))%mod
    low=sum(weighted(k) for k in range(2*m+1))%mod
    mid=sum(weighted(k) for k in range(2*m+1,3*m+1))%mod
    gap=sum(weighted(k) for k in range(3*m+1,4*m+1))%mod
    hi=sum(weighted(k) for k in range(4*m+1,p))%mod
    assert hi==0,(p,'upper shell nonzero',hi)
    q=1
    sigma=0
    q0=q1=0
    for j in range(m):
        if j:
            t=j
            ratio_num=3*t*(6*t+1)*(3*t+1)
            ratio_den=4*(3*t+2)**3
            q=q*ratio_num*pow(ratio_den,-1,mod2)%mod2
            sigma+=2*pow(6*t+1,-1,mod2)+pow(3*t,-1,mod2)+pow(3*t+1,-1,mod2)-3*pow(3*t+2,-1,mod2)
            sigma%=mod2
        q0=(q0+(6*j+5)*q)%mod2
        q1=(q1+q*(2+(6*j+5)*(3*pow(2,-1,mod2)+sigma)))%mod2
    formula=p*a[2*m]*pow(32,-1,mod)*(q0+p*q1)%mod
    assert mid==formula,(p,'middle formula mismatch',mid,formula)
    assert a[3*m]%p==0 and a[3*m]%(p*p)!=0
    g=1
    gap0=0
    for j in range(m):
        if j:
            t=j
            g=g*t*(6*t-1)*(6*t+1)*pow(9*(2*t+1)**3,-1,p)%p
        gap0=(gap0+(6*j+4)*g)%p
    a3_norm=(a[3*m]//p)%p
    last_q=q%p
    assert a3_norm == a[2*m]*pow(32,-1,p)*last_q%p,(p,'single seed mismatch',a3_norm,last_q)
    gap_one_seed=(-p*p*a[2*m]*pow(576,-1,p)*last_q*gap0)%mod
    gap_formula=(-p*p*a3_norm*pow(18,-1,p)*gap0)%mod
    assert gap==gap_formula==gap_one_seed,(p,'gap formula mismatch',gap,gap_formula,gap_one_seed)
    assert direct == (low+formula+gap_formula)%mod,(p,'full reduction mismatch',direct,low,formula,gap_formula)
    seed=a[2*m]*pow(32,-1,mod2)*(1+p*3*pow(2,-1,mod2))%mod2
    assert a[2*m+1]%mod == p*seed%mod
    return dict(p=p,m=m,full=direct,low=low,mid=mid,gap=gap,high=hi, gap0_mod_p=gap0,last_q_mod_p=last_q,
                q0_mod_p=q0%p,q1_mod_p=q1%p,
                a2m_mod_p=a[2*m]%p, normalized_middle=(mid//p)%mod2,
                native_target_residue=((direct-p)//(p*p))%p if (direct-p)%(p*p)==0 else None)

if __name__=='__main__':
    rows=[study(p) for p in primes_leq(1999)]
    print('passed',len(rows),'target',sum(p['p']%24 in (13,19) for p in rows),'failures=0')
    for v in rows:
        if v['p'] in (7,13,19,31,67,373):
            print(v)
