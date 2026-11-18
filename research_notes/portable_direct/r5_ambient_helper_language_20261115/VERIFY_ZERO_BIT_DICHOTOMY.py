"""Exhaustive 3-bit language verification of the zero-helper dichotomy.
Requires VERIFY_AMBIENT_HELPERS.py in the same directory. Uses exact integer
branch-and-bound over all old advice subsets, not random sampling.
"""
import json
from itertools import combinations
from VERIFY_AMBIENT_HELPERS import exact_min_cover, library_ok

def run():
    d=3
    Y=(1,2,4)
    outside=tuple(v for v in range(1<<d) if v not in Y)
    rows=[]
    for bits in range(1<<len(outside)):
        X=tuple(sorted(Y+tuple(v for j,v in enumerate(outside) if (bits>>j)&1)))
        a, aw=exact_min_cover(d,X,Y,'a')
        ab, abw=exact_min_cover(d,X,Y,'ab')
        expected_a=5 if 0 in X else 6
        assert a==expected_a and ab==6
        assert library_ok(Y,[tuple(row) for row in aw],'a')
        assert library_ok(Y,[tuple(row) for row in abw],'ab')
        rows.append({'X':list(X),'includes_zero':0 in X,'kappa_a':a,'kappa_ab':ab})
    by_zero={str(z):[sum(1 for row in rows if row['includes_zero']==z),
                     sorted(set(row['kappa_a'] for row in rows if row['includes_zero']==z))]
             for z in [False,True]}
    report={'status':'PASS_R5_ZERO_BIT_DICHOTOMY_EXHAUSTIVE_D3',
            'frozen_science_pin':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
            'scope':'d=r=3, Y={001,010,100}, all 32 old languages X with Y subseteq X subseteq Q3',
            'cases':len(rows),'summary_by_zero_membership':by_zero,'exact_rows':rows,
            'theorem':'For all d>=r>=3 and Y={e_i}: kappa_a(X,Y;2)=r+2 if zero in X else 2r; kappa_ab(X,Y;2)=2r. Finite d3 run corroborates the universal proof.'}
    print(json.dumps(report,indent=2,ensure_ascii=False,sort_keys=True))
if __name__=='__main__':run()
