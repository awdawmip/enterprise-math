#!/usr/bin/env python3
"""R284FQ: exact n=16 exclusion at q=2,u=1 in the reset-free four-phase model.

Completeness:
(1) seven-pattern coordinate-permutation histogram enumeration;
(2) all six necessary last-update flow cuts;
(3) all first-bit choices on all edges;
(4) for remaining patterns, every homogeneous-type prefix count and every
    omission subset (size <= 2), from all reachable stable source states.
Any legal fixed order induces a path in the prefix-count lattice; no surviving
histogram has such a path on all four edges. All arithmetic is exact integer.
"""
from itertools import combinations
from math import comb
import json

Q,U,N=2,1,16
PAIRS=((0,1),(1,2),(2,3),(3,0),(0,2),(1,3))
PAT={}
for p in range(1,8):
    bits=(0,p&1,(p>>1)&1,(p>>2)&1)
    transitions=tuple(i for i in range(4) if bits[i]!=bits[(i-1)%4])
    last=tuple(next((i-t)%4 for t in range(4) if (i-t)%4 in transitions)
               for i in range(4))
    PAT[p]=(bits,last)

def compositions(n):
    for marks in combinations(range(n+6),6):
        seq=(-1,)+marks+(n+6,)
        yield tuple(seq[i+1]-seq[i]-1 for i in range(7))

def cuts_for_pair(i,j):
    edges=[(p-1,PAT[p][1][i],4+PAT[p][1][j]) for p in range(1,8)
           if PAT[p][0][i]!=PAT[p][0][j]]
    opts={}
    for verts in range(1,256):
        columns=tuple(p for p,l,r in edges if (verts>>l)&1 and (verts>>r)&1)
        if columns:
            opts[columns]=min(opts.get(columns,9),verts.bit_count())
    return [(columns,Q*k+2*U+1) for columns,k in opts.items()]

CUTS=[cuts_for_pair(*ij) for ij in PAIRS]

def necessary(hist):
    distance=(2*Q+4*U+1,)*4+(2*(Q+U)+1,)*2
    for (i,j),need,cuts in zip(PAIRS,distance,CUTS):
        if sum(hist[p-1] for p in range(1,8)
               if PAT[p][0][i]!=PAT[p][0][j])<need:
            return False
        if not any(sum(hist[p] for p in cols)>=threshold
                   for cols,threshold in cuts):
            return False
    return True

def words_and_types(hist):
    pp=tuple(p for p,k in enumerate(hist,1) for _ in range(k))
    w=tuple(0 if phase==0 else sum(((p>>(phase-1))&1)<<k
            for k,p in enumerate(pp)) for phase in range(4))
    return w,pp

def stable(words,phase):
    groups=[[] for _ in range(4)]
    for k in range(N):
        for age in range(1,5):
            edge=(phase-age)%4
            if (words[edge]^words[(edge+1)%4])>>k&1:
                groups[edge].append(k)
                break
        else:
            raise AssertionError("constant column")
    masks=[0]
    for group in groups:
        errors=[sum(1<<k for k in sub)
                for r in range(min(Q,len(group))+1)
                for sub in combinations(group,r)]
        masks=[a|b for a in masks for b in errors]
    return {words[phase]^mask for mask in masks}

def observed_masks(states):
    y=bytearray(1<<N)
    for phase,words in enumerate(states):
        for w in words:
            y[w]|=1<<phase
            for k in range(N):y[w^(1<<k)]|=1<<phase
    if any(v.bit_count()>1 for v in y):
        raise AssertionError("flow-cut candidate with stable collision")
    x=bytearray(y)
    for w in range(1<<N):
        for k in range(N):x[w]|=y[w^(1<<k)]
    return x

def first_bit_choices(words,states,forced,edge):
    next_phase=(edge+1)%4
    old,new=1<<edge,1<<next_phase
    change=words[edge]^words[next_phase]
    options=[]
    for bit in range(N):
        mask=1<<bit
        if not change&mask:continue
        target=words[next_phase]&mask
        for s in states[edge]:
            x=(s&~mask)|target
            label=forced[x]
            if label & ~(old|new) or label&(old|new)==(old|new):
                break
        else:
            options.append(bit)
    return options

def local_grid(words,pp,states,forced,edge):
    next_phase=(edge+1)%4
    old,new=1<<edge,1<<next_phase
    allowed=old|new
    groups=[tuple(k for k,p in enumerate(pp)
                  if p==typ and PAT[typ][0][edge]!=PAT[typ][0][next_phase])
            for typ in sorted(set(pp))
            if PAT[typ][0][edge]!=PAT[typ][0][next_phase]]
    assert 1<=len(groups)<=2
    if len(groups)==1:groups.append(())
    amax,bmax=map(len,groups)
    safe={}
    for a in range(amax+1):
      for b in range(bmax+1):
        if not a+b:continue
        attempted=groups[0][:a]+groups[1][:b]
        mask=sum(1<<k for k in attempted)
        omissions=[0]+[sum(1<<k for k in sub)
                 for r in range(1,min(Q,len(attempted))+1)
                 for sub in combinations(attempted,r)]
        good=True
        for source in states[edge]:
            base=(source&~mask)|(words[next_phase]&mask)
            for omitted in omissions:
                physical=base ^ ((source^words[next_phase])&omitted)
                found=forced[physical]
                if found&~allowed or found&allowed==allowed:
                    good=False
                    break
            if not good:break
        safe[(a,b)]=good
    reached={(0,0)}
    for total in range(amax+bmax):
        for a,b in tuple(reached):
            if a+b!=total:continue
            for next_state in ((a+1,b),(a,b+1)):
                na,nb=next_state
                if na<=amax and nb<=bmax and safe.get(next_state,False):
                    reached.add(next_state)
    return {"groups":(amax,bmax),"local_safe_nodes":sum(safe.values()),
            "all_nonempty_nodes":len(safe),"locally_safe_path":(amax,bmax) in reached}

def main():
    viable=[h for h in compositions(N) if necessary(h)]
    assert len(viable)==36
    first_pass=[]
    for h in viable:
        words,pp=words_and_types(h)
        states=[stable(words,i) for i in range(4)]
        forced=observed_masks(states)
        choices=[first_bit_choices(words,states,forced,i) for i in range(4)]
        if all(choices):first_pass.append((h,words,pp,states,forced,choices))
    assert len(first_pass)==8
    final=[]
    for h,words,pp,states,forced,choices in first_pass:
        grid=[local_grid(words,pp,states,forced,i) for i in range(4)]
        assert not all(g["locally_safe_path"] for g in grid)
        final.append({"histogram":h,"words":words,
                      "stable_sizes":[len(z) for z in states],
                      "first_bit_choices_per_edge":[len(x) for x in choices],
                      "prefix_grid":grid})
    result={"model":{"q":Q,"u":U,"n":N},
            "histograms_exhausted":comb(N+6,6),
            "six_cut_survivors":len(viable),
            "histograms_with_legal_first_bit_each_edge":len(first_pass),
            "histograms_with_locally_safe_path_all_edges":0,
            "conclusion":"n_min(2,1)>=17",
            "remaining_eight":final}
    print(json.dumps(result,sort_keys=True,indent=2))

if __name__=="__main__":
    main()
