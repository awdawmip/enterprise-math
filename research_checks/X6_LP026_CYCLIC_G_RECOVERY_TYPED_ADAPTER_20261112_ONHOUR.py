#!/usr/bin/env python3
"""Finite-horizon native G reconstruction from a typed cyclic depth observer.
Standalone proposed adapter/checker; not an import of existing project modules.
"""
from collections import defaultdict

class NoReachableNativeLift(ValueError): pass
class AmbiguousNativeNorm(ValueError): pass

def recover_native_norm(relative, depth, modulus, word_length):
    r=tuple(relative)
    if len(r)!=6 or not all(type(x) is int and x>=0 for x in r) or min(r)!=0:
        raise ValueError('expected min-zero nonnegative six-axis section')
    if type(modulus) is not int or modulus<0 or type(depth) is not int:
        raise ValueError('invalid exact depth/modulus')
    if type(word_length) is not int or word_length<0:
        raise ValueError('word_length must be nonnegative')
    depths=(depth,) if modulus==0 else (h for h in range(-word_length,word_length+1) if (h-depth)%modulus==0)
    norms=set()
    for h in depths:
        z=tuple(x+h for x in r)
        L=sum(abs(x) for x in z)
        if L<=word_length and (word_length-L)%2==0:
            norms.add(sum(x*x for x in z))
            if len(norms)>1: raise AmbiguousNativeNorm((r,depth,modulus,word_length))
    if not norms: raise NoReachableNativeLift((r,depth,modulus,word_length))
    return next(iter(norms))

def key(z,m):
    h=min(z)
    return tuple(x-h for x in z),h if m==0 else h%m

def test(nmax=9):
    dist={(0,)*6:1}; checks=0; ambiguity=0
    for n in range(nmax+1):
        for m in (0,1,2,3,4):
            groups=defaultdict(set)
            for z in dist: groups[key(z,m)].add(sum(x*x for x in z))
            for (r,h), norms in groups.items():
                try:
                    actual=recover_native_norm(r,h,m,n)
                except AmbiguousNativeNorm:
                    assert len(norms)>1,(n,m,r,h,norms)
                    ambiguity+=1
                else: assert norms=={actual},(n,m,r,h,norms,actual)
                checks+=1
        if n<nmax:
            nxt=defaultdict(int)
            for z,v in dist.items():
                for i in range(6):
                    for d in (-1,1):
                        zz=list(z);zz[i]+=d;nxt[tuple(zz)]+=v
            dist=dict(nxt)
    assert recover_native_norm((0,0,0,1,1,1),0,1,3)==3
    assert recover_native_norm((0,)*6,0,1,0)==0
    a=(-3,-3,0,-1,-1,-1);r,h=key(a,3)
    assert recover_native_norm(r,h,3,9)==21
    try: recover_native_norm((0,)*6,0,1,6)
    except AmbiguousNativeNorm: pass
    else: raise AssertionError('expected ambiguous native norm')
    print('PASS_X6_TYPED_CYCLIC_G_RECOVERY',checks,'cover_key_cases; ambiguous_cases',ambiguity)
    print('m=3,N=9 boundary native G=21 (BRC remains unsafe)')
    return checks

if __name__=='__main__': test()
