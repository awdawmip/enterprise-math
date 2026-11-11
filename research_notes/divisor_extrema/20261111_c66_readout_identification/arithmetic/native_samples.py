"""Original positive BRC histogram kernel against the modular census' selected paths."""
from argparse import ArgumentParser
from collections import Counter
from fractions import Fraction as Q
import json
from pathlib import Path
import sys
from single_readout import reduce_field, gap_rank, sample_words

RATES=(Q(1,4),Q(1),Q(4))


def run(brc,reference):
    totals=Counter()
    records=[]

    def push(state,stock,symbol):
        dest=[brc.weight_histogram([]) for _ in range(3)]
        pos='2357'.index(symbol)
        for i,hist in enumerate(state):
            if hist.is_zero:
                continue
            den=stock[0]+stock[1]+stock[2]*RATES[i]+stock[3]
            rate=RATES[i] if symbol=='5' else 1
            prob=stock[pos]*rate/den
            exits=((0,Q(7,8)),(i,Q(1,8))) if symbol=='3' else (
                (min(i+1,2) if symbol=='2' else i,Q(1)),)
            for target,feedback in exits:
                z=brc.histogram_serial(hist,brc.weight_histogram([prob*feedback]))
                dest[target]=brc.histogram_recoalesce(dest[target],z)
                totals['serial']+=1
                totals['recoalesce']+=1
        stock[pos]-=1
        return dest

    def full(k,gaps,s):
        stock=[k,k,k+1,1]
        state=[brc.weight_histogram([1] if i==s else []) for i in range(3)]
        word='23'.join('5'*m for m in gaps)
        for symbol in word:
            state=push(state,stock,symbol)
        assert stock == [0,0,2,1]
        assert sum(h.count for h in state)==2**k
        masses=[]
        for tail in ('557','575','755'):
            # Tail symbols preserve the state. Multiply each full histogram by
            # its accumulated native-rate likelihood only once per tail & state.
            amount=Q(0)
            branches=0
            for i,hist in enumerate(state):
                if hist.is_zero:
                    continue
                five,seven=2,1
                likelihood=Q(1)
                for symbol in tail:
                    total=five*RATES[i]+seven
                    likelihood*=(five*RATES[i] if symbol=='5' else seven)/total
                    five-=int(symbol=='5')
                    seven-=int(symbol=='7')
                result=brc.histogram_serial(hist,brc.weight_histogram([likelihood]))
                amount+=result.total_mass
                branches+=result.count
                totals['serial']+=1
            assert branches==2**k
            totals['native_complete_tail_probabilities']+=1
            totals['complete_paths_counted_with_multiplicity']+=branches
            masses.append(amount)
        assert sum(masses)==sum(h.total_mass for h in state)
        return masses

    for k in (7,16):
        for gaps in sample_words(k):
            a,b=[full(k,gaps,s) for s in range(2)]
            ratios=[v/w for v,w in zip(a,b)]
            h=max(ratios)/min(ratios)
            assert h==reference(k,gaps)
            records.append(dict(k=k,gaps=gaps,lex_index=gap_rank(gaps),H=str(h),H_mod_p=reduce_field(h)))
    return dict(kernel='enterprise_math/brc_histogram.py',native_families=[7,16],
                totals=dict(totals),samples=records)


if __name__=='__main__':
    parser=ArgumentParser(description=__doc__)
    parser.add_argument('--model',type=Path,required=True)
    parser.add_argument('--native-root',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    sys.path[:0]=[str(args.native_root.resolve()),str(args.model.resolve())]
    from enterprise_math import brc_histogram
    from observable_minimum import hilbert_ratio
    result=run(brc_histogram,hilbert_ratio)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
