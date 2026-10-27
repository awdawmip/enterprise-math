#!/usr/bin/env python3
"""R335 exact symbolic certificate for the fourth-highest BRC Newton coefficient.

This is a mathematical certificate *conditional on the author-side R330
rational extraction identity*. It derives every low-order E/N polynomial
from the complete signed twelve-step K/J data and proves the jet recurrence
as a symbolic polynomial identity, rather than extrapolating sampled r.
"""
import argparse
import json
from math import comb
import sympy as S


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def poly_add(a, b):
    z = [0] * max(len(a), len(b))
    for i, x in enumerate(a): z[i] += x
    for i, x in enumerate(b): z[i] += x
    return z


def term(n, scale, shift):
    return [0] * shift + [scale * choose(n, i) for i in range(n + 1)] if n >= 0 else [0]


def kernel(i):
    d = (-choose(4, i) + choose(2, i - 1),
         choose(5, i - 1) - choose(5, i - 2),
         choose(7, i - 2), -choose(9, i - 3))
    z = [0]
    for jj, x in enumerate(d, 1):
        if x: z = poly_add(z, term(i + 1 - jj, -x, i - 1))
    return z


def forcing(i):
    z = [0]
    for x, n in ((-choose(3, i - 1), i),
                 (-choose(6, i - 1), i - 1),
                 (choose(8, i - 2), i - 2)):
        if x: z = poly_add(z, term(n, x, i))
    return z


def coeff_series(poly, symbol):
    return sum(S.Integer(v) * symbol ** i for i, v in enumerate(poly))


def main():
    y, z, eps, j, r, m, u = S.symbols('y z eps j r m u')
    a = S.Rational(4, 5)
    x = (1 - y) / 2
    t = y * z
    k_total = sum(coeff_series(kernel(i), t) * x ** i for i in range(1, 13))
    a_total = 1 + t + sum(coeff_series(forcing(i), t) * x ** i for i in range(1, 11))
    kp = S.Poly(S.expand(k_total), y)
    ap = S.Poly(S.expand(a_total), y)
    E = [S.factor(-kp.nth(i + 1)) for i in range(5)]
    N = [S.factor(ap.nth(i)) for i in range(4)]
    expected_e = [1 - 5*z/4, z, z*(11*z*z-16*z+4)/16,
                  z*z*(3*z-8)*(3*z-2)/8,
                  z*z*(9*z**3-308*z*z+392*z-64)/64]
    expected_n = [S.Integer(1), S.Integer(0), -z*(5*z-2)/2,
                  -z*z*(17*z-18)/4]
    for actual, target in zip(E, expected_e):
        assert S.simplify(actual - target) == 0
    for actual, target in zip(N, expected_n):
        assert S.simplify(actual - target) == 0

    # Exact derivatives of g_j at z=a, normalized by (-a)^(j-d).
    p = lambda w: -(69*w + 11)/80
    h = lambda w: (4761*w*w - 6685*w - 9354)/6400
    v = lambda w: -3*(109503*w**3 - 513636*w**2 - 391199*w - 1307460)/512000
    ef = [[S.factor(S.diff(el,z,d).subs(z,a)/S.factorial(d)) for d in range(4)] for el in E]
    nf = [[S.factor(S.diff(nl,z,d).subs(z,a)/S.factorial(d)) for d in range(4)] for nl in N]
    def mul(A, B): return [sum(A[k]*B[i-k] for k in range(i+1)) for i in range(4)]
    def power(A, n):
        out = [1,0,0,0]
        for _ in range(n): out = mul(out, A)
        return out
    jets = [[S.Integer(1),0,0,0]]
    for k in range(1,7):
        curr = mul(nf[k] if k < len(nf) else [0]*4, power(ef[0], k))
        for ell in range(1,min(k,4)+1):
            sub = mul(mul(ef[ell], jets[k-ell]), power(ef[0],ell-1))
            curr = [curr[i]-sub[i] for i in range(4)]
        jets.append([S.factor(c) for c in curr])
    for k in range(1,7): assert S.simplify(jets[k][1]*(-a)**(1-k)-p(k)) == 0
    for k in range(2,7): assert S.simplify(2*jets[k][2]*(-a)**(2-k)-h(k)) == 0
    for k in range(3,7): assert S.simplify(6*jets[k][3]*(-a)**(3-k)-v(k)) == 0

    # The formal identity for any j>=7: all j-ell>=3 when 1<=ell<=4.
    # Higher E_ell carry E0^(ell-1)=O(eps^4), and N_j E0^j=O(eps^7).
    jet = lambda w: (1+p(w)*eps/(-a)+h(w)*eps**2/(2*(-a)**2)
                     +v(w)*eps**3/(6*(-a)**3))
    next_normalized = 0
    for ell in range(1,5):
        summand = -E[ell].subs(z,a+eps)*(-a)**(-ell)*jet(j-ell)*E[0].subs(z,a+eps)**(ell-1)
        next_normalized += S.expand(summand).coeff(eps,3)
    next_normalized = S.factor(next_normalized*6*(-a)**3)
    assert S.simplify(next_normalized - v(j)) == 0

    # e_3 of the r shifted factors from R330 Eq.(4).
    n = r-j
    s1 = j*(j+1)/2
    s2 = j*(j+1)*(2*j+1)/6
    s3 = s1**2
    b1 = -(n*j/2+n*(n-1)/4)
    b2 = (n*j*j+j*n*(n-1)+n*(n-1)*(2*n-1)/6)/4
    b3 = -(n*j**3+3*j*j*n*(n-1)/2+3*j*n*(n-1)*(2*n-1)/6+(n*(n-1)/2)**2)/8
    power1 = s1+b1-j*m
    power2 = s2+b2-2*s1*m+j*m*m
    power3 = s3+b3-3*s2*m+3*s1*m*m-j*m**3
    e3 = S.Poly(S.expand((power1**3-3*power1*power2+2*power3)/6),m)
    # Weighted sums of m^k g_{j,m} a^m / (-a)^j for j>=3.
    moments = [1,-p(j),-p(j)+h(j),-p(j)+3*h(j)-v(j)]
    W = S.factor(sum(e3.nth(k)*moments[k] for k in range(4)))
    # Verify exceptional j=0,1,2 directly, avoiding extrapolation of jet formulas.
    g = [S.Integer(1), -z]
    g.append(S.expand(N[2]*E[0]**2 - E[1]*g[1] - E[2]*g[0]*E[0]))
    for jj in range(3):
        raw = []
        for degree in range(4):
            expr = g[jj]
            for _ in range(degree): expr = S.expand(z*S.diff(expr,z))
            raw.append(S.factor(expr.subs(z,a)/(-a)**jj))
        low = S.factor(sum(e3.nth(k).subs(j,jj)*raw[k] for k in range(4)))
        assert S.simplify(low-W.subs(j,jj)) == 0

    # Falling-factorial decomposition and exact signed binomial expectation.
    residual = S.expand(W)
    falling = []
    for kk in range(6,-1,-1):
        ck = S.factor(S.Poly(residual,j).nth(kk))
        if ck != 0:
            falling.append((kk,ck))
            residual = S.expand(residual-ck*S.prod(j-i for i in range(kk)))
    assert residual == 0
    C = S.factor(sum(ck*S.prod(r-i for i in range(kk))*S.Rational(-2,3)**kk
                     for kk,ck in falling))
    asserted_C = -r*(r-2)*(r-1)*(729*r**3+1332*r**2-36437*r+101640)/162000
    assert S.simplify(C-asserted_C) == 0

    # Convert the top four powers in q to the Newton coefficient Delta^(r-3).
    A = -S.Rational(3,10)*r*(r-1)
    B = r*(r-1)*(243*r*r-95*r-3542)/5400
    P1 = S.factor(r*r+A)
    P2 = S.factor(S.binomial(r,2)*r*r+A*r*(r-1)+B)
    P3 = S.factor(S.binomial(r,3)*r**3+A*S.binomial(r-1,2)*r*r+B*r*(r-2)+C)
    St2 = lambda v: S.binomial(v,3)+3*S.binomial(v,4)
    St3 = lambda v: S.binomial(v,4)+10*S.binomial(v,5)+15*S.binomial(v,6)
    scaled = S.factor(S.expand_func(P3+S.binomial(r-2,2)*P2+St2(r-1)*P1+St3(r)))
    Q = S.factor(scaled/(r*(r-1)*(r-2)))
    expected = S.Rational(2,10125)*(1458*r**3-3681*r**2-1304*r+1425)
    assert S.simplify(Q-expected) == 0
    shifted = S.factor(expected.subs(r,u+3))
    assert S.simplify(shifted-S.Rational(2,10125)*(1458*u**3+9441*u**2+15976*u+3750)) == 0
    assert all(S.Poly(shifted,u).coeff_monomial(u**k)>0 for k in range(4))
    return {
      'schema':'R335_FOURTH_NEWTON_SYMBOLIC_CERTIFICATE_V1',
      'status':'PASS',
      'model':'complete signed 12-step BRC auxiliary K/J model',
      'mathematical_dependency':'R330 author-side exact extraction and degree <=r',
      'E4':str(S.factor(E[4])), 'N3':str(S.factor(N[3])),
      'normalized_third_jet':'-3*(109503*j**3-513636*j**2-391199*j-1307460)/512000, j>=3',
      'third_jet_universal_recurrence':'symbolic polynomial identity PASS for j>=7; bases j=3..6 verified',
      'exceptional_j012':'independent exact raw moment checks PASS',
      'q_to_the_r_minus_3_ratio':str(C),
      'falling_factors':[[int(k),str(vv)] for k,vv in falling],
      'claim':'c[r,r-3]=2*6**r*(1458*r**3-3681*r**2-1304*r+1425)/10125 for r>=3',
      'shifted_positive_polynomial':'2*(1458*u**3+9441*u**2+15976*u+3750)/10125, u=r-3>=0',
      'arithmetic':'symbolic exact rational, no float signs',
      'review':'AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED'}

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--out',default='R335_SYMBOLIC_EVIDENCE.json')
    opts=parser.parse_args()
    result=main()
    with open(opts.out,'w',encoding='utf-8') as f:
        json.dump(result,f,indent=2,ensure_ascii=False);f.write('\n')
    print('PASS:',result['claim'])
