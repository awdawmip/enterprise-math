# D25 — Original E3 at p=373: exhaustive geometric Frobenius sign calibration

Date: 2026-11-08 (Asia/Hong_Kong). **AUTHOR-SIDE EXACT FINITE-OBJECT CERTIFICATE / EXECUTED / UNREVIEWED / NOT_ADMITTED / NOT H0-B0**.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; **unchanged frozen scientific pin** enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3. This is a new exhaustive check for the original target prime p=373, rather than the previously published general CM sign argument or previous exhaustive tests at p=13,19.

## Exact original object and observer

Use the **original, non-twisted** E3 elliptic curve
\[
E_3:\ y^2+xy+cy=x^3,\qquad c=(2-T)/108
\]
over \(k=\mathbb F_{373}[T]/(T^2-2)\), where \((2/373)=-1\), \(q=373^2=139129\), and \(c=76+335T\). The observed quantity is the actual finite-field geometric \(q\)-Frobenius trace \(t_q=q+1-\#E_3(k)\), **not** the auxiliary Hesse norm, a rank-one semilinear model, or the missing native divided-power \([X]U\).

For every \(x=a+bT\), the quadratic equation in \(y\) has discriminant
\[
D(x)=(x+c)^2+4x^3=D_0+D_1T
\]
where, writing \(c=c_0+c_1T\),
\[
D_0=(a+c_0)^2+2(b+c_1)^2+4(a^3+6ab^2)\pmod p,
\]
\[
D_1=2(a+c_0)(b+c_1)+4(3a^2b+2b^3)\pmod p.
\]
The number of affine \(y\)-solutions equals \(1+\chi_{k}(D(x))\), with the convention \(\chi_k(0)=0\). Because \(k/\mathbb F_p\) is quadratic,
\[
\chi_k(D)=\chi_p(N(D)),\quad N(D)=D_0^2-2D_1^2\in\mathbb F_p.
\]
This last identity follows by raising \(N(D)=D^{p+1}\) to \((p-1)/2\), which yields \(D^{(p^2-1)/2}\).

## Exhaustive p=373 computation and certificate

Two different exact tests were performed for **every one of all 139129** \(x\in k\):
(A) the Legendre character of the norm in \(\mathbb F_{373}\);
(B) membership of the discriminant \(D(x)\) in an independently constructed set of all \(q\) squares \(z^2\), including 0. The two agree for every \(x\); all arithmetic is integer modular arithmetic.

| Original-class observation | Exact computed result |
|---|---:|
| \(|k|\) | 139129 |
| Number of distinct squares in \(k\), including zero | 69565 |
| \(D(x)=0\) | 3 |
| \(D(x)\ne0\), quadratic residue | 69190 |
| \(D(x)\) nonresidue | 69936 |
| \(\sum_{x\in k}\chi_k(D(x))\) | **-746** |
| \(\#E_3(k)=1+q+\sum\chi_k(D(x))\) | **138384 = 372²** |
| \(t_q=q+1-\#E_3(k)\) | **+746 = 2·373** |
| q-Frobenius characteristic polynomial | **\(X^2-746X+139129=(X-373)^2\)** |

The three roots of \(D(x)=0\), written \(x=a+bT\), are
\[
(17,245),\quad(31,228),\quad(45,273).
\]
Their associated points of order two have \(y=-(x+c)/2\); for these \(x\) the corresponding \(y\) pairs are respectively \((140,83),(133,278),(126,69)\). The original \(E_3\) also has the evident order-three flex \(P=(0,0)\), whose tangent is \(y=0\).

**Finite-object theorem (p=373 only):** The original curve has
\[
\boxed{\#E_3(\mathbb F_{373^2})=138384,\quad t_{373^2}=+746,\quad \pi_{373^2}=[+373].}
\]
Proof: The displayed complete finite enumeration proves the point count; for any elliptic curve over \(\mathbb F_q\), Frobenius satisfies \(\pi_q^2-[t_q]\pi_q+[q]=0\) in its endomorphism ring. Here this becomes \((\pi_q-[373])^2=0\). An elliptic curve's endomorphism ring has no nonzero zero-divisors (every nonzero endomorphism is an isogeny), so \(\pi_q=[373]\). This is a proof for this specific finite-field curve, not a bounded-prime sample promoted to a universal theorem.

As regression controls, the **same exact executed algorithm** gives p=13: \(\#E_3(\mathbb F_{13^2})=144\), trace +26; p=19: \(\#E_3(\mathbb F_{19^2})=324\), trace +38, agreeing with the earlier separately recorded small-fiber counts.

## Consequence for the real native benchmark, with precise type boundary

For any actually authenticated realization of the **same original curve** on which the native Frobenius square is identified with the geometric q-Frobenius action on \(H^1_{\rm cris}(E_3)\), its normalized second iterate must act as \([+373]^*\), i.e. \(+373\) times the identity on that cohomology (orientation/convention and comparison map to the stated H0/B0 module must be supplied). An auxiliary semilinear matrix whose square is \(-373I\) cannot become this \(+373I\) by a pure semilinear basis change because \(C^{-1}M\sigma(C)\) squares to \(C^{-1}M\sigma(M)C\). This is a **specific, newly independently counted geometric sign oracle** for the authentic p=373 original-class comparison.

The native benchmark required by issue #1559 remains **NOT_EXECUTED / PENDING_OWNER**: the actual fixed H0/B0 divided-power representative, \([X]U\bmod 139129\), actual module rank, Frobenius direction and normalization \(\eta\), the signed odd Green/Hesse \(\kappa\), original \(\Delta_{373}-R_{373}\) readout and an independent native reproducer. The finite-field geometric point count does not produce or replace those measurements. Do not impose a rank-one interpretation or an identification with a rank-two crystalline module without the actual native map. The earlier source-aligned scalar port gave \(\Delta_{373}=R_{373}=196\) **author-side**, with its own provenance; this experiment neither alters nor recredits that result.

## Reproduction / source preservation / next action

Actual executed standard-Python source: research_notes/portable_direct/d25_p373_original_e3_geometric_frobenius_exact_20261108.py. It exhaustively enumerates all field elements, independently evaluates character via norm and explicit square image, checks every root count, records the three zero-discriminant roots and cross-regresses p=13,19. There is no floating-point arithmetic, probabilistic sampling, model substitution, formal proof assistant, or native divided-power compute.

BRC signed carrier: (original E3 model, p, coordinate field k, x=a+bT, discriminant D, norm Legendre readout, square-membership readout, q-Frobenius trace). The two equivalent character observers may be safely combined for this point-count objective; they are not a substitute for the future signed H0/B0 operator and odd-branch observer. External two-coordinate field notation is not a complete native X6 slice; the P000/ACTIVE worldview remains unchanged.

Source control: previously read exact control request onhour11-20261106-1400-exact-research-lane-continuation returned SUCCEEDED for a **read-only continuation**, not an own session/claim. This author artifact is not a Source result, Task claim, activity registration, checkpoint or independent review. Research logical lane label chatgpt-research-onhour-enterprise-math-20260923 remains separated from maintenance chatgpt-hourly-enterprise-math-20260921; actual Site Researcher authority is not granted on the present client. Retain the original request, frozen scientific pin and any legitimate prior owner. Do not create a duplicate CLAIM.

**Next exact action:** authorized original-class #1559 executor must obtain and compute the genuine p373 H0/B0 \([X]U\) and Frobenius matrix/normalization, compare its actual geometric sign against the independently enumerated \(\pi_q=[373]\) only after supplying the cohomology comparison, and check signed \(\kappa\) and \(\Delta-R\). If such a native execution cannot be completed, keep #1559 PENDING_OWNER; portable C4 remains an unproved route distinct from native admission.
