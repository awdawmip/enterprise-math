#!/usr/bin/env python3
"""Finite exact six-axis C12 root-fiber/shortest-BRC branch check (author-scoped)."""
from itertools import combinations, product
from collections import defaultdict, Counter
import hashlib
import json

DIM = 6
Z = (0,) * DIM

def unit(k, sign=1):
    out = [0] * DIM
    out[k] = sign
    return tuple(out)

def add(a, b):
    return tuple(x+y for x,y in zip(a,b))

def subtract(a, b):
    return tuple(x-y for x,y in zip(a,b))

def taxicab(z):
    return sum(abs(x) for x in z)

def sign_root(frame, direction):
    i,j,k = frame
    if direction == 1:
        return subtract(unit(k), unit(j))
    return subtract(unit(j), unit(k))

def macro_orbit(frame, direction):
    i,j,k=frame
    return ((unit(i),unit(j,-1),unit(k),unit(i,-1),unit(j),unit(k,-1))
            if direction==1 else
            (unit(i),unit(k,-1),unit(j),unit(i,-1),unit(k),unit(j,-1)))

def trace(frame, direction, word):
    phases=macro_orbit(frame,direction)
    states=[]
    for r in range(6):
        a,b=phases[r],phases[(r+1)%6]
        d=subtract(b,a)
        if taxicab(d)!=2 or sum(int(c!=0) for c in d)!=2:
            raise ValueError(('macro is not a two-step displacement',frame,direction,r))
        middle=add(a,b) if word[r] else Z
        if taxicab(subtract(middle,a))!=1 or taxicab(subtract(b,middle))!=1:
            raise ValueError(('not shortest two primitive steps',frame,direction,r,word))
        states.extend((a,middle))
    return tuple(states)

def run():
    groups=defaultdict(list)
    total=0
    visible=0
    macro_edge_checks=0
    for frame in combinations(range(DIM),3):
        for direction in (1,-1):
            for word in product((0,1), repeat=6):
                states=trace(frame,direction,word)
                total+=1
                macro_edge_checks+=6
                if states[3] == Z:
                    if word[1] != 0:
                        raise ValueError('nonzero root disappeared')
                    continue
                visible+=1
                if word[1] != 1 or states[3] != sign_root(frame,direction):
                    raise ValueError('incorrect signed root')
                groups[states[3]].append((frame,direction,word,states[4:7]))
    if total != 2560 or visible != 1280 or len(groups) != 20:
        raise ValueError(('total/root census',total,visible,len(groups)))
    histogram=Counter()
    future=Counter()
    outputs=0
    for root,records in groups.items():
        frames={frame for frame,direction,word,tail in records}
        directions={direction for frame,direction,word,tail in records}
        if len(directions)!=1:
            raise ValueError(('root-direction mixing',root))
        direction=next(iter(directions))
        j=next(iter(frames))[1]
        k=next(iter(frames))[2]
        if any(frame[1:] != (j,k) for frame in frames):
            raise ValueError(('root not identifying j,k',root))
        m=j
        if len(frames)!=m or len(records)!=32*m:
            raise ValueError(('root-frame/branch cardinality',root))
        expected_x4=unit(k if direction==1 else j)
        if {t[0] for _,_,_,t in records}!={expected_x4}:
            raise ValueError(('x4 non-deterministic',root))
        observed_x5=Counter(t[1] for _,_,_,t in records)
        if observed_x5[Z]!=16*m or len(observed_x5)!=m+1:
            raise ValueError(('mixed second step',root,observed_x5))
        for frame in frames:
            i=frame[0]
            expected_x5=subtract(expected_x4,unit(i))
            if observed_x5[expected_x5]!=16:
                raise ValueError(('wrong BRC exterior count',root,frame))
        if len({t[2] for _,_,_,t in records})!=m:
            raise ValueError(('wrong third step frame ambiguity',root))
        for frame,direction2,word,t in records:
            i=frame[0]
            if t[2]!=unit(i,-1):
                raise ValueError(('x6 cannot recover frame',root,frame))
            x5_expected=(subtract(expected_x4,unit(i)) if word[2] else Z)
            if t[1]!=x5_expected:
                raise ValueError(('x5 branch mismatch',root,frame))
        histogram[str(m)]+=1
        future[str(m+1)]+=1
        outputs+=len(observed_x5)
    result={
        'schema':'EM_X6_UNIT79_FULL_BRANCH_ROOT_FIBER_EXACT_V1',
        'domain':'six signed axes, 20 ascending triads, both q/q^-1 orientations, each of 64 two-step shortest-path branch words',
        'axis_index_base':0,
        'branch_semantics':{'0':'INNER via anchor Cell (zero in local chart)','1':'OUTER via a_r+a_{r+1}'},
        'total_labeled_paths':total,
        'native_macro_edge_two_shortest_path_checks':macro_edge_checks,
        'nonzero_root_compatible_paths':visible,
        'distinct_nonzero_signed_root_cells':len(groups),
        'root_frame_fiber_histogram':dict(sorted(histogram.items())),
        'x5_distinct_outcome_histogram':dict(sorted(future.items())),
        'sum_distinct_x5_outcomes_across_roots':outputs,
        'x4_determined_given_signed_root':True,
        'all_20_roots_x5_nondeterministic_when_both_brc_branches_allowed':True,
        'x5_inner_mass_per_root':'16*m, where m is the number of eligible source frames',
        'x5_each_outer_mass_per_root':16,
        'x6_recovers_lost_source_i_for_every_labeled_path':True,
        'truth_scope':'exact finite exhaustive all20 x both directions x all64 shortest-branch words, no R063/Helly full benchmark or current source task admission',
        'failed_checks':0
    }
    return result

if __name__=='__main__':
    print(json.dumps(run(), sort_keys=True, ensure_ascii=False, indent=2))
