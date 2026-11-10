"""Finite state/transition checks for RegionEvidence.

The complete request vector is a verification oracle.  Production RegionEvidence
receives only declared controlled writes or an already-proved empty prefix.
"""
from __future__ import annotations

from collections import Counter
from itertools import product
from pathlib import Path
import argparse
import json

from region import RegionEvidence

ROOT = Path(__file__).resolve().parent


def verify(region, codes, colors, *, all_preferred=False):
    B = region.modulus
    delta, prefix = region.delta, region.prefix
    expected_members = [code % B if code and code % delta == prefix else None
                        for code in codes]
    assert region.members == expected_members
    expected_refs = dict(Counter(x for x in expected_members if x is not None))
    assert region.refs == expected_refs
    assert len(region.refs.active) == len(set(region.refs.active))
    assert {x for x,n in enumerate(region.refs.values) if n} == set(expected_refs)
    assert all(region.refs.positions[x] == i
               for i,x in enumerate(region.refs.active))
    free = {x for x in range(B) if x % delta == prefix and x not in expected_refs}
    assert region.tree.free_count == len(free)
    assert {x for x in range(B) if region.contains(x)} == free
    assert len(region.touched) == len(set(region.touched))
    assert {i for i,m in enumerate(region.marked) if m} == set(region.touched)
    assert all(region.marked[i] for i,x in enumerate(region.members) if x is not None)
    queries = 0
    for start in range(B):
        options = [c for c in range(colors) if (start+c) % B in free]
        expected = options[0] if options else None
        assert region.select(start, colors) == expected
        queries += 1
        if all_preferred:
            for preferred in range(B):
                color = (preferred-start) % B
                want = color if preferred in free and color < colors else expected
                assert region.select(start, colors, preferred) == want
                queries += 1
    mu = colors // delta
    if len(expected_refs) < mu:
        assert all(any((start+c) % B in free for c in range(colors))
                   for start in range(B))
    return queries


def make(slots, width, level, prefix, codes):
    region = RegionEvidence(slots, width)
    initial = [0] * slots
    # Empty code 0 means no request.  The prefix is therefore actually empty,
    # including when it contains the residue 0 of a future nonempty code B.
    assert not any(code and code % (1 << level) == prefix for code in initial)
    region.acquire(level, prefix)
    for slot, code in enumerate(codes):
        region.bind(slot, code)
    return region


def exhaustive(slots=2, widths=(2,3)):
    rows = []
    for width in widths:
        B, colors = 1 << width, slots + 1
        states = transitions = reacquisitions = queries = 0
        for level in range(width+1):
            for prefix in range(1 << level):
                for codes in product(range(B+1), repeat=slots):
                    initial = make(slots, width, level, prefix, codes)
                    queries += verify(initial, codes, colors, all_preferred=True)
                    states += 1
                    operations = ([('bind',s,k) for s in range(slots) for k in range(B+1)]
                                  + [('copy',d,s) for d in range(slots) for s in range(slots)]
                                  + [('drop',s) for s in range(slots)])
                    for operation in operations:
                        region = make(slots, width, level, prefix, codes)
                        new_codes = list(codes)
                        if operation[0] == 'bind':
                            _, slot, code = operation
                            region.bind(slot, code); new_codes[slot] = code
                        elif operation[0] == 'copy':
                            _, dest, src = operation
                            region.copy(dest, src); new_codes[dest] = new_codes[src]
                        else:
                            _, slot = operation
                            region.drop(slot); new_codes[slot] = 0
                        queries += verify(region, new_codes, colors)
                        transitions += 1
                    # Reacquisition is permitted only where the current table
                    # actually contains no nonempty request in the new prefix.
                    for next_level in range(width+1):
                        for next_prefix in range(1 << next_level):
                            if any(code and code % (1 << next_level) == next_prefix
                                   for code in codes):
                                continue
                            region = make(slots, width, level, prefix, codes)
                            region.acquire(next_level, next_prefix)
                            assert region.touched == [] and not any(region.marked)
                            queries += verify(region, codes, colors)
                            reacquisitions += 1
        rows.append(dict(slots=slots,width=width,modulus=B,colors=colors,
                         initial_states=states,controlled_transitions=transitions,
                         empty_prefix_reacquisitions=reacquisitions,
                         selector_queries=queries))
    return rows


def reuse_family(rounds):
    r, width, colors = 6, 3, 7
    region = RegionEvidence(r,width)
    codes = [0]*r
    # An actual preceding read establishes this prefix.  This control-only
    # test starts at that supplied evidence boundary and performs no old reads.
    region.acquire(1,1)
    snapshots=[]
    for turn in range(rounds):
        start=(1+turn*colors)%8
        color=region.select(start,colors)
        assert color is not None
        key=1+turn*colors+color
        assert key%8 not in {code%8 for code in codes if code}
        region.bind(0,key);codes[0]=key
        assert len(region.refs)==1<colors//2
        assert region.events['acquisitions']==1
        if turn < 8 or turn==rounds-1:
            snapshots.append(dict(turn=turn,target_start=start,key=key,residue=key%8,
                                  free=region.tree.free_count,refs=dict(region.refs)))
    return dict(rounds=rounds,request_slots=r,prefix=[1,1],mu=colors//2,
                initial_observation_boundary='supplied proved empty prefix',
                old_request_bit_reads_after_boundary=0,final_members=region.members,
                final_refs=dict(region.refs),events=region.events,snapshots=snapshots)


def alias_recycling():
    region=RegionEvidence(2,3);region.acquire(1,1);codes=[0,0];rows=[]
    operations=[('bind',0,1),('copy',1,0),('drop',0),('drop',1),
                ('bind',0,8),('bind',1,0),('copy',1,0),('drop',0),('drop',1),
                ('bind',0,3),('copy',1,0),('bind',0,5),('drop',1)]
    for op in operations:
        if op[0]=='bind':region.bind(op[1],op[2]);codes[op[1]]=op[2]
        elif op[0]=='copy':region.copy(op[1],op[2]);codes[op[1]]=codes[op[2]]
        else:region.drop(op[1]);codes[op[1]]=0
        verify(region,codes,3,all_preferred=True)
        rows.append(dict(operation=op,refs=dict(region.refs),free=region.tree.free_count))
    return rows


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--out',default=str(ROOT/'region_control_checks.json'))
    args=parser.parse_args()
    result=dict(status='PASS',scope='Exact finite control states and declared update transitions',
                physical_BRC_execution=False,exhaustive=exhaustive(),
                alias_recycling=alias_recycling(),
                reuse_family=[reuse_family(t) for t in (8,32,128,512)])
    Path(args.out).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(status=result['status'],exhaustive=result['exhaustive'],
                         reuse_family=[dict(rounds=x['rounds'],events=x['events'])
                                       for x in result['reuse_family']]),ensure_ascii=False))


if __name__=='__main__':main()
