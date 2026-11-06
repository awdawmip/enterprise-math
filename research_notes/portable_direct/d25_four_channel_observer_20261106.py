"""D25 target four-channel additive residual, exact integer checks."""
from d25_gauss_second_jet_20261106 import residues, primes

def channels(p):
    r=residues(p)
    A=(r['P']//p+r['C1'])%(p*p)
    B=r['K0']%(p*p)
    assert (A*B-1)%p==0
    q=[((A*B-1)//p)%p, (r['C2']*B)%p, (A*r['D1'])%p, (-2*r['J'])%p]
    assert sum(q)%p == r['second_digit_residue'] == (r['W']-p)//(p*p)%p
    return dict(p=p,A=A,B=B,product_lift=q[0],second_Gauss_jet=q[1],weighted_first_jet=q[2],signed_triangle=q[3],residual=sum(q)%p)

if __name__=='__main__':
    rows=[channels(p) for p in primes(997) if p%24 in (13,19)]
    assert len(rows)==45 and all(v['residual']==0 for v in rows)
    for item in rows:
        if item['p'] in (13,19,67,373,997):print(item)
    assert all(rows[1][x]!=0 for x in ['product_lift','second_Gauss_jet','weighted_first_jet','signed_triangle'])
    print("45 TARGET PRIME OBSERVERS PASSED")
