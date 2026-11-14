#!/usr/bin/env python3
"""Exact EC49FOE 84-edge BRC forcing-core census.

Frozen ordered signed-prefix words -> rooted cover costs ->
direct lawful-root enumeration of all size-16/17/18 boundary subsets.
Integer exact arithmetic. Uses unchanged VERIFY_EC49FNY_INDEPENDENT.py.
Usage:
 python VERIFY_EC49FOE.py MASTER EDGES ORIGINAL24 --out cases.json
Optional --lo / --hi split the 51 sorted cases into batches.
"""
import argparse, hashlib, itertools, json
from pathlib import Path
import VERIFY_EC49FNY_INDEPENDENT as native

MASTER_SHA='cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e'
PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
ROOTS=(3,5,6,7)
BASE=(0,5,138,8192)
B=155
U=tuple(i for i in range(24) if not any(m>>i&1 for m in BASE))
assert len(U)==18

def load_master(path,case_ids):
    it=iter(path.read_text().split())
    assert tuple(int(next(it)) for _ in range(3))==(94,178850,38169)
    words=[]
    for _ in range(94):
        words.append([])
        for _ in range(int(next(it))):
            label=int(next(it)); code=next(it)
            words[-1].append((label,int(code[:2],16),tuple(bytes.fromhex(code[2:]))))
    rows={}
    for k in range(38169):
        keys=tuple(int(next(it)) for j in range(7))
        if k in case_ids: rows[k]=keys
    try:
        next(it)
        raise AssertionError("unexpected suffix")
    except StopIteration:
        pass
    assert len(rows)==len(case_ids)
    return words,rows

def census_case(case,words,keys):
    prof={r:native.table(words,keys,r) for r in ROOTS}
    options={label:tuple(j for j,r in enumerate(ROOTS) if label in prof[r][1])
             for label in range(24)}
    assert all(options[l] for l in U)
    for j,mask in enumerate(BASE):
        assert not any(mask & BASE[k] for k in range(j))
        assert all(j in options[l] for l in range(24) if mask>>l&1),case
    tab=[prof[r][2] for r in ROOTS]
    begin=[sum(1<<prof[r][1][l] for l in range(24) if BASE[j]>>l&1)
           for j,r in enumerate(ROOTS)]
    bits=[[1<<prof[r][1][l] if l in prof[r][1] else 0 for l in U]
          for r in ROOTS]
    calls=0; leaves=0
    def f(indices):
        nonlocal calls,leaves
        calls+=1
        masks=begin.copy(); multi=[]
        for i in indices:
            opts=options[U[i]]
            if len(opts)==1:masks[opts[0]]|=bits[opts[0]][i]
            else:multi.append(i)
        best=10**9
        def dfs(k):
            nonlocal best,leaves
            if k==len(multi):
                leaves+=1
                val=sum(tab[j][masks[j]] for j in range(4))
                if val<best:best=val
                return
            i=multi[k]
            for j in options[U[i]]:
                old=masks[j]; masks[j]|=bits[j][i]
                dfs(k+1); masks[j]=old
        dfs(0)
        assert best<10**9
        return best
    full=f(tuple(range(18)))
    deletion=[f(tuple(i for i in range(18) if i!=omit)) for omit in range(18)]
    h16=[f(t) for t in itertools.combinations(range(18),16)]
    assert calls==172
    assert max(h16)<=B,(case,max(h16))
    strict_del=[U[i] for i,x in enumerate(deletion) if x>B]
    cores=([list(U)] if full>B and not strict_del else
           [[l for l in U if l!=omit] for omit in strict_del] if full>B else [])
    return {'case':case,'full_cost':full,'H16':max(h16),
            'H17':max(deletion),'H18':full,
            'deletion_costs':dict(zip(map(str,U),deletion)),
            'minimal_cores':cores,
            'h_star':min(map(len,cores)) if cores else None,
            'strict_size16':sum(x>B for x in h16),
            'strict_size17':len(strict_del),
            'strict_size18':int(full>B),
            'boundary_checks':calls,'root_assignment_leaf_count':leaves}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('master',type=Path)
    ap.add_argument('edges',type=Path)
    ap.add_argument('original24',type=Path)
    ap.add_argument('--lo',type=int,default=0)
    ap.add_argument('--hi',type=int,default=51)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args()
    assert hashlib.sha256(a.master.read_bytes()).hexdigest()==MASTER_SHA
    edges=[tuple(map(int,l.split())) for l in a.edges.read_text().splitlines() if l.strip()]
    assert len(edges)==84 and len(set(edges))==84
    cases=sorted(set(itertools.chain.from_iterable(edges)))
    assert len(cases)==51
    original={}
    for line in a.original24.read_text().splitlines():
        z=line.split(); original[int(z[0])]=tuple(map(int,z[1:4]))
    assert all(original[x]==original[y] for x,y in edges)
    words,rows=load_master(a.master,set(cases))
    records=[]
    for i,c in enumerate(cases):
        if a.lo<=i<a.hi:
            rec=census_case(c,words,rows[c])
            rec['original_optimizer_triple']=original[c]
            records.append(rec)
            print('CASE',c,'full',rec['full_cost'],
                  'H16',rec['H16'],'h*',rec['h_star'],
                  'cores',len(rec['minimal_cores']),flush=True)
    result={'schema':'EC49FOE_CASE_BATCH_V1','pin':PIN,
            'source_master_sha256':MASTER_SHA,
            'edges_sha256':hashlib.sha256(a.edges.read_bytes()).hexdigest(),
            'original24_sha256':hashlib.sha256(a.original24.read_bytes()).hexdigest(),
            'case_count':len(records),'cases':records}
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print('BATCH_PASS',len(records),'checks',172*len(records),
          'leaves',sum(z['root_assignment_leaf_count'] for z in records),flush=True)

if __name__=='__main__':main()
