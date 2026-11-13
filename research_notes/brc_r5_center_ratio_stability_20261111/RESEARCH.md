# R5 — Reflection-pair mechanism and an exact local stability interval

Date: 2026-11-11 (Asia/Shanghai). Scope: author-side exact mathematics in the frozen seven-likelihood-ratio P/Q–BRC Blackwell observer model. The auxiliary one-variable family below is a comparative algebraic perturbation; the task's frozen scientific inputs remain unchanged.

## Scientific provenance and exact object

Frozen pins: GLOBAL a01383f825ef9d43b4b754254303298c64041568; ENTERPRISE-MATH 86149263e38c22292c9def1e0f69092efa1be77e.

Prior scientific result: [PR #2045](https://github.com/awdawmip/enterprise-math/pull/2045) counted 14,832 full 14-arc K4+double-high-edge circuits and 288 single-arc degeneracies among 15,120 candidate target assignments. [PR #2043](https://github.com/awdawmip/enterprise-math/pull/2043) supplies the adjacent-ray structural setting.

Carrier: signed masses on labeled source–target arcs. Observer: target and source marginals plus per-source first likelihood-ratio moments. The residual preserves the source-pair and target-label joint relations erased by that observer. BRC reuse: REUSE_APPLIED to the exact K2,3 residual decomposition from previous R5 results; no unproved port/target quotient is used.

Let the frozen target-ratio numerators be

\[
r=(2,10,15,20,25,30,38).
\]

Choose a low-degree source pair (p,q) in J={1,2,3,5}; call the other ports (h,k). Put seven distinct target labels into the slots

\[
(A,B,C,D,E,F,G)=(pq,ph,pk,qh,qk,hk,hk),
\]

with the two copies of the high-high pair identified under F/G exchange, and choose their unique canonical labeling F<G. There are 7!/2=2520 assignments per choice of low pair, and six choices of the low pair.

Set a,b,c,d,e,f,g to the *numeric ratio numerators* attached to A,B,C,D,E,F,G. Define the exact integer flow coefficients

\[
\begin{aligned}
u_A&=(b-c)(d-e),&u_B&=(c-a)(d-e),&
u_C&=(a-b)(d-e),\\
u_D&=-(b-c)(e-a),&u_E&=-(b-c)(a-d),\\
v_F&=-u_B(b-g)-u_D(d-g),&
v_G&=-u_B(f-b)-u_D(f-d).
\end{aligned}
\]

With Delta=g-f, the seven signed edge flows are

\[
(\Delta u_A,\Delta u_B,\Delta u_C,\Delta u_D,\Delta u_E,v_F,v_G).
\]

Opposite signs are placed at the two sources incident to each target; all four sources have zero total mass and zero first moment. The seven numerators are distinct throughout the considered parameter range. The first five coefficients and Delta are nonzero, so the full 14-arc circuit loses one high-high arc exactly when v_F=0 or v_G=0.

## Theorem A — The 288 degeneracies are exactly opposite-edge reflection matchings

**At the frozen ratio tuple** a candidate loses one arc if and only if target label 3 is F or G and the other high-high target label H, together with the ordinary K4 slots, obeys

\[
\boxed{A+H=6,\qquad B+E=6,\qquad C+D=6.}
\]

These are equalities of **target indices**, encoding the reflected numeric pairs (2,38), (10,30), (15,25), whose sums are each 40.

**Algebraic sufficiency.** If target label 3 is F, then g=40-a, e=40-b, d=40-c. Thus d-e=b-c, b-g=-(e-a) and d-g=-(c-a). Substitution into the displayed formula gives

\[
-v_F=(c-a)(d-e)(b-g)-(b-c)(e-a)(d-g)=0.
\]

The case G=3 is symmetric. There are 3! ways to assign the three reflection pairs to the opposite-edge pairs of K4 and 2^3 ways to orient them. Hence 48 degeneracies per low source pair, and 6*48=288 overall.

**Exact finite converse.** The independent standard-library checker enumerates all 2520 assignments modulo F/G exchange and computes both high-high flows by integer arithmetic. Exactly 48 cases have a zero coefficient, all satisfying the three reflection equations, and neither high-high coefficient is ever simultaneously zero. This exhausts the finite domain and establishes the frozen if-and-only-if criterion.

In particular, the previously observed zero at target index 3 has an exact explanation: the six *other* ratios form three equal-sum pairs. The unused central ratio need not numerically equal their midpoint for the zero to persist.

## Theorem B — Exact maximal census-stability window when only the central ratio varies

Define an explicitly comparative, not repinned, family

\[
r(t)=(2,10,15,t,25,30,38),\qquad 15<t<25.
\]

The original frozen model corresponds to t=20. All label and port semantics are unchanged. **For every real t satisfying**

\[
\boxed{\frac{4730}{249}<t<\frac{5230}{249}}
\]

there are exactly 288 single-edge degeneracies and 14,832 full-support assignments, with *precisely the same* 288 degeneracy patterns as for t=20. Equivalently, the full census is stable for

\[
\boxed{|t-20|<\frac{250}{249}.}
\]

This is the maximal connected open interval containing t=20 on which that census and the degeneracy set remain unchanged. At each of the two endpoint values exactly 288 further assignments degenerate, resulting in 576 degeneracies and 14,544 full-support assignments.

**Exact proof.** For a fixed label assignment, each of v_F and v_G is affine in any individual one of a,b,c,d,e,f,g, because the defining products use each numeric ratio variable at most once per monomial. Consequently in the single-variable t-family, v(t)=v(0)+t(v(1)-v(0)) exactly. Enumerate both coefficient functions over the 2520 assignments. Treat v(0)=v(1)=0 as an identically zero coefficient; for all nonconstant affine coefficients store the exact rational root -v(0)/(v(1)-v(0)) using Fraction arithmetic.

The certificate finds exactly 48 identically zero coefficients, all the reflection patterns above, and 84 distinct finite critical values over the real line (4320 individual coefficient-root occurrences). Exactly 18 critical values lie in (15,25); the nearest below and above 20 are 4730/249 and 5230/249. An exact root census rules out *every real intermediate value*, not merely a sample of rational t. Both nearest critical values actually occur:

- (A,B,C,D,E,F,G)=(0,1,2,3,4,5,6) has v_F(t)=249t-4730.
- (A,B,C,D,E,F,G)=(0,2,3,4,5,1,6) has v_F(t)=249t-5230.

The checker proves 48 newly vanishing assignments per low source pair at either endpoint. As the seven ratios stay distinct throughout this window, no other arc in the same candidate simultaneously vanishes. This establishes the endpoint counts and maximality.

## Verification, exact scope, and next scientific unit

The script VERIFY_CENTER_DEGENERACY_STABILITY.py uses only Python 3 standard-library itertools and fractions, and checks the complete domain of 2520 assignments per low source pair; the six low-source pairs give the 15,120 assignments. The output EXACT_OUTPUT.txt was produced by executing the calculation locally, with final marker PASS_EXACT_CENTER_RATIO_CIRCUIT_CENSUS_STABILITY. Arithmetic is exact integers and rational numbers; no floating-point inference is used.

Theorems A and B concern possible signed residual circuits across observer fibers. They do not assert which of these circuits occurs as an adjacent edge of the **single** physically admissible pinned fiber F_b={E>=0 : CE=b}. That unresolved question is the next research unit: reconstruct exact frozen C,b using the earlier immutable WITNESS and rank-15 repair-coordinate artifact; for each candidate residual direction, test exact nonnegative feasibility while allowing common positive support outside the circuit, and certify the support-union nullity-one condition. Preserve proofs and provenance of any new realized edge or excluded class. This work does not change P000 or the task's science pins.
