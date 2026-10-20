#!/usr/bin/env python3
from __future__ import annotations
import json, itertools, re
from pathlib import Path
HERE=Path(__file__).resolve().parent
EXPECTED_CIDS=[
'R047P-M1-CUT-XOR','R047P-M2-RELATIONAL-REFINEMENT','R047P-M3-CONTACT-PARITY-PROPAGATOR','R047P-M4-BRANCH-RECOALESCE','R047P-M5-AUTOMORPHISM-ORBIT-COLLAPSE','R047P-M6-INCIDENCE-BALANCE-FLOW',
'R047I-C01','R047I-C02','R047I-C03','R047I-C04','R047I-C05','R047I-C06']
KENGS=['KENG-01_GEOMETRIC_MEASURE_COHERENCE','KENG-02_CYCLE_CLOSURE_AND_RELATIVE_PHASE','KENG-03_DIFFUSIVE_RELAXATION','KENG-04_BOUNDED_MODE_SPECTRUM']
BR={'B0_NATIVE_DIRECT','B1_UNIFORM_READOUT','B2_CALIBRATED_PARAMETER_BRIDGE','B3_TARGET_SPECIFIC_ADAPTER','B4_ILLEGAL_LEAKAGE'}
EV={'E0_UNMAPPED','E1_QUALITATIVE_MECHANISM','E2_EXACT_STRUCTURAL_CONSTRAINT','E3_QUANTITATIVE_IN_SAMPLE','E4_QUANTITATIVE_HOLDOUT','E5_CROSS_KENG_SHARED_EXPLANATION'}
def load(n): return json.loads((HERE/n).read_text(encoding='utf-8'))

def validate_artifacts():
    F=load('R047C_FREEZE_INTEGRITY.json'); M=load('R047C_CALIBRATION_MATRIX.json'); P=load('R047C_PARAMETER_DEBT.json'); H=load('R047C_HOLDOUT_LEDGER.json'); L=load('R047C_TARGET_LEAKAGE_AUDIT.json'); D=load('R047C_EXPLANATORY_DEBT_VECTORS.json'); Q=load('R047C_PARETO_FRONTIER.json'); X=load('R047C_CROSS_ARM_REPLICATION_MATRIX.json')
    assert F['verdict']=='PASS_NO_MISMATCH'
    assert F['project_arm']['observed_head']=='deff14d75ef93815d6a8dcb8aa79039e68aa390a'
    assert F['project_arm']['recomputed_candidate_set_sha256']=='bf309a1b6d0bebf10a58345af768bac0b63747934eccb63538d0e0fe6cf0d494'
    assert F['isolated_arm']['accepted_bundle_sha256']=='d85f3687c3cef311712ac18718cf41d51b6bee21db6efadea9576d971a2e4d96'
    assert F['isolated_arm']['accepted_candidate_set_sha256']=='220e7f72ba9c4cbffc8fcd98b6b7df9b952bbccaaa0b4415cb36f47ea4b0eb3f'
    assert F['calibration_target']['observed_git_blob']=='bc24a121897a912f026b0c85af914268f00997e5'
    assert all(v==0 for k,v in F['candidate_core_immutability'].items() if k.endswith('edits') or k.endswith('rewrites'))
    cells=M['cells']; assert len(cells)==48==M['cell_count']
    cid_by_alias={a:v['id'] for a,v in M['candidate_registry'].items()}; kid_by_alias={a:v['id'] for a,v in M['protocol_registry'].items()}
    pairs={(cid_by_alias[c['c']],kid_by_alias[c['k']]) for c in cells}; assert pairs==set(itertools.product(EXPECTED_CIDS,KENGS))
    for c in cells:
        assert c['b'] in BR and c['e'] in EV
        assert c['e'] not in {'E3_QUANTITATIVE_IN_SAMPLE','E4_QUANTITATIVE_HOLDOUT','E5_CROSS_KENG_SHARED_EXPLANATION'}
        assert c['b']!='B4_ILLEGAL_LEAKAGE'
        assert c['c'] in M['candidate_registry'] and c['k'] in M['protocol_registry']
        aliases={n.split(':',1)[0] for n in c['bridge']}
        types={M['typed_node_registry'][a] for a in aliases}
        assert 'N0_DEFINABLE_FROM_FROZEN_CORE' in types and 'FROZEN_N1_STATE_OR_OPERATION' in types and 'PROTOCOL_MAPPING' in types
        assert any(a in aliases for a in ('RO','TA'))
    ga=M['global_assertions']; assert not any(ga.values())
    assert P['fitted_parameter_count_total']==0 and P['new_core_parameter_count']==0 and P['target_specific_core_patch_count']==0
    assert H['e4_pass_count']==0 and len(H['protocol_splits'])==4
    splits=list(H['protocol_splits'].values())
    assert len(splits)==4
    for h in splits:
        assert h['construction'] and h['holdout'] and h['independence_rule']
    assert H['candidate_constraint_holdout_cells']==48 and len(H['candidate_results'])==12
    a=L['classical_pi_numeric_selection_audit']
    assert a['selection_loss_kind']=='NONE' and a['classical_pi_numeric_value_used_as_selection_loss'] is False and a['classical_pi_decimal_or_approximation_compared_to_candidate_output'] is False and a['machine_auditable_answer']=='YES_NOT_USED'
    assert L['live_bridge_imports']['illegal_effective_definition_import_count']==0
    assert len(D['vectors'])==12 and all(v['keng_E4_coverage']==0 and v['fitted_parameter_count']==0 and v['illegal_import_count']==0 for v in D['vectors'])
    assert Q['strict_dominance_pairs']==[] and Q['strict_winner'] is None and Q['winner_selected'] is False and set(Q['pareto_frontier_declared_axes'])==set(EXPECTED_CIDS)
    assert X['analysis_started_after_all_48_cells'] is True
    sel=json.dumps({'pareto':Q,'selection':a},ensure_ascii=False)
    assert not re.search(r'3\.14\d*',sel)
    return True

def xor(a,b): return tuple(x^y for x,y in zip(a,b))
def rpe_step(edges,p,q,n):
    aq=[0]*n
    for u,v in edges:
        aq[v]^=q[u]
        if (v,u) in edges: pass
    return q, tuple(p[i]^aq[i] for i in range(n))
def rpe_inv(edges,q,r,n):
    aq=[0]*n
    for u,v in edges: aq[v]^=q[u]
    return tuple(r[i]^aq[i] for i in range(n)), q

def check_rpe():
    for n in range(1,4):
      und=[(i,j) for i in range(n) for j in range(i+1,n)]
      for mask in range(1<<len(und)):
        e=[]
        for k,(u,v) in enumerate(und):
          if mask>>k & 1: e += [(u,v),(v,u)]
        for bits in itertools.product((0,1),repeat=2*n):
          p=bits[:n]; q=bits[n:]
          q1,r=rpe_step(e,p,q,n)
          assert rpe_inv(e,q1,r,n)==(p,q)
          seen=set(); z=(p,q)
          for _ in range(1<<(2*n)):
            assert z not in seen
            seen.add(z); z=rpe_step(e,*z,n)
            if z==(p,q): break
          else: raise AssertionError('RPE did not close from initial state')
    return True

def base_or(edges,x,n):
    y=[0]*n
    for u,v in edges:
        y[v] |= x[u]
    return tuple(y)
def csr_build(edges,n,s):
    nodes=[('v',i) for i in range(n)]
    relay=[]; redges=[]
    for ei,(u,v) in enumerate(edges):
        chain=[('v',u)]+[('e',ei,j) for j in range(1,s)]+[('v',v)]
        for z in chain[1:-1]: relay.append(z)
        for a,b in zip(chain,chain[1:]): redges.append((a,b))
    nodes+=relay
    return nodes,redges
def csr_step(nodes,redges,y):
    z={n:0 for n in nodes}
    for a,b in redges: z[b]|=y[a]
    return z
def check_csr():
    graphsets=[(2,[(0,1)]),(3,[(0,1),(1,2)]),(3,[(0,1),(0,2),(2,1)]),(3,[(0,1),(1,0)])]
    for n,e in graphsets:
      for s in (1,2,3):
       nodes,re=csr_build(e,n,s)
       for x in itertools.product((0,1),repeat=n):
        y={z:0 for z in nodes}
        for i,b in enumerate(x): y[('v',i)]=b
        for _ in range(s): y=csr_step(nodes,re,y)
        bx=base_or(e,x,n)
        assert tuple(y[('v',i)] for i in range(n))==bx
        assert all(y[z]==0 for z in nodes if z[0]=='e')
        for _ in range(s): y=csr_step(nodes,re,y)
        assert tuple(y[('v',i)] for i in range(n))==base_or(e,bx,n)
    return True

def check_balance_conservation():
    graphs=[(2,[(0,1)]),(3,[(0,1),(1,2)]),(3,[(0,1),(0,2),(1,2)])]
    for n,E in graphs:
      deg=[0]*n; adj=[[] for _ in range(n)]
      for u,v in E: deg[u]+=1;deg[v]+=1;adj[u].append(v);adj[v].append(u)
      for q in itertools.product(range(4),repeat=n):
       for v in range(n):
        if deg[v] and q[v]>=deg[v]:
          z=list(q); z[v]-=deg[v]
          for u in adj[v]: z[u]+=1
          assert sum(z)==sum(q)
    return True

def run_all():
    checks={'artifact_integrity':validate_artifacts(),'RPE_reversibility_and_pure_periodicity':check_rpe(),'CSR_micro_macro_composition':check_csr(),'incidence_balance_conservation':check_balance_conservation()}
    print(json.dumps({'status':'PASS','checks':checks,'count':len(checks)},indent=2))
    return checks
if __name__=='__main__': run_all()
