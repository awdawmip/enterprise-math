#!/usr/bin/env python3
import json, hashlib, math, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[1]
FROZEN_PARENT='87230fd13c5a008e559f3d168b96fc5fe1948b2a'
checks=[]
def ck(name,cond,detail=''):
    checks.append((name,bool(cond),str(detail)))
    if not cond: raise AssertionError(f'{name}: {detail}')
def load(name): return json.loads((ROOT/name).read_text(encoding='utf-8'))
# NATIVE_GENERATOR_BEGIN
def native_generate(n):
    side={(s,r) for s in ('OU','OV','UV') for r in range(1,n+1)}
    plus={(i,j) for i in range(n) for j in range(n-i)}
    minus={(i,j) for i in range(max(0,n-1)) for j in range(n-1-i)} if n>=2 else set()
    rooted={(i,j) for i,j in plus if i==0 or j==0}
    closing={(i,j) for i,j in plus if i+j==n-1} if n else set()
    return {'area':len(side),'root_full':len(plus),'root_two_ray':len(rooted),'all_cycles':len(plus)+len(minus),'closing':len(closing)}
# NATIVE_GENERATOR_END
def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0: p.pop()
    return p
def shift(p,h):
    out=[0]*len(p)
    for j,a in enumerate(p):
        for k in range(j+1): out[k]+=a*math.comb(j,k)*(h**(j-k))
    return trim(out)
def sub(a,b):
    m=max(len(a),len(b)); return trim([(a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0) for i in range(m)])
def val(p,n): return sum(a*n**i for i,a in enumerate(p))
enum=load('R059D_STAGE_AC_ENUMERATION_N1_NMAX.json')
area=load('R059D_STAGE_AC_AREA_LAW_PROOF.json')
root=load('R059D_STAGE_AC_ROOT_LAW_PROOF.json')
inv=load('R059D_STAGE_AC_SQUARE_ROOT_INVERSION_PROOF.json')
bridge=load('R059D_STAGE_AC_PRIOR_STAGE_BRIDGE_LEDGER.json')
sem=load('R059D_STAGE_AC_NATIVE_SEMANTICS_CLAIM_LEDGER.json')
col={x:i for i,x in enumerate(enum['columns'])}
def dec(v): return {x:v[i] for x,i in col.items()}
rows={0:dec(enum['degenerate_n0'])}; rows.update({v[col['n']]:dec(v) for v in enum['rows']})
for n in range(enum['n_max']+1):
    g=native_generate(n); r=rows[n]
    ck(f'area_replay_{n}',g['area']==r['A'])
    ck(f'full_replay_{n}',g['root_full']==r['R_full'])
    ck(f'two_ray_replay_{n}',g['root_two_ray']==r['R_two_ray'])
    ck(f'all_cycle_replay_{n}',g['all_cycles']==r['C_all3'])
    ck(f'closing_replay_{n}',g['closing']==r['C_close'])
ck('control_area_n1',native_generate(1)['area']==3); ck('control_area_n2',native_generate(2)['area']==6)
ck('control_root_full_n1',native_generate(1)['root_full']==1); ck('control_root_full_n2',native_generate(2)['root_full']==3)
ck('control_root_two_ray_n1',native_generate(1)['root_two_ray']==1); ck('control_root_two_ray_n2',native_generate(2)['root_two_ray']==3)
ck('negative_allcycles_n2',native_generate(2)['all_cycles']!=3); ck('negative_closing_n2',native_generate(2)['closing']!=3)
ck('n3_area',native_generate(3)['area']==9); ck('n3_full',native_generate(3)['root_full']==6)
ck('n3_two_ray',native_generate(3)['root_two_ray']==5); ck('n3_divergence',native_generate(3)['root_full']!=native_generate(3)['root_two_ray'])
A=area['symbolic_certificate']['closed_form_polynomial_coefficients_low_to_high']; Ai=area['symbolic_certificate']['recurrence_increment_polynomial_coefficients_low_to_high']
ck('area_symbolic_recurrence',sub(A,shift(A,-1))==trim(Ai)); ck('area_symbolic_base',val(A,0)==area['symbolic_certificate']['base']['value'])
D=root['full_T1_branch']['symbolic_certificate']['doubled_closed_form_polynomial_coefficients_low_to_high']; Di=root['full_T1_branch']['symbolic_certificate']['doubled_recurrence_increment_polynomial_coefficients_low_to_high']
ck('full_root_symbolic_recurrence',sub(D,shift(D,-1))==trim(Di)); ck('full_root_symbolic_base',val(D,0)==root['full_T1_branch']['symbolic_certificate']['base']['doubled_value'])
Q=root['rooted_two_ray_branch']['symbolic_certificate']['closed_form_polynomial_coefficients_low_to_high_for_n_ge_1']
ck('two_ray_symbolic_recurrence',sub(Q,shift(Q,-1))==[2]); ck('two_ray_symbolic_base',val(Q,1)==1)
ck('root_status_underdetermined',root['ROOT_LAW_STATUS']=='UNDERDETERMINED_NATIVE_EXTENSION')
ck('triangular_not_unique',root['primary_freezes']['TRIANGULAR_ROOT_LAW_UNIQUELY_SELECTED'] is False)
ck('two_exact_inverse_branches',inv['INVERSION_STATUS']=='UNDERDETERMINED_BETWEEN_TWO_EXACT_NATIVE_READOUT_BRANCHES')
ck('both_branches_controls',inv['shared_frozen_controls']['both_branches_satisfy_all_four'] is True)
ck('zero_branch_independent',inv['zero_extension']['area_zero']==inv['zero_extension']['full_root_zero']==inv['zero_extension']['two_ray_root_zero']==0)
ck('bridge_not_promoted',bridge['PRIOR_R059D_BRIDGE_STATUS']=='DIAGNOSTIC_COMPATIBILITY_ONLY__EXACT_SELECTION_BRIDGE_OPEN')
ck('unique_native_claim_unresolved',any(c['claim_id']=='AC-ROOT-UNIQUE-LAW' and c['admissibility_verdict']=='UNRESOLVED' for c in sem['claims']))
src=Path(__file__).read_text(encoding='utf-8'); gen=src.split('# NATIVE_GENERATOR_BEGIN',1)[1].split('# NATIVE_GENERATOR_END',1)[0]
for token in ['3*n','3 * n','n*(n+1)','n * (n + 1)','sqrt(','math.sqrt','**0.5','** 0.5']: ck(f'generator_forbids_{token}',token not in gen)
history='LOCAL_GIT_UNAVAILABLE_REQUIRES_EXTERNAL_CHECKPOINT_COMPARE'
if (REPO/'.git').exists():
    cp=subprocess.run(['git','-C',str(REPO),'diff','--name-status',f'{FROZEN_PARENT}..HEAD'],capture_output=True,text=True,check=True)
    bad=[x for x in cp.stdout.splitlines() if x and x.split('\t')[-1].startswith('research_results/R059D_STAGE_') and not x.split('\t')[-1].startswith('research_results/R059D_STAGE_AC/')]
    ck('historical_r059d_result_mutated',not bad,bad); history='PASS_GIT_DIFF'
payload='\n'.join(f'{n}:{int(ok)}:{d}' for n,ok,d in checks).encode(); digest=hashlib.sha256(payload).hexdigest()
print(json.dumps({'schema':'R059D_STAGE_AC_DETERMINISTIC_CHECKER_OUTPUT_V1','status':'PASS','checks_total':len(checks),'checks_passed':sum(ok for _,ok,_ in checks),'checks_failed':sum(not ok for _,ok,_ in checks),'checks_digest_sha256':digest,'history_gate':history,'primary_disposition':'N1_N2_CONTROLS_UNDERDETERMINE_NATIVE_EXTENSION','summary':'Exact native set-generation replay passes through n=256; area incidence law has an independent recurrence proof; two control-compatible root primitives diverge at n=3, so the triangular branch is not uniquely selected; inversion is branch-dependent; target-leakage generator scan passes.'},sort_keys=True))
