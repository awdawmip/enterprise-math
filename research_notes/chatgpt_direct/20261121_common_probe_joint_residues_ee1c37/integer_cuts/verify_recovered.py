"""Verify exact modular survivors while explicitly reporting star status.

All inequalities use integer arithmetic. NumPy is used only for small bounded
integer occupancy arrays inside modular_fibers/joint_axes; no solver is called.
"""
from pathlib import Path
from fractions import Fraction
import argparse,importlib.util,json,sys,hashlib
from parallel_family import exact_family
from modular_fibers import scan
from joint_axes import scan_joint

HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--delivery-root',type=Path,default=ROOT/'delivery')
    p.add_argument('--directory',type=Path,default=HERE/'joint_exact');p.add_argument('--frames',type=int,nargs='+',default=[1,2]);p.add_argument('--output',type=Path,default=HERE/'recovered_verification.json')
    p.add_argument('--require-stars',action='store_true');a=p.parse_args()
    sys.path.insert(0,str(a.delivery_root/'fractional/next_cuts'))
    from discovery_common import verify_stars
    spec=importlib.util.spec_from_file_location('native_modular_survivor_verifier',a.delivery_root/'fractional/proof/verify.py')
    native=importlib.util.module_from_spec(spec);spec.loader.exec_module(native)
    bad,pair=native.observation_tables();known={};results=[]
    for f in a.frames:
        path=a.directory/f'cover_{f}.json';data=path.read_bytes();doc=json.loads(data);free=int(doc['free_mask']);cores=list(map(int,doc['core_masks']))
        assert len(cores)==2 and not cores[0]&cores[1] and (cores[0]|cores[1])^((1<<125)-1)==free
        for m in cores:
            known.setdefault(m,native.native_class(m,bad,pair));assert known[m]==(12,1104)
        for r in doc['weights']:
            m=int(r['mask'])
            if m not in known:known[m]=native.native_class(m,bad,pair)
            assert known[m]==(r['size'],r['cost'])
        cover_check=exact_family(doc['weights'],free);assert cover_check['exact_feasible']
        weight={int(r['mask']):Fraction(r['numerator'],r['denominator']) for r in doc['weights']}
        q,worst=verify_stars(weight,free)
        if a.require_stars:assert worst[0]>=0
        checks=[]
        for modulus in [2,3,4,5]:
            ch=scan(doc,modulus,True);assert ch['violating_dp_minima']==0;checks.append(ch)
        joint=scan_joint(doc,3,True);assert joint['violating_dp_minima']==0
        row={'frame':f,'witness_sha256':hashlib.sha256(data).hexdigest(),'support':len(weight),
             'full_cost':9858,'label_weight':12,'all_stars_satisfied':worst[0]>=0,
             'minimum_star_slack':str(Fraction(worst[0],q)),
             'worst_anchor_mask':str(worst[1]),'worst_point':worst[2],
             'single_form_modular_checks':checks,'joint_axes_modular_checks':joint,
             'represented_index_checks':sum(ch['represented_index_checks'] for ch in checks)+joint['represented_index_checks']}
        results.append(row);print(json.dumps({k:v for k,v in row.items() if k not in ['single_form_modular_checks','joint_axes_modular_checks']}),flush=True)
    out={'schema':'MODULAR_SURVIVORS_WITH_EXPLICIT_STAR_STATUS_V1','frames':results,'native_classes_checked':len(known),
         'scope':'Exact feasible points for the declared modular families; full-star feasibility is separately reported and must not be inferred.'}
    a.output.write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':main()
