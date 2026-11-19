"""Exact CRT minimization over all translation orbits in the radius-two cover neighborhood.

Each of the 29 distinct labelled phase shapes is minimized over all 3360
translations and all 2^20 root signs. The sign minimum uses the established
exact meet-in-the-middle algorithm. A final full Gray enumeration checks the
winning phase vector. The search input consists of the exhaustively classified
local shapes, not a supplied optimum.
"""
from __future__ import annotations

import json
import argparse
from math import prod
from pathlib import Path
import sys
from time import perf_counter

DIRECTORY = Path(__file__).resolve().parent
PRIOR = DIRECTORY.with_name('riesel_mixed_20261119')
sys.path.insert(0, str(PRIOR))
from minimize import crt_parameters, mitm_minimum, gray_minimum


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--divisible-by-3',action='store_true')
    args=parser.parse_args()
    suffix='_mod3' if args.divisible_by_3 else ''
    begin=perf_counter()
    original=json.loads((PRIOR / 'certificate.json').read_text())['original']
    local=json.loads((DIRECTORY / 'local_shapes_results.json').read_text())
    rows=original['rows'];primes=[r['p'] for r in rows]
    old=local['original_u_phases'];es=local['effective_periods'];L=local['period']
    product=prod(primes)
    # 3*M is divisible by every p, and is 3 mod 6 because M is odd.
    # Thus the constrained CRT fixes a=3 mod 6 while retaining all signs.
    crt_base=3*product if args.divisible_by_3 else product
    modulus=2*crt_base
    basis=[(modulus//p)*pow(modulus//p,-1,p)%modulus for p in primes]
    inverses=[pow(2,-1,p) for p in primes]
    global_min=modulus; shapes=[]
    for index,phases in enumerate(local['canonical_representatives']):
        roots=[r['a_residue']*pow(2,old_c-new_c,r['p'])%r['p']
               for r,old_c,new_c in zip(rows,old,phases)]
        best=modulus
        for shift in range(L):
            base,deltas=crt_parameters(roots,basis,crt_base,modulus)
            candidate,mask=mitm_minimum(base,deltas,modulus)
            if candidate<best:
                best,best_shift,best_mask=candidate,shift,mask
                best_roots=list(roots);best_base=base;best_deltas=list(deltas)
            roots=[c*inv%p for c,inv,p in zip(roots,inverses,primes)]
        row={'shape_index':index,'canonical_u_phases':phases,'minimum_root':str(best),
             'translation_in_u':best_shift,'sign_mask':best_mask}
        shapes.append(row)
        if best<global_min:
            global_min=best;winning_index=index
            winning_roots=best_roots;winning_mask=best_mask;winning_shift=best_shift
            winning_base=best_base;winning_deltas=best_deltas;winning_canonical=list(phases)
        print(json.dumps({'shape':index,'minimum_root':str(best),'global_minimum':str(global_min),
                          'elapsed_seconds':round(perf_counter()-begin,3)}),flush=True)
        (DIRECTORY / ('search_checkpoint'+suffix+'.json')).write_text(json.dumps({'completed_shapes':shapes,'best_so_far':str(global_min)},indent=2)+'\n')
    assert gray_minimum(winning_base,winning_deltas,modulus)==(global_min,winning_mask)
    winning_rows=[]
    for i,(r,e,c,root) in enumerate(zip(rows,es,winning_canonical,winning_roots)):
        u=(c+winning_shift)%e
        b=(2*u+1)%r['order']
        ares=((-1 if (winning_mask>>i)&1 else 1)*root)%r['p']
        assert global_min%r['p']==ares
        assert ares*ares*pow(2,b,r['p'])%r['p']==1
        winning_rows.append({'p':r['p'],'order':r['order'],'exponent_phase':b,
                             'a_residue':ares,'u_period':e,'u_phase':u})
    all_hits=[[r['p'] for r in winning_rows if (n-r['exponent_phase'])%r['order']==0]
              for n in range(2*L)]
    assert all(all_hits[n] for n in range(1,2*L,2))
    assert global_min%2==1 and 2*global_min*global_min-1>max(primes)
    assert not args.divisible_by_3 or global_min%3==0
    result={'schema':'RIESEL_RADIUS_TWO_TRANSLATED_ROOT_MINIMUM_V1',
            'researcher_id':'EM-DIRECT-970E1C','research_activity_id':'RA-D2EC212845B63844081F9A14',
            'scope':'Original 20-channel odd cover and all covers differing in exactly two u-phases, then every global u-translation and independent root sign. Exact minimum over this finite union only.',
            'shape_count':len(shapes),'translations_per_shape':L,'root_signs_per_translation':2**len(rows),
            'distinct_odd_root_classes':len(shapes)*L*2**len(rows),
            'root_divisible_by_3_required':args.divisible_by_3,
            'odd_crt_modulus':str(modulus),'minimum_positive_odd_root':str(global_min),
            'minimum_square_k':str(global_min**2),'minimum_root_digits':len(str(global_min)),
            'winning_shape_index':winning_index,'winning_translation_u':winning_shift,
            'winning_sign_mask':winning_mask,'winning_gray_check_passed':True,
            'source_url':original['source_url'],'source_table':'Table 6 with an exact radius-two phase modification and global even translation',
            'rows':winning_rows,'all_shape_minima':shapes,
            'odd_covered':sum(bool(all_hits[n]) for n in range(1,2*L,2)),
            'even_covered':sum(bool(all_hits[n]) for n in range(0,2*L,2)),
            'uncovered_phases':[n for n,h in enumerate(all_hits) if not h],
            'elapsed_seconds':perf_counter()-begin}
    (DIRECTORY / ('optimized_results'+suffix+'.json')).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('rows','all_shape_minima','uncovered_phases')},indent=2))


if __name__=='__main__':main()
