"""Verify the short parity separators and the stronger combined witnesses.

Standard library only. Reuses the adjacent original finite-menu checker for
new positive classes, without altering that earlier proof directory.
"""
from pathlib import Path
from fractions import Fraction
from itertools import product
import importlib.util,json,argparse
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('full_star_native_verifier',HERE.parent/'proof/verify.py')
native=importlib.util.module_from_spec(spec);spec.loader.exec_module(native)
P=list(product(range(5),repeat=3))
FORMS=[(0,0,1)]+[(0,1,a)for a in range(5)]+[(1,a,b)for a in range(5)for b in range(5)]

def fraction_weight(rows,mask,cores):
    return sum((Fraction(r['numerator'],r['denominator'])for r in rows if(int(r['mask'])&mask).bit_count()%2),Fraction(sum((c&mask).bit_count()%2 for c in cores)))

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,default=HERE/'verification_result.json');a=parser.parse_args()
    cuts=json.loads((HERE/'parity_cuts.json').read_text());separators=[]
    for item in cuts['results']:
        old=json.loads((HERE.parent/'proof'/f'cover_{item["frame"]}.json').read_text());cores=list(map(int,old['core_masks']))
        coordinate_weights=[]
        for c in item['all_coordinate_fibers']:
            axis,value=c['axis_zero_based'],c['value'];mask=sum(1<<i for i,p in enumerate(P)if p[axis]==value)
            assert mask.bit_count()==25 and str(mask)==c['fiber_mask']
            actual=fraction_weight(old['weights'],mask,cores)
            coordinate_weights.append(actual)
            assert actual==Fraction(c['odd_weight_numerator'],c['odd_weight_denominator'])
            assert (actual<1)==c['strict_violation']
            floor=Fraction(c['floor_weight_numerator'],c['floor_weight_denominator'])
            assert 2*floor+actual==25
        c=item['strongest_of_15'];actual=Fraction(c['odd_weight_numerator'],c['odd_weight_denominator']);assert actual<1
        assert actual==min(coordinate_weights)
        assert item['violated_fibers']==sum(w<1 for w in coordinate_weights)
        separators.append({'frame':item['frame'],'axis_zero_based':c['axis_zero_based'],'value':c['value'],'odd_weight':str(actual),'strict_gap':str(1-actual),'violated_coordinate_fibers':item['violated_fibers']})
    bad,pair=native.observation_tables();known={};combined=[]
    for frame in range(1,6):
        path=HERE/'full_system'/f'cover_{frame}.json';doc=json.loads(path.read_text());cores=list(map(int,doc['core_masks']))
        result=native.verify_one(path,bad,pair,known)
        parity=[]
        for form in FORMS:
            for value in range(5):
                mask=sum(1<<i for i,p in enumerate(P)if sum(x*y for x,y in zip(form,p))%5==value)
                assert mask.bit_count()==25
                weight=fraction_weight(doc['weights'],mask,cores);assert weight>=1
                parity.append(weight)
        result.update(affine_fiber_parity_cuts_checked=155,minimum_parity_weight=str(min(parity)),parity_equalities=sum(w==1 for w in parity))
        combined.append(result);print(json.dumps(result),flush=True)
    output={'schema':'FULL_STAR_PARITY_SEPARATION_AND_JOINT_FEASIBILITY_V1','old_points_strictly_separated':separators,'new_combined_feasible_points':combined,'new_native_classes_checked':len(known),'total_fiber_parity_checks':775,'total_internal_star_checks':sum(r['star_checks_inside_free']for r in combined),'scope':'cuts separate old points; the complete full-star family plus all 155 affine-fiber parity inequalities still has exact rational cost-9858 feasible witnesses'}
    a.output.write_text(json.dumps(output,indent=2)+'\n');print(json.dumps({'all_verified':True,'native_classes':len(known),'star_checks':output['total_internal_star_checks']}),flush=True)

if __name__=='__main__':main()
