#!/usr/bin/env python3
import hashlib,importlib.util,json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
checks=[]
def ck(name,cond,detail=''):
    checks.append((name,bool(cond),str(detail)))
    if not cond: raise AssertionError(f'{name}: {detail}')

spec=importlib.util.spec_from_file_location('gen',ROOT/'r059d_stage_ah_generator.py')
gen=importlib.util.module_from_spec(spec);spec.loader.exec_module(gen)

def L(a,b): return 3*(a*a+a*b+b*b)-3*a+1

def reference_word(r):
    if r==0:return ''
    a,b=r,0;half=[]
    while a-b>1:
        if L(a,b+1)<=3*r*r:
            half.append('1');b+=1
        else:
            half.append('2');a-=1;b+=1
    center='2' if a-b==1 else ''
    return ''.join(half)+center+''.join({'1':'3','2':'2','3':'1'}[c] for c in reversed(half))

def J_ag(r):
    j=0
    for R in range(1,r+1):
        x=3*j+2
        if x*x+6*R*x-3*R*R<=0:j+=1
    return j

def anti(w): return w==''.join({'1':'3','2':'2','3':'1'}[c] for c in reversed(w))

def invariant_trace(r):
    if r==0:return True
    a,b=r,0;rho=-4
    while a-b>1:
        ck(f'rho_invariant_{r}_{a}_{b}',rho==3*r*r-L(a,b+1),(rho,3*r*r-L(a,b+1)))
        if rho>=0:
            ao,bo=a,b
            rho-=3*(ao+2*bo+3);b+=1
        else:
            ao,bo=a,b
            rho+=3*(ao-bo-3);a-=1;b+=1
    return True

# Metadata/theorem typing.
for fn in ['R059D_STAGE_AH_PROTOCOL.json','R059D_STAGE_AH_AUTONOMOUS_GENERATOR.json','R059D_STAGE_AH_WORD_GROWTH_THEOREM.json','R059D_STAGE_AH_COUNT_READOUT_THEOREM.json','R059D_STAGE_AH_TARGET_LEAKAGE_AUDIT.json']:
    ck(f'exists_{fn}',(ROOT/fn).exists())
proto=json.loads((ROOT/'R059D_STAGE_AH_PROTOCOL.json').read_text())
thm=json.loads((ROOT/'R059D_STAGE_AH_WORD_GROWTH_THEOREM.json').read_text())
leak=json.loads((ROOT/'R059D_STAGE_AH_TARGET_LEAKAGE_AUDIT.json').read_text())
ck('frozen_AG_head',proto['accepted_ag_owner_head']=='5063495ff0df643890cd1f4c72ffd2077161c13d')
ck('theorem_proved',thm['status']=='PROVED' and thm['theorem']=='FULL_N_MOTZKIN_WORD_FORWARD_GENERATOR_PROVED')
ck('leakage_pass',leak['status']=='PASS' and leak['generator_is_forward_autonomous'] is True)

# Source firewall scan.
src=(ROOT/'r059d_stage_ah_generator.py').read_text().lower()
for token in ['sqrt','sin(','cos(','tan(','occupancy','source_q','jump_table','word_table']:
    ck('source_forbidden_'+token,token not in src)

# Exact all-radius finite implementation replay through mandatory holdout ceiling.
for r in range(0,4097):
    w=gen.generate_word(r);ref=reference_word(r)
    ck(f'word_{r}',w==ref)
    ck(f'anti_{r}',anti(w))
    out=gen.readouts(r,w)
    j=J_ag(r)
    ck(f'J_{r}',out['J']==j,(out['J'],j))
    ck(f'len_{r}',len(w)==r+j)
    ck(f'C_{r}',out['C']==6*len(w))
    ck(f'D_{r}',out['D']==2*r+1)
    ck(f'Vmod6_{r}',(out['V']-(1+3*r*(r+1)))%6==0)
    if r<=512: invariant_trace(r)

# D6 closure/locality on deterministic discriminators.
DIR={(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)}
for r in [1,2,3,4,5,11,15,64,128,256,512,1024,4096]:
    out=gen.generate_enterprise_circle_N(r);fb=out['full_boundary']
    ck(f'd6_closed_{r}',fb[0]==fb[-1])
    ck(f'd6_edges_{r}',len(fb)-1==out['C'],(len(fb)-1,out['C']))
    ck(f'd6_unique_{r}',len(set(fb[:-1]))==len(fb)-1)
    for u,v in zip(fb,fb[1:]):
        ck(f'd6_local_{r}_{u}_{v}',(v[0]-u[0],v[1]-u[1]) in DIR)

# Extended checkpoints beyond holdout.
for r in [8192,16384]:
    w=gen.generate_word(r);ref=reference_word(r);out=gen.readouts(r,w)
    ck(f'extended_word_{r}',w==ref)
    ck(f'extended_J_{r}',out['J']==J_ag(r))

payload='\n'.join(f'{n}:{int(ok)}:{d}' for n,ok,d in checks).encode()
out={
 'schema':'R059D_STAGE_AH_DETERMINISTIC_CHECKER_OUTPUT_V1',
 'status':'PASS',
 'checks_total':len(checks),
 'checks_passed':sum(ok for _,ok,_ in checks),
 'checks_failed':sum(not ok for _,ok,_ in checks),
 'checks_digest_sha256':hashlib.sha256(payload).hexdigest(),
 'history_gate':'PENDING_EXTERNAL_GITHUB_COMPARE',
 'validation':'exact word/readout replay r=0..4096; residual invariant r=1..512; D6 discriminators; extended 8192/16384'
}
print(json.dumps(out,sort_keys=True))
