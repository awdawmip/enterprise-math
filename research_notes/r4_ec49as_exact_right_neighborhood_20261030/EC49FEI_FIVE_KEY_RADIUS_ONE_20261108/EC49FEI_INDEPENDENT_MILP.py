"""EC49FEI independent SciPy/HiGHS set-cover crosscheck of every enumerated depth.
Dependencies EC49FEH_EXACT_CERT.py, EC49FEH_INDEPENDENT_CHECK.py, saved EC49FEI_REPORT.json.
"""
import json
from EC49FEH_INDEPENDENT_CHECK import milp_cover
import EC49FEH_EXACT_CERT as E
import EC49FEI_EXACT_ONE_KEY as R

def run():
    report=json.load(open('EC49FEI_REPORT.json'))
    tested=0
    for record in report['records']:
        keys=list(R.BASE);keys[(4,6,7,9).index(record['h'])+1]=tuple(record['new'])
        groups=[]
        for h,signatures in R.SIGNATURES.items():
            available={(w,s) for k in keys for w,s in E.pool(h,k)}
            for s in signatures:
                words={E.native(w) for w,t in available if t==s}
                assert words
                groups.append(words)
        for i,early in enumerate(report['early_four']):
            checked=[]
            for depth,exact in enumerate(record['depth_covers'][i],1):
                actual=milp_cover(early,groups,depth)
                assert actual==exact,(record['h'],record['new'],i,depth,actual,exact)
                checked.append(actual);tested+=1
            assert len(set().union(*(E.prefixes(w) for w in early)))+sum(checked)==record['all_four_bounds'][i]
    assert tested==2432
    return {'independent_solver':'SciPy/HiGHS integer set cover, MIP gap=0 on all nontrivial depths',
            'inventories':29,'early_variants_each':4,'depth_instances_checked':tested,
            'matches_exact_bitmask_DP':True}

if __name__=='__main__':print(json.dumps(run(),indent=2))
