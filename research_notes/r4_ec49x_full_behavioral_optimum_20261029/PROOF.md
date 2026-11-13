# EC49X — Exact optimum for the *full* unseeded behavioral fixed-cost observer

**Date:** 2026-10-29. **Status:** `AUTHOR_PROVED / EXACT_FRACTION_CHECK_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED`.

**Scientific predecessor:** EC49W, Draft PR #1672, immutable commit `acd5552193e8ef25938d9c4fefabd29f3bf31599` (`PROOF.md` and `NEXT_TASK.md`). EC49W settled the always-buy-S subclass and proved strict nonattainment of the shared-seed convex-hull endpoint, leaving the full behavioral optimum open. This note settles *that precise missing optimum*, allowing arbitrary history-dependent randomized STOP/A/B prefix decisions and arbitrary code-and-U-dependent randomized decisions to omit S. It does not attempt the full `(alpha,beta)` region.

## 1. Exact model and BRC observer

Let initial history and terminal observation be `w,z ∈ {0,1,2}` and first signal `u ∈ {0,1}`. Source laws are

\[
Q(w,z)=1/9,\qquad P(w,z)=\begin{cases}1/6 & z=w,\\1/12& z\ne w,\end{cases}
\qquad t_w(u)=\tfrac12+(2u-1)\eta\sigma_w,
\quad\eta=1/200,\quad\sigma=(1,0,-1).
\]

The joint source leaf is `R(w,u,z) = R(w,z)t_w(u)` for `R∈{P,Q}`. Each source has 18 strictly positive, exactly normalized rational leaves, with the *same* marginal `P(w,u)=Q(w,u)`. Define the signed **difference of two positive probability readouts**, not a primitive signed-BRC amplitude,

\[
\Delta_w(u,z) = [P(w,z)-Q(w,z)]t_w(u)
  =\frac{(3\mathbf1_{w=z}-1)t_w(u)}{36}.
\]

Before erasing `w`, the observer chooses `STOP` or first action `A` (cost 1) / `B` (cost 2), along with one retained bit `D`; the four paid information states are `c∈{A0,A1,B0,B1}`. After erasure it sees `u` and may independently buy `S` (cost 1) to see `z`, or omit it; it finally accepts/rejects using only available information. Randomization is fresh, source-blind, and **does not retain a common seed correlating choices at separated information sets**. The expected source-equal costs are `C1=43/48` and `C2=7/8`. The objective is `δ=α−β` where `α=P(accept)` and `β=Q(accept)`. The observations and future operation (a choice after `u`, then acceptance) are part of the declared BRC readout scope; projecting them away requires proof.

## 2. Theorem (exact all-real behavioral optimum)

For all legal real-valued independent-coin behavioral policies in this model, including arbitrary random post-`u` omission of `S`,

\[
\boxed{\max_{C_1=43/48,\;C_2=7/8}\bigl(\alpha-\beta\bigr)=\frac{59}{576}.}
\]

The maximum is attained without shared random seeds by an explicit rational policy. The exact previous open interval `59/576 ≤ δ* < 11/96` therefore collapses to one point. A complete-history rational controller from EC49V at these same costs has `α−β=7/48`; thus it exceeds the maximum achievable compressed discrimination by at least

\[
\boxed{\frac7{48}-\frac{59}{576}=\frac{25}{576}.}
\]

This is an **attained full-memory versus optimal compressed-policy gap**, not a claim that `7/48` is the global full-memory optimum at these costs.

## 3. Exact reduction from adaptive sensing to a full-S relaxation

Let `x_{wc}≥0` be the first-stage probability of buying code `c` when initial history is `w`, with `\sum_c x_{wc}≤1`. Its STOP probability is `1−\sum_c x_{wc}`. Let `s_{cu}∈[0,1]` be the conditional probability of buying S from retained state `c` after seeing `u`. The no-persistent-seed information restriction gives the **causal product** `Pr(c,S\mid w,u)=x_{wc}s_{cu}`. Therefore

\[
\begin{split}
C_1&=\frac13\sum_{w,c} k_cx_{wc},\qquad k_{A0}=k_{A1}=1,\quad k_{B0}=k_{B1}=2,\\
C_2&=\frac13\sum_{w,c,u}x_{wc}t_w(u)s_{cu}.
\end{split}
\]

Any terminal decision without observing `z` has zero `P−Q` contrast, because `P(w,u)=Q(w,u)`; the same holds for an early STOP. Since buying `S` is decided before seeing `z`, the greatest possible terminal discrimination for a *fixed* prefix and S rule is exactly

\[
\delta(x,s)=\sum_{c,u}s_{cu}\sum_z\left[\sum_wx_{wc}\Delta_w(u,z)\right]_+,
\quad [a]_+=\max(0,a).
\]

This equality follows by accepting exactly the cells with positive signed coefficient. In particular, without asserting that changing a sensing policy preserves its costs,

\[
\delta(x,s)\le D(x):=\sum_{c,u,z}\left[\sum_wx_{wc}\Delta_w(u,z)\right]_+.
\tag{1}
\]

Let `b=\sum_{w,c\in\{B0,B1\}}x_{wc}` be the total expensive-action prefix mass and

\[
m=\sum_{w,c,u}x_{wc}t_w(u)(1-s_{cu})\ge0
\]

be the unsensed paid-prefix mass. Since `\sum_u t_w(u)=1` and `C1−C2=1/48`, **exact cost accounting** yields

\[
3(C_1-C_2)=b+m=\boxed{1/16}.
\tag{2}
\]

Thus `0≤b≤1/16`. From `3C1=43/16=\sum_{w,c}x_{wc}+b`, the total STOP mass is

\[
h:=\sum_w\left(1-\sum_cx_{wc}\right)=\boxed{5/16+b}.
\tag{3}
\]

These identities hold under every real randomized source-blind policy; they do *not* convert a pathwise behavior into a shared-seed lottery. The nonnegative residual `m` is an explicit preserved BRC resource/branch coordinate, not silently erased.

## 4. Convex endpoint theorem reducing the continuum to 288 vertices

Fix any `b∈[0,1/16]`. Consider all feasible prefix arrays `x` with this `b`, fixed first cost `C1=43/48`, but *relax* the second cost and evaluate `D(x)` as if every paid action bought S. This is solely a **proof upper bound**, so it need not satisfy `C2=7/8`.

Write `h_w` for STOP mass and `b_w` for total B mass at history `w`. Then

\[
\sum_wh_w=5/16+b,\qquad \sum_w b_w=b,\qquad
x_{w,A0}+x_{w,A1}=1-h_w-b_w.
\]

The row capacity conditions `h_w+b_w≤1` are automatically satisfied because

\[
\sum_w(h_w+b_w)=5/16+2b\le7/16<1.
\]

Therefore `(h_w)` and `(b_w)` range *independently* over two ordinary nonnegative three-coordinate simplices with their indicated total masses. The function `D(x)` is convex in all prefix coordinates, since it is a sum of positive parts of linear forms. For fixed `h_w,b_w`, split A mass between A0/A1 and B mass between B0/B1: a convex function achieves a maximum at extreme choices of each split. Fixing those **pure labels**, the resulting prefix `x` is affine in the two simplex vectors, so `D` again attains a maximum at their vertices.

Consequently the entire fixed-`b` relaxation is attained among exactly

\[
3\text{ STOP histories}\times3\text{ B histories}
\times 2^3\text{ A labelings}\times2\text{ B labels}=\boxed{144}
\]

labeled vertices. Explicitly, for STOP index `i`, B index `j`, pure A tags `a_w∈{A0,A1}` and B tag `q∈{B0,B1}`, put

\[
\begin{split}
h_w(b)&=(5/16+b)\,\mathbf1_{w=i},\\
b_w(b)&=b\,\mathbf1_{w=j},\\
x_{w,a_w}(b)&=1-h_w(b)-b_w(b),\\
x_{j,q}(b)&\mathrel{+}=b.
\end{split}
\]

Call the resulting (exact) value `D_v(b)`. For any such fixed labeling `v`, each entry of `x_v(b)` is affine in `b`, hence `D_v(b)` is convex on `[0,1/16]`. Their pointwise maximum `F(b)=\max_v D_v(b)` is also convex. A convex function on a closed interval is bounded above by the maximum of its two endpoint values:

\[
\max_{0\le b\le1/16}F(b)=\max\{F(0),F(1/16)\}.
\tag{4}
\]

This is a theorem over all **real** prefix and post-`u` behavior parameters. No finite grid or floating numerical extrapolation is involved; finite computation is used only for the 288 exact, formally justified endpoint candidates.

## 5. Certified endpoint values and attained witness

The attached standalone standard-library `VERIFY.py` enumerates all 144 labeled vertices at `b=0` and all 144 at `b=1/16`. Every value is evaluated in exact rational arithmetic by the literal 18-leaf source formula and the positive-part terminal rule. The complete CSV is `ENDPOINT_VERTICES.csv`. It obtains:

| Expensive mass b | Vertex count | Exact maximum F(b) | Labeled maximizers |
|---|---:|---:|---:|
| 0 | 144 | 59/576 | 72 |
| 1/16 | 144 | 59/576 | 48 |

Combining (1), (4), and these exact results gives the universal upper bound `δ≤59/576` for every legal real behavior under both fixed costs.

The following independently randomized rational prefix attains it: `w=0→A0` surely; `w=1→A1` surely; `w=2→STOP` with `3/8`, `A0` with `9/16`, `B0` with `1/16`. On paid branches always buy S. Accept iff `z∈{0,2}` after A0, iff `z=1` after A1, and iff `z=2` after B0. Exact leaf summation gives

\[
(\alpha,\beta,C_1,C_2)=\boxed{(109/192,\,67/144,\,43/48,\,7/8)},
\qquad \alpha-\beta=59/576.
\]

The policy uses independent randomization at one initial history, does not retain its outcome as an illegal common seed, and its terminal rule depends only on available `c,u,z`. It certifies attainment and proves the theorem.

## 6. Verification boundary, related science, and next obligation

`VERIFY.py` executed with Python's `fractions.Fraction`: it verifies source positive normalization and equal `(W,U)` marginals, computes 288 exact vertex values, certifies the endpoint maxima, verifies the rational attaining `(alpha,beta,C1,C2)` and 64 additional rational causal-factorization/cost-conservation sanity examples. These 64 examples are checks, *not* the proof of the all-real quantifier. The universal argument is the analytic conditional factorization, nonnegative contraction, two-simplex extreme point reduction and convex endpoint lemma. No native formal proof assistant checker has run; independent mathematical review and canonical result admission remain outstanding.

**BRC scope:** The population consists of source-labeled 18-leaf positive rational paths `(w,u,z)`, with preserved provenance `w`, action code `c` and second sensing decision. Positive-part evaluation is a statistical decision *readout* of a difference of two positive source measures; it is not a replacement of native signed/phase BRC. No claim is made about the user's locked P000 ontology, native six-axis X6 spatial coordinates, three-dimensional crystal layer, or heartbeat time; they remain unchanged. A typed transfer would need an X6/three-dimensional-layer carrier, a legitimate path correspondence, a declared readout and operation-preservation proof.

**Related external work (not a novelty assertion):** Anderson & Montúfar, *The Value Function Semi-Algebraic Set in Partially Observable Markov Decision Processes*, ICML 2026, PMLR 306:2677–2715, provides a semialgebraic characterization for infinite-horizon memoryless-stochastic POMDP value functions. Bork et al., *Multi-Cost-Bounded Reachability Analysis of POMDPs*, UAI 2025, PMLR 286:355–387, studies resource-bounded POMDP reachability. Our exact theorem is a finite two-source, two-stage, no-shared-seed, fixed-expectation-cost model and cannot be inferred directly from either paper. See `SOURCES.md`.

**Next exact question EC49Y:** Characterize the full `(alpha,beta)` achievable section at `eta=1/200`, `C1=43/48`, `C2=7/8`, including its nonconvex boundary and the role of no-S trajectories; determine which rational points admit rational independent behavioral kernels and compare with the shared-seed convex hull. Preserve the closed optimal-δ result as a fixed dependency, not a re-opened research target. Obtain independent adversarial verification of the endpoint reduction before any native admission.

**Frozen inputs:** `awdawmip/chatgpt-global-knowledge` GLOBAL_KNOWLEDGE_V1 `main@96ae9f7d749b54ff03afe9764b4aaf77dce9a759`, `awdawmip/enterprise-math` `main@12023ac5e9d9c257b310bf46c8c0c6757189da72`; applicable `AGENTS.md`, P000, ACTIVE worldview and portable research protocol loaded and unchanged. The original EC49W scientific definition and the present research author role are distinct from canonical active Task ownership and independent Driver review.
