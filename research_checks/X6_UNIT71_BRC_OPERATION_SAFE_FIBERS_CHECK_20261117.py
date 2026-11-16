#!/usr/bin/env python3
"""Exact finite check of observer-fiber native path counts; author-scoped evidence, no native benchmark replay."""
import json
from collections import defaultdict
from itertools import product
from math import factorial, isqrt

D=6

def signature(z):
    lo=min(z)
    r=tuple(x-lo for x in z)
    return r,sum(x*x for x in z),sum(abs(x) for x in z)

def exact_fiber(sig):
    r,g,t=sig
    R=sum(r); Q=sum(x*x for x in r)
    disc=R*R+3*(g-Q)
    if disc<0:return tuple()
    q=isqrt(disc)
    if q*q!=disc:return tuple()
    out=set()
    for num in (-R-q,-R+q):
        if num%3:continue
        h=num//3
        z=tuple(h+x for x in r)
        if min(z)!=h or sum(x*x for x in z)!=g or sum(abs(x) for x in z)!=t:continue
        out.add(z)
    return tuple(sorted(out))

def short_mass(z):
    a=[abs(x) for x in z]
    t=sum(a)
    return factorial(t)//(factorial(a[0])*factorial(a[1])*factorial(a[2]))

def compositions(total,n):
    if n==1:
        yield (total,)
    else:
        for x in range(total+1):
            for tail in compositions(total-x,n-1):
                yield (x,)+tail

def native_count_with_excess(z,k):
    a=[abs(x) for x in z]+[0,0,0]
    L=sum(a)+2*k
    f=factorial(L)
    total=0
    for q in compositions(k,6):
        denominator=1
        for ai,qi in zip(a,q):
            denominator*=factorial(qi)*factorial(qi+ai)
        if f%denominator:raise ArithmeticError('nonintegral path term')
        total+=f//denominator
    return total

def run():
    sigs={signature(z) for z in product(range(-10,11),repeat=3)}
    counts={"observed_signatures":len(sigs),"singleton":0,"double":0,"balanced_double":0,"nonbalanced_double":0,
            "axis_labeled_equal_double":0,"orientation_distinct_double":0,"native_layer_checks":0,"counterexamples":0}
    examples={}
    for sig in sorted(sigs):
        zs=exact_fiber(sig)
        if len(zs)==1:
            counts['singleton']+=1
            continue
        if len(zs)!=2:raise ValueError((sig,zs))
        counts['double']+=1
        a,b=zs
        r=sig[0]
        balanced=(sorted(r)[0]+sorted(r)[2]==2*sorted(r)[1])
        equal_mass=short_mass(a)==short_mass(b)
        if balanced!=equal_mass:raise AssertionError(('short-mass criterion',sig,zs))
        counts['balanced_double' if balanced else 'nonbalanced_double']+=1
        same_slots=all(abs(x)==abs(y) for x,y in zip(a,b))
        if same_slots!=(r==(0,0,0)):raise AssertionError(('named-axis criterion',sig,zs))
        counts['axis_labeled_equal_double']+=int(same_slots)
        if a!=b:counts['orientation_distinct_double']+=1
        for k in range(4):
            v1=native_count_with_excess(a,k)
            v2=native_count_with_excess(b,k)
            if (v1==v2)!=balanced:raise AssertionError(('native-layer criterion',sig,zs,k,v1,v2))
            counts['native_layer_checks']+=1
        if balanced and not same_slots and 'unweighted_equal_named_different' not in examples:
            examples['unweighted_equal_named_different']={'r':r,'G':sig[1],'T':sig[2],'a':a,'b':b,
                'native_layers_a':[native_count_with_excess(a,k) for k in range(3)],
                'native_layers_b':[native_count_with_excess(b,k) for k in range(3)],
                'abs_a':tuple(map(abs,a)),'abs_b':tuple(map(abs,b))}
        if same_slots and 'named_equal_oriented_different' not in examples:
            examples['named_equal_oriented_different']={'r':r,'G':sig[1],'T':sig[2],'a':a,'b':b}
        if not balanced and 'unweighted_unequal' not in examples:
            examples['unweighted_unequal']={'r':r,'G':sig[1],'T':sig[2],'a':a,'b':b,'mass_a':short_mass(a),'mass_b':short_mass(b)}
    result={'schema':'EM_X6_UNIT71_OPERATION_SAFE_BRC_FIBER_FINITE_V1','date':'2026-11-17','scope':
           'observed can3,G,T signatures of all signed Z3 points in [-10,10]^3, complete global integer fibers; six-axis native paths k=0..3',
           'counts':counts,'examples':examples,'status':'FINITE_EXECUTED_AUTHOR_ONLY_UNREVIEWED_NOT_ADMITTED'}
    print(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2))

if __name__=='__main__':run()
