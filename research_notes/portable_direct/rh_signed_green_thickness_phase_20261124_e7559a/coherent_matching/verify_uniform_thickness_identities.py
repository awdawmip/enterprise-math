#!/usr/bin/env python3
"""Exact finite validation of the new uniform-thickness interfaces."""
from fractions import Fraction as F
from itertools import combinations, product
from math import isqrt
from pathlib import Path
import argparse
import json


def primes_and_mu(limit):
    factors=[[] for _ in range(limit+1)]
    for p in range(2,limit+1):
        if not factors[p]:
            for n in range(p,limit+1,p):factors[n].append(p)
    mu=[0]*(limit+1);mu[1]=1
    for n in range(2,limit+1):
        mu[n]=0 if any(n%(p*p)==0 for p in factors[n]) else (-1)**len(factors[n])
    return factors,mu


def polynomial_add(*polys):
    out={}
    for poly in polys:
        for key,value in poly.items():out[key]=out.get(key,F(0))+value
    return {k:v for k,v in out.items() if v}


def polynomial_scale(poly,scalar):
    return {k:v*scalar for k,v in poly.items() if v*scalar}


def polynomial_multiply(left,right):
    out={}
    for (i,j),x in left.items():
        for (k,l),y in right.items():
            key=(i+k,j+l);out[key]=out.get(key,F(0))+x*y
    return {k:v for k,v in out.items() if v}


def symbolic_checks():
    one={(0,0):F(1)};gamma={(1,0):F(1)};gamma1={(0,1):F(1)}
    gamma2=polynomial_multiply(gamma,gamma)
    g1=one;g2=polynomial_scale(gamma,-1);g3=polynomial_add(gamma2,gamma1)
    assert polynomial_add(g2,gamma)=={}
    assert polynomial_add(g3,polynomial_multiply(gamma,g2),polynomial_scale(gamma1,-1))=={}
    c0=polynomial_add(one,gamma,polynomial_add(gamma,polynomial_scale(one,-1)),polynomial_scale(g2,2))
    assert c0=={}
    c1=polynomial_add(polynomial_multiply(polynomial_add(gamma,polynomial_scale(one,-1)),g2),polynomial_scale(g3,3))
    assert c1==polynomial_add(gamma,polynomial_scale(gamma2,2),polynomial_scale(gamma1,3))
    return 4


def interpolate(nodes,values,n):
    for j in range(len(nodes)-1):
        if nodes[j]<=n<=nodes[j+1]:
            width=nodes[j+1]-nodes[j]
            return ((nodes[j+1]-n)*values[j]+(n-nodes[j])*values[j+1])/width
    raise AssertionError('integer outside closed grid')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('uniform_thickness_identity_certificate.json'))
    args=parser.parse_args()
    limit=128;factors,mu=primes_and_mu(limit)
    harmonic=[F(0)]
    for n in range(1,limit+1):harmonic.append(harmonic[-1]+F(1,n))
    counts={'source_product_divisor':0,'unit_subtraction':0,'hyperbola':0,'complete_prefix_kernel':0,'small_node_grids':0,'small_node_signed_vectors':0,'closed_integer_evaluations':0}
    integer_thicknesses=[1,2,3,5]
    for a in integer_thicknesses:
        weighted_mu=[F(0)]+[F(mu[n],n**a) for n in range(1,limit+1)]
        cumulative_mu=[F(0)]
        f=[F(0)]*(limit+1);D=[F(0)]*(limit+1)
        for n in range(1,limit+1):
            cumulative_mu.append(cumulative_mu[-1]+weighted_mu[n])
            exact_product=F(1)
            for p in factors[n]:exact_product*=1-F(1,p**a)
            divisor_sum=sum((weighted_mu[d] for d in range(1,n+1) if n%d==0),F(0))
            assert exact_product==divisor_sum
            counts['source_product_divisor']+=1;f[n]=exact_product
            D[n]=(f[n]-(1 if n==1 else 0))/a
            assert D[n]==(F(0) if n==1 else exact_product/a)
            counts['unit_subtraction']+=1
        for y in range(1,limit+1):
            N=isqrt(y)
            hyperbola=sum((weighted_mu[d]*(y//d) for d in range(1,N+1)),F(0))
            hyperbola+=sum((cumulative_mu[y//r] for r in range(1,N+1)),F(0))-N*cumulative_mu[N]
            assert hyperbola==sum(f[1:y+1],F(0))
            counts['hyperbola']+=1
            road=sum(((F(y,n)-1)*D[n] for n in range(1,y+1)),F(0))
            swapped=sum((weighted_mu[d]*(F(y,d)*harmonic[y//d]-(y//d)) for d in range(1,y+1)),F(0))/a-F(y-1,a)
            assert road==swapped
            counts['complete_prefix_kernel']+=1
    for B in (8,16,32,64):
        Y=isqrt(B)
        for A in (1,2,3):
            if A>=B:continue
            candidates=sorted({A+1,Y,Y+1,B-1}-{A,B})
            candidates=[n for n in candidates if A<n<B]
            for size in range(len(candidates)+1):
                for selected in combinations(candidates,size):
                    nodes=(A,*selected,B)
                    small=[j for j,n in enumerate(nodes) if n<=Y]
                    counts['small_node_grids']+=1
                    for signs in product((-1,0,1),repeat=len(small)):
                        values=[F(0)]*len(nodes)
                        for j,sign in zip(small,signs):values[j]=F(nodes[j]*sign)
                        energy=F(0)
                        for n in range(A,B+1):
                            value=interpolate(nodes,values,n)
                            energy+=value*value/(n*n)
                            counts['closed_integer_evaluations']+=1
                        assert energy<=2*Y
                        counts['small_node_signed_vectors']+=1
    result={'schema':'EM_UNIFORM_SINGLE_THICKNESS_IDENTITY_V1','status':'PASS','arithmetic':'Exact rational arithmetic and symbolic polynomials; no floating-point admission','scope':'Finite identities and interpolation-bound checks only; the all-positive-thickness asymptotic is proved analytically in the companion document','integer_thicknesses':integer_thicknesses,'maximum_source_integer':limit,'counts':counts,'formal_laurent_identity_checks':symbolic_checks(),'unit_convention':'D_a(1)=0; complete prefix subtracts (y-1)/a'}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False))


if __name__=='__main__':main()
