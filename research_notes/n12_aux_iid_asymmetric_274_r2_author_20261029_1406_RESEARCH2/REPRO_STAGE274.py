#!/usr/bin/env python3
"""Stage274: exact finite Bellman + independent full-word P/Q audit.
External 12-step ternary IID model only; no native-X6 or canonical admission claim.
Python standard library only; mathematical predicates use Fraction exclusively.
"""
from fractions import Fraction as F
from collections import Counter

N = 12
P = (F(1, 8), F(1, 24), F(5, 6))
Q = (F(1, 12), F(1, 12), F(5, 6))
STATES = [(i, j, n-i-j) for n in range(N+1)
          for i in range(n+1) for j in range(n-i+1)]
assert len(STATES) == 455
p = {s: P[0]**s[0]*P[1]**s[1]*P[2]**s[2] for s in STATES}
q = {s: Q[0]**s[0]*Q[1]**s[1]*Q[2]**s[2] for s in STATES}

def nxt(s, z):
    return tuple(s[i] + (i == z) for i in range(3))

LAMBDA_P = F(445906494464, 2706255861)
LAMBDA_Q = F(76440567684, 902085287)
H = F(1758667527952600918633, 20945528728608964608)
T, S2, S3, S4 = (0,0,5), (1,2,5), (1,2,6), (1,2,7)

# The count recursion is legitimate because the two *prefix masses* and every
# remaining IID suffix law depend only on counts. No count-policy restriction
# is placed on the original ordered-history strategy space.
B, ties, costs = {}, {}, {}
for s in reversed(STATES):
    actions = {'P': LAMBDA_Q*q[s], 'Q': LAMBDA_P*p[s]}
    if sum(s) < N:
        actions['C'] = q[s] + sum(B[nxt(s, z)] for z in range(3))
    minimum = min(actions.values())
    B[s] = minimum
    ties[s] = tuple(a for a, v in actions.items() if v == minimum)
    costs[s] = actions
assert B[(0,0,0)] == H
assert {s: a for s, a in ties.items() if len(a)>1} == {
    T: ('P','C'), S3: ('Q','C')}
assert ties[S2] == ('C',) and ties[S4] == ('Q',)
assert sum(len(c) for c in costs.values()) == 1274
strict_gaps = [v-min(a.values()) for a in costs.values()
               for v in a.values() if v>min(a.values())]
assert len(strict_gaps) == 817
assert all(g > 0 for g in strict_gaps)

def policy(t_continue, s3_continue):
    choices = {s: ties[s][0] for s in STATES}
    choices[T] = 'C' if t_continue else 'P'
    choices[S3] = 'C' if s3_continue else 'Q'
    return choices

def count_observers(choices):
    """A separate backwards calculation of all four source observers."""
    obs = {}
    for s in reversed(STATES):
        action = choices[s]
        if action == 'P':
            obs[s] = (F(0), q[s], F(0), F(0))
        elif action == 'Q':
            obs[s] = (p[s], F(0), F(0), F(0))
        else:
            children = [obs[nxt(s,z)] for z in range(3)]
            obs[s] = (sum(x[0] for x in children),
                      sum(x[1] for x in children),
                      p[s]+sum(x[2] for x in children),
                      q[s]+sum(x[3] for x in children))
    return obs[(0,0,0)]

def ordered_history_audit(choices):
    """Independent DFS: no aggregation/merging of distinct ordered words."""
    out = [F(0) for _ in range(4)]
    terminal_mass = [F(0), F(0)]
    count = Counter()
    def dfs(s, mp, mq, word):
        count['nodes'] += 1
        if s == T:
            count['T'] += 1
        if s == S3:
            count['S3'] += 1
            if word[:5] == (2,)*5:
                count['S3_descends_from_T'] += 1
        action = choices[s]
        if action != 'C':
            count['terminal'] += 1
            terminal_mass[0] += mp
            terminal_mass[1] += mq
            if action == 'P':
                out[1] += mq
            else:
                out[0] += mp
            out[2] += len(word)*mp
            out[3] += len(word)*mq
        else:
            for z in range(3):
                dfs(nxt(s,z), mp*P[z], mq*Q[z], word+(z,))
    dfs((0,0,0), F(1), F(1), ())
    assert terminal_mass == [F(1), F(1)]
    return tuple(out), count

names = ('K','J','Jnew','M')
choices = { 'K': policy(False,False), 'J': policy(True,False),
            'Jnew': policy(True,True), 'M': policy(False,True)}
points = {}
counts = {}
for name in names:
    v, c = ordered_history_audit(choices[name])
    assert v == count_observers(choices[name]), name
    assert v[3] > v[2], name
    assert LAMBDA_P*v[0] + LAMBDA_Q*v[1] + v[3] == H, name
    points[name], counts[name] = v, c
K, J, Jnew, M = (points[n] for n in names)
assert (counts['K']['S3'], counts['J']['S3']) == (80,83)
assert (counts['M']['S3'], counts['Jnew']['S3']) == (80,83)
assert (counts['K']['S3_descends_from_T'],
        counts['J']['S3_descends_from_T']) == (0,3)
assert all(80*(Jnew[i]-J[i]) == 83*(M[i]-K[i]) for i in range(4))

# Thus every Bellman-equality history strategy has the four-observer form
# K + r*(J-K) + (k/80)*(M-K), 0<=r<=1, 0<=k<=80+3*r.
# The two source likelihoods of all reached S3 words are identical.
# All k in this range are attainable by conditional coin k/(80+3*r).
def orient(A, B_, C):
    return (B_[0]-A[0])*(C[1]-A[1]) - (B_[1]-A[1])*(C[0]-A[0])
polygon = (K, J, Jnew, M)
turns = [orient(polygon[i],polygon[(i+1)%4],polygon[(i+2)%4])
         for i in range(4)]
assert all(x < 0 for x in turns), turns
area = abs(sum(polygon[i][0]*polygon[(i+1)%4][1]
               -polygon[(i+1)%4][0]*polygon[i][1]
               for i in range(4)))/2
assert area == F(7179682704150390625,1104122877824872835186688)
Gplus = (F(187155450011,2641807540224),
         F(219610483345,278628139008))
assert orient(K,J,M) < 0 < orient(K,J,Gplus)

# The feasible point is an exact positive mixture of zero-dual-gap corners.
weights = (F(49,100),F(49,100),F(1,50))
point274 = tuple(weights[0]*K[i]+weights[1]*J[i]+weights[2]*M[i]
                 for i in range(4))
assert point274 == (F(131763207049,1761205026816),
                    F(865980121505,1114512556032),
                    F(3234116608093,660451885056),
                    F(538252197985,92876046336))
assert point274[3] > point274[2]
assert H-LAMBDA_P*point274[0]-LAMBDA_Q*point274[1] == point274[3]

# Next independently checked frontier: new S4 action after reaching M.
M2_choices = dict(choices['M'])
M2_choices[S4] = 'C'
assert choices['M'][S4] == 'Q'
M2, M2_counts = ordered_history_audit(M2_choices)
assert M2 == count_observers(M2_choices)
assert M2_counts['nodes'] == 10573 and M2_counts['terminal'] == 7049
M2_slack = LAMBDA_P*M2[0]+LAMBDA_Q*M2[1]+M2[3]-H
assert M2_slack == F(1798033664453125,654547772769030144) > 0
point275 = tuple(weights[0]*M[i]+weights[1]*Jnew[i]+weights[2]*M2[i]
                 for i in range(4))
assert point275 == (F(1175053055941,15850845241344),
                    F(867218405255,1114512556032),
                    F(1079662613531,220150628352),
                    F(539955234235,92876046336))
assert point275[3] > point275[2]
assert orient(M,Jnew,point275) < 0 < orient(M,Jnew,K)

print('STAGE274_EXACT_ALL_REAL_FACE_PASS')
print('model N=12 states=455 legal_actions=1274 positive_action_gaps=817 exact_ties=2')
print('ties', {str(s): ties[s] for s in (T,S3)})
print('minimum_strict_positive_gap', min(strict_gaps))
print('lambdaP',LAMBDA_P,'lambdaQ',LAMBDA_Q,'H',H)
for name in names:
    print(name,'observations',*[str(z) for z in points[name]],
          'ordered_nodes',counts[name]['nodes'],
          'ordered_terminal',counts[name]['terminal'],
          'reached_S3',counts[name]['S3'])
print('nested_reach_S3_Tstop=80_Tcontinue=83_Tdescendant=3')
print('exact_parameter_domain 0<=r<=1, 0<=k<=80+3*r')
print('quadrilateral_R274 area',area,'negative_turns',*[str(z) for z in turns])
print('Stage273_R273_shared_edge_K-J opposite_sides',
      orient(K,J,M),orient(K,J,Gplus))
print('point274',*[str(z) for z in point274],
      'time_gap_QminusP',point274[3]-point274[2])
print('Stage275_M2',*[str(z) for z in M2],
      'ordered_nodes',M2_counts['nodes'],'ordered_terminal',M2_counts['terminal'],
      'old_dual_slack',M2_slack)
print('Stage275_exterior_point',*[str(z) for z in point275],
      'orientation',orient(M,Jnew,point275),
      'Stage274_feasible_upper_bound',point275[3])
print('audit_5_policies_ordered_nodes',sum(c['nodes'] for c in counts.values())+M2_counts['nodes'],
      'audit_5_policies_terminal',sum(c['terminal'] for c in counts.values())+M2_counts['terminal'])
