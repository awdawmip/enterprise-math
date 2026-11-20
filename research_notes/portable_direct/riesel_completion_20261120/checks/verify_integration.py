"""Root integration check: direct modular powers for every gcd pair.

This consumes the full independently recomputed period dictionary and verifies
the translated graph by direct powers, without the graph builders' recurrence.
It also checks that the packaged scalar results and inherited source pins agree.
"""
from hashlib import sha256
from itertools import combinations
import json
from math import gcd
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]


def read(relative):
    return json.loads((BASE/relative).read_text())


def main():
    graph=read('obstruction/translated_graph_certificate.json')
    packets=read('obstruction/period_dictionary.json')
    prior_check=read('obstruction/verification_results.json')
    assert prior_check['all_assertions_passed']
    assert prior_check['exact_dictionary_rows_recomputed']==513
    assert prior_check['native_source_blob_pins_verified']
    assert [r['q'] for r in packets]==list(range(1,514))
    A,S,t=map(int,[graph['A'],graph['S'],graph['offset']])
    edges={}
    pairs=0
    for row in packets:
        gap,g=int(row['q']),int(row['G'])
        for i in range(1,515-gap):
            # Direct evaluation, independent of both recurrence constructions.
            common=gcd(A*pow(2,S*(t+i),g)-1,g)
            if common>1:
                edges[i,i+gap]=str(common)
            pairs+=1
    assert pairs==131841
    expected={(e['i'],e['j']):e['gcd'] for e in graph['edges']}
    assert edges==expected and len(edges)==11
    cover=set(graph['minimum_vertex_cover'])
    assert cover=={88,146,514}
    assert all(i in cover or j in cover for i,j in edges)
    matching=[tuple(e) for e in graph['matching']]
    assert all(e in edges for e in matching)
    assert len({v for edge in matching for v in edge})==6
    assert set(graph['maximum_independent_set'])==set(range(1,515))-cover

    finite=read('finite_cover/exact_complexity_certificate.json')
    a=int(finite['root_a'])
    exponents=[2*r['private_u'] for r in finite['Q0']]
    assert sorted(exponents)==[6,12,20,32,152]
    samples=[(a*a<<n)-1 for n in exponents]
    assert all(gcd(x,y)==1 for x,y in combinations(samples,2))
    assert all(all(x%p for p in finite['P']) for x in samples)
    assert a%(2*int(finite['M']))==int(finite['a_star'])
    assert finite['exact_minimum_P_outside_cover_primes']==5
    assert finite['full_cover_period']==20160
    assert len(str(a))==225 and len(str(a*a))==450

    k=509203
    six_exponents=[1,3,4,11,15,19]
    six=[k*(1<<n)-1 for n in six_exponents]
    assert all(gcd(x,y)==1 for x,y in combinations(six,2))
    P6=[3,5,7,13,17,241]
    assert all(any((k*pow(2,n,p)-1)%p==0 for p in P6) for n in range(24))
    assert 2*k-1>max(P6)
    triangle_costs=[]
    for ns in [[2,5,13],[2,4,6]]:
        xs=[k*(1<<n)-1 for n in ns]
        assert all(gcd(x,y)>1 for x,y in combinations(xs,2))
        joint=gcd(gcd(xs[0],xs[1]),xs[2])
        triangle_costs.append(1 if joint>1 else 2)
    assert triangle_costs==[2,1]

    shapes=read('shapes/verification.json')
    assert shapes['native_source_blobs_verified']
    assert shapes['two_disjoint_families_phase_vectors']==232243200
    assert shapes['two_families_odd_root_classes']==243524645683200
    source=read('source_scope.json')
    assert source['native_project_source_commit']==prior_check['project_source_commit']==shapes['project_source_commit']
    manifest=read('theory/computation_manifest.json')
    # The manifest has its own schema; this check records its complete hash.
    assert isinstance(manifest,dict)

    paths=['obstruction/period_dictionary.json','obstruction/translated_graph_certificate.json',
           'obstruction/verification_results.json','finite_cover/exact_complexity_certificate.json',
           'theory/proof.md','theory/verify_theory.py','theory/results.json','theory/computation_manifest.json',
           'shapes/verification.json','source_scope.json']
    result={
        'schema':'RIESEL_V5_ROOT_INTEGRATION_CHECK',
        'researcher_id':'EM-DIRECT-970E1C',
        'activity_id':'RA-D2EC212845B63844081F9A14',
        'all_assertions_passed':True,
        'direct_modular_power_pair_checks':pairs,
        'translated_edges':11,'deleted_centres':sorted(cover),
        'fixed_old_root_extra_cover_lower_bound':511,
        'finite_base_extra_cover_minimum':5,'finite_base_pair_gcd_count':10,
        'classic_509203_total_cover_minimum':6,'classic_pair_gcd_count':15,
        'same_boolean_triangle_different_cover_costs':triangle_costs,
        'native_source_commit':source['native_project_source_commit'],
        'inputs_sha256':{s:sha256((BASE/s).read_bytes()).hexdigest() for s in paths},
        'scope':'Author integration check, using the separately recomputed full dictionary; not independent institutional Review or proof of old-root finite-cover nonexistence.'}
    (BASE/'checks/integration_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['all_assertions_passed','direct_modular_power_pair_checks','fixed_old_root_extra_cover_lower_bound','finite_base_extra_cover_minimum','classic_509203_total_cover_minimum']}))


if __name__=='__main__':
    main()
