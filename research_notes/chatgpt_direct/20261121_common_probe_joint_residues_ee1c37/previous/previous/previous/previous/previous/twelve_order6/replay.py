"""Optimize twelve labels in the presence of an affine element of order six or twelve."""
import argparse
from collections import Counter
from pathlib import Path
from tempfile import TemporaryDirectory
from itertools import product
import json
import subprocess
import sys

HERE=Path(__file__).resolve().parent

def subgroup(g):
    eye=bytes(range(125));elts={eye};power=g
    while power!=eye:
        elts.add(power);power=bytes(g[p]for p in power)
    return frozenset(elts)

def classes(linear,n):
    groups={subgroup(g)for g in linear if len(subgroup(g))==n}
    a=min(groups,key=lambda b:sorted(b))
    gen=min(g for g in a if subgroup(g)==a)
    equivalent=set()
    for l in linear:
        inv=bytes(l.index(i)for i in range(125))
        h=bytes(l[gen[p]]for p in inv)
        equivalent.add(subgroup(h))
    assert equivalent==groups
    return gen,len(equivalent)

def run(older,groupdir,original):
    sys.path[:0]=[str(older/'curve'),str(older/'bounds'),str(groupdir),str(original)]
    from generate import maps
    from prior_bounds import observation_file
    from cyclic11 import observations,class_cost
    from frontier9.native.replay_joint import run as native
    linear,translations,_=maps()
    ret={}
    with TemporaryDirectory() as tmp:
        w=Path(tmp)
        observation_file(w/'menus')
        exe=w/'orbits'
        subprocess.run(['c++','-O3','-std=c++17','-mpopcnt',str(HERE/'orbits.cpp'),'-o',str(exe)],check=True)
        for n,cap in [(12,31250),(6,10224)]:
            g,conj=classes(linear,n)
            (w/'g').write_text(str(n)+' '+' '.join(map(str,g))+'\n')
            proc=subprocess.run([str(exe),str(w/'menus'),str(w/'g'),'12',str(cap)],capture_output=True,text=True,check=True)
            lines=proc.stdout.splitlines()
            cost,small,comps,runcomps,large=map(int,lines[0].split())
            assert cost==(31251 if n==12 else 10224)
            summary={'conjugate_linear_subgroups':conj,'short_supports':[[int(y)for y in l.split()[1:]] for l in proc.stderr.splitlines()if l.startswith('bank ')],
                     'short_cover_nodes':small,'residual_supports':comps,'searched_residuals':runcomps,'forced_nodes':large}
            if n==12:
                assert len(lines)==1
                summary['exists']=False
                assert 'multiplicity 0' in proc.stderr
            else:
                rows=[list(map(int,l.split()))for l in lines[1:]]
                assert rows==json.loads((HERE/'groups.json').read_text())
                assert len(rows)==12 and sorted(p for r in rows for p in r)==list(range(125))
                table={frozenset(r)for r in rows}
                assert all(frozenset(g[p]for p in r)in table for r in rows)
                full_group={bytes(t[p] for p in a) for t in translations for a in linear}
                st=[h for h in full_group if all(frozenset(h[p]for p in r)in table for r in rows)]
                assert len(st)==6 and frozenset(st)==subgroup(g)
                assert 'multiplicity 4' in proc.stderr
                H=subgroup(g)
                normal=[]
                for h in full_group:
                    inverse=bytes(h.index(i) for i in range(125))
                    if bytes(h[g[i]] for i in inverse) in H:normal.append(h)
                fixed_tables={frozenset(frozenset(h[p] for p in r) for r in rows) for h in normal}
                assert len(normal)==24 and len(fixed_tables)==4
                summary.update(fixed_subgroup_optima=4,normalizer_order=len(normal),sample_stabilizer=len(st),
                               conjugate_affine_subgroups=len(full_group)//len(normal),distinct_optima=len(full_group)//len(st))
                from itertools import combinations
                bad,q=observations()
                assert not any((bad[a][b]>>c)&1 for r in rows for a,b,c in combinations(r,3))
                assert sum(class_cost(r,q)for r in rows)==10224
                code=[None]*125
                for j,r in enumerate(rows):
                    for p in r:code[p]=j
                receipt=json.loads(json.dumps(native(code,1)))
                assert receipt['joint']['by_queries']=={'0':21026,'1':10224}
                summary.update(minimum=cost,receipt=receipt,row_profile=sorted([s,c,v]for (s,c),v in Counter((len(r),class_cost(r,q))for r in rows).items()))
            ret[str(n)]=summary
    return ret

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--older',type=Path,required=True)
    p.add_argument('--group',type=Path,required=True);p.add_argument('--original',type=Path,required=True)
    a=p.parse_args();print(json.dumps(run(a.older.resolve(),a.group.resolve(),a.original.resolve()),sort_keys=True,indent=2))
