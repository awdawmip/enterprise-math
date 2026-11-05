#!/usr/bin/env python3
"""PREFIX-520 exact finite-group certificate for candidate four-STAR phase paths.
No external dependencies; only integers, complete finite enumeration, and assert.
"""
import json
from collections import defaultdict
from itertools import permutations

# Fixed K4 edge/STAR data from PREFIX-518; indices 0..5 denote L1..L6.
AXES = [(0,1),(2,3),(0,2),(1,3),(1,2),(0,3)]
STARS = [{0,2,5},{0,3,4},{1,2,4},{1,3,5}]
GROUP = list(permutations(range(4)))
IDENTITY = GROUP.index((0,1,2,3))
AXIS_MAP = [[AXES.index(tuple(sorted((g[a],g[b])))) for a,b in AXES] for g in GROUP]

def phase(g, p):
    return (1 if p > 0 else -1) * (AXIS_MAP[g][abs(p)-1]+1)

def act(g, state):
    star, prev, current = state
    return (GROUP[g][star], phase(g, prev), phase(g, current))

def neighbors(star, p):
    return {(-1 if p>0 else 1)*(a+1) for a in STARS[star] if a != abs(p)-1}

def actual_successors(s):
    star, prev, current = s
    stays = neighbors(star, current)-{prev}
    others = [t for t in range(4) if t != star and abs(current)-1 in STARS[t]]
    assert len(stays)==len(others)==1
    return {(star,current,b) for b in stays} | {(others[0],current,b) for b in neighbors(others[0],current)}

STATES = [(S,old,now) for S in range(4) for ax in sorted(STARS[S])
          for sign in (-1,1) for now in [sign*(ax+1)] for old in sorted(neighbors(S,now))]
assert len(STATES)==48 and len(set(STATES))==48
BASE = {-1:(0,3,-1), 1:(0,-3,1)}
assert all(b in STATES for b in BASE.values())
COORD = {}
for sign in (-1,1):
    for g in range(24):
        s = act(g, BASE[sign])
        assert s not in COORD # free 24-element orbit
        COORD[s] = (sign,g)
assert len(COORD)==48
PORTS = {}
for sign in (-1,1):
    s=BASE[sign]
    stay = sorted(t for t in actual_successors(s) if t[0]==s[0])
    switched = sorted(t for t in actual_successors(s) if t[0]!=s[0])
    assert len(stay)==1 and len(switched)==2
    PORTS[sign]=stay+switched

# Every physical symbolic successor coincides with transported canonical port.
local_checks=0
covariance_checks=0
for s in STATES:
    sign,g=COORD[s]
    predicted=[act(g,t) for t in PORTS[sign]]
    assert set(predicted)==actual_successors(s) and len(predicted)==3
    for j,t in enumerate(predicted):
        assert COORD[t][0]==-sign
        h=COORD[PORTS[sign][j]][1]
        composition=tuple(GROUP[g][GROUP[h][i]] for i in range(4))
        assert GROUP[COORD[t][1]]==composition
        for branch in (0,1):
            old,now=s[2],t[2]
            microtrace=(-old,now) if branch==0 else (now,-old)
            # +/- phase is a signed basis step; both trace choices displace now-old.
            disp={i:0 for i in range(1,7)}
            for x in microtrace:disp[abs(x)]+=1 if x>0 else -1
            target={i:0 for i in range(1,7)}
            target[abs(old)]-=1 if old>0 else -1
            target[abs(now)]+=1 if now>0 else -1
            assert disp==target
            local_checks+=1
    for h in range(24):
        moved=act(h,s)
        moved_ports=[act(h,t) for t in predicted]
        assert set(moved_ports)==actual_successors(moved)
        # The local ports are equivariant *as indexed ports*, unlike raw axis sorting.
        sign_h,g_h=COORD[moved]
        assert moved_ports==[act(g_h,t) for t in PORTS[sign_h]]
        covariance_checks+=3

# Two macrosteps preserve the sign of the current phase; index positive orbit by S4.
ORBIT=[act(g,BASE[1]) for g in range(24)]
INDEX={s:i for i,s in enumerate(ORBIT)}
def next_states(s):
    z,g=COORD[s]
    return [act(g,t) for t in PORTS[z]]

def matrix_mult(A,B):
    n=len(A); C=[[0]*n for _ in range(n)]
    for i in range(n):
        for k,x in enumerate(A[i]):
            if x:
                for j,y in enumerate(B[k]):
                    if y:C[i][j]+=x*y
    return C

B=[[0]*24 for _ in range(24)]
for i,s in enumerate(ORBIT):
    for t in next_states(s):
        for u in next_states(t):B[i][INDEX[u]]+=1
assert all(sum(row)==9 for row in B)
IDENT=[[int(i==j) for j in range(24)] for i in range(24)]
POWERS=[IDENT]
for k in range(1,6):POWERS.append(matrix_mult(POWERS[-1],B))
# q(X)=(X-9)(X-1)(X+3)(X^2+2X+9)
# = X^5-5X^4-26X^3-78X^2-135X+243.
coeff=(243,-135,-78,-26,-5,1)
assert all(sum(coeff[k]*POWERS[k][i][j] for k in range(6))==0
           for i in range(24) for j in range(24))

# Direct 48-state recurrence, not matrix multiplication, checks independent path DP.
counts=defaultdict(int,{BASE[1]:1})
returns=[]
for n in range(31):
    returns.append(counts[BASE[1]])
    nxt=defaultdict(int)
    for s,num in counts.items():
        for t in next_states(s):nxt[t]+=num
    counts=nxt
EVEN=[returns[2*i] for i in range(16)]
assert EVEN[:9]==[1,0,5,28,297,2360,22381,198996,1794257]
assert all(returns[2*i+1]==0 for i in range(15))
assert all(EVEN[m+5]==5*EVEN[m+4]+26*EVEN[m+3]+78*EVEN[m+2]+135*EVEN[m+1]-243*EVEN[m]
           for m in range(len(EVEN)-5))
# Time reversal or global sign inversion gives equal return counts for both signs.
for s in STATES:
    z,g=COORD[s]
    opposite=(s[0],-s[1],-s[2])
    assert set((t[0],-t[1],-t[2]) for t in next_states(s))==set(next_states(opposite))

# A nonzero 5x5 Hankel determinant proves the stated scalar recurrence has order exactly five.
def det(A):
    # Fraction-free Bareiss elimination, exact integers.
    M=[row[:] for row in A]; size=len(M); denominator=1;sgn=1
    for k in range(size-1):
        if M[k][k]==0:
            j=next((j for j in range(k+1,size) if M[j][k]),None)
            if j is None:return 0
            M[k],M[j]=M[j],M[k];sgn=-sgn
        pivot=M[k][k]
        for i in range(k+1,size):
            for j in range(k+1,size):
                num=M[i][j]*pivot-M[i][k]*M[k][j]
                assert num%denominator==0
                M[i][j]=num//denominator
        for i in range(k+1,size):M[i][k]=0
        denominator=pivot
    return sgn*M[-1][-1]
hankel=det([[EVEN[i+j] for j in range(5)] for i in range(5)])
assert hankel==-44718096384
summary={
    "status":"ALL_CHECKS_PASS",
    "scope":"PREFIX-518 four-STAR candidate phase-switch relation; not physical rotation selection",
    "task_frozen_pin":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
    "directed_phase_states":len(STATES),
    "S4_group_size":len(GROUP),"free_phase_orbits":2,"states_per_orbit":24,
    "canonical_states":{str(k):list(v) for k,v in BASE.items()},
    "canonical_ports":{str(k):[list(t) for t in v] for k,v in PORTS.items()},
    "port_cocycles":{str(k):[COORD[t][1] for t in PORTS[k]] for k in PORTS},
    "local_microtrace_checks":local_checks,"covariance_port_checks":covariance_checks,
    "two_step_matrix_shape":[24,24],"two_step_row_sum":9,
    "annihilating_polynomial_descending":[1,-5,-26,-78,-135,243],
    "polynomial_matrix_entries_checked":24*24,
    "initial_even_return_counts":EVEN[:12],
    "odd_return_counts_zero_for_n_1_to_29":True,
    "recurrence":"a[m+5] = 5*a[m+4]+26*a[m+3]+78*a[m+2]+135*a[m+1]-243*a[m]",
    "even_macroedge_labeled_return_count":"4^m * a[m] at 2m macroedges",
    "hankel_5x5_determinant":hankel,
    "exact_arithmetic":True,
    "no_external_dependencies":True
}
print(json.dumps(summary,ensure_ascii=False,indent=2))
