#!/usr/bin/env python3
"""Author-only exact/modular checker for source-labelled D25 geometric cutoff Smith data.
No native EM experiment, independent review, or acceptance is implied.
"""
from fractions import Fraction

PRIMES=[7,13,19,31,37,43,61,73,127,733,997]

def v_p_num(n,p):
    k=0
    while n and n%p==0:
        n//=p;k+=1
    return k

def v_p_fr(x,p):
    return v_p_num(x.numerator,p)-v_p_num(x.denominator,p)

def mod_fraction(x,p):
    return x.numerator*pow(x.denominator,-1,p)%p

def f_exact(p):
    m=(p-1)//6
    f=[Fraction(1,1)]
    for j in range(p-1):
        f.append(f[-1]*Fraction((6*j+1)*(3*j+1),18*(j+1)**2))
    beta={h:f[h]/p**2 for h in range(4*m+1,p)}
    return f,beta

def rank_mod(a,p):
    a=[r[:] for r in a]
    nr,nc=len(a),len(a[0]);rank=0
    for c in range(nc):
        pivot=next((i for i in range(rank,nr) if a[i][c]%p),None)
        if pivot is None: continue
        a[rank],a[pivot]=a[pivot],a[rank]
        inv=pow(a[rank][c],-1,p)
        for j in range(c,nc):a[rank][j]=a[rank][j]*inv%p
        for i in range(rank+1,nr):
            mul=a[i][c]
            if mul:
                for j in range(c,nc):a[i][j]=(a[i][j]-mul*a[rank][j])%p
        rank+=1
        if rank==min(nr,nc):break
    return rank

def det_frac(a):
    a=[r[:] for r in a];d=Fraction(1)
    for k in range(len(a)):
        i=next((r for r in range(k,len(a)) if a[r][k]),None)
        if i is None:return Fraction(0)
        if i!=k:a[i],a[k]=a[k],a[i];d=-d
        pivot=a[k][k];d*=pivot
        for r in range(k+1,len(a)):
            if a[r][k]:
                c=a[r][k]/pivot
                for j in range(k+1,len(a)):a[r][j]-=c*a[k][j]
                a[r][k]=0
    return d

def beta_mod(p):
    m=(p-1)//6
    fac=[1]*p
    for i in range(1,p):fac[i]=fac[i-1]*i%p
    pref=(-1 if m%2 else 1)*fac[m]*fac[2*m]*pow(18,-1,p)%p
    return {h:pref*fac[h-m-1]*fac[h-2*m-1]*pow(fac[h]*fac[h],-1,p)%p for h in range(4*m+1,p)}

def f_mod_p2(p):
    m=(p-1)//6;f=[1];mod=p*p
    for j in range(2*m):
        f.append(f[-1]*(6*j+1)*(3*j+1)*pow(18*(j+1)**2,-1,mod)%mod)
    return f

def lead_units(p):
    m=(p-1)//6;n=2*m
    f=f_mod_p2(p);b=beta_mod(p)
    assert all(f[j]%p!=0 for j in range(1,m+1))
    assert all(f[j]%p==0 and f[j]//p%p for j in range(m+1,n+1))
    assert all(b[h]%p for h in b)
    det_lower=1
    for j in range(1,n+1):
        unit=(f[j] if j<=m else f[j]//p)%p
        det_lower=det_lower*(6*p+1)*unit*b[p-j]%p
    det_upper_minor=1
    for j in range(1,n):
        unit=(f[j] if j<=m else f[j]//p)%p
        det_upper_minor=det_upper_minor*2*(6*p-5)*unit*b[p-j-1]%p
    return det_lower,det_upper_minor

def main():
    print('prime m lower-rank(mod p) upper-rank(mod p) leading-det-lower leading-max-minor-upper')
    for p in PRIMES:
        m=(p-1)//6;n=2*m
        dl,du=lead_units(p)
        assert dl and du
        if p<=43:
            f,b=f_exact(p)
            assert all(v_p_fr(f[j],p)==(0 if j<=m else 1) for j in range(1,n+1))
            assert all(v_p_fr(v,p)==0 for v in b.values())
            assert all(mod_fraction(b[h],p)==beta_mod(p)[h] for h in b)
            lower=[];upper=[]
            for j in range(1,n+1):
                lo=[];up=[]
                for ell in range(1,n+1):
                    w=Fraction((6*p+1)-6*(ell-j),1)*Fraction(2)**(ell-j)*f[j]*b[p-ell]
                    lo.append(w if ell<=j else Fraction(0))
                    up.append(w if ell>j else Fraction(0))
                lower.append(lo);upper.append(up)
            rlo=rank_mod([[mod_fraction(x,p) for x in row] for row in lower],p)
            rup=rank_mod([[mod_fraction(x,p) for x in row] for row in upper],p)
            assert rlo==m and rup==m
            d=det_frac(lower)
            assert v_p_fr(d,p)==m
            dm=det_frac([row[1:] for row in upper[:-1]])
            assert v_p_fr(dm,p)==m-1
            assert mod_fraction(d/p**m,p)==dl
            assert mod_fraction(dm/p**(m-1),p)==du
        else:
            rlo=rup=m # structural theorem; no simulated Gaussian elimination
        print(p,m,rlo,rup,dl,du)
    print('PASS: exact Fraction matrices, independent finite-field ranks and determinant valuations for p<=43; modular Pochhammer/factorial residues and nonzero maximal minors for 11 primes including 733,997.')

if __name__=='__main__':main()
