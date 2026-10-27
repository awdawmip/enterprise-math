#!/usr/bin/env python3
"""Author-only D25 original weighted-216 mid-band mod-p^3 certificate.
Finite p-adic parameter jet. NOT native fixed H0/B0 and NOT all-prime LIFT.
"""
from math import comb, factorial, isqrt
import hashlib
import json

def isprime(p):
    return p >= 2 and all(p % q for q in range(2, isqrt(p) + 1))

def run(p):
    assert p > 3 and isprime(p) and p % 6 == 1
    m = (p - 1) // 6
    start, finish = 2*m + 1, 3*m
    mod, pm = p**3, p**2
    def w(n):
        return ((6*n+1)*comb(2*n,n)**2*comb(3*n,n)*pow(216,-n,mod)) % mod
    mid = [w(n) for n in range(start,finish+1)]
    assert all(x % p == 0 for x in mid)
    mid_actual = (sum(mid) % mod)//p
    n = start
    base = (factorial(2*n)*(factorial(3*n)//p) *
            pow(factorial(n),-5,pm) * pow(216,-n,pm)) % pm
    wilson = (factorial(p-1)+1)//p % p
    base_w = (-2 * factorial(4*m+2) * pow(factorial(n),-5,pm)
              *pow(216,-n,pm) * (1+p*((3*pow(2,-1,pm)-wilson)%pm))) % pm
    assert base_w == base
    c2, d1 = 1, 0
    J_weighted, J_scalar, J_log_weighted = 0, 0, 0
    all_predicted_terms = []
    for k in range(m):
        weight = 6*k+5
        J_weighted = (J_weighted + weight*c2) % pm
        J_scalar = (J_scalar + c2) % p
        J_log_weighted = (J_log_weighted + weight*(c2%p)*d1) % p
        q_shift = (c2*(1 + (p*pow(3,-1,pm)*d1))) % pm
        predicted = (base*(weight+2*p)*q_shift) % pm
        all_predicted_terms.append(predicted)
        if k < m-1:
            inv6 = pow(6,-1,pm)
            inv3 = pow(3,-1,pm)
            a = ((6*k+7)*inv6)%pm
            b = k+1
            c = ((3*k+4)*inv3)%pm
            d = ((3*k+5)*inv3)%pm
            c2 = (c2*pow(2,-1,pm)*a*b*c*pow(d,-3,pm))%pm
            inv6p, inv3p = inv6%p, inv3%p
            ap = (6*k+7)*inv6p%p
            bp = b%p
            cp = (3*k+4)*inv3p%p
            dp = (3*k+5)*inv3p%p
            assert ap*bp*cp*dp%p != 0
            d1 = (d1+pow(ap,-1,p)+pow(bp,-1,p)+pow(cp,-1,p)
                  -3*pow(dp,-1,p))%p
    mid_pred = base*(J_weighted + (p*pow(3,-1,pm)*(6*J_scalar + J_log_weighted)))%pm
    assert mid_pred == mid_actual
    assert [(u//p)%pm for u in mid] == all_predicted_terms
    low = sum(w(k) for k in range(0,start))%mod
    full = sum(w(k) for k in range(p))%mod
    high = sum(w(k) for k in range(3*m+1,4*m+1))%mod
    assert all(w(k)==0 for k in range(4*m+1,p))
    assert (low+p*mid_pred+high)%mod == full
    return {"p":p,"m":m,"base_q_over_p_mod_p2":base,
            "Wilson_quot_mod_p":wilson,"Jw_mod_p2":J_weighted,
            "J0_mod_p":J_scalar,"Jt_weighted_mod_p":J_log_weighted,
            "mid_quot_mod_p2":mid_actual,"mid_mod_p3":sum(mid)%mod,
            "low_through_2m_mod_p3":low,"high_mod_p3":high,
            "full_W_mod_p3":full}

if __name__ == '__main__':
    recs=[run(p) for p in (7,13,19,31,37,43,61,67,73,211,373)]
    blob=json.dumps(recs,sort_keys=True,separators=(',',':'))
    print(blob)
    print('SHA256='+hashlib.sha256(blob.encode()).hexdigest())
    print('D25_WEIGHTED216_MIDDLE_PARAMETER_JET_PASS')
