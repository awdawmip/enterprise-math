#!/usr/bin/env python3
"""Independent 79-positive-branch exact expansion for 250 C293 endpoints.
Direct dual second derivative checks at 16 midpoints are diagnostics,
NOT a substitute for C290/C292 continuous full-4D interval certificates.
"""
from fractions import Fraction as R
import C275_STANDALONE_EXACT_REPLAY as s
import C288_ISOLATING_BOXES_EXACT as c288
import C291_INDEPENDENT_SECOND_JET as jet
from C293_AUTHOR_VERIFY_EXACT import load_certificate, at, D_FINE, R_NEWTON

def independent_F(v,W):
    f=R(0)
    for j in s.J:
        t=R(W[j]);node=s.U[j]
        for k,p in enumerate(v):
            t*=(s.Z-p)*abs(node-s.U[s.I[k]])
            t/=(s.Z-s.U[s.I[k]])*abs(node-p)
        f+=t
    for i,p in enumerate(v):
        t=R(s.Q)*s.A/s.H/((2-p*p)*(3-p*p))**3
        for j in s.J:t*=(s.Z-s.U[j])/abs(p-s.U[j])
        for k,q in enumerate(v):
            if i!=k:t*=(s.Z-q)/abs(p-q)
        f+=t
    return f

def run():
    records,_=load_certificate();paths,_=c288.build_paths();W,_=s.floor_fixed_masses()
    assert len(paths)==len(records)==125
    n=njet=0
    for i,((idx,k),p) in enumerate(zip(records,paths)):
        assert idx==i
        lo=R(k,D_FINE);hi=R(k+1,D_FINE)
        for t in (lo,hi):
            v=at(p,t);z=independent_F(v,W)
            assert z==s.original_F(v,W),(i,'product mismatch')
            assert (z<s.Q if t==lo else z>s.Q)
            n+=1
        if i%8==0:
            vm=at(p,(lo+hi)/2);zj=jet.direct_jet(vm,W)
            assert zj.v==independent_F(vm,W)
            assert zj.g[2]/s.Q>R(6,5)
            assert R(0)<zj.h[2][2]/s.Q<850
            assert abs((zj.v/s.Q-1)/(zj.g[2]/s.Q))<R_NEWTON
            njet+=1
    assert n==250 and njet==16
    print('C293_INDEPENDENT_POSITIVE_PRODUCT_PASS 250/250 exact endpoints, 16/16 normal jet centers')

if __name__=='__main__':run()
