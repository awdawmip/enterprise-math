# D25/LIFT — inert quadratic Hesse coefficient carrier: conjugation, norm obstruction and rank-one semilinear criterion

2026-10-25 · TASK_RESEARCH · PORTABLE AUTHOR DERIVATION · UNREVIEWED / NOT_ADMITTED / NOT A NATIVE CM EXPERIMENT. Source Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 is not changed. This note consumes, without recrediting, the previously Source-checkpointed Hesse reflection identity, symmetric/odd Green split and p=373 odd-branch witness.

## Exact statement, domain, and proof

Let p>=13 be prime, p congruent to 13 or 19 (mod 24), n=(p-1)/3, and
\[
c_k=\frac{(3k)!}{27^k(k!)^3},\quad A_p(X)=\sum_{k=0}^n c_kX^k,\quad B_p(X)=A_p(1-X).
\]
All displayed rational coefficients have p-unit denominators. Work in the quadratic unramified coefficient ring \(R_r=(\mathbb Z/p^r\mathbb Z)[T]/(T^2-2)\), r>=3, with u=(2-T)/4, \(\bar u=1-u=(2+T)/4\), \(Y=u(1-u)=1/8\), and \(\sigma(T)=-T\). Since p=13 or 19 (mod24) has p=5 or 3 (mod8), \((2/p)=-1\); thus \(R_1=\mathbb F_{p^2}\) and the ring involution sigma reduces to the coefficient-field Frobenius \(z\mapsto z^p\) **mod p only**. This is not an assertion about crystalline Frobenius on a native H0/B0 module.

Consume the exact *previously proved* source-labeled factorization
\[
A_p(X)=G_p(Y)+\frac p2(1-2X)\Phi_p(Y),\quad
B_p(X)=G_p(Y)-\frac p2(1-2X)\Phi_p(Y),
\]
where G and Phi are p-integral polynomials. At the two tagged ports, exactly over \(\mathbb Z_{(p)}[T]/(T^2-2)\),
\[
A_p(u)=G+\frac {pT}4\Phi,\quad A_p(\bar u)=G-\frac {pT}4\Phi,
\quad G=G_p(1/8),\quad\Phi=\Phi_p(1/8).
\]
**New exact trace/norm transport for this ordinary source carrier** therefore is
\[
\boxed{\operatorname{Tr}_{R}(A_p(u))=2G,\quad
\operatorname{N}_{R}(A_p(u))=G^2-\frac{p^2}{8}\Phi^2.}
\]
Consequently the quadratic discriminant of the two tagged ports satisfies
\[
\boxed{\operatorname{Tr}(A)^2-4\operatorname{N}(A)=\frac{p^2}{2}\Phi^2.}
\]
Both formulas are exact rational identities, valid before modular reduction. If \(A_p(u)=a+bT\bmod p^3\) with canonical representatives \(0\le a,b<p^3\), the inherited odd factorization forces \(p\mid b\), and \(v=b/p\bmod p\) obeys
\[
\Phi\bmod p=4v,\qquad
\frac{\operatorname N(A)-G^2}{p^2}\equiv-2v^2\pmod p,\qquad
\frac{\operatorname{Tr}(A)^2-4\operatorname N(A)}{p^2}\equiv8v^2\pmod p.
\]
The denominator divisions in the latter expressions are exact integer divisions after choosing residue representatives of quantities divisible by p²; their mod-p class is well defined. Trace/norm mod p² erase the signed order-p odd deviation; the third digit of norm detects its square but does **not** recover its sign or the ordered port.

## Frobenius distinction and conditional complete invariant

Let \(q_p(2)=(2^{p-1}-1)/p\). Because the Euler branch \(2^{(p-1)/2}\equiv-1\bmod p\), squaring the unique p-adic expansion of that branch gives
\[
\boxed{T^p\equiv-\bigl(1+\tfrac p2q_p(2)\bigr)T\pmod{p^2}.}
\]
Hence \(T\mapsto T^p\) and \(\sigma(T)=-T\) differ at the second digit by \(-pq_p(2)T/2\) unless the Fermat quotient vanishes. More basically, \(z\mapsto z^p\) is not generally additive on \(R_2\). The canonical unramified coefficient-ring Frobenius lift is sigma, but neither it nor the pth-power function is by itself a native semilinear CM/divided-power Frobenius operator.

There is a *conditional* comparison criterion on a **rank-one \(\mathbb F_{p^2}\)-module**, not an assertion that native H0/B0 has that rank. For \(\alpha\in\mathbb F_{p^2}^{\times}\), define \(F_\alpha(x)=\alpha\sigma(x)\). Then \(F_\alpha^2=\operatorname N(\alpha)\operatorname{id}\). Two such semilinear operators are equivalent under a scalar basis change iff their coefficients have equal norm: if \(e'=z e\), the coefficient transforms to \(\alpha'=\alpha\,\sigma(z)/z\), which preserves norm; conversely \(\operatorname N(\alpha'/\alpha)=1\), and the norm-one group (order p+1) equals the image of \(z\mapsto\sigma(z)/z=z^{p-1}\) from \(\mathbb F_{p^2}^{\times}\). This proves sufficiency without assuming a new axiom. A source-fixed normalization factor \(\eta\) changes the invariant by \(\operatorname N(\eta)\); absent an authenticated native basis, semilinear direction, and normalization, no numerical equality with the native Frobenius square may be asserted.

Whenever \(p\mid A_p(u)\) is established for a stated prime, put \(\alpha=A_p(u)/p\bmod p\). This alpha is an *ordinary Hesse candidate carrier*. Its norm is a rigorous test datum if a later independently sourced comparison actually identifies it with a normalized native rank-one coefficient. That identification has **not** been obtained.

## Exact p=373 witness and bounded author arithmetic

For p=373, p³=51,895,117, direct factorial coefficient recurrence and arithmetic in \(R_3\) give
\[
A_{373}(u)\equiv34\,338\,380+8\,126\,924 T\pmod{51\,895\,117}.
\]
Here \(G\bmod p=0\), \(G/p\bmod p=302\), \(v=(8\,126\,924/373)\bmod373=154\), \(\Phi\bmod373=4v=243\), consistent with the **earlier** independently source-recorded Phi witness. New derived data:
\[
\operatorname N(A)\equiv18\,225\,899\pmod{51\,895\,117},\quad
\frac{\operatorname N(A)-G^2}{373^2}\equiv312\pmod{373},
\]
\[
\boxed{\frac{\operatorname{Tr}(A)^2-4\operatorname N(A)}{373^2}\equiv244\ne0\pmod{373};\qquad
\operatorname N(\alpha)=302^2-2(154)^2\equiv131\ne0\pmod{373}.}
\]
The previous separate derivative-even observation \(E_{373}=0\) and Green odd integral \(T_{\rm odd}(1/8)=173\ne0\) are **consumed**, not recredited. The nonzero norm/discriminant witness is a distinct arithmetic observation: vanishing of that derivative-even observer does not collapse the two conjugate source ports. Also \(q_{373}(2)\equiv204\bmod373\), so \(T^{373}\equiv101082T\bmod139129\), while \(\sigma(T)=-T\); and \(A_{373}(u)^{373}\equiv0\bmod373^2\), despite \(\sigma(A_{373}(u))\ne0\bmod373^2\). This directly excludes equating naive p-th power with this second-digit coefficient-ring involution.

Using exact integers (no floating point), eight sample primes were checked against the direct factorial polynomial and the independent trace/norm algebra:

| p | G/p mod p | v=b/p mod p | N(alpha) mod p | (N(A)-G²)/p² mod p | discr/p² mod p |
|--:|--:|--:|--:|--:|--:|
| 13 | 7 | 6 | 3 | 6 | 2 |
| 19 | 8 | 11 | 12 | 5 | 18 |
| 37 | 15 | 36 | 1 | 35 | 8 |
| 43 | 8 | 41 | 13 | 35 | 32 |
| 61 | 36 | 35 | 5 | 51 | 40 |
| 67 | 6 | 10 | 37 | 1 | 63 |
| 211 | 154 | 209 | 76 | 203 | 32 |
| 373 | 302 | 154 | 131 | 312 | 244 |

For all eight **tested primes** G mod p=0; this finite observation is not promoted here to a theorem about every p in the congruence classes. The general trace/norm and Frobenius-lift identities above are proved algebraically, independently of these finite tests. The rank-one criterion uses standard finite-field group theory; it is conditional as a native CM interpretation. All checks are author-run; no independent review or Lean/native CM experiment has occurred.

Reproducible exact check (Python 3.8+, p from the fixed eight-prime list):

~~~python
def one(p):
    assert p >= 13 and p % 24 in (13, 19)
    n, mod = (p - 1) // 3, p**3
    def mul(x, y):
        return ((x[0]*y[0]+2*x[1]*y[1])%mod,
                (x[0]*y[1]+x[1]*y[0])%mod)
    inv4 = pow(4, -1, mod)
    u = (2*inv4%mod, -inv4%mod)
    coeff, power, val = 1, (1, 0), (0, 0)
    for k in range(n+1):
        val = ((val[0]+coeff*power[0])%mod,
               (val[1]+coeff*power[1])%mod)
        if k < n:
            coeff = (coeff*(3*k+1)*(3*k+2)*(3*k+3)
                     *pow(27*(k+1)**3,-1,mod))%mod
            power = mul(power,u)
    a,b = val
    assert a%p==0 and b%p==0  # asserted ONLY for listed checked primes
    v=b//p%p
    norm=(a*a-2*b*b)%mod
    gap=(norm-a*a)%mod
    d=(4*a*a-4*norm)%mod
    assert gap%(p*p)==0 and d%(p*p)==0
    assert gap//(p*p)%p==(-2*v*v)%p
    assert d//(p*p)%p==(8*v*v)%p
    return p,a//p%p,v,norm//(p*p)%p,gap//(p*p)%p,d//(p*p)%p

for p in (13,19,37,43,61,67,211,373):
    print(one(p))
~~~

## Source separation and next real scientific test

BRC typed carrier/provenance: (p, original labeled A/B ports, u/sigma(u), Y=1/8, coefficient ring R_3, G, Phi, valuation, Tr, Norm, discriminant, conditional semilinear coefficient). The involution is the verified **ordinary quadratic coefficient** involution; it is not silently a native H0/B0 divided-power Frobenius, its scalar normalization or the original κ. In particular, the rank-one classification cannot be imposed on an unverified rank-two native structure.

The earliest unresolved mother-target unit remains: authenticate the original-class fixed H0/B0 divided-power representative, actual \([X]U\bmod p^2\), Frobenius direction, and native normalization; only then test the *conditional* necessary square invariant against any proposed ordinary Hesse coefficient map and the genuine \(\omega+6\nabla_\lambda\omega\), κ and \(\Delta_p-R_p\) readouts. If the native rank or coefficient identification differs, retype the comparison rather than forcing 131. This portable note is not a native Source checkpoint, Result, review, CM experiment, or D25/LIFT proof. Preserve Source's inherited completed units, already reviewed work, and current Task owner; D25/LIFT remains OPEN.
