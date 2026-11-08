# D25 — Universal W216/V2304 complementary-unit reciprocity and a common cubic kernel

Date: 2026-11-09 (Asia/Hong_Kong). Classification: **TASK_RESEARCH / AUTHOR_SIDE_ALL_PRIME_PROOF / EXACT_23_PRIME_REGRESSION / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE**.

Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, publication \`TP2-B6F4FC938FF94941C1B7\`, immutable science pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. Research logical lane \`chatgpt-research-onhour-enterprise-math-20260923\` only. This is an author-side extension of the same-run initial W grade-1/grade-2 reflected-unit theorem, not a repeated proof of the inherited first-jet or native experiment.

## 1. Two exact original sequences

For every prime \(p>3\), put

\[
A_n=\frac{(2n)!(3n)!}{(n!)^5 216^n}
=\frac{\binom{2n}{n}^2\binom{3n}{n}}{216^n},\qquad
C_n=\frac{(4n)!}{(n!)^4 2304^n}
=\frac{\binom{4n}{2n}\binom{2n}{n}^2}{2304^n}.
\]

The frozen weighted sums use \((6n+1)A_n\) and \((8n+1)C_n\); **the theorem below is about the source-labelled unweighted coefficient units**, which are needed for but not identical to the signed sum observer.

For \(1\le q<p\), set

\[
i=\lfloor2q/p\rfloor,\qquad j=\lfloor3q/p\rfloor,\qquad
k=\lfloor4q/p\rfloor.
\]

Since \(q<p\), the exact valuations are

\[
v_p(A_q)=i+j,\quad v_p(A_{p-q})=3-i-j,\qquad
v_p(C_q)=k,\quad v_p(C_{p-q})=3-k.\tag{U0}
\]

Thus every complementary pair has **total valuation exactly three in either original model**, with no exception for \(1\le q<p\).

Define normalized leading units modulo \(p\):

\[
\mathcal A_q=A_q/p^{i+j},\quad
\mathcal A_{p-q}=A_{p-q}/p^{3-i-j},\quad
\mathcal C_q=C_q/p^k,\quad
\mathcal C_{p-q}=C_{p-q}/p^{3-k}.
\]

## 2. Universal reciprocal pair laws

**Theorem (both original models, every prime p>3):**

\[
\boxed{\mathcal A_q\mathcal A_{p-q}\equiv
\frac{(-1)^{i+j+1}j!(2-j)!}{36q^3}\pmod p,}\tag{U1}
\]

\[
\boxed{\mathcal C_q\mathcal C_{p-q}\equiv
\frac{(-1)^{k+1}k!(3-k)!}{576q^3}\pmod p.}\tag{U2}
\]

Therefore their normalized pair-product ratio has **no dependence on q except its finite valuation stratum**:

\[
\boxed{
\frac{\mathcal A_q\mathcal A_{p-q}}
{\mathcal C_q\mathcal C_{p-q}}
\equiv 16(-1)^{i+j-k}
\frac{j!(2-j)!}{k!(3-k)!}\pmod p.}\tag{U3}
\]

As \(q\) traverses the six open rational intervals separated by \(p/4,p/3,p/2,2p/3,3p/4\), the exact ratio is

| \(q\) interval | \(0<q<p/4\) | \(p/4<q<p/3\) | \(p/3<q<p/2\) | \(p/2<q<2p/3\) | \(2p/3<q<3p/4\) | \(3p/4<q<p\) |
|---|---:|---:|---:|---:|---:|---:|
| \((\mathcal A_q\mathcal A_{p-q})/(\mathcal C_q\mathcal C_{p-q})\) | \(16/3\) | \(-16\) | \(8\) | \(8\) | \(-16\) | \(16/3\) |

No endpoint ambiguity occurs, since \(p>3\) is coprime to 12. Thus W216 and V2304 share a universal \(q^{-3}\) complementary-pair kernel; only *six exact stratum multipliers* differ. This is an exact common structural interface for the two distinct coefficient models.

### Complete algebraic proof

For \(0\le s\le3<p\) and \(0<r<p\), the factorial block unit identity is

\[
\frac{(sp+r)!}{p^s}\equiv(-1)^s\,s!\,r!\pmod p.\tag{F}
\]

Indeed remove the factors \(p,2p,\ldots,sp\), apply Wilson to each full nonmultiple block, and reduce the terminal incomplete block modulo \(p\).

Also \(r!(p-r)!\equiv(-1)^r r\pmod p\). Writing the pair numerator for W as

\[
(2q)!(2p-2q)!\ \times\ (3q)!(3p-3q)!,
\]

and using (F) with respective block counts \((i,1-i)\) and \((j,2-j)\), the normalized factorial-pair products become

\[
\frac{(2q)!(2p-2q)!}{p}
\equiv(-1)^{i+1}2q,
\]

\[
\frac{(3q)!(3p-3q)!}{p^2}
\equiv(-1)^{q+j}j!(2-j)!\,3q.
\]

The denominator \([q!(p-q)!]^5 216^p\) is congruent to
\((-1)^q q^5\,216\) modulo \(p\). Division gives (U1).

For V, the two numerator arguments add to \(4p\), with block counts \(k\) and \(3-k\), remainders \(r=4q-kp\) and \(p-r\). Their normalized product is

\[
(-1)^3 k!(3-k)!\,r!(p-r)!
\equiv(-1)^{k+1}k!(3-k)!\,4q\pmod p.
\]

The denominator \([q!(p-q)!]^4 2304^p\equiv q^4 2304\pmod p\).
Division gives (U2). Taking the ratio gives (U3), and direct evaluation on the six intervals yields the table. All divisions are by p-units.

## 3. Exact, independent finite regression

The attached executable standard-library Python verifier computes the *original integer binomial coefficients* modulo the exact power \(p^{v+1}\), divides by the exact valuation \(p^v\), and checks both RHS values for **every** \(q=1,\ldots,p-1\) over 23 primes

\[
5,7,11,13,17,19,23,29,31,37,43,61,67,73,97,109,127,157,163,193,211,229,373.
\]

Coverage: **2,072 complementary index pairs**, or **4,144 separate W/V exact leading-unit product checks**; all passed. This verifies the implementation and representative samples, not a general proof (which is the factorial argument above).

At \(p=373\): for \(q=125\in(p/3,p/2)\), the W and V normalized pair products are \(105\) and \(153\) respectively, so \(105/153\equiv8\pmod{373}\), the exact middle-strip constant. At \(q=94\in(p/4,p/3)\) the ratio is \(-16\equiv357\pmod{373}\). At \(q=1\) it is \(16/3\equiv254\pmod{373}\). The previously proven grade-1 ↔ grade-2 W mirror law is the \(p/3<q<p/2\) subcase of (U1).

## 4. Relevance and remaining exact experiment

This is a *source-preserving BRC companion-pair carrier*: each record retains model W/V, index \(q,p-q\), its exact valuation grade and unit coefficient. Complementary product has a common \(q^{-3}\) observer with a six-region repair coordinate; replacing the signed sums by products would discard the intended additive cancellation, so **no W-V supercongruence is inferred from (U3) alone**.

Next scientific action: construct an additive/derivative (first-jet) transport compatible with this six-strip \(q^{-3}\) kernel and the original signed weight and truncation. A proposed telescoping identity must recover \(B_p\), the grade-1 harmonic jet and the grade-2 inverse mirror together; compare the two original models rather than requiring each stratum to vanish independently.

The hard native requirement remains **#1559**: same-original-class \(p=373\) H0/B0 divided-power \([X]U\bmod139129\), actual rank, semilinear Frobenius direction/eta, signed Green/Hesse kappa, original Delta-R and independent reproduction. That experiment is **NOT_EXECUTED / PENDING_OWNER**. This theorem does not substitute for it or create Source, Researcher CLAIM, Result, review or Foundation authority.

Status: **AUTHOR_SIDE_PROOF / EXACT_4144_CHECKS / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE**. Frozen pin, accepted D24 RR/DR and P000 unchanged.
