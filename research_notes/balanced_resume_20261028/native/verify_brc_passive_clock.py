#!/usr/bin/env python3
"""Execute only the new positive clock observer; reuse the exact source pulse."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
import argparse
import hashlib
import json
from u2_incidence_prefix import load_kernel

def main(repo_root):
    R=load_kernel(repo_root)
    half=R.edge(Q(1,2))
    row=[R.brc.CWM_ZERO]*12;row[0]=R.brc.CWM_ONE
    observations=[]
    twelve=None
    for t in range(49):
        expected=[sum(Q(comb(t,j),2**t) for j in range(t+1) if j%12==r) for r in range(12)]
        assert [x.total for x in row]==expected
        total=R.total(row)
        assert (total.count,total.total,total.dominant)==(2**t,Q(1),Q(1,2**t))
        phase=row[11].total/4
        observations.append(str(phase))
        if t==12:twelve=expected
        row=[R.merge(R.serial(row[r],half),R.serial(row[(r-1)%12],half)) for r in range(12)]
    assert min(twelve)==Q(1,2048)
    assert Q(observations[11])==Q(1,8192)
    assert Q(observations[22])==Q(88179,2097152)
    for t in range(49):
        hit=sum(Q(comb(j-1,10),2**j) for j in range(11,t+1))
        binomial_tail=sum(Q(comb(t,j),2**t) for j in range(11,t+1))
        assert hit==binomial_tail
    alpha=Q(3,512)
    remainder=[(p-alpha/12)/(1-alpha) for p in twelve]
    assert min(remainder)>=0 and sum(remainder)==1
    for t,value in enumerate(observations):
        assert abs(Q(value)-Q(1,48))<=Q(1,4)*Q(509,512)**(t//12)
    report={'status':'EXACT_POSITIVE_CLOCK_OBSERVER_PASS','horizon':48,
            'source_world_reexecuted':False,'source_pulse_blob':'bd80290c259cc60995069613a5f4b5f5b41a13d1',
            'BRC_source_blob':R.BLOB,'BRC_calls':dict(R.CALLS),'phase_at_11':observations[11],
            'phase_at_22':observations[22],'twelve_step_min_entry':str(min(twelve)),
            'minorization_alpha':str(alpha),'clock_mean_wait':2,'mean_first_detection':22,
            'native_clock_selection':'UNKNOWN','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_name('brc_passive_clock_validation.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--repo-root',required=True)
    main(p.parse_args().repo_root)
