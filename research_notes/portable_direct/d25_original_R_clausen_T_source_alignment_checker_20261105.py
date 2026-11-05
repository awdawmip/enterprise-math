#!/usr/bin/env python3
"""Frozen R vs signed Clausen T. Import adjacent D25 terminal checker; no saved JSON required."""
try:
    from d25_terminal_boundary_rank2_checker_20261105 import check as prior_case, primes
except ImportError:  # Full local evidence checker used these earlier names.
    from d25_terminal_boundary_rank2_checker_20261105 import audit as prior_case, primes_upto as primes
import json

failed=[]; anchors=[]
for p in primes(10000):
    z=prior_case(p,p<=250)
    n=(p-1)//6
    c_terminal=z['C_p']; terminal=z['T_p']
    delta=z.get('delta',z.get('delta_mod_p'))
    if c_terminal!=pow(10,-1,p): failed.append((p,'terminal unit != 1/10'))
    # Independently iterate the source-original C_r and B_i.
    b=1; c=pow(10,-1,p); S=V=original_R=0
    for i in range(1,n+1):
        b=b*(6*i-5)*(3*i-2)*pow(36*i*i,-1,p)%p
        if i>1:
            r=i-1
            c=c*36*r*r*pow((6*r+5)*(3*r+2),-1,p)%p
        S=(S+c)%p; V=(V+i*c)%p
        original_R=(original_R+2*b*((6*i+1)*S-6*V))%p
    if original_R!=terminal: failed.append((p,'source-original R != terminal T',original_R,terminal))
    if p%24 in (13,19) and original_R!=delta:
        failed.append((p,'finite target Delta != R',delta,original_R))
    if p in (7,13,19,139,373,997):
        anchors.append({'p':p,'C_p':c_terminal,'R_frozen':original_R,'T_p':terminal,'Delta_p':delta})
result={
    'primes_checked':len(primes(10000)),
    'target_primes_checked':sum(p%24 in (13,19) for p in primes(10000)),
    'failures':failed, 'anchors':anchors,
    'scope':'Source-typed R=T and universal C=1/10; full LIFT only finite test',
    'native_H0_B0':'NOT_RUN'
}
print(json.dumps(result,indent=2))
assert not failed
