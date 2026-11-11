# R713 — Odd-ring BRC microphase area-optimal schedule counting and information fibers

Date: 2026-11-11 (Asia/Shanghai). Author-side exact combinatorial result; mathematical review pending.
Mother Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142.
Researcher-ID: EM-X6-77629F; Research-Activity-ID: RA-A7C5EE2EA9667D1DC0870B1F.
Frozen scientific source: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Inputs: R711/R711b @8fe4c9ce43183e9394d1e4047585ba51c336c483; R712 @e74bb4deb28b07bbfb12c147a282a336d72dd4e5. Current normative rules were read separately. Task observed HANDOFF_READY / NEEDS_DISPATCH, owner taskbook/unassigned as of 2026-11-11 12:16 CST; no CLAIM from this author.

## Defined candidate operation and exact observer

Fix an odd labelled full-firing cycle of m>=5 Cells, five ordered phases 1,...,5, at most one incident elementary TRANSFER per Cell per phase, and exactly one positive source-labelled transfer of each of two opposite types on every physical edge. A macrostep freezes its old Cell/triad gate and commits its candidate triad update after phase 5. The event model is the explicitly declared R709b–R712 candidate extension. For edge i, phases p_i<q_i contain its two distinct events; the plus and minus types may appear in either order. Feasibility of the phase schedule is exactly the cyclic disjointness constraint {p_i,q_i}∩{p_(i+1),q_(i+1)}=∅. All positive BRC event occurrences, source/type and phase order remain separate; signed physical-edge current is only a derived integer observer.

Define D_t = #{i:p_i <= t < q_i} for t=1,...,4 and area A=sum_t D_t=sum_i(q_i-p_i). Put w_i=q_i-p_i-1>=0. Hence A=m+sum_i w_i. R712 proved the minimum A=m+3 over all full odd-ring five-phase schedules for every odd m>=5.

A phase-pair word has fixed labelled edge 0 (no quotient by rotations, reflections or phase relabelling). Write U_m for the number of pair words with area m+3, and T_m for the number of corresponding fully typed (+,-) phase histories. Within a phase, events on disjoint edges are unordered.

## Theorem A — exact generating function and recurrence

For every odd m>=5, T_m=2^m U_m, and

\[
\boxed{\sum_{\substack{m\ge5\\m\text{ odd}}}U_m z^m=
\frac{8z^5(5-9z^2+z^4)}{(1-3z^2+z^4)^2}.}
\]

Equivalently let c_k=U_(2k+5), for k>=0. Then

\[
\sum_{k\ge0}c_k x^k=\frac{8(5-9x+x^2)}{(1-3x+x^2)^2}.
\]

The first four values are c_0=40, c_1=168, c_2=576, c_3=1848; for all k>=4,

\[
c_k=6c_{k-1}-11c_{k-2}+6c_{k-3}-c_{k-4}.
\]

### Complete proof

Let G be the Petersen graph of all ten two-subsets v=(p,q) of {1,2,3,4,5}, with adjacency when subsets are disjoint. Put w(v)=q-p-1. Let A_G be its 10x10 adjacency matrix and D(y)=diag(y^{w(v)}), M(y)=A_G D(y). By expanding matrix powers, the exact generating polynomial tr(M(y)^m) counts every **rooted** admissible length-m phase-pair word once, weighted by y raised to total excess area. Therefore U_m=[y^3]tr(M(y)^m) for odd m>=5.

Write F(z,y)=det(I-z M(y)). Formal matrix/determinant algebra gives

\[
\sum_{m\ge1}\operatorname{tr}(M(y)^m)z^m = -z\,\partial_z\log F(z,y).
\]

An exact finite 10-column Leibniz expansion through y^3 yields

\[
F=d_0(z)+yd_1(z)+y^2d_2(z)+y^3d_3(z)+O(y^4)
\]

with

\[
\begin{aligned}
d_0&=1-3z^2+z^4,\\
d_1&=-2z^2+2z^4,\\
d_2&=-4z^2+11z^4-2z^6,\\
d_3&=-4z^2+16z^4-8z^5-6z^6.
\end{aligned}
\]

The attached Python script independently computes all four displayed polynomials by exact integer subset/sign dynamic programming for the Leibniz determinant (no SymPy or floating-point requirement). The y^3 coefficient of the formal logarithm equals

\[
d_3/d_0-d_1d_2/d_0^2+d_1^3/(3d_0^3).
\]

Since d_0,d_1,d_2 are even in z, its odd-in-z part is precisely -8z^5/d_0. Odd-length extraction and differentiation thus give

\[
-z\frac{d}{dz}\left(-\frac{8z^5}{d_0}\right)
=\frac{8z^5(5-9z^2+z^4)}{(1-3z^2+z^4)^2}.
\]

The Petersen graph has no odd closed walk shorter than five. This proves the first identity. Each phase-pair word admits independently a plus-first/minus-first choice for each edge, giving 2^m typed histories with the same area and terminal positive-counter ledger. Each Cell sends at most one event of each type in a macrostep, so initial stocks of at least one per type suffice for every such ordering in the declared candidate gate. Multiplication by 2^m proves the typed count.

## Theorem B — asymptotic raw-history entropy

Let \(\varphi=(1+\sqrt5)/2\) and \(r=(3-\sqrt5)/2=\varphi^{-2}\), **ordinary combinatorial counting constants**, unrelated to physical angles or native propagation. The x-denominator has a double dominant pole at x=r; its principal coefficient is

\[
A_*=\frac{8(5-9r+r^2)}{(1-r^2)^2}=\frac{32}{3\sqrt5-5}>0.
\]

Therefore, as k tends to infinity,

\[
\boxed{U_{2k+5}\sim A_* k\varphi^{2k},\quad
T_m=\Theta(m(2\varphi)^m)\quad(m\to\infty,\ m\text{ odd}).}
\]

For reconstructing exactly **which raw typed five-phase history** occurred from a fixed completed edge ledger on the labelled cycle, the minimum fixed-length reversible record is

\[
\boxed{B_m=\lceil\log_2 T_m\rceil=m+\lceil\log_2 U_m\rceil
=m\log_2(2\varphi)+\log_2m+O(1).}
\]

This is a raw-history fiber count, not a claim that every possible future V39 observer requires that many bits. A future-safe quotient requires its own exact fiber-constancy certificate.

## Exact verification, examples and reproducibility

Run: python R713_ODD_RING_COUNT_VERIFY.py > R713_ODD_RING_COUNT_RESULTS.json

The script uses only Python 3 standard library; no trig, pi, ordinary wave propagators or BRC-positive mass cancellation. It (1) recomputes the four determinant coefficient polynomials via integer subset DP; (2) independently counts all closed phase-pair words by weighted adjacency DP for the **49 odd lengths** m=5,7,...,101 and matches each count to the rational-function recurrence; (3) enumerates the full four-boundary residual profile distribution for m=5,7,...,21 and checks the sharp peak from R712.

| odd m | U_m (area m+3) | also minimum peak (finite exact check) |
|--:|--:|--:|
|5|40|40|
|7|168|168|
|9|576|72|
|11|1848|528|
|13|5720|104|
|15|17280|1320|
|17|51272|136|
|19|150024|2736|
|21|434112|168|

The result JSON includes all 49 counts, exact determinant coefficients, nine full peak-optimal histograms, and selected typed counts and required bit lengths. Execution status: R713_ODD_RING_AREA_OPTIMAL_ENTROPY_PASS. The finite joint-peak table does not assert an infinite-length formula for that narrower family.

## BRC/native scope and next research dependency

BRC resolution: COMPOSE_APPLIED (positive source-labelled path/TRANSFER occurrences retained; signed edge flux is a typed observer only). Combinatorial phase labels do not by themselves establish physical heartbeat intervals or real native Link/Port permission. Original Cell/branch source and joint relations are preserved; the exact counting formula is a quotient for the declared **area-only counting question**. P000 V5 and the ACTIVE six-axis/three-dimensional-slice worldview are unchanged.

The result is an author-side exact combinatorial derivation with executed finite arithmetic checks. Independent mathematical review, Source-native Result, and native event-admission comparison remain pending.

Next: prove or disprove closed formulas suggested by the nine finite counts for schedules simultaneously optimizing peak and area; classify which typed histories remain distinct under future V39 (j,h); test full frozen Link/Port semantics against five-phase frozen-prepare/commit.