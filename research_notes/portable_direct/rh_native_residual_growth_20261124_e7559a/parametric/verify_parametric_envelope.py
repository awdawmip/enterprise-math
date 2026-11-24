#!/usr/bin/env python3
"""Exact finite comparison of PAV and an independent all-subhat envelope."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from functools import lru_cache
from math import isqrt
import argparse
import json


@lru_cache(None)
def mass(u,v):
    return F(v-u,u*v)


def prefix(values,L):
    result=[F(0)]
    for n,z in enumerate(values,L):
        result.append(result[-1]+mass(n,n+1)*z)
    return result


def tau(prefix_values,L,u,x,v):
    left=(prefix_values[x-L]-prefix_values[u-L])/mass(u,x)
    right=(prefix_values[v-L]-prefix_values[x-L])/mass(x,v)
    return (left-right)/x


def pav_residual(values,L):
    pools=[]
    for n,z in enumerate(values,L):
        pools.append([n,n+1,mass(n,n+1)*z])
        while len(pools)>1:
            a,b=pools[-2:]
            if a[2]/mass(a[0],a[1])<=b[2]/mass(b[0],b[1]):
                break
            pools[-2:]=[[a[0],b[1],a[2]+b[2]]]
    fit=[F(0)]*len(values)
    for u,v,s in pools:
        fit[u-L:v-L]=[s/mass(u,v)]*(v-u)
    return prefix([a-b for a,b in zip(values,fit)],L)


def hat_background(u,x,v):
    return sum((F(n-u,(x-u)*n) if n<=x else F(v-n,(v-x)*n)
                for n in range(u+1,v)),F(0))


@lru_cache(None)
def geometry(L,x,R):
    a,b,h=x-L,R-x,R-L
    rows=[]
    for u in range(L,x):
        for v in range(x+1,R+1):
            c=F(h*(x-u)*(v-x),a*b*(v-u))
            B=hat_background(u,x,v)
            rows.append((u,v,c,B))
    Bfull=hat_background(L,x,R)
    assert all(0<c<=1 and c*B<=Bfull for _,_,c,B in rows)
    assert all(c*B<Bfull for u,v,c,B in rows if (u,v)!=(L,R))
    return F(h*x,a*b),Bfull,rows


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('parametric_envelope_certificate.json'))
    args=parser.parse_args()
    drifts=(F(0),F(1,4),F(1,2),F(1))
    counts={k:0 for k in ('sequences','split_points','pav_envelope_equalities',
                         'paid_drift_transitions','strict_paid_increases','flat_paid_transitions',
                         'compensator_checks','full_cost_drops_forbidden','zero_contact_checks')}
    for h in range(2,7):
        L,R=2,2+h
        indices=list(map(F,range(L,R)))
        for raw in product((-2,0,3),repeat=h):
            A=list(map(F,raw))
            pa=prefix(A,L)
            pav_by_drift={nu:pav_residual([z+nu*n for z,n in zip(A,indices)],L) for nu in drifts}
            g_lists=[[-F(3)]*h,indices,[n*n for n in indices]]
            g_data=[(g,prefix(g,L),pav_residual([a+c for a,c in zip(A,g)],L)) for g in g_lists]
            for x in range(L+1,R):
                C,Bfull,rows=geometry(L,x,R)
                lines=[(c*tau(pa,L,u,x,v),c*B) for u,v,c,B in rows]
                r0=C*pav_by_drift[F(0)][x-L]
                assert r0>=max(F(0),tau(pa,L,L,x,R))
                old_r=old_u=None
                for nu in drifts:
                    envelope=max([F(0)]+[intercept-nu*slope for intercept,slope in lines])
                    r=C*pav_by_drift[nu][x-L]
                    assert r==envelope
                    u=r+nu*Bfull
                    assert u>=r0
                    if old_u is not None:
                        assert r<=old_r and u>=old_u
                        counts['paid_drift_transitions']+=1
                        counts['strict_paid_increases']+=u>old_u
                        counts['flat_paid_transitions']+=u==old_u
                    old_r,old_u=r,u
                    counts['pav_envelope_equalities']+=1
                kill=max([F(0)]+[intercept/slope for intercept,slope in lines])
                killed=C*pav_residual([z+kill*n for z,n in zip(A,indices)],L)[x-L]
                assert killed==0
                if kill>0:
                    half=C*pav_residual([z+(kill/2)*n for z,n in zip(A,indices)],L)[x-L]
                    assert half>0
                counts['zero_contact_checks']+=1
                step=[F(n>=x) for n in range(L,R)]
                all_g=g_data+[(step,prefix(step,L),pav_residual([a+c for a,c in zip(A,step)],L))]
                for g,pg,rg in all_g:
                    cost=-tau(pg,L,L,x,R)
                    assert cost>=0
                    compensated=C*rg[x-L]
                    assert F(0)<=r0-compensated<=cost
                    assert compensated+cost>=r0
                    counts['compensator_checks']+=1
                    counts['full_cost_drops_forbidden']+=compensated+cost>=r0
                counts['split_points']+=1
            counts['sequences']+=1

    examples=[]
    for L,x,R,raw in [(2,3,5,(0,-1,0)),(2,3,4,(0,-1))]:
        A=list(map(F,raw));pa=prefix(A,L);C,B,rows=geometry(L,x,R)
        output=[]
        for nu in drifts:
            r=C*pav_residual([a+nu*n for n,a in enumerate(A,L)],L)[x-L]
            if R==5:
                assert r==(1-nu)/4 and r+nu*B==F(1,4)+F(5,24)*nu
            else:
                assert r==(1-nu)/3 and r+nu*B==F(1,3)
            output.append({'nu':str(nu),'residual':str(r),'full_paid':str(r+nu*B)})
        examples.append({'packet':[L,x,R],'values':list(raw),'tau':str(tau(pa,L,L,x,R)),
                         'background':str(B),'parameter_rows':output})

    # A nonmonotone compensator shows the theorem's stated scope is essential.
    L,x,R=2,3,5; A=[F(0),F(-1),F(0)]; nonmonotone=[-a for a in A]
    C,B,rows=geometry(L,x,R)
    before=C*pav_residual(A,L)[x-L]
    paid=-tau(prefix(nonmonotone,L),L,L,x,R)
    assert before==F(1,4) and paid==F(5,24)<before

    composites=[]
    for x in range(4,129):
        if any(x%d==0 for d in range(2,isqrt(x)+1)):
            assert hat_background(x-1,x,x+1)==F(1,x)
            composites.append(x)
    result={'schema':'RH_PARAMETRIC_RESIDUAL_ENVELOPE_V1','status':'PASS',
            'arithmetic':'Exact fractions; PAV checked against independent enumeration of every same-pivot subhat.',
            'input_domain':'L=2; h=2,...,6; all A in {-2,0,3}^h',
            'drifts_exact':[str(z) for z in drifts],
            'compensators':'constant -3; n; n^2; 1_(n>=x), each nondecreasing',
            'counts':counts,'examples':examples,
            'scope_counterexample':{'packet':[2,3,5],'A':[0,-1,0],'nonmonotone_C':[0,1,0],
                                    'old_residual':str(before),'paid_new_residual':str(paid)},
            'composite_atom_check':{'integer_range':[4,128],'composite_pivots':composites,
                                    'count':len(composites),'exact_background':'1/x',
                                    'ordinary_prime_mass':'0 by compositeness; no logarithms evaluated',
                                    'zero_contact_threshold':'1'},
            'scope':'Finite implementation evidence; all-parameter results are proved in PARAMETRIC_RESIDUAL_ENVELOPE.md. Author work, not independent Review.'}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'counts':counts,'composite_pivots':len(composites)}))


if __name__=='__main__':main()
