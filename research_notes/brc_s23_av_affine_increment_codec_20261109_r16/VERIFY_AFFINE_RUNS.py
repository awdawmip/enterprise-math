#!/usr/bin/env python3
"""Exact, output-sensitive affine-run codec for S23/AV risk block tables.

Input: r15 verified n_start,n_end,A,B constants for R_theta(m,n-m)=A+B*theta.
Output: n0,n1,A0,B0,dA,dB: R(n)=A0+B0*theta+(n-n0)*(dA+dB*theta),
for every integer n0 <= n <= n1. Adjacent runs share exactly one endpoint.

All decisions and checks are integer pairs or rational endpoint signs (not floats).
"""
import argparse, bisect, csv, hashlib, os, random
from collections import Counter
from fractions import Fraction as F
from time import perf_counter

LO = F(262204504569236716045286, 10**24)
HI = F(262204504569236716045287, 10**24)


def read_blocks(path):
    with open(path, newline='', encoding='utf-8') as f:
        rows = [tuple(map(int, (r['n_start'],r['n_end'],r['A'],r['B'])))
                for r in csv.DictReader(f, delimiter='\t')]
    assert rows and rows[0] == (128,128,0,0)
    for j, (s, e, a, b) in enumerate(rows):
        assert s <= e
        if j:
            ps, pe, pa, pb = rows[j-1]
            assert s == pe + 1
            assert all((a-pa)+(b-pb)*z > 0 for z in (LO,HI))
    return rows


def build_runs(blocks):
    # First form a run-length encoding of increments, not of risk values.
    events = []
    for i, (s, e, a, b) in enumerate(blocks):
        if i:
            old = blocks[i-1]
            events.append((s, s, (a-old[2], b-old[3])))
        if s < e:
            events.append((s+1, e, (0,0)))
    assert events and events[0][0] == blocks[0][1]+1
    increments = []
    for l, r, d in events:
        if increments and increments[-1][1]+1 == l and increments[-1][2] == d:
            p,_,_=increments[-1]
            increments[-1]=(p,r,d)
        else:
            assert not increments or increments[-1][1]+1 == l
            increments.append((l,r,d))
    assert increments[-1][1] == blocks[-1][1]
    starts = [r[0] for r in blocks]
    def original_value(n):
        j=bisect.bisect_right(starts,n)-1
        assert j>=0 and n <= blocks[j][1]
        return blocks[j][2:4]
    runs=[]
    for l,r,(da,db) in increments:
        a,b=original_value(l-1)
        runs.append((l-1,r,a,b,da,db))
        assert (a+da*(r-l+1),b+db*(r-l+1))==original_value(r)
    for i in range(1,len(runs)):
        assert runs[i-1][1]==runs[i][0]
        assert runs[i-1][4:]!=runs[i][4:] # maximal constant-difference runs
        prev,cur=runs[i-1],runs[i]
        assert (prev[2]+prev[4]*(prev[1]-prev[0]),prev[3]+prev[5]*(prev[1]-prev[0]))==cur[2:4]
    return runs, original_value


def validate(blocks, runs, original_value, probes):
    ends=[x[1] for x in runs]
    def restore(n):
        j=bisect.bisect_left(ends,n)
        assert j < len(runs)
        s,e,a,b,da,db=runs[j]
        assert s <= n <= e
        return a+(n-s)*da, b+(n-s)*db
    # Check all original piece boundaries, and every compressed boundary.
    keys={blocks[0][0], blocks[-1][1]}
    for s,e,_,_ in blocks:
        keys.update((s,e))
        if e>s:keys.update((s+1,e-1))
    for s,e,_,_,_,_ in runs:
        keys.update((s,e))
        if e>s:keys.add(s+1)
    rng=random.Random(0x20261109)
    for _ in range(probes):keys.add(rng.randint(blocks[0][0],blocks[-1][1]))
    for n in keys:
        assert restore(n)==original_value(n),(n,restore(n),original_value(n))
    return len(keys)


def write_runs(path, runs):
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w=csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['n0','n1','A0','B0','dA','dB']);w.writerows(runs)
    with open(path, 'rb') as f: data=f.read()
    return hashlib.sha256(data).hexdigest(),len(data)


def main():
    cli=argparse.ArgumentParser();cli.add_argument('blocks');cli.add_argument('output');cli.add_argument('--probes',type=int,default=10000)
    args=cli.parse_args(); t0=perf_counter()
    blocks=read_blocks(args.blocks)
    runs, original=build_runs(blocks)
    probes=validate(blocks,runs,original,args.probes)
    sha,bytes_out=write_runs(args.output,runs)
    with open(args.blocks,'rb') as f: input_bytes=f.read()
    cnt=Counter((r[4],r[5]) for r in runs)
    print('PASS_EXACT_AFFINE_INCREMENT_CODEC',os.path.basename(args.blocks))
    print('source_sha256',hashlib.sha256(input_bytes).hexdigest(),'source_bytes',len(input_bytes))
    print('n_range',blocks[0][0],blocks[-1][1],'constant_blocks',len(blocks),'affine_runs',len(runs))
    print('runs_zero',cnt[(0,0)],'runs_positive',len(runs)-cnt[(0,0)],'distinct_increments',len(cnt))
    print('exact_query_checks',probes,'last_affine',blocks[-1][2:4])
    print('output_sha256',sha,'output_bytes',bytes_out,'elapsed_sec',round(perf_counter()-t0,3))
    print('compression_rows',round(len(blocks)/len(runs),3),'compression_bytes',round(len(input_bytes)/bytes_out,3))
    if blocks[-1][1]==2000128:assert (len(blocks),len(runs),len(cnt))==(3426,102,13)
    if blocks[-1][1]==1000000000128:assert (len(blocks),len(runs),len(cnt))==(9698,298,23)

if __name__=='__main__':main()
