"""Own nonauthor exact consumption of immutable remaining271 compact trees.

Imports only this Driver's arithmetic prepared before new Source delivery.
Does not import/run the producer or its consumers. Verifies all Source bytes,
all complete saved branches and alternate-coset spheres; native acceptance
requires the separate actual RR/control review. q2-1 is joined to its already
Source-verified independent review receipt and is not scientifically rerun.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,re,argparse
import reviewer_order2_math_core as M

HERE=Path(__file__).resolve().parent
CORE_SHA='569c130db1a3ed04be5e66cdd2f699a766b091fe340d5888a90c3252dcaf9f1a'
SOURCE='953db05d78bd0f175a99d0406f850691d479ae26'
PREFIX='research_artifacts/mcp/RS-T6-P17-ORDER2-PORTABLE-CERTIFICATE-20260923/MCP-2b2adc7725e84b0c90908ba5db66a17f/c00a2e10ac40d9d32159/'
SOURCE_ROOT=HERE/'source953'
OLD_REVIEW_DIR=HERE.parent/'q2-1-review'
OLD_SOURCE_ROOT=None
TASK='RS-T6-P17-ORDER2-PORTABLE-CERTIFICATE-20260923'
PUB='TP2-33BFE7DD84657DAB803C'
SOURCE_COMPACT_SHA='fa7e5bcc32ffa7c853e8d767fc949d74fd8a55533a6bb26a9125644fa5c65273'

def integer(value):
    M.check(type(value) is str and re.fullmatch(r'-?(0|[1-9][0-9]*)',value),
            'canonical signed decimal proof integer')
    M.check(value!='-0','noncanonical negative zero')
    return int(value)

def index(value):
    M.check(type(value) is int,'exact index integer, excluding bool')
    return value

def verify_custody():
    M.check(hashlib.sha256((HERE/'reviewer_order2_math_core.py').read_bytes()).hexdigest()
            ==CORE_SHA,'unchanged own pre-Source arithmetic')
    manifest=M.read_json(HERE/'ACTUAL_NEW_SOURCE_COMPLETE_VERIFIED.json')
    M.check(manifest['source_commit']==SOURCE and manifest['outer8_native_manifest_verified']
            is True and manifest['outer8_bytes']==899432,'complete immutable Source prerequisite')
    seen=set()
    for row in manifest['rows']:
        M.check(row['path'] not in seen,'unique Source path')
        seen.add(row['path'])
        raw=(SOURCE_ROOT/row['path']).read_bytes()
        M.check(len(raw)==row['bytes'] and hashlib.sha256(raw).hexdigest()==row['sha256'],
                'complete Source bytes/SHA256')
        M.check(hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
                ==row['git_blob_sha1'],'complete Source Git blob')
    root=SOURCE_ROOT
    checkpoint=M.read_json(root/PREFIX/'_checkpoint.json')
    pins={r['path']:r for r in manifest['rows']}
    M.check(len(checkpoint['output_manifest'])==8,'all eight required outputs')
    for row in checkpoint['output_manifest']:
        pin=pins[row['path']]
        M.check(pin['sha256']==row['sha256'].removeprefix('sha256:')
                and pin['git_blob_sha1']==row['git_blob_sha1'].removeprefix('sha1:'),
                'actual native checkpoint-manifest binding')
    return root,manifest

def consume_case(exact,ledger,common):
    cid=exact['id']
    M.check(ledger['pattern_id']==cid,'original pattern ID')
    M.check([[integer(v) for v in x] for x in ledger['positive_atoms']]
            ==[list(v) for v in exact['positive_atoms']],'positive signed descriptors')
    M.check([[integer(v) for v in x] for x in ledger['negative_atoms']]
            ==[list(v) for v in exact['negative_atoms']],'negative signed descriptors')
    M.check(integer(ledger['positive_vertical_mass'])==2331-exact['positive_budget']
            and integer(ledger['negative_vertical_mass'])==2331-exact['negative_budget'],
            'both exact fixed-atom masses')
    M.check(integer(ledger['q0_positive_budget'])==exact['positive_budget']
            and integer(ledger['q0_negative_budget'])==exact['negative_budget'],
            'both exact residual budgets')
    radius=exact['radius_squared']
    M.check(integer(ledger['radius_squared'])==radius,'exact necessary sphere radius')
    M.check([integer(v) for v in ledger['mixed_targets']]==exact['targets'],
            'all six independently derived original targets')
    admissible=exact['maximal_p17_domain']=='ADMISSIBLE'
    M.check(type(ledger['maximal_p17_admissible']) is bool
            and ledger['maximal_p17_admissible']==admissible,'separate exact domain label')
    largest=max([17]+[v for row in exact['cofactor_factorizations'] for v in row])
    M.check(integer(ledger['largest_vertical_prime'])==largest,'composite complete factor domain')
    M.check(ledger['literal_relaxed_outcome_even_if_outside_domain'] is True,
            'outside label is not substituted for literal classification')
    rep=[integer(v) for v in ledger['particular_q0']]
    M.check(len(rep)==16 and M.residues(rep)==exact['targets'],
            'actual representative in original mixed coset')
    offset=[w*v for w,v in zip(common['weights'],rep)]
    h=[M.dot(offset,star)/d for star,d in zip(common['stars'],common['norms'])]
    M.check(sum(d*c*c for d,c in zip(common['norms'],h))==M.dot(offset,offset),
            'complete exact affine Gram identity')
    M.check(all(d>radius for d in common['norms']),'all adjacent-completeness premises')
    M.check(ledger['certificate_encoding']=='COMPACT_INDEXED_TWO_CHOICE_TREE_V1',
            'declared actual compact encoding')
    nodes=ledger['nodes']
    by={index(node['id']):node for node in nodes}
    M.check(len(by)==len(nodes) and index(ledger['root'])==0,'unique node IDs and root0')
    visited=set()
    decisions=[]
    def visit(nid,i,suffix,spent):
        M.check(nid in by and nid not in visited,'connected child exists and unique parent')
        visited.add(nid)
        node=by[nid]
        M.check(index(node['index'])==i and 0<=i<16,'correct descending index/no hidden leaf')
        center=h[i]+sum(common['mu'][j][i]*suffix[j-i-1] for j in range(i+1,16))
        quotient,remainder=divmod(center.numerator,center.denominator)
        M.check(center.numerator==quotient*center.denominator+remainder
                and 0<=remainder<center.denominator,'independent Euclidean divrem')
        expected={-quotient-1,-quotient}
        edges=node['edges']
        M.check(len(edges)==2 and {integer(e['z']) for e in edges}==expected,
                'both complete adjacent integer choices')
        for edge in edges:
            value=integer(edge['z'])
            norm=spent+common['norms'][i]*(F(value)+center)**2
            pruned=norm>radius
            M.check(edge['action']==('NORM_PRUNED' if pruned else 'CHILD'),
                    'each exact norm decision, strict pruning and equality retention')
            decisions.append({'node':nid,'index':i,'higher_z':[str(v) for v in suffix],
                              'chosen':str(value),'center':M.pair(center),
                              'prior_norm':M.pair(spent),'norm':M.pair(norm),
                              'norm_minus_radius':M.pair(norm-radius),'strict_prune':pruned})
            if pruned:
                M.check('child' not in edge,'no hidden pruned child')
            else:
                M.check(i>0,'claimed zero-sphere-leaf result cannot hide a full feasible leaf')
                visit(index(edge['child']),i-1,[value]+suffix,norm)
    visit(0,15,[],F())
    M.check(visited==set(by),'every declared node reachable exactly once')
    M.check(ledger['complete_traversal'] is True and ledger['resource_exhausted'] is False
            and ledger['outcome']=='EMPTY' and ledger['survivors']==[],
            'actual complete EMPTY outcome/resource status')
    alternate=M.alternate_full_sphere(exact,common)
    M.check(alternate['leaves']==[],'independent alternate-coset full sphere is empty')
    alternate_rep=list(map(int,alternate['alternate_q0']))
    M.check(M.residues([a-b for a,b in zip(alternate_rep,rep)])==[0]*6,
            'alternate/Source roots differ in full saturated original kernel')
    strict=[F(*map(int,d['norm_minus_radius'])) for d in decisions if d['strict_prune']]
    payload=json.dumps({'saved_tree_decisions':decisions,'alternate_sphere':alternate},
                       sort_keys=True,separators=(',',':')).encode()
    return ({'case_id':cid,'outcome':'EMPTY_NECESSARY_AFFINE_SPHERE',
             'maximal_p17_domain':exact['maximal_p17_domain'],
             'cofactor_factorizations':exact['cofactor_factorizations'],
             'positive_budget':str(exact['positive_budget']),
             'negative_budget':str(exact['negative_budget']),
             'radius_squared':str(radius),'mixed_targets':[str(v) for v in exact['targets']],
             'actual_source_representative':[str(v) for v in rep],
             'affine_centers':[M.pair(v) for v in h],
             'consumed_nodes':len(visited),'consumed_twochild_choices':len(decisions),
             'strict_prunes':len(strict),'smallest_strict_prune_margin':M.pair(min(strict)),
             'sphere_leaves':0,'completed_signed_budget_candidates':0,
             'independent_alternate_representative':alternate['alternate_q0'],
             'independent_alternate_choices':alternate['choice_count'],
             'independent_alternate_prunes':alternate['strict_prune_count'],
             'independent_alternate_sphere_leaves':0,
             'full_local_exact_decision_and_alternate_trace_sha256':hashlib.sha256(payload).hexdigest()},
            json.loads(payload))

def run():
    root,custody=verify_custody()
    portable=M.read_json(root/'research_artifacts/T6_P17_ORDER1_SUPPORT_20260923/portable_input.json',M.PORTABLE_SHA)
    problem=M.read_json(root/'research_artifacts/T6_P17_ORDER1_SUPPORT_20260923/order2_problem.json',M.PROBLEM_SHA)
    common=M.verify_common(portable)
    exact=M.verify_family_descriptors(problem)
    certificate=M.read_json(root/PREFIX/'BATCH_COMPACT_CERTIFICATE.json',SOURCE_COMPACT_SHA)
    M.check(certificate['task_id']==TASK and certificate['publication_id']==PUB,'actual scientific scope')
    M.check(certificate['schema']=='T6_P17_ORDER2_REMAINING271_COMPACT_CERTIFICATE_V1',
            'actual complete compact certificate schema')
    expected=[x for x in exact if x['id']!='q2-1']
    ids=[x['id'] for x in expected]
    ledgers=certificate['case_ledgers']
    M.check(len(ledgers)==271 and [c['pattern_id'] for c in ledgers]==ids
            and certificate['completed_pattern_ids']==ids,'271 exact disjoint exhaustive IDs/order')
    M.check(len({c['pattern_id'] for c in ledgers})==271,'no duplicated case')
    M.check(certificate['complete_traversal'] is True and certificate['resource_exhausted'] is False
            and certificate['outside_patterns_classified_not_skipped'] is True,
            'full complete literal classification not domain-only')
    M.check(certificate['global_T6_complete'] is False and certificate['p19_replayed'] is False
            and certificate['q2_1_replayed'] is False,'preserved global/no-repeat limits')
    M.check(min(common['norms'])>2*max(x['radius_squared'] for x in exact),
            'independently rederived structural upper-bound premise')
    rows=[]
    traces=[]
    for case,ledger in zip(expected,ledgers):
        result,trace=consume_case(case,ledger,common)
        rows.append(result)
        traces.append({'case_id':case['id'],'exact_proof_check':trace})
    nodes=sum(r['consumed_nodes'] for r in rows)
    edges=sum(r['consumed_twochild_choices'] for r in rows)
    prunes=sum(r['strict_prunes'] for r in rows)
    M.check(nodes==index(certificate['total_node_count']) and edges==index(certificate['total_edge_count']),
            'counts derived only after all saved proof consumption')
    M.check(certificate['classification_counts']=={'EMPTY':271,'LOCAL_KERNEL':0}
            and index(certificate['survivor_count'])==0,'actual aggregate outcomes')
    admissible=sum(r['maximal_p17_domain']=='ADMISSIBLE' for r in rows)
    outside=sum(r['maximal_p17_domain']=='OUTSIDE' for r in rows)
    M.check(admissible==153==index(certificate['prime17_admissible_count'])
            and outside==118==index(certificate['outside_domain_count']),
            'all new domain labels and literal outsider trees consumed')
    olddir=OLD_REVIEW_DIR
    oldcustody=M.read_json(olddir/'IMMUTABLE_Q2_1_COMPLETE_SOURCE_VERIFIED.json')
    M.check(oldcustody['all11_complete_verified'] is True
            and oldcustody['source_commit']=='c406e50f16d8e1d3ba359f3291299170d7940bad',
            'exact previously verified immutable q2-1 custody')
    for pin in oldcustody['rows']:
        raw=((OLD_SOURCE_ROOT/pin['path']) if OLD_SOURCE_ROOT else Path(pin['local_path'])).read_bytes()
        M.check(hashlib.sha256(raw).hexdigest()==pin['sha256']
                and hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==pin['git_blob_sha1'],
                'unchanged q2-1 Source bytes/hash/blob')
    old=M.read_json(olddir/'Q2_1_INDEPENDENT_SOURCE_MATHEMATICAL_REVIEW_RECEIPT.json',
                    '50de657e66fe3b05e2b53dd0ea0323a2bf24f49a24beacbde9da6228b577228a')
    M.check(old['source_commit']==oldcustody['source_commit'] and old['pattern_id']=='q2-1'
            and old['fully_consumed_nodes']==8 and old['fully_consumed_exact_choices']==16
            and old['sphere_leaves']==0 and old['completed_signed_budget_candidates']==0
            and old['independent_alternate_representative_full_sphere']['leaves']==[],
            'unchanged prior genuinely independent q2-1 check joined')
    prior=certificate['prior_q2_1']
    M.check(prior['source_commit']==oldcustody['source_commit']
            and prior['ledger_sha256']=='0cacbc773fc6f4bb995f36ad127aa07fd7cfa5bf6e79195a2b78db3549da016c'
            and prior['replayed'] is False and prior['counts_included_in_new_compute_totals'] is False,
            'actual unchanged old unit reference, not duplicated new compute')
    result={'schema':'T6_FULL272_SOURCE_PINNED_NONAUTHOR_EXACT_DRIVER_REVIEW_V1',
            'scientific_source_commit':SOURCE,'source_compact_sha256':SOURCE_COMPACT_SHA,
            'disposition':'FULL272_NECESSARY_AFFINE_SPHERES_INDEPENDENT_MATHEMATICAL_CHECK_PASS',
            'reviewer_id':'EM-DVR-4CF7AF','reviewer_session':'MCP-1449d85a8d3f47e68d770736b3d2a497',
            'new_cases':271,'new_consumed_nodes':nodes,'new_consumed_twochild_choices':edges,
            'new_exact_strict_norm_prunes':prunes,'new_admissible':admissible,'new_outside':outside,
            'full_cases':272,'full_nodes':nodes+8,'full_choices':edges+16,'full_prunes':prunes+9,
            'full_admissible':admissible+1,'full_outside':outside,
            'sphere_leaves':0,'completed_signed_budget_candidates':0,'resource_stops':0,
            'full_mixed_kernel_saturated':True,'all_271_original_targets_budgets_and_domain_rederived':True,
            'all_live_and_pruned_branches_independently_consumed':True,
            'all271_alternate_original_cosets_independently_exhausted':True,
            'producer_or_producer_consumer_code_imported_or_executed':False,
            'q2_1_scientific_run_repeated':False,'new_result_construction_authored':False,
            'nonblind_review':True,'actual_RR_or_native_DR_review_completed_by_this_script':False,
            'global_parent_complete':False,'native_mathematical_acceptance':False,
            'all8_required_source_outputs_byte_verified':True,
            'local_verbose_archive_claimed_Source_verified':False,
            'prior_q2_1_source':oldcustody['source_commit'],
            'prior_q2_1_review_receipt_sha256':'50de657e66fe3b05e2b53dd0ea0323a2bf24f49a24beacbde9da6228b577228a',
            'min_GS_squared':M.pair(min(common['norms'])),
            'strict_D_min_minus_twice_all_R_max':M.pair(min(common['norms'])-2*max(x['radius_squared'] for x in exact)),
            'case_checks':rows}
    trace_raw=(json.dumps({'schema':'T6_OWN_FULL271_EXACT_LOCAL_TRACE_V1','source_commit':SOURCE,
                           'case_exact_checks':traces},sort_keys=True,separators=(',',':'))+'\n').encode()
    (HERE/'FULL271_OWN_EXACT_DECISION_AND_ALTERNATE_TRACES_LOCAL.json').write_bytes(trace_raw)
    result['local_full_trace_bytes']=len(trace_raw)
    result['local_full_trace_sha256']=hashlib.sha256(trace_raw).hexdigest()
    (HERE/'FULL272_INDEPENDENT_SOURCE_MATHEMATICAL_REVIEW_RECEIPT.json').write_text(
        json.dumps(result,indent=2)+'\n')
    print(f'OWN_EXACT_SOURCE_PASS: new271 nodes={nodes}, choices={edges}, strictprunes={prunes}; '
          f'full272={nodes+8}/{edges+16}/{prunes+9}; all271 alternate spheres empty; RR/native pending')
    return result

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root',type=Path,default=SOURCE_ROOT,
                        help='exact Source953 files in repository-relative layout')
    parser.add_argument('--old-q2-review-dir',type=Path,default=OLD_REVIEW_DIR,
                        help='unchanged prior unit custody manifest and own receipt')
    parser.add_argument('--old-q2-source-root',type=Path,
                        help='optional exact Sourcec406 files in repository-relative layout')
    args=parser.parse_args()
    SOURCE_ROOT=args.source_root
    OLD_REVIEW_DIR=args.old_q2_review_dir
    OLD_SOURCE_ROOT=args.old_q2_source_root
    run()
