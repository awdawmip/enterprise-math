#!/usr/bin/env python3
"""Finite Q_p vanishing pattern and conditional two-digit p^3 observer audit."""
import json
from d25_clausen_p3_boundary_checker_20261105 import primes, check

def audit(limit=997):
    rows=[]
    for p in primes(limit):
        v=check(p)
        target=p%24 in (13,19)
        Q=v['Q_mod_p3']; dQ=v['thetaQ_mod_p3']
        assert (Q%p==0)==target,(p,'vanishing classification')
        if target:
            a=(Q//p)%p; b=(Q//(p*p))%p
            d=dQ%p; e=(dQ//p)%p
            T=v['boundary_over_p2_mod_p']
            assert 12*a*d%p==1,(p,'first-digit observer')
            residual=((12*a*d-1)//p+a*a+12*a*e+12*b*d-T)%p
            assert residual==0,(p,'third-digit observer')
            if p in (13,19,139,373):
                rows.append({'p':p,'a':a,'b':b,'d':d,'e':e,
                    'T':T,'first':1,'second_residual':residual})
    return {'p_6n1_through_997':len(primes(limit)),
            'target_count':sum(p%24 in (13,19) for p in primes(limit)),
            'complement_count':sum(p%24 in (1,7) for p in primes(limit)),
            'target_Q_vanishing':'ALL IN FINITE RANGE',
            'complement_Q_nonvanishing':'ALL IN FINITE RANGE',
            'failures':0,'anchors':rows,
            'status':'FINITE OBSERVED; ALL-PRIME VANISHING CONJECTURAL; UNREVIEWED'}

if __name__=='__main__':
    print(json.dumps(audit(),indent=2))
