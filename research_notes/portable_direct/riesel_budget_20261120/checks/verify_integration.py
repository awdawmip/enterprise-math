"""Cross-check the integrated mathematical certificates and inherited source pins.

Branch verifiers establish arithmetic results; this checks that the merged
report uses the same old root/observer and preserves the stated quantifiers.
"""
from hashlib import sha1,sha256
import json
import sys
from math import gcd,prod
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]
ROOT=next(p for p in BASE.parents if (p/'research_notes/portable_direct/riesel_mixed_20261119/certificate.json').is_file())

def load(name):return json.loads((BASE/name).read_text())
def blob(b):return sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

def main():
    sys.set_int_max_str_digits(0)
    scope=load('source_scope.json')
    inherited=[]
    for dep in scope['scientific_dependencies']:
        p=ROOT/dep['path'];b=p.read_bytes()
        assert blob(b)==dep['git_blob'],str(p)
        inherited.append(dict(dep,sha256=sha256(b).hexdigest()))
    cost=load('cost/total_cost_certificate.json')
    forbidden=load('forbidden/forbidden_extension_certificate.json')
    m2=load('forbidden/m2_extension_certificate.json')
    budget=load('budget/window_certificate.json')
    minimum=load('minimum/minimum_six_certificate.json')
    fixed=load('fixed/verification_results.json')
    recheck=load('checks/fixed_integration_results.json')
    inputs=load('fixed/input.json')
    P=cost['P'];a=int(cost['a_star']);M=int(cost['M'])
    assert len(P)==20 and M==prod(P)
    assert a==int(forbidden['a_star'])==int(m2['a_star'])==int(inputs['a'])
    assert P==forbidden['P']==m2['P']==[r['p'] for r in inputs['original_twenty_channels']]
    roots=[]
    for c in cost['numeric_certificates']:
        root=int(c['root_a']);Q=[r['p'] for r in c['Q']]
        assert root%(2*M)==a and c['exact_total_tau']==20+c['exact_delta_P']
        assert c['exact_delta_P']==len(Q)
        assert len(c['witnesses'])==len(P)+len(Q)
        assert len(c['all_pairwise_gcds'])==(20+len(Q))*(19+len(Q))//2
        assert all(r['gcd']==1 for r in c['all_pairwise_gcds'])
        roots.append({'delta_P':c['exact_delta_P'],'tau':c['exact_total_tau'],
                      'a_digits':c['root_summary']['decimal_digits']})
    assert cost['mixed_skeleton_count']==62
    assert [r[0] for r in cost['cofinite_bases_s_seed_h_j']]==[13,14,15,16]
    assert forbidden['exact_minimum_P_outside_cover_primes']==11
    assert forbidden['total_cover_size_bound']==31
    assert 'exact_total_tau' not in forbidden  # Do not attach the other subfamily's equality to this root.
    assert m2['exact_delta_P']==33 and m2['exact_total_tau']==53
    assert len(m2['private_witnesses'])==53 and len(m2['all_pairwise_gcd_checks'])==1378
    root_m2=int(m2['root_a_hex'],16)
    assert root_m2%(2*M)==a and root_m2%int(m2['T_Bm'])==0
    assert all(r['relative_order_R']>2 and r['q']>17 for r in m2['rows'])
    assert minimum['exhaustive_search']['found'] is False
    assert minimum['maximum_relevant_order']==16 and minimum['finite_window_length']==32
    assert minimum['six_prime_witness']['k']==509203
    assert budget['k509203']['exact_total_cost']==6
    assert len(budget['k509203']['six_coprime_exponents'])==6
    assert budget['old_hole_budget5']['sample_count']==36*2**5
    assert budget['old_hole_budget5']['max_exponent']==210*2**5
    assert fixed['all_assertions_passed'] and recheck['all_assertions_passed']
    assert fixed['packet_backend']=='independent_GMP_full_recomputation_in_this_run'
    assert recheck['packet_backend']=='comparison_to_supplied_independent_GMP_full_recomputation'
    for key in ['exact_packets_verified','complete_pair_count_two_ambient_windows',
                'main_window_minimum_prime_cover_size','joint_example_minimum_prime_cover_size',
                'native_projected_updates_verified']:
        assert fixed[key]==recheck[key]
    assert fixed['any_full_cover_minimum_primes_outside_old_P']==892
    assert fixed['if_old_P_is_retained_minimum_total_primes']==912
    assert fixed['joint_example_maximum_pairwise_coprime_size']==880
    assert fixed['joint_example_minimum_prime_cover_size']==881
    native=scope['native_source']['modules']
    assert fixed['project_source_blobs']==native
    for c in [cost,forbidden,m2]:
        assert {n:r.get('observed',r.get('observed_git_blob_sha1'))
                for n,r in c['project_source_blob_checks'].items()}==native
    assert {n:r['observed'] for n,r in budget['native_source_checks_before_import'].items()}==native
    out=BASE/'checks/integration_results.json'
    files=[p for p in BASE.rglob('*') if p.is_file() and p!=out and '__pycache__' not in p.parts]
    manifest=[{'path':str(p.relative_to(BASE)),'bytes':p.stat().st_size,
               'sha256':sha256(p.read_bytes()).hexdigest(),'git_blob':blob(p.read_bytes())}
              for p in sorted(files)]
    result={'schema':'enterprise-math.riesel-v6-integration.v1','all_checks_passed':True,
            'researcher_id':scope['researcher_id'],'activity_id':scope['research_activity_id'],
            'inherited_sources_verified':inherited,'numeric_total_cost_examples':roots,
            'same_old_P_and_a_star_across_branches':True,
            'forbidden_744_digit_root_total_upper_bound_not_equality':True,
            'classical_budget_horizon':'2**t','universal_finite_cover_minimum':6,
            'fixed_old_root_additional_lower_bound':892,
            'fixed_old_root_finite_cover_existence':'UNRESOLVED',
            'same_fixed_root_joint_gap':[880,881],
            'native_blob_identity_shared':native,
            'file_manifest_excluding_this_output':manifest,
            'review_status':'Author exact verification and same-context cross-checks; not independent project Review.'}
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'all_checks_passed':True,'files_in_manifest':len(manifest),
                      'fixed_lower_bound':892,'universal_minimum':6,
                      'total_cost_examples':roots,'output':str(out)}))

if __name__=='__main__':main()
