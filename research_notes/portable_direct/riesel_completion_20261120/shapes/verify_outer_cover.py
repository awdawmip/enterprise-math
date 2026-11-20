"""Exact verifier for a second family of square-compatible odd covers.

The numerical candidate finder is not used here. This checks the candidate,
the distinguishing mod-3 invariant, and the native BRC residual dynamics.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha1, sha256
import json
from math import gcd
from pathlib import Path
import sys

DIRECTORY = Path(__file__).resolve().parent
ROOT = next(p for p in DIRECTORY.parents
            if (p/'research_notes/portable_direct/riesel_families_20261119').is_dir())
PREVIOUS = ROOT/'research_notes/portable_direct/riesel_families_20261119/phase'
sys.path.insert(0, str(PREVIOUS))
from prepare_family import PRIMES, PERIODS, PHASES, ROWS, INDEX, L, M, membership


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source-dir', type=Path, default=ROOT/'vendor_src')
    args = parser.parse_args()
    data = json.loads((DIRECTORY/'outer_cover_result.json').read_text())
    vector = data['phases']
    assert data['prime_channels'] == PRIMES and data['periods'] == PERIODS
    assert len(vector) == len(PRIMES) == 20 and L == 3360
    a = int(data['a'])
    assert a % 2 == 1 and int(data['k']) == a*a
    assert 2*a*a-1 > max(PRIMES)
    assert [a % p for p in PRIMES] == data['root_residues']
    for p, c, e in zip(PRIMES, vector, PERIODS):
        assert 0 <= c < e
        assert (a*a*pow(2, 2*c+1, p)-1) % p == 0
    assert all(any(u % e == c for c, e in zip(vector, PERIODS)) for u in range(L))

    # Every member of the previous full translation closure has delta=1.
    i7, i241 = INDEX[7], INDEX[241]
    invariant_old = (PHASES[i241]-PHASES[i7]) % 3
    invariant_new = (vector[i241]-vector[i7]) % 3
    assert invariant_old == 1 and invariant_new == 2
    assert not any(membership([(c-t) % e for c,e in zip(vector, PERIODS)])
                   for t in range(L))

    # Iota fixes the mod-1120 coordinate and negates the mod-3 coordinate.
    unit = 1121
    assert unit % 1120 == 1 and unit % 3 == 2
    assert gcd(unit,L) == 1 and unit*unit % L == 1
    assert sorted(unit*u % L for u in range(L)) == list(range(L))
    reflected_base = [unit*c % e for c,e in zip(PHASES,PERIODS)]
    assert all(any(u % e == c for c,e in zip(reflected_base,PERIODS)) for u in range(L))
    preimage_shifts = [t for t in range(L)
                      if membership([(pow(unit,-1,e)*(c-t)) % e
                                     for c,e in zip(vector,PERIODS)])]
    assert preimage_shifts == list(range(56,L,240))

    prior = json.loads((ROOT/'research_notes/portable_direct/riesel_mixed_20261119/results.json').read_text())
    for name, expected in prior['project_source_blobs'].items():
        body = (args.source_dir/'enterprise_math'/name).read_bytes()
        assert sha1(b'blob '+str(len(body)).encode()+b'\0'+body).hexdigest() == expected
    sys.path.insert(0,str(args.source_dir.resolve()))
    from enterprise_math.brc_transport import Affine, EffectHistogram, euclidean_digits
    step = EffectHistogram.from_terms(1,[(1,Affine(((2,),),(1,)),1)])

    def advance(x,p):
        (point, weights), = step.evaluate((x,)).items()
        assert weights.entries == ((Fraction(1),1),)
        assert point[0].denominator == 1
        return euclidean_digits(int(point[0]),(p,))[1][0]

    native_rows=[]
    for p,c,e,row in zip(PRIMES,vector,PERIODS,ROWS):
        d=row['order']
        x=(a*a-1) % p
        cycle=[]
        for n in range(d):
            cycle.append(x)
            x=advance(x,p)
        assert x==cycle[0]
        zeros=[n for n,r in enumerate(cycle) if r==0]
        assert zeros==[(2*c+1) % d]
        assert [u for u in range(e) if cycle[(2*u+1) % d]==0]==[c]
        native_rows.append({'p':p,'order_2':d,'odd_u_period':e,'odd_u_phase':c,
                            'zero_exponent_phase':zeros[0]})
    previous_count=json.loads((PREVIOUS/'family_input.json').read_text())['distinct_translated_phase_vectors']
    assert previous_count==116121600
    result={
        'schema':'RIESEL_MOD3_REFLECTED_COVER_FAMILY_V5',
        'researcher_id':'EM-DIRECT-970E1C',
        'activity_id':'RA-D2EC212845B63844081F9A14',
        'a':str(a),'k':str(a*a),'candidate_sha256':sha256((DIRECTORY/'outer_cover_result.json').read_bytes()).hexdigest(),
        'period':L,'odd_classes_covered':L,'invariant_old':invariant_old,'invariant_new':invariant_new,
        'unit':unit,'unit_is_involution':True,'preimage_shifts':preimage_shifts,
        'previous_family_phase_vectors':previous_count,'two_disjoint_families_phase_vectors':2*previous_count,
        'two_families_odd_root_classes':2*previous_count*2**20,
        'native_rows':native_rows,'project_source_commit':prior['project_source_commit'],
        'project_source_blobs':prior['project_source_blobs'],'native_source_blobs_verified':True,
        'scope':'Two disjoint valid subfamilies; not all fixed-P covers and no new minimum claimed. Multiplication of the index is a bijection of the finite covering domain, not a future-preserving quotient of the original shift dynamics.'}
    (DIRECTORY/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({key:result[key] for key in ['a','odd_classes_covered','invariant_old','invariant_new','two_disjoint_families_phase_vectors','two_families_odd_root_classes','native_source_blobs_verified']},indent=2))


if __name__=='__main__':
    main()
