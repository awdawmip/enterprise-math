"""PREFIX-1018: exact universal sign certificate for a frozen BRC terminal observer.

Requires Python 3 and SymPy. No floating-point arithmetic or unpinned
native BRC transition is used. The inherited observer is PREFIX-1016.
"""
from fractions import Fraction
from math import comb
from sympy import Matrix, Poly, Rational, cancel, expand, fraction, simplify, symbols, zeros

n, m, t, z = symbols("n m t z")

# 1. Eliminate the 7-state derivative module for f(t)=g(t)^6,
#    g(t)=sum_r t^r/(r!)^2 and t*g''+g'-g=0.
M = zeros(7, 7)
for j in range(7):
    if j < 6:
        M[j, j+1] = 6-j
    if j:
        M[j, j-1] = Rational(j)/t
        M[j, j] = -Rational(j)/t
rows = [Matrix([[1, 0, 0, 0, 0, 0, 0]])]
for _ in range(7):
    rows.append((rows[-1].diff(t) + rows[-1]*M).applyfunc(cancel))

p = {
    0: -6*(576*t*t - 170*t + 1),
    1: -(2304*t**3 - 5724*t*t + 516*t - 1),
    2: 21*t*(224*t*t - 116*t + 3),
    3: 7*t*t*(112*t*t - 344*t + 43),
    4: -350*t**3*(2*t - 1),
    5: -28*t**4*(2*t - 5),
    6: 21*t**5,
    7: t**6,
}
identity = zeros(1, 7)
for j, poly in p.items():
    identity += poly*rows[j]
assert all(cancel(component) == 0 for component in identity)

# Extract the polynomial recurrence coefficients in the A6(r)/(r!)^2 basis.
coeff = {}
for j, poly in p.items():
    for (power,), a in Poly(poly, t).terms():
        shift = j-power
        factor = 1
        for k in range(j):
            factor *= n+shift-k
        coeff[shift] = expand(coeff.get(shift, 0)+a*factor)
assert set(coeff) == {-2, -1, 0, 1}
assert simplify(coeff[1]-(n+1)**7) == 0
assert simplify(coeff[0]+2*(2*n+1)*(14*n**4+28*n**3+28*n*n+14*n+3)) == 0
assert simplify(coeff[-1]-4*n*(196*n*n+59)) == 0
assert simplify(coeff[-2]+1152*(2*n-1)) == 0

def alpha(k):
    return 2*(2*k+1)*(14*k**4+28*k**3+28*k*k+14*k+3)/(k+1)**5
def beta(k):
    return 4*k**3*(196*k*k+59)/(k+1)**5
def gamma(k):
    return 1152*(2*k-1)*k*k*(k-1)**2/(k+1)**5

# Independent exact multinomial splitting, and recurrence verification.
N = 15
A = [1]*(N+1)
for d in range(2, 7):
    A = [sum(comb(k,j)**2*A[k-j] for j in range(k+1))
         for k in range(N+1)]
assert A[:4] == [1,6,66,996]
for k in range(2,N):
    assert (k+1)**5*A[k+1] == (
        2*(2*k+1)*(14*k**4+28*k**3+28*k*k+14*k+3)*A[k]
        -4*k**3*(196*k*k+59)*A[k-1]
        +1152*(2*k-1)*k*k*(k-1)**2*A[k-2]
    )

# A global, invariant rational enclosure for R_k=A6(k+1)/A6(k).
def lower(k):
    return 36-Rational(90)/k+Rational(180)/k**2-Rational(360)/k**3-Rational(2500)/k**4
def upper(k):
    return 36-Rational(90)/k+Rational(180)/k**2-Rational(360)/k**3+Rational(2500)/k**4

for k in (9,10):
    assert lower(k) < Fraction(A[k+1],A[k]) < upper(k)

assert simplify(3*n*(196*n*n+59)-288*(2*n-1)*(n-1)**2) == 3*(4*n**3+480*n*n-325*n+96)

certificates = {}
def prove_positive(name,expr,variable,shift):
    numerator,denominator = fraction(cancel(expr))
    num = Poly(expand(numerator.subs(variable,z+shift)),z)
    den = Poly(expand(denominator.subs(variable,z+shift)),z)
    assert all(c>0 for c in num.all_coeffs())
    assert all(c>0 for c in den.all_coeffs())
    certificates[name] = {
        "shift":shift,
        "numerator_degree":num.degree(),
        "denominator_degree":den.degree(),
        "numerator_coefficient_count":len(num.all_coeffs()),
        "denominator_coefficient_count":len(den.all_coeffs()),
        "numerator_constant":str(num.all_coeffs()[-1]),
        "denominator_constant":str(den.all_coeffs()[-1]),
        "numerator_leading":str(num.all_coeffs()[0]),
        "denominator_leading":str(den.all_coeffs()[0]),
        "numerator_coefficients_ascending":[str(c) for c in reversed(num.all_coeffs())],
        "denominator_coefficients_ascending":[str(c) for c in reversed(den.all_coeffs())],
    }

# Inductively preserve both bounds (r>=11).
lo_step = alpha(n)-beta(n)/lower(n-1)+gamma(n)/(lower(n-1)*upper(n-2))
hi_step = alpha(n)-beta(n)/upper(n-1)+gamma(n)/(upper(n-1)*lower(n-2))
prove_positive("ratio_lower_slack",lo_step-lower(n),n,11)
prove_positive("ratio_upper_slack",upper(n)-hi_step,n,11)

# The exact PREFIX-1016 three-shift positive-port contrast.
c1 = -Rational(72,5)*(72*m*m+163*m+80)/(m+1)
c2 = Rational(2,5)*(144*m**3+1135*m*m+2367*m+1310)/((m+1)*(m+2))
c3 = -Rational(2,5)*(m+8)*(2*m+5)/(m+2)

prove_positive("contrast_monotonicity",c1/lower(m+1)+c2,m,10)
prove_positive("contrast_global_lower_bound",
               (c1/lower(m+1)+c2)/upper(m+2)+c3,m,10)

finite = {}
for k in range(1,10):
    delta = c1.subs(m,k)*A[k+1]+c2.subs(m,k)*A[k+2]+c3.subs(m,k)*A[k+3]
    assert delta.q==1 and delta>0
    finite[str(k+4)] = str(delta)

print("PREFIX-1018 THEOREM VERIFIED: Q+_(n,1)>Q+_(n,j), all n>=5, j=2..6")
print("ratio seeds:", {k:str(Fraction(A[k+1],A[k])) for k in (9,10)})
print("finite n=5..13:", finite)
for name,data in certificates.items():
    print(name,"degrees",data["numerator_degree"],data["denominator_degree"],
          "all coefficients strictly positive")

if __name__=="__main__":
    import json
    import pathlib
    evidence = {
        "schema":"PREFIX1018_R6_EXACT_INEQUALITY_CERTIFICATE_V1",
        "frozen_p000_commit":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
        "source_theorem":"PREFIX-1016, three A6 shifts",
        "finite_positive_n":finite,
        "ratio_seeds":{str(k):str(Fraction(A[k+1],A[k])) for k in (9,10)},
        "certificates":certificates,
        "verified_claim":"All integers n>=5, strict Q+_n,1>Q+_n,j for j=2..6",
        "status":"AUTHOR_COMPUTER_ASSISTED_EXACT_PROOF_NOT_INDEPENDENTLY_REVIEWED",
    }
    path = pathlib.Path(__file__).with_name("PREFIX1018_R6_GLOBAL_POSITIVE_PORT_CERT.json")
    path.write_text(json.dumps(evidence,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print("Certificate saved:",path.name)
