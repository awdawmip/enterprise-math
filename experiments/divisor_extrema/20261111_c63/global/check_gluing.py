"""Check the constants used to join the arbitrary-length prefix to the 63-pair suffix."""
from fractions import Fraction as Q
from math import factorial, gcd
from pathlib import Path
import json
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'numeric'))
from certify_schedules import block_maps

def rational(pair):
    return Q(*map(int,pair))

def load_result(name):
    return json.loads((ROOT/'numeric'/name).read_text())

def potential(r,c):
    s=c-r-1
    if s<=0:
        return Q(16)**s
    return Q(16**(s-1)*factorial(2*r+c+1),factorial(3*r+3))

def run():
    small=load_result('schedule_certificates.json')
    assert [v['k'] for v in small]==list(range(2,101))
    for row in small:
        assert rational(row['exact_ahead_delta']) < rational(row['exact_competitor_lower'])
        if row['k']>=3:
            assert rational(row['exact_competitor_lower'])>2*rational(row['exact_ahead_delta'])
    cut=load_result('cut63_full.json')
    upper=rational(cut['ahead_derivative_sup'])
    assert [row['stock'] for row in cut['rows']]==list(range(2,97))
    weighted=[(potential(63,row['stock'])*rational(row['lower'])/upper,row['stock'])
              for row in cut['rows']]
    worst,where=min(weighted)
    assert where==64 and worst>14
    ext=load_result('cut63_extension.json')
    assert (ext['finite_start'],ext['finite_end'],ext['large_stock_start'])==(97,318,319)
    assert ext['finite_min_ratio_floor']>2 and rational(ext['large_stock_ratio_at_start'])>2
    p,q,s,t=1,0,0,1
    for r in range(1,64):
        index=0 if r==1 else 1
        from itertools import islice
        a,b,h=next(islice(block_maps(r,r+1),index,None))
        p,q,s,t=q*(b-h),p*a+q*(a+h),t*(b-h),s*a+t*(a+h)
        common=gcd(p,q,s,t)
        p,q,s,t=(v//common for v in (p,q,s,t))
    assert min(t,s+t)>0
    assert upper==Q(abs(p*t-q*s),8*min(t,s+t)**2)
    minimum_over_upper=Q(min(t,s+t),max(t,s+t))**2
    assert minimum_over_upper>Q(99,100)
    assert Q(377,378)*Q(21,10)*Q(99,100)>2
    return dict(k_checked=[2,100],cut=63,least_finite_competitor_stock=where,
                small_cut_competitor_lower_over_U_floor=worst//1,
                canonical_cut_min_over_U_exceeds='99/100',prefix_canonical_distortion_exceeds='377/378',
                high_defect_comparison_exceeds='2',unbounded_stock_start=319)

if __name__=='__main__':
    print(json.dumps(run(),indent=2))
