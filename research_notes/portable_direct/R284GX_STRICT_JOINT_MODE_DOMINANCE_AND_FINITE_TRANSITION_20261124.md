# R284GX — Strict joint mode-count dominance and finite transition scan

2026-11-24. Independent auxiliary fixed four-phase binary-tag model research, author proof, NOT_REVIEWED. No native physical attribution or P000 change. Continuation of frozen GV at cc7c920e534ed7898177b272d834564bf03b3721:research_notes/portable_direct/R284GV_TWO_CUT_COUNT_AND_FIXED_DIAGONAL_GAP_20261124.md (blob e3b1e1787b5fa5fb53a3f9078cc10affde20ce86); its GS/GL pins remain unchanged. Prior activity RA-B82240E8488EF5A1DA5186C4 read at main (blob 77a212e3bc4dd1fa6a7558ff09b6daf17621ab97), historical researcher EM-DIRECT-0C386E. Current gateway identity check returned BACKEND_IDENTITY_CHECK_UNAVAILABLE, operation_sent=false; no live owner/identity verification, no shared CLAIM, no protected state update. Independent new nonoverwriting note under docs/RESEARCH_CONSOLE_FALLBACK.md. Current canonical entry files and P000/ACTIVE worldview read via GitHub.

## Theorem (all low-omission parameters)

For integers u>=1, 0<=q<u, put d=u-q>=1, H=2q+u+1, J=q+3u, m=q+u. Let S=N(H,J,H), P=N(H-1,J+1,H), Q=N(H,J+1,H-1) be the GV safe single-edge mode-word counts. Then

**S > P+Q.**

This strengthens the prior separate inequalities; the P<S side was previously open. It implies PQ/S^2<1/4 and the asymmetric-to-symmetric full-cycle mode-word count ratio (PQ/S^2)^2<1/16. These are unlabelled mode counts; physical-coordinate factorials are separate.

## Proof by exact positive residual recombination

Write C(n,k)=0 if n<0 or k outside [0,n]. Define l_a=C(a+u-1,a)-C(a+u-1,a-1), 0<=a<u, and r_b=C(b+m-1,b)-C(b+m-1,b-1), 0<=b<m. Extend by zero. Both positive on their ranges. By the hockey-stick identity U_i=sum_{a<=i} l_a=C(i+u,i)-C(i+u,i-1) for 0<=i<=u (the term l_u is zero); V_j=sum_{b<=j} r_b=C(j+m,j)-C(j+m,j-1) for 0<=j<=m. The analogous t=1 reflections in GV collapse via Pascal to U_i and V_j. In S the left kernel is exactly U_i+q l_{i-1} (for q=0 the second term vanishes); right kernel V_j. Q uses U_i,V_j. P uses l_a,r_b. The middle B inventories are d,d-1,d+1 respectively for S,Q,P, and A inventories H,H,H-1. Therefore

S-Q = sum_{i=0..u,j=0..m} U_i V_j C(H-i-j+d-1,d)
      + q sum_{i=0..u,j=0..m} l_{i-1} V_j C(H-i-j+d,d),

where the Pascal difference is interpreted as zero for negative remaining A inventory (and also at remaining A=0). All terms are nonnegative.

Expand the cumulative kernels in the first sum. For each original pair (a,b) let h=H-1-a-b, I=u-a>=1, B0=m-b>=1. Then I+B0=h+d. The first sum's coefficient of l_a r_b is

sum_{alpha=0..I,beta=0..B0} C(h+d-alpha-beta,d).

If h<0 both this coefficient and the corresponding P coefficient vanish. If h>=0, every integer k=0..h is realizable as alpha+beta since I+B0=h+d>=h. All contributions are nonnegative. Consequently the coefficient is at least sum_{k=0..h} C(h+d-k,d)=C(h+d+1,d+1), precisely the corresponding P coefficient. For a=b=0, h=2q+u>=1 and I,B0>=1, the k=1 coefficient is counted at least twice, both terms positive. Also l_0 r_0=1. Thus S-Q>P, strictly, for all parameters including q=0 and d=1.

More precisely, define M_k(a,b)=max(0,min(I,k)-max(0,k-B0)+1). The exact gap S-P-Q equals

sum_{a,b:h>=0} l_a r_b [sum_{k=0..h}(M_k-1) C(h+d-k,d)
                         + q sum_{beta=0..min(B0,h)} C(h-beta+d,d)].

The second sum is the q l_{i-1} contribution. This is a positive expansion retaining both residual port caps. The proof uses the GV exact counting observer only: positive multiplicity recombination, not an independent-port approximation. It does not identify the path sets by erasing their distinct histories.

## Finite exact transition evidence

Using the locally recovered GW arbitrary-precision packed convolution implementation (source reproduced below), ran all u=1..64 and all q=0..u-1. 2080 parameter pairs satisfy S>P+Q; all 2016 adjacent q comparisons have K(q+1,u)<K(q,u), where K=PQ(J+1)^2/(S^2 H) uses exact fractions. No K=1 ties. Each row has one initial interval of asymmetric wins. Largest q with K>1 for u=1,2,4,8,16,32,64 respectively: 0,0,2,5,9,16,27. All-row cut list:
0,0,1,2,3,3,4,5,5,6,6,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,14,15,15,16,16,16,17,17,18,18,18,19,19,20,20,20,21,21,21,22,22,22,23,23,23,24,24,25,25,25,25,26,26,26,27,27,27.
This is a finite experiment, not a global monotonicity proof.

## Recovered prior GW computation and replay

Previous turn's file /mnt/data/r284gw/check.py existed locally and was used in the executed scan. The prior report claimed a growing near-diagonal gap theorem, uP/S->1, uQ/S->2, uK->32/3 for d->infinity,d=o(u). Its full proof was not durably published according to the preceding report. Preserve the reported target and actual code here; this note does not certify the absent GW uniform concentration proof. Reconstruct it from the positive convolution if needed. The present theorem is independent of that claim.

```python
from math import comb,isqrt
from fractions import Fraction

def C(n,k): return comb(n,k) if 0<=k<=n else 0

def counts(q,u,A,B,D):
    s=2*u+1-(D-2*q);t=A-2*q-s;m=q+s;g=B-2*m
    L=[sum(C(q+k-1,k)*(C(i-k+s-1,i-k)-C(i-k+s-1,i-t-1)) for k in range(min(i,t)+1)) if q else C(i+s-1,i)-C(i+s-1,i-t-1) for i in range(s+t)]
    R=[C(j+m-1,j)-C(j+m-1,j-t-1) for j in range(m+t)]
    L.reverse();R.reverse();width=(max(L).bit_length()+max(R).bit_length()+min(len(L),len(R)).bit_length()+7)//8
    packed=lambda seq:int.from_bytes(b''.join(v.to_bytes(width,'little') for v in seq),'little')
    raw=(packed(L)*packed(R)).to_bytes(width*(len(L)+len(R)-1),'little')
    off=A-(s+t-1)-(m+t-1)
    return sum(int.from_bytes(raw[z*width:(z+1)*width],'little')*C(z+off+g,g) for z in range(len(L)+len(R)-1) if z+off>=0)

def dp(q,u,A,B,D):
    r=2*u+1;M=max(0,D-q);p=lambda x:max(0,x);v=[0]*(B+1)
    for a in range(A+1):
        for b in range(B+1):
            D2=p(A-a-2*q)+p(p(b-q)+M-q)
            D3=max(0,D-2*q,p(a-q)-q,B-b+p(a-q)-2*q+M)
            v[b]=0 if min(D2,D3)<r else 1 if a==b==0 else v[b]+(v[b-1] if b else 0)
    return v[B]

def configs(q,u):
    H=2*q+u+1;J=q+3*u
    return [(H,J,H),(H-1,J+1,H),(H,J+1,H-1)]

if __name__=='__main__':
    n=0; comparisons=0; ties=0; cuts=[]
    for u in range(1,65):
        prev=None; cut=-1
        for q in range(u):
            H=2*q+u+1;J=q+3*u
            S,P,Q=[counts(q,u,*c) for c in configs(q,u)]
            assert S>P+Q,(u,q,S,P,Q)
            k=Fraction(P*Q*(J+1)**2,S*S*H)
            if prev is not None:
                assert k<prev,(u,q)
                comparisons+=1
            if k>1:cut=q
            if k==1:ties+=1
            prev=k;n+=1
        cuts.append(cut)
    print('S>P+Q:',n,'strict K decreases:',comparisons,'ties:',ties,'cuts',cuts)
```

Next: prove monotonicity of K in q or find a counterexample using ratios of positive port coefficients; reconstruct GW uniform concentration proof and preserve its exact range. No formal Result/Review or shared progress claimed.
