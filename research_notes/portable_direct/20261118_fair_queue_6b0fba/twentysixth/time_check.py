"""Neighbour-link logs of the V1R local INNER rule. No joint scheduler is an input."""
import argparse
from collections import Counter
import contextlib
from functools import lru_cache
from hashlib import sha256
import io
from itertools import permutations, product
import json
from pathlib import Path
import runpy
import sys

PIN = 'c0f816e2ab6be0145a3edd1a77488bddfd42a2f6'
FILES = {
    'frame': ('experiments/x6_cell_internal_state_v1_20260906/check_triadic_port_frame.py',
              '34058e33af5d8e325e3804bdbcf92f06918d48817b3ba5f8ded02e34c337a964'),
    'path': ('experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py',
             '6f0d79a519c53fed1300b3fabf500c34e30aa46cdd63b409fa6ecc115071ecb4'),
    'cwm': ('src/enterprise_math/brc_weighted.py',
            '4f3e356227a1c964d33a3ddae94922463ba28097a43b8d1b8f6cd9ca5615fc9f')}


def least_period(word):
    return next(d for d in range(1,len(word)+1)
                if all(x==word[(i+d)%len(word)] for i,x in enumerate(word)))


def check(repo):
    for fname, expected in FILES.values():
        assert sha256((repo/fname).read_bytes()).hexdigest()==expected
    path = runpy.run_path(str(repo/FILES['path'][0]))
    with contextlib.redirect_stdout(io.StringIO()):
        source = runpy.run_path(str(repo/FILES['frame'][0]))
    R,F = source['R'],source['F']
    sys.path.insert(0,str(repo/'src'))
    from enterprise_math import brc_weighted as brc
    assert Path(brc.__file__).resolve()==(repo/FILES['cwm'][0]).resolve()
    ledger_hash = sha256()
    @lru_cache(None)
    def mass(keys):
        combined=brc.CWM_ZERO
        for key in keys:
            # Each key is a distinct matching contact occurrence or macro-phase.
            matched=brc.cwm_propagate(brc.cwm_edge(1),brc.cwm_edge(1))
            combined=brc.cwm_recoalesce(combined,matched)
        assert combined.total==combined.count
        return int(combined.total)

    def direction(port):
        return tuple((1 if port>0 else -1) if i+1==abs(port) else 0 for i in range(6))
    @lru_cache(None)
    def unit_leg(port):
        dv=direction(port)
        return (path['shortest_event_count'](dv),path['shortest_path_multiplicity'](dv))
    def actual(frame):
        state=(frame,0)
        layers=[]
        for _ in range(12):
            current,mode=state
            after=F(state)
            relevant=current if mode==0 else after[0]
            arrow=-1 if mode==0 else 1       # pivot-relative I or O
            legs=tuple((token,port,arrow) for token,port in enumerate(relevant))
            assert len(set(abs(p) for _,p,_ in legs))==3
            for _,p,a in legs:
                assert unit_leg(a*p)==(1,1)
            layers.append(legs)
            state=after
        assert state==(frame,0)
        return tuple(layers)

    def read(layers,port):
        return tuple(next(((a,t) for t,p,a in layer if p==port),None) for layer in layers)

    samples, stats, absent = {},Counter(),0
    example={}
    signframes = {(1,2,-3):1,(-1,-2,3):-1}
    for frame in source['frames']:
        layers=actual(frame)
        for port in range(-6,7):
            if not port:
                continue
            log=read(layers,port)
            if abs(port) not in map(abs,frame):
                assert not any(log)
                absent+=1
                continue
            j=[abs(x) for x in frame].index(abs(port))
            delta=1 if port>0 else -1
            hits=tuple(int((-1)**k * (1 if frame[(j-k)%3]>0 else -1)==delta) for k in range(6))
            assert all(bool(log[2*k])==hits[k] and bool(log[(2*k-1)%12])==hits[k] for k in range(6))
            tokens=[log[2*k][1] for k in range(6) if hits[k]]
            assert sorted(tokens)==[0,1,2]
            assert all(log[(2*k-1)%12]==(1,log[2*k][1]) for k in range(6) if hits[k])
            anon=tuple(v[0] if v else 0 for v in log)
            period=least_period(anon)
            assert least_period(log)==12 and period==(4 if len({x>0 for x in frame})==1 else 12)
            stats[period]+=1
            samples.setdefault(log,hits)
            ledger_hash.update(repr((frame,port,log)).encode()+b'\n')
            if signframes.get(frame)==port:
                example[port]=log
    assert absent==5760 and stats=={4:1440,12:4320}

    # Only one representative per distinct anonymous 6-bit mask is needed for the overlap.
    by_mask={hits:log for log,hits in samples.items()}
    assert len(by_mask)==8
    match_hist=Counter()
    for a,log_a in by_mask.items():
        for b,log_b in by_mask.items():
            overlaps=[]
            for d in range(12):
                matched=tuple(t for t in range(12) if log_a[t] and log_b[(t+d)%12]
                              and log_a[t][0]==-log_b[(t+d)%12][0])
                h=d//2
                correlations=[mass(tuple(k for k in range(6) if a[k] and b[(k+u)%6])) for u in (h,h+1)]
                assert mass(matched)==(sum(correlations) if d%2 else 0)
                overlaps.append(mass(matched))
            has_alt=least_period(a)==2 or least_period(b)==2
            assert max(overlaps)==(3 if has_alt else 5)
            match_hist[max(overlaps)]+=1

    compressed={tuple(v for v in log if v) for log in samples}
    async_cases=0
    for a,b in product(sorted(compressed),repeat=2):
        for d in range(6):
            if not all(a[i][0]==-b[(i+d)%6][0] for i in range(6)):
                continue
            matches=[]
            for rename in permutations(range(3)):
                ix=tuple(i for i in range(6) if rename[a[i][1]]==b[(i+d)%6][1])
                matches.append(mass(ix))
            assert max(matches)==3
            async_cases+=1

    exa,exb=example[1],example[-1]
    at=tuple(i for i in range(12) if exa[i] and exb[(i+1)%12] and exa[i][0]==-exb[(i+1)%12][0])
    assert mass(at)==5
    assert exa[-1]==(1,0) and exa[0]==(-1,0) # a real two-layer outgoing/return witness
    return {'source_revision':PIN,'sha256':{k:h for k,(_,h) in FILES.items()},
            'raw_frames':len(source['frames']),'active_frame_directed_port_pairs_by_anonymous_period':dict(stats),
            'absent_frame_directed_port_pairs':absent,'distinct_token_logs':len(samples),'mask_pairs':64,
            'mask_pairs_by_optimal_equal_tick_arrow_matches':dict(match_hist),
            'distinct_compressed_token_logs_with_inherited_cut':len(compressed),
            'compressed_pairs_times_admissible_cyclic_offsets':async_cases,'fixed_permutation_trials_per_case':6,
            'source_ledger_digest_sha256':ledger_hash.hexdigest(),'example_until_wrap':{'A_local_log':exa,
            'B_local_log':exb,'offset_for_B':1,'matched_micro_ordinal_mod12':at}}


if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--repo',type=Path,required=True)
    print(json.dumps(check(p.parse_args().repo),indent=2))
