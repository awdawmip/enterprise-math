#!/usr/bin/env python3
"""PREFIX-822 exact integral observer verifier. Python 3 standard library only.
Reproduces finite rank tests and direct named-state word tests; universal result
is proved separately in the companion manuscript.
"""
from collections import deque
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
import json

PRIME = 1_000_000_007

def matrices(q,a,b):
    indices=[(z,k,h) for z in (0,1) for k in range(q+1-z) for h in range(k+1)]
    loc={t:i for i,t in enumerate(indices)}
    n=len(loc)
    assert n==(q+1)**2
    R=[[0]*n for _ in range(n)]
    A=[[0]*n for _ in range(n)]
    for row,(z,k,h) in enumerate(indices):
        if (z,k+1,h+1) in loc:
            R[row][loc[z,k+1,h+1]]=h+1
        if z==0 and (1,k,h) in loc:
            R[row][loc[1,k,h]]=b
        if z==1:
            A[row][loc[0,k,h]]=a
    C=[[0]*n for _ in range(q+1)]
    for l in range(q+1):
        C[l][loc[0,l,0]]=1
        if l:C[l][loc[1,l-1,0]]=1
    Q=[[R[i][j]+A[i][j] for j in range(n)] for i in range(n)]
    return indices,R,A,Q,C

def apply(M,v):
    return [sum(x*y for x,y in zip(row,v)) for row in M]

def rowmul(v,M,p=None):
    out=[0]*len(v)
    for i,x in enumerate(v):
        if x:
            for j,y in enumerate(M[i]):
                if y:out[j]+=x*y
    return [x%p for x in out] if p else out

class RowSpace:
    def __init__(self,n):
        self.n=n
        self.piv={}
    def add(self,v):
        v=[int(x)%PRIME for x in v]
        for j,u in self.piv.items():
            if v[j]:
                c=v[j]
                v=[(v[k]-c*u[k])%PRIME for k in range(self.n)]
        for j,x in enumerate(v):
            if x:
                inv=pow(x,-1,PRIME)
                v=[t*inv%PRIME for t in v]
                self.piv[j]=v
                return v
        return None
    def rank(self):
        return len(self.piv)

def q_rank(Q,C):
    n=len(Q);space=RowSpace(n);rows=C
    for horizon in range(n):
        for row in rows:space.add(row)
        rows=[rowmul(row,Q,PRIME) for row in rows]
    return space.rank()

def word_rank(R,A,C):
    space=RowSpace(len(R));pending=deque()
    for row in C:
        v=space.add(row)
        if v is not None:pending.append(v)
    while pending:
        v=pending.popleft()
        for M in (R,A):
            w=space.add(rowmul(v,M,PRIME))
            if w is not None:pending.append(w)
    return space.rank()

def rank_of_rows(rows,n):
    space=RowSpace(n)
    for row in rows:space.add(row)
    return space.rank()

def rational_q_rank(Q,C):
    """Characteristic-zero full-horizon rank, for small q boundary witnesses."""
    n=len(Q);piv={};rows=C
    for horizon in range(n):
        for row in rows:
            v=[Fraction(x) for x in row]
            for j,u in piv.items():
                if v[j]:
                    c=v[j];v=[v[k]-c*u[k] for k in range(n)]
            for j,x in enumerate(v):
                if x:
                    piv[j]=[z/x for z in v]
                    break
        rows=[rowmul(row,Q) for row in rows]
    return len(piv)

def moments(pop,ix,beta):
    loc={key:i for i,key in enumerate(ix)}
    v=[0]*len(ix)
    for S,mass in pop.items():
        z=int(0 in S);weights=[beta[i] for i in S if i!=0]
        E=[1]+[0]*len(weights)
        for weight in weights:
            for h in range(len(weights),0,-1):
                E[h]+=weight*E[h-1]
        for h,val in enumerate(E):
            v[loc[z,len(weights),h]]+=mass*val
    return v

def native_step(pop,op,q,a,beta):
    out={}
    for S,mass in pop.items():
        if op=="R":
            for i in S:
                dest=tuple(x for x in S if x!=i)
                out[dest]=out.get(dest,0)+mass*beta[i]
        else:
            if 0 not in S and len(S)<q:
                dest=tuple(sorted((*S,0)))
                out[dest]=out.get(dest,0)+mass*a
    return {s:v for s,v in out.items() if v}

def projection(v,ix,q,b):
    x=ix.index((0,q,0));y=ix.index((0,q,1));z=ix.index((1,q-1,0))
    ans=v.copy();ans[x]+=ans[z];ans[y]+=b*ans[z]
    return ans[:z]+ans[z+1:]

def section(v,ix,q):
    z=ix.index((1,q-1,0))
    return v[:z]+[0]+v[z:]

def reduced_matrix(M,ix,q,b):
    N=len(ix)-1
    out=[[0]*N for _ in range(N)]
    for j in range(N):
        e=[0]*N;e[j]=1
        col=projection(apply(M,section(e,ix,q)),ix,q,b)
        for i,x in enumerate(col):out[i][j]=x
    assert all(x>=0 for row in out for x in row)
    return out

def exact_named_check(q):
    m=q+2;a=2;b=3;beta=[b]+list(range(1,m))
    ix,R,A,Q,C=matrices(q,a,b)
    RR=reduced_matrix(R,ix,q,b);AA=reduced_matrix(A,ix,q,b)
    states=[s for n in range(q+1) for s in combinations(range(m),n)]
    asserts=0
    for S in states:
        pop={S:1}
        full=moments(pop,ix,beta)
        for op,M in (("R",R),("A",A)):
            assert apply(M,full)==moments(native_step(pop,op,q,a,beta),ix,beta)
            asserts+=1
        assert apply(C,full)==[int(len(S)==i) for i in range(q+1)]
        asserts+=1
        for length in range(5):
            for word in product("RA",repeat=length):
                current=pop
                red=projection(full,ix,q,b)
                for op in word:
                    current=native_step(current,op,q,a,beta)
                    red=apply(RR if op=="R" else AA,red)
                assert red==projection(moments(current,ix,beta),ix,q,b),(q,S,word)
                asserts+=1
    return dict(q=q,named_states=len(states),exact_assertions=asserts)

def run():
    rows=[]
    for q in range(1,11):
        for a,b in product((1,2),(0,1,3)):
            ix,R,A,Q,C=matrices(q,a,b)
            n=len(ix)
            qr=q_rank(Q,C);wr=word_rank(R,A,C)
            assert wr==n-1,("word rank",q,a,b,wr)
            # Modular combined-rank pattern is a finite observation.
            expected_q=(n-(q+1)//2) if b>0 else (q+1)*(q+2)//2+2*(q-1)
            assert qr==expected_q,("Q rank",q,a,b,qr,expected_q)
            cqkernel=(q+1)//2 if b>0 else (q-1 if q>=2 else 1)
            assert n-rank_of_rows(C+Q,n)==cqkernel
            assert n-rank_of_rows(C+R+A,n)==1
            rows.append(dict(q=q,a=a,b=b,moment_dim=n,Q_modular_rank=qr,
                immediate_CQ_kernel=cqkernel,separate_word_rank=wr))
    rational=[]
    for b,rank in ((0,21),(1,23)):
        ix,R,A,Q,C=matrices(4,1,b)
        actual=rational_q_rank(Q,C)
        assert actual==rank,(b,actual)
        rational.append(dict(q=4,a=1,b=b,rational_Q_rank=actual))
    named=[exact_named_check(q) for q in range(1,5)]
    assert sum(x["exact_assertions"] for x in named)==3332
    return dict(schema="PREFIX822_EXACT_OBSERVER_CHECK_V1",
        frozen_input="f42f2906d77f24085c123f3ccfe9667d41caa96d",
        status="ALL_EXACT_ASSERTIONS_PASSED",
        method="exact integer path counts, prime-field elimination modulo 1000000007, and Fraction Gaussian elimination for q=4",
        verification_scope="q=1..10, a in {1,2}, b in {0,1,3}; named-state words up to length four at q=1..4",
        interpretation="Modular ranks are characteristic-zero lower bounds. General separate-word upper bound proved in companion theorem. General Q-only formula is open.",
        finite_rank_rows=rows,exact_rational_boundary=rational,
        named_state_checks=named)

if __name__=="__main__":
    result=run()
    dest=Path(__file__).with_name("PREFIX822_R6_ALL_CAPACITY_WORD_OBSERVER_RESULTS.json")
    dest.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:v for k,v in result.items() if k!="finite_rank_rows"},indent=2))
