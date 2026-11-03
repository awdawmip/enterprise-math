"""D25 original-216 argument jet modulo p^3, using exact p-unit modular arithmetic.
Author-side finite regression, not native H0/B0 or canonical acceptance.
"""
from math import comb
import json


def prime_list(limit):
    flags = bytearray(b'\x01') * (limit + 1)
    flags[0:2] = b'\x00\x00'
    for a in range(2, int(limit**0.5) + 1):
        if flags[a]:
            flags[a*a:limit+1:a] = b'\x00' * (((limit - a*a)//a) + 1)
    return [p for p in range(5, limit + 1) if flags[p] and p % 24 in (13, 19)]


def check_prime(p):
    m = p**3
    g = dg = ddg = 0
    gk = 1
    for k in range(p):
        g = (g + gk) % m
        dg = (dg + 2*k*gk) % m
        ddg = (ddg + 4*k*(k-1)*gk) % m
        if k < p-1:
            gk = gk * (6*k + 1) * (3*k + 1) * pow(36*(k+1)**2, -1, m) % m

    w = wp = wpp = 0
    values = [0, 0, 0]
    factors = [1, 1, 1]
    bases = [1 + p*l for l in (1, 2, 3)]
    bk = 1
    for k in range(p):
        weighted = (6*k+1)*bk
        w = (w + weighted) % m
        wp = (wp + k*weighted) % m
        wpp = (wpp + k*(k-1)*weighted) % m
        for i in range(3):
            values[i] = (values[i] + weighted * factors[i]) % m
            factors[i] = (factors[i] * bases[i]) % m
        if p in (13, 19, 373):
            raw = comb(2*k, k)**2 * comb(3*k, k) * pow(216, -k, m) % m
            assert bk == raw, (p, k, bk, raw)
        if k < p-1:
            bk = bk * (2*k+1)*(3*k+1)*(3*k+2) * pow(36*(k+1)**3, -1, m) % m

    assert g % p == 0, p
    assert dg % p != 0, p
    assert (ddg + dg - (2*pow(9,-1,m))*g) % (p*p) == 0, p
    assert wp % (p*p) == (3*dg*dg + 4*g*dg) % (p*p), p
    assert wpp % p == (2*dg*dg) % p, p
    for l,v in zip((1,2,3), values):
        delta = p*l*(3*dg*dg+4*g*dg) + p*p*l*l*dg*dg
        assert (v - w - delta) % m == 0, (p,l)
    plus=values[0]
    minus=0
    bk=1
    tminus=1
    for k in range(p):
        minus=(minus+(6*k+1)*bk*tminus)%m
        tminus=tminus*(1-p)%m
        if k<p-1:
            bk=bk*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3,-1,m)%m
    assert (plus+minus-2*w-2*p*p*dg*dg) % m == 0, p
    return {"p":p,"G_over_p_mod_p2":(g//p)%(p*p),"Gprime_mod_p2":dg%(p*p),"weighted_derivative_mod_p2":wp%(p*p),"weighted_second_derivative_mod_p":wpp%p,"W_1_mod_p3":w,"W_1_plus_p_mod_p3":plus,"symmetric_curvature_mod_p3":(plus+minus-2*w)%m}


def main():
    ps=prime_list(2000)
    rows=[check_prime(p) for p in ps]
    out={"status":"PASS","domain":"every prime p <= 2000 with p mod 24 in {13,19}","case_count":len(rows),"argument_lifts_per_p":[1,2,3],"original_integer_binomial_independent_cases":[13,19,373],"sample_rows":[x for x in rows if x['p'] in (13,19,373)]}
    with open('/mnt/data/d25_second_digit_argument_jet_20261103_results.json','w',encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2);f.write('\n')
    print(json.dumps(out,ensure_ascii=False,indent=2))

if __name__=='__main__':
    main()
