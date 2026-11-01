# Stage355-B — An exact universal TV floor and a strict `r3`-strip Pareto exclusion

**Date:** 2026-11-01 (Asia/Shanghai). **Author role:** portable author / ongoing `进取数论研究2` context; **classification:** `PORTABLE_AUTHOR_THEOREM / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING`. This is a self-contained theorem of the **external Bernoulli/BRC auxiliary observer**, not a P000/X6 or physical model theorem.

## 1. Source and scope pins

Frozen, *separately verified* canonical inputs for this research run:

* `awdawmip/chatgpt-global-knowledge main@c1d957ec4b54c76df0d5ddcecf4b8f6f6f319f1e`: `00_BOOTSTRAP.md`, `OPERATING_MANUAL.md`, Enterprise Math project route, P000 startup/original blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`, ACTIVE `我眼中的世界.md`, mathematics/BRC/registration and code policies.
* `awdawmip/enterprise-math main@f3e38a72335239e95d2b020d782b7e67b98c006e`: native P000 V5, `AGENTS.md`, current control authority, `docs/AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md`, `docs/PORTABLE_RESEARCH_PROTOCOL.md`.
* Last authored scientific source: PR #1736 immutable head `ad7f7816ca0939c610256f2ad60bfe3b62fec9eb`; Stage354-B source comparison, Stage353-B exact right-arc allocation and Stage355-B handoff. None of those author's unreviewed global lemmas is needed in this new proof.

The native service's read-only `em_status` returned version `0.6.11`, `research_authority_granted=false`, `executor_binding_configured=false`. A bounded current-owner/task query returned `CONTROL_QUOTA` rather than a verified owner list. No formal claim, native task result, independent review, or acceptance is implied by publication here. Existing Stage352-B safety-denied source bytes are not reproduced or re-routed.

## 2. Exact external model

For `0<=x,y<=1`, let

\[
 w=(1,3,3,1),\quad m=(61,21,9,9),\quad B_k(z)=z^k(1-z)^{3-k},\quad
 r_k(x,y)=\frac{4B_k(x)+B_k(y)}5-\frac{m_k}{160}.
\]

Define the source-labeled total-variation budget and independent source-audit cost:

\[
 b(x,y)=\frac5{32}\sum_{k=0}^3 w_k|r_k(x,y)|,\qquad
 D_3(a,z)=\frac12\sum_{k=0}^3 w_k|B_k(a)-B_k(z)|,
\]
\[
 c(x,y)=\frac{63D_3(1/4,x)+D_3(3/4,x)+9D_3(1/4,y)+7D_3(3/4,y)}{256}.
\]

The original source/port factors are retained: no cross-source total collapsing, no hidden-state access, and no change to 16 source-word comparisons. The total two-source objective is

\[
 T(q_1,q_2)=\frac{33}{1024}+c(q_1)+c(q_2),\qquad
 b(q_1)+b(q_2)\le 2\beta_*+E.
\]

Here `q_*=(x_*,y_*)` means the particular root `r0=r1=0` in the rational isolator below, `beta_*=b(q_*)`, and `0<=E<=11/5000`. We do not assume that this root is globally error-minimizing. Our theorem applies to **any feasible pair**, hence also to any global minimizer if one exists (compactness guarantees existence).

## 3. New exact theorem

**Theorem (strict excluded residual tube, fully quantified).** For every real `E` in `[0,11/5000]`, any feasible `(q1,q2)` with either source satisfying

\[
 \boxed{|r_3(q_i)|\le \frac1{2000}}
\]

is strictly Pareto-improvable: replacing that source by the **single fixed rational point**

\[
 \boxed{Q=\bigl(29/125,349/625\bigr)}
\]

strictly decreases both `b(q_i)` and `c(q_i)`, and hence keeps the pair feasible while strictly lowering `T`. Consequently **no unrestricted global optimum** in the declared two-source model contains a source in that closed residual tube, for any of the real budgets in this interval. In particular, the entire algebraic boundary `r3=0` is eliminated; the result is stronger than excluding just an isolated boundary point or a numerical mesh.

This is not a theorem that both sources lie on the Stage353 right `r1=0` arc; it removes one genuine competing residual stratum without appealing to the unreviewed Stage336/342 strict-dominance lemma.

### 3.1 Global error floor from source-labeled TV duality

Write for any subset `S` of `{0,1,2,3}`:

\[
 P_S(z)=\sum_{k\in S}w_k B_k(z),\quad M_S=\sum_{k\in S}w_km_k.
\]

Because `sum_k w_k B_k(z)=1` and `sum_k w_k m_k=160`, we have `sum_k w_k r_k=0`. Therefore the elementary positive-mass / total-variation identity yields

\[
 \boxed{b(x,y)=\frac5{16}\max_{S\subseteq\{0,1,2,3\}}\left(\frac{4P_S(x)+P_S(y)}5-\frac{M_S}{160}\right).}\tag{TV}
\]

For a cubic polynomial `p`, its four Bernstein coefficients on any rational interval `[l,h]` are exactly

\[
 \left(p(l),\;p(l)+\frac{h-l}{3}p'(l),\;p(h)-\frac{h-l}{3}p'(h),\;p(h)\right).
\]

The Bernstein convex-hull property puts the entire real continuum `p([l,h])` between the minimum and maximum of these coefficients. Apply the lower coefficient to each `P_S(x), P_S(y)` inside (TV), then maximize over all 16 retained subsets. A full `[0,1]^2` cover with **67 closed dyadic rational rectangles** proves:

\[
 \boxed{\forall(x,y)\in[0,1]^2:\quad b(x,y)\ge 3779/10^6 =0.003779.}\tag{1}
\]

The certificate covers the whole square with nonoverlapping rectangle interiors and exact area sum 1; every one of its 67 leaves passes the exact Bernstein lower-bound test. Its maximum bisection depth is 37. This is an **independent absolute b-floor**; it neither cites nor re-proves Stage346's **sharp** uniqueness/floor claim.

### 3.2 Independent algebraic isolator of `q*`, without a global-minimum assumption

Set `s=1-x, t=1-y`. The two equalities `r0=r1=0` reduce **exactly** to

\[
 4s^2+t^2=41/16,\qquad 4s^3+t^3=61/32.
\]

For `s` in the rational range

\[
 0.768916059144<s<0.768916059145
\]

set `t(s)=sqrt(41/16-4s^2)`. The exact rational sign test

\[
 \left[(41/16-4s^2)^3-(61/32-4s^3)^2\right]_{s=s_{lo}}<0,
 \quad[\cdots]_{s=s_{hi}}>0
\]

has the desired orientation because `61/32-4s^3>0` throughout the box. Also

\[
 \frac{d}{ds}\left(4s^3+t(s)^3\right)=12s(s-t(s))>0
\]

in that entire box, so there is exactly one selected solution. Squared-rational interval comparisons certify

\[
 0.444491142719<t<0.444491142727.
\]

Thus `0.231083940855<x_*<0.231083940856` and `0.555508857273<y_*<0.555508857281`. Since `r2(q*)>0`, the zero-sum identity forces `r3(q*)=-3r2(q*)<0`, and

\[
 \beta_*=\frac{15}{16}\left[\frac{4x_*^2(1-x_*)+y_*^2(1-y_*)}5-\frac9{160}\right].
\]

The cubic `z^2(1-z)` increases for `0<z<2/3`, so direct rational interval evaluation gives the independently certified bounds

\[
 \boxed{0.0037791336185<\beta_*<0.0037791336191<0.00377914.}\tag{2}
\]

### 3.3 Universal per-source budget cap

For every feasible two-source pair, (1) and (2) imply for either source

\[
 b(q_i)\le 2\beta_*+E-b(q_{3-i})
 <2(0.00377914)+0.0022-0.003779
 =0.00597928<0.00598.\tag{3}
\]

The proof uses **no assumption** that `q*` minimizes `b` globally; this is why (1), not Stage346, supplies the other source's floor.

### 3.4 Fully exact tube exclusion and rational dominating point

Direct substitution gives

\[
 \boxed{b(Q)=408627/10^8=0.00408627,\quad c(Q)=130337110081/(4\cdot10^{12})=0.03258427752025.}\tag{4}
\]

A second exact Bernstein covering, now of the complete `[0,1]^2`, has **73 dyadic leaves**, maximum depth **31**. Each rectangle `R=[xl,xh]×[yl,yh]` passes at least one of three *strict* certificates:

1. **NO_R3_STRIP (26 leaves):** using monotonicity of `r3=(4x^3+y^3)/5-9/160`, either `r3(xl,yl)>1/2000` or `r3(xh,yh)<-1/2000`.
2. **B_OVER_CAP (26 leaves):** the exact TV/Bernstein lower bound `L_b(R)>299/50000=0.00598` excludes all budget-feasible source points by (3).
3. **Q_STRICT_DOMINATES (21 leaves):** exact lower bounds satisfy **both** `L_b(R)>408627/10^8` and `L_c(R)>130337110081/(4*10^12)`, proving the pointwise strict domination (4).

Here `L_c` is derived with the same source-preserving dual identity

\[
 D_3(a,z)=\max_{S\subseteq\{0,1,2,3\}}[P_S(a)-P_S(z)],
\]

using exact **upper** Bernstein coefficients for each `P_S(z)` to bound each of the four source-labeled `D3` terms **separately**. There is no numerical sampling or sign convention at an absolute-value equality boundary. The 73 leaf rectangles have exact total area 1, pairwise disjoint interiors, and closed coverage including all boundaries. A separate 37-leaf certificate independently excludes the sharp `r3=0` stratum (18 no-boundary, 12 over-budget, 7 dominance leaves).

Every point with `|r3|<=1/2000` and `b<0.00598` therefore belongs to a **strict-dominance** leaf. In particular, replacing it by `Q` reduces `b` and `c`, proving the theorem.

## 4. Reproducibility and certificate integrity

All identities, interval endpoints, polynomial coefficients, comparisons, leaves, area, pairwise interior disjointness, witness values, algebraic root isolation, and final budget relation are checked using Python's built-in `fractions.Fraction`, with assertions enabled. No floating-point value is used for a theorem check; decimal output is only for humans.

Execute in this directory:

```bash
python REPRO_STAGE355B.py --check
```

To independently regenerate CSV certificates (controlled overwrite of this folder's certificate files):

```bash
python REPRO_STAGE355B.py --write
python REPRO_STAGE355B.py --check
```

The script's `--check` mode reconstructs its exact deterministic bisection and requires **byte-equivalent parsed CSV rows**, then independently checks every recorded leaf condition, exact unit-square area, and pairwise nonoverlap. The execution stdout was reproduced twice with byte-identical output. Terminal success marker:

`STAGE355B_GLOBAL_TV_FLOOR_AND_R3_STRATUM_STRICT_DOMINATION_EXACT_PASS`

Artifacts: `REPRO_STAGE355B.py`, `REPRO_STAGE355B_EXECUTED_STDOUT.txt`, `CERTIFICATE_STAGE355B_B_FLOOR.csv` (67 leaves), `CERTIFICATE_STAGE355B_R3_DOMINATION.csv` (37 leaves), `CERTIFICATE_STAGE355B_R3_STRIP.csv` (73 leaves), and `NEXT_TASK_PACKET_356B.md`.

**Limits:** No unconditional global structure theorem has been established for all other residual-sign chambers; no exact P000 native X6, third slice coordinate, triadic closure, independent time, Cell-address codec, or future-operation-preserving bridge is claimed. All project mathematical admission and role-based reviews remain separate from author-executed exact arithmetic.

## 5. Next discriminating mathematical problem

Stage356-B should establish an analogous **exact exclusion or counterexample for `r0=0`** under the same budget ceiling, *or* classify the remaining b/c-active Pareto strata using a sourcewise exact sign chamber certificate. The new `r3` tube exclusion is a reusable constrained-domain lemma, not a substitute for the unreviewed full-model Stage352 condition. Avoid re-performing the 67/73-leaf checks unless the source-defined model changes.
