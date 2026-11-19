"""Exact arithmetic checks of the finite Clausen interpolation at 1/2."""
import argparse
import json
from fractions import Fraction
from math import comb, isqrt
from pathlib import Path


def primes(bound):
    return [p for p in range(5,bound+1,6) if all(p%i for i in range(2,isqrt(p)+1))]


def legendre_rows(M, modulus):
    # D_n=P_n(t)/t^n at t^2=1/2. D_{-1}=0 is only a start-up convention.
    prev,cur=0,1
    inv2=pow(2,-1,modulus)
    power=1
    for n in range(M+1):
        value=power*cur*((6*n+1)*cur-12*n*prev)%modulus
        yield cur,prev,value
        if n<M:
            prev,cur=cur,((2*n+1)*cur-2*n*prev)*pow(n+1,-1,modulus)%modulus
            power=power*inv2%modulus


def raw_binomial(p):
    modulus=p**3
    power=1
    inv=pow(216,-1,modulus)
    total=0
    for n in range((2*p-1)//3+1):
        total=(total+(6*n+1)*comb(2*n,n)**2*comb(3*n,n)*power)%modulus
        power=power*inv%modulus
    return total


def swisher(p):
    modulus=p**3
    term=1
    total=0
    for n in range((2*p-1)//3+1):
        total=(total+(6*n+1)*term)%modulus
        term=-term*pow(3*n+1,3,modulus)*pow(3*n+3,-3,modulus)%modulus
    return total


def second_jet(p,r):
    # Direct second Hasse coefficient in F_p[Z]/Z^3, independent of interpolation.
    coeff=[1,0,0]
    total=0
    for n in range(p//2+1):
        total=(total+(6*n+1)*coeff[2])%p
        scalar=(2*n+1)*pow(4*(n+1)**3,-1,p)%p
        gap=n*(n+1)-r*(r+1)
        a,b,c=coeff
        coeff=[scalar*gap*a%p,scalar*(gap*b-a)%p,scalar*(gap*c-b)%p]
    return total


def product_values(n,modulus):
    """Evaluate the terminating polynomial at integer degree n, without Legendre recurrence."""
    term=1
    total=0
    un=n*(n+1)
    for k in range(n+1):
        total=(total+(6*k+1)*term)%modulus
        if k<n:
            term=term*(2*k+1)*(k*(k+1)-un)*pow(4*(k+1)**3,-1,modulus)%modulus
    return total


def verify(p):
    M=(2*p-1)//3
    r=(p-2)//3
    H=p//2
    mod=p**3
    u=r*(r+1)%p
    nodes={}
    curvature=0
    for j,(d,prev,A) in enumerate(legendre_rows(M,mod)):
        if j in (r,M):
            nodes[j]=(d,prev,A)
            assert A==product_values(j,mod)
        if j>H:
            continue
        if j==r:
            weight=-162%p
        else:
            inv=pow(u-j*(j+1),-1,p)
            phi_prime=-1 if j==H else H
            weight=inv*(inv-9)*pow(2*phi_prime,-1,p)%p
        assert weight!=0
        curvature=(curvature+weight*(A%p))%p
    assert curvature==second_jet(p,r)
    A,B=nodes[r][2],nodes[M][2]
    blend=((4*p+2)*A+(1-p)*B)*pow(3*(p+1),-1,mod)%mod
    correction=-2*curvature*pow(81,-1,p)%p
    raw=raw_binomial(p)
    assert (blend+p*p*correction)%mod==raw
    E=swisher(p)
    assert E==(mod-2*p)%mod
    target=p%24 in (17,23)
    if target:
        for n in (r,M):
            d,prev,node=nodes[n]
            assert d%p==0 and node%p==0
            normalized=pow(2,-n,p*p)*(d//p)*((6*n+1)*p*(d//p)-12*n*prev)%(p*p)
            assert normalized==(node//p)%(p*p)
        assert (blend+p)%(p*p)==0
        residue=(blend+p)//(p*p)%p
        assert (residue==2*curvature*pow(81,-1,p)%p)==((2*raw-E)%mod==0)
    else:
        residue=None
    return dict(p=p,r=r,M=M,H=H,A_r_mod_p3=A,A_M_mod_p3=B,
                L_mod_p3=blend,R_mod_p=curvature,
                W_minus_L_over_p2_mod_p=correction,W_mod_p3=raw,E_mod_p3=E,
                bridge_residue_mod_p3=(2*raw-E)%mod,target_digit=residue,
                nonzero_kernel_entries=H+1)


def small_rational(p):
    r=(p-2)//3
    M=(2*p-1)//3
    u=Fraction(-2,9)
    def F(z):
        c=Fraction(1)
        total=0
        for k in range(M+1):
            total+=(6*k+1)*c
            c=c*(2*k+1)*(k*(k+1)-z)/Fraction(4*(k+1)**3)
        return total
    def true_mod(x):
        return x.numerator*pow(x.denominator,-1,p**3)%p**3
    A,B=F(r*(r+1)),F(M*(M+1))
    blend=Fraction(2*(2*p+1),3*(p+1))*A+Fraction(1-p,3*(p+1))*B
    curv=(F(u)-blend)/((u-r*(r+1))*(u-M*(M+1)))
    return dict(W=true_mod(F(u)),weighted_divided_difference_mod_p=true_mod(curv)%p)


def literature_regression(bound):
    rows=[]
    for p in range(5,min(bound,251)+1):
        if any(p%i==0 for i in range(2,isqrt(p)+1)):
            continue
        modulus=p**3
        inv=pow(216,-1,modulus)
        power=1
        total=0
        for k in range(p):
            total=(total+(6*k+1)*comb(2*k,k)**2*comb(3*k,k)*power)%modulus
            power=power*inv%modulus
        sign=1 if p%3==1 else -1
        split=pow(-6,(p-1)//2,p)==1
        assert (total-sign*p)%(modulus if split else p*p)==0
        assert (comb(3*p,p)*comb(2*p,p)**2-12)%modulus==0
        rows.append((p,split))
    return dict(full_sum_bound=min(bound,251),full_sum_count=len(rows),
                split_mod_p3_count=sum(split for _,split in rows),
                good_mod_p2_count=len(rows),polynomial_boundary_checks=len(rows))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--bound',type=int,default=1250)
    parser.add_argument('--out',type=Path)
    args=parser.parse_args()
    rows=[verify(p) for p in primes(args.bound)]
    small={str(row['p']):small_rational(row['p']) for row in rows if row['p']<=41}
    for row in rows:
        independent=small.get(str(row['p']))
        if independent:
            assert independent['W']==row['W_mod_p3'] and independent['weighted_divided_difference_mod_p']==row['R_mod_p']
    output=dict(literature_regression=literature_regression(args.bound),prime_bound=args.bound,all_prime_count=len(rows),
                target_prime_count=sum(x['p']%24 in (17,23) for x in rows),
                residue_counts={str(c):sum(x['p']%24==c for x in rows) for c in (5,11,17,23)},
                kernel_basis_checks=sum(x['nonzero_kernel_entries'] for x in rows),
                vanishing_curvature=[x['p'] for x in rows if x['R_mod_p']==0],
                finite_nonzero_bridge=[x['p'] for x in rows if x['bridge_residue_mod_p3']],
                independent_rational=small,
                samples=[x for x in rows if x['p'] in (5,11,17,23,41,311)])
    serialized=json.dumps(output,sort_keys=True,indent=2)+'\n'
    if args.out: args.out.write_text(serialized)
    else: print(serialized,end='')


if __name__=='__main__':
    main()
