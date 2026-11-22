"""R5: finite-field Hasse-jet certificates for all thresholds 1<=m<=30.
Exact arithmetic, scalar five-event model pinned at enterprise-math@75d986aa.
Demonstrates a double or higher pole at 18 primitive orders, sufficient for
M_m^(>=1) = Lambda_1. Run with Python 3 standard library.
"""
from itertools import product
from math import comb, isqrt, lcm
import csv
import sys

PRICES = range(214, 315)
EVENTS = (
    {214, 215, 216, 217, 218},
    {214, 216, 217, 218, 219, 220, 221},
    {215, 216, 217, 218, 219, 220, 221},
    set(range(223, 291)), set(range(296, 313)),
)
# Exactly the independently archived m=1 order/p/z witness set.
CERT = (
    (32, 97, 28), (54, 109, 36), (25, 101, 16), (49, 197, 16),
    (11, 23, 4), (13, 53, 16), (17, 103, 64), (19, 191, 69),
    (23, 47, 4), (29, 59, 4), (62, 311, 264), (37, 149, 16),
    (41, 83, 4), (43, 173, 16), (47, 283, 64), (59, 709, 551),
    (61, 367, 64), (73, 293, 16),
)
# A zero residue at one conjugate is not evidence of cyclotomic vanishing;
# these fixed alternate conjugates of the SAME primitive order give witnesses.
ALTERNATES = {
    (9, 41): (83, 3),
    (11, 59): (709, 20),
    (18, 59): (709, 20),
    (29, 62): (311, 11),
}

def factor_primes(n):
    out = []
    t = 2
    while t*t <= n:
        if n % t == 0:
            out.append(t)
            while n % t == 0: n //= t
        t += 1
    if n > 1: out.append(n)
    return out

def is_prime(n):
    return n > 1 and all(n % k for k in range(2, isqrt(n)+1))

def unit(n):
    return [1] + [0]*n

def minus(a, b, p):
    return [(x-y) % p for x,y in zip(a,b)]

def plus(a, b, p):
    return [(x+y) % p for x,y in zip(a,b)]

def times(a, b, p):
    return [sum(a[k]*b[j-k] for k in range(j+1)) % p
            for j in range(len(a))]

def q_power(price, p, z, J):
    # q=z(1+t), q^price=z^price * sum(binomial(price,j)t^j).
    zp = pow(z, price, p)
    return [zp*comb(price,j) % p for j in range(J+1)]

def overlapping_three_numerator(m, d, p, z, J):
    total = [0]*(J+1)
    xs = {price:q_power(price,p,z,J) for price in range(214,222)}
    one = unit(J)
    for mask in range(1,8):
        selected = [i for i in range(3) if mask & (1<<i)]
        r = len(selected)
        support = sorted(set().union(*(EVENTS[i] for i in selected)))
        # The product P_U already has more zeros than this jet can observe.
        if sum(price%d==0 for price in support) > J:
            continue
        block = one[:]
        for price in support:
            block = times(block, minus(one, xs[price],p),p)
        strides = [m**(r-1-i) for i in range(r)]
        dp = [[0]*(J+1) for _ in range(m**r)]
        dp[0] = one[:]
        for price in support:
            delta = [int(price in EVENTS[i]) for i in selected]
            offset = sum(v*s for v,s in zip(delta,strides))
            x = xs[price]
            for flat in range(m**r):
                # Lexicographic ascending order incorporates unlimited copies.
                if all((flat // strides[k])%m >= delta[k] for k in range(r)):
                    dp[flat] = plus(dp[flat],times(x,dp[flat-offset],p),p)
        prefix = [sum(row[k] for row in dp)%p for k in range(J+1)]
        term = times(block,prefix,p)
        total = plus(total,[v*(1 if r%2 else -1)%p for v in term],p)
    return total

def disjoint_total_count_numerator(m, d, p, z, J, support):
    one = unit(J)
    if sum(price%d==0 for price in support) > J:
        return [0]*(J+1)
    h = [one[:]] + [[0]*(J+1) for _ in range(m-1)]
    block = one[:]
    for price in sorted(support):
        x = q_power(price,p,z,J)
        block = times(block,minus(one,x,p),p)
        for k in range(1,m):
            h[k] = plus(h[k],times(x,h[k-1],p),p)
    prefix = [sum(row[k] for row in h)%p for k in range(J+1)]
    return times(block,prefix,p)

def numerator_jet(m,d,p,z,J):
    a = overlapping_three_numerator(m,d,p,z,J)
    b = disjoint_total_count_numerator(m,d,p,z,J,EVENTS[3])
    c = disjoint_total_count_numerator(m,d,p,z,J,EVENTS[4])
    one = unit(J)
    return minus(one,times(times(minus(one,a,p),minus(one,b,p),p),
                           minus(one,c,p),p),p)

def proof_rows(first=1,last=30):
    lambda_1 = lcm(*(d for d in range(1,315)
                     if sum(price%d==0 for price in PRICES)>=2))
    assert lambda_1==814202665467037976682352800
    assert lcm(*(d for d,p,z in CERT))==lambda_1
    for d,p,z in CERT:
        assert is_prime(p) and (p-1)%d==0
        assert pow(z,d,p)==1 and all(pow(z,d//t,p)!=1 for t in factor_primes(d))
    summary={0:0,1:0,2:0};rows=[]
    for m in range(first,last+1):
        for d,p,z in CERT:
            nd=sum(price%d==0 for price in PRICES)
            assert nd>=2
            J=min(2,nd-2)
            coefficients=numerator_jet(m,d,p,z,J)
            k=next((k for k,v in enumerate(coefficients) if v),None)
            if k is None:
                p,z=ALTERNATES[(m,d)]
                assert is_prime(p) and (p-1)%d==0
                assert pow(z,d,p)==1 and all(pow(z,d//t,p)!=1 for t in factor_primes(d))
                coefficients=numerator_jet(m,d,p,z,J)
                k=next((k for k,v in enumerate(coefficients) if v),None)
            assert k is not None and k <= nd-2, (m,d,coefficients)
            summary[k]+=1
            rows.append((m,d,nd,p,z,k,coefficients[k]))
    return lambda_1,summary,rows

if __name__ == '__main__':
    first=int(sys.argv[2]) if len(sys.argv)>2 else 1
    last=int(sys.argv[3]) if len(sys.argv)>3 else 30
    L,s,rows=proof_rows(first,last)
    filename=sys.argv[1] if len(sys.argv)>1 else 'R5_M1_M30_WITNESS_JETS.csv'
    with open(filename,'w',newline='',encoding='utf8') as f:
        w=csv.writer(f)
        w.writerow(('m','primitive_order','denominator_zero_order','prime','primitive_root','first_nonzero_jet_order','nonzero_jet_residue'))
        w.writerows(rows)
    print(f'PASS: {len(rows)} verified finite-field root/jet witnesses for m={first}..{last}; jet orders {s}; Lambda_1={L}')
    print(f'FILE={filename}; ALTERNATES={ALTERNATES}')
