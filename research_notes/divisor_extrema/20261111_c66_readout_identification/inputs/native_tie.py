"""Native positive-mass BRC check of a rational accidental three-tail tie."""
from argparse import ArgumentParser
from fractions import Fraction as F
from pathlib import Path
import json
import sys


def experiment(native_root, certificate):
    sys.path.insert(0,str(native_root.resolve()))
    from enterprise_math import brc_histogram as brc
    witness=json.loads(certificate.read_text())['physical_readout_witness']
    t=F(witness['second_input_at_equal_H'])
    rates=(F(1,4),F(1),F(4))
    tails=('557','575','755')
    operations=0
    branches=0
    def mass(gaps,tail,u):
        nonlocal operations,branches
        word=''.join('5'*m+'23' for m in gaps[:-1])+'5'*gaps[-1]+tail
        stock=[3,3,4,1]
        seed=(F(7,8),u/8,(1-u)/8)
        rows=[brc.weight_histogram([v] if v else []) for v in seed]
        for symbol in word:
            ix='2357'.index(symbol)
            after=[brc.weight_histogram([]) for _ in rows]
            for i,hist in enumerate(rows):
                if hist.is_zero: continue
                rate=rates[i]
                probability=stock[ix]*(rate if symbol=='5' else 1)/(stock[0]+stock[1]+stock[2]*rate+stock[3])
                if symbol=='3': targets=[(0,F(7,8)),(i,F(1,8))]
                else: targets=[(min(2,i+1) if symbol=='2' else i,F(1))]
                for dest,p in targets:
                    stepped=brc.histogram_serial(hist,brc.weight_histogram([p*probability]))
                    after[dest]=brc.histogram_recoalesce(after[dest],stepped)
                    operations+=1
            stock[ix]-=1
            rows=after
        assert not any(stock)
        n=sum(v.count for v in rows)
        assert n==sum(bool(v) for v in seed)*8
        branches+=n
        return sum(v.total_mass for v in rows)
    points=[F(0),t/2,t,(1+t)/2,F(1)]
    summary=[]
    for gaps in witness['words']:
        masses=[[mass(gaps,tail,u) for tail in tails] for u in points]
        spreads=[]
        for row in masses[1:]:
            quotients=[a/b for a,b in zip(row,masses[0])]
            spreads.append(max(quotients)/min(quotients))
        summary.append(spreads)
    assert summary[0][1]==summary[1][1]==F(witness['common_H'])
    assert summary[0][0]<summary[1][0] and summary[0][2]>summary[1][2] and summary[0][3]>summary[1][3]
    return dict(common_H=str(summary[0][1]),second_input_at_equal_H=str(t),complete_tail_masses=30,
                each_of_serial_and_recoalescence_calls=operations,branches_with_multiplicity=branches,
                anchored_comparisons=['first<second','equal','first>second','first>second'])


if __name__=='__main__':
    p=ArgumentParser(description=__doc__)
    p.add_argument('--native-root',type=Path,required=True)
    p.add_argument('--certificate',type=Path,required=True)
    args=p.parse_args()
    print(json.dumps(experiment(args.native_root,args.certificate),indent=2))
