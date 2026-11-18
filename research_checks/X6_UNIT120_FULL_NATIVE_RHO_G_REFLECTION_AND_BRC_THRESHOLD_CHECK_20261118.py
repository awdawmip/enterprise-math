#!/usr/bin/env python3
"""X6 Unit120: exact full signed Z6 min-zero/quadratic reflection and BRC threshold.
Author-side finite exhaustive corroboration; not the original R063 benchmark.
"""
from collections import Counter, defaultdict
from itertools import product
from math import factorial, isqrt
import json


def require(ok, why):
    if not ok:
        raise RuntimeError(why)


def rho(z):
    h = min(z)
    return tuple(v-h for v in z)


def g(z):
    return sum(v*v for v in z)


def brc(z):
    t = sum(abs(v) for v in z)
    den = 1
    for v in z:
        den *= factorial(abs(v))
    return factorial(t)//den


def reflection(z):
    s = sum(z)
    if s % 3:
        return None
    return tuple(v-s//3 for v in z)


def recover(r, norm, sign):
    R = sum(r)
    D = 6*norm - 6*sum(v*v for v in r) + R*R
    if D < 0:
        return None
    root = isqrt(D)
    if root*root != D:
        return None
    s = root if sign >= 0 else -root
    if (s-R)%6:
        return None
    h = (s-R)//6
    z = tuple(v+h for v in r)
    return z if rho(z)==r and g(z)==norm else None


def run():
    cube = list(product(range(-2,3), repeat=6))
    fibers = defaultdict(list)
    source_with_integral_reflection = 0
    reflected_inside_cube = 0
    reconstruction = 0
    for z in cube:
        q, norm, s = rho(z), g(z), sum(z)
        fibers[(q,norm)].append(z)
        require(recover(q,norm,1 if s>=0 else -1)==z, 'lossless sign reconstruction')
        reconstruction+=1
        y = reflection(z)
        if y is not None:
            source_with_integral_reflection+=1
            require(reflection(y)==z and rho(y)==q and g(y)==norm,
                    'exact reflection involution invariant')
            if all(-2<=v<=2 for v in y):
                reflected_inside_cube+=1
    for key, fiber in fibers.items():
        require(len(fiber) in (1,2), f'fiber too large {key}')
        for z in fiber:
            y=reflection(z)
            if len(fiber)==2:
                require(y in fiber and y!=z, 'two-point reflection fiber')
            elif y is not None and y!=z:
                require(y not in cube, 'missing in-cube alias')
    shell = {}
    unequal_shells = {}
    for N in range(6):
        zset=[z for z in cube if g(z)==N]
        require(all(all(abs(v)<=2 for v in z) for z in zset),'shell coverage')
        by=defaultdict(list)
        for z in zset:
            by[rho(z)].append(z)
        require(all(len(v)<=2 for v in by.values()),'shell fiber')
        unequal=[v for v in by.values() if len(v)==2 and brc(v[0])!=brc(v[1])]
        shell[str(N)]={'native_endpoints':len(zset),
                       'observer_fibers':len(by),
                       'double_fibers':sum(len(v)==2 for v in by.values()),
                       'BRC_mismatching_double_fibers':len(unequal)}
        unequal_shells[N]=len(unequal)
    require(all(unequal_shells[N]==0 for N in range(5)),
            'no BRC mismatch in all full native shells below G5')
    require(unequal_shells[5]>0, 'G5 first BRC mismatch')
    x=(-1,-2,0,0,0,0);y=(0,-1,1,1,1,1)
    require(g(x)==g(y)==5 and rho(x)==rho(y)==(1,0,2,2,2,2),'G5 witness')
    require(reflection(x)==y and brc(x)==3 and brc(y)==120,'G5 BRC witness')
    require(len(cube)==15625 and reconstruction==15625,'cube complete')
    return {'schema':'X6_UNIT120_FULL_RHO_G_REFLECTION_CERTIFICATE_V1',
            'classification':'AUTHOR_PROOF_EXACT_INTEGER_CUBE_AND_FULL_G0_TO_G5',
            'frozen_P000_V5':'59538f585d037d09ef687b28715c4bc1a3f9fe03',
            'cube_size':len(cube),'cube_reconstructed':reconstruction,
            'cube_fibers':len(fibers),
            'integral_reflection_source_count':source_with_integral_reflection,
            'reflections_landing_in_cube':reflected_inside_cube,
            'shells_G0_to_G5':shell,'first_BRC_ambiguity_native_G':5,
            'witness':{'x':x,'y':y,'rho':rho(x),'G':5,
                       'BRC_x':brc(x),'BRC_y':brc(y)}}


if __name__=='__main__':
    print(json.dumps(run(),sort_keys=True,ensure_ascii=False,separators=(',',':')))
