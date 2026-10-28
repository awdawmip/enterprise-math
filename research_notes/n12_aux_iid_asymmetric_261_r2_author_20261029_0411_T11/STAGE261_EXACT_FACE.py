#!/usr/bin/env python3
"""Stage261 complete exact certificate; external ternary IID N=12 ONLY.

Independent of SciPy or floating-point optimizers. Python 3, standard library.
All assertions use fractions.Fraction; ordered DFS does not merge histories.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product

N = 12
P = (F(1, 8), F(1, 24), F(5, 6))
Q = (F(1, 12), F(1, 12), F(5, 6))
E = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
LAM_P = F(2985984, 35755)
LAM_Q = F(1922052, 35755)
H_EXPECTED = F(1106067577, 20594880)
BORDER = F(22312869149, 23219011584)
C5 = (
    F(1692824803, 15479341056), F(4308598685, 5804752896),
    F(2711460067, 644972544), F(2260130659, 483729408),
)
C12 = (
    F(25325973227, 139314069504), F(10403158555, 17414258688),
    F(34493690603, 5804752896), F(9303029477, 1451188224),
)
A = (C5[0] + C12[0]) / 2 - F(3, 20000)
B = (C5[1] + C12[1]) / 2
V_EXPECTED = F(180113344229101789, 32429521843200000)
AREA_EXPECTED = F(69108758447265625, 101085468550861160448)


def add(s, inc):
    return tuple(s[k] + inc[k] for k in range(3))


def likelihood(s):
    return F(2, 3)**s[0] * F(2)**s[1]

STATES = tuple((i, j, d-i-j)
               for d in range(N+1)
               for i in range(d+1)
               for j in range(d-i+1))
assert len(STATES) == 455


@lru_cache(None)
def bellman(s):
    """Returns exact conditional dual cost per unit P source mass."""
    l = likelihood(s)
    costs = [LAM_Q*l, LAM_P]  # P-stop, Q-stop
    if sum(s) < N:
        costs.append(l + sum((P[k]*bellman(add(s,E[k]))[0]
                              for k in range(3)), F(0)))
    val = min(costs)
    return val, tuple(k for k,c in enumerate(costs) if c == val), costs

for s in sorted(STATES, key=sum, reverse=True):
    bellman(s)
H = bellman((0, 0, 0))[0]
assert H == H_EXPECTED
TIES = tuple(s for s in STATES if len(bellman(s)[1]) > 1)
assert TIES == ((0,0,5),(0,0,6),(0,1,5),(0,0,7),
                (0,0,8),(0,0,9),(0,0,10),(0,0,11))
assert all(len(bellman(s)[1]) <= 2 for s in STATES)
ALTERNATIVES = sum(len(bellman(s)[2]) for s in STATES)
STRICT_GAPS = sum(c > bellman(s)[0] for s in STATES
                  for c in bellman(s)[2])
assert (ALTERNATIVES, STRICT_GAPS) == (1274, 811)


def act(s, mask):
    ties = bellman(s)[1]
    return ties[mask[TIES.index(s)]] if len(ties) == 2 else ties[0]


@lru_cache(None)
def suffix(s, mask):
    """Four conditional observers, exact state quotient."""
    a = act(s, mask)
    if a == 0:  # decide P
        return F(0), F(1), F(0), F(0)
    if a == 1:  # decide Q
        return F(1), F(0), F(0), F(0)
    tail = tuple(suffix(add(s,E[k]),mask) for k in range(3))
    return (sum((P[k]*tail[k][0] for k in range(3)), F(0)),
            sum((Q[k]*tail[k][1] for k in range(3)), F(0)),
            1 + sum((P[k]*tail[k][2] for k in range(3)), F(0)),
            1 + sum((Q[k]*tail[k][3] for k in range(3)), F(0)))


def ordered_dfs(mask):
    """Independent unmerged ordered-history path enumerator with P/Q masses."""
    obs = [F(0),F(0),F(0),F(0)]
    terminal = [F(0),F(0)]
    nodes = 0
    leaves = 0

    def visit(s, pm, qm):
        nonlocal nodes, leaves
        nodes += 1
        assert qm == pm*likelihood(s)
        a = act(s, mask)
        if a in (0,1):
            leaves += 1
            terminal[0] += pm
            terminal[1] += qm
            if a == 0:
                obs[1] += qm
            else:
                obs[0] += pm
            return
        assert sum(s) < N
        obs[2] += pm
        obs[3] += qm
        for k in range(3):
            visit(add(s,E[k]),pm*P[k],qm*Q[k])

    visit((0,0,0), F(1), F(1))
    assert terminal == [F(1),F(1)]
    return tuple(obs),nodes,leaves


masks_by_vector = {}
for mask in product((0,1),repeat=len(TIES)):
    v = suffix((0,0,0),mask)
    assert v[3] + LAM_P*v[0] + LAM_Q*v[1] == H
    assert v[3] > v[2]
    masks_by_vector.setdefault(v, mask)
assert len(masks_by_vector) == 16
assert len(list(product((0,1),repeat=len(TIES)))) == 256
assert C5 in masks_by_vector and C12 in masks_by_vector

nodes_sum = leaves_sum = 0
for v, mask in masks_by_vector.items():
    vd, nd, ld = ordered_dfs(mask)
    assert v == vd
    nodes_sum += nd
    leaves_sum += ld

# Exact rational monotone-chain hull (no floating-point geometry).
def cross(a,b,c):
    return ((b[0]-a[0])*(c[1]-a[1])
            -(b[1]-a[1])*(c[0]-a[0]))

point_to_vector = {v[:2]:v for v in masks_by_vector}
points = sorted(point_to_vector)

def chain(seq):
    out = []
    for x in seq:
        while len(out) >= 2 and cross(out[-2],out[-1],x) <= 0:
            out.pop()
        out.append(x)
    return out

hull_pts = chain(points)[:-1] + chain(points[::-1])[:-1]
vertices = [point_to_vector[x] for x in hull_pts]
assert len(vertices) == 5
assert all(cross(hull_pts[i],hull_pts[(i+1)%5],hull_pts[(i+2)%5])>0
           for i in range(5))
assert all(cross(hull_pts[i],hull_pts[(i+1)%5],x)>=0
           for i in range(5) for x in points)
area = abs(sum((hull_pts[i][0]*hull_pts[(i+1)%5][1]
                -hull_pts[(i+1)%5][0]*hull_pts[i][1]
                for i in range(5)),F(0)))/2
assert area == AREA_EXPECTED
assert C5 in vertices and C12 in vertices
assert {i for i in range(5) if vertices[i] in (C5,C12)} in ({0,4},{1,2},{2,3},{3,4},{0,1})
# New face is on the strictly opposite side of the C5-C12 edge from Stage260.
assert 2*C5[0]+C5[1] == BORDER
assert 2*C12[0]+C12[1] == BORDER
assert all(2*v[0]+v[1] < BORDER for v in vertices if v not in (C5,C12))
assert 2*A+B == BORDER-F(3,10000)

D5 = next(v for v in vertices if v[:2] == (F(1166286571,11609505792), F(3274031045,4353564672)))
# Positive exact barycentric weights for target (A,B) using C5, D5, C12.
det = cross(C5,D5,C12)
assert det != 0
wD = cross(C5,(A,B),C12)/det
wC12 = cross(C5,D5,(A,B))/det
wC5 = 1-wD-wC12
weights = (wC5,wD,wC12)
assert weights == (
    F(64838811099718633,140932662207031250),
    F(13060694016,349169921875),
    F(14164453533437333,28186532441406250))
assert all(0<w<1 for w in weights)
assert sum(weights)==1
witness = tuple(sum((weights[j]*v[k]
                     for j,v in enumerate((C5,D5,C12))),F(0))
                for k in range(4))
assert witness[:2] == (A,B)
assert witness[3]>witness[2]
assert witness[3] == H-LAM_P*A-LAM_Q*B == V_EXPECTED
assert witness == (
    A,B,F(659238036620443201,129718087372800000),V_EXPECTED)

print('STAGE261_BELLMAN_PASS',len(STATES),ALTERNATIVES,STRICT_GAPS,len(TIES))
print('DUAL', 'lambdaP',LAM_P,'lambdaQ',LAM_Q,'theta',(0,1),'H',H)
print('POLICY_ENUMERATION',256,'UNIQUE_FOUR_VECTORS',len(masks_by_vector))
print('ORDERED_DFS',nodes_sum,leaves_sum,'P_Q_TERMINAL_MASS_1_EACH')
print('HULL_CCW_5_EXACT_AREA',area)
for z,v in enumerate(vertices):
    print('HULL_VERTEX',z,'BITS',''.join(map(str,masks_by_vector[v])),
          'eP_eQ_tP_tQ',*(str(x) for x in v))
print('EDGE_CONTACT',BORDER,'SIDE_OUTSIDE_LESS','CAP_EDGE_GAP',F(3,10000))
print('TARGET',A,B,'OPTIMUM',V_EXPECTED,'TIME_P',witness[2],
      'TIME_Q',witness[3], 'TIME_GAP',witness[3]-witness[2])
print('PRIMAL_WEIGHTS_C5_D5_C12',*(str(w) for w in weights))
print('STAGE261_EXACT_ALL_REAL_FACE_PASS')
