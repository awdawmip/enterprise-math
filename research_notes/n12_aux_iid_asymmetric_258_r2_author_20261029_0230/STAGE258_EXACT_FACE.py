#!/usr/bin/env python3
"""Stage258 complete exact five-vertex Bellman contact-face certificate.

External ternary IID, N=12, full ordered-history randomized policy class.
All proof-critical arithmetic: Python stdlib Fraction; no numeric solver.
"""
from fractions import Fraction as F

N=12
P=(F(1,8),F(1,24),F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
LP=F(644972544,8007455)
LQ=F(418575732,8007455)
STATES=tuple((i,j,d-i-j) for d in range(N+1) for i in range(d+1)
             for j in range(d-i+1))
assert len(STATES)==455

def child(s,z):
    return tuple(s[k]+(k==z) for k in range(3))

def likelihood(s):
    return F(2,3)**s[0] * F(2)**s[1]

# Bellman inequality in P-labelled mass for tQ+LP eP+LQ eQ.
H,OPT={},{}
action_costs=strict_gaps=0
for s in reversed(STATES):
    op={'P':LQ*likelihood(s),'Q':LP}
    if sum(s)<N:
        op['C']=likelihood(s)+sum(P[z]*H[child(s,z)] for z in range(3))
    h=min(op.values())
    H[s]=h
    OPT[s]=tuple(a for a in ('P','Q','C') if a in op and op[a]==h)
    action_costs+=len(op)
    strict_gaps+=sum(x>h for x in op.values())
assert action_costs==1274 and strict_gaps==808
TIES={(0,0,k) for k in range(2,N)} | {(0,1,2)}
assert {s for s in STATES if len(OPT[s])>1}==TIES
assert all(OPT[(0,0,k)]==('P','C') for k in range(2,N))
assert OPT[(0,1,2)]==('Q','C')
assert OPT[(0,0,0)]==OPT[(0,0,1)]==('C',)
assert OPT[(0,0,N)]==('P',)
H0=H[(0,0,0)]
assert H0==F(30134718329,576536760)

# Neutral-prefix cutoff k (2..12), and unique nonneutral tie at (0,1,2).
# D(k,Q/C) uses only Bellman-minimal actions.
def action(s,k,mode):
    if s[0]==s[1]==0:
        return 'P' if sum(s)>=k else 'C'
    if s==(0,1,2):
        return mode
    return OPT[s][0]

def suffix(k,mode):
    obs={}
    for s in reversed(STATES):
        a=action(s,k,mode)
        if a=='P':obs[s]=(F(0),F(1),F(0),F(0))
        elif a=='Q':obs[s]=(F(1),F(0),F(0),F(0))
        else:
            childobs=[obs[child(s,z)] for z in range(3)]
            obs[s]=(
                sum(P[z]*childobs[z][0] for z in range(3)),
                sum(Q[z]*childobs[z][1] for z in range(3)),
                1+sum(P[z]*childobs[z][2] for z in range(3)),
                1+sum(Q[z]*childobs[z][3] for z in range(3)))
    return obs[(0,0,0)]

# Deliberately unmerged complete ordered-history DFS propagating P/Q masses.
def ordered_dfs(k,mode):
    obs=[F(0)]*4
    terminal=[F(0),F(0)]
    nodes=leaves=0
    def go(hist,pm,qm):
        nonlocal nodes,leaves
        nodes+=1
        s=(hist.count(0),hist.count(1),hist.count(2))
        a=action(s,k,mode)
        if a=='C':
            obs[2]+=pm
            obs[3]+=qm
            for z in range(3):
                go(hist+(z,),pm*P[z],qm*Q[z])
        else:
            leaves+=1
            terminal[0]+=pm
            terminal[1]+=qm
            if a=='P':obs[1]+=qm
            else:obs[0]+=pm
    go((),F(1),F(1))
    assert terminal==[F(1),F(1)]
    return tuple(obs),nodes,leaves

V={}
total_nodes=total_leaves=0
for k in range(2,N+1):
    for mode in ('Q','C'):
        v=suffix(k,mode)
        w,n,l=ordered_dfs(k,mode)
        assert v==w,(k,mode)
        V[(k,mode)]=v
        total_nodes+=n
        total_leaves+=l
        assert v[3]>v[2]
        assert v[3]+LP*v[0]+LQ*v[1]==H0

# Four-observer branch difference includes correct order/provenance multiplicity.
DELTA=tuple(V[(3,'C')][i]-V[(3,'Q')][i] for i in range(4))
assert DELTA==(
    -F(135736825,15479341056),F(51756025,5804752896),
    F(88211975,644972544),F(116205575,483729408))
assert tuple(V[(2,'C')][i]-V[(2,'Q')][i] for i in range(4))==tuple(F(2,3)*d for d in DELTA)
assert all(tuple(V[(k,'C')][i]-V[(k,'Q')][i] for i in range(4))==DELTA
           for k in range(3,N+1))

def cross(o,a,b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])

def on_segment(u,a,b):
    if cross(a,b,u)!=0:return False
    if b[0]==a[0]:raise ValueError('vertical comparison not handled')
    t=(u[0]-a[0])/(b[0]-a[0])
    return F(0)<=t<=F(1) and all(u[i]==a[i]+t*(b[i]-a[i]) for i in range(4))

# The entire equality-policy error hull is five vertices; all other policies
# lie on the two indicated segments (the k=2 C point is a separate vertex).
Q2,Q12=V[(2,'Q')],V[(12,'Q')]
C2,C3,C12=V[(2,'C')],V[(3,'C')],V[(12,'C')]
for k in range(2,N+1):
    assert on_segment(V[(k,'Q')],Q2,Q12)
    if k>=3: assert on_segment(V[(k,'C')],C3,C12)
POLYGON=(C2,C3,C12,Q12,Q2)
assert all(cross(POLYGON[i],POLYGON[(i+1)%5],POLYGON[(i+2)%5])>0 for i in range(5))
AREA=abs(sum(POLYGON[i][0]*POLYGON[(i+1)%5][1]-
             POLYGON[i][1]*POLYGON[(i+1)%5][0] for i in range(5)))/2
assert AREA==F(245333081919015625,202170937101722320896)
EDGE=2*Q2[0]+Q2[1]
assert EDGE==2*Q12[0]+Q12[1]==F(22960038649,23219011584)
assert all(2*w[0]+w[1]<EDGE for w in (C2,C3,C12))
# Two exact endpoint vertices coincide with Stage257's U2--U3 edge.
assert Q2==(F(1011440903,15479341056),F(4981428985,5804752896),
            F(1298095367,644972544),F(1038314759,483729408))
assert Q12==(F(29383188527,139314069504),F(9874231855,17414258688),
             F(31963078703,5804752896),F(8184999377,1451188224))

# Strict outside-Stage257 cap point; *independently* specified two tie coins.
A=F(12018216825031,87071293440000)
B=F(7754698736957,10883911680000)
assert EDGE-(2*A+B)==F(3,10000)
u=F(3702061401486841727,7541641324012500000)  # stop after 3 neutrals vs continue to 8
v=F(120762919703,125116484375)  # decide Q vs continue at (0,1,2)
assert F(0)<u<1 and F(0)<v<1
w3q,w3c,w8q,w8c=u*v,u*(1-v),(1-u)*v,(1-u)*(1-v)
assert w3q+w3c+w8q+w8c==1 and min(w3q,w3c,w8q,w8c)>0
M=tuple(w3q*V[(3,'Q')][i]+w3c*V[(3,'C')][i]+w8q*V[(8,'Q')][i]+w8c*V[(8,'C')][i] for i in range(4))
assert M==(A,B,F(109497793172713451801,29050811000524800000),
           F(28372647518343096989,7262702750131200000))
assert M[3]>M[2]
assert M[3]==H0-LP*A-LQ*B
assert all(suffix(k,mode)==ordered_dfs(k,mode)[0] for k,mode in ((3,'Q'),(3,'C'),(8,'Q'),(8,'C')))

if __name__=='__main__':
    print('STAGE258_EXACT_ALL_REAL_FACE_PASS')
    print('states',len(STATES),'actions',action_costs,'strict_gaps',strict_gaps,'ties',len(TIES))
    print('dual LP',LP,'LQ',LQ,'thetaQ=1','Hroot',H0)
    for label,vec in zip(('C2','C3','C12','Q12','Q2'),POLYGON):
        print(label,*[str(v) for v in vec])
    print('delta',*[str(d) for d in DELTA],'delta_k2_factor',F(2,3))
    print('area',AREA,'shared_edge_2a_plus_b',EDGE)
    print('target_a,b',A,B,'outside_previous_support',EDGE-2*A-B)
    print('coins',u,v,'weights',w3q,w3c,w8q,w8c)
    print('optimal_observers',*[str(x) for x in M])
    print('ordered_nodes',total_nodes,'terminal_branches',total_leaves)
    print('STAGE258_PROOF_CERTIFICATE_PASS')
