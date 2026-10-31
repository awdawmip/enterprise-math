#!/usr/bin/env python3
"""Stage276 exact Bellman primal/dual certificate (external N=12 IID model).
Only the Python standard library is used; every number in the proof is rational.
"""
from fractions import Fraction as F
from collections import Counter

N = 12
P = (F(1, 8), F(1, 24), F(5, 6))
Q = (F(1, 12), F(1, 12), F(5, 6))
STATES = [(i, j, n-i-j) for n in range(N+1)
          for i in range(n+1) for j in range(n-i+1)]
assert len(STATES) == 455 and sum(P) == sum(Q) == 1
p = {s: P[0]**s[0]*P[1]**s[1]*P[2]**s[2] for s in STATES}
q = {s: Q[0]**s[0]*Q[1]**s[1]*Q[2]**s[2] for s in STATES}
T, S = (0, 0, 5), (0, 1, 11)

def step(s, z):
    return tuple(s[i] + (i == z) for i in range(3))

def bellman(lp, lq):
    b, actions, gaps = {}, {}, []
    for s in reversed(STATES):
        c = {'P': lq*q[s], 'Q': lp*p[s]}
        if sum(s) < N:
            c['C'] = q[s] + sum(b[step(s,z)] for z in range(3))
        b[s] = min(c.values())
        actions[s] = tuple(a for a in c if c[a] == b[s])
        gaps.extend(v-b[s] for v in c.values() if v > b[s])
    return b, actions, gaps

LP, LQ = F(2145488384, 11690591), F(1072744192, 11690591)
B, EQ, gaps = bellman(LP, LQ)
H = F(16434433593089254321, 180962645235204096)
assert B[(0,0,0)] == H
assert {s: a for s, a in EQ.items() if len(a) > 1} == {
    T: ('P','C'), S: ('P','Q')}
assert len(gaps) == 817 and min(gaps) > 0
assert sum(2 + (sum(s) < N) for s in STATES) == 1274

# The same state Bellman value lower-bounds ALL ordered-history policies.
# A count-state calculation is a proof technique, not a strategy restriction.
def policy(t_continue, s_declares_q, tie_map=EQ, terminal=S):
    a = {s: tie_map[s][0] for s in STATES}
    a[T] = 'C' if t_continue else 'P'
    a[terminal] = 'Q' if s_declares_q else 'P'
    return a

def count_observers(a):
    out = {}
    for s in reversed(STATES):
        if a[s] == 'P':
            out[s] = (F(0),q[s],F(0),F(0))
        elif a[s] == 'Q':
            out[s] = (p[s],F(0),F(0),F(0))
        else:
            children = [out[step(s,z)] for z in range(3)]
            out[s] = (sum(v[0] for v in children),
                      sum(v[1] for v in children),
                      p[s]+sum(v[2] for v in children),
                      q[s]+sum(v[3] for v in children))
    return out[(0,0,0)]

def ordered_audit(a, marker=S):
    """Separate unmerged walk; maintains every ordered word and both source masses."""
    obs = [F(0)]*4
    terminal_mass = [F(0),F(0)]
    count = Counter()
    def visit(s, mp, mq, word):
        count['nodes'] += 1
        if s == marker:
            count['marker'] += 1
            if word[:5] == (2,)*5:
                count['marker_from_T'] += 1
        action = a[s]
        if action == 'C':
            for z in range(3):
                visit(step(s,z),mp*P[z],mq*Q[z],word+(z,))
        else:
            count['terminals'] += 1
            terminal_mass[0] += mp
            terminal_mass[1] += mq
            if action == 'P': obs[1] += mq
            else: obs[0] += mp
            obs[2] += len(word)*mp
            obs[3] += len(word)*mq
    visit((0,0,0),F(1),F(1),())
    assert terminal_mass == [F(1),F(1)]
    return tuple(obs),count

flags = {'U':(False,False),'V':(True,False),
         'W':(True,True),'X':(False,True)}
pts, counts = {}, {}
for name, pair in flags.items():
    a = policy(*pair)
    v, c = ordered_audit(a)
    assert v == count_observers(a)
    assert v[3] > v[2]
    assert LP*v[0]+LQ*v[1]+v[3] == H
    pts[name],counts[name] = v,c
assert (counts['U']['marker'], counts['V']['marker']) == (5,6)
assert (counts['U']['marker_from_T'],counts['V']['marker_from_T']) == (0,1)
assert (counts['X']['marker'],counts['W']['marker']) == (5,6)
assert all(5*(pts['W'][i]-pts['V'][i]) ==
           6*(pts['X'][i]-pts['U'][i]) for i in range(4))

# All zero-gap history-dependent policies are U+r(V-U)+(k/5)(X-U),
# 0<=r<=1 and 0<=k<=5+r. These constraints are also sufficient.
def orient(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
poly = tuple(pts[z] for z in 'UVWX')
turns = tuple(orient(poly[i],poly[(i+1)%4],poly[(i+2)%4])
              for i in range(4))
assert all(v > 0 for v in turns)
area = abs(sum(poly[i][0]*poly[(i+1)%4][1]
              -poly[(i+1)%4][0]*poly[i][1]
              for i in range(4)))/2
assert area == F(19622268829345703125,103511519796081828298752)

# Stage275 exact predecessor: share precisely its Jplus--M2 side W--X.
OLD_LP = F(38096641024,218617401)
OLD_LQ = F(6434343396,72872467)
OLD_B, OLD_EQ, old_gaps = bellman(OLD_LP, OLD_LQ)
S4 = (1,2,7)
assert {s: a for s,a in OLD_EQ.items() if len(a)>1} == {
    T: ('P','C'), S4: ('Q','C')}
def old_policy(t_cont, s4_cont):
    a = {s: OLD_EQ[s][0] for s in STATES}
    a[T]='C' if t_cont else 'P'
    a[S4]='C' if s4_cont else 'Q'
    return a
M = count_observers(old_policy(False,False))
Jnew = count_observers(old_policy(True,False))
Jplus = count_observers(old_policy(True,True))
M2 = count_observers(old_policy(False,True))
assert Jplus == pts['W'] and M2 == pts['X']
assert orient(Jplus,M2,M) * orient(pts['W'],pts['X'],pts['U']) < 0

A = F(1162027955941,15850845241344)
D = F(868777330255,1114512556032)
weights = (F(169151113,233811820000),
           F(343659922061,701435460000),
           F(1786340423,3507177300))
assert all(w>0 for w in weights) and sum(weights)==1
mix = tuple(sum(weights[j]*pts[name][i]
                for j,name in enumerate('VWX')) for i in range(4))
VAL=F(19001515155589573655,3257327614233673728)
assert mix[0]==A and mix[1]==D and mix[3]==VAL
assert mix[3]>mix[2]
assert VAL==H-LP*A-LQ*D
OLD_UPPER=F(541791009235,92876046336)
assert OLD_UPPER-VAL == F(3508358828125,203582975889604608)>0

print('STAGE276_EXACT_ALL_REAL_FACE_PASS')
print('state_count',len(STATES),'action_costs',1274,
      'strict_gaps',len(gaps),'minimum_strict_gap',min(gaps))
print('dual',LP,LQ,'root_H',H,'ties',T,S)
for name in 'UVWX':
    c=counts[name]
    print(name,'observers',*[str(t) for t in pts[name]],
          'ordered_nodes',c['nodes'],'terminals',c['terminals'],
          'reached_S',c['marker'],'descendant_S',c['marker_from_T'])
print('exact_region_area',area,'turns',*[str(z) for z in turns])
print('old_shared_edge_WX', Jplus==pts['W'] and M2==pts['X'])
print('target_caps',A,D,'weights_VWX',*[str(x) for x in weights])
print('target_eP_eQ_tP_tQ',*[str(x) for x in mix])
print('global_optimum',VAL,'improvement_over_stage275_feasible',OLD_UPPER-VAL)
print('total_ordered_nodes',sum(c['nodes'] for c in counts.values()),
      'total_terminals',sum(c['terminals'] for c in counts.values()))

# Continuation Stage277: next adjacent exact face, ties T and S5=(1,2,8).
S5 = (1,2,8)
LP2 = F(8245757952,44495173)
LQ2 = F(4104296772,44495173)
B2, EQ2, gaps2 = bellman(LP2,LQ2)
H2 = F(7860156606936445891,86094494776590336)
assert B2[(0,0,0)] == H2
assert {s:a for s,a in EQ2.items() if len(a)>1} == {
    T:('P','C'),S5:('Q','C')}
assert len(gaps2)==817 and min(gaps2)>0

def policy2(t_continue, s5_continue):
    a={s:EQ2[s][0] for s in STATES}
    a[T]='C' if t_continue else 'P'
    a[S5]='C' if s5_continue else 'Q'
    return a

p2,c2={},{}
for name,fl in {'U':(False,False),'V':(True,False),
                'W':(True,True),'X':(False,True)}.items():
    a=policy2(*fl)
    v,c=ordered_audit(a,marker=S5)
    assert v==count_observers(a)
    assert v[3]>v[2]
    assert LP2*v[0]+LQ2*v[1]+v[3]==H2
    p2[name],c2[name]=v,c
assert c2['U']['marker']==c2['X']['marker']==145
assert c2['V']['marker']==c2['W']['marker']==155
assert c2['U']['marker_from_T']==c2['X']['marker_from_T']==0
assert c2['V']['marker_from_T']==c2['W']['marker_from_T']==10
assert all(145*(p2['W'][i]-p2['V'][i]) ==
           155*(p2['X'][i]-p2['U'][i]) for i in range(4))
P2=tuple(p2[z] for z in 'UVWX')
turns2=tuple(orient(P2[i],P2[(i+1)%4],P2[(i+2)%4])
             for i in range(4))
assert all(v<0 for v in turns2)
area2=abs(sum(P2[i][0]*P2[(i+1)%4][1]
              -P2[(i+1)%4][0]*P2[i][1] for i in range(4)))/2
assert area2==F(1357884918212890625,207023039592163656597504)
assert p2['U']==pts['U'] and p2['V']==pts['V']
assert orient(pts['U'],pts['V'],pts['X']) * orient(p2['U'],p2['V'],p2['X']) < 0
# Pick one strict interior witness of the Stage277 region.
w2=(F(49,100),F(49,100),F(1,50))
y2=tuple(w2[0]*p2['U'][i]+w2[1]*p2['V'][i]+w2[2]*p2['X'][i]
         for i in range(4))
assert y2[3]>y2[2] and LP2*y2[0]+LQ2*y2[1]+y2[3]==H2
assert orient(p2['U'],p2['V'],y2) * orient(pts['U'],pts['V'],pts['X']) < 0
print('STAGE277_EXACT_ALL_REAL_FACE_PASS')
print('dual277',LP2,LQ2,'root_H277',H2,'ties277',T,S5)
for name in 'UVWX':
    c=c2[name]
    print('277',name,'observers',*[str(z) for z in p2[name]],
          'nodes',c['nodes'],'terminals',c['terminals'],
          'reached_S5',c['marker'],'from_T',c['marker_from_T'])
print('area277',area2,'turns',*[str(z) for z in turns2])
print('shared_edge_R276_R277_UV',p2['U']==pts['U'] and p2['V']==pts['V'])
print('Stage277_witness_caps_optimum',y2[0],y2[1],y2[3],
      'time_gap',y2[3]-y2[2])
print('Stage277_ordered_nodes',sum(c['nodes'] for c in c2.values()),
      'terminals',sum(c['terminals'] for c in c2.values()))
