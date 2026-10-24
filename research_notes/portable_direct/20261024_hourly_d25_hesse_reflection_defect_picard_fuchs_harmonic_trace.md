# D25/LIFT — exact inhomogeneous Picard–Fuchs certificate for the Hesse reflection defect

2026-10-24 · portable TASK_RESEARCH author derivation · **UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT**.

**Scope and provenance.** Parent task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, publication \`TP2-B6F4FC938FF94941C1B7\`; immutable scientific Source pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\` is unchanged. Research logical conversation \`chatgpt-research-hourly-enterprise-math-20260923\` (not maintenance). This is an independently checkable **ordinary Hesse coefficient-polynomial theorem**, not a claim to current winning CLAIM/open/run, native CM \`[X]U\`, mathematical admission, or original LIFT completion.

**Consumed inputs, not re-credited:** the accepted CM0/SIMPLE Legendre/Hesse congruence from the frozen parent; the norm-2 Hesse parameter construction at [\`d921541f\`](https://github.com/awdawmip/enterprise-math/blob/d921541fdc3bb38201d72ba302922769fc837143/research_notes/portable_direct/20261024_hourly_d25_inert_hesse_norm2_frobenius_branch_collision_p2.md); and the all-target reflection-defect integrality at [\`238626c2\`](https://github.com/awdawmip/enterprise-math/blob/238626c2bb75a51b843c3cb3e1af56c60a30e530/research_notes/portable_direct/20261024_hourly_d25_hesse_polynomial_reflection_defect_first_digit_bridge.md). The **new mathematical unit** here is an exact inhomogeneous differential-operator equation, its Hesse-coordinate pullback, and an explicit **base-field finite-harmonic formula** for the second-digit scalar, verified by a separate implementation.

## 1. Exact rational differential-operator theorem (not only mod p)

Let \`p=6m+1 >=13\` be a prime, \`n=(p-1)/3=2m\`, and work over \`Z_(p)[X]\`. Put

\[
c_k=\frac{(3k)!}{27^k(k!)^3}=\frac{(1/3)_k(2/3)_k}{(k!)^2},\quad
A(X)=\sum_{k=0}^n c_k X^k,\quad
P(X)=P_n(1-2X)={}_2F_1(-n,n+1;1;X).
\]

Here \`P_n\` denotes the standard Legendre polynomial. By the frozen coefficient congruence \`A(X)=P(X) (mod p)\`, the quotient \`C(X)=(A(X)-P(X))/p\` has coefficients in \`Z_(p)\`. Because \`n\` is even, \`P(1-X)=P(X)\` exactly. Define the previously established reflection defect
\[
\mathscr D(X)=\frac{A(X)-A(1-X)}{p}=C(X)-C(1-X).
\]

Define the rational hypergeometric differential operator, acting on ordinary **polynomials**, by
\[
\mathcal L=X(1-X)\frac{d^2}{dX^2}+(1-2X)\frac{d}{dX}-\frac29.
\]

**Theorem A (exact, all stated primes).**
\[
\boxed{\mathcal L A=-\frac{p(p+1)}9c_nX^n,\qquad
\mathcal L P=-\frac{p(p+1)}9P.}
\tag{1}
\]
Consequently
\[
\boxed{\mathcal L C=\frac{p+1}{9}(P-c_nX^n),}
\tag{2}
\]
and, using the exact reflection symmetry of \`P\`,
\[
\boxed{\mathcal L\mathscr D=
\frac{(p+1)c_n}{9}\big((1-X)^n-X^n\big).}
\tag{3}
\]

**Proof.** In \`X^k\`, the coefficient of \`\mathcal L A\` is
\`(k+1)^2 c_{k+1}-(k+1/3)(k+2/3)c_k\`, which vanishes for \`0<=k<n\` by the exact hypergeometric recurrence. At \`k=n\`, there is no \`c_{n+1}\`, leaving \`-(n+1/3)(n+2/3)c_n=-p(p+1)c_n/9\`. The exact Legendre equation is \`X(1-X)P''+(1-2X)P'+n(n+1)P=0\`. Since \`n(n+1)+2/9=p(p+1)/9\`, the second equation of (1) follows. Subtract and divide by \`p\` to obtain (2). The operator \`\mathcal L\` commutes with \`X\mapsto1-X\`: the sign changes in its first-derivative factor and in the argument derivative cancel. Subtract (2) at \`X\` and \`1-X\`; \`P(1-X)=P(X)\` cancels exactly, proving (3). No finite-prime fitting, Frobenius/GM assumption or approximate argument is used. QED.

**Meaning and boundary.** The antisymmetric \`p\`-lift defect obeys an explicitly forced differential equation with **only** the original terminal coefficient \`c_n\` and source exponent \`n\` on the right. The inhomogeneity is not arbitrary: it records the finite-truncation boundary, including its sign under \`X\mapsto1-X\`. This is a strictly stronger structural certificate than observing that the derivative trace is divisible by \`p\`. It **does not** assert \`\mathscr D\` is an actual crystalline/Frobenius or divided-power representative.

## 2. Exact pullback to the normalized Hesse parameter

Work in the norm-2 quadratic coefficient algebra \`R_N=(Z/p^N Z)[T]/(T^2-2)\` with \`u=(2-T)/4=\lambda^{-3}\`, \`\sigma(T)=-T\`, \`\sigma(\lambda)=2/\lambda\`, as fixed by the consumed source-parameter theorem. Let \`F(\lambda)=\mathscr D(\lambda^{-3})\`; all denominators \`3,\lambda\` are units at the stated primes.

The ordinary chain rule gives
\[
\frac{d}{dX}=-\frac{\lambda^4}{3}\frac{d}{d\lambda},\qquad
\frac{d^2}{dX^2}=
\frac{\lambda^8}{9}\frac{d^2}{d\lambda^2}
+\frac{4\lambda^7}{9}\frac{d}{d\lambda}.
\]
Substitution in (3) gives the **exact rational Hesse-coordinate inhomogeneous equation**
\[
\boxed{
(\lambda^5-\lambda^2)F''(\lambda)
+(\lambda^4+2\lambda)F'(\lambda)-2F(\lambda)
=(p+1)c_n\left[(1-\lambda^{-3})^n-\lambda^{-3n}\right].
}
\tag{4}
\]

For the *ordinary source-polynomial* second-digit even derivative \`E_p\` from the consumed reflection result,
\[
E_p=\frac{\mathscr D'(u)}2\bmod p
\quad\Rightarrow\quad
\boxed{E_p=-\frac{\lambda^4}{6}F'(\lambda)\bmod p.}
\tag{5}
\]
The coefficient-conjugation symmetry makes the last expression lie in the fixed subfield \`F_p\`. The \`d/d\lambda\` in (4)–(5) is **ordinary differentiation of this explicit polynomial pullback**, **not** a declared Gauss–Manin connection on \`\omega\` and not the original \`\kappa\` observable.

## 3. An extension-free harmonic/trace computation of the missing scalar

Let \`d_k=(-n)_k(n+1)_k/(k!)^2\` be the coefficient of \`X^k\` in \`P(X)\`. For \`0<=k<=n\`, the denominators \`3j+1,3j+2\` below are \`p\`-units, and
\[
\frac{d_k}{c_k}=
\prod_{j=0}^{k-1}\left(1-\frac p{3j+1}\right)
                         \left(1+\frac p{3j+2}\right).
\]
Define \`L_0=0\` and
\[
L_k=\sum_{j=0}^{k-1}\left(\frac1{3j+1}-\frac1{3j+2}\right).
\]
Expanding the product through its first \`p\`-digit proves **coefficientwise**
\[
\boxed{C(X)\equiv\sum_{k=0}^n c_kL_k X^k\pmod p.}
\tag{6}
\]
For \`v=\sigma(u)=1-u\`, we have \`u+v=1\`, \`uv=1/8\`. Let the *base-field trace sequence* be
\[
W_r=u^r+v^r,\qquad
W_0=2,\quad W_1=1,\quad
W_{r+2}=W_{r+1}-\frac18 W_r.
\]
Since \`\mathscr D'(u)=C'(u)+C'(v)\`, (6) yields
\[
\boxed{
E_p\equiv
\frac12\sum_{k=1}^{n}k\,c_k\,L_k\,W_{k-1}\pmod p.
}
\tag{7}
\]
Every quantity on the right lies in \`F_p\`; **no quadratic-extension arithmetic or division by an unknown Frobenius eigenvalue is needed** to compute this ordinary Hesse lift-defect port. Equations (3), (4), (7) are compatible descriptions of a single source-preserving finite polynomial; they are not three independent D25 observations.

The BRC/carrier discipline is explicit: retain \`(p,n;c_k,L_k,W_k;u,v,\sigma;\mathscr D,E_p)\`, the original upper cutoff \`n\`, the odd source/reflection branch and the derivative observer. Collapsing \`A'_p(u)\` to its first-digit \`h\` loses \`E_p\`; equation (7) restores **that** declared observer only, not native \`[X]U\bmod p^2\` or the unknown \`c_p\` product normalization. Resolution: \`COMPOSE_APPLIED\` to the existing Hesse/Legendre coefficient and reflection interface, not a new BRC family or a claim about X6 physics.

## 4. Exact computation and independent author checks

The checker independently reconstructs (i) the **direct** \`A'_p(u)\` in \`R_2\` modulo \`p^2\`, using only the factorial coefficient recurrence and pair multiplication; (ii) the extension-free formula (7) in \`F_p\`. It verifies that the scalar component of \`A'_p(u)\` is divisible by \`p\` and that its quotient equals (7). For every prime \`p<2000\` satisfying \`p mod 24 in {13,19}\`, **77/77** exact checks passed with zero mismatches. The directly computed selected residues match (7):

| p | E_p (mod p) | A'_p(u) (mod p²) as a+bT |
|---:|---:|:---|
| 13 | 10 | 130+119T |
| 19 | 16 | 304+42T |
| 37 | 26 | 962+947T |
| 43 | 1 | 43+1456T |
| 61 | 49 | 2989+2734T |
| 67 | 36 | 2412+2103T |
| 211 | 200 | 42200+16204T |

Additionally, the exact rational polynomial identities (1)–(3) were independently expanded at \`p=13,19,37,43\` and matched coefficientwise. The general theorem is the proof in §1, **not** the bounded checks. Formal proof checker NOT_RUN; native source CM/divided-power experiment NOT_RUN; independent review NOT_RUN.

Minimal reproduction for (7), with no external Python libraries:
\`\`\`python
def even_lift_scalar(p):
    n = (p - 1) // 3
    inv8 = pow(8, -1, p)
    W = [2, 1]
    for _ in range(2, n):
        W.append((W[-1] - inv8 * W[-2]) % p)
    ck = 1
    Lk = 0
    total = 0
    for k in range(1, n + 1):
        j = k - 1
        ck = ck * (3*j+1)*(3*j+2)*(3*j+3) * pow(27*k**3, -1, p) % p
        Lk = (Lk + pow(3*j+1, -1, p) - pow(3*j+2, -1, p)) % p
        total = (total + k * ck * Lk * W[k-1]) % p
    return total * pow(2, -1, p) % p

assert [even_lift_scalar(p) for p in (13,19,37,43,61,67,211)] == [10,16,26,1,49,36,200]
\`\`\`

## 5. Frontier and next strict input

**Author-proved portable additions:** exact hypergeometric boundary equations (1)–(3), their Hesse pullback (4) and derivative (5), and the p-adic harmonic/trace formula (6)–(7) with 77 finite author checks. All are **UNREVIEWED / NOT_ADMITTED** and do not advance the native Source checkpoint automatically. The certified Source checkpoint and its completed units, contribution IDs and do-not-repeat list remain byte-preserved; this note does not override them.

**Next smallest scientific unit:** inspect the actual primitive CM/divided-power \`[X]U\bmod p^2\` with fixed \`H_0/B_0\`, the authentic \`\omega+6\nabla_\lambda\omega\` representative, the native semilinear Frobenius direction and source-chosen product normalization \`c_p\`. Determine whether (4) admits a **source-proved** transport from the ordinary reflection defect to the genuine \`\kappa\` class; if not, state the precise missing comparison datum. Do not identify (4) with a GM equation merely because its coordinate is \`\lambda\`, or change the task's frozen source pin or claim that the new base-field scalar proves \`\Delta_p=R_p\bmod p\`. Parallel owner/Driver integration and an actual fresh eligible CLAIM/open remain necessary for a new native checkpoint; do not borrow any maintenance conversation.

Current status: \`UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT\`, D25/LIFT and parent Objective OPEN.
