"""Cross-check a real single-column overlap against all positive native BRC paths."""
from argparse import ArgumentParser
from fractions import Fraction as F
from pathlib import Path
import json
import sys

from verify_templates import block_word


def experiment(native_root):
    sys.path.insert(0,str(native_root.resolve()))
    from enterprise_math import brc_histogram as brc
    tails=('557','575','755')
    rates=(F(1,4),F(1),F(4))
    points=(F(0),F(1,2),F(1))
    branches=0
    operations=0

    def mass(word,stock,u):
        nonlocal operations,branches
        seed=(F(7,8),u/8,(1-u)/8)
        rows=[brc.weight_histogram([v] if v else []) for v in seed]
        branch_count=sum(bool(v) for v in seed)*2**word.count('3')
        stock=list(stock)
        for symbol in word:
            ix='2357'.index(symbol)
            after=[brc.weight_histogram([]) for _ in rows]
            for i,hist in enumerate(rows):
                if hist.is_zero: continue
                rate=rates[i]
                prob=stock[ix]*(rate if symbol=='5' else 1)/(stock[0]+stock[1]+stock[2]*rate+stock[3])
                if symbol=='3':
                    targets=((0,F(7,8)),(i,F(1,8)))
                else:
                    targets=((min(2,i+1) if symbol=='2' else i,F(1)),)
                for dest,p in targets:
                    serial=brc.histogram_serial(hist,brc.weight_histogram([p*prob]))
                    after[dest]=brc.histogram_recoalesce(after[dest],serial)
                    operations+=1
            stock[ix]-=1
            rows=after
        assert not any(stock)
        assert branch_count==sum(v.count for v in rows)
        branches+=branch_count
        return sum(v.total_mass for v in rows)

    cut=[(F(0),F(0))]*3
    for j,tail in enumerate(tails):
        word='5'*11+tail
        cut[j]=tuple(mass(word,(0,0,13,1),u) for u in (F(0),F(1)))

    templates=((0,2,3,0,0),(1,1,0,3,0),(0,5,0,0,0))
    records=[]
    for template in templates:
        gaps=template+(0,)
        prefix=''.join('5'*n+'23' for n in gaps)
        rows=[[mass(prefix+'5'*11+tail,(6,6,18,1),u) for tail in tails] for u in points]
        assert all(2*x==y+z for x,y,z in zip(rows[1],rows[0],rows[2]))
        slopes=[x/y for x,y in zip(rows[2],rows[0])]
        a,b,g,d=block_word(6,18,gaps)
        for j,(low,high) in enumerate(cut):
            assert slopes[j]==(a*high+b*low)/(g*high+d*low)
        signature=tuple(sorted(slopes)[i] for i in (0,2))
        records.append(dict(gaps=template,column_557=str(slopes[0]),endpoints=list(map(str,signature))))
    assert len(set(tuple(row['endpoints']) for row in records))==len(templates)
    assert F(records[0]['column_557'])<F(records[1]['column_557'])<F(records[2]['column_557'])
    return dict(inventory=[6,6,18,1],common_following_gap=0,terminal_gap=11,records=records,
                full_word_probabilities=27,terminal_calibration_probabilities=6,
                positive_branch_count_with_multiplicity=branches,each_of_serial_and_recoalescence_calls=operations)

if __name__=='__main__':
    parser=ArgumentParser(description=__doc__)
    parser.add_argument('--native-root',type=Path,required=True)
    args=parser.parse_args()
    print(json.dumps(experiment(args.native_root),indent=2))
