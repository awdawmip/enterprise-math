"""Check the R10 row and the single occupied-port rule. Standard library only."""
import argparse
from collections import Counter
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations_with_replacement, product
import json
from math import gcd
from pathlib import Path
import sys

PRIOR_SHA = '094b8394e203f63c3f451c43a63782fd3657537e09723988b573ce02c743ecd4'
R10_SHA = '02c7f1bb20e567a6f652adaf600f9ac434894c79680375f78f727c56e5651af3'
ARCHIVE_SHA = 'c1b1d2d3c9ce952e922263b04537d849419832e6d6acde0060eb45e6de684335'
NAMES = (('A0','B0'), ('A1','B1','B2'), ('A2','A3','B3','B4'))


def load_source(path, name):
    spec = spec_from_file_location(name,path)
    mod = module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def ceiling(a,b):
    return -((-a)//b)


def groups(counter):
    return [[*key,n] for key,n in sorted(counter.items()) if n]


def site_trace(capacity, source=None, stop=12):
    waiting = [list(row) for row in NAMES]
    pending, walls = [], []
    phase = 0
    rows, named_rows, release, blocked = [], [], [], []
    for time in range(3,stop+1):
        if time>3:
            phase = (phase+1)%3
            walls += [ticket for ticket in pending if ticket[0]==time]
            pending = [ticket for ticket in pending if ticket[0]>time]
            occupied = sum(ticket[1]==2 for ticket in pending)
            stock = min(map(len,waiting))
            avail = stock if capacity is None else min(stock,capacity-occupied)
            if phase==1 and stock>0 and avail==0:
                blocked.append(time)
            do = int(phase==1 and avail>0)
            if source:
                original,arith = source
                for fn in (original.burst_unit,original.burst_orbit):
                    assert fn(arith,avail,phase,(1,),(1,2,0)) == (do,2 if do else phase,(0,do,0))
            if do:
                release.append(time)
                for port,delay in enumerate((1,2,3)):
                    role = (port+phase)%3
                    name = waiting[role].pop(0)
                    pending.append((time+delay,port,role,name))
                phase = 2
        assert capacity is None or sum(s[1]==2 for s in pending)<=capacity
        total = [name for row in waiting for name in row]+[s[3] for s in pending+walls]
        assert sorted(total)==sorted(name for row in NAMES for name in row)
        rows.append(dict(time=time,q=list(map(len,waiting)),phase=phase,
                         pending=groups(Counter((port,role,t-time) for t,port,role,_ in pending)),
                         wall=groups(Counter((port,role) for _,port,role,_ in walls))))
        named_rows.append(dict(time=time,waiting=[s.copy() for s in waiting],
                               pending=sorted(pending),walls=sorted(walls)))
    return dict(releases=release,blocked=blocked,numeric=rows,named=named_rows)


def dense_schedule(n,h,C,delay,tau,ready,free):
    # Actual chronological gate, completion and indivisible commitment.
    phase = (-tau)%n
    expiry = [t for t in free if t>0]
    emitted = []
    t = 0
    while len(emitted)<len(ready):
        expiry = [v for v in expiry if v>t]
        if phase==0 and t>=ready[len(emitted)] and len(expiry)<C:
            emitted.append(t)
            expiry.append(t+delay)
            phase = (-h)%n
        phase = (phase+1)%n
        t += 1
        assert t<=tau+max(ready,default=0)+(delay+2*n)*(len(ready)+1)+2
    return emitted


def initial_profile(n,h,tau,free):
    running = 0
    keys = []
    for i,when in enumerate(sorted(free)):
        running = max(running,ceiling(when-tau-i*h,n))
        keys.append(running)
    return keys


def formula(n,h,C,delay,tau,ready,free):
    pulse = initial_profile(n,h,tau,free)
    extra = max(0,ceiling(delay-C*h,n))
    lower = []
    result = []
    for i,when in enumerate(ready):
        t0 = tau+i*h
        lower.append(max(0,ceiling(when-t0,n),pulse[i] if i<C else 0))
        offset = max(v+extra*((i-j)//C) for j,v in enumerate(lower))
        result.append(t0+n*offset)
    return result


def tests():
    backlog = 0
    for n in range(2,8):
        for h,C,delay,tau in product(range(1,n),range(1,6),range(1,14),range(n)):
            ready = [0]*13
            got = dense_schedule(n,h,C,delay,tau,ready,[0]*C)
            b = max(0,ceiling(delay-C*h,n))
            assert got == [tau+i*h+n*(i//C)*b for i in range(13)]
            backlog+=1
    histories = 0
    for n,h,C,delay,tau in [(3,2,1,3,1),(3,2,2,3,1),(4,1,2,6,2),(5,3,3,8,1)]:
        # All sorted release-readiness inputs of length four in this range.
        requests=list(combinations_with_replacement(range(7),4))
        signatures={}
        for free in combinations_with_replacement(range(delay+1),C):
            key=tuple(initial_profile(n,h,tau,free))
            first=dense_schedule(n,h,C,delay,tau,[0]*C,free)
            assert tuple((v-tau-i*h)//n for i,v in enumerate(first))==key
            output=[]
            for ready in requests:
                got=dense_schedule(n,h,C,delay,tau,ready,free)
                assert got==formula(n,h,C,delay,tau,ready,free)
                output.append(tuple(got))
                histories+=1
            assert signatures.setdefault(key,output)==output
    residue_grids = 0
    for n,h,C,delay in [(3,2,1,3),(3,2,2,3),(4,1,3,8),(5,2,4,13),(7,4,2,5)]:
        b=max(0,ceiling(delay-C*h,n))
        period=C*h+n*b
        for tau,M in product(range(n),range(1,31)):
            g=gcd(period,M)
            size=C*(M//g)
            times=dense_schedule(n,h,C,delay,tau,[0]*size,[0]*C)
            seen=Counter(s%M for s in times)
            for v in range(M):
                assert seen[v]==sum((tau+r*h-v)%g==0 for r in range(C))
            assert len(seen)==(M//g)*min(C,g//gcd(g,h))
            assert (len(set(seen.values()))==1 and len(seen)==M)==(gcd(h,g)==1 and C%g==0)
            residue_grids+=1
    assert dense_schedule(3,2,1,5,1,[0],[1])==[1]
    assert dense_schedule(3,2,1,5,1,[0],[4])==[4]
    return dict(backlog_parameter_sets=backlog,interval_and_queue_inputs=histories,
                exact_residue_frequency_grids=residue_grids)


def verification(prior,archive,r10):
    previous = prior/'feedback_checked.json'
    assert sha256(previous.read_bytes()).hexdigest()==PRIOR_SHA
    earlier=json.loads(previous.read_text())
    source=None
    if r10:
        assert sha256(r10.read_bytes()).hexdigest()==R10_SHA
        orig=load_source(r10,'p09_original_feedback')
        ar=orig.P.Arithmetic()
        ar.stage='p09_single_material'
        source=orig,ar
    base=site_trace(None,source)
    limited=site_trace(1,source)
    assert base['numeric'][:7]==earlier['original_local_rows']
    if archive:
        assert sha256(archive.read_bytes()).hexdigest()==ARCHIVE_SHA
        prev=load_source(prior/'feedback_check.py','p09_prior_check')
        prev.compare_archive(archive,base['numeric'][:7])
    assert base['releases']==[4,6] and limited['releases']==[4,9]
    assert limited['blocked']==[6]
    assert base['numeric'][:3]==limited['numeric'][:3]
    assert base['numeric'][3]!=limited['numeric'][3]
    assert site_trace(2,source)==base
    limited6,limited9=limited['numeric'][3],limited['numeric'][6]
    assert (limited6['q'],limited6['phase'],limited9['q'],limited9['phase'])==([1,2,3],1,[0,1,2],2)
    assert base['numeric'][6]['wall']==limited['numeric'][9]['wall']
    assert base['numeric'][-1]==limited['numeric'][-1]
    # Empty versus occupied residual with same free gate and equal stock.
    assert dense_schedule(3,2,1,3,0,[0],[0])==[0]
    assert dense_schedule(3,2,1,3,0,[0],[1])==[3]
    return dict(source=dict(public_prior_sha256=PRIOR_SHA,original_archive_sha256=ARCHIVE_SHA,
                            original_feedback_py_sha256=R10_SHA,material='111',row=735,
                            snapshot_member_sha256=earlier['archived_snapshot_member_sha256'],
                            events_member_sha256=earlier['archived_event_member_sha256'],
                            original_heldout_rows_compared=[3,4,5,6,7,8,9]),
                original_baseline=base['numeric'],capacity_one=limited,
                two_berths_match_original_through=12,
                formula_and_initial_state_tests=tests())


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--prior',type=Path,default=Path(__file__).resolve().parents[1]/'sixtyfifth')
    parser.add_argument('--archive',type=Path)
    parser.add_argument('--r10',type=Path)
    arguments=parser.parse_args()
    print(json.dumps(verification(arguments.prior,arguments.archive,arguments.r10),indent=2,sort_keys=True))
