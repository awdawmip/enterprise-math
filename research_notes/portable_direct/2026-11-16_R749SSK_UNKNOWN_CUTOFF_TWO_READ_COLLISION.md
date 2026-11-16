# R749SSK — Exact unknown-cutoff collisions for the smoothed two-read source observer

Date: 2026-11-16. Scientific status: AUTHOR_EXACT_NOT_REVIEWED. Independent portable algebraic research, not a native X6 or BRC promotion.

Frozen science: five distinct labeled positive sources with weights (1,1,2,3,6), the first weight-one source marked. Preserve predecessor scientific pin a72226e2430ffa4786321ac86e7f0c599d5f0389 (R749SSJ, PR #2563, commit 495a7a59c5e3f91c9177c68a4f7659fd3fbd3b95). No shared X6 CLAIM is asserted.

## Model, question and theorem

For integer q >= 6, set

\[
\Omega_q=\{k\in\mathbb Z_{\ge0}^5:k_1+k_2+2k_3+3k_4+6k_5\le q-1\},\quad
C_q=|\Omega_q|,\qquad T_q=\sum_{k\in\Omega_q} k_1.
\]

For one real calibration pair (e,d) in [-2,2]^2, *shared by both observations*, define

\[
X_q(e,d)=\frac{T_q+e}{C_q+d},\quad
S(q)=18q^4+54q^3-345q^2+2070q-16315,
\quad Y_q(e,d)=q^3 X_q(e,d)-\frac{S(q)}{108},
\]

and \(F_q(e,d)=(Y_q(e,d),Y_{q+6}(e,d))\).

Predecessor R749SSJ proved that for a known q the two-read map F_q uniquely determines the real calibration pair. We determine whether it determines *unknown* q.

**Theorem A (exact non-identifiability and open overlap).** There exist distinct cutoffs q=6 and p=7 and interior admissible errors satisfying \(F_6(e,d)=F_7(e',d')\). Moreover \(F_6((-2,2)^2)\cap F_7((-2,2)^2)\) contains a nonempty open subset of \(\mathbb R^2\). Therefore even exact two-read smoothed observations do not universally recover an unknown cutoff when calibration errors are real.

**Theorem B (fixed known denominator bias).** Even if the common denominator error is externally fixed to the known integer d=-1, two admissible real numerator errors at q=6 and p=8 produce exactly the same two-read smoothed observation.

**Theorem C (these two particular collisions are resolved by a third read).** The next six-step observations differ by the two strictly positive fractions calculated below; this is a local separation result, not a universal three-read injectivity theorem.

## Proof of Theorem A: exact rational interior witness

Source-count anchors, independently derivable from the five labeled weights, are:

| q | C_q | T_q |
|---:|---:|---:|
| 6 | 41 | 50 |
| 7 | 65 | 91 |
| 12 | 380 | 881 |
| 13 | 506 | 1261 |

The zero-error state at q=6 has

\[
F_6(0,0)=\left(\frac{400643}{4428},\frac{690461}{10260}\right).
\]

At p=7 choose the exact rational pair

\[
e'=\frac{445301541473}{452834122344},\qquad
d'=-\frac{16718273227}{37736176862}.
\]

Strictly \(0<e'<1\) and \(-1<d'<0\), so both states are interior. Exact rational substitution proves

\[
\boxed{F_6(0,0)=F_7(e',d').}
\]

For a fully reconstructive derivation, given output (y0,y1) and candidate p, let

\[
x_0=\frac{y_0+S(p)/108}{p^3},\quad
x_1=\frac{y_1+S(p+6)/108}{(p+6)^3}.
\]

Solving the two count equations gives

\[
d'=\frac{T_{p+6}-T_p-x_1 C_{p+6}+x_0 C_p}{x_1-x_0},
\qquad e'=x_0(C_p+d')-T_p.
\]

With the displayed F_6 data and p=7 this yields the above reduced fractions exactly.

For any q, let A=C_q+d and B=C_{q+6}+d. Both are positive. Direct differentiation of the *explicit real observer chart* yields

\[
\det D F_q(e,d)
=\frac{q^3(q+6)^3}{AB}\bigl(X_q(e,d)-X_{q+6}(e,d)\bigr).
\]

R749SSJ proves \(X_{q+6}(e,d)-X_q(e,d)>1\) for all stated q,e,d, so both Jacobians at our interior preimages are nonzero. The inverse-function theorem gives open output neighborhoods inside both images; their intersection is open and nonempty. This proves robust (positive-area) ambiguity in the real calibration chart. It does not alter P000's discrete native-space premise.

## Proof of Theorem B: known d=-1

Further count anchors are \( (C_8,T_8)=(98,156)\) and \((C_{14},T_{14})=(662,1767)\). Take

\[
e_6=-\frac{96083110}{75133251},\qquad
e_8=\frac{20416063}{33392556}.
\]

Both satisfy \(-2<e_6,e_8<2\), and direct exact substitution gives

\[
\boxed{F_6(e_6,-1)=F_8(e_8,-1)=
\left(\frac{9031928401}{100177668},
\frac{7216422841}{100177668}\right).}
\]

To reproduce the construction, use the linearity
\(Y_q(e,-1)=Y_q(0,-1)+q^3e/(C_q-1)\).
The two equal-reading equations for q=6 versus p=8 form a nonsingular 2-by-2 rational linear system for (e_6,e_8). Its unique solution is exactly the displayed pair. This example fixes the same known denominator error under both competing hypotheses.

## Proof of Theorem C and new frontier

For the Theorem A collision, the next observations at q+12 and p+12 differ by

\[
Y_{18}(0,0)-Y_{19}(e',d')
=\frac{2499325179139188767}{1219962360222318330}>0.
\]

For Theorem B,

\[
Y_{18}(e_6,-1)-Y_{20}(e_8,-1)
=\frac{321813705516}{162895381165}>0.
\]

Thus the third observer separates these *specified states*. The general injectivity of a three-read sequence remains a new mathematical question.

## Exact verification, evidence and scope

Companion self-contained Python 3 file: R749SSK_UNKNOWN_CUTOFF_COLLISION_CERT.py; run it in the same directory. Its exact Fraction calculations reproduce six count anchors, both collisions, all strict interior bounds, two nonzero Jacobians and both third-read gaps. The companion JSON result is R749SSK_UNKNOWN_CUTOFF_COLLISION_RESULTS.json with status PASS.

The source count recurrence initializes a[0]=1; loops over *each of the five labeled* weights w=(1,1,2,3,6) with ascending updates a[n]+=a[n-w]. This counts exact weighted sums. Then \(C_q=\sum_{n<q}a[n]\) and \(T_q=\sum_{j=1}^{q-1}C_j\), the latter from marking the first weight-one source. All displayed fractions are rational identities; open-overlap requires the cited known-q six-shift theorem and the standard inverse-function theorem.

**Verification boundary:** exact two constructed coincidences and their third-read differences; no infinite enumeration and no universal three-read result. Math author proof and reproducible computation, pending independent mathematical review. An integer-only error model is strictly smaller than the continuous square and remains separately unresolved at unbounded q.

**Enterprise Math interpretation:** the smooth two-read projection is not observer-safe for forgetting the cutoff/provenance label on the stated real-error domain. Retain labeled source identity, common-error relation and ordered six-step observations; do not infer native X6 Cell/Port/BRC dynamics from this scalar calculation. Next: classify intersections of three-read image surfaces and ask for an exact, typed future-observer fiber criterion. Separately, address the unknown-cutoff bounded-integer-error case.
