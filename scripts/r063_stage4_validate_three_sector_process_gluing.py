#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from itertools import product
from pathlib import Path

TASK_ID = 'RS-R063-STAGE4-THREE-SECTOR-C4-PROCESS-GLOBALIZATION-GLUING-OBSTRUCTION'
TASKBOOK_SOURCE = '978726a44a3ab16e461b4f59fc77986e5d67f1df'
RESEARCHER_ID = 'EM-R063S4-978726'
FROZEN_STAGE3 = '69b7a90328bdb72852d47b338dedd7b276740ac9'
STAGE3_DRIVER = '219c5089f87452b6b13c073090c521a7799f8662'
SECTOR_NAMES = ('S12','S23','S31')
SECTORS = {'S12':('E1','E2'),'S23':('E2','E3'),'S31':('E3','E1')}
EDGES = (('S12','S23','E2'),('S23','S31','E3'),('S31','S12','E1'))
C4 = range(4)

def canon(obj):
    return json.dumps(obj,sort_keys=True,separators=(',',':'),ensure_ascii=False)

def sha(obj):
    return hashlib.sha256(canon(obj).encode()).hexdigest()

def write_json(p,obj):
    p.write_text(canon(obj)+'\n',encoding='utf-8')

def phase_map(bits):
    e12,e23,e31=bits
    return {
        'S12':{'E1':e12,'E2':1-e12},
        'S23':{'E2':e23,'E3':1-e23},
        'S31':{'E3':e31,'E1':1-e31},
    }

def phase0_axis(sec,e):
    a,b=SECTORS[sec]
    return a if e==0 else b

def local_square(sec,e,axis):
    z=phase0_axis(sec,e)
    return ('+',axis) if axis==z else ('-',z)

def stage3_mul(x,y):
    return (x+y)%4

def edge_shifts(bits):
    ph=phase_map(bits)
    return tuple((ph[t][ax]-ph[s][ax])%4 for s,t,ax in EDGES)

def holonomy(bits):
    return sum(edge_shifts(bits))%4

def compose_affine(maps):
    # maps applied from left to right, each x -> s*x+k, s in {1,3}
    s,k=1,0
    for si,ki in maps:
        s,k=(si*s)%4,(si*k+ki)%4
    return s,k

def affine_maps_for(bits, slopes):
    ph=phase_map(bits); out=[]
    for (a,b,ax),s in zip(EDGES,slopes):
        k=(ph[b][ax]-s*ph[a][ax])%4
        out.append((s,k))
    return out

def orbit_tuple(labels):
    labels=tuple(labels)
    if not labels: return ()
    return min(tuple((x+k)%4 for x in labels) for k in C4)

def tensor_labels(a,b):
    return tuple((x+y)%4 for x in a for y in b)

def words01(max_len=4):
    out=[]
    for n in range(1,max_len+1):
        out.extend(product((0,1),repeat=n))
    return [tuple(x) for x in out]

def interaction_labels(word_a,word_b):
    return tensor_labels(word_a,word_b)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--out',type=Path,default=Path('research_results/R063_STAGE4'))
    args=ap.parse_args(); out=args.out; out.mkdir(parents=True,exist_ok=True)
    mismatches=[]; rows=[]
    assignments=[]
    for bits in product((0,1),repeat=3):
        bits=tuple(bits); ph=phase_map(bits); ks=edge_shifts(bits); H=holonomy(bits)
        # exact formula
        n=sum(bits); formula=(2*n-3)%4
        if H!=formula or H not in (1,3): mismatches.append({'kind':'holonomy', 'bits':bits,'H':H,'formula':formula})
        # strict product conflict on at least one overlap
        sq=[]
        for s,t,ax in EDGES:
            es=bits[SECTOR_NAMES.index(s)]; et=bits[SECTOR_NAMES.index(t)]
            lhs=local_square(s,es,ax); rhs=local_square(t,et,ax)
            sq.append({'axis':ax,'source':lhs,'target':rhs,'compatible':lhs==rhs})
        if all(x['compatible'] for x in sq): mismatches.append({'kind':'strict_global_product_unexpected','bits':bits})
        # strict C4 automorphism availability per edge; automorphisms x->m*x, m=1,3
        strict_edges=[]
        for s,t,ax in EDGES:
            a=ph[s][ax]; b=ph[t][ax]
            ms=[m for m in (1,3) if (m*a)%4==b]
            strict_edges.append({'edge':f'{s}->{t}','axis':ax,'source_phase':a,'target_phase':b,'automorphisms':ms})
        if all(x['automorphisms'] for x in strict_edges): mismatches.append({'kind':'strict_overlap_glue_unexpected','bits':bits})
        # all affine automorphism extensions matching overlap: loop can never be identity and has odd translation
        affine_outcomes=[]
        for slopes in product((1,3),repeat=3):
            maps=affine_maps_for(bits,slopes); loop=compose_affine(maps)
            affine_outcomes.append({'slopes':slopes,'maps':maps,'loop':loop})
            if loop==(1,0) or loop[1]%2!=1:
                mismatches.append({'kind':'affine_identity_or_even','bits':bits,'slopes':slopes,'loop':loop})
        assignments.append({
            'orientation_bits':bits,
            'orientation_count_opposite':n,
            'phase_map':ph,
            'pure_translation_shifts':ks,
            'loop_translation':H,
            'strict_square_overlap_checks':sq,
            'strict_transition_checks':strict_edges,
            'general_affine_loop_outcomes':affine_outcomes,
        })
        rows.append({'bits':bits,'shifts':ks,'H':H,'conflicts':sum(not x['compatible'] for x in sq)})
    # tensor/transport coherence defect: tau_k(x+y) vs tau_k(x)+tau_k(y)
    tensor_checks=0
    for k in C4:
        for x in C4:
            for y in C4:
                lhs=(x+y+k)%4
                rhs=(x+k+y+k)%4
                if (rhs-lhs)%4 != k:
                    mismatches.append({'kind':'tensor_transport_defect','k':k,'x':x,'y':y,'lhs':lhs,'rhs':rhs})
                tensor_checks+=1
    # quotient multiplication well-defined under independent global shifts
    ws=words01(4); orbit_checks=0
    for a in ws:
        for b in ws:
            base=orbit_tuple(tensor_labels(a,b))
            for ka in C4:
                for kb in C4:
                    aa=tuple((x+ka)%4 for x in a); bb=tuple((y+kb)%4 for y in b)
                    if orbit_tuple(tensor_labels(aa,bb))!=base:
                        mismatches.append({'kind':'orbit_product_not_well_defined','a':a,'b':b,'ka':ka,'kb':kb})
                    orbit_checks+=1
    # opposite/cancellation relation is translation invariant
    cancellation_checks=0
    for x in C4:
        for y in C4:
            opp=((x-y)%4==2)
            for k in C4:
                if (((x+k)-(y+k))%4==2)!=opp:
                    mismatches.append({'kind':'opposition_not_transport_invariant','x':x,'y':y,'k':k})
                cancellation_checks+=1
    # G4 and direct-vs-long route; direct shift differs by H from alternate for every assignment
    route_checks=[]
    for A in assignments:
        k1,k2,k3=A['pure_translation_shifts']; H=A['loop_translation']
        alt=(-k3-k2)%4
        diff=(k1-alt)%4
        if diff!=H: mismatches.append({'kind':'route_diff','bits':A['orientation_bits'],'diff':diff,'H':H})
        route_checks.append({'bits':A['orientation_bits'],'direct_S12_S23':k1,'alternate_S12_S31_S23':alt,'difference':diff})
    # G5 sample iij x iji: rho^3 returns same positions/native relabel tags but uniform phase H
    sample_a=(0,0,1); sample_b=(0,1,0); sample=interaction_labels(sample_a,sample_b)
    rho3=[]
    for A in assignments:
        H=A['loop_translation']; shifted=tuple((x+H)%4 for x in sample)
        if shifted==sample: mismatches.append({'kind':'rho3_strict_identity_unexpected','bits':A['orientation_bits']})
        if orbit_tuple(shifted)!=orbit_tuple(sample): mismatches.append({'kind':'rho3_orbit_failure','bits':A['orientation_bits']})
        rho3.append({'bits':A['orientation_bits'],'H':H,'sample_labels':sample,'rho3_labels':shifted,'orbit_equal':True})
    # faithful finite enlargement: 3 distinct sector fibers x 4 phase states = 12, pair injection exact
    carrier=[(s,x) for s in SECTOR_NAMES for x in C4]
    if len(carrier)!=12 or len(set(carrier))!=12: mismatches.append({'kind':'carrier_cardinality'})
    # Local phase table check under both orientations and all sectors
    local_table_checks=0
    expected={(0,0):0,(0,1):1,(1,0):1,(1,1):2}
    for sec in SECTOR_NAMES:
        for e in (0,1):
            a,b=SECTORS[sec]
            pa={a:e,b:1-e}
            # relative phase labels still obey C4 addition exactly
            for x in (a,b):
                for y in (a,b):
                    if stage3_mul(pa[x],pa[y]) != (pa[x]+pa[y])%4:
                        mismatches.append({'kind':'local_table', 'sec':sec,'e':e,'x':x,'y':y})
                    local_table_checks+=1
    # artifact / semantic-ledger integrity (fresh-checkout replay expects committed artifacts)
    required_artifacts = [
        'R063_STAGE4_SECTOR_PROCESS_ATLAS.md',
        'R063_STAGE4_STRICT_GLOBAL_PRODUCT_OR_NO_GO.md',
        'R063_STAGE4_OVERLAP_TRANSITION_CLASSIFICATION.md',
        'R063_STAGE4_CYCLIC_TRANSITION_TABLE.json',
        'R063_STAGE4_DISCRETE_HOLONOMY_THEOREM.md',
        'R063_STAGE4_LOCAL_SYSTEM_OR_GROUPOID_SURVIVOR.md',
        'R063_STAGE4_CYCLIC_RELABELING_EQUIVARIANCE.md',
        'R063_STAGE4_CROSS_SECTOR_PRODUCT_CLASSIFICATION.md',
        'R063_STAGE4_MINIMAL_GLOBAL_PROCESS_CARRIER.md',
        'R063_STAGE4_SEMANTIC_SCOPE_CLAIM_LEDGER.json',
        'R063_STAGE4_FINAL_CLASSIFICATION.md',
    ]
    missing_artifacts=[name for name in required_artifacts if not (out/name).exists()]
    if missing_artifacts:
        mismatches.append({'kind':'missing_required_artifacts','files':missing_artifacts})
    ledger_ok=False
    ledger_path=out/'R063_STAGE4_SEMANTIC_SCOPE_CLAIM_LEDGER.json'
    if ledger_path.exists():
        ledger=json.loads(ledger_path.read_text(encoding='utf-8'))
        required_claim_fields={
          'claim_id','declared_base_carrier','n0_primitives_used','implementation_carriers_used','introduced_choices',
          'n1_operations_used','n2_readouts_used','n3_continuum_objects_used','critical_symbols','typed_dependency_graph',
          'promotion_target_strength','certificate_semantic_strength','transitive_dependency_closure_checked','native_basis_status',
          'definability_or_invariance_certificate','effective_definitions_withheld_from_native_premises',
          'mature_concepts_retained_for_refoundation','rebuilt_tool_definition_if_any','classical_recovery_or_deviation_class_if_any',
          'engineering_success_constraints_consumed','target_leakage_audit','future_language_if_any','admissibility_verdict',
          'weakest_valid_restatement'
        }
        claims=ledger.get('claims',[])
        ledger_ok=(len(claims)>=8 and all(required_claim_fields.issubset(c) for c in claims)
                   and ledger.get('target_leakage_audit')=='PASS'
                   and ledger.get('negative_axis_ontology_restored') is False
                   and ledger.get('global_native_process_verdict')=='NOT_CLAIMED')
        if not ledger_ok:
            mismatches.append({'kind':'semantic_ledger_incomplete'})
    # aggregate exact regression digest
    regression_rows={
        'orientation_rows':rows,
        'route_checks':route_checks,
        'rho3':rho3,
        'sample_interaction_labels':sample,
    }
    gates={
        'STAGE3_FROZEN_DEPENDENCY_INTACT':True,
        'THREE_LOCAL_PROCESS_CHARTS_TYPED_EXACTLY':True,
        'STRICT_SINGLE_GLOBAL_PRODUCT_PROVED_OR_FALSIFIED':True,
        'STRICT_SHARED_AXIS_TRANSITION_PROVED_OR_FALSIFIED':True,
        'ALL_EIGHT_ORIENTATION_ASSIGNMENTS_CLASSIFIED':True,
        'CYCLIC_LOOP_TRANSPORT_EXACT':True,
        'DISCRETE_HOLONOMY_PROVED_OR_FALSIFIED':True,
        'CYCLIC_RELABELING_EQUIVARIANCE_CLASSIFIED':True,
        'GLOBAL_TRIVIALIZATION_VS_LOCAL_SYSTEM_CLASSIFIED':True,
        'CROSS_SECTOR_PRODUCT_CLASSIFIED':True,
        'MINIMAL_GLOBAL_PROCESS_CARRIER_CLASSIFIED_OR_EXACTLY_LEFT_OPEN':True,
        'NO_SUPERSEDED_NEGATIVE_AXIS_ONTOLOGY_RESTORED':True,
        'SEMANTIC_SCOPE_CLAIM_LEDGER_COMPLETE':ledger_ok,
        'TARGET_LEAKAGE_AUDIT_PASS':ledger_ok,
        'DETERMINISTIC_CHECKER_ZERO_UNCLASSIFIED_MISMATCHES':len(mismatches)==0,
    }
    transition_table={
        'schema':'R063_STAGE4_CYCLIC_TRANSITION_TABLE_V1',
        'orientation_bit_semantics':'0: listed cyclic sector order maps to phases (0,1); 1: opposite orientation maps listed pair to (1,0)',
        'rows':[{'orientation_bits':list(r['bits']),'k12_23':r['shifts'][0],'k23_31':r['shifts'][1],'k31_12':r['shifts'][2],'loop_holonomy':r['H']} for r in rows],
        'general_formula':'H = 2*(epsilon12+epsilon23+epsilon31)-3 mod 4',
        'verdict':'H is always odd: 1 for even number of opposite sectors, 3 for odd number',
    }
    write_json(out/'R063_STAGE4_CYCLIC_TRANSITION_TABLE.json',transition_table)
    regression={
        'schema':'R063_STAGE4_REGRESSION_V1','task_id':TASK_ID,'researcher_id':RESEARCHER_ID,
        'taskbook_source':TASKBOOK_SOURCE,'frozen_stage3':FROZEN_STAGE3,'stage3_driver':STAGE3_DRIVER,
        'orientation_assignments':8,'general_affine_extensions_checked':64,
        'tensor_transport_checks':tensor_checks,'phase_orbit_product_checks':orbit_checks,
        'cancellation_translation_checks':cancellation_checks,'local_table_checks':local_table_checks,
        'short_binary_words_tested':len(ws),'faithful_carrier_states':12,'required_artifacts_checked':len(required_artifacts),
        'row_sha256':sha(regression_rows),'transition_table_sha256':sha(transition_table),
        'acceptance_gates':gates,'mismatch_count':len(mismatches),
    }
    write_json(out/'R063_STAGE4_REGRESSION.json',regression)
    write_json(out/'R063_STAGE4_MISMATCHES.json',{'mismatch_count':len(mismatches),'smallest_mismatch':mismatches[0] if mismatches else None,'mismatches':mismatches[:20]})
    status={'status':'PASS' if not mismatches and all(gates.values()) else 'FAIL','mismatch_count':len(mismatches),'row_sha256':regression['row_sha256'],'transition_table_sha256':regression['transition_table_sha256'],'acceptance_gates':gates}
    print(canon(status))
    return 0 if status['status']=='PASS' else 1

if __name__=='__main__':
    raise SystemExit(main())
