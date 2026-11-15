#!/usr/bin/env python3
"""Exact BRC S23 author certificate: W4 finite repair and irrational diagonal obstruction.
No external libraries; run python VERIFY_BRC_F4_REPAIR_DIAGONAL.py.
"""
from fractions import Fraction as F
from itertools import combinations
import json

N = 16800000
LIMIT = 6*N//5
M = ((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),
     (0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20))
A=(0,0,0,1,1,1); B=(2,2,3,2,2,4); C=(5,6,7,8,9,10); G=(0,0,1,2,2,3)
PAIRS=("34 24 34 24","34 23 34 34","34 34 34 23","24 24 12 12",
       "12 13 23 24","23 34 12 13","24 34 12 14")
FREE=("53/80 0 27/80 0;1 0 0 0;1/15 1/15 2/5 7/15;1/15 0 2/5 8/15",
      "2/5 0 2/5 1/5;2/5 2/5 0 1/5;2/5 1/5 0 2/5;3/5 2/5 0 0",
      "3/5 2/5 0 0;2/5 2/5 1/5 0;1/3 43/105 3/35 6/35;1/7 2/35 2/5 2/5")
NAMES=("D1","D2","D3","D4","D6","D7","D8","K1r","K2r","K3r")

def scaled(s):
    r=F(s)*N
    assert r.denominator==1, (s,r)
    return r.numerator

def mix(rows):
    out=[]
    for ws in M:
        row=[]
        for j in range(4):
            t=sum(ws[k]*rows[k][j] for k in range(6))
            assert t%20==0
            row.append(t//20)
        assert sum(row)==N and min(row)>=0
        out.append(tuple(row))
    return tuple(out)

def decoder(rows):
    assert all(len(r)==4 and sum(r)==N and min(r)>=0 for r in rows)
    return mix(tuple(rows[G[k]] for k in range(6)))

def pair(s):
    return decoder([[N*word.count(str(j))//2 for j in range(1,5)] for word in s.split()])

def free(s):
    return decoder([[scaled(p) for p in row.split()] for row in s.split(';')])

BANK=tuple(pair(s) for s in PAIRS)+tuple(free(s) for s in FREE)
assert len(BANK)==10

def prepare(z):
    zz=[scaled(x) for x in z]
    assert len(zz)==11 and min(zz)>=0 and max(zz)<=N
    src=[]
    for a,b,c in zip(A,B,C):
        x=zz[a]; y=zz[b]; w=zz[c]
        assert ((N-x)*y)%N==0 and ((N-x)*(N-y))%N==0
        mid=(N-x)*y//N; tail=(N-x)*(N-y)//N
        assert (tail*w)%N==0
        last=tail*w//N
        src.append((x,mid,last,tail-last))
    return mix(src)

def risk2(p,q):
    return max(sum(abs(a-b) for a,b in zip(u,v)) for u,v in zip(p,q))

def minimum(p,bank=BANK):return min(risk2(p,q) for q in bank)

RAW={
 'W':[1,0,0,0,1,0,0,0,0,0,0], 'J':[1,'1/3',0,0,0,0,0,0,0,1,0],
 'A':['1/7',1,0,0,0,0,1,1,1,0,1], 'B':[1,'1/7',0,0,0,0,1,1,1,0,1],
 'C':['1/7',1,0,0,0,1,0,0,0,0,0], 'X':[1,'1/15',0,0,0,0,1,1,1,0,1],
 'Y':[1,0,0,0,0,0,0,0,1,1,1], 'Z':[0,1,0,1,0,1,1,0,0,0,0],
}
for k,s in enumerate(("00000000000","00000001000","00000000001","00101000000",
                      "00110000000","00101001000","00100000001","00100000000"),1):
    RAW['T'+str(k)]=[int(d) for d in s]
RAW['U']=[int(d) for d in '00110000001']
RAW['V']=[int(d) for d in '10000000000']
RAW['H']=['1/4',1,0,0,0,1,0,0,0,0,0]
RAW['Hm']=['1/5',1,0,0,0,1,0,0,0,0,0]
assert len(RAW)==20

def J(t):return prepare([1,t,0,0,0,0,0,0,0,1,0])
def F3(s,t,u):return prepare([s,t,u,0,0,1,0,0,0,0,0])
W4=prepare(['1/3',0,1,'1/2',0,1,0,0,0,0,0])
old_max=max(minimum(prepare(z)) for z in RAW.values())
assert old_max==LIMIT
assert minimum(W4)==LIMIT
w4_risks=[risk2(W4,q) for q in BANK]

edge_indices=[]
for a in range(5):
    pts=(J(F(a,5)),J(F(a+1,5)))
    worst=[max(risk2(p,q) for p in pts) for q in BANK]
    val=min(worst); assert val<=LIMIT, (a,val)
    edge_indices.append(worst.index(val))

# Exact finite grid only: the grid does not establish full 3D coverage.
grid_count=0; grid_worst=0; grid_hits=[0]*10
for a in range(21):
    for b in range(21):
        for c in range(21):
            p=F3(F(a,20),F(b,20),F(c,20))
            risks=[risk2(p,q) for q in BANK]
            v=min(risks)
            assert v<=LIMIT,(a,b,c,v)
            grid_count+=1; grid_worst=max(grid_worst,v);grid_hits[risks.index(v)]+=1
assert grid_count==9261 and grid_worst==LIMIT

# Ten-strategy incompatibility certificate (strict < 3/5 lower bound).
P=[prepare(RAW[n]) for n in ('W','X','Y','Z','T5','U','V','Hm')]+[J(1),J(F(1,5))]
assert all(minimum(p,BANK[:7])>=LIMIT for p in P)
forbidden=[]
for a,b,c in combinations(range(10),3):
    w=max(sum(max(P[z][i][j] for z in (a,b,c)) for j in range(4))-N for i in range(6))
    if 5*w>=9*N:forbidden.append((a,b,c))
assert len(forbidden)==84
min_hits=100000
for n in range(3**10):
    labels=[]; t=n
    for i in range(10):labels.append(t%3);t//=3
    hits=sum(labels[a]==labels[b]==labels[c] for a,b,c in forbidden)
    assert hits>=1,n
    min_hits=min(min_hits,hits)
assert min_hits==1

# Completely rational diagonal witness: x=19/50, s=u=x, t=v=0.
x=F(19,50)
diagonal=F3(x,0,x)
risks=[risk2(diagonal,q) for q in BANK]
assert risks[0]==scaled(F(1539,2500))*2 and all(
    v==scaled(F(31,50))*2 for v in (risks[4],risks[6],risks[7],risks[9]))
assert min(risks)==scaled(F(1539,2500))*2>LIMIT

# Polynomial certificate on the full real diagonal interval [1/3, 2/5].
# p(x)-q has degree <=2. Use exact values at 0,+1,-1 to recover coefficients.
def rprepare(z):
    src=[]
    for a,b,c in zip(A,B,C):
        xx=F(z[a]);bb=F(z[b]);cc=F(z[c])
        src.append((xx,(1-xx)*bb,(1-xx)*(1-bb)*cc,(1-xx)*(1-bb)*(1-cc)))
    return tuple(tuple(sum(F(M[i][k],20)*src[k][j] for k in range(6)) for j in range(4)) for i in range(6))

def pdiag(x):return rprepare([x,0,x,0,0,1,0,0,0,0,0])

def pval(p,x):return p[0]+p[1]*x+p[2]*x*x

def pminus(a,b):return tuple(a[i]-b[i] for i in range(3))

def prange(p):
    lo=F(1,3);hi=F(2,5)
    pts=[lo,hi]
    if p[2]:
        m=-p[1]/(2*p[2])
        if lo<=m<=hi:pts.append(m)
    v=[pval(p,t) for t in pts]
    return min(v),max(v)

samples=[pdiag(v) for v in (0,1,-1)]
TARGET=((0,2,-1),(1,0,0),(1,0,0),(1,0,0),
        (1,-1,0),(1,0,0),(1,-1,0),(1,-1,0),(1,0,0),(1,-1,0))
symbolic_event_checks=0;symbolic_equal_events=0
for d,q in enumerate(BANK):
    equal_event=False
    for i in range(6):
        components=[]
        for j in range(4):
            v0=samples[0][i][j]-F(q[i][j],N)
            v1=samples[1][i][j]-F(q[i][j],N)
            vm=samples[2][i][j]-F(q[i][j],N)
            components.append((v0,(v1-vm)/2,(v1+vm)/2-v0))
        for mask in range(1,15):
            event=tuple(sum((components[j][k] for j in range(4) if (mask>>j)&1),F(0)) for k in range(3))
            mn,mx=prange(pminus(TARGET[d],event))
            assert mn>=0,(d,i,mask,TARGET[d],event,mn,mx)
            symbolic_event_checks+=1
            if event==tuple(F(v) for v in TARGET[d]):equal_event=True;symbolic_equal_events+=1
    assert equal_event, d

result={
 'pass':'PASS_BRC_S23_W4_REOPT_FINITE_GRID_AND_GOLDEN_DIAGONAL_20261102',
 'source_pin':'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
 'quantifier':'seven specified fixed kernels; optimize three real stochastic kernels over S20+J(real)+G20+W4',
 'finite_old_policies':len(RAW),'added_witness':'W4=F4(1/3,0,1,1/2)',
 'kernel_rows':FREE,'old_policies_max_min_tv':'3/5','w4_min_tv':'3/5',
 'w4_per_decoder_risk2':w4_risks,'five_J_segment_decoder_indices':edge_indices,
 'F3_grid_denominator':20,'F3_grid_vertices':grid_count,'F3_grid_max_min_tv':'3/5',
 'grid_selected_decoder_counts':dict(zip(NAMES,grid_hits)),
 'lower_core':('W','X','Y','Z','T5','U','V','Hm','J(1)','J(1/5)'),
 'forbidden_triples':len(forbidden),'three_labels_checked':3**10,'minimum_monochromatic_forbidden_triples':min_hits,
 'diagonal_interval':'[1/3,2/5]','diagonal_risk_formula':'min(2*x-x*x,1-x)',
 'diagonal_unique_maximizer':'(3-sqrt(5))/2', 'diagonal_maximum':'(sqrt(5)-1)/2',
 'diagonal_rational_witness':'F3(19/50,0,19/50)','rational_witness_risk':'1539/2500',
 'diagonal_exact_event_inequalities':symbolic_event_checks,'diagonal_exact_equal_events':symbolic_equal_events,
 'full_F3_continuum_certified':False, 'full_F4_continuum_reoptimized':False,
 'scientific_status':'author exact-arithmetic certificate and analytic derivation; independent review and native Result pending'
}
print(json.dumps(result,ensure_ascii=False,indent=2))
