#!/usr/bin/env python3
"""PREFIX-275: exact C4 ordered-path-pair BRC observer tomography.

Scope: declared Gaussian-rational Hermitian Gram observer with independently
preparable per-label C4 phases, NOT native heartbeat dynamics or source import.
All scientific arithmetic uses exact provenance-labeled BRC ordered pairs.
"""
from fractions import Fraction as F
from itertools import product, combinations
import json

ZERO=(F(0),F(0)); ONE=(F(1),F(0))
I=(F(0),F(1))
PHASES=(ONE,I,(F(-1),F(0)),(F(0),F(-1)))

def add(a,b): return (a[0]+b[0],a[1]+b[1])
def conj(a): return (a[0],-a[1])
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(a,c): return (a[0]*c,a[1]*c)

def make_gram(k):
    # Labeled vectors in a declared detector residual carrier Q(i)^(k+2),
    # each has a private identity coordinate so Gram is strictly PD.
    vs=[]
    for i in range(k):
        v=[ZERO for _ in range(k+2)]
        v[i]=ONE
        v[k]=(F(i+1,3),F((i%3)-1,4))
        v[k+1]=(F((i%2)+1,5),F(i+2,7))
        vs.append(tuple(v))
    gram=[]
    for i in range(k):
        row=[]
        for j in range(k):
            acc=ZERO
            for x,y in zip(vs[i],vs[j]):
                acc=add(acc,mul(conj(x),y))
            row.append(acc)
        gram.append(tuple(row))
    return tuple(gram)

def readout(gram,m,p):
    """Path-pair ordered BRC: preserve all labels (a,b) and Gaussian phases."""
    k=len(gram); total=ZERO
    for a in range(k):
        for b in range(k):
            weight=mul(mul(conj(PHASES[p[a]]),PHASES[p[b]]),gram[a][b])
            total=add(total,scale(weight,m[a]*m[b]))
    assert total[1]==0,('non-Hermitian BRC outcome',total)
    return total[0]

def design(k):
    z=(0,)*k
    out=[z]
    for i in range(k-1):
        p=list(z);p[i]=2;out.append(tuple(p))
    for i,j in combinations(range(k-1),2):
        p=list(z);p[i]=p[j]=2;out.append(tuple(p))
    for i in range(k-1):
        p=list(z);p[i]=1;out.append(tuple(p))
        for j in range(i+1,k-1):
            p=list(z);p[i]=1;p[j]=2;out.append(tuple(p))
    assert len(out)==1+k*(k-1)==len(set(out))
    return tuple(out)

def reconstruct(gram,m):
    k=len(gram)
    z=(0,)*k
    base=readout(gram,m,z)
    singles={}
    for i in range(k-1):
        p=list(z);p[i]=2
        singles[i]=readout(gram,m,p)
    B={}
    for i,j in combinations(range(k-1),2):
        p=list(z);p[i]=p[j]=2
        B[i,j]=(readout(gram,m,p)-singles[i]-singles[j]+base)/4
    for i in range(k-1):
        B[i,k-1]=-(singles[i]-base)/2-sum((B[min(i,j),max(i,j)] for j in range(k-1) if j!=i),F(0))
    D=base-sum(B.values(),F(0))
    C={}
    for i in range(k-1):
        p=list(z);p[i]=1
        def iz(q):
            # Remove known real contributions from non-incident path pairs.
            s=[(-1 if phase==2 else 1) for phase in q]
            unrelated=sum((b*s[a]*s[b_] for (a,b_),b in B.items() if a!=i and b_!=i),F(0))
            return readout(gram,m,q)-D-unrelated
        z0=iz(p)
        for j in range(i+1,k-1):
            q=list(p);q[j]=2
            C[i,j]=(z0-iz(q))/2
        C[i,k-1]=z0+sum((C[j,i] for j in range(i)),F(0))-sum((C[i,j] for j in range(i+1,k-1)),F(0))
    assert len(B)==len(C)==k*(k-1)//2
    wantD=sum((m[i]*m[i]*gram[i][i][0] for i in range(k)),F(0))
    assert D==wantD
    for i,j in combinations(range(k),2):
        assert B[i,j]==2*m[i]*m[j]*gram[i][j][0]
        assert C[i,j]==2*m[i]*m[j]*gram[i][j][1]
    return D,B,C

def feature_row(p):
    k=len(p); row=[1]
    # Real cross and imaginary cross coordinates ordered identically.
    for i,j in combinations(range(k),2):
        relative=mul(conj(PHASES[p[i]]),PHASES[p[j]])
        row.append(int(relative[0]))
    for i,j in combinations(range(k),2):
        relative=mul(conj(PHASES[p[i]]),PHASES[p[j]])
        row.append(-int(relative[1]))
    return row

def bareiss_determinant(a):
    a=[list(row) for row in a]
    n=len(a);prev=1;sign=1
    for z in range(n-1):
        if a[z][z]==0:
            pivot=next((r for r in range(z+1,n) if a[r][z]),None)
            if pivot is None:return 0
            a[z],a[pivot]=a[pivot],a[z];sign=-sign
        p=a[z][z]
        for i in range(z+1,n):
            for j in range(z+1,n):
                num=a[i][j]*p-a[i][z]*a[z][j]
                assert num%prev==0
                a[i][j]=num//prev
        for i in range(z+1,n):a[i][z]=0
        prev=p
    return sign*a[-1][-1]

def signature_readout(p,D,B,C):
    v=D
    for (i,j),b in B.items():
        q=mul(conj(PHASES[p[i]]),PHASES[p[j]])
        v+=b*q[0]-C[i,j]*q[1]
    return v

def fmt(x):return str(x.numerator) if x.denominator==1 else str(x.numerator)+'/'+str(x.denominator)

def stage50_two_port_probe():
    c=I;coherence=scale(c,F(1,2))
    vals=[]
    for phase in range(4):
        z=mul(PHASES[phase],coherence)
        vals.append(F(5,18)*(1-z[0]))
    assert vals==[F(5,18),F(5,12),F(5,18),F(5,36)]
    return [fmt(v) for v in vals]

def main():
    report={"schema":"PREFIX275_AUTHOR_SIDE_EXACT_C4_TOMOGRAPHY_V1","model":"independent labeled C4 phases; complete fixed detector Gram; ordered provenance path pairs","cases":[]}
    for k in range(2,7):
        g=make_gram(k)
        m=tuple(F(i+2,i+3) for i in range(k))
        D,B,C=reconstruct(g,m)
        phases=design(k)
        M=[feature_row(p) for p in phases]
        det=bareiss_determinant(M)
        assert det!=0,('singular_design',k)
        assert all(readout(g,m,p)==signature_readout(p,D,B,C) for p in phases)
        classes=4**(k-1)
        for p0 in product(range(4),repeat=k-1):
            p=p0+(0,)
            assert readout(g,m,p)==signature_readout(p,D,B,C)
        report["cases"].append({"k":k,"fixed_phase_settings":len(phases),"accessible_real_dimensions":1+k*(k-1),"hidden_diagonal_dimensions":k-1,"full_gram_dimensions":k*k,"all_global_phase_quotient_settings_checked":classes,"design_determinant":str(det),"strict_pd_by_private_identity_coordinates":True,"result":"PASS"})
    # Independent exact nonidentifiability witness within the strictly PD cone.
    a=((ONE,ZERO),(ZERO,ONE))
    b=(((F(3,2),F(0)),ZERO),(ZERO,(F(1,2),F(0))))
    m=(F(1),F(1))
    for p0 in range(4):
        assert readout(a,m,(p0,0))==readout(b,m,(p0,0))==2
    assert a!=b and a[0][0]!=b[0][0]
    assert F(3,2)>0 and F(1,2)>0
    report["diagonal_kernel_counterexample"]={"gram_a":"diag(1,1)","gram_b":"diag(3/2,1/2)","fixed_all_on_C4_outcome":"2 for all four relative phases","single_path_outcome_1":"1 versus 3/2"}
    report["source_stage50_two_port_coherence_test"]={"coherence":"i/2","four_phases_0_1_2_3":stage50_two_port_probe(),"scope":"Stage50 declared external reader formula, not native law or Stage46 source import"}
    report["source_import_executed"]=False
    report["native_model_law_verified"]=False
    report["native_claim_verified"]=False
    print(json.dumps(report,ensure_ascii=False,sort_keys=True,indent=2))

if __name__=='__main__':main()
