#!/usr/bin/env python3
"""EC49FMG: exact vector, lawful word/prefix witnesses, optional independent DP.
--independent: recompute seven audited indices with independent Python trie DP.
--run-all: recompute every one of the 200 fixed-key minima using original C++ engine.
"""
import collections
import hashlib
import itertools
import json
import subprocess
import sys
import tempfile
from pathlib import Path

P = Path(__file__).resolve().parent
ROOT = P.parent
sys.path.insert(0, str(ROOT / 'EC49FJD_RELEASE_B11_COMPLETE_20261111'))
from EC49FGW_RADIUS5_SCREEN import PIN, all_words, pref, raw_key

E = json.loads((P / 'EXACT_VECTOR_EC49FMG.json').read_text())
assert E['scientific_pin'] == PIN == 'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
assert E['global_slice'] == [1420, 1620]
C = E['exact_prefix_costs']
assert len(C) == 200 and all(type(v) is int and v > 0 for v in C)
assert hashlib.sha256(bytes(C)).hexdigest() == E['local_execution_provenance']['raw_cost_byte_vector_sha256']
assert dict(collections.Counter(str(v) for v in C)) == {str(k):v for k,v in E['histogram'].items()}
assert min(C) == 98 and [i + 1420 for i,v in enumerate(C) if v == 98] == [1468, 1542, 1615]
labels = sorted(tuple(map(int, x.split(':'))) for x in E['required_observation_labels'])
cat = list(all_words())
assert len(cat) == 178850 and sorted({lab for lab,_ in cat}) == labels
labid = {x:i for i,x in enumerate(labels)}
bykey = collections.defaultdict(list)
support = collections.defaultdict(int)
lookup = set(cat)
for lab,w in cat:
    k = raw_key(w)
    support[k] |= 1 << labid[lab]
    bykey[k].append((labid[lab], pref(w)[-1].hex()))
assert len(support) == 94
base = {(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}
outside = sorted(set(support) - base)
cases = []
for dropped in itertools.combinations(sorted(base),2):
    for added in itertools.combinations(outside,2):
        ks = sorted((base - set(dropped)) | set(added))
        mask = 0
        for k in ks: mask |= support[k]
        if mask == (1<<24)-1: cases.append(ks)
assert len(cases) == 6315
for cert in E['explicit_word_witnesses']:
    i = cert['index']
    ks = set(map(tuple, cert['keys']))
    assert sorted(ks) == cases[i] and C[i-1420] == cert['cost']
    words = cert['words']
    assert len(words) == len(labels) == 24
    prefixes = set()
    for lab,w in zip(labels, words):
        assert (lab,w) in lookup and raw_key(w) in ks
        prefixes.update(pref(w))
    assert len(prefixes) == cert['cost']
    print('EC49FMG_EXPLICIT_SIGNED_X6_WITNESS_PASS',i,len(prefixes),flush=True)
print('EC49FMG_FROZEN_CATALOG_AND_200_COST_VECTOR_PASS',len(cat),len(cases),len(C),flush=True)

def independent_optimum(keyset):
    """Independent integer root trie and demand-subset DP (no C++ output input)."""
    roots = collections.defaultdict(list)
    for lab,w in cat:
        if raw_key(w) in keyset:
            roots[pref(w)[0]].append((lab,w))
    rcost,options = {},collections.defaultdict(list)
    for rt,rows in roots.items():
        local = sorted({lab for lab,_ in rows})
        li = {lab:j for j,lab in enumerate(local)}
        children,terminal = [{}],[0]
        for lab,w in rows:
            u = 0
            for p in pref(w):
                v = children[u].get(p)
                if v is None:
                    v = len(children)
                    children[u][p] = v
                    children.append({})
                    terminal.append(0)
                u = v
            terminal[u] |= 1<<li[lab]
        def solve(u):
            d={0:0}
            if terminal[u]: d[terminal[u]]=0
            for v in children[u].values():
                q=solve(v)
                nd={}
                for a,x in d.items():
                    for b,y in q.items():
                        m=a|b
                        nd[m]=min(nd.get(m,10**9),x+y)
                d=nd
            return {m:c+int(u!=0 and m!=0) for m,c in d.items()}
        d=solve(0)
        f=[10**9]*(1<<len(local))
        for m,c in d.items(): f[m]=c
        for j in range(len(local)):
            for m in range(len(f)):
                if not m>>j&1: f[m]=min(f[m],f[m|(1<<j)])
        rcost[rt]=f
        for lab,j in li.items(): options[lab].append((rt,j))
    assert len(options)==24
    acc={rt:0 for rt in roots}
    order=sorted(options,key=lambda lab:len(options[lab]))
    best=10**9
    def rec(j):
        nonlocal best
        if j==24:
            best=min(best,sum(rcost[rt][mask] for rt,mask in acc.items()))
            return
        for rt,b in options[order[j]]:
            acc[rt] |= 1<<b
            rec(j+1)
            acc[rt] &= ~(1<<b)
    rec(0)
    return best

if '--independent' in sys.argv:
    for i in (1420,1452,1460,1468,1542,1615,1619):
        ans=independent_optimum(set(cases[i]))
        assert ans==C[i-1420],(i,ans,C[i-1420])
        print('EC49FMG_INDEPENDENT_PYTHON_EXACT_PASS',i,ans,flush=True)

if '--run-all' in sys.argv:
    cpp=ROOT/'EC49FKY_ONE_KEY_SWAP_84_LOCAL_OPTIMUM_20261112'/'SCAN_7KEY_GENERAL.cpp'
    with tempfile.TemporaryDirectory() as d:
        d=Path(d)
        with (d/'input.txt').open('w') as out:
            out.write('200\n')
            for ks in cases[1420:1620]:
                rows=[a for k in ks for a in bykey[k]]
                out.write(str(len(rows))+'\n')
                for lab,path in rows: out.write(f'{lab} {path}\n')
        subprocess.run(['g++','-std=c++17','-O3',str(cpp),'-o',str(d/'scan')],check=True)
        with (d/'input.txt').open('rb') as inp,(d/'output.txt').open('wb') as out:
            subprocess.run([str(d/'scan')],stdin=inp,stdout=out,check=True)
        lines=(d/'output.txt').read_text().splitlines()
        assert len(lines)==200
        assert [int(x.split()[0]) for x in lines]==list(range(200))
        assert [int(x.split()[1]) for x in lines]==C
        print('EC49FMG_ALL_200_EXACT_CPP_REPLAY_PASS',flush=True)
