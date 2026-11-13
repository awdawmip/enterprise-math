#!/usr/bin/env python3
"""953-event / 2,880-prefix actual R5 word corpus full Fenwick cross-check.

Requires two unmodified predecessor source files at:
research_notes/brc_r5_dual_zero_right_persistence_20261112/VERIFY_RIGHT_PERSISTENCE.py
research_notes/brc_r5_dual_zero_right_persistence_20261112/VERIFY_TRIE_CODEC.py
Pinned predecessor commit: ad7013218d0474e1e942906e3beadec1eccb9213
They are intentionally NOT duplicated in this research branch.
"""
from pathlib import Path
from collections import defaultdict
from fractions import Fraction as F
from time import perf_counter
import sys

predecessor=(Path(__file__).resolve().parents[1] /
    "brc_r5_dual_zero_right_persistence_20261112")
if not all((predecessor/name).is_file()
           for name in ("VERIFY_RIGHT_PERSISTENCE.py","VERIFY_TRIE_CODEC.py")):
    raise FileNotFoundError(
        "Materialize both exact predecessor scripts from immutable commit "
        "ad7013218d0474e1e942906e3beadec1eccb9213 under "+str(predecessor))
sys.path.insert(0,str(predecessor))
import VERIFY_TRIE_CODEC as prior

words=prior.words
assert len(words)==1065 and sum(map(len,words.values()))==6379
root={}
for pair,word in words.items():
    node=root
    for a in word:node=node.setdefault(a,{})
    assert "#" not in node
    node["#"]=pair

pairs=[]; intervals={}; node_count=0
def dfs(node, prefix=()):
    global node_count
    node_count+=1
    start=len(pairs)
    if "#" in node:pairs.append(node["#"])
    for a in sorted(k for k in node if k!="#"):
        dfs(node[a],prefix+(a,))
    intervals[prefix]=(start,len(pairs))
dfs(root)
T=len(pairs)
assert (T,node_count,len(intervals))==(1065,2880,2880)
rank={p:i for i,p in enumerate(pairs)}
by_wall=defaultdict(list)
for q,n in words:
    by_wall[(1-F(36*q,n))/23].append((q,n))
events=sorted(by_wall.items())
assert len(events)==953

bit=[0]*(T+1)
active=set(); writes=0
start=perf_counter()
for r,added in events:
    for p in added:
        active.add(p)
        j=rank[p]+1
        while j<=T:
            bit[j]+=1; writes+=1; j+=j&-j
    def prefix(j):
        v=0
        while j:
            v+=bit[j];j-=j&-j
        return v
    indicators=[int(p in active) for p in pairs]
    direct=[0]
    for v in indicators:direct.append(direct[-1]+v)
    for lo,hi in intervals.values():
        assert prefix(hi)-prefix(lo)==direct[hi]-direct[lo]
    assert prefix(T)==len(active)
seconds=perf_counter()-start
assert writes==6277 and len(active)==T

# Exact logical packed fields (excluding static event keys and navigation).
N,E=2880,2879
bp_bits=2*N+4*E+N
new_bits=bp_bits+11*T+11*T+27
old_bits=(N+E)+4*E+N+12*T+T+11*N
assert (bp_bits,new_bits,old_bits)==(20156,43613,65680)
assert ((new_bits+7)//8,(old_bits+7)//8)==(5452,8210)

print("ORIGINAL_SELECTED_CERTIFICATE_WORDS",T)
print("ORIGINAL_TRIE_NODES",node_count)
print("DISTINCT_THRESHOLDS",len(events))
print("EXACT_PREFIX_QUERIES_VERIFIED",len(events)*node_count)
print("EXACT_FENWICK_COUNTER_WRITES",writes)
print("FULL_QUERY_LOOP_SECONDS_LOCAL",round(seconds,6))
print("BP_INDEXED_FENWICK_PACKED_BYTES",5452)
print("PRIOR_INDEXED_PREFIX_COUNTER_PACKED_BYTES",8210)
print("PASS_R5_FULL_WORD_CORPUS_FENWICK_953_BY_2880")
