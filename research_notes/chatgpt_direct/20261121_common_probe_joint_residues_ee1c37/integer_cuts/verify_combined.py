"""Exact native-class, point/type, full-star, parallel-fiber/type verification.

This script uses Python's standard library and the unchanged predecessor
native finite-menu verifier. No optimizer or numerical tolerance is used.
"""
from pathlib import Path
import argparse,importlib.util,json,hashlib
from parallel_family import exact_family

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--delivery-root',type=Path,default=ROOT/'delivery')
    p.add_argument('--witness-dir',type=Path,default=HERE/'full_system')
    p.add_argument('--output',type=Path,default=HERE/'combined_verification.json')
    a=p.parse_args()
    path=a.delivery_root/'fractional/proof/verify.py'
    spec=importlib.util.spec_from_file_location('unchanged_native_finite_checker',path)
    native=importlib.util.module_from_spec(spec);spec.loader.exec_module(native)
    bad,pair=native.observation_tables();known={};results=[]
    for f in range(1,6):
        src=a.witness_dir/f'cover_{f}.json';data=src.read_bytes();d=json.loads(data)
        row=native.verify_one(src,bad,pair,known)
        new=exact_family(d['weights'],int(d['free_mask']))
        assert new['exact_feasible']
        row.update(witness_sha256=hashlib.sha256(data).hexdigest(),
                   parallel_fiber_type_checks=new['tested'],minimum_new_parity_weight=new['minimum']['lhs'])
        results.append(row);print(json.dumps(row),flush=True)
    out={'schema':'FULL_STAR_PARALLEL_FIBER_TYPE_EXACT_FEASIBILITY_V1',
         'frames':results,'native_classes_verified':len(known),
         'total_star_checks':sum(r['star_checks_inside_free'] for r in results),
         'total_parallel_fiber_type_checks':sum(r['parallel_fiber_type_checks'] for r in results),
         'scope':'Exact cost-9858 rational witnesses for all five frames, satisfying every full-star inequality and every parity combination of one parallel-fiber union with the four prescribed type counts. This is not an integer partition.'}
    a.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'all_verified':True,'native_classes':len(known),'star_checks':out['total_star_checks'],'parity_checks':out['total_parallel_fiber_type_checks']}),flush=True)

if __name__=='__main__':main()
