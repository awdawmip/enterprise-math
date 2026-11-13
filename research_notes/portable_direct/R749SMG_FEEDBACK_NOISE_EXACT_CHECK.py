"""R749SMG: exact rational validation of feedback-before-query observer ranks."""
from fractions import Fraction as F
from itertools import product
from math import prod
import json
from pathlib import Path

S=(1,-1)
H=list(product(S,repeat=3))
W=list(product(S,repeat=3))
E=(F(0),F(1,4),F(1,2),F(3,4),F(1))

def rank(A):
    a=[list(row) for row in A]; k=0; m=len(a)
    for j in range(len(a[0])):
        p=next((i for i in range(k,m) if a[i][j]),None)
        if p is None: continue
        a[k],a[p]=a[p],a[k]
        v=a[k][j];a[k]=[u/v for u in a[k]]
        for i in range(k+1,m):
            if a[i][j]:
                v=a[i][j];a[i]=[x-v*y for x,y in zip(a[i],a[k])]
        k+=1
        if k==m:break
    return k

def det(A):
    a=[list(row) for row in A];n=len(a);v=F(1)
    for j in range(n):
        p=next((i for i in range(j,n) if a[i][j]),None)
        if p is None:return F(0)
        if p!=j:a[p],a[j]=a[j],a[p];v=-v
        d=a[j][j];v*=d
        for i in range(j+1,n):
            if a[i][j]:
                u=a[i][j]/d
                for k in range(j+1,n):a[i][k]-=u*a[j][k]
                a[i][j]=F(0)
    return v

def q(a,b,c,z,ep):
    x,y,t=z; alpha=[1-2*e for e in ep]
    return F(2+alpha[0]*a*x,4)*F(2+alpha[1]*b*(y if a==1 else t),4)*F(2+alpha[2]*c*y*t,4)

def matrix(ep):
    return [[q(*w,z,ep) for z in H] for w in W]

def q0(a,b,c,z):
    x,y,t=z
    return F(2+a*x,4)*F(2+b*(y if a==1 else t),4)*F(2+c*y*t,4)

BASE=[[q0(*w,z) for z in H] for w in W]

def post(ep):
    return [[sum(BASE[j][k]*prod(1-e if o[i]==w[i] else e for i,e in enumerate(ep)) for j,w in enumerate(W)) for k in range(8)] for o in W]

def marginal(M,idx):
    return [[sum(M[j][k] for j,w in enumerate(W) if tuple(w[i] for i in idx)==o) for k in range(8)] for o in product(S,repeat=len(idx))]

def pred(ep):
    a,b,c=[e!=F(1,2) for e in ep]
    if a:return 2**(1+b+c)
    if b and not c:return 3
    return 2**(b+c)

def mult(M,p):return [sum(x*y for x,y in zip(row,p)) for row in M]
def tv(u,v):return sum(abs(x-y) for x,y in zip(u,v))/2

py=[F(1+F(y,2),8) for x,y,t in H]
pt=[F(1+F(t,2),8) for x,y,t in H]
assert min(py+pt)>=F(1,16)
counts={}; contrast=[]
for ep in product(E,repeat=3):
    M=matrix(ep)
    assert all(sum(M[i][j] for i in range(8))==1 for j in range(8))
    assert all(x>=0 for row in M for x in row)
    r=rank(M);assert r==pred(ep),(ep,r)
    counts[r]=counts.get(r,0)+1
    expected=F(1,4096)*prod(abs(1-2*e)**4 for e in ep)
    assert abs(det(M))==expected,(ep,det(M),expected)
    if ep[0]==ep[2]==F(1,2) and ep[1]!=F(1,2):
        P=post(ep)
        assert rank(P)==2 and rank(M)==3
        assert tv(mult(P,py),mult(P,pt))==0
        measured=tv(mult(M,py),mult(M,pt))
        assert measured==abs(1-2*ep[1])/8
        contrast.append({"epsilon_B":str(ep[1]),"feedback_TV":str(measured)})
for ea in E:
    M=matrix((ea,F(0),F(0)))
    for mask in range(8):
        idx=[i for i in range(3) if mask>>i & 1]
        assert 1<=rank(marginal(M,idx))<=2**len(idx)

result={"status":"PASS","scientific_pin":"a72226e2430ffa4786321ac86e7f0c599d5f0389",
 "scope":"A public bit is fed back into the second named-port selector; B,C post-noise",
 "rational_noise_values":["0","1/4","1/2","3/4","1"],
 "matrix_cases":125,"exact_rank_and_determinant_checks":125,
 "rank_counts":{str(k):v for k,v in sorted(counts.items())},
 "positional_marginal_checks":40,
 "all_real_parameter_rank_theorem":"See companion R749SMG proof",
 "determinant_abs":"prod_i(abs(1-2*epsilon_i)**4)/4096",
 "contrast":{"postprocessed_rank":2,"feedback_rank":3,"postprocessed_TV":"0",
 "feedback_TV":"abs(1-2*epsilon_B)/8","positive_priors":"(1+y/2)/8 versus (1+t/2)/8"},
 "contrast_checks":contrast}
print(json.dumps(result,indent=2,ensure_ascii=False))
Path(__file__).with_name("R749SMG_FEEDBACK_NOISE_EXACT_RESULTS.json").write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
