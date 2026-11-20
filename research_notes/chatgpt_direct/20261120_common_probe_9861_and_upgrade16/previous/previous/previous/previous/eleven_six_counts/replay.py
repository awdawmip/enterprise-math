"""Count and classify the eleven-label optima with a cyclic symmetry of order six."""
import argparse
from collections import Counter
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory

HERE = Path(__file__).resolve().parent

def verify(previous):
    older = previous/'previous'
    sys.path[:0] = [str(previous/'group'), str(older/'curve'), str(older/'bounds')]
    from generate import maps
    from prior_bounds import observation_file
    from cyclic11 import observations, class_cost
    from itertools import combinations
    linear, translations, _ = maps()
    identity = bytes(range(125))
    def compose(a,b):
        return bytes(a[x] for x in b)
    def cyclic(g):
        powers = {identity}
        u = g
        while u not in powers:
            powers.add(u)
            u = compose(g,u)
        return frozenset(powers)
    subgroups = {cyclic(g) for g in linear if len(cyclic(g)) == 6}
    h = min(subgroups, key=sorted)
    generator = min(g for g in h if cyclic(g) == h)
    with TemporaryDirectory() as folder:
        w = Path(folder)
        observation_file(w/'obs')
        (w/'g').write_text('6 '+' '.join(map(str,generator))+'\n')
        subprocess.run(['c++','-O3','-std=c++17','-mpopcnt', str(HERE.parent/'twelve_order6/orbits.cpp'),'-o',w/'orbits'],check=True)
        proc = subprocess.run([w/'orbits', w/'obs', w/'g','11','11292'], capture_output=True, text=True, check=True)
    first = list(map(int,proc.stdout.splitlines()[0].split()))
    assert first[0] == 11292
    multiplicity = int(next(line for line in proc.stderr.splitlines() if line.startswith('multiplicity ')).split()[1])
    def table(rows):return frozenset(frozenset(row) for row in rows)
    def act(g,partition):return frozenset(frozenset(g[p] for p in row) for row in partition)
    samples = [table(rows) for rows in json.loads((HERE/'groups.json').read_text())]
    group = {compose(t,a) for t in translations for a in linear}
    inverse = lambda g:bytes(g.index(i) for i in range(125))
    normalizer = [g for g in group if compose(g,compose(generator,inverse(g))) in h]
    bad, masks = observations()
    full_orbits = []
    per_h = set()
    stabilizers = []
    for sample in samples:
        assert len(sample) == 11 and sorted(p for r in sample for p in r) == list(range(125))
        assert not any(bad[a][b]>>c&1 for r in sample for a,b,c in combinations(sorted(r),3))
        assert sum(class_cost(sorted(r),masks) for r in sample) == 11292
        stabilizer = {g for g in group if act(g,sample) == sample}
        assert stabilizer == h
        stabilizers.append(len(stabilizer))
        own = {act(g,sample) for g in normalizer}
        assert own.isdisjoint(per_h)
        per_h |= own
        full_orbits.append(len(group)//len(stabilizer))
    assert len(per_h) == multiplicity
    old = list(map(int,(older/'native/eleven.txt').read_text().split()))
    known = table([[p for p in range(125) if old[p]==j] for j in range(11)])
    which = [i for i,s in enumerate(samples) if any(act(g,s)==known for g in group)]
    assert len(which) == 1
    return {'minimum':11292,'fixed_subgroup_optima':multiplicity,'stabilizers':stabilizers,
            'classes_under_full_group':full_orbits,'total':sum(full_orbits),
            'known_witness_orbit':which[0],'normalizer_order':len(normalizer),'search_signature':first}

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--previous',type=Path,required=True)
    print(json.dumps(verify(p.parse_args().previous.resolve()),sort_keys=True,indent=2))
