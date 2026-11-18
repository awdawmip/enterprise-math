# R762EW — Exact all-trit Frobenius discrepancy and third-trit BRC repair

Scientific date: 2026-11-18. Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS, immutable TP2-8B7E13C5904A2D6F1142. Frozen scientific sources, P000 and ACTIVE worldview unchanged. This is **positive six-named-branch full-three-coordinate BRC terminal arithmetic**. No signed native Cell/Link/Port event licence is claimed. Author-side proof and exact checks, independent review NOT_REVIEWED.

## Model and previously saved input

Let \(q=3^a\), \(a\ge1\), \(Q=3q\), and \(R_Q=\mathbb Z[(\mathbb Z/Q\mathbb Z)^3]\). All coordinates \(X,Y,Z\) are retained. Six named positive BRC branches give
\[
P_Q=1+X+Z+XY+YZ+XYZ.
\]
The injective group-ring map \(\iota:R_q\hookrightarrow R_Q\) cubes the three coordinate generators. Define
\[
 A=\iota(P_q)=1+X^3+Z^3+(XY)^3+(YZ)^3+(XYZ)^3,
 \qquad D=(P_Q^3-A)/3\in R_Q.
\]
R762EV ([PR #2746](https://github.com/awdawmip/enterprise-math/pull/2746)) established the integral six-named-branch identity \(P_Q^3=A+3D\), with 30 ordered repeated-pair types, 20 triple-distinct types and augmentation \(\epsilon(D)=70\). This work extends its second-trit congruence to arbitrarily many trits, and derives the exact third-trit correction.

## Theorem 1: exact all-trit valuation, sharp for every short-range block

For every integer \(m\ge1\), put \(\Delta_m=P_Q^{3m}-A^m\) and \(r=v_3(m)\). Then
\[
\boxed{ \Delta_m\in3^{r+1}R_Q\quad \text{for every }m\ge1. }
\]
For **every** \(1\le m<q\), the coefficient of \(X\), with Y and Z endpoints both zero, is
\[
\boxed{[X]\Delta_m=3m.}
\]
Consequently, writing \(\operatorname{content}(\Delta_m)\) for the positive gcd of its integer terminal coefficients,
\[
\boxed{v_3(\operatorname{content}(\Delta_m))=1+v_3(m)
       \qquad(1\le m<q).}
\]
Equivalently, for every \(h\ge1\) and every \(1\le m<q\),
\[
\boxed{P_Q^{3m}\equiv\iota(P_q^m)\pmod{3^h}
  \iff 3^{h-1}\mid m.}
\]
The \(h=2\) case recovers the R762EV exact mod-9 criterion; \(h=3\) yields the sharp mod-27 criterion \(9\mid m\). The stated quantifiers hold for every \(q=3^a\), \(a\ge1\).

### Proof

The exact commutative group-ring binomial expansion is
\[
\Delta_m=\sum_{j=1}^m 3^j\binom mj A^{m-j}D^j .
\]
The integer relation \(j\binom mj=m\binom{m-1}{j-1}\) implies
\[
v_3\binom mj\ge v_3(m)-v_3(j).
\]
Thus for every \(1\le j\le m\),
\[
v_3\left(3^j\binom mj\right)
\ge v_3(m)+j-v_3(j)\ge v_3(m)+1 .
\]
Because A and D have integral coefficients, this establishes the uniform divisibility without an upper bound on m.

Now let \(1\le m<q\). A path of \(3m\) named branches has each coordinate increment between 0 and \(3m<Q\), so none of its three terminal coordinates can wrap. Reaching (1,0,0) forces all branches to be identity or X and exactly one to be X. Its position has \(3m\) choices, so \([X]P_Q^{3m}=3m\). Every exponent in \(A^m\) has X-coordinate a multiple of 3 before wrap; hence \([X]A^m=0\). Therefore \([X]\Delta_m=3m\), exactly realizing the universal lower bound on 3-divisibility. The gcd statement and modular equivalence follow. QED.

## Theorem 2: universal third-trit correction and sharp truncation

For every \(m\ge0\) and \(r\in\{0,1,2\}\), in \(R_Q/27R_Q\),
\[
\boxed{
P_Q^{3m+r}\equiv
\left(A^m+3mA^{m-1}D+
9\binom m2 A^{m-2}D^2\right)P_Q^r\pmod{27}.}
\]
Omit terms with negative powers (equivalently, include a j-term only when \(j\le m\)).

For every \(1\le m<q\), the first-order truncation is valid modulo 27 precisely when \(m\equiv0,1\pmod3\):
\[
\boxed{P_Q^{3m}\equiv A^m+3mA^{m-1}D\pmod{27}
\iff m\not\equiv2\pmod3 .}
\]
The third-trit correction is indispensable whenever \(m\equiv2\pmod3\); the endpoint (2,0,0) supplies the exact coefficient witness
\[
\boxed{[X^2]\left(P_Q^{3m}-A^m-3mA^{m-1}D\right)
  =9\binom m2,\quad 1\le m<q.}
\]

### Proof

Expansion of \((A+3D)^m\) modulo 27 retains exactly \(j=0,1,2\); all \(j\ge3\) terms carry \(3^3\). Multiply by \(P_Q^r\). If \(m\equiv0,1\pmod3\), then \(3\mid\binom m2\), so the quadratic term vanishes modulo 27.

When \(m<q\), the no-wrap bound \(3m<Q\) applies. A path ending at (2,0,0) has exactly two X branches and all others identities, hence \([X^2]P_Q^{3m}=\binom{3m}{2}\). Every \(A^m\) monomial has X-coordinate a multiple of 3, so \([X^2]A^m=0\). In the exact cubic \(D=(P^3-A)/3\), \([X^2]D=1\), and \([X^2]A^{m-1}D=1\) (the A factor can only use identity branches). Subtraction gives \(\binom{3m}{2}-3m=9\binom m2\). When \(m\equiv2\pmod3\), this is 9 modulo 27. QED.

## Verification and exact arithmetic semantics

Companion author script R762EW_VERIFY.py uses only the six named BRC integer shift operators on the complete three-coordinate terminal group; numpy.int64 is used solely for exact modular integer arrays, with reduction after each step and no float operations. For \(q=9,Q=27\), it constructs \(P_Q^3\) before reduction, confirms integral D with 38 nonzero cells and augmentation 70, and calculates \(D^2\bmod27\) (201 support cells). It verifies 27 whole-vector third-trit identities for all \(m=0,\ldots,8\), \(r=0,1,2\), totaling **531,441 exact terminal coefficient comparisons**; tests the first-order iff and the (2,0,0) witnesses. A separate block at \(q=27,Q=81\) checks \(m=1,\ldots,9\) modulo 81, including the sharp valuation at \(m=9\). Results: PASS. Symbolic proofs establish the quantified statements; these finite checks validate the implementations. Independent review NOT_REVIEWED; formal checker NOT_PERFORMED.

## Next research question

For arbitrary \(h\ge1\), the polynomial \((A+3D)^m\) truncated at \(j=h-1\) suffices modulo \(3^h\); the sharp all-trit theorem tells exactly when **all** correction terms vanish for \(m<q\). The open task is to integrate this jet with the previously established normalized content \(3^{-f_q(n)}P_q^n\), calculate a minimal observer-specific future-operation horizon, and preserve original branch and signed Port provenance before any native X6 transfer. Signed TRIADIC_CLOSURE_E Cell/Link/Port licence and V17/V29/V39 transport remain independent unresolved tasks.