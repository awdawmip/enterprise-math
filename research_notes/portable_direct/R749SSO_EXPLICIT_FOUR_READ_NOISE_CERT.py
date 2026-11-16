#!/usr/bin/env python3
"""R749SSO: exact four-read 7/8 guaranteed-noise-gap certificate; Python stdlib."""
from fractions import Fraction as F
from itertools import permutations
import json

W=(1,1,2,3,6)
N=26
n=[0]*(N+1); n[0]=1
for w in W:
    for t in range(w,N+1): n[t]+=n[t-w]
C=[0]*(N+1); T=[0]*(N+1)
for q in range(1,N+1):
    C[q]=C[q-1]+n[q-1]
    T[q]=T[q-1]+C[q-1]
assert [(C[q],T[q]) for q in (7,8,13,14,19,20,25,26)] == [
    (65,91),(98,156),(506,1261),(662,1767),
    (2106,7447),(2576,9553),(6331,28883),(7441,35214)]
def S(q): return 18*q**4+54*q**3-345*q**2+2070*q-16315

ONE={(0,0):F(1)}; E={(1,0):F(1)}; D={(0,1):F(1)}
def const(n): return {(0,0):F(n)} if n else {}
def add(*ps):
    o={}
    for p in ps:
        for k,v in p.items(): o[k]=o.get(k,F(0))+v
    return {k:v for k,v in o.items() if v}
def mul(a,b):
    o={}
    for (i,j),v in a.items():
        for (k,l),w in b.items():
            z=(i+k,j+l); o[z]=o.get(z,F(0))+v*w
    return {k:v for k,v in o.items() if v}
def scale(a,t): return {k:v*t for k,v in a.items() if v*t}
def det(rows):
    o={}
    for perm in permutations(range(3)):
        t=ONE
        for i in range(3): t=mul(t,rows[i][perm[i]])
        inv=sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
        o=add(o,scale(t,-1 if inv%2 else 1))
    return o
def row(j):
    q,p=7+6*j,8+6*j
    v=scale(add(const(C[q]),D),p**3)
    u=add(scale(add(const(T[q]),E),q**3),
          scale(add(const(C[q]),D),F(S(p)-S(q),108)))
    return v,scale(u,-1),add(scale(u,C[p]),scale(v,-T[p]))
rows=[row(j) for j in range(4)]
H2=det([rows[i] for i in (0,1,2)])
H3=scale(det([rows[i] for i in (0,1,3)]),6)
coef2={(2,0):-25999464658656,(2,1):-2170402847280,
 (1,0):25665881152213864,(1,1):3818332725903764,(1,2):8517190893192,
 (0,0):-45032970208568420,(0,1):-49829920474516588,
 (0,2):-4939292865911139,(0,3):923243492481}
coef3={(2,0):-2376041366849184,(2,1):-111784049774064,
 (1,0):2145129655398174560,(1,1):315754546776127640,(1,2):531210657740480,
 (0,0):-851458936224224926,(0,1):-4586875289048978667,
 (0,2):-423838272588088662,(0,3):55771703467759}
assert H2=={k:F(v) for k,v in coef2.items()}
assert H3=={k:F(v) for k,v in coef3.items()}
def terms(coef,degree):
    m=max(j for i,j in coef if i==degree)
    return [coef.get((degree,j),0) for j in range(m+1)]
a,b,c=[terms(coef2,k) for k in (2,1,0)]
A,B,Cc=[terms(coef3,k) for k in (2,1,0)]
def padd(*ps):
    o=[0]*max(map(len,ps))
    for p in ps:
        for i,x in enumerate(p): o[i]+=x
    while len(o)>1 and o[-1]==0:o.pop()
    return o
def pmul(p,q):
    o=[0]*(len(p)+len(q)-1)
    for i,v in enumerate(p):
        for j,w in enumerate(q):o[i+j]+=v*w
    while len(o)>1 and o[-1]==0:o.pop()
    return o
def psub(p,q):return padd(p,[-x for x in q])
x=psub(pmul(a,Cc),pmul(A,c))
y=psub(pmul(a,B),pmul(A,b))
z=psub(pmul(b,Cc),pmul(B,c))
resultant=psub(pmul(x,x),pmul(y,z))
Q=[109796349314075020060949372306640574723358682,
 -38045439719073116059985350517020931359464817,
 -2277402286244385991893563886215342942920759,
 923053369069668327403631270396371444479035,
 14501898594290005726122391371730051335594,
 175742992512176288201620423729874424]
expected=pmul(pmul(pmul([65,1],[506,1]),[1569882365,234443938]),Q)
assert resultant==[-67436544*t for t in expected]
qmargin=Q[0]-sum(2**i*abs(t) for i,t in enumerate(Q) if i)
assert qmargin==16979397777109496872916184850765128499562660
Rmin=67436544*63*504*(1569882365-2*234443938)*qmargin
def norm(p):return sum(2**i*abs(v) for i,v in enumerate(p))
a2,a3,b2,b3=norm(a),norm(A),norm(b),norm(B)
c2,c3=norm(c),norm(Cc)
ymax=a2*b3+a3*b2
h2max=4*a2+2*b2+c2
h3max=4*a3+2*b3+c3
pmax=a2*h3max+a3*h2max
vmax=[];umax=[];kmax=[]
for j in range(4):
    q,p=7+6*j,8+6*j
    vmax.append(p**3*(C[q]+2))
    umax.append(q**3*(T[q]+2)+(abs(S(p)-S(q))*(C[q]+2)+107)//108)
    kmax.append((C[q]+2)*(C[p]+2))
def row_bound(indices,multiplier):
    return multiplier*sum(kmax[j]*(vmax[k]*umax[l]+umax[k]*vmax[l])
      for j,k,l in ((indices[0],indices[1],indices[2]),
                    (indices[1],indices[0],indices[2]),
                    (indices[2],indices[0],indices[1])))
det2=row_bound((0,1,2),1)
det3=row_bound((0,1,3),6)
pcoef=a2*det3+a3*det2
qcoef=b2*det3+b3*det2
bigK=(pmax+4*ymax)*pcoef+ymax*qcoef
assert det2==3142649593132974464
assert det3==152526800932915943616
assert Rmin==40028915051766416168336192988259455494375902399536945123683205120
assert bigK==2385528822152469524812195767070353196847512054610269204964931381755904
minimum_gap=F(Rmin,bigK)
noise_radius=minimum_gap/2
# Identity: R=P^2-2eJP-JQ; P=a*H3-A*H2, J=a*B-A*b, Q=b*H3-B*H2.
# Each L_j dot (E,D,1) = (C_(7+6j)+d)(C_(8+6j)+D)*Delta_j.
# Hence |H2|<=det2*max|Delta|, |H3|<=det3*max|Delta| and
# |R|<=bigK*max|Delta| on all four error-square parameters.
assert minimum_gap>F(1,100000) and minimum_gap<F(1,10000)
result={
 "schema":"R749SSO_FOUR_READ_QUANTITATIVE_GAP_CERT_V1","status":"PASS",
 "weights":list(W),"cutoffs":[7,8],"read_offsets":[0,6,12,18],
 "domain":"common real (e,d) and (E,D) independently in [-2,2]^2",
 "resultant_lower_bound":str(Rmin),
 "determinant_bounds":[str(det2),str(det3)],
 "coefficient_bounds":{"a2":str(a2),"a3":str(a3),"b2":str(b2),"b3":str(b3),
  "c2":str(c2),"c3":str(c3),"J":str(ymax),"H2":str(h2max),"H3":str(h3max),"P":str(pmax)},
 "P_coefficient":str(pcoef),"Q_coefficient":str(qcoef),
 "K_integer":str(bigK),"guaranteed_sup_distance":str(minimum_gap),
 "guaranteed_noise_radius":str(noise_radius),
 "verification":"Reconstructed exact source counts, determinant coefficients, full resultant factorization and integer interval/Lipschitz bounds.",
 "boundary":"Certified conservative gap for cutoffs 7 versus 8; AUTHOR_EXACT_NOT_REVIEWED"
}
with open("R749SSO_FOUR_READ_EXPLICIT_GAP_RESULTS.json","w",encoding="utf-8") as fh:
    json.dump(result,fh,ensure_ascii=False,sort_keys=True,indent=2);fh.write("\n")
print("PASS; exact lower gap",minimum_gap,"noise radius",noise_radius)
