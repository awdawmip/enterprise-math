#!/usr/bin/env python3
"""D25 prime-power port shadow exact verifier, separate from native experiment."""
from math import comb, isqrt
import json

def prime(q):
    return q >= 2 and all(q % d for d in range(2, isqrt(q) + 1))

def direct(m, e, q):
    a = b = 0
    x = pow(2, -1, q)
    for k in range(m + 1):
        t = comb(m, k) * comb(2*m + e, k) * pow(x, k, q) % q
        a = (a + t) % q
        b = (b + (1-6*e+12*k)*t) % q
    return a, b

def verify():
    checked = higher = collapsed = 0
    examples = {}
    for q in range(5, 998):
        if not prime(q): continue
        e1 = 0 if q % 6 == 1 else 1
        m1 = (q-1-4*e1)//6
        A1, B1 = direct(m1, e1, q)
        for r in range(1, 12):
            n = q**r
            er = 0 if n % 6 == 1 else 1
            m = (n-1-4*er)//6
            if m > 600: break
            c = pow(2, -((q+1)//2)*(r//2), q) if q % 6 == 5 else 1
            predicted = (c*pow(A1,r,q)%q, c*pow(A1,r-1,q)*B1%q)
            observed = direct(m, er, q)
            assert predicted == observed, (q,r,n,predicted,observed)
            checked += 1; higher += (r>=2)
            collapsed += (r>=2 and A1==0 and observed==(0,0))
            if (q,r) in {(5,5),(7,4),(11,3),(13,3),(17,2),(29,2)}:
                examples[f"{q}^{r}"] = {"N":n,"base":[A1,B1],"ports":list(observed)}
    assert (checked,higher,collapsed)==(188,22,9)
    return {"prime_bound":997,"m_bound":600,"rows":checked,"higher":higher,
            "base_A_zero_both_zero":collapsed,"examples":examples,
            "all_exact_checks_passed": True}
if __name__=="__main__":
    print(json.dumps(verify(),indent=2))
