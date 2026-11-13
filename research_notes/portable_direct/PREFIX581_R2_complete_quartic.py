#!/usr/bin/env python3
"""Frozen native 96-port X6-BRC: exact all-axis/gate fourth cumulant certificate.
Reconstructs pinned labelled original edges, keeps all 6 axes, 96 ports and gate.
Requires SymPy. Writes a complete 126-monomial rational machine certificate.
"""
import json
from itertools import product
from math import factorial, comb
from pathlib import Path
import sympy as sp

STARS=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(star,c):
    return tuple((-1 if c>0 else 1)*k for k in STARS[star] if k!=abs(c))
PHASES=tuple((a,p,sgn*k) for a in range(4) for k in STARS[a] for sgn in (-1,1) for p in near(a,sgn*k))
PHASE_INDEX={x:i for i,x in enumerate(PHASES)}
def successors(ph):
    a,p,c=PHASES[ph]
    b=next(b for b in range(4) if b!=a and abs(c) in STARS[b])
    return tuple(PHASE_INDEX[t] for t in [(a,c,k) for k in near(a,c) if k!=p]+[(b,c,k) for k in near(b,c)])
NEXT=tuple(successors(i) for i in range(48))
TARGET=PHASE_INDEX[(0,1,-3)]
ACTIONS=tuple(product(range(3),(0,1)))
def sg(phase,k):
    c=PHASES[phase][2]
    return (1 if c>0 else -1) if abs(c)==k else 0
def edge(port,act):
    ph,bit=divmod(port,2);slot,newbit=act
    nxt=NEXT[ph][slot]
    weights=[]
    for k in range(1,7):
        left,right=sg(ph,k),sg(nxt,k)
        val=abs(left)+abs(right)-abs(right)+abs(left)
        assert val in (0,2)
        weights.append(val//2)
    gate=int(bit==newbit==1 and nxt==TARGET)
    return 2*nxt+newbit,tuple(weights)+(gate,)

N=96
E=[[(j,*r) for ac in ACTIONS for j,r in [edge(i,ac)]] for i in range(N)]
assert all(len(row)==6 for row in E)
assert all(sum(x[1:7])==1 for row in E for x in row)
assert sum(r[7] for row in E for r in row)==3
one=sp.ones(N,1); pi=sp.ones(1,N)/N
P=sp.zeros(N,N)
for i,row in enumerate(E):
    for rec in row:P[i,rec[0]]+=sp.Rational(1,6)
assert P*one==one and pi*P==pi
adj=[set(rec[0] for rec in row) for row in E]
rev=[set() for _ in range(N)]
for i,row in enumerate(adj):
    for j in row:rev[j].add(i)
def flood(graph):
    seen={0}; stack=[0]
    while stack:
        for v in graph[stack.pop()]:
            if v not in seen:seen.add(v);stack.append(v)
    return seen
assert len(flood(adj))==N and len(flood(rev))==N
colors=[None]*N;colors[0]=0; stack=[0]
while stack:
    i=stack.pop()
    for j in adj[i]:
        if colors[j] is None: colors[j]=1-colors[i];stack.append(j)
        else: assert colors[j]==1-colors[i]
assert sorted((colors.count(0), colors.count(1)))==[48,48]
Z=sp.eye(N)-P+one*pi
Zinv=Z.inv()
assert Z*Zinv==sp.eye(N)

def rate4(v):
    m=[sp.zeros(N,N) for _ in range(5)]
    for i,row in enumerate(E):
        for rec in row:
            j=rec[0]
            w=sum(v[k]*rec[k+1] for k in range(7))
            for k in range(1,5):m[k][i,j]+=sp.Rational(w**k,6*factorial(k))
    L=[sp.Integer(1)]; V=[one]
    for k in range(1,5):
        u=sp.zeros(N,1)
        for j in range(1,k+1):u+=m[j]*V[k-j]
        l=(pi*u)[0]; L.append(l)
        rhs=u-l*one
        for j in range(1,k):rhs-=L[j]*V[k-j]
        vv=Zinv*rhs
        assert (pi*vv)[0]==0 and (sp.eye(N)-P)*vv==rhs
        V.append(vv)
    l1,l2,l3,l4=L[1:]
    return sp.factor(24*l4-24*l1*l3-12*l2**2+24*l1**2*l2-6*l1**4)

def compositions(n,total):
    if n==1:yield (total,)
    else:
        for x in range(total+1):
            for tail in compositions(n-1,total-x):
                yield (x,)+tail

GRID=list(compositions(6,4))
assert len(GRID)==126
values={}
for node in GRID:
    v=(node[0],node[1],node[2],node[3],node[4],0,node[5])
    values[node]=rate4(v)
fval={node[:5]:values[node] for node in GRID}
DELTA={}
for gamma in (g for total in range(5) for g in compositions(5,total)):
    acc=sp.S(0)
    for eta in product(*(range(q+1) for q in gamma)):
        coef=(-1)**(sum(gamma)-sum(eta))
        for a,b in zip(gamma,eta):coef*=comb(a,b)
        acc+=coef*fval[eta]
    DELTA[gamma]=sp.factor(acc)
assert len(DELTA)==126
y=sp.symbols('y1:7')
S=sum(y); Pfull=0
for gamma,diff in DELTA.items():
    if not diff:continue
    term=diff*S**(4-sum(gamma))
    for i,k in enumerate(gamma):
        for j in range(k):term*=4*y[i]-j*S
        term/=factorial(k)
    Pfull+=term
Pfull=sp.Poly(sp.expand(Pfull)/sp.Integer(256),*y)
assert Pfull.total_degree()==4 and len(Pfull.terms())==126
for node,val in values.items():
    assert Pfull.eval(dict(zip(y,node)))==val

heldout={
  'R1-K': (1,0,0,0,0,-1),
  'R1+R2-K': (1,1,0,0,0,-1),
  'R1-R3+K': (1,0,-1,0,0,1),
  'R1+R2+R3+R4+R5-2K': (1,1,1,1,1,-2)
}
for name,v in heldout.items():
    expected=rate4((v[0],v[1],v[2],v[3],v[4],0,v[5]))
    got=Pfull.eval(dict(zip(y,v)))
    assert got==expected,(name,got,expected)

def orig6(a1,a2,a3,a4,a5,a6,b):
    return Pfull.eval(dict(zip(y,(a1-a6,a2-a6,a3-a6,a4-a6,a5-a6,b))))

a,b,c=sp.symbols('a b c')
restriction=sp.Poly(sp.expand(orig6(0,0,0,0,a,b,c)),a,b,c)
prior579={
 'a4_b4':'-659/93312','a3b_ab3':'85/5832','a2b2':'-191/15552',
 'a3c_b3c':'319/746496','a2bc_ab2c':'-149/248832',
 'a2c2_b2c2':'39167/28311552','abc2':'-7031/4718592',
 'ac3_bc3':'-3378511/1528823808','c4':'434651857/97844723712'}
expected579=(
 sp.Rational(prior579['a4_b4'])*(a**4+b**4)
 +sp.Rational(prior579['a3b_ab3'])*(a**3*b+a*b**3)
 +sp.Rational(prior579['a2b2'])*a*a*b*b
 +sp.Rational(prior579['a3c_b3c'])*(a**3+b**3)*c
 +sp.Rational(prior579['a2bc_ab2c'])*(a*a*b+a*b*b)*c
 +sp.Rational(prior579['a2c2_b2c2'])*(a*a+b*b)*c*c
 +sp.Rational(prior579['abc2'])*a*b*c*c
 +sp.Rational(prior579['ac3_bc3'])*(a+b)*c**3
 +sp.Rational(prior579['c4'])*c**4)
assert restriction.as_expr()==sp.expand(expected579)

s,t=sp.symbols('s t')
YGate=sp.Poly(sp.expand(orig6(
 -3*s/sp.Integer(64),-s/sp.Integer(64),
 -3*s/sp.Integer(64),-s/sp.Integer(64),0,0,s+t)),s,t)
prior580=[
 '87518285/21743271936','89759141/5435817984',
 '1656329771/65229815808','35360777/2038431744',
 '434651857/97844723712']
assert YGate.as_expr()==sum(sp.Rational(v)*s**(4-k)*t**k for k,v in enumerate(prior580))
assert orig6(1,1,1,1,1,1,0)==0
def one_axis_gate_poly(i):
    aa,bb=sp.symbols('aa bb')
    v=[sp.Integer(0)]*7
    v[i-1]=aa;v[6]=bb
    return sp.Poly(sp.expand(orig6(*v)),aa,bb)
family={}
for i in range(1,7):
    pol=one_axis_gate_poly(i)
    family[str(i)]={f'{4-j},{j}':str(pol.coeff_monomial((4-j,j))) for j in range(5)}
assert family['1']==family['3'] and family['2']==family['4'] and family['5']==family['6']
assert family['1']!=family['2'] and family['1']!=family['5'] and family['2']!=family['5']

C={k:v for k,v in Pfull.terms()}
def c_at(e):return C.get(tuple(e),sp.Integer(0))
M=sp.zeros(6,6)
for i in range(5):
    for j in range(5):
        e=[0]*6;e[i]=1;e[j]+=1;e[5]=2
        M[i,j]=c_at(e)/(6 if i==j else 12)
for i in range(5):
    M[i,5]=-sum(M[i,j] for j in range(5))
    M[5,i]=M[i,5]
M[5,5]=sum(M[i,j] for i in range(5) for j in range(5))
assert M==M.T and M*sp.ones(6,1)==sp.zeros(6,1)
assert M.rank()==5 and M[:5,:5].det()!=0
assert M[4,5]==sp.Rational(-7031,56623104)
assert M[4,4]==sp.Rational(39167,169869312)
V=sp.zeros(6,1)
for i in range(5):
    e=[0]*6;e[i]=1;e[5]=3
    V[i]=c_at(e)/4
V[5]=-sum(V[i] for i in range(5))
assert sum(V)==0 and V[4]==sp.Rational(-3378511,6115295232)

out={
 'schema':'ENTERPRISE_MATH_PREFIX581_R2_COMPLETE_NATIVE_SEVEN_OBSERVER_QUARTIC_V1',
 'research_state':'AUTHOR_SIDE_EXACT_RATIONAL_PROOF_UNREVIEWED',
 'frozen_science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'basis':['R1','R2','R3','R4','R5','K'],
 'original_sixth_axis_recovery':'R6=d-R1-R2-R3-R4-R5',
 'poly_degree':4,'simplex_grid_size':len(values),
 'polynomial_nonzero_monomials':len(Pfull.terms()),
 'cyclic_graph_classes':[colors.count(0),colors.count(1)],
 'quartic_slice_Ri_Rj_K_K':[[str(x) for x in row] for row in M.tolist()],
 'quartic_slice_Ri_K_K_K':[str(x) for x in V],
 'quartic_slice_rank':M.rank(),
 'quartic_slice_principal_minor_1_to_5':str(M[:5,:5].det()),
 'simplex_grid_directional_values':{'/'.join(map(str,k)):str(val) for k,val in values.items()},
 'homogeneous_quartic_monomials':{'/'.join(map(str,k)):str(val) for k,val in Pfull.terms()},
 'newton_coefficients':{'/'.join(map(str,k)):str(val) for k,val in DELTA.items()},
 'one_axis_gate_polynomials_coeff_of_ai^(4-j)_b^j':family,
 'heldout':{name:str(Pfull.eval(dict(zip(y,v)))) for name,v in heldout.items()},
 'checks':[
  '96 ports x 6 labelled actions original BRC edge semantics',
  'exact 96x96 Z inverse',
  '126 independently evaluated rational quartic rates',
  'exact Newton interpolation and 126 grid matches',
  'four direct out-of-grid checks including sum-zero',
  'PREFIX579 full (R5,R6,K) polynomial',
  'PREFIX580 full (Y,K) polynomial',
  'six-axis deterministic identity',
  'three gate-coupling axis families',
  'K^2 slice rank five and row sums zero',
  '96-port strong connectivity, period two',
  'no floating point computation'
 ],
 'status':'ALL_ASSERTIONS_PASS'
}
Path(__file__).with_name(
 'PREFIX581_R2_complete_six_axis_gate_quartic_certificate.json'
).write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('ALL_ASSERTIONS_PASS',len(Pfull.terms()))
