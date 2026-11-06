#!/usr/bin/env python3
"""Exact independent finite certificate for PREFIX-543.
Frozen four-STAR candidate pin f42f2906d77f24085c123f3ccfe9667d41caa96d.
Integer phase recurrence and native INNER/OUTER branch DP; no external dependencies.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from math import comb
import json
import sys

S=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):return tuple((-1 if c>0 else 1)*x for x in S[a] if x!=abs(c))
P=tuple((a,p,e*x) for a in range(4) for x in S[a] for e in (-1,1) for p in near(a,e*x))
I={v:i for i,v in enumerate(P)}
def successors(i):
    a,p,c=P[i]
    b=next(b for b in range(4) if b!=a and abs(c) in S[b])
    return tuple(I[v] for v in [(a,c,k) for k in near(a,c) if k!=p]+[(b,c,k) for k in near(b,c)])
NX=tuple(successors(i) for i in range(48)); T=I[(0,1,-3)]
def sig(i):return (1 if P[i][2]>0 else -1) if abs(P[i][2])==1 else 0
def ep(i):return abs(sig(i))
def tau(r,i,j):
    x=ep(i)+ep(j)-abs(sig(j)-r)+abs(sig(i)-r)
    assert x%2==0 and x//2 in (0,1)
    return x//2
assert len(P)==len(I)==48 and T not in NX[T] and all(len(set(row))==3 for row in NX)
assert sum(len(n) for n in NX)==144

# Three shared seed arrays. U[n][i] tracks (p,k) for n steps from phase i,
# with every arrival to T counted as potential; the first root transition is handled separately.
def phase_hists(D):
    result=[None]*48
    for r in (-1,0,1):
        U=[{(0,0):1} for _ in P]
        for d in range(D+1):
            if d:
                for i in range(48):
                    if sig(i)!=r:continue
                    row=defaultdict(int)
                    for j in NX[i]:
                        for (p,k),v in U[j].items():
                            row[p+tau(r,i,j),k,int(j==T)]+=v
                    assert sum(row.values())==3**d
                    if result[i] is None:result[i]=[None]*(D+1)
                    result[i][d]=dict(row)
            else:
                for i in range(48):
                    if sig(i)==r:
                        result[i]=[None]*(D+1);result[i][0]={(0,0,0):1}
            if d==0 or d==D:continue
            W=[]
            for i in range(48):
                row=defaultdict(int)
                for j in NX[i]:
                    for (p,k),v in U[j].items():
                        row[p+tau(r,i,j),k+int(j==T)]+=v
                W.append(dict(row))
            U=W
    return result

def labeled_poly(phase,d,b0):
    hist=defaultdict(int)
    for (p,k,e),n in phase.items():
        assert e in (0,1) and n>0
        if b0:
            assert d-2*k-e>=0
            base=n*2**(d-2*k-e)
            for h in range(k+1):
                a=base*comb(k,h)*3**(k-h)
                hist[p,h]+=a
                if e:hist[p,h+1]+=a
        else:
            assert d-2*k>=0
            base=n*2**(d-2*k)
            for h in range(k+1):hist[p,h]+=base*comb(k,h)*3**(k-h)
    return dict(hist)

def raw(root,D,b0):
    states={(root,b0,0,0):1};res=[];r=sig(root)
    for d in range(D+1):
        hist=defaultdict(int)
        for (i,b,K,h),v in states.items():
            delta=abs(sig(i)-r)
            assert K>=delta and (K-delta)%2==0
            hist[(K-delta)//2,h]+=v
        assert sum(hist.values())==6**d
        res.append(dict(hist))
        if d==D:break
        W=defaultdict(int)
        for (i,b,K,h),v in states.items():
            for j in NX[i]:
                for bit in (0,1):
                    W[j,bit,K+ep(i)+ep(j),h+int(b and bit and j==T)]+=v
        states=W
    return res

def theoretical_moments(phase,p,b0):
    sub=[(k,e,n) for (pp,k,e),n in phase.items() if pp==p]
    N=sum(n for k,e,n in sub)
    ek=Fraction(sum(k*n for k,e,n in sub),N)
    ee=Fraction(sum(e*n for k,e,n in sub),N)
    ek2=Fraction(sum(k*k*n for k,e,n in sub),N)
    ekfall2=Fraction(sum(k*(k-1)*n for k,e,n in sub),N)
    eke=Fraction(sum(k*e*n for k,e,n in sub),N)
    vk=ek2-ek*ek
    ve=ee-ee*ee
    cke=eke-ek*ee
    mu=ek/4+(ee/2 if b0 else 0)
    fac2=ekfall2/16+(eke/4 if b0 else 0)
    var=Fraction(3,16)*ek+vk/16
    if b0:var+=ee/4+ve/4+cke/4
    return mu,fac2,var,ek,ee,vk,cke

def raw_moments(hist,p):
    sub=[(h,n) for (pp,h),n in hist.items() if pp==p]
    N=sum(n for h,n in sub)
    mu=Fraction(sum(h*n for h,n in sub),N)
    fac2=Fraction(sum(h*(h-1)*n for h,n in sub),N)
    var=fac2+mu-mu*mu
    return mu,fac2,var

def fracstr(x):return str(x.numerator) if x.denominator==1 else str(x.numerator)+"/"+str(x.denominator)

if __name__=='__main__':
    D=int(sys.argv[1]) if len(sys.argv)>1 else 16
    phase=phase_hists(D)
    preds=tuple(i for i in range(48) if T in NX[i])
    assert len(preds)==3, preds
    assert {P[i] for i in preds}=={(0,-6,1),(1,-4,1),(1,-5,1)}
    assert all(sig(i)==1 and tau(1,i,T)==0 for i in preds)
    full_signatures={0:[],1:[]}
    checked=0;moment_fibers=0;changed=0
    demos={}
    for i in range(48):
        raw0=raw(i,D,0);raw1=raw(i,D,1)
        for d in range(D+1):
            H=phase[i][d]
            A=labeled_poly(H,d,0)
            B=labeled_poly(H,d,1)
            assert A==raw0[d] and B==raw1[d],(i,d)
            checked+=2
            if A!=B:
                changed+=1
                assert i in preds
            else:
                assert i not in preds or d==0 or all(e==0 for (p,k,e) in H)
            for p in set(key[0] for key in H):
                for b0,hist in [(0,A),(1,B)]:
                    assert theoretical_moments(H,p,b0)[:3]==raw_moments(hist,p)
                    moment_fibers+=1
            if i==preds[0] and d in (1,4,8,12,D):
                hh0={str(k):v for k,v in sorted(A.items())}
                hh1={str(k):v for k,v in sorted(B.items())}
                demos[f'd{d}']={'b0_0':hh0,'b0_1':hh1}
        for b0 in (0,1):
            # use previously computed arrays rather than recalculating
            rr=raw0 if b0==0 else raw1
            full_signatures[b0].append(tuple(tuple(sorted(rr[d].items())) for d in range(D+1)))
    for b0 in (0,1):
        assert len(full_signatures[b0])==48
    # The known PREFIX-533 26 all-length b0 classes are recovered by depth 5.
    # For each root, the boundary correction is zero except for three target predecessors;
    # those three have identical (r,tau) and lie in exactly two b0 classes.
    finite5=phase_hists(5)
    classes=[]
    for b0 in (0,1):
        fingerprints={}
        for i in range(48):
            fp=tuple(tuple(sorted(labeled_poly(finite5[i][d],d,b0).items())) for d in range(6))
            fingerprints.setdefault(fp,[]).append(i)
        assert len(fingerprints)==26
        classes.append({tuple(sorted(z)) for z in fingerprints.values()})
    assert classes[0]==classes[1]
    assert any(set(cl)==set((preds[0],preds[2])) for cl in classes[0])
    assert any(tuple(cl)==(preds[1],) for cl in classes[0])
    # Exact global moment identities under uniform phase and branch label choices.
    # For arbitrary d, p, bit the generating identity is derived in the accompanying note.
    output={
        'status':'ALL_CHECKS_PASS','max_depth':D,'phases':48,'directed_edges':144,
        'gate_target':P[T], 'target_predecessors':[P[i] for i in preds],
        'root_depth_bit_histogram_equalities':checked,
        'conditional_moment_equalities':moment_fibers,
        'histogram_pairs_changed_by_initial_bit':changed,
        'root_signature_classes_upto_depth':{str(b):len(set(full_signatures[b])) for b in (0,1)},
        'depth5_root_class_partitions_identical':classes[0]==classes[1],
        'demos':demos,
        'method':'phase_only_3seed_plus_boundary_bit_exact_integer_vs_raw_branch_DP; rational_moments'
    }
    print(json.dumps(output,indent=2,ensure_ascii=False,sort_keys=True))
