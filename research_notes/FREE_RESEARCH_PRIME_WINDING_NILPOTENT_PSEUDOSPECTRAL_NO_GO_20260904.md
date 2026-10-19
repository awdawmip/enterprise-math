# Free Research — Nilpotent Quotient Operator and Pseudospectral No-Go

Status: `FREE_RESEARCH_FRONTIER / EXACT_FINITE_NO_GO / EIGENVALUE_GAP_TRIVIAL / PSEUDOSPECTRAL_GROWTH_SHARP / VARIANCE_ROUTE_REQUIRED / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Parent: `FREE_RESEARCH_PI_PRIME_GEOMETRY_FRONTIER_V6_20260904.md`

## 1. Correction of the spectral target

The previous frontiers sometimes described the missing native mechanism as a “spectral gap” for the quotient-return operator. At finite scale that phrase is too weak and potentially misleading.

Every prime-power quotient action strictly lowers every positive state. Therefore every finite positive combination of such actions is represented by a strictly triangular matrix and is nilpotent. Its eigenvalue spectrum is already exactly `{0}`.

The genuine obstruction is not an eigenvalue near `-1`. It is logarithmic growth of the resolvent/pseudoinverse caused by long nonnormal quotient chains.

---

## 2. Finite quotient operator

Fix a cutoff `N>=1`. Let

\[
V_N
=\{f:\{0,1,\ldots,N\}\to\mathbb R:f(0)=0\}.
\]

For an action label `a>=2`, define

\[
(Q_af)(n):=f(\lfloor n/a\rfloor).
\]

Let `S` be a finite collection of such labels and let `w_a>=0` with

\[
\sum_{a\in S}w_a=1.
\]

Define the one-step return operator

\[
P:=\sum_{a\in S}w_aQ_a.
\]

Since

\[
\lfloor n/a\rfloor<n
\qquad(n>0,a>=2),
\]

the matrix of `P` in increasing state order is strictly triangular.

Hence

\[
\boxed{\operatorname{Spec}(P)=\{0\}.}
\]

---

## PNO-T01 — Uniform finite nilpotence depth

Every length-`k` quotient history with labels at least `2` ends at a state no larger than

\[
\left\lfloor\frac{n}{2^k}\right\rfloor.
\]

Therefore, if

\[
2^k>N,
\]

then every length-`k` history from every state `n<=N` reaches `0`. Since functions in `V_N` vanish at `0`,

\[
\boxed{P^k=0.}
\]

Let

\[
L_N:=\min\{k:2^k>N\}
=\lceil\log_2(N+1)\rceil.
\]

Then

\[
\boxed{P^{L_N}=0.}
\]

This conclusion is independent of the prime labels and the positive weights.

---

## PNO-T02 — Exact resolvent expansion

Nilpotence gives the finite identity

\[
\boxed{
(I+P)^{-1}
=I-P+P^2-\cdots+(-1)^{L_N-1}P^{L_N-1}.
}
\]

Every `Q_a` is a contraction in the supremum norm, and so is their convex combination `P`. Consequently,

\[
\boxed{
\|(I+P)^{-1}\|_{\infty\to\infty}
\le L_N.
}
\]

Thus a first-order return residual of size `O(1/log N)` can yield at best an `O(1)` bound through this argument:

\[
L_N\cdot O(1/\log N)=O(1).
\]

This exactly matches the point at which the one-step return equation stalled before Selberg smoothing.

---

## PNO-T03 — Logarithmic amplification is sharp

Take the deterministic operator

\[
P=Q_2.
\]

Choose a state whose successive quotient-by-two ancestors have length `L` before reaching zero, and prescribe a residual field `g` with alternating signs along this chain:

\[
g(q_2^j(n))=(-1)^j.
\]

Then

\[
\left((I+Q_2)^{-1}g\right)(n)
=
\sum_{j=0}^{L-1}(-1)^jg(q_2^j(n))
=L.
\]

Since `||g||_infty=1`,

\[
\boxed{
\|(I+Q_2)^{-1}\|_{\infty\to\infty}=L
}
\]

on this chain.

Therefore the logarithmic loss is not a loose estimate. It is attained by an exact finite sign-alternating history field.

---

## 3. Consequence for the Enterprise PNT route

An eigenvalue calculation cannot distinguish the arithmetic centered field from the worst-case alternating chain, because both live under a nilpotent operator with spectrum `{0}`.

The required extra structure must control one of the following:

1. singular values of the signless operator `I+P` in an arithmetic weighted norm;
2. pseudospectral amplification of the nonnormal quotient matrix;
3. a carré-du-champ/variance form on competing quotient histories;
4. positive higher provenance energies that rule out coherent alternation across the full quotient 2-complex.

This validates the pair-simplex variance direction and refines the next target:

\[
\boxed{
\text{ordinary eigenvalue gap is solved but irrelevant;}
\quad
\text{the missing invariant is a weighted singular/curvature gap.}
}
\]

---

## 4. Relation to the odd-simplex energy

The deterministic `Q_2` chain can realize maximal alternating amplification because it has only one route at each step. Once all prime-power action pairs are filled by direct `ab` edges, every two-step route belongs to an odd triangle.

The weighted pair-simplex inequality

\[
4U^2|f(n)|^2
\le3(UE_1+E_{\rm dir}+E_{\rm tr})
\]

is therefore a nonnormal resolvent control mechanism, not merely an eigenvalue exclusion. It penalizes the coherent alternating chain by comparing it with competing recoalescing histories.

The PNT zero-energy criterion shows that the actual centered arithmetic field enters the low-energy sector of this full complex. A native remainder theorem must quantify the singular gap on that arithmetic sector.

---

## 5. Finite exact verification

The companion checker verifies for arbitrary positive rational weights:

- strict state lowering;
- endpoint bounds after every finite word;
- nilpotence at depth `L_N`;
- the finite Neumann inverse identity;
- the supremum norm upper bound;
- exact sharpness for deterministic quotient-by-two chains.

No asymptotic prime-distribution theorem is used.

---

## 6. Updated next theorem

The correct target is a weighted lower singular-value estimate, not a new eigenvalue theorem. One useful form is

\[
\boxed{
\|(I+P_N)f\|_{\mathcal H_N}^2
+\mathcal C_N(f)
\ge c\|f\|_{\mathcal H_N}^2,
}
\]

where:

- `H_N` is a logarithmic or prime-winding weighted finite Hilbert space;
- `C_N` is the direct/transported pair-simplex collision energy;
- `c>0` is uniform in `N` on the centered arithmetic subspace.

A proof would convert the pair-simplex geometry into a native quantitative remainder mechanism. The ordinary spectrum of `P_N` supplies no further information because it is already identically zero.
