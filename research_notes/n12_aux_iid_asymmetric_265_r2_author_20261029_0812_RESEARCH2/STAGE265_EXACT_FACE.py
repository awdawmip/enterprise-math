#!/usr/bin/env python3
"""Stage265 exact author certificate. External finite ternary IID model only; NOT native P000.
Run: python STAGE265_EXACT_FACE.py (Python stdlib Fraction, no SciPy needed).
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product

N = 12
P = (F(1, 8), F(1, 24), F(5, 6))
Q = (F(1, 12), F(1, 12), F(5, 6))
a = F(2501401941677, 29023764480000)
b = F(13264221055, 17414258688)
LP = F(6216128, 68615)
LQ = F(3900924, 68615)
H = F(90763458197, 1600650720)
OPT = F(348042679485689167, 62233299993600000)
AREA = F(4606719970703125, 67390312367240773632)

states = [(i,j,n-i-j) for n in range(N+1) for i in range(n+1) for j in range(n-i+1)]
def child(s, k):
    return tuple(x + (i==k) for i,x in enumerate(s))
D, actions, positive_gaps = {}, {}, []
action_count = 0
for s in reversed(states):
    ratio = F(2,3)**s[0] * 2**s[1]
    candidates = {'P': LQ*ratio, 'Q': LP}
    if sum(s) < N:
        candidates['C'] = ratio + sum(P[k]*D[child(s,k)] for k in range(3))
    minimum = min(candidates.values())
    D[s] = minimum
    actions[s] = [act for act in ('P','Q','C') if act in candidates and candidates[act] == minimum]
    positive_gaps.extend(v-minimum for v in candidates.values() if v>minimum)
    action_count += len(candidates)

assert len(states) == 455 and action_count == 1274
assert len(positive_gaps) == 817 and min(positive_gaps) == F(2048,177147)
assert D[(0,0,0)] == H
TIES = [s for s in states if len(actions[s]) > 1]
assert TIES == [(0,0,5),(0,1,9)]
assert [actions[s] for s in TIES] == [['P','C'],['Q','C']]

def fixed_policy(bits):
    d = {s:actions[s][0] for s in states}
    for s,j in zip(TIES,bits):
        d[s] = actions[s][j]
    return d

def merged_dag(policy):
    mass = defaultdict(lambda: (F(0), F(0)))
    mass[(0,0,0)] = (F(1),F(1))
    out = [F(0)]*6 # eP, eQ, tP, tQ, terminalP, terminalQ
    for s in states:
        pp,qq = mass[s]
        decision = policy[s]
        if decision == 'P':
            out[1] += qq
            out[4] += pp;out[5] += qq
        elif decision == 'Q':
            out[0] += pp
            out[4] += pp;out[5] += qq
        else:
            out[2] += pp;out[3] += qq
            for k in range(3):
                a0,b0=mass[child(s,k)]
                mass[child(s,k)]=(a0+pp*P[k],b0+qq*Q[k])
    assert out[4:] == [F(1),F(1)]
    return tuple(out[:4])

def independent_ordered_dfs(policy):
    out=[F(0)]*6
    nodes=terminals=0
    def go(word,pp,qq):
        nonlocal nodes,terminals
        nodes+=1
        s=(word.count(0),word.count(1),word.count(2))
        act=policy[s]
        if act=='P':
            out[1]+=qq;out[4]+=pp;out[5]+=qq;terminals+=1
        elif act=='Q':
            out[0]+=pp;out[4]+=pp;out[5]+=qq;terminals+=1
        else:
            out[2]+=pp;out[3]+=qq
            for k in range(3):
                go(word+(k,),pp*P[k],qq*Q[k])
    go((),F(1),F(1))
    assert out[4:] == [F(1),F(1)]
    return tuple(out[:4]),nodes,terminals

B={};nodes=terminals=0
for bits in product((0,1),repeat=len(TIES)):
    pol=fixed_policy(bits)
    v=merged_dag(pol)
    independent,nn,tt=independent_ordered_dfs(pol)
    assert v==independent
    assert v[3]>v[2] and v[3]+LP*v[0]+LQ*v[1]==H
    B[bits]=v
    nodes+=nn;terminals+=tt
    print('VERTEX',bits,tuple(map(str,v)),'DFS',nn,tt)
assert (nodes,terminals)==(2824,1884)

H5,I5,H6,I6=(B[k] for k in ((0,0),(0,1),(1,0),(1,1)))
assert H5==(F(3750849409,46438023168),F(13498546055,17414258688),F(8819755201,1934917632),F(7717391977,1451188224))
assert H6==(F(1420974803,15479341056),F(4343298685,5804752896),F(3244810067,644972544),F(2829330659,483729408))
def orient(u,v,w):
    return (v[0]-u[0])*(w[1]-u[1])-(v[1]-u[1])*(w[0]-u[0])
R=(H5,I5,I6,H6)
turns=[orient(R[j],R[(j+1)%4],R[(j+2)%4]) for j in range(4)]
assert min(turns)>0
signed_cap=[orient(R[j],R[(j+1)%4],(a,b)) for j in range(4)]
assert min(signed_cap)>0
area=abs(sum(R[j][0]*R[(j+1)%4][1] - R[(j+1)%4][0]*R[j][1] for j in range(4)))/2
assert area == AREA

# Stage264 vertices, exact immutable antecedent, edge adjacency not approximate
G5=(F(668435839,7739670528), F(2229900905,2902376448))
G6=(F(1524881053,15479341056),F(4295642435,5804752896))
assert all(orient(H5,H6,v)>0 for v in (G5,G6))
assert all(orient(H5,H6,v)<0 for v in (I5,I6))
assert orient(H5,H6,(a,b)) == -F(46865,17414258688)

# Strictly positive exact primal mixture on one simplex of the four-corner equality hull.
w=(F(374206659479903,837585449218750),F(18135982964736,418792724609375),F(136674183619,268027343750))
assert min(w)>0 and sum(w)==1
mix=tuple(sum(w[j]*p[i] for j,p in enumerate((H5,I5,H6))) for i in range(4))
assert mix==(a,b,F(398394906718840411,82977733324800000),OPT)
assert mix[3]-mix[2]==F(2870888257469,3627970560000)>0
assert H-LP*a-LQ*b==OPT
# The opposite edge to probe in Stage266; a discovery target, not proved feasible here.
next_mid=((I5[0]+I6[0])/2,(I5[1]+I6[1])/2)
next_cap=(next_mid[0]-F(1,10000), next_mid[1])
assert all(F(0)<c<F(1) for c in next_cap)
assert orient(I5,I6,next_cap)<0
print('BELLMAN',len(states),action_count,len(positive_gaps),'MIN_GAP',min(positive_gaps),'TIES',TIES)
print('DUAL LP',LP,'LQ',LQ,'THETA_P',0,'THETA_Q',1,'H',H)
print('R265_ORDER H5 I5 I6 H6','TURNS',*map(str,turns),'AREA',AREA)
print('CAPS',a,b,'V',OPT,'TP',mix[2],'TQ_MINUS_TP',mix[3]-mix[2],'MIX',*map(str,w))
print('ORIENT_H5_H6_CAP',orient(H5,H6,(a,b)),'NEXT266_CAPS',*map(str,next_cap),'NEXT_ORIENT',orient(I5,I6,next_cap))
print('ORDERED_DFS',nodes,terminals)
print('STAGE265_EXACT_ALL_REAL_FACE_PASS')
