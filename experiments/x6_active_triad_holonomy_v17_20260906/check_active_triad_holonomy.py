#!/usr/bin/env python3
from collections import Counter
from itertools import combinations, permutations

# ----- J(6,3) frame connection -----
charts=tuple(combinations(range(6),3))

def adjacent(S,T): return len(set(S)&set(T))==2

def repl(S,T):
    shared=set(S)&set(T)
    leaving=next(x for x in S if x not in shared)
    entering=next(x for x in T if x not in shared)
    return {x:(x if x in shared else entering) for x in S}

def compose_maps(f,g): return {x:f[g[x]] for x in g}

def hol(loop):
    h={x:x for x in loop[0]}
    for a,b in zip(loop,loop[1:]):
        h=compose_maps(repl(a,b),h)
    return h

def parity_on_base(h,S):
    p=tuple(S.index(h[x]) for x in S)
    return sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2

S0=(0,1,2)
flat=(S0,(0,1,3),(0,1,4),S0)
curved=(S0,(0,1,3),(0,2,3),S0)
hf=hol(flat); hc=hol(curved)
assert all(hf[x]==x for x in S0)
assert parity_on_base(hf,S0)==0
assert parity_on_base(hc,S0)==1
assert sum(hc[x]!=x for x in S0)==2
assert len(flat)-1==len(curved)-1==3

# All simple chart triangles reproduce 60 flat / 60 transposition holonomies.
triangles=tuple(
    tri for tri in combinations(charts,3)
    if all(adjacent(a,b) for a,b in combinations(tri,2))
)
classes=Counter()
for tri in triangles:
    loop=tri+(tri[0],)
    h=hol(loop); S=tri[0]
    if all(h[x]==x for x in S):
        classes['flat']+=1
        assert parity_on_base(h,S)==0
    else:
        classes['curved']+=1
        assert parity_on_base(h,S)==1
        assert sum(h[x]!=x for x in S)==2
assert classes=={'flat':60,'curved':60}

# ----- S3 normal-subgroup / quotient minimality -----
S3=tuple(permutations(range(3)))
ID=(0,1,2)

def comp(g,h): return tuple(g[h[i]] for i in range(3))
def inv(g):
    out=[0]*3
    for i,x in enumerate(g): out[x]=i
    return tuple(out)
def parity(p): return sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2

normal=[]
for mask in range(1<<6):
    H={S3[i] for i in range(6) if mask>>i & 1}
    if ID not in H: continue
    if not all(comp(a,b) in H for a in H for b in H): continue
    if not all(inv(a) in H for a in H): continue
    if not all(comp(comp(g,h),inv(g)) in H for g in S3 for h in H): continue
    normal.append(H)
assert sorted(len(H) for H in normal)==[1,3,6]
A3=next(H for H in normal if len(H)==3)
assert all(parity(h)==0 for h in A3)

# Charge-only quotient by A3 merges exactly the three transpositions.
trans=[p for p in S3 if parity(p)==1]
assert len(trans)==3
for a in trans:
    for b in trans:
        assert comp(inv(a),b) in A3

# Any composition-respecting group quotient that keeps all three transpositions
# distinct must have trivial kernel.
for H in normal:
    if len(H)==1: continue
    distinct=True
    for a,b in combinations(trans,2):
        if comp(inv(a),b) in H:
            distinct=False
    assert not distinct

# ----- history compression witness -----
# Same start/end triad and same event count but different charge.
assert flat[0]==flat[-1]==curved[0]==curved[-1]
assert len(flat)==len(curved)
assert parity_on_base(hf,S0)!=parity_on_base(hc,S0)

print('PASS_X6_ACTIVE_TRIAD_HOLONOMY_V17')
print('simple_triangles',len(triangles))
print('flat_triangles',classes['flat'])
print('curved_triangles',classes['curved'])
print('same_endpoint_same_count_charge_collision',True)
print('S3_normal_subgroup_orders',tuple(sorted(len(H) for H in normal)))
print('charge_only_minimal_group_quotient','C2')
print('exact_compositional_odd_lift_state','full S3')
print('physical_transport_law_admitted',False)
