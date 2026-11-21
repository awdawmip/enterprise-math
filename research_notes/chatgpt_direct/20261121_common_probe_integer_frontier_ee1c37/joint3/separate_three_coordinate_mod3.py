"""Exhaust all three-coordinate additive modulus-three cuts exactly."""
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import lcm
from pathlib import Path
import argparse
import json
import subprocess
import time

TYPES = ((9,557),(10,744),(11,936),(11,944))
COUNTS = (2,5,2,1)
POINTS = list(product(range(5), repeat=3))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--witness', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    started = time.monotonic()
    source = Path(__file__).with_suffix('.cpp')
    # The engine is shared with the shorter named C++ file.
    source = source.with_name('three_coordinate_mod3.cpp')
    binary = a.output.parent/'three_coordinate_mod3'
    subprocess.run(['c++','-O3','-std=c++20',str(source),'-o',str(binary)],check=True)
    data = a.witness.read_bytes(); doc = json.loads(data)
    free = int(doc['free_mask']); rows = doc['weights']
    weights = [Fraction(r['numerator'],r['denominator']) for r in rows]
    den = lcm(*(w.denominator for w in weights))
    assert den.bit_length()<230
    fibers = [sum(1<<p for p,x in enumerate(POINTS) if x[axis]==value)
              for axis in range(3) for value in range(5)]
    limbs = lambda x: ' '.join(str((x>>(64*i))&((1<<64)-1)) for i in range(4))
    lines = [f'{len(rows)} {limbs(den)}', ' '.join(str((free&h).bit_count()) for h in fibers)]
    for row,w in zip(rows,weights):
        mask=int(row['mask']);typ=TYPES.index((row['size'],row['cost']))
        lines.append(f'{typ} {limbs(w.numerator*(den//w.denominator))} '+' '.join(str((mask&h).bit_count()) for h in fibers))
    run = subprocess.run([str(binary)],input='\n'.join(lines)+'\n',text=True,capture_output=True,check=True)
    result=json.loads(run.stdout)
    lam=result['fiber_coefficients']; aa=result['type_coefficients'];q=3
    coeff=[sum(lam[axis][point[axis]] for axis in range(3))%q for point in POINTS]
    rhs=(sum(coeff[p] for p in range(125) if free>>p&1)+sum(x*y for x,y in zip(aa,COUNTS)))%q
    assert rhs==result['rhs']
    lhs=sum((w*((sum(coeff[p] for p in range(125) if int(row['mask'])>>p&1)
                   +aa[TYPES.index((row['size'],row['cost']))])%q)
             for row,w in zip(rows,weights)),Fraction())
    assert sum(x<<(64*i) for i,x in enumerate(result['denominator_limbs']))==den
    assert lhs==Fraction(sum(x<<(64*i) for i,x in enumerate(result['lhs_limbs'])),den)
    result.update(frame=doc['frame'],witness_sha256=sha256(data).hexdigest(),
                  source_sha256=sha256(source.read_bytes()).hexdigest(),
                  lhs=str(lhs),gap=str(lhs-rhs),point_coefficients=coeff,
                  arithmetic='exact unsigned 256-bit integers; direct Python Fraction check',
                  seconds=time.monotonic()-started,review_status='NOT_REVIEWED')
    a.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='point_coefficients'}))


if __name__=='__main__':main()
