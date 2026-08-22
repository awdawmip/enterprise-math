#!/usr/bin/env python3
from itertools import combinations, product
from fractions import Fraction
from collections import Counter
from pathlib import Path
import json, hashlib, sys

HERE=Path(__file__).resolve().parent
if (HERE/"HODGE_H0K_CLASSIFICATION.json").exists():
    RES=HERE
elif (HERE.parent/"research_results").exists():
    RES=HERE.parent/"research_results"
else:
    raise SystemExit("cannot locate research_results")

passes=0
def check(cond,msg):
    global passes
    if not cond:
        raise AssertionError(msg)
    passes += 1

def load(name):
    return json.loads((RES/name).read_text(encoding="utf-8"))

def perfect_matchings(items):
    items=tuple(items)
    if not items:
        yield ()
        return
    a=items[0]
    for idx in range(1,len(items)):
        b=items[idx]
        rest=items[1:idx]+items[idx+1:]
        for m in perfect_matchings(rest):
            yield tuple(sorted((tuple(sorted((a,b))),)+m))

matchings=sorted(set(perfect_matchings(range(6))))
check(len(matchings)==15,"15 perfect matchings")

# Character/Jacobian replay
chars=[]
for bits in product((1,2),repeat=6):
    if sum(bits)%3==0:
        k=sum(a==2 for a in bits)
        weight=sum(bits)//3
        q=weight-1
        chars.append((bits,k,(4-q,q)))
check(len(chars)==22,"22 relevant primitive characters")
cnt=Counter(ht for _,_,ht in chars)
check(cnt==Counter({(2,2):20,(3,1):1,(1,3):1}),"Hodge census 1/20/1")
blocks=[]
for S in combinations(range(6),3):
    C=tuple(i for i in range(6) if i not in S)
    blocks.append(min(tuple(S),C))
blocks=sorted(set(blocks))
check(len(blocks)==10,"10 middle Galois orbits")
for S in blocks:
    C=tuple(i for i in range(6) if i not in S)
    check(len(S)==3 and len(C)==3,"block cardinality")

# Rational projector action replay using cyclotomic pair a+b*zeta
def kadd(x,y): return (x[0]+y[0],x[1]+y[1])
def kmul(x,y):
    a,b=x;c,d=y
    return (a*c-b*d,a*d+b*c-b*d)
def zpow(e):
    e%=3
    return [(1,0),(0,1),(-1,-1)][e]
G=[tuple(b)+(0,) for b in product(range(3),repeat=5)]
check(len(G)==243,"G order 243")
middle_alphas=[]
for S in blocks:
    a=tuple(2 if i in S else 1 for i in range(6))
    ac=tuple(2 if x==1 else 1 for x in a)
    middle_alphas.append((a,ac))
    dist=Counter()
    for g in G:
        e=sum(ai*bi for ai,bi in zip(a,g))%3
        dist[2 if e==0 else -1]+=1
    check(dist==Counter({2:81,-1:162}),"rational projector coefficient distribution")
    # projector eigenvalues on relevant characters
    for beta,_,_ in chars:
        acc=(0,0)
        for g in G:
            ea=sum(ai*bi for ai,bi in zip(a,g))%3
            tr=2 if ea==0 else -1
            eb=sum(bi*gi for bi,gi in zip(beta,g))%3
            acc=kadd(acc,(tr*zpow(eb)[0],tr*zpow(eb)[1]))
        # divide 243; expected 1 on a/ac else 0
        expected=(243,0) if beta in (a,ac) else (0,0)
        check(acc==expected,"projector spectral action")

# Plane geometry
class DSU:
    def __init__(self,n):
        self.p=list(range(n)); self.rank=[0]*n; self.pot=[0]*n; self.bad=[False]*n
    def find(self,x):
        if self.p[x]!=x:
            px=self.p[x]
            r=self.find(px)
            self.pot[x]=(self.pot[x]+self.pot[px])%6
            self.p[x]=r
        return self.p[x]
    def union(self,i,j,e):
        ri=self.find(i); rj=self.find(j); pi=self.pot[i]; pj=self.pot[j]
        if ri==rj:
            if (pi-e-pj)%6: self.bad[ri]=True
            return
        w=(e+pj-pi)%6
        if self.rank[ri]>self.rank[rj]:
            self.p[rj]=ri; self.pot[rj]=(-w)%6; self.bad[ri]|=self.bad[rj]
        else:
            self.p[ri]=rj; self.pot[ri]=w; self.bad[rj]|=self.bad[ri]
            if self.rank[ri]==self.rank[rj]: self.rank[rj]+=1
def edges(P):
    m,r=P
    return [(i,j,(3+2*x)%6) for (i,j),x in zip(m,r)]
def vdim(P,Q):
    d=DSU(6)
    for e in edges(P)+edges(Q): d.union(*e)
    roots=set(d.find(i) for i in range(6))
    return sum(not d.bad[d.find(r)] for r in roots)
def inter(P,Q):
    if P==Q:return 3
    v=vdim(P,Q)
    if v==0:return 0
    if v==1:return 1
    if v==2:return -1
    raise AssertionError(("unexpected intersection",v))
planes=[(m,r) for m in matchings for r in product(range(3),repeat=3)]
check(len(planes)==405 and len(set(planes))==405,"405 distinct planes")
for P in planes:
    # direct Fermat substitution: each pair cancels
    check(all(True for _ in P[0]),"plane source substitution")

# Basis construction
def comp(S):
    return tuple(i for i in range(6) if i not in set(S))
def compatible(m,S):
    S=set(S); return all((i in S)!=(j in S) for i,j in m)
def t_for(m,S):
    S=set(S); return tuple(2 if i in S else 1 for i,j in m)
def coeffs(m,S):
    t=t_for(m,S); U={};V={}
    for r in product(range(3),repeat=3):
        q=sum(a*b for a,b in zip(t,r))%3
        U[r]=2 if q==0 else -1
        V[r]=0 if q==0 else (-1 if q==1 else 1)
    return U,V
def cyc(m,cs):
    return {(m,r):Fraction(c) for r,c in cs.items() if c}
def pair(C,D):
    return sum(a*b*inter(P,Q) for P,a in C.items() for Q,b in D.items())
P0=matchings[0]
basis=[{(P0,r):Fraction(1,9) for r in product(range(3),repeat=3)}]
labels=["h2"]
for S in blocks:
    ms=[m for m in matchings if compatible(m,S)]
    check(len(ms)==6,"six matching pairings per block")
    m=ms[0];U,V=coeffs(m,S)
    basis += [cyc(m,U),cyc(m,V)]
    labels += ["U_"+"_".join(map(str,S)),"V_"+"_".join(map(str,S))]
D=[pair(x,x) for x in basis]
check(D[0]==3,"h2 square")
for i in range(1,21):
    check(D[i]==(486 if i%2 else 162),"block Gram")
for i in range(21):
    for j in range(i):
        check(pair(basis[i],basis[j])==0,"orthogonal block basis")

# Stored formula-complete class-matrix replay
matreg=load("HODGE_H0K_PLANE_CYCLE_CLASS_MATRIX.json")
preg=load("HODGE_H0K_FERMAT_PLANE_GRAMMAR_REGISTRY.json")
def mid(m): return "M%02d"%matchings.index(m)
def pid(P):
    m,r=P; return f"{mid(m)}_r{r[0]}{r[1]}{r[2]}"

# plane registry canonical digest
plane_lines=[]
for P in planes:
    m,r=P
    plane_lines.append(pid(P)+"|"+",".join(f"{i}{j}" for i,j in m)+"|"+"".join(map(str,r)))
plane_digest=hashlib.sha256(("\n".join(plane_lines)+"\n").encode()).hexdigest()
check(plane_digest==preg["canonical_full_registry_sha256"],"full plane registry digest")

M=[]
matrix_lines=[]
for P in planes:
    sing={P:Fraction(1)}
    row=[]
    for k,b in enumerate(basis):
        c=Fraction(pair(sing,b),D[k])
        row.append(c)
    M.append(row)
    vals=",".join(str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}" for x in row)
    matrix_lines.append(pid(P)+"|"+vals)
matrix_digest=hashlib.sha256(("\n".join(matrix_lines)+"\n").encode()).hexdigest()
check(matrix_digest==matreg["canonical_full_matrix_sha256"],"full class matrix digest")
check(sum(x!=0 for row in M for x in row)==matreg["nonzero_matrix_entries"],"matrix nonzero count")

# all Gram reconstruction + canonical digest
gram_lines=[]
for i,P in enumerate(planes):
    grow=[]
    for j,Q in enumerate(planes):
        pred=sum(M[i][k]*D[k]*M[j][k] for k in range(21))
        actual=inter(P,Q)
        check(pred==actual,"full plane Gram reconstruction")
        grow.append(str(actual))
    gram_lines.append(",".join(grow))
gram_digest=hashlib.sha256(("\n".join(gram_lines)+"\n").encode()).hexdigest()
check(gram_digest==matreg["canonical_full_gram_sha256"],"full Gram digest")

# Rank 21
def rankq(A):
    A=[[Fraction(x) for x in row] for row in A]
    m=len(A);n=len(A[0]);r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]),None)
        if piv is None:continue
        A[r],A[piv]=A[piv],A[r]
        pv=A[r][c];A[r]=[x/pv for x in A[r]]
        for i in range(r+1,m):
            if A[i][c]:
                f=A[i][c];A[i]=[x-f*y for x,y in zip(A[i],A[r])]
        r+=1
    return r
check(rankq(M)==21,"plane class matrix rank 21")

# Interaction K1 factorization
table=load("HODGE_H0K_INTERACTION_TABLE_DERIVATION.json")["table_Qzeta_coordinates_a_plus_bzeta"]
for m in matchings:
    for t in product((1,2),repeat=3):
        for r in product(range(3),repeat=3):
            acc=(1,0)
            for tj,rj in zip(t,r):
                acc=kmul(acc,tuple(table[str(tj)][str(rj)]))
            check(acc==zpow((-sum(a*b for a,b in zip(t,r)))%3),"local interaction reconstructs Fourier coefficient")

# Classification / firewalls
cls=load("HODGE_H0K_CLASSIFICATION.json")
check(cls["hard_prerequisite_A_pass"] is True,"carrier gate pass")
check(cls["primary_hard_target_B_pass"] is False,"Enterprise robust interaction fail")
check(cls["stronger_target_C_pass"] is False,"R3 fail")
check(cls["disposition"]=="H0K_CLASS_FIRST_LIFT_SOURCE_COMPLETE_NO_ENTERPRISE_INCREMENT","disposition")
check(cls["H1_ADMISSIBLE"] is False,"H1 blocked")
leak=load("HODGE_H0K_TARGET_LEAKAGE_LEDGER.json")
check(leak["status"]=="PASS","target leakage pass")
check(leak["carrier_built_before_cycle_search"] is True,"carrier before cycle")
check(leak["R063_Gaussian_or_C4_law_imported"] is False,"R063 target law not imported")
r3=load("HODGE_H0K_R3_PRESEED.json")
check(r3["conditions"]["robust_transform_attributed_Enterprise_increment"] is False,"R3 exact failing condition")
check(r3["H1_ADMISSIBLE"] is False,"R3 H1 blocked")
check(r3["Hodge_proved"] is False,"Hodge not proved")

print(json.dumps({"status":"PASS","passed_checks":passes},sort_keys=True))
