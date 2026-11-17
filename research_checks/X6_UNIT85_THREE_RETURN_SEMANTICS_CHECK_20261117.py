#!/usr/bin/env python3
"""Exact integer census of three *typed* return predicates in native signed X6.

Pinned scientific interpretation: P000 V5 six signed primitive axes, rho(z)=z-min(z)*1.
This independent checker does not execute any original R063/Helly benchmark.
"""
from collections import defaultdict
from math import comb, factorial
import json

AXES=6
MAX_L=12
ZERO=(0,)*AXES


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def axis_convolution(length, h):
    """Exact independent coefficient: [sum of 6 labelled +/- walks ending at (h,)*6]."""
    dp={0:1}
    for _ in range(AXES):
        next_dp=defaultdict(int)
        for used, multiplicity in dp.items():
            for t in range(abs(h), length-used+1, 2):
                plus=(t+h)//2
                require(0<=plus<=t, 'invalid sign decomposition')
                next_dp[used+t]+=multiplicity*comb(used+t,t)*comb(t,plus)
        dp=next_dp
    return dp.get(length,0)


def run():
    dist={ZERO:1}
    rows=[]
    checked_fibers=0
    total_states=0
    for length in range(MAX_L+1):
        require(sum(dist.values())==12**length, f'mass conservation at {length}')
        total_states+=len(dist)
        depth={}
        for h in range(-length//AXES, length//AXES+1):
            endpoint=(h,)*AXES
            dp_count=dist.get(endpoint,0)
            coefficient=axis_convolution(length,h)
            require(dp_count==coefficient, f'coefficient disagreement L={length},h={h}')
            checked_fibers+=1
            if dp_count:
                depth[str(h)]=dp_count
        signed_native=dist.get(ZERO,0)
        signed_relative=sum(depth.values())
        positive_relative=(factorial(length)//(factorial(length//AXES)**AXES)
                           if length%AXES==0 else 0)
        rows.append({'length':length,'signed_native_zero':signed_native,
                     'signed_minzero_relative_return':signed_relative,
                     'positive_minzero_relative_return':positive_relative,
                     'signed_diagonal_depth_multiplicity':depth,
                     'reachable_native_endpoints':len(dist)})
        if length<MAX_L:
            nxt=defaultdict(int)
            for z, mass in dist.items():
                for axis in range(AXES):
                    a=list(z);a[axis]+=1;nxt[tuple(a)]+=mass
                    a[axis]-=2;nxt[tuple(a)]+=mass
            dist=nxt
    by_length={r['length']:r for r in rows}
    require(all(by_length[L]['signed_minzero_relative_return']==by_length[L]['signed_native_zero'] for L in range(6)), 'first divergence earlier than 6')
    require((by_length[6]['signed_native_zero'],by_length[6]['signed_minzero_relative_return'],by_length[6]['positive_minzero_relative_return'])==(19920,21360,720), 'six-step triple')
    require(by_length[12]['positive_minzero_relative_return']==7484400, 'published positive section result')
    return {'schema':'X6_UNIT85_SIGNED_POSITIVE_NATIVE_RETURN_EXACT_V1',
            'scope':'native six labelled signed axes; min-zero quotient observer; positive six-step subset',
            'max_horizon':MAX_L, 'tested_diagonal_depth_fibers':checked_fibers,
            'total_native_support_states_cumulative':total_states,
            'results':rows, 'failures':0,
            'review':'AUTHOR_EXACT_UNREVIEWED_NOT_ADMITTED'}

if __name__=='__main__':
    print(json.dumps(run(), ensure_ascii=False,sort_keys=True,separators=(',',':')))
