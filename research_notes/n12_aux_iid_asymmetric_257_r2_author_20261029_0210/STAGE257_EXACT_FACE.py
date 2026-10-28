#!/usr/bin/env python3
"""Exact finite certificate, Stage257 (external ternary IID, N=12).

Reproduces the Bellman support, 24 deterministic contact policies,
complete ordered-history P/Q source mass observations, exact five-vertex
contact polygon, and a feasible strict-exterior rational cap pair.
Only Python stdlib Fraction is used for all proof-bearing arithmetic.
"""
from fractions import Fraction as F

N = 12
P = (F(1, 8), F(1, 24), F(5, 6))
Q = (F(1, 12), F(1, 12), F(5, 6))
LP = F(3869835264, 48435355)
LQ = F(2516141892, 48435355)
STATES = tuple((i,j,d-i-j) for d in range(N+1)
               for i in range(d+1) for j in range(d-i+1))
assert len(STATES) == 455

def child(s,z):
    return tuple(s[t]+(t==z) for t in range(3))

def likelihood(s):
    return F(2,3)**s[0] * F(2)**s[1]

# Bellman inequality for tQ + LP*eP + LQ*eQ (P-normalized)
H, actions = {}, {}
num_costs = num_strict = 0
for s in reversed(STATES):
    candidates = {'P': LQ*likelihood(s), 'Q': LP}
    if sum(s) < N:
        candidates['C'] = (likelihood(s) +
                           sum(P[z]*H[child(s,z)] for z in range(3)))
    m = min(candidates.values())
    H[s] = m
    actions[s] = tuple(k for k in ('P','Q','C')
                       if k in candidates and candidates[k] == m)
    num_costs += len(candidates)
    num_strict += sum(v > m for v in candidates.values())
assert num_costs == 1274 and num_strict == 807
expected_ties = {(0,0,k) for k in range(1,N)} | {(0,1,1)}
assert {s for s in STATES if len(actions[s]) > 1} == expected_ties
assert all(actions[(0,0,k)] == ('P','C') for k in range(1,N))
assert actions[(0,1,1)] == ('Q','C')
assert actions[(0,0,0)] == ('C',)
assert actions[(0,0,12)] == ('P',)
H0 = H[(0,0,0)]
assert H0 == F(90579154987, 1743672780)
assert 1 + LP/F(24) == LQ/F(12)  # neutral P / continue tie

# Exactly 24 count-state pure optimal policies (k=1..12, mode=Q/C).
def action(s,k,mode):
    if s[0] == 0 and s[1] == 0:
        return 'P' if sum(s) >= k else 'C'
    if s == (0,1,1):
        return mode
    return actions[s][0]

def count_dp(k,mode):
    obs = {}
    for s in reversed(STATES):
        act = action(s,k,mode)
        if act == 'P': obs[s] = (F(0), F(1), F(0), F(0))
        elif act == 'Q': obs[s] = (F(1), F(0), F(0), F(0))
        else:
            vs = [obs[child(s,z)] for z in range(3)]
            obs[s] = (sum(P[z]*vs[z][0] for z in range(3)),
                      sum(Q[z]*vs[z][1] for z in range(3)),
                      1+sum(P[z]*vs[z][2] for z in range(3)),
                      1+sum(Q[z]*vs[z][3] for z in range(3)))
    return obs[(0,0,0)]

def ordered_dfs(k,mode):
    out = [F(0) for _ in range(4)]
    terminal = [F(0), F(0)]
    nodes = leaves = 0
    def visit(h, pm, qm):
        nonlocal nodes, leaves
        nodes += 1
        s = (h.count(0),h.count(1),h.count(2))
        act = action(s,k,mode)
        if act == 'C':
            out[2] += pm
            out[3] += qm
            for z in range(3):
                visit(h+(z,),pm*P[z],qm*Q[z])
        else:
            leaves += 1
            terminal[0] += pm
            terminal[1] += qm
            if act == 'P': out[1] += qm
            else: out[0] += pm
    visit((),F(1),F(1))
    assert terminal == [F(1),F(1)],terminal
    return tuple(out), nodes, leaves

V={}
nodes_total=leaves_total=0
for k in range(1,N+1):
    for mode in ('Q','C'):
        v = count_dp(k,mode)
        w,n,l = ordered_dfs(k,mode)
        assert v == w,(k,mode)
        nodes_total += n
        leaves_total += l
        assert v[3] >= v[2]
        assert v[3] + LP*v[0] + LQ*v[1] == H0
        V[(k,mode)] = v

# Q-mode policies are exactly Stage256's C_k policies, verified at endpoints.
assert V[(1,'Q')] == (F(1743753479,46438023168),
                       F(16033302265,17414258688),
                       F(2066239751,1934917632),
                       F(1622821127,1451188224))
assert V[(12,'Q')] == (F(30348774917,139314069504),
                        F(9753923645,17414258688),
                        F(31316233733,5804752896),
                        F(7902199747,1451188224))

DELTA = tuple(V[(2,'C')][t]-V[(2,'Q')][t] for t in range(4))
DELTA_HALF = tuple(V[(1,'C')][t]-V[(1,'Q')][t] for t in range(4))
assert DELTA_HALF == tuple(x/2 for x in DELTA)
assert all(tuple(V[(k,'C')][t]-V[(k,'Q')][t] for t in range(4)) == DELTA
           for k in range(2,N+1))
assert DELTA[0] < 0 < DELTA[1]
assert DELTA[3] > DELTA[2]

def cross(a,b,c):
    return ((b[0]-a[0])*(c[1]-a[1])-
            (b[1]-a[1])*(c[0]-a[0]))

Q1,Q12 = V[(1,'Q')],V[(12,'Q')]
C2,C12 = V[(2,'C')],V[(12,'C')]
# Every Q_k is on segment Q1--Q12, every C_k (k>=2) on C2--C12.
for k in range(1,N+1):
    u=V[(k,'Q')]
    assert cross(Q1,Q12,u) == 0 and Q1[0] <= u[0] <= Q12[0]
    w=(u[0]-Q1[0])/(Q12[0]-Q1[0])
    assert F(0) <= w <= F(1)
    assert all(u[t]==Q1[t]+w*(Q12[t]-Q1[t]) for t in range(4))
    if k>=2:
        u=V[(k,'C')]
        assert cross(C2,C12,u) == 0 and C2[0] <= u[0] <= C12[0]
        w=(u[0]-C2[0])/(C12[0]-C2[0])
        assert F(0) <= w <= F(1)
        assert all(u[t]==C2[t]+w*(C12[t]-C2[t]) for t in range(4))

# All and only equality policies generate this pentagon in the (eP,eQ) plane.
POLYGON = (V[(1,'C')],C2,C12,Q12,Q1)
turns=[cross(POLYGON[i],POLYGON[(i+1)%5],POLYGON[(i+2)%5])
       for i in range(5)]
assert all(x>0 for x in turns)
AREA=abs(sum(POLYGON[i][0]*POLYGON[(i+1)%5][1]-
             POLYGON[i][1]*POLYGON[(i+1)%5][0]
             for i in range(5)))/2
assert AREA == F(361875536423559625,303256405652583481344)
for v in V.values():
    assert v[3]-v[2]>0

# The Stage256 opposite edge Q1--Q12 is an entire shared edge.
EDGE=2*Q1[0]+Q1[1]
assert EDGE == 2*Q12[0]+Q12[1]
assert all(2*v[0]+v[1]<EDGE for v in POLYGON[:3])

# Concrete rational caps across that edge, strictly inside Stage257 pentagon.
TARGET_A=(Q1[0]+Q12[0])/2-F(1,10000)
TARGET_B=(Q1[1]+Q12[1])/2-F(1,10000)
assert (TARGET_A,TARGET_B) == (
    F(11110053918781,87071293440000),
    F(2685806568569,3627970560000))
assert EDGE - (2*TARGET_A+TARGET_B) == F(3,10000)

# An explicit 3-point mixed strategy, with strictly positive exact weights.
W3 = F(47417565732639347237,61486950094953906250)
W12= F(11416570966257880613,61486950094953906250)
WC = F(6530347008,151360484375)
assert W3+W12+WC==1 and min(W3,W12,WC)>0
MIX = tuple(W3*V[(3,'Q')][t]+W12*V[(12,'Q')][t]+WC*V[(12,'C')][t]
            for t in range(4))
assert MIX[:2] == (TARGET_A,TARGET_B)
assert MIX[3] > MIX[2]
assert MIX[3] == H0-LP*TARGET_A-LQ*TARGET_B
assert MIX[3] == F(48250126915010865853,14643503500262400000)

if __name__=='__main__':
    print('STAGE257_EXACT_ALL_REAL_FACE_PASS')
    print('states',len(STATES),'action_costs',num_costs,
          'strict_positive_gaps',num_strict,'tie_states',len(expected_ties))
    print('dual LP',LP,'LQ',LQ,'thetaP=0 thetaQ=1 Hroot',H0)
    print('polygon_vertex_order C1star C2star C12star Q12 Q1')
    for name,v in zip(('C1star','C2star','C12star','Q12','Q1'),POLYGON):
        print(name,' '.join(str(x) for x in v))
    print('delta_full',' '.join(str(x) for x in DELTA))
    print('delta_half',' '.join(str(x) for x in DELTA_HALF))
    print('area',AREA)
    print('shared_edge_2a_plus_b',EDGE)
    print('target_caps',TARGET_A,TARGET_B,'outside_old_side',EDGE-2*TARGET_A-TARGET_B)
    print('root_weights',W3,W12,WC)
    print('optimal_observers',' '.join(str(x) for x in MIX))
    print('ordered_nodes',nodes_total,'terminal_branches',leaves_total)
    print('STAGE257_PROOF_CERTIFICATE_PASS')
