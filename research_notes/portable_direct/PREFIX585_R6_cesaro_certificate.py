#!/usr/bin/env python3
"""PREFIX-585-R6 exact certificate: cumulative gate-pair cubic bias.
Pure standard library. Finite tests audit the all-N algebraic proof in the note.
"""
from fractions import Fraction as F
import json

L = F(1, 5184)
C = F(7, 15552)
Q = [F(0), F(1,576), -F(1,864), F(1,1728), F(1,1944)]
for _ in range(256):
    Q.append((-3*Q[-1] + 2*Q[-2] + 6*Q[-3] + 3*Q[-4] + Q[-5])/9)
assert all(9*Q[n+5]+3*Q[n+4]-2*Q[n+3]-6*Q[n+2]-3*Q[n+1]-Q[n] == 0 for n in range(256))

# H(z) = Q(z) - L/(1-z) = N(z)/[5184 D(z)],
# N(z)= -9 +60z+23z^2+10z^3; D(z)=(z^2+2z+3)^2.
N = [-9,60,23,10]
D = [9,12,10,4,1]
H = [q-L for q in Q]
for n in range(256):
    assert 5184*sum((F(D[k])*H[n-k] for k in range(min(n,4)+1)),F(0)) == (N[n] if n < len(N) else 0)

H1 = F(sum(N), 5184*sum(D))
Hp1 = (F(sum(k*a for k,a in enumerate(N)))*sum(D)-F(sum(N))*sum(k*a for k,a in enumerate(D)))/(5184*sum(D)**2)
assert H1 == C
assert Hp1 == F(1,7776)

# Rational upper envelope for the analytic tail, valid for all m>=5:
# |C - S_m| <= rho^m[(sqrt(34)+2m)/(2304 sqrt(2)) +1/(2304 sqrt(3))]
# < U_m = (3/5)^m [5/2688 + 5m/8064 + 1/3840]
# by sqrt34<6, sqrt2>7/5, sqrt3>5/3.
assert 34<36 and F(49,25)<2 and F(25,9)<3

def U(m):
    return F(3,5)**m * (F(5,2688)+ F(5*m,8064)+F(1,3840))
assert U(5)==F(11367,28000000) and U(5)<C
# U_{m+1}/U_m < (3/5)*(1+1/m) <=18/25<1 for m>=5.
assert F(18,25)<1

S = F(0)
partial = {}
for m in range(1,256):
    S += Q[m-1] - L
    if m<=8:partial[str(m)]=str(S)
    assert (S<0 if m==1 else S==0 if m==3 else S>0)
    if m>=5: assert abs(S-C) < U(m)

result={
    "schema":"PREFIX585_R6_CESARO_CERTIFICATE_V1",
    "exact_terms_checked":256,
    "recurrences_checked":256,
    "gf_coefficients_checked":256,
    "expected_limit":str(L),
    "summed_bias":str(H1),
    "first_weighted_bias":str(Hp1),
    "finite_partial_bias":partial,
    "N5_rational_tail_majorant":str(U(5)),
    "all_length_proof":"H(z) rational; geometric derivative tail bound and decreasing rational U_m for m>=5; exact m=1..4",
    "status":"ALL_CHECKS_PASS"
}
print(json.dumps(result,ensure_ascii=False,indent=2))
