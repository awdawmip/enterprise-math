#!/usr/bin/env python3
"""R749SG: exact Walsh ancestry kernel check for signed-Port support paths.

R749SF homogeneous conditional kernel; no native event authorization.
"""
from fractions import Fraction as F
from itertools import combinations, product
from collections import Counter
import json

AX = range(6)
SUP = [frozenset(c) for c in combinations(AX,2)]
EDGES = [(a,b) for a in SUP for b in SUP if len(a & b)==1]
assert len(EDGES)==120
SIG = list(product((-1,1),repeat=3))

def near(b):
    return [c for c in SUP if len(c & b)==1]

def nexts(e):
    a,b=e
    return [(b,c) for c in near(b)]

def state_axes(e):
    return tuple(sorted(e[0]|e[1]))

def forced(e,nxt):
    return nxt[1]==(e[0]^e[1])

def transition(e,nxt,s,theta):
    """Conditioned signed 2-child row; exact Fraction arithmetic."""
    axes=state_axes(e)
    a,b=e
    c=nxt[1]
    target=state_axes(nxt)
    old=dict(zip(axes,s))
    new_ax=next(iter(c-b))
    assert len(c-b)==1
    new={x:old[x] for x in b}
    d={}
    for bit in (-1,1):
        new[new_ax]=bit
        if forced(e,nxt):
            assert new_ax in old
            prob=(1+theta*old[new_ax]*bit)/2
        else:
            prob=F(1,2)
        out=tuple(new[x] for x in target)
        if prob:
            d[out]=d.get(out,F(0))+prob
    assert sum(d.values())==1
    return d

def ancestry_step(e,nxt,anc):
    a,b=e
    c=nxt[1]
    new_ax=next(iter(c-b))
    r={x:anc[x] for x in b}
    if forced(e,nxt) and new_ax in anc and anc[new_ax] is not None:
        origin,h=anc[new_ax]
        r[new_ax]=(origin,h+1)
    else:
        r[new_ax]=None
    assert set(r)==set(nxt[0]|nxt[1])
    return r

def exact_path_kernel(path,theta):
    matrix={}
    for signs in SIG:
        d={signs:F(1)}
        for e,nxt in zip(path,path[1:]):
            u={}
            for s,mass in d.items():
                for t,w in transition(e,nxt,s,theta).items():
                    u[t]=u.get(t,F(0))+mass*w
            d=u
        matrix[signs]=d
    return matrix

def formula(path,theta):
    init=state_axes(path[0])
    anc={x:(x,0) for x in init}
    for e,nxt in zip(path,path[1:]):
        anc=ancestry_step(e,nxt,anc)
    current=state_axes(path[-1])
    k=sum(v is not None for v in anc.values())
    assert len({v[0] for v in anc.values() if v is not None})==k
    rows={}
    for bits in SIG:
        signed_init=dict(zip(init,bits))
        row={}
        for end_bits in SIG:
            signed_end=dict(zip(current,end_bits))
            pr=F(1)
            for x in current:
                v=anc[x]
                if v is None:
                    pr*=F(1,2)
                else:
                    a,h=v
                    pr*=(1+theta**h*signed_init[a]*signed_end[x])/2
            if pr:
                row[end_bits]=pr
        assert sum(row.values())==1
        rows[bits]=row
    return anc,k,rows

def rank_rational(mat):
    a=[list(r) for r in mat]
    rows=len(a)
    cols=len(a[0])
    i=0
    for j in range(cols):
        pivot=next((t for t in range(i,rows) if a[t][j]),None)
        if pivot is None:
            continue
        a[i],a[pivot]=a[pivot],a[i]
        divisor=a[i][j]
        a[i]=[v/divisor for v in a[i]]
        for t in range(rows):
            if t!=i and a[t][j]:
                factor=a[t][j]
                a[t]=[v-factor*w for v,w in zip(a[t],a[i])]
        i+=1
        if i==rows:
            break
    return i

def check(path,theta,rank=False):
    anc,k,pred=formula(path,theta)
    got=exact_path_kernel(path,theta)
    assert got==pred,(path,anc,got,pred)
    if rank:
        mat=[[got[s].get(t,F(0)) for t in SIG] for s in SIG]
        expected=2**sum(v is not None and
                        (theta!=0 or v[1]==0) for v in anc.values())
        assert rank_rational(mat)==expected,(path,expected)
    return k

results={}
for steps in range(1,4):
    tally=Counter()
    total=0
    for e in EDGES:
        def traverse(path):
            if len(path)==steps+1:
                yield path
                return
            for nxt in nexts(path[-1]):
                yield from traverse(path+[nxt])
        for path in traverse([e]):
            anc={x:(x,0) for x in state_axes(path[0])}
            for old,new in zip(path,path[1:]):
                anc=ancestry_step(old,new,anc)
            k=sum(v is not None for v in anc.values())
            # Exhaustive 120*8^steps support-path count, selected independent
            # 8x8 Fraction-kernel comparisons and exact matrix-rank checks.
            if steps==1 or (steps==2 and total%8==0) or \
                    (steps==3 and total%64==0):
                assert check(path,F(8,9),rank=(steps<=2))==k
            tally[k]+=1
            total+=1
    assert total==120*8**steps
    results[str(steps)]={
        "path_count":total,
        "surviving_ancestor_counts":{str(k):tally[k] for k in range(4)}
    }

path=[EDGES[0]]
for _ in range(3):
    e=path[-1]
    path.append((e[1],e[0]^e[1]))
assert check(path,F(0),rank=True)==3
assert check(path,F(1),rank=True)==3

mu_plus={s:F(1+s[0]*s[1],8) for s in SIG}
mu_minus={s:F(1-s[0]*s[1],8) for s in SIG}
assert sum(mu_plus.values())==sum(mu_minus.values())==1
assert all(sum(mu[s]*s[j] for s in SIG)==0
           for mu in (mu_plus,mu_minus) for j in range(3))
mat=exact_path_kernel(path,F(8,9))
for mu,expected in [(mu_plus,F(64,81)),(mu_minus,F(-64,81))]:
    post={t:sum(mu[s]*mat[s].get(t,F(0)) for s in SIG) for t in SIG}
    assert sum(post[t]*t[0]*t[1] for t in SIG)==expected

results.update({
    "status":"PASS",
    "signed_frame_count":960,
    "unsigned_edge_count":120,
    "theta_test":"8/9",
    "conditional_p":"1/2",
    "rank_full_terminal_p_half_by_k":{"0":1,"1":2,"2":4,"3":8},
    "missing_initial_walsh_moments_by_k":{"0":7,"1":6,"2":4,"3":0},
    "boundary_triangle_rank_p_zero":1,
    "boundary_triangle_rank_p_one":8,
    "joint_pair_moment_after_3_forced":"±64/81",
    "native_event_permission":False
})
print(json.dumps(results,indent=2,sort_keys=True))
