#!/usr/bin/env python3
"""Exact modular audit for branch-neutral D25 Clausen unit certificate.
Requires previously published d25_clausen_p3_boundary_checker_20261105.py.
Author-side experiment; NOT a native H0/B0 experiment.
"""
import json
from d25_clausen_p3_boundary_checker_20261105 import check, primes

def audit(limit=997):
    branch={"Q_DIVISIBLE":0,"WEIGHTED_FACTOR_DIVISIBLE":0}
    anchors=[]
    for p in primes(limit):
        m2=p*p; m3=m2*p; n=(p-1)//6
        old=check(p)
        Q=old["Q_mod_p3"]; D=old["theta_Q_mod_p3"]
        T=old["tail_over_p2_mod_p"]
        C=(Q+12*D)%m3
        # Independently checked original full W and signed boundary.
        assert old["W_mod_p3"]%m2==p
        assert Q*C%m2==p
        if Q%p==0:
            assert C%p!=0 and (Q//p)%p
            X,Y=Q,C; which="Q_DIVISIBLE"
        else:
            assert C%p==0 and Q%p and (C//p)%p
            X,Y=C,Q; which="WEIGHTED_FACTOR_DIVISIBLE"
        branch[which]+=1
        assert (X//p)%m2 == (pow(Y,-1,m2)*(1+p*T))%m2
        assert old["W_mod_p3"]==p
        # The terminating hypergeometric polynomial solves the Gauss ODE.
        q=[1]
        for k in range(1,n+1):
            q.append(q[-1]*(6*k-5)*(3*k-2)*pow(18*k*k,-1,p)%p)
        for k in range(n+2):
            c=(k*k*q[k]) if k<=n else 0
            if k:
                j=k-1
                c-=(6*j+1)*(3*j+1)*pow(18,-1,p)*q[j]
            assert c%p==0,(p,k,"Gauss ODE")
        if p%24 in (13,19):
            assert which=="Q_DIVISIBLE" # finite-class observation
            H=pow(12*D,-1,m2); A=(Q//p)%m2
            assert D%p and A%p
            assert A == (H+p*H*(T-H*H))%m2
            if p in (13,19,139,373):
                anchors.append([p,A,H,T])
        else:
            assert which=="WEIGHTED_FACTOR_DIVISIBLE" # finite only
    return {"schema":"D25_BRANCH_NEUTRAL_CLAUSEN_EXACT_AUDIT_V1",
            "range":"primes p=1 mod6, 7<=p<=997",
            "count":len(primes(limit)),"branch_counts":branch,
            "failures":0,"anchors":anchors,
            "scope":"finite exact original-binomial checks; native H0B0 NOT_RUN"}

if __name__=="__main__":
    print(json.dumps(audit(),indent=2))
