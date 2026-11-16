"""R638: exact Z[t] signed BRC quadratic-background three-reference precision."""
from itertools import combinations,permutations
from math import comb
import json

def b(n,k): return comb(n,k) if 0<=k<=n else 0
def norm(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    return a
def add(*rows):
    z=[0]*max(map(len,rows))
    for r in rows:
        for i,v in enumerate(r):z[i]+=v
    return norm(z)
def scale(x,k):return norm([v*k for v in x])
def sub(x,y):return add(x,scale(y,-1))
def mul(x,y):
    z=[0]*(len(x)+len(y)-1)
    for i,a in enumerate(x):
        for j,bv in enumerate(y):z[i+j]+=a*bv
    return norm(z)
def prod(rows):
    p=[1]
    for x in rows:p=mul(p,x)
    return p
def shift(x,n):return [0]*n+list(x)
def divint(x,d):
    assert d and all(z%d==0 for z in x)
    return norm([z//d for z in x])
def ord5(x):return next((i for i,v in enumerate(x) if v%5),10**9)
def coeff(x,i):return x[i] if i<len(x) else 0
def K(i):
    ds=(-b(4,i)+b(2,i-1),b(5,i-1)-b(5,i-2),b(7,i-2),-b(9,i-3))
    return add(*([shift([-v*b(i+1-j,q) for q in range(i+2-j)],i-1) for j,v in enumerate(ds,1) if v and i+1-j>=0] or [[0]]))
def det3(C):
    a,bv,c=C[0];d,e,f=C[1];g,h,i=C[2]
    return a*(e*i-f*h)-bv*(d*i-f*g)+c*(d*h-e*g)
def adj3(C):
    a,bv,c=C[0];d,e,f=C[1];g,h,i=C[2]
    return [[e*i-f*h,c*h-bv*i,bv*f-c*e],
            [f*g-d*i,a*i-c*g,c*d-a*f],
            [d*h-e*g,bv*g-a*h,a*e-bv*d]]
def v5(n):
    assert n;v=0
    while n%5==0:n//=5;v+=1
    return v

c=[0,5,1,2,3,4]
P=[K(i) for i in range(1,13,2)]
M=[K(i) for i in range(2,13,2)]
U=[P[j][2*j:] for j in range(6)]
V=[M[j][2*j+1:] for j in range(6)]
assert [x[0] for x in U]==[2,-8,6,106,83,9]
assert [x[0] for x in V]==[-1,-11,53,119,36,1]
assert all(P[j]==shift(U[j],2*j) and M[j]==shift(V[j],2*j+1) for j in range(6))
W=scale(prod([z for j in range(6) for z in (U[j],V[j])]),12)
H0=[7,0,3,1];H1=[-2,4,0,5];H2=[11,0,-3]
backgrounds=[add(H0,scale(H1,z),scale(H2,z*z)) for z in c]
triple_table=[]; recovery_checks=0; inverse_coeff_checks=0
for axis_triplet in combinations(range(6),3):
    C=[[1,c[x],c[x]**2] for x in axis_triplet]
    det=det3(C);e=v5(det);N=e+1;mod=5**N
    assert e in (0,1)
    triple_table.append({'axes_1based':[x+1 for x in axis_triplet], 'determinant':det, 'five_adic_exponent':e, 'minimum_modulus':mod})
    adj=adj3(C)
    for a in (1,2,4):
        depth=a+8
        refs=[[coeff(backgrounds[x],i)%mod for i in range(depth+1)] for x in axis_triplet]
        recovered_H=[]
        unit=det//5**e
        unit_inv=pow(unit%5,-1,5)
        for k in range(3):
            row=[]
            for i in range(depth+1):
                num=sum(adj[k][m]*refs[m][i] for m in range(3))%mod
                assert num%5**e==0
                row.append(((num//5**e)*unit_inv)%5)
                assert row[-1]==coeff([H0,H1,H2][k],i)%5
                inverse_coeff_checks+=1
            recovered_H.append(row)
        for pi in permutations(range(6)):
            Y=[add(backgrounds[x],mul(shift([1,pi[x]+1],a),P[pi[x]])) for x in range(6)]
            found=[]
            for x in range(6):
                jb=[(coeff(Y[x],i)-sum(c[x]**k*recovered_H[k][i] for k in range(3)))%5 for i in range(depth+1)]
                first=next((i for i,v in enumerate(jb) if v),None)
                found.append(5 if first is None else (first-a)//2)
            assert tuple(found)==pi
            recovery_checks+=1
assert recovery_checks==20*3*720
assert sum(t['five_adic_exponent'] for t in triple_table)==4

# All four exceptional triples admit complete Z[t] collisions.
collision_identity_checks=0;collision_reference_checks=0;collision_witnesses=[]
for z in (1,2,3,4):
    ref_indices=[0,1,c.index(z)]
    assert len(set(ref_indices))==3
    remaining=sorted(set(range(6))-set(ref_indices))
    p,q=remaining[-2:]
    g=lambda x:c[x]*(c[x]-z)
    gp=g(p)
    assert gp and gp%5 and 12%gp==0
    assert g(q)%5
    for a in (1,2,4):
        v=[a+2*j for j in range(6)]
        target=[shift(W,k) for k in v]
        T=divint(sub(target[p],target[q]),gp)
        for x in range(6):
            newlabel=q if x==p else p if x==q else x
            F=add(shift([gp],v[x]),shift([-g(x)],v[p]),shift([g(x)],v[q]))
            assert all(t==0 for t in F[:v[newlabel]])
            Q=F[v[newlabel]:]
            assert Q and Q[0]%5
            Ap=scale(shift(mul(prod([f for j in range(6) for side,f in enumerate((U[j],V[j])) if (j,side)!=(newlabel,0)]),Q),a),12//gp)
            Am=scale(shift(mul(prod([f for j in range(6) for side,f in enumerate((U[j],V[j])) if (j,side)!=(newlabel,1)]),Q),a-1),12//gp)
            hx=scale(T,g(x))
            assert ord5(Ap)==a and ord5(Am)==a-1
            assert add(mul(Ap,P[newlabel]),hx)==target[x]
            assert add(mul(Am,M[newlabel]),hx)==target[x]
            collision_identity_checks+=2
        for x in ref_indices:
            reference=scale(T,g(x))
            assert all(t%5==0 for t in reference)
            collision_reference_checks+=1
        assert any(t%25!=0 for t in scale(T,g(1)))
        collision_witnesses.append({'z':z,'a':a,'swapped_axes_1based':[p+1,q+1],'g_at_p':gp,'g_at_q':g(q)})
for a in (1,2,4):
    depth=a+7
    for j in (4,5):
        assert all((coeff(mul(shift([1],a),P[j]),i)==0 and coeff(mul(shift([1],a-1),M[j]),i)==0) for i in range(depth+1))
result={
    'schema':'R638_QUADRATIC_SIGNED_BRC_EXACT_EVIDENCE_V1',
    'result':'PASS',
    'marker':'R638_QUADRATIC_THREE_REFERENCE_5ADIC_EXACT_PASS',
    'frozen_science':'R462@18783e01e3646c72b7aab3b16d3f565e83e6446f',
    'predecessor':'R637@0e3dc3d63f9d5daa689a2cee0425b1b8af2e160e',
    'model':'H_x=H0+c_x H1+c_x^2 H2, c=(0,5,1,2,3,4), signed R462 K pairs',
    'arithmetic':'integer polynomial and exact coefficient arithmetic modulo 5**N, no float',
    'triples':triple_table,'triple_count':len(triple_table),
    'mod5_triples':sum(t['minimum_modulus']==5 for t in triple_table),
    'mod25_triples':sum(t['minimum_modulus']==25 for t in triple_table),
    'gain_orders':[1,2,4],'permutations_per_triple_per_gain_order':720,
    'recovery_checks':recovery_checks,'coefficient_inverse_checks':inverse_coeff_checks,
    'full_polynomial_collision_checks':collision_identity_checks,
    'mod5_reference_checks':collision_reference_checks,
    'collision_witnesses':collision_witnesses,
    'claim_scope':'one fixed synthetic quadratic axis-background class; source-native X6 operator not established'
}
with open('R638_EVIDENCE.json','w') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(result['marker'],result['recovery_checks'],result['mod5_triples'],result['mod25_triples'],result['full_polynomial_collision_checks'],result['mod5_reference_checks'])
