# EC49FQF–FQG: Exact cross-prior regret and certified mixed-prior BRC phases

**Mathematical status:** AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.  
**Authority:** independent portable research; not a formal Task CLAIM, Result, Review, Working Truth, Foundation change, or a P000 revision.  
**Frontier:** EC49FPY–EC49FQE, [EC49FQE PR #2524](https://github.com/awdawmip/enterprise-math/pull/2524).  
**Frozen science pin:** \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`. No change to frozen observations or scientific source.

## Exact domain

Native BRC class **16943** has 310 original legal configurations, 141 different named-root cost profiles, 144 permitted terminal scalar observations indexed 0..143 and 84 named-root scalar observations indexed 144..227. Distinct profiles have positive integer multiplicities \(m_i\) with \(\sum_i m_i=310\). A valid policy is a finite adaptive decision tree whose response-labelled leaves uniquely identify all 141 profiles. Terminal observation price \(t>0\), named-root observation price \(r>0\).

For any policy \(P\), let \((R_u,T_u)\) denote the total numbers of named-root and terminal reads across all 141 profiles, and \((R_w,T_w)\) the same totals weighted by configuration multiplicity. Two different priors give:
\[
C_u(P;r,t)=(R_u r+T_u t)/141,\qquad
C_w(P;r,t)=(R_w r+T_w t)/310.
\]
These are different objectives on the **same** finite native-BRC response table; neither drops root-residual distinctions.

Pinned original master source SHA256: \`cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e\`; named-root profile CSV SHA256: \`a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f\`. The full pinned source bytes and executable evidence are included in the companion user-delivered reproducibility archive.

## EC49FQF: Sharp regret and impossibility of shared optimality

**Theorem.** For *all real* \(r/t\ge3\), the exact separate global optima are
\[
\inf_P C_u(P;r,t)=\frac{4r+296t}{141},\qquad
\inf_P C_w(P;r,t)=\frac{4r+688t}{310}.
\]
Among **all** policies optimal for U, the least attainable W cost is precisely
\[
\min_{\;P:C_u(P)=\min C_u} C_w(P)=\frac{4r+707t}{310},
\]
with sharp unavoidable W regret \(19t/310\). Conversely, among all policies optimal for W, the least attainable U cost is
\[
\min_{\;P:C_w(P)=\min C_w} C_u(P)=\frac{4r+298t}{141},
\]
with sharp unavoidable U regret \(2t/141\). No single identifying strategy can be optimal under both priors anywhere on \(r/t\ge3\).

**Exact Bellman anchor at \(r:t=3:1\).** For each profile subset S, query q with proper response blocks \(S_{q,v}\), price c(q)∈{1,3}, and prior aggregate weight \(W_j(S)\), let
\[
D_j(S)=\min_{q:\text{separates }S}\big(c(q)W_j(S)+\sum_{v:|S_{q,v}|>1}D_j(S_{q,v})\big),
\quad D_j(\{s\})=0.
\]
It is an exact full-depth recurrence: all recursive proper blocks are strictly smaller than S, so induction covers *every* admissible adaptive finite policy. Recalculation from frozen inputs yields \`D_U(full)=308\`, \`D_W(full)=700\`. Exhaustive optimal first-query sets:
- U optimum: **{32,34,140,142}**.
- W optimum: **{16,23,59,88}**.

The two sets are disjoint. Under first q32/q34 the best **W** cost is 769; under q140/q142 it is 719. Both exceed unrestricted W optimum 700. Under q16/q23 the best **U** cost is 310; under q59/q88 it is 311. Both exceed unrestricted U optimum 308. These other-prior lower bounds allow arbitrary subsequent adaptation; no additional constraint was imposed after the first query.

A fresh lexicographic Bellman recursion—first preserve the exact primary Bellman optimum on every current subset, then minimize the other prior over those surviving choices—constructs two complete sharp policies:

| Witness | First q | \(R_u\) | \(T_u\) | \(R_w\) | \(T_w\) | U @3:1 | W @3:1 |
|---|---:|---:|---:|---:|---:|---:|---:|
| U-first, W-secondary | 140 | 4 | 296 | 4 | 707 | 308 | 719 |
| W-first, U-secondary | 16 | 4 | 298 | 4 | 688 | 310 | 700 |

**High-price proof.** In the exact native data there are two terminal-response fibers, each with two distinct root-cost profiles of multiplicity one. No sequence of terminal-only readings distinguishes the two members in either pair. Correct identification thus forces at least one named-root observation on the path of *each* of the four profiles, so for every full identifying policy \(R_u,R_w\ge4\). Write \(x=r/t\) and normalize \(t=1\):
\[
141C_u(P;x,1)=[3R_u+T_u]+(x-3)R_u
\ge308+4(x-3),
\]
\[
310C_w(P;x,1)=[3R_w+T_w]+(x-3)R_w
\ge700+4(x-3).
\]
Both bounds are attained by the displayed policies. If P is U-optimal at x≥3, every nonnegative step must be sharp, so it was already U-optimal at x=3, and its first q lies in {32,34,140,142}. The constrained other-prior Bellman table gives \(3R_w+T_w\ge719\), while \(R_w\ge4\), hence \(310C_w(P;x,1)\ge719+4(x-3)=4x+707\); the U-first tree attains it. Symmetrically a W-opt policy must first choose {16,23,59,88}, forcing \(3R_u+T_u\ge310\) and then \(141C_u(P;x,1)\ge4x+298\). Restoring t gives the theorem. ∎

## EC49FQG: two certified mixture-prior intervals

For \(0\le\alpha\le1\), define profile mass
\[
p_\alpha(i)=\frac{\alpha}{141}+\frac{(1-\alpha)m_i}{310}.
\]
At \(r/t\ge3\), the following are **globally optimal** for *all real prices* in that ray and every α in the stated intervals:
\[
\boxed{0\le\alpha\le4/5:\quad
F_\alpha(r,t)=\alpha\frac{4r+298t}{141}+
(1-\alpha)\frac{4r+688t}{310}.}
\]
The attaining policy is the W-first lexicographic witness.
\[
\boxed{5/6\le\alpha\le1:\quad
F_\alpha(r,t)=\alpha\frac{4r+296t}{141}+
(1-\alpha)\frac{4r+707t}{310}.}
\]
The attaining policy is the U-first lexicographic witness.

**Exact anchors at 3:1:** for rational α=a/b, integral profile weights
\[
w_i=310a+141(b-a)m_i,\quad \sum_i w_i=43710b
\]
permit a fully integral all-depth Bellman solver. The following exact minima were freshly calculated and all 310 original configurations were independently replayed:

| α | scaled integer minimum \(\sum_i w_i \times\) read cost | optimal counts \((R_u,T_u;R_w,T_w)\) |
|---|---:|---|
| 1/2 | 194800 | (4,298;4,688) |
| 3/4 | 387000 | (4,298;4,688) |
| 4/5 | 483100 | (4,298;4,688) |
| 5/6 | 578779 | (4,296;4,707) |

At α=0 and α=1 the previous exact single-prior Bellman optima were independently recovered (W=700 and U=308). Consequently the W-first witness attains the global optimum at both α endpoints 0 and 4/5; likewise U-first attains it at both 5/6 and 1. Because a pointwise infimum of affine policy costs is **concave** as a function of α, the optimal value between two known endpoints is at least their chord. The fixed witness attains that exact chord and is an upper bound, proving equality throughout each closed interval. At \(r/t>3\), every mixture policy needs an expected aggregate of at least four root observations under either component prior, and both witnesses achieve exactly four. The same affine lower-bound argument extends the certificate to all \(r/t\ge3\). ∎

**Open:** the true mixture-optimal phase changes in \(4/5<\alpha<5/6\), including possible additional supporting policies, remain unproved. The two **known witnesses** cross at α=\(2679/3299\); this is only their pairwise price-line intersection, **not** a certified global critical mixing fraction. Also open: \(r/t<3\), different priors and other BRC root classes.

## Evidence and verification limits

- Code: fresh exact lexicographic Bellman, exact mixed-prior Bellman at four α anchors, and a **separate original-source parser** that independently reconstructs the 144 terminal and 84 named-root responses and replays **all 310 configurations** on the witness trees; this check does not import the Bellman optimizer.
- Certificates: complete query/response/leaf trees, full 228-option initial-query costs for both base priors, four mixture anchors, and verified root/terminal read counts. A compact lossless zlib/base64 of both primary trees is supplied in this branch; the full inputs, optimizer, source files, certificates, code, and SHA256 manifest are preserved in the complete companion evidence archive.
- Observed independent test flags: \`INDEPENDENT_310_REPLAY_PASS\` for both lex trees; \`EC49FQF_HIGH_PRICE_CROSS_PRIOR_REGRET_EXACT_PASS\`; \`INDEPENDENT_MIXTURE_REPLAY_PASS\` for α=1/2,3/4,4/5,5/6.
- Exact integer/rational proof of this declared finite decision model, **not** a claim of mathematical independent review, live Task ownership, external physical observation or general asymptotic BRC complexity.

**Authors/role:** current independent RESEARCHER identity is tracked separately in the native registration/Activity. A portable GitHub research note does not confer Task CLAIM or formal review.
