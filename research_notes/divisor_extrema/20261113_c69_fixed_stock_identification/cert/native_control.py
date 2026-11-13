"""Independent exact positive-mass verification of cross-label separation."""
from argparse import ArgumentParser
from fractions import Fraction
from pathlib import Path
from math import comb
import json
import sys

def compositions(total, parts):
    if parts==1:
        yield (total,)
        return
    for m in range(total+1):
        for later in compositions(total-m, parts-1):
            yield (m,)+later

def main(native):
    sys.path.insert(0, str(native.resolve()))
    from mixed_kernel import responses
    controls = []
    most_bits = 0
    most_tails = 0
    for r in range(1,5):
        for c in range(2,11):
            observed = {}
            count = 0
            for word in compositions(c-2, r+1):
                rows,_ = responses(r,c,word)
                seen = set()
                for label in (3,4,5):
                    z = (7*rows[0][label]+rows[1][label])/(7*rows[0][label]+rows[2][label])
                    assert observed.setdefault(z, word)==word
                    seen.add(z)
                    most_bits=max(most_bits, z.denominator.bit_length())
                most_tails += len(seen)
                count += 1
            assert count == comb(r+c-2,r)
            controls.append([r,c,count,len(observed)])
    return dict(stocks=len(controls),words=sum(x[2] for x in controls),exact_tail_columns=3*sum(x[2] for x in controls),
                distinct_columns_within_stocks=most_tails,max_denominator_bits=most_bits,rows=controls)

if __name__=='__main__':
    p=ArgumentParser(description=__doc__)
    p.add_argument('--prior',type=Path,required=True,help='C67/joint directory containing mixed_kernel.py')
    print(json.dumps(main(p.parse_args().prior),indent=2))
