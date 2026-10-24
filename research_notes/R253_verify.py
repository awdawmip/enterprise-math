#!/usr/bin/env python3
"""R253: exact positive BRC restricted 6-axis affine observer/provenance test.

Source-semantic correspondence: Affine (diag(eps,eps,1,1,1,1), k e1),
ControlPacket.from_edges/then. Local model only; NOT a native package import.
"""
from collections import Counter, defaultdict
from math import ceil, comb, log2
import json
import sys

# Every outgoing edge has unit weight and multiplicity one.
# edge-id 0/1 is the source-local alternative selector; paths record its order.
EDGES = {
    0: ((2, (-1,-1)), (2, (1,-1))),
    1: ((0, (-1,-1)), (0, (1,-1))),
    2: ((1, (1, 1)), (2, (1,-1))),
}

def affine_then(first, later):
    eps,k = first
    eta,b = later
    return (eta*eps, eta*k+b)

def inverse_anchor(effect):
    eps,k=effect
    return -eps*k

def from_anchor_holonomy(p,eps):
    """Exact inverse: affine map with given inverse-anchor and holonomy."""
    return (eps, -eps*p)

def brc_step(h):
    output=Counter()
    for (q, eps,k),count in h.items():
        for target, effect in EDGES[q]:
            e,v=affine_then((eps,k),effect)
            output[(target,e,v)]+=count
    return output

def anchor_hist(hist):
    out=Counter()
    for (q,e,k),count in hist.items():
        out[-e*k]+=count
    return out

def tagged_hist(hist, keep_terminal=True):
    out=Counter()
    for (q,e,k),count in hist.items():
        key=(q,-e*k,e) if keep_terminal else (-e*k,e)
        out[key]+=count
    return out

def full_hist(hist,keep_terminal=True):
    out=Counter()
    for (q,e,k),count in hist.items():
        key=(q,e,k) if keep_terminal else (e,k)
        out[key]+=count
    return out

def restore_hist_from_tag(hist,keep_terminal=True):
    out=Counter()
    for key,count in hist.items():
        if keep_terminal:
            q,p,e=key
            new_key=(q,*from_anchor_holonomy(p,e))
        else:
            p,e=key
            new_key=from_anchor_holonomy(p,e)
        out[new_key]+=count
    return out

def brute_paths(start,depth):
    items=[(start,1,0,'')]
    for _ in range(depth):
        nxt=[]
        for q,e,k,path in items:
            for i,(t,(ee,b)) in enumerate(EDGES[q]):
                nxt.append((t,ee*e,ee*k+b,path+str(i)))
        items=nxt
    groups=defaultdict(list)
    for q,e,k,path in items:
        groups[(q,e,k)].append(path)
    return groups

counts={q:Counter({(q,1,0):1}) for q in (0,1)}
results=[]
first_path_collision={}
first_tagged_difference=None
for m in range(49):
    # The tagged observer (terminal control, inverse anchor, holonomy)
    # is exactly equivalent to (terminal control, affine effect).
    for start in (0,1):
        h=counts[start]
        assert sum(h.values())==2**m
        assert all(v>0 for v in h.values())
        assert all(e in (-1,1) and abs(k)<=m and k%2==m%2 for q,e,k in h)
        assert restore_hist_from_tag(tagged_hist(h))==full_hist(h)
        assert restore_hist_from_tag(tagged_hist(h,False),False)==full_hist(h,False)
        want=Counter({m-2*j:comb(m,j) for j in range(m+1)})
        assert anchor_hist(h)==want
    if first_tagged_difference is None and tagged_hist(counts[0],False)!=tagged_hist(counts[1],False):
        first_tagged_difference=m
    h=counts[0]
    M=max(h.values())
    worst_bits=(M-1).bit_length() # ceil(log2 M), exactly, incl M=1
    lower=ceil((2**m)/(6*(m+1)))
    assert M>=lower
    results.append({"m":m,"paths":str(2**m),"terminal_full_effect_support":len(h),
                    "max_provenance_fiber":str(M),"minimum_worst_fiber_tag_bits":worst_bits,
                    "pigeonhole_lower_bound":str(lower)})
    if m<=13:
        brute=brute_paths(0,m)
        assert Counter({k:len(v) for k,v in brute.items()})==h
        if not first_path_collision:
            collided=[(k,v) for k,v in sorted(brute.items()) if len(v)>1]
            if collided:
                first_path_collision={"m":m,"fibers":[{"observable":str(k),"ordered_edge_words":v} for k,v in collided]}
    counts={q:brc_step(counts[q]) for q in counts}
assert first_tagged_difference==3,first_tagged_difference
assert first_path_collision['m']==3,first_path_collision
# Exact R252 effect-depth-three witness in repaired inverse-anchor coordinates.
c={j:Counter({(j,1,0):1}) for j in (0,1)}
for _ in range(3): c={j:brc_step(c[j]) for j in c}
a=tagged_hist(c[0],False); b=tagged_hist(c[1],False)
assert a[(-1,-1)]==3 and b[(-1,-1)]==2
assert a[(-1,1)]==0 and b[(-1,1)]==1
assert a[(1,1)]==3 and b[(1,1)]==2
assert a[(1,-1)]==0 and b[(1,-1)]==1
assert anchor_hist(c[0])==anchor_hist(c[1])

report={
  "schema":"EM_R253_HOLONOMY_REPAIR_AND_PROVENANCE_GROWTH_V1",
  "source_model":"R252 positive unit-weight three-control two-edge six-axis Affine subalgebra",
  "current_global_snapshot":"420ddde0f088d90160ac4fdd5cf12ec873d82fc1",
  "current_source_snapshot":"5404753a7a923c4ca9a3654256c057db878a7f35",
  "native_source_execution":False,
  "reuses":"R252 exact edge model; current brc_transport.Affine.then/.inverse and brc_control_port.ControlPacket.from_edges/.then semantics",
  "tag_reconstruction_formula":"effect=(epsilon,-epsilon*p*e1), p=inverse_anchor(effect), epsilon in {+1,-1}",
  "first_anchor_plus_holonomy_difference_between_start0_and_start1":first_tagged_difference,
  "first_terminal_plus_affine_provenance_collision_start0":first_path_collision,
  "verified_depths_all_DP":"0..48 inclusive",
  "verified_explicit_word_enumeration":"0..13 inclusive",
  "sharp_bit_scope":"one holonomy bit recovers FULL AFFINE EFFECT, not ordered path provenance",
  "provenance_lower_bound":"ceil(2^m/[6(m+1)]) histories per largest terminal+full-effect fiber; tag bits Omega(m)",
  "selected_depths":[r for r in results if r['m'] in (0,1,2,3,8,12,16,24,32,40,48)],
  "status":"PASS"
}
print(json.dumps(report,ensure_ascii=False,sort_keys=True,indent=2))
