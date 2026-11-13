#!/usr/bin/env python3
"""R119.2 exact close-time pair oracle for the six-phase S23 observer.
A local-only exact rational checker. Imports the already-verified R118 band lemma.
"""
from fractions import Fraction as F
from math import floor
import random, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "brc_s23_av_r118_two_band_s23_20261113"))
from check_r118 import eligible, cuts_phase, six_cuts, atoms, midpoint, exact_band_open, frac

rng=random.Random(1192026)
stat={'seed':1192026,'random_cases':0,'old_atoms':0,'relative_atoms':0,'joint_bit_calls':0,'joint_witnesses':0,'brute_new_atoms':0,'large_signed_cases':0,'max_witness_bitlength':0}

def relative_cuts(a,c,d):
    slopes={a,c,a-d,c-d}
    v=list(slopes)
    slopes.update(v[i]-v[j] for i in range(len(v)) for j in range(i+1,len(v)))
    out=set()
    for m in slopes:out.update(cuts_phase(m,F(0)))
    return out

def affine_arc_segments(theta,aa,cc,bit):
    """Fixed affine phase slopes aa,cc and optional complement bit.
    Returns [lower,upper) on fractional y in [0,1); coefficients pairs.
    """
    pa=aa*theta; pc=cc*theta
    va=(F(aa),F(-floor(pa)))
    vc=(F(cc),F(-floor(pc)))
    av=frac(pa);cv=frac(pc)
    if av==cv:
        return [] if bit else [((F(0),F(0)),(F(0),F(1)))]
    if bit==0:va,vc=vc,va;av,cv=cv,av
    if av<cv: return [(va,vc)]
    out=[(va,(F(0),F(1)))]
    if cv>0:out.append(((F(0),F(0)),vc))
    return out

def pair_oracle_open(lo,hi,t,d,j,x,a,c,bit0,bit1):
    mid=(lo+hi)/2
    seg0=affine_arc_segments(mid,a,c,bit0)
    seg1=affine_arc_segments(mid,a-d,c-d,bit1)
    y_slope=t-j
    for low0,up0 in seg0:
      for low1,up1 in seg1:
        # Fixed pairwise endpoint order throughout this pre-refined cell.
        low=max((low0,low1),key=lambda p:p[0]*mid+p[1])
        up=min((up0,up1),key=lambda p:p[0]*mid+p[1])
        if low[0]*mid+low[1]>=up[0]*mid+up[1]:continue
        w=exact_band_open(lo,hi,y_slope-up[0],x-up[1],y_slope-low[0],x-low[1])
        if w is not None:
            assert eligible(w,t,j,x,a,c)==bool(bit0)
            assert eligible(w,t+d,j,x,a,c)==bool(bit1)
            stat['joint_witnesses']+=1
            stat['max_witness_bitlength']=max(stat['max_witness_bitlength'],w.numerator.bit_length(),w.denominator.bit_length())
            return w
    return None

def pair_oracle(atom,t,d,j,x,a,c,bit0,bit1):
    stat['joint_bit_calls']+=1
    lo,hi,point=atom
    if point:
        if eligible(lo,t,j,x,a,c)==bool(bit0) and eligible(lo,t+d,j,x,a,c)==bool(bit1):return lo
        return None
    return pair_oracle_open(lo,hi,t,d,j,x,a,c,bit0,bit1)

def run_case(j,x,a,c,old_times,t,d,huge=False):
    old_cuts=set()
    for s in old_times:old_cuts|=six_cuts(s,j,x,a,c)
    old_atoms=atoms(old_cuts)
    stat['old_atoms']+=len(old_atoms)
    rel=old_cuts|relative_cuts(a,c,d)
    refined=atoms(rel)
    stat['relative_atoms']+=len(refined)
    signatures=set()
    for atom in refined:
        sig=tuple(eligible(midpoint(atom),s,j,x,a,c) for s in old_times)
        for b0 in (0,1):
          for b1 in (0,1):
            w=pair_oracle(atom,t,d,j,x,a,c,b0,b1)
            if w is not None:
                assert tuple(eligible(w,s,j,x,a,c) for s in old_times)==sig
                signatures.add((sig,b0,b1))
    if not huge:
        brute_cuts=old_cuts|six_cuts(t,j,x,a,c)|six_cuts(t+d,j,x,a,c)
        brute=atoms(brute_cuts)
        stat['brute_new_atoms']+=len(brute)
        direct={(tuple(eligible(midpoint(atom),s,j,x,a,c) for s in old_times),int(eligible(midpoint(atom),t,j,x,a,c)),int(eligible(midpoint(atom),t+d,j,x,a,c))) for atom in brute}
        assert direct==signatures, (j,x,a,c,old_times,t,d,direct,signatures)
    assert signatures
    return len(old_atoms),len(refined),len(signatures)

def main():
    for _ in range(250):
        j=rng.randint(-2,2);a=rng.randint(-3,3);c=rng.randint(-3,3)
        x=F(rng.randint(-8,8),rng.randint(1,7))
        old_times=tuple(sorted(rng.sample(list(range(-4,5)),rng.randint(1,3))))
        t=rng.randint(-8,8); d=rng.choice([-3,-2,-1,1,2,3])
        run_case(j,x,a,c,old_times,t,d)
        stat['random_cases']+=1
    for t in (10**80+7,-(10**80+7),10**150+19,-(10**150+19)):
        run_case(0,F(1,2),-2,3,(-3,-1,0,2,4),t,1,huge=True)
        stat['large_signed_cases']+=1
    stat['status']='R119_NEIGHBOR_PASS'
    with open(Path(__file__).with_name('verification_r119_neighbor.json'),'w') as f:json.dump(stat,f,indent=2,sort_keys=True)
    print(stat)
if __name__=='__main__':main()
