# Stage357-B — Exact exclusion of every feasible outer component of the r₀=0 boundary

Date: 2026-11-01 (Asia/Shanghai). Authorship: Research2 continuing portable-author series, not a native Source-registered or independently reviewed Result.

**Claim (author proof, exact rational interval certificate).** Let `w=(1,3,3,1)`, `m=(61,21,9,9)`, and, for `x,y∈[0,1]`, put

\[
 B_k(z)=z^k(1-z)^{3-k},\quad
 r_k(x,y)=\frac{4B_k(x)+B_k(y)}5-\frac{m_k}{160},\quad
 b(x,y)=\frac5{32}\sum_{k=0}^3 w_k|r_k(x,y)|,
\]
\[
 D_3(a,z)=\frac12\sum_{k=0}^3w_k|B_k(a)-B_k(z)|,\qquad
 c(x,y)=\frac{63D_3(1/4,x)+D_3(3/4,x)+9D_3(1/4,y)+7D_3(3/4,y)}{256}.
\]

For **every real** `x,y∈[0,1]` satisfying

\[
 r_0(x,y)=0,\qquad b(x,y)\le\frac{299}{50000},\qquad
 x\in[0,229/1000]\cup[233/1000,1],
\]
there exists a **specific rational** `Q∈[0,1]^2` for which `b(Q)<b(x,y)` **and** `c(Q)<c(x,y)`.

Consequently no single source on this outer portion of `r₀=0` can occur in a globally minimal additive two-source configuration under any upper error budget. This is independent of Stage355's global error-floor theorem or Stage356's central-arc theorem. In combination with Stage356 (whose author proof remains unreviewed), the **entire `r₀=0` locus at `b≤299/50000` is strictly Pareto-dominated except for the selected common-zero `q*`.** This does **not** establish the global optimizer across other residual sign chambers.

## Proof and exact certificate

On `r₀=0`, set `t=1-y` and `s=1-x`; the *exact* algebraic relation is

\[
4s^3+t^3=61/32. \tag{1}
\]

Let `I=[u,v]⊆[0,1]` be any closed rational interval in `x`. Equation (1) forces

\[
A=61/32-4(1-u)^3\le t^3\le C=61/32-4(1-v)^3.
\]

If `C<0` or `A>1`, the entire `x` interval has no solution with `y∈[0,1]` (`NO_R0`). Otherwise clip to `[0,1]` and enclose each cube root by integer bisection to denominator `10^10`. Taking complements gives a guaranteed *rational rectangle* `I×J` containing **all real** solutions of (1) above `I`. The floor/root routine deliberately permits outward-only rounding.

For any rational interval `Z=[z₋,z₊]⊆[0,1]`, enclose `B_k(Z)` using nonnegative interval multiplication of `Z^k` and `(1−Z)^{3−k}`. Propagate these enclosures through all **four originally labeled** residuals and **four separate audit channels**. For any interval `V=[a,b]`, the value

\[
L_{|\cdot|}(V)=\max(0,a,-b)
\]

is a certified lower bound on `|z|` for every `z∈V`. Thus interval calculations return **lower** bounds `b_low(I)≤b(x,y)` and `c_low(I)≤c(x,y)` for every real point of the algebraic arc above `I`. This is a full labeled 16-subset total-variation comparison, not a reduction that erases provenance.

Every leaf is justified by exactly one of:

- `NO_R0`: equation (1) has no `y∈[0,1]` over this cell;
- `B_EXCLUDED`: `b_low(I)>299/50000`, so no point in this cell satisfies the budget condition;
- `DOMINATED`: a rational witness `Q` has **both** `b(Q)<b_low(I)` and `c(Q)<c_low(I)`.

The `x` domain is initially the two intervals `[0,229/1000]` and `[233/1000,1]`. If a cell has no certificate yet, bisect its `x` interval *exactly* in half. A terminal partition of **71 disjoint interiors, closed endpoint-covering intervals** is reached at maximum subdivision depth **13**. All `x` widths sum *exactly* to `996/1000`, the initial total width. Counts: left (`NO_R0` 4, `B_EXCLUDED` 1, `DOMINATED` 15); right (`NO_R0` 2, `B_EXCLUDED` 18, `DOMINATED` 31). No possible zero of (1) is left unclassified outside the central slab.

**Explicit witnesses.** All 15 left-side domination cells use the one fixed rational point

`Q_L=(0.2310839408555, 0.555508857277)`.

Right-side candidate witnesses are generated deterministically as rational points `Q_i=(x_i,y_i)` for

\[
x_i=\frac{i}{10^6},\quad i=232000,232050,\ldots,245000,
\]

where `y_i` is the *rational midpoint after 38 exact bisections* of `[1/2,3/4]` along the strictly decreasing function `y↦r₁(x_i,y)`, whose endpoint signs are checked. `r₁(Q_i)` need **not** equal zero: rationality is deliberate. The certificate searches this finite library and records one strict two-objective witness for each of the 31 right-side cells. The universal quantifier follows from interval enclosure and exact partition, **not** from sampling points on the curve.

`REPRO_STAGE357B.py` uses standard-library `fractions.Fraction` and only exact integer/rational arithmetic, checks all strict comparisons and regenerates `CERTIFICATE_STAGE357B_OUTER_R0.csv`. Two actual executions produced byte-identical stdout and a deterministic 71-row nonempty certificate. The full executed output appears in `REPRO_STAGE357B_EXECUTED_STDOUT.txt`. A witness in the output is a rational point in the *original two-dimensional parameter space* and therefore preserves the actual source-labeled `b,c` definitions. Replacing one source by a strict two-objective dominator preserves the additive two-source model's total error feasibility and strictly reduces its cost, proving the optimization corollary.

## Provenance, typed scope, next obstacle

Frozen control reads: `GLOBAL_KNOWLEDGE_V1 main@54fa7d60d81f96fd4ff80a18304013fec0b7b94e`, Enterprise Math `main@76e2ebe9125f7dd4318d020494197bbd65bd3d91` (actual GitHub connector reads). Current authoritative P000 V5, ACTIVE Heartbeat X6/time and joint-relation preservation, the portable protocol, and continuing Stage356 author record `PR #1736@f9fb3fb816998c5d7d00ca8af355b8a69417e639` were read. All 16 source subset comparisons and four audit channels are retained. This auxiliary Bernoulli model has **no established** typed bridge to native X6, third slice coordinate, independent time, triadic closure, Cell addresses, or BRC–Shor computation. `BRC_REUSE_APPLIED` only as a labeled-branch/provenance-preserving observer and exact-positive-rational proof technique; no native BRC-Shor computation is claimed.

The native `em_status` v0.6.11 reports `research_authority_granted=false`, control sync `UPSTREAM_CODE_REVIEW_REQUIRED`, and active job quota 5/5. A current formal owner/claim was not verified; this independent author-side material is `UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING`, **not** a Source Result, CLAIM, accepted theorem or P000 premise. The latest global knowledge source itself was read at a distinct GitHub-verified main snapshot; a bundled native global pin does not supersede that main snapshot.

**Stage358-B:** classify the **off-`r₀=0`** nearby chambers for `b≤299/50000`, especially adjacent `r₁=0` competitors after `E†`, using exact interval enclosures and rigorous local optimality/strict domination tests. In parallel seek an independent audit of Stage356 before promoting the combined `r₀=0` corollary; keep the P000/X6 transfer obligation separate.
