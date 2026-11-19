#!/usr/bin/env python3
"""Independent NumPy reproduction: PREFIX-930 exact two-flip W and prior union.
Requires NumPy; all arithmetic integral. Run script verified_U.bin [sorted_W.bin].
"""
import sys
import numpy as np
N=1<<32
Q0,NQ=262145,131072
def main():
    if len(sys.argv) not in (2,3):
        raise SystemExit("usage: script verified_U.bin [sorted_W.bin]")
    A=np.arange(Q0,524288,2,dtype=np.int64)
    blocks=[];raw=0
    for j in range(19):
        Y=np.bitwise_xor(A,1<<j)
        for i in range(19):
            B=np.abs(Y-(1<<i))
            ok=(B>=Q0)&(B<=524287)&((B&1)==1)
            ids=((A[ok]-Q0)//2)*NQ+(B[ok]-Q0)//2
            if ids.size:
                assert np.all(((1<<i)%B[ok])==(Y[ok]%B[ok]))
                blocks.append(ids);raw+=int(ids.size)
    C=np.unique(np.concatenate(blocks))
    if len(sys.argv)==3:
        C.astype("<u8",copy=False).tofile(sys.argv[2])
    U=np.fromfile(sys.argv[1],dtype="<u8").astype(np.int64)
    assert U.size==5295478 and np.all(U[1:]>U[:-1])
    inS=np.zeros(NQ,dtype=bool);inD=np.zeros(NQ,dtype=bool)
    for pos,b in enumerate(A):
        r=1;early=False;late=False
        for d in range(1,53):
            r=(2*r)%int(b)
            if r==1 or r==b-1:
                if d<=31:early=True
                else:late=True
        inS[pos]=early;inD[pos]=(not early) and late
    assert inS.sum()==24 and inD.sum()==91
    inL=inD.copy()
    for v in (262145,321651,440667,440669,524273,524275,524277,524279,524281,524283,524285,440665,524287):
        inL[(v-Q0)//2]=True
    assert inL.sum()==104
    inT=np.zeros(NQ,dtype=bool)
    for t in range(1024):inT[(77081*t+12345)%NQ]=True
    assert inT.sum()==1024
    oBZS=0;oV=0
    for offset in range(0,C.size,1000000):
        ids=C[offset:offset+1000000];ai=ids//NQ;bi=ids%NQ
        a=Q0+2*ai;b=Q0+2*bi
        B=(b<33*((N+a-1)//a))|(a<33*((N+b-1)//b))
        Z=(a//np.gcd(a,b))*b<N
        prior=B|Z|inS[bi]
        oBZS+=int(np.count_nonzero(prior))
        V=inL[ai]|inL[bi]|((a>=500001)&inT[bi])|((b>=500001)&inT[ai])
        oV+=int(np.count_nonzero(V&~prior))
    uidx=np.searchsorted(C,U)
    hit=(uidx<C.size)&(C[np.minimum(uidx,C.size-1)]==U)
    oU=int(np.count_nonzero(hit))
    held=U[hit];ai=held//NQ;bi=held%NQ
    a=Q0+2*ai;b=Q0+2*bi
    uV=int(np.count_nonzero(inL[ai]|inL[bi]|((a>=500001)&inT[bi])|((b>=500001)&inT[ai])))
    oV-=uV
    new=C.size-oBZS-oU-oV
    print("raw_witness_parameters=",raw)
    print("unique_ordered_pair_certificates=",C.size)
    print("overlap_BZS=",oBZS)
    print("overlap_U_outside_BZS=",oU)
    print("overlap_V_outside_K=",oV)
    print("increment_over_PREFIX929=",new)
    print("new_certified_union=",7505960064+new)
    print("remaining_certificate_complement=",NQ*NQ-7505960064-new)
    assert (raw,C.size,oBZS,oU,oV,new)==(35782672,29360142,13072459,8689,61146,16217848)
if __name__=="__main__":main()
