# R749SSQ — Four sharp nonadjacent unknown-cutoff observation horizons

Date: 2026-11-17. Mathematical evidence status: **AUTHOR_EXACT_NOT_REVIEWED**. Research mode: independent portable five-labeled-source scalar-observer research. Frozen scientific source: **awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389**. Direct predecessor: R749SSP ([PR #2579](https://github.com/awdawmip/enterprise-math/pull/2579)), immutable scientific commit 6becc32889e633f4e34a1d251e26a03809e7e27b. Earlier relevant sources: R749SSK–SSL (#2566), R749SSM (#2572), and R749SSO (#2577). This new result preserves all predecessors' scientific inputs and claims no shared Task, CLAIM, Result, review, native X6 dynamics, or BRC Port theorem.

## Mathematical model and theorem

There are five distinct *labeled* sources with weights (1,1,2,3,6); the first unit-weight source is marked. For every integer q≥6 define

\[
\Omega_q=\{k\in\mathbb Z_{\ge0}^5:k_1+k_2+2k_3+3k_4+6k_5\le q-1\},\quad
C_q=|\Omega_q|,\quad T_q=\sum_{k\in\Omega_q}k_1.
\]

Define S(q)=18q⁴+54q³−345q²+2070q−16315, and the exact smoothed observation

\[
Y_q(e,d)=q^3\frac{T_q+e}{C_q+d}-\frac{S(q)}{108},\qquad
\mathcal O_q^{(m)}(e,d)=(Y_{q+6j}(e,d))_{j=0}^{m-1}.
\]

Every candidate cutoff q has an independently chosen real error pair (e,d) in the closed square [−2,2]²; within that candidate state the pair is common to all ordered six-shift observations. Cutoff provenance q is hidden from the observer. The least observation horizon h(q,p) is the least m≥1 for which the m-read image sets of two known candidate cutoffs q,p are disjoint.

**Exact result:**

| Distinct nonadjacent cutoffs | Sharp h(q,p) |
|---|---:|
| (6,8) | **3** |
| (7,9) | **4** |
| (8,10) | **3** |
| (9,12) | **4** |

In particular, the minimum observation horizon is **not determined by cutoff gap p−q**: gap 2 may require three or four reads, even with identical source weights and error bounds. Every result quantifies over the *entire continuum* of allowed error pairs, and lower-bound witnesses are exact.

## General exact algebra

For candidate q and competitor p>q, let a_j=q+6j and b_j=p+6j. Given q-side variables (e,d), form

\[
V_j=b_j^3(C_{a_j}+d),\qquad
U_j=a_j^3(T_{a_j}+e)+\frac{S(b_j)-S(a_j)}{108}(C_{a_j}+d),
\]

\[
L_j=(V_j,-U_j,C_{b_j}U_j-T_{b_j}V_j).
\]

Equality of the j-th observed outputs implies L_j·(E,D,1)=0 for the competitor's pair (E,D). Consequently three-read equality requires H₀₁₂(e,d)=det(L₀,L₁,L₂)=0. Four-read equality requires the simultaneous conditions H₀₁₂=H₀₁₃=0, where H₀₁₃=det(L₀,L₁,L₃). The provided exact certificate clears *positive rational* denominators and removes integer content, retaining precisely these zero sets. This construction does not divide by any unknown observation differences.

For constructive collisions, let (y₀,y₁) denote the first two q-side observations, and put

\[
x_j=\frac{y_j+S(p+6j)/108}{(p+6j)^3}\quad (j=0,1).
\]

Whenever x₁−x₀≠0, there is exactly one competing error pair satisfying the first two read equations:

\[
D=\frac{T_{p+6}-T_p-x_1C_{p+6}+x_0C_p}{x_1-x_0},
\qquad E=x_0(C_p+D)-T_p.
\]

The exact rational interval verifier confirms the inversion denominator excludes zero for every root bracket used below. Since the first two rows have rank two, H₀₁₂=0 then forces the third row to agree as well. Thus our algebraic roots plus permitted inversion witnesses are sufficient, not merely necessary.

## Two-read collisions and uniform three-read separation

Take (e,d)=(−1,−1) at cutoff q. Exact rational inversion produces the following competing cutoff-p parameters, strictly within (−2,2)²:

| (q,p) | Competing E | Competing D |
|---|---|---|
| (6,8) | 1173149794/1356947469 | −153764778/150771941 |
| (8,10) | 48524220279/51776767012 | −12269249984/12944191753 |

Substitution yields exact equality at the first two observations for each pair. To prove three reads always separate them, take the primitive integer H₀₁₂(e,d), substitute e=4x−2, d=4y−2 and expand in the complete tensor-product Bernstein basis over 0≤x,y≤1. The full basis is nonnegative and sums to one. Every coefficient is strictly negative:

| Pair | Minimum Bernstein coefficient | Maximum Bernstein coefficient |
|---|---:|---:|
| (6,8) | −2318795247385256 | −553578065493336 |
| (8,10) | −102594142867888936 | −3736000130840640 |

Hence H₀₁₂(e,d)<0 throughout the real error square and no three-read collision exists for either pair. The exact two-read witnesses establish sharp minimum **three**.

## Algebraic three-read collisions for (7,9) and (9,12)

At pair (7,9), fix d=−3/2. Let e* be the unique real root of the primitive quadratic H₀₁₂(e,−3/2) inside the rational interval

\[
-1173743640/10^9<e_*<-1173743630/10^9.
\]

At pair (9,12), fix d=−7/4. Let e* be the unique real root of H₀₁₂(e,−7/4) inside

\[
-759826230/10^9<e_*<-759826220/10^9.
\]

The certificate constructs both exact integer/rational polynomials, obtains opposite strict signs at the two rational endpoints of each interval, and uses exact Sturm root counts to prove uniqueness. It evaluates the rational inversion formulas using exact outward rational interval arithmetic. In the first pair (E,D) lies strictly in (1,2)×(−1,0); in the second it lies strictly in (1,2)×(−2,−1). Each first-two-read inversion is nondegenerate, and H₀₁₂ vanishes at the exact algebraic root, so all three observations coincide at admissible error pairs. Thus neither pair can be resolved by three or fewer reads.

## Four-read separation where simple resultant positivity fails

Set f=primitive(H₀₁₂) and g=primitive(H₀₁₃). Both are quadratic in e with polynomial dependence on d. In each of the pairs (7,9) and (9,12), the exact resultant Res_e(f,g) factors as a nonzero integer constant times three degree-one factors in d and a degree-five polynomial Q(d).

Exact Sturm sign-variation/root-count arithmetic proves every linear factor is nonzero for −2≤d≤2; Q has exactly **one** real zero there, and that zero lies in the following *rational* bracket:

\[
(7,9):\quad 660727283709/10^{12}<d_*<660727283711/10^{12},
\]

\[
(9,12):\quad 1390693182037/10^{12}<d_*<1390693182039/10^{12}.
\]

The next-to-last exact Euclidean subresultant of f and g has degree one in e: A(d)e+B(d). Because it belongs to the polynomial ideal generated by f and g, any common root necessarily satisfies A(d)e+B(d)=0. The exact verifier applies outward rational interval-Horner bounds to A and B on each entire d* bracket. These bounds prove A(d)≠0 there and force

\[
(7,9):\quad 1125< -B(d_*)/A(d_*) <1127,
\]

\[
(9,12):\quad 6< -B(d_*)/A(d_*) <8.
\]

Both contradict |e|≤2. Therefore *even though a resultant root occurs inside the denominator-error square*, it does not correspond to an admissible numerator-error state; four-read equality is impossible. Combined with the constructed exact three-read collisions, each pair has sharp minimum **four**. The degree-five resultant coefficients, linear subresultant coefficients, full fractional error enclosures and exact zero-count checks are reproduced by the companion Python certificate and its JSON output.

## Verification and scope

Run the companion Python 3/SymPy script R749SSQ_NONADJACENT_OBSERVER_CERT.py. It reconstructs all C_q,T_q from the five labeled source generating factors (1−z^w)⁻¹; verifies two exact rational two-read witnesses; computes every bivariate Bernstein coefficient for two three-read exclusions; checks exact algebraic three-read root isolation and strict admissibility using rational interval arithmetic; and computes both four-read resultants, Sturm root counts and linear subresultant error exclusions. The completed author run returned PASS and generated R749SSQ_NONADJACENT_OBSERVER_RESULTS.json. These are exact integer/rational algebra computations and exhaustive analytic sign arguments, not floating-point mesh sampling. Independent mathematical review is still required before any theorem promotion.

**Semantic boundary:** This is a scalar auxiliary observer with five retained source labels and a within-state joint calibration relation. It is not a full X6 Cell coordinate, native time event, triadic closure law or typed BRC Port construction. Forgetting the hidden cutoff is unsafe for future observation horizons below the proved minima. A transfer to native Port/BRC must explicitly embed the retained cutoff/branch provenance and prove a future-observer fibre equivalence; no such map is claimed.

**Next scientific questions:** classify all nonadjacent cutoff pairs, determine whether four observations always distinguish any two distinct cutoffs for real bounded errors, derive scale-dependent explicit separation margins, and independently address infinite-range one-read injectivity for integer-only errors. The algebraic *resultant-root plus inadmissible-parameter* certificate developed here is reusable when resultant positivity alone cannot prove disjointness.
