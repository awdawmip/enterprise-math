"""Compare original BRC positive histograms with the compact C64 TV/H model.

Examples start immediately after the two C62 preparing histories, with pure
memory state 0 or 1. Complete likelihood ratios H remove those histories' own
frequencies. Each later 3 branches with weights 7/8 and 1/8 in every example.
"""
import argparse
from collections import Counter
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys

from suffix_limits import block,evaluate,total_variation
from observable_minimum import T,hilbert_ratio


def run(canonical_dir):
    sys.path.insert(0,str(canonical_dir.resolve()))
    from enterprise_math import brc_histogram as brc
    expected_hashes = {
        "brc_histogram.py":"9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1",
        "brc_rational_holonomy.py":"2591640fe348da9cd7f293a957bea9ae92c82943",
        "brc_weighted_recurrent.py":"4e6b3132580e3cd70a20a0d8bd4d28792b961afb",
    }
    for name,pinned in expected_hashes.items():
        raw=(canonical_dir/'enterprise_math'/name).read_bytes()
        assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==pinned
    counts=Counter()
    rates=(Q(1,4),Q(1),Q(4))
    def step(hists,stock,symbol):
        dest=[brc.weight_histogram([]) for _ in range(3)]
        assert stock[symbol]>0
        for s,hist in enumerate(hists):
            if hist.is_zero:
                continue
            denom=stock['2']+stock['3']+rates[s]*stock['5']+stock['7']
            prob=stock[symbol]*(rates[s] if symbol=='5' else 1)/denom
            if symbol=='3':
                updates=((0,Q(7,8)),(s,Q(1,8)))
            else:
                updates=((min(2,s+1) if symbol=='2' else s,Q(1)),)
            for target,w in updates:
                term=brc.histogram_serial(hist,brc.weight_histogram([prob*w]))
                dest[target]=brc.histogram_recoalesce(dest[target],term)
                counts['histogram_serial']+=1
                counts['histogram_recoalesce']+=1
        stock[symbol]-=1
        return dest

    def branch(k,gaps,s0):
        stock={'2':k,'3':k,'5':k+1,'7':1}
        hists=[brc.weight_histogram([1] if i==s0 else []) for i in range(3)]
        word='23'.join('5'*m for m in gaps)
        for sym in word:
            hists=step(hists,stock,sym)
        assert stock=={'2':0,'3':0,'5':2,'7':1}
        total=sum(h.total_mass for h in hists)
        pi=[h.total_mass/total for h in hists]
        assert sum(h.count for h in hists)==2**k
        # Compact path filter is independent of histogram serial/recoalescence.
        c=k+1-gaps[0]; u=Q(1-s0)
        for r,m in zip(range(k-1,0,-1),gaps[1:-1]):
            u=evaluate(block(r,c,m),u)
            c-=m
        weights=[Q(7),u,1-u]
        for s,rate in enumerate(rates):
            for n in range(c,2,-1):
                weights[s]*=n*rate/(1+n*rate)
        assert pi==[w/sum(weights) for w in weights]
        counts['compact_state_coordinates_checked']+=3
        tail_masses=[]
        for j,tail in enumerate(('557','575','755')):
            tail_hists=hists
            remaining=dict(stock)
            for sym in tail:
                tail_hists=step(tail_hists,remaining,sym)
            combined=brc.weight_histogram([])
            for h in tail_hists:
                combined=brc.histogram_recoalesce(combined,h)
                counts['histogram_recoalesce']+=1
            assert combined.count==2**k
            assert combined.total_mass==total*sum(p*T[i][j] for i,p in enumerate(pi))
            counts['complete_tail_branches_with_multiplicity']+=combined.count
            counts['complete_tails_checked']+=1
            tail_masses.append(combined.total_mass)
        assert sum(tail_masses)==total
        return pi,tail_masses

    cases=[(2,'A',(1,0,0)),(3,'exceptional_second',(0,0,2,0))]
    for k,letters in ((4,"ABCDE"),(9,"DE"),(10,"DE")):
        named=dict(A=(1,)*(k-1)+(0,0),B=(1,)*(k-2)+(0,1,0),C=(1,)*(k-2)+(0,0,1),
                   D=(1,)*(k-3)+(0,0,2,0),E=(2,0)+(1,)*(k-3)+(0,0))
        cases.extend((k,name,named[name]) for name in letters)
    for k,name,gaps in cases:
        (p,a),(q,b)=[branch(k,gaps,s) for s in (0,1)]
        delta=sum(abs(x-y) for x,y in zip(p,q))/2
        ratios=[x/y for x,y in zip(a,b)]
        spread=max(ratios)/min(ratios)
        assert delta==total_variation(k,gaps) and spread==hilbert_ratio(k,gaps)
        counts['schedule_TV_and_H_matches']+=1
    return dict(status="PASS",source="awdawmip/enterprise-math@de41b8cd9e6b0ea52345d5f669af924f9379318a",
        kernel_blobs=expected_hashes,cases=[dict(k=k,name=n,gaps=p) for k,n,p in cases],counts=dict(counts))


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inherited",type=Path,default=Path(__file__).resolve().parents[1]/"inherited")
    args=parser.parse_args()
    print(json.dumps(run(args.inherited),indent=2))
