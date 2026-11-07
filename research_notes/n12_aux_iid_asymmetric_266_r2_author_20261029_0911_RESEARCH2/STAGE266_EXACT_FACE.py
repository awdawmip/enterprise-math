#!/usr/bin/env python3
"""Stage266 exact N=12 ternary IID Bellman/ordered-history certificate.

Entire proof check uses only Python standard library Fraction arithmetic.  No
floating-point inference, external theorem assumptions, or signed mass model.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, product
from math import factorial

N = 12
P = (F(1, 8), F(1, 24), F(5, 6))
Q = (F(1, 12), F(1, 12), F(5, 6))
a = F(4693965992729, 58047528960000)
b = F(26764770235, 34828517376)
lamP = F(12729920, 136697)
lamQ = F(7907076, 136697)
STATES = tuple((i, j, n-i-j) for n in range(N+1)
               for i in range(n+1) for j in range(n-i+1))
ZERO = (0, 0, 0)
T1, T2 = (0, 0, 5), (0, 1, 10)

def child(s, z):
    t = list(s)
    t[z] += 1
    return tuple(t)

pm = {s: P[0]**s[0] * P[1]**s[1] * P[2]**s[2] for s in STATES}
qm = {s: Q[0]**s[0] * Q[1]**s[1] * Q[2]**s[2] for s in STATES}

def exact_bellman():
    H, costs, tied = {}, {}, {}
    for s in reversed(STATES):
        d = {'P': lamQ * qm[s], 'Q': lamP * pm[s]}
        if sum(s) < N:
            d['C'] = qm[s] + sum(H[child(s, z)] for z in range(3))
        costs[s] = d
        H[s] = min(d.values())
        tied[s] = tuple(k for k, v in d.items() if v == H[s])
    return H, costs, tied

H, action_costs, allowed = exact_bellman()
assert len(STATES) == 455
assert sum(map(len, action_costs.values())) == 1274
TIES = {s: acts for s, acts in allowed.items() if len(acts) > 1}
assert TIES == {T1: ('P', 'C'), T2: ('Q', 'C')}, TIES
GAPS = [v-H[s] for s, costs in action_costs.items() for v in costs.values() if v > H[s]]
assert len(GAPS) == 817
assert len(GAPS) + sum(map(len, allowed.values())) == 1274
assert H[ZERO] == F(11494057433, 199304226)

def policy(bits):
    d = {s: allowed[s][0] for s in STATES}
    d[T1] = ('P', 'C')[bits[0]]
    d[T2] = ('Q', 'C')[bits[1]]
    return d

def from_counts(pi):
    """Combinatorial count-state propagation, each count carries order multiplicity."""
    flow = defaultdict(F)
    flow[ZERO] = F(1)
    eP=eQ=tP=tQ=massP=massQ=F(0)
    for s in STATES:
        f=flow[s]
        if f == 0: continue
        decision=pi[s]
        if decision=='C':
            assert sum(s)<N
            tP += f*pm[s]
            tQ += f*qm[s]
            for z in range(3): flow[child(s,z)] += f
        else:
            massP += f*pm[s];massQ += f*qm[s]
            if decision == 'P': eQ += f*qm[s]
            elif decision == 'Q': eP += f*pm[s]
            else: raise AssertionError(decision)
    assert massP == massQ == 1
    return (eP,eQ,tP,tQ)

def ordered_history_dfs(pi):
    """Independent recursive enumeration of actual ordered paths and P/Q weights."""
    totals = {'eP':F(0),'eQ':F(0),'tP':F(0),'tQ':F(0),
              'massP':F(0),'massQ':F(0),'nodes':0,'leaves':0}
    def visit(s,probP,probQ):
        totals['nodes']+=1
        decision=pi[s]
        if decision=='C':
            assert sum(s)<N
            totals['tP']+=probP
            totals['tQ']+=probQ
            for z in range(3):visit(child(s,z),probP*P[z],probQ*Q[z])
        else:
            totals['leaves']+=1
            totals['massP']+=probP
            totals['massQ']+=probQ
            if decision=='P':totals['eQ']+=probQ
            else: totals['eP']+=probP
    visit(ZERO,F(1),F(1))
    assert totals['massP']==totals['massQ']==1
    return (totals['eP'],totals['eQ'],totals['tP'],totals['tQ']),totals

def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])

def hull(ids, vectors):
    points=sorted(((vectors[t][0],vectors[t][1],t) for t in ids))
    low=[]
    for p in points:
        while len(low)>=2 and cross(low[-2],low[-1],p)<=0:low.pop()
        low.append(p)
    up=[]
    for p in reversed(points):
        while len(up)>=2 and cross(up[-2],up[-1],p)<=0:up.pop()
        up.append(p)
    return low[:-1]+up[:-1]

def barycentric(ids, vectors, caps):
    u,v,w=[vectors[k] for k in ids]
    x,y=caps
    D=(v[0]-u[0])*(w[1]-u[1])-(v[1]-u[1])*(w[0]-u[0])
    if D==0:return None
    t=((x-u[0])*(w[1]-u[1])-(y-u[1])*(w[0]-u[0]))/D
    h=((v[0]-u[0])*(y-u[1])-(v[1]-u[1])*(x-u[0]))/D
    return (1-t-h,t,h)

vectors={};history=[]
for bits in product((0,1),repeat=2):
    x=from_counts(policy(bits))
    y,meta=ordered_history_dfs(policy(bits))
    assert x==y
    assert lamP*x[0]+lamQ*x[1]+x[3]==H[ZERO]
    vectors[bits]=x
    history.append(meta)
assert len(set((v[0],v[1]) for v in vectors.values()))==4
for v in vectors.values():assert v[3] > v[2],v

# Cross-check the full Stage265 source-aware edge as four-observer vectors.
I5=(F(1763120017,23219011584),F(6802983965,8707129344),
    F(4453822913,967458816),F(3922172551,725594112))
I6=(F(443710351,5159780352),F(1462089145,1934917632),
    F(3279966317,644972544),F(960037303,161243136))
assert I5 in vectors.values() and I6 in vectors.values()

pts = hull(list(vectors),vectors)
assert len(pts)==4
area = sum(pts[i][0]*pts[(i+1)%4][1]-pts[i][1]*pts[(i+1)%4][0] for i in range(4))/2
assert area > 0
assert all(cross(pts[i],pts[(i+1)%4],pts[(i+2)%4])>0 for i in range(4))
mixtures=[]
for ids in combinations(vectors,3):
    weights=barycentric(ids,vectors,(a,b))
    if weights is not None and all(x>0 for x in weights):
        mixtures.append((ids,weights))
assert mixtures, 'No strictly positive rational primal mixture at requested caps'
ids, weights=mixtures[0]
assert sum(weights)==1
obs=tuple(sum(weights[j]*vectors[ids[j]][i] for j in range(3)) for i in range(4))
assert (obs[0],obs[1])==(a,b)
assert obs[3]>obs[2]
V=H[ZERO]-lamP*a-lamQ*b
assert V == obs[3]
assert V == F(282137639660138177,49593269164032000)

print('STAGE266_EXACT_ALL_REAL_FACE_PASS')
print('states',len(STATES),'action_costs',sum(map(len,action_costs.values())),
      'positive_gaps',len(GAPS),'tie_states',TIES)
print('minimum_positive_gap',min(GAPS))
print('dual lamP',lamP,'lamQ',lamQ,'thetaP=0 thetaQ=1 H',H[ZERO])
print('caps a',a,'b',b)
print('V',V,'decimal',float(V))
for k,v in vectors.items():
    print('policy',k, 'eP,eQ,tP,tQ',','.join(map(str,v)),
          'tQ-tP',v[3]-v[2])
print('ccw_face',[(p[2],str(p[0]),str(p[1])) for p in pts])
print('area',area)
print('strict_positive_mixture',ids,list(map(str,weights)),
      'time_gap',obs[3]-obs[2])
print('history_nodes',sum(h['nodes'] for h in history),
      'terminal_leaves',sum(h['leaves'] for h in history),
      'double_source_exact_normalization',True)
print('stage265_shared_edge I5,I6 verified full observer equality')

# Forward Stage267: exact, independently ordered-history-verified feasible exterior witness.
K = policy((0, 1))
assert K[(1, 2, 0)] == 'Q'
K[(1, 2, 0)] = 'C'
obsK = from_counts(K)
obsK_hist, K_meta = ordered_history_dfs(K)
assert obsK == obsK_hist
assert obsK == (
    F(71046311473,990677827584),F(109630907431,139314069504),
    F(1722912951593,371504185344),F(63545971253,11609505792))
cap267 = tuple(F(49,100)*(vectors[(0,1)][i]+vectors[(1,1)][i]) +
               F(1,50)*obsK[i] for i in range(4))
assert cap267 == (
    F(3776724593681,49533891379200),
    F(1799211749497,2321901158400),
    F(3355004206763,687970713600),
    F(3336652788737,580475289600))
assert cap267[3] > cap267[2]
outer = cross(vectors[(0,1)],vectors[(1,1)],cap267)
assert outer == F(-47704025643875,11501279977342425366528)
assert cross(vectors[(0,1)],vectors[(1,1)],vectors[(0,0)]) > 0
old_support_gap = lamP*cap267[0]+lamQ*cap267[1]+cap267[3]-H[ZERO]
assert old_support_gap == F(2449655187043,317396922649804800)
print('STAGE267_EXACT_FEASIBILITY_WITNESS_PASS')
print('Stage267 K ordered_nodes',K_meta['nodes'],
      'terminal_leaves',K_meta['leaves'], 'two_source_normalized',True)
print('Stage267 candidate_caps',cap267[:2],
      'feasible_time_Q',cap267[3], 'outside_orient',outer,
      'old_support_gap',old_support_gap)
