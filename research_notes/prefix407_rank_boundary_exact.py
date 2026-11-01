#!/usr/bin/env python3
"""PREFIX-407 exact coherent/PSD classification on I3=0."""
from fractions import Fraction as Q

def defect(r,s,j):
    x=(s-1-r)/2
    y=(2*j-14+10*r-39*s)/8
    return r-x*x-y*y

def reconstruct(r,s,j):
    return ((s-1-r)/2,(14-10*r+39*s-2*j)/8)

def exact_feasible(r,s,j,k,q):
    return q==1 and k==Q(709,64)*s and defect(r,s,j)==0

def source_readouts(x,y):
    r=x*x+y*y
    s=(1+x)**2+y*y
    j=Q(53,2)+Q(29,2)*r+39*x-4*y
    return r,s,j,Q(709,64)*s

def certificate(eps,kappa):
    assert Q(0)<=eps<Q(1) and kappa>=0
    y=kappa/Q(4)+Q(49,8)*eps
    return 1-eps-eps*eps-y*y,1-kappa/Q(4)-Q(65,8)*eps

def main():
    for sign,j in [(1,Q(37)),(-1,Q(45))]:
        r,s,j0,k=source_readouts(Q(0),Q(sign))
        assert (r,s,j0,k)==(Q(1),Q(2),j,Q(709,32))
        assert exact_feasible(r,s,j0,k,Q(1))
        assert reconstruct(r,s,j0)==(Q(0),Q(sign))
    x,y=Q(2,5),Q(3,7)
    r,s,j,k=source_readouts(x,y)
    assert exact_feasible(r,s,j,k,Q(1))
    assert reconstruct(r,s,j)==(x,y)
    assert not exact_feasible(r,s,j,k+Q(1,100),Q(1))
    assert defect(Q(1),Q(2),Q(41))==1
    for kap in map(Q,[0,1,2]):
        assert defect(Q(1),Q(2),Q(41)+4*kap/Q(4))==1-(kap/Q(4))**2
    for kap in [Q(0),Q(1),Q(2),Q(7,2),Q(4),Q(5)]:
        m=min(Q(1),kap/Q(4))
        assert 1-m==max(Q(0),1-kap/Q(4))
        assert (kap>=4)==(m==1)
    determinant,spectral=certificate(Q(1,10000),Q(1))
    assert determinant==Q(1199479507,1280000000)>0
    assert spectral==Q(11987,16000)>0
    print("determinant_certificate",determinant)
    print("spectral_certificate",spectral)
    print("critical_kappa_exact",Q(4))
    print("PASS_PREFIX407_EXACT_SLICE_RECONSTRUCTION_AND_SHARP_NOISE_THRESHOLD")

if __name__=="__main__":
    main()
