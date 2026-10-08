"""Bounded audit regression from binomial coefficient formulae, not author code."""
import json
from math import comb
from sympy import QQ
from sympy.polys.rings import ring

R, a = ring('a', QQ)
N = 43
zero, one = R.zero, R.one

def mul(u, v):
    out = [zero for _ in range(N+1)]
    for i,x in enumerate(u):
        for j,y in enumerate(v[:N+1-i]):
            out[i+j] += x*y
    return out

def inv(u):
    out = [one/u[0]] + [zero for _ in range(N)]
    for i in range(1,N+1):
        out[i] = -sum((u[j]*out[i-j] for j in range(1,i+1)),zero)/u[0]
    return out

def shift(u,k):
    return [zero]*k+u[:N+1-k]

# [z^n] V = sum Catalan(k) binom(n-k,2k) a^k.
# [z^n] H = sum binom(2k,k) binom(n-k,2k) a^k.
V = [sum((R(comb(2*k,k)//(k+1)*comb(n-k,2*k))*a**k
          for k in range(n//3+1)),zero) for n in range(N+1)]
H = [sum((R(comb(2*k,k)*comb(n-k,2*k))*a**k
          for k in range(n//3+1)),zero) for n in range(N+1)]
T = [-a*x for x in shift(V,3)]
T[0] += 2
T[1] -= 1
Ti = inv(T)
Qscaled = shift(mul(mul(V,H),Ti),4)  # Q = (s/108) Qscaled
B = [a*x for x in shift(V,2)]
B[0] += 1
Gxscaled = [-x for x in shift(mul(mul(mul(V,B),H),mul(Ti,Ti)),4)]
checked = []
for n in range(1,N+1):
    assert H[n-1].diff(a)-Gxscaled[n-1] == n*Qscaled[n]
    checked.append(n)

primes=[5,7,11,13,17,19,23,29,31,37,41,43]
rows=[]
for p in primes:
    coeffs=list(Qscaled[p].values())
    assert all(int(q.denominator)%p for q in coeffs)
    assert all(int(q.numerator)%p==0 for q in coeffs)
    rows.append({'p':p,'Qscaled_coefficient':str(Qscaled[p]),
                 'every_numerator_divisible_by_p':True})
result={'scope':'Independent finite exact-polynomial regression in QQ[a]; not the all-prime proof',
        'method':'Binomial expansions for H and V, direct power-series inversion for T',
        'author_code_imported_or_executed':False,
        'identity_n_range':[min(checked),max(checked)],
        'first_Q_coefficient':str(Qscaled[4]),'prime_checks':rows}
print(json.dumps(result,indent=2))
