#!/usr/bin/env python3
"""Exact finite checks for PREFIX-823 combined Q-only future-observer theorem.
No external packages; all arithmetic is in integers or the prime field F_1000000007.
The report is a finite regression, not the general proof.
"""
import json
from collections import defaultdict
from itertools import combinations
from fractions import Fraction
P=1_000_000_007

def model(q,a,b):
    labels=[(z,k,h) for z in (0,1) for k in range(q+1-z) for h in range(k+1)]
    idx={t:i for i,t in enumerate(labels)}
    # Q columns as target row/coeff pairs
    columns=[]
    for z,k,h in labels:
        terms=[]
        if h: terms.append((idx[(z,k-1,h-1)],h))
        if z: terms.append((idx[(0,k,h)],b))
        elif k<q: terms.append((idx[(1,k,h)],a))
        columns.append([(i,c) for i,c in terms if c])
    C=[[0]*len(labels) for _ in range(q+1)]
    for i,(z,k,h) in enumerate(labels):
        if h==0:C[k+z][i]=1
    return labels,columns,C

def q_next(M,cols):
    n=len(cols); out=[]
    for row in M:
        z=[0]*n
        for col,terms in enumerate(cols):
            z[col]=sum(row[i]*c for i,c in terms)%P
        out.append(z)
    return out

def modular_rank(rows,n):
    piv={}
    for row in rows:
        a=[v%P for v in row]
        for j,p in sorted(piv.items()):
            if a[j]:
                t=a[j]
                for k in range(j,n):a[k]=(a[k]-t*p[k])%P
        j=next((i for i,x in enumerate(a) if x),None)
        if j is not None:
            inverse=pow(a[j],P-2,P)
            piv[j]=[(x*inverse)%P for x in a]
    return len(piv)

def q_rank(q,a,b):
    labels,cols,C=model(q,a,b)
    # General Cayley-Hamilton bound is N; for the b>0 theorem 2q+1 powers suffice.
    rows=[];M=C; ranks={}
    for t in range((2*q+1) if b else (q+3)):
        rows.extend(M)
        if t in (q+1,2*q):ranks[str(t)]=modular_rank(rows,len(labels))
        M=q_next(M,cols)
    return modular_rank(rows,len(labels)),len(labels),ranks

def fraction_rank(rows,n):
    piv={}
    for row in rows:
        r=[Fraction(x) for x in row]
        for j,pr in sorted(piv.items()):
            if r[j]:
                v=r[j]
                for k in range(j,n):r[k]-=v*pr[k]
        j=next((i for i,x in enumerate(r) if x),None)
        if j is not None:
            v=r[j];piv[j]=[x/v for x in r]
    return len(piv)

def rational_check(q,a,b):
    labels,cols,C=model(q,a,b); N=len(labels)
    M=C; rows=[]
    for t in range((2*q+1) if b else (q+2)):
        rows.extend(M)
        # exact integer C Q^t (no modulus)
        nextM=[]
        for row in M:
            z=[sum(row[i]*w for i,w in terms) for terms in cols]
            nextM.append(z)
        M=nextM
    return fraction_rank(rows,N)

def named_regression(q,a,b):
    # m=q+1 unmarked sources with distinct positive weights. Marked source index 0.
    other=list(range(1,q+2)); beta={0:b,**{i:i for i in other}}
    states=[frozenset(c) for k in range(q+1) for c in combinations(range(q+2),k)]
    labels,cols,C=model(q,a,b); idx={p:i for i,p in enumerate(labels)}
    assertions=0
    for S in states:
        # Direct named evolution and moment-coordinate evolution for Q^t.
        D={S:1};V=[0]*len(labels)
        z=1 if 0 in S else 0; U=S-{0}
        for h in range(len(U)+1):
            e=0
            for sel in combinations(U,h):
                prod=1
                for i in sel:prod*=beta[i]
                e+=prod
            V[idx[(z,len(U),h)]]=e
        for t in range(2*q+1):
            obs=[0]*(q+1)
            for state,mass in D.items():obs[len(state)]+=mass
            cv=[sum(C[l][i]*V[i] for i in range(len(labels))) for l in range(q+1)]
            assert obs==cv,(q,a,b,S,t,obs,cv)
            assertions+=1
            DD=defaultdict(int)
            for state,mass in D.items():
                for i in state:
                    if beta[i]:DD[state-{i}]+=mass*beta[i]
                if 0 not in state and len(state)<q:
                    DD[state|{0}]+=mass*a
            D=DD
            VV=[0]*len(labels)
            for col,terms in enumerate(cols):
                for row,c in terms:VV[row]+=V[col]*c
            V=VV
    return len(states),assertions

def main():
    positive=[];singular=[]
    for q in range(1,11):
        for a in (1,2):
            for b in (1,3):
                rank,N,horiz=q_rank(q,a,b)
                target=N-(q+1)//2
                assert rank==target,(q,a,b,rank,target)
                assert horiz[str(2*q)]==target
                positive.append(dict(q=q,a=a,b=b,dim=N,observed_rank=rank,target=target,horizon_2q=horiz[str(2*q)]))
        for a in (1,2):
            rank,N,horiz=q_rank(q,a,0)
            conjectured=(q+1)*(q+2)//2+2*(q-1)
            assert rank==conjectured,(q,a,rank,conjectured)
            singular.append(dict(q=q,a=a,b=0,dim=N,observed_rank=rank,observed_pattern=conjectured))
    rational=[]
    for q in range(1,6):
        for b in (0,1,3):
            rank=rational_check(q,1,b)
            target=(q+1)*(q+2)//2+2*(q-1) if b==0 else (q+1)**2-(q+1)//2
            assert rank==target,(q,b,rank,target)
            rational.append(dict(q=q,a=1,b=b,rational_rank=rank))
    named=[];total=0
    for q in range(1,5):
        for a,b in ((1,0),(1,1),(2,3)):
            states,count=named_regression(q,a,b)
            total+=count
            named.append(dict(q=q,a=a,b=b,named_states=states,exact_histogram_assertions=count))
    print(json.dumps({'status':'ALL_EXACT_ASSERTIONS_PASSED','prime':P,'positive_b_cases':len(positive),'b_zero_cases':len(singular),'rational_cases':len(rational),'named_cases':len(named),'named_histogram_assertions':total,'positive_b':positive,'b_zero':singular,'named':named,'rational':rational,'limits':'prime-field modular ranks for q<=10; unrestricted signed integer named-state histogram equality for q<=4; proof supplies both all-q characteristic-zero rank formulas; these tests cover finite instances'},indent=2,ensure_ascii=False))

if __name__=='__main__':main()
