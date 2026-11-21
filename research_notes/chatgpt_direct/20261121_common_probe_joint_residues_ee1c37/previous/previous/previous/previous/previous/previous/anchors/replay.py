"""Classify minimum-cost pairs of size 12, then solve the common-centre case."""
from collections import Counter
from itertools import product
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import subprocess
import sys

HERE = Path(__file__).resolve().parent
GROUP = HERE.parent / 'group'
if not GROUP.is_dir():
    GROUP = HERE.parents[1] / 'group'
sys.path.insert(0, str(GROUP))
from generate import bank, maps, profiles

POINTS = list(product(range(5), repeat=3))
LOW_MASK = (1 << 64) - 1

def members(row):
    while row:
        low = row & -row
        yield low.bit_length() - 1
        row ^= low

def moved(row, perm):
    return sum(1 << perm[i] for i in members(row))

def marginals(row):
    return [Counter(POINTS[i][j] for i in members(row)) for j in range(3)]

def centre(row):
    counts = marginals(row)
    assert all(sorted(count.values()) == [2,2,2,2,4] for count in counts)
    return POINTS.index(tuple(next(x for x,n in count.items() if n == 4) for count in counts))

def verify(folder):
    linear,trans,_ = maps()
    group = [bytes(t[i] for i in g) for g in linear for t in trans]
    rows = bank(folder,linear,trans,8728)
    keys = list(rows)
    for (size,cost),expected in [((9,557),[1,2,2,2,2]), ((10,744),[2]*5), ((12,1104),[2,2,2,2,4])]:
        for row in rows[size,cost]:
            assert all(sorted(m.values()) == expected for m in marginals(row))

    full = rows[12,1104]
    first = min(full)
    assert {moved(first,g) for g in group} == set(full)
    stabilizer = [g for g in group if moved(first,g) == first]
    partners = {m for m in full if not m & first}
    orbits = []
    pairs = []
    common = None
    while partners:
        second = min(partners)
        orbit = {moved(second,g) for g in stabilizer}
        orbit |= {moved(first,g) for g in group if moved(second,g) == first}
        assert orbit <= partners
        partners -= orbit
        same = centre(first) == centre(second)
        if same:
            assert common is None and len(orbit) == 1
            common = second
        orbits.append(len(orbit))
        pairs.append((first,second))
    assert sorted(orbits) == [1,12,12,16,24,48]
    pair = first | common
    ctr = centre(first)
    pair_stab = [g for g in group if moved(pair,g) == pair and moved(first,g) in (first,common)]
    assert len(pair_stab) == 96 and all(g[ctr] == ctr for g in pair_stab)

    # Every remaining profile must include exactly one row containing the uncovered centre.
    centre_reps = {}
    centre_counts = {}
    for key,items in rows.items():
        viable = {m for m in items if m >> ctr & 1 and not m & pair}
        centre_counts[key] = len(viable)
        reps = []
        while viable:
            rep = min(viable)
            orb = {moved(rep,g) for g in pair_stab}
            assert orb <= viable
            viable -= orb
            reps.append(rep)
        centre_reps[key] = reps
    assert {k:c for k,c in centre_counts.items() if c} == {(9,576):16,(11,936):24}

    jobs = []
    applicable = 0
    for total,counts in profiles(keys,8728):
        i = keys.index((12,1104))
        if counts[i] < 2:
            continue
        applicable += 1
        left = counts.copy()
        left[i] -= 2
        for j,key in enumerate(keys):
            if not left[j]:
                continue
            for rep in centre_reps[key]:
                residual = left.copy()
                residual[j] -= 1
                q = [(keys[k][1],n) for k,n in enumerate(residual) if n]
                fixed = [first,common,rep]
                jobs.append([total,len(fixed),len(q),*[x for m in fixed for x in (m&LOW_MASK,m>>64)],*[x for p in q for x in p]])
    assert len(jobs) == 5

    with (folder/'rows.txt').open('w') as stream:
        for (s,c),group_rows in rows.items():
            print(s,c,len(group_rows),file=stream)
            for row in group_rows:
                print(row&LOW_MASK,row>>64,0,file=stream)
    (folder/'jobs.txt').write_text(''.join(' '.join(map(str,j))+'\n' for j in jobs))
    exe = folder/'residual'
    subprocess.run(['c++','-std=c++17','-O3','-mpopcnt',str(HERE/'cover.cpp'),'-o',str(exe)],check=True)
    raw = subprocess.check_output([str(exe),str(folder/'rows.txt'),str(folder/'jobs.txt')],cwd=folder,text=True)
    transcript = [list(map(int,line.split())) for line in raw.splitlines()]
    assert len(transcript) == len(jobs) and all(ok==0 for _,_,_,_,_,ok in transcript)
    # The unrestricted lowest cost has one size/cost profile, verified upstream.
    costs = profiles(keys,8728)
    lowest = [(cost,dict((key,n) for key,n in zip(keys,counts) if n)) for cost,counts in costs if cost == 8709]
    assert lowest == [(8709,{(9,557):9,(10,744):2,(12,1104):2})]
    largest = rows[13,1296]
    first13 = min(largest)
    assert {moved(first13,g) for g in group} == set(largest)
    sym13 = [g for g in group if moved(first13,g) == first13]
    rem13 = {v for v in largest if not v & first13}
    pairs13 = []
    while rem13:
        v = min(rem13)
        equiv = {moved(v,g) for g in sym13} | {moved(first13,g) for g in group if moved(v,g) == first13}
        assert equiv <= rem13
        rem13 -= equiv
        pairs13.append((first13,v))
    assert len(pairs13) == 4

    with (folder/'minimum_bank').open('w') as stream:
        print(2,file=stream)
        for (size,price) in [(9,557),(10,744)]:
            items=rows[size,price]
            print(size,price,len(items),file=stream)
            for m in items:print(m&LOW_MASK,m>>64,file=stream)
    minimum=folder/'minimum'
    subprocess.run(['c++','-std=c++17','-O3','-mpopcnt',str(HERE/'minimum.cpp'),'-o',str(minimum)],check=True)
    audited=[]
    for source,extra in ((pairs,[]),(pairs13,['only-nines'])):
        (folder/'anchors').write_text(''.join(' '.join(str(v)for m in (x,y)for v in (m&LOW_MASK,m>>64))+'\n' for x,y in source))
        raw=subprocess.check_output([str(minimum),str(folder/'minimum_bank'),str(folder/'anchors'),*extra],text=True)
        residual=[list(map(int,line.split())) for line in raw.splitlines()]
        assert len(residual)==len(source) and all(ok == 0 for _,_,ok in residual)
        audited.append([n for _,n,_ in residual])
    return {'minimum_8709_nodes':audited[0],'two_thirteen_8719_nodes':audited[1],
            'pointed_pair_orbits':sorted(orbits),'pair_choices_with_first_fixed':sum(orbits),
            'common_centre_profiles':applicable,'common_centre_jobs':[(cost,number)for _,cost,_,_,number,_ in transcript],
            'common_centre_lower_bound':8729}

if __name__=='__main__':
    with TemporaryDirectory() as tmp:
        print(json.dumps(verify(Path(tmp)),sort_keys=True,indent=2))
