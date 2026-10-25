#!/usr/bin/env python3
"""C316 exact floor-defect residue classification for frozen C275 auxiliary.
Python stdlib Fraction only; optional --with-c314 validates frozen C284 path
slopes and original C275 masses. Not a native BRC/X6 or Source admission result.
"""
import sys, os, json
from math import prod
from fractions import Fraction as F
from pathlib import Path
NUM = (0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 3, 3, 1, 6, 2, 3, 6, 1, 6, 3, 2, 7, 3, 4, 8, 1, 21, 9, 6, 4, 10, 14, 5, 11, 2, 9, 12, 13, 14, 3, 7, 15, 17, 14, 5, 6, 13, 15, 17, 10, 11, 13, 16, 18, 22, 28, 36, 46, 63, 96, 152, 246, 528, 1971, 1)
DEN = (1, 2057, 539, 289, 136, 93, 68, 51, 39, 31, 27, 21, 17, 15, 13, 11, 10, 9, 8, 7, 13, 6, 11, 5, 14, 13, 4, 23, 7, 10, 19, 3, 17, 8, 5, 17, 7, 9, 17, 2, 41, 17, 11, 7, 17, 23, 8, 17, 3, 13, 17, 18, 19, 4, 9, 19, 21, 17, 6, 7, 15, 17, 19, 11, 12, 14, 17, 19, 23, 29, 37, 47, 64, 97, 153, 247, 529, 1972, 1)
I=(5,50,55,56)
U=tuple(F(a,b) for a,b in zip(NUM,DEN))
J=tuple(j for j in range(79) if j not in I)
Q=2**128
H=2**166
A=F(6912*50000**2,17**2)
Z=F(141421356237309504880,10**20)

def G(u): return (A/H)/(((2-u*u)*(3-u*u))**3)

def mass_individual(j):
    u=U[j]; b=Q*G(u)
    for r,v in enumerate(U):
        if r!=j: b *= (Z-v)/abs(u-v)
    return b

def mass_factored(j, common_product):
    u=U[j]
    return (Q*G(u))*(common_product/(Z-u))/prod(abs(u-v) for r,v in enumerate(U) if r!=j)

def main(use_c314=False):
    assert len(U)==79 and all(U[j]<U[j+1] for j in range(78))
    common=prod(Z-u for u in U)
    masses={}; eps={}; rounded={}
    for j in J:
        a=mass_individual(j); b=mass_factored(j,common)
        assert a==b and a>0
        w=a.numerator//a.denominator
        assert 0<w<a
        e=1-F(w)/a
        assert F(1,2**130)<e<F(1,2**118)
        if abs(I[0]-j)%2==0:
            kappa=(2-e)/e
            assert 2**119-1 < kappa < 2**131-1
        masses[j]=a;rounded[j]=w;eps[j]=e
    counter={'near':0,'reinforcing':0,'constant_gaps':0}
    by_moving={str(k):{'near':0,'reinforcing':0,'constant_gaps':0} for k in range(4)}
    if use_c314:
        base=Path(__file__).resolve().parent/'EM_C301_EXACT_PORTABLE'
        if not base.is_dir(): raise FileNotFoundError('Place EM_C301_EXACT_PORTABLE/ from C314 ZIP beside this script')
        sys.path.insert(0,str(base))
        here=os.getcwd()
        try:
            os.chdir(base)
            import C275_STANDALONE_EXACT_REPLAY as src
            import C288_ISOLATING_BOXES_EXACT as pathmod
            W0,B0=src.floor_fixed_masses()
            assert all(W0[j]==rounded[j] and B0[j]==masses[j] for j in J)
            paths,_=pathmod.build_paths()
        finally: os.chdir(here)
        assert len(paths)==125
        assert [(i,[k for k,d in enumerate(p['d']) if not d]) for i,p in enumerate(paths) if 0 in p['d']]==[(28,[1])]
        slopes=[tuple(p['d']) for p in paths]
        coverage='125_FROZEN_C284_C293_SLOPES_VERIFIED'
    else:
        slopes=[(1,1,1,1)]*28+[(1,0,1,1)]+[(1,1,1,1)]*96
        coverage='125_FROZEN_PATH_SLOPE_PROFILE_FROM_C315_NOT_INDEPENDENTLY_LOADED'
    for slope in slopes:
        for k,i in enumerate(I):
            for j in J:
                if not slope[k]: cat='constant_gaps'
                else: cat='near' if abs(i-j)%2==0 else 'reinforcing'
                counter[cat]+=1;by_moving[str(k)][cat]+=1
    assert counter=={'near':18712,'reinforcing':18713,'constant_gaps':75}
    assert sum(counter.values())==125*300
    lo=min(eps,key=eps.get);hi=max(eps,key=eps.get)
    assert (lo,hi)==(68,0)
    v1={75:F(1),77:F(-1)};v2={76:F(1),78:F(-1)}
    assert sum(v1.values())==sum(v2.values())==0
    def observe(v):return (v.get(75,0)-v.get(77,0),v.get(76,0)-v.get(78,0))
    assert observe(v1)==(2,0) and observe(v2)==(0,2)
    out={'schema':'C316_FLOOR_DEFECT_PARITY_AUDIT_V1',
      'coverage':coverage,
      'source_model':'C275_79_POSITIVE_RATIONAL_AUXILIARY',
      'fixed_nonintegral_masses':len(J),
      'floor_defect_exact_bound':'2^-130 < epsilon_j < 2^-118 (every fixed label)',
      'near_pole_condition_number_bound':'2^119-1 < kappa_j < 2^131-1',
      'smallest_epsilon_label':lo,'largest_epsilon_label':hi,
      'count':counter,'by_moving_index':by_moving,
      'local_residue_kernel_rank':2,
      'gcd_native_claim':False,'source_mathematical_admission':False}
    print(json.dumps(out,indent=2,sort_keys=True))
    return out

if __name__=='__main__':main('--with-c314' in sys.argv)
