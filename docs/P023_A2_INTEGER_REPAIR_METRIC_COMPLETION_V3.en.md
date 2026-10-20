# P023 / A2 — Integer Repair Metric Completion Boundary, v3 Supplement

Status: `PROVED OWNER RESEARCH / FOUNDATION-BACKFLOW CANDIDATE`  
Owner: A2 future-compatible quotient  
Bridge: P005 projective precision / Foundation

## 1. Integer repair geometry is uniformly discrete

For integer alphabet base `B>=2`, A2 defines

\[
D_B(E,F)=L_B(\rho(E,F))+L_B(\rho(F,E)).
\]

Whenever `E` and `F` are distinct precision relations,

\[
\boxed{D_B(E,F)\ge1.}
\]

Thus zero is not an accumulation point of positive repair distances.

## 2. General theorem — integer-valued metrics are complete

Let `(M,d)` be any metric space with `d:M x M -> N_0`. Every Cauchy sequence is eventually constant.

### Proof

Take `epsilon=1/2`. For a Cauchy sequence `(x_n)`, there exists `N` such that `m,n>=N` implies `d(x_m,x_n)<1/2`. Since `d` is a nonnegative integer, this forces `d(x_m,x_n)=0`, hence `x_m=x_n`. The sequence is eventually constant and converges. ∎

Consequently every finite-valued A2 repair-metric space is already Cauchy complete.

## 3. No nontrivial Cauchy infinite-refinement point

A sequence of pairwise distinct A2 precision states cannot be Cauchy. In particular, a strict refinement chain does not converge merely because more finite coordinates have been retained.

Therefore

\[
\boxed{\text{integer repair geometry does not itself generate an infinite-precision limit point}.}
\]

## 4. Projective completion is a different construction

For a countable primitive binary task family, finite coordinate states can be represented by finite subsets `S subset N`. Under unit binary repair cost,

\[
\boxed{D(S,T)=|S\triangle T|.}
\]

This is integer-valued, so the finite-support state space is complete.

But the same finite coordinate system has a projective/product completion `{0,1}^N`, containing infinite-support profiles. Hence

\[
\boxed{\text{projective completion}\ne\text{A2 repair-metric completion}.}
\]

Finite-shadow compatibility does not select one completion automatically.

## 5. How a nontrivial metric completion can be manufactured

Add positive coordinate weights `w_i` with `sum_i w_i<infinity` and define

\[
d_w(S,T)=\sum_{i\in S\triangle T}w_i.
\]

Finite-support profiles are then dense in the full Boolean product because infinite profiles are approximated by finite truncations whose tail weight tends to zero. For example `w_i=2^{-i}` makes later coordinates arbitrarily cheap.

Thus a nontrivial metric infinite completion requires additional structure supplying arbitrarily small positive distances.

## 6. Precision-quantum criterion

More generally, if a metric satisfies

\[
x\ne y\Longrightarrow d(x,y)\ge\delta>0,
\]

then it is uniformly discrete and every Cauchy sequence is eventually constant. Therefore a necessary condition for a nontrivial Cauchy completion is

\[
\boxed{0\text{ is an accumulation point of positive distances}.}
\]

In precision language: an infinite metric refinement limit requires later strict refinements to become arbitrarily cheap in the chosen metric. That is an extra geometric assumption, not a consequence of finite quotient data.

## 7. Foundation boundary

This theorem does not forbid inverse limits, product completions, or other formal completions. It separates them from the intrinsic integer repair metric.

A future Foundation change should distinguish finite/projective compatibility of precision shadows, existence of formal infinite compatible profiles, actual-state realization of those profiles, and metric convergence under a declared precision geometry. None of these implications should be inserted without an explicit theorem.

## 8. P017 specialization

If a number-theory program realizes every finite binary task pattern but each actual state has finite support, then actual profiles can be dense in the product completion while remaining complete and discrete under unit repair/Hamming distance.

This provides a concrete program-level pressure test for the distinction above without promoting the completion to physical ontology.
