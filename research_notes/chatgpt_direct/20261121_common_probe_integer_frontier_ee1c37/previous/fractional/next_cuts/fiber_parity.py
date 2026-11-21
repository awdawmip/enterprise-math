"""Exact short integer cuts for the five full-star fractional witnesses."""
from pathlib import Path
from itertools import product
from fractions import Fraction
import json
HERE=Path(__file__).resolve().parent
P=list(product(range(5),repeat=3))

def fibers():
    return [(axis,value,sum(1<<i for i,p in enumerate(P)if p[axis]==value))for axis in range(3)for value in range(5)]

def compute():
    results=[]
    for frame in range(1,6):
        doc=json.loads((HERE.parent/'proof'/f'cover_{frame}.json').read_text());rows=doc['weights'];cores=list(map(int,doc['core_masks']));cuts=[]
        for axis,value,mask in fibers():
            assert mask.bit_count()==25
            core_odd=sum((m&mask).bit_count()%2 for m in cores)
            odd=sum((Fraction(r['numerator'],r['denominator'])for r in rows if(int(r['mask'])&mask).bit_count()%2),Fraction(core_odd))
            floor_sum=sum((Fraction(r['numerator'],r['denominator'])*((int(r['mask'])&mask).bit_count()//2)for r in rows),Fraction(sum((m&mask).bit_count()//2 for m in cores)))
            assert 2*floor_sum+odd==25
            cuts.append({'axis_zero_based':axis,'value':value,'fiber_mask':str(mask),'odd_weight_numerator':odd.numerator,'odd_weight_denominator':odd.denominator,'floor_weight_numerator':floor_sum.numerator,'floor_weight_denominator':floor_sum.denominator,'strict_violation':odd<1,'core_odd_weight':core_odd})
        best=min(cuts,key=lambda c:Fraction(c['odd_weight_numerator'],c['odd_weight_denominator']))
        assert best['strict_violation']
        results.append({'frame':frame,'strongest_of_15':best,'violated_fibers':sum(c['strict_violation']for c in cuts),'all_coordinate_fibers':cuts})
        print(json.dumps({'frame':frame,'best':best,'violated_fibers':results[-1]['violated_fibers']}),flush=True)
    out={'schema':'ODD_FIBER_INTEGER_CUTS_V1','scope':'strictly separates five supplied full-star rational points; does not assert infeasibility of the strengthened relaxation','cut':'sum_C (|C intersect H| mod 2) x_C >= 1, H any 25-point coordinate fiber','equivalent_cut':'sum_C floor(|C intersect H|/2) x_C <= 12','results':results}
    (HERE/'parity_cuts.json').write_text(json.dumps(out,indent=2)+'\n')
    return out

if __name__=='__main__':compute()
