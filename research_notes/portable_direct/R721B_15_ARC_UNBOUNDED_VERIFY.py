"""R721b: exact 15-directed-arc CNB six-holonomy all-length witness.
No numerical packages. Boolean lifted-state eventual fixed point + literal DFS.
"""
import json

ROOT='012'
FRAMES=('012','021','102','120','201','210')
EDGES='''012>024 012>123 012>124
013>012 013>023
023>012 023>013
024>023 024>124
123>013 123>023 123>134
124>123 124>134
134>013'''.split()
assert len(EDGES)==len(set(EDGES))==15
assert all(len(set(e[:3]) & set(e[4:]))==2 for e in EDGES)
A={}
for e in EDGES:
    u,v=e.split('>')
    A.setdefault(u,[]).append(v)

def move(frame,to):
    outgoing=next(x for x in frame if x not in to)
    incoming=next(x for x in to if x not in frame)
    return frame.replace(outgoing,incoming)

def dfs_hist(m):
    counts={h:0 for h in FRAMES}
    def visit(prev,here,first,frame,d):
        if d==m:
            if here==ROOT and prev!=first:counts[frame]+=1
            return
        for nxt in A.get(here,[]):
            if nxt!=prev:
                visit(here,nxt,nxt if first is None else first,move(frame,nxt),d+1)
    visit(None,ROOT,None,ROOT,0)
    return counts

def propagate_states(states):
    nex=set();holonomy=set()
    for prev,here,frame,first in states:
        for nxt in A.get(here,[]):
            if nxt==prev:continue
            f=move(frame,nxt)
            nex.add((here,nxt,f,first))
            if nxt==ROOT and here!=first:holonomy.add(f)
    return nex,holonomy

states={(ROOT,w,move(ROOT,w),w) for w in A[ROOT]}
reached={1:len(states)}; supports={}; past={frozenset(states):1}
cycle=None
for m in range(2,100):
    states,obs=propagate_states(states)
    reached[m]=len(states)
    supports[m]=sorted(obs)
    if m>=4:assert obs==set(FRAMES), (m,obs)
    frozen=frozenset(states)
    if frozen in past:
        cycle={'first_seen_at_length':past[frozen], 'repeated_at_length':m,
               'period':m-past[frozen], 'state_count':len(states)}
        break
    past[frozen]=m
assert cycle=={'first_seen_at_length':10,'repeated_at_length':11,
               'period':1,'state_count':270},cycle
# State recurrence is deterministic; equality of states at m=10 and m=11
# proves equality for all subsequent m and thus full six-state support forever.
for m in range(4,8):
    observed=dfs_hist(m)
    assert set(h for h,n in observed.items() if n)>={*FRAMES}

out={
 'schema':'R721B_15_ARC_CNB_UNBOUNDED_S3_V1',
 'status':'R721B_15_ARC_ALL_LENGTHS_EXACT_PASS',
 'domain':{'accessible_axes':'01234','root':'012','edges':len(EDGES),
           'possible_directed_arcs':60, 'model':'V17 rooted cyclic nonbacktracking'},
 'arcs':EDGES,
 'length_supports_4_through_11':{str(m):supports[m] for m in range(4,12)},
 'lifted_state_counts_by_length':{str(m):reached[m] for m in range(1,12)},
 'eventual_fixed_point_certificate':cycle,
 'exhaustive_DFS_histograms':{str(m):dfs_hist(m) for m in range(4,8)},
 'proof':'Identical lifted reachable-state sets at steps 10 and 11 force identical future sets by deterministic propagation; all six holonomies are supported at steps 4..11.'
}
print(json.dumps(out,indent=2,ensure_ascii=False))
