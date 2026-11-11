"""R726: exact reversal duality for R725 sharp five-axis V17/CNB 15-arc carriers.
Uses only Python 3 standard library; arbitrary-precision integer counts.
"""
import json
from collections import defaultdict
from itertools import combinations, permutations

ROOT = '012'
TRIADS = tuple(''.join(t) for t in combinations('01234', 3))
ARCS = tuple((a,b) for a in TRIADS for b in TRIADS if len(set(a)&set(b))==2)
ARC_ID = {edge:i for i,edge in enumerate(ARCS)}
FRAMES = tuple(sorted(''.join(t) for t in permutations(ROOT)))
REPS = (211733226574,423074469777,5363347296468,14021360160796,
        378233292275810,2287401872294258)

def reverse_mask(mask):
    return sum(1<<ARC_ID[b,a] for i,(a,b) in enumerate(ARCS) if (mask>>i)&1)

def relabel_mask(mask, mapping):
    def renamed(t):
        return ''.join(sorted(mapping[x] for x in t))
    return sum(1<<ARC_ID[renamed(a),renamed(b)] for i,(a,b) in enumerate(ARCS)
               if (mask>>i)&1)

def orbit(mask):
    out = set()
    for p in permutations('012'):
        for q in permutations('34'):
            mapping = dict(zip('01234',p+q))
            out.add(relabel_mask(mask, mapping))
    return out

def step(frame, target):
    leaving = next(x for x in frame if x not in target)
    arriving = next(x for x in target if x not in frame)
    return frame.replace(leaving, arriving)

def count_paths(mask, limit=12):
    """Count positive rooted directed length-m CNB walks by final frame."""
    outgoing = {u:tuple(b for i,(a,b) in enumerate(ARCS)
                        if a==u and (mask>>i)&1) for u in TRIADS}
    curr = defaultdict(int)
    for neighbor in outgoing[ROOT]:
        curr[(ROOT, neighbor, step(ROOT,neighbor), neighbor)] += 1
    result = {}
    for m in range(2,limit+1):
        nxt = defaultdict(int)
        for (previous,current,frame,first), count in curr.items():
            for neighbor in outgoing[current]:
                if neighbor != previous:
                    nxt[(current,neighbor,step(frame,neighbor),first)] += count
        curr = nxt
        if m>=4:
            hist={fr:0 for fr in FRAMES}
            for (previous,current,frame,first), count in curr.items():
                if current==ROOT and previous!=first:
                    hist[frame]+=count
            result[m]=hist
    return result

def inverse_frame(frame):
    return ''.join(ROOT[frame.index(x)] for x in ROOT)

def main():
    assert len(ARCS)==60 and len(FRAMES)==6
    assert [m.bit_count() for m in REPS]==[15]*6
    assert all(len(orbit(m))==12 for m in REPS)
    assert not any(orbit(REPS[i]) & orbit(REPS[j])
                   for i in range(6) for j in range(i+1,6))
    pairs=[]
    for i,mask in enumerate(REPS):
        d=reverse_mask(mask)
        matches=[j+1 for j,rep in enumerate(REPS) if d in orbit(rep)]
        assert len(matches)==1
        pairs.append(matches[0])
    assert pairs==[2,1,4,3,6,5]
    assert all(reverse_mask(reverse_mask(m))==m for m in REPS)
    assert not any(reverse_mask(m) in orbit(m) for m in REPS)
    assert len(set().union(*(orbit(m) for m in REPS)))==72
    assert {len(orbit(m) | orbit(reverse_mask(m))) for m in REPS}=={24}

    tables=[count_paths(mask,12) for mask in REPS]
    by_length={str(m):[sum(t[m].values()) for t in tables] for m in range(4,13)}
    for vals in by_length.values():
        assert vals[0]==vals[1] and vals[2]==vals[3] and vals[4]==vals[5]
    for i,mask in enumerate(REPS):
        reverse_counts=count_paths(reverse_mask(mask),12)
        for m in range(4,13):
            assert all(tables[i][m][frame]==reverse_counts[m][inverse_frame(frame)]
                       for frame in FRAMES)
    assert [by_length['6'][i] for i in (0,2,4)]==[13,14,6]
    assert [by_length['7'][i] for i in (0,2,4)]==[42,43,24]
    return {
        'schema':'R726_FIVE_AXIS_DIRECTION_REVERSAL_DUALITY_V1',
        'status':'R726_DIRECTION_REVERSAL_DUALITY_PASS',
        'source':'R725 at a9ba60cab51fc98e4b39f73e5d0eda7f49c51bb3',
        'frozen_science':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
        'six_representative_masks':list(REPS),
        'orbit_image_under_arc_reversal':pairs,
        'extended_orbit_count':3,
        'extended_orbit_sizes':[24,24,24],
        'all_length_orbit_count_after_unorientation':2,
        'full_length_labeled_networks':48,
        'short_horizon_labeled_networks':24,
        'positive_CNB_path_counts_by_representative':by_length,
        'finite_integer_check_length_range':[4,12],
        'exact_scope':'R725 72-network complete classification and mathematical inversion bijection for all m>=4'
    }

if __name__=='__main__':
    print(json.dumps(main(),ensure_ascii=False,indent=2,sort_keys=True))
