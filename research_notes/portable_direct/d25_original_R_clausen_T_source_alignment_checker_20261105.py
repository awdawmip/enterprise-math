#!/usr/bin/env python3
"""Frozen D25 tail R compared to Clausen T: uses existing independent p³ data; not native H0/B0."""
import json, pathlib
path=pathlib.Path(__file__).parent
data=json.loads((path/'d25_terminal_boundary_rank2_results_20261105.json').read_text())
failed=[]; anchors=[]
for z in data['details']:
    p,n=z['p'],z['n']
    assert p==6*n+1
    if z['C_p']!=pow(10,-1,p): failed.append((p,'C_p != 1/10'))
    # The original FROZEN coefficient c_r is not the later reflected r_r.
    # Its first term is 1/10; c_{r+1}/c_r = 36*r*r / ((6*r+5)*(3*r+2)).
    b=1; c=pow(10,-1,p); s=v=R=0
    for i in range(1,n+1):
        b=b*(6*i-5)*(3*i-2)*pow(36*i*i,-1,p)%p
        if i>1:
            r=i-1
            c=c*36*r*r*pow((6*r+5)*(3*r+2),-1,p)%p
        s=(s+c)%p;v=(v+i*c)%p
        R=(R+2*b*((6*i+1)*s-6*v))%p
    if R!=z['T_p']: failed.append((p,'R_frozen != T',R,z['T_p']))
    if z['target'] and R!=z['delta_mod_p']:
        failed.append((p,'finite Delta != R',z['delta_mod_p'],R))
    if p in (7,13,19,139,373,997):
        anchors.append({'p':p,'C_p':z['C_p'],'R_frozen':R,'T_p':z['T_p'],'Delta_p':z['delta_mod_p']})
result={'n':len(data['details']),'targets':sum(z['target'] for z in data['details']),
'failed':failed,'anchors':anchors,
'proof_scope':'source alignment all p=6n+1; target Delta-R relation all p=13,19 mod24',
'full_target_zero_all_prime_proven':False,'native_H0_B0':'NOT_RUN'}
print(json.dumps(result,indent=2));assert not failed
