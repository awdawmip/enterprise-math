#!/usr/bin/env python3
"""GH-123: exact marked Hasse first-jet connection under 2-torsion re-origin."""
from d25_gh121_marked_cm_fiber_exact import (
    p, P, T, b, rows, C, add, sub, neg, mul, div, power, evaluate
)

PD = [j * coef % p for j,coef in enumerate(P)][1:]
H0, J0 = evaluate(P,T), evaluate(PD,T)
assert (H0,J0) == ((783,0),(0,1424))

observed=[]
for k,(alpha,c2,lam,Tp,zp,Rp) in enumerate(rows):
    # alpha²+alpha+(1+T)/8=0, differentiated with respect to T.
    alpha_dot=neg(div(C(1),mul(C(8),add(mul(C(2),alpha),C(1)))))
    c_dot=mul(C(3),alpha_dot)
    dlog_lambda=div(c_dot,mul(C(2),c2))
    numerator=add(add(mul(C(3),power(alpha,2)),mul(C(2),alpha)),b)
    numerator_dot=add(mul(add(mul(C(6),alpha),C(2)),alpha_dot),div(C(1),C(8)))
    beta_dot=sub(div(numerator_dot,power(c2,2)),
                 div(mul(mul(C(2),numerator),c_dot),power(c2,3)))
    T_dot=mul(C(8),beta_dot)
    Jp=evaluate(PD,Tp)
    H_new=evaluate(P,Tp)
    weight_inv=div(C(1),power(lam,p-1))
    lhs=mul(Jp,T_dot)
    rhs=mul(weight_inv,add(J0,mul(dlog_lambda,H0)))
    assert lhs==rhs
    assert mul(H_new,power(lam,p-1))==H0
    observed.append((k,alpha_dot,dlog_lambda,T_dot,Jp,lhs))

assert observed==[
    (0,(2584,1292),(78,218),(636,958),(3032,1282),(94,1491)),
    (1,(763,2055),(2470,1966),(554,2076),(1689,2223),(763,1901))
]
print('PASS_GH123_MARKED_HASSE_JET_CONNECTION')
print('Hasse(T) =',H0,' derivative =',J0)
for k,alpha_dot,L,T_dot,Jp,lhs in observed:
    print('branch',k,'alpha_dot',alpha_dot,'lambda_log_derivative',L,
          'Tprime_dot',T_dot,'Hasse_prime',Jp,'covariant_jet',lhs)
print('CHECKED: Ha_prime(T_alpha)*T_alpha_dot = lambda^(-(p-1))*[Ha_prime(T)+(lambda_dot/lambda)*Ha(T)]')
