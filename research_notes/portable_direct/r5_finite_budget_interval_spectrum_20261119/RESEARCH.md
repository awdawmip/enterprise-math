# R5 — Finite-horizon budget safety: exact witness-interval certificate

Date: 2026-11-19. Scientific status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**.

## Immutable scientific source and exact scope

Predecessor: \`awdawmip/enterprise-math@aea9c4b067520428a3489040690b1f5cb1d96a12:research_notes/portable_direct/r5_budget_spectrum_20261119/RESEARCH.md\` (BS1–BS4). Model: BCPT1–3 at \`78ef1422e6d661ace839b0c2ad916b7f50e40518\`. Original frozen scientific pin **435e77af0d180eac32bd1f9c4c464bc4010b7551** is unchanged; historical center-table SHA-256 **50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b** was not recomputed.

This result concerns a **finite deterministic auxiliary source-faithful positive-prefix observer**, not a native R5 256-state Bellman/Port proof. Current P000 and Heartbeat World X6 foundations are unchanged. No quotient/collapse is asserted safe for negative feedback, branch/source identity, future native operations or BRC without an exact transfer certificate.

## Model

Let Ω be a finite response set, A a finite action alphabet, T_a:Ω→Ω deterministic, c_a:Ω→ℕ a nonnegative *integer* cost, and L:Ω→2^[n] a named positive-support label. Fix x∈Ω, a nonempty finite replacement set Y⊆Ω∖{x}, and finite word horizon H≥0. For w∈A* let C_z(w) be its cumulative transition cost starting at z (zero for the empty word). D_y(w) asserts label inclusion L(T_{w_j}x)⊆L(T_{w_j}y) at **every prefix**, including the empty prefix. One common representative y must cover the whole word but may depend on the completed word.

The declared fixed-word safety predicate is

$$
\operatorname{SAFE}_H(B)\ \Longleftrightarrow\
\forall w\in A^{\le H},\ C_x(w)\le B
\ \Rightarrow\ \exists y\in Y:\ D_y(w)\ \wedge\ C_y(w)\le B.
$$

Define m(w)=min{C_y(w):y∈Y and D_y(w)}, with min∅=+∞.

## BIS1 — Exact bad-budget interval theorem

**Theorem.** For every integer budget B≥0,

$$
\boxed{\{B:\neg\operatorname{SAFE}_H(B)\}=
\bigcup_{\substack{w\in A^{\le H}\\m(w)>C_x(w)}}
([C_x(w),m(w)-1]\cap\mathbb N).}
$$

If m(w)=+∞, the interval is the unbounded integer ray [C_x(w),+∞).

**Proof.** A fixed word w falsifies the budget-safety implication precisely when C_x(w)≤B but no full-prefix-compatible representative has cost ≤B. By the minimum's definition the latter is equivalent to B<m(w). These two inequalities define exactly the listed interval, with the correct empty and infinite cases. Negating the universal quantifier over all words gives their union. Since H and A are finite, this is a finite union. QED.

The exact word w is a reproducible certificate of every individual unsafe interval; the union/complement gives the exact verdict at **every budget** from one finite-word enumeration, not one repeated budget search.

## BIS2 — Exact eventual behavior and improvement over BS4

Merge overlapping or adjacent witness intervals. There are at most Σ_{j=0}^H |A|^j connected integer components. If at least one word has m(w)=∞, then all B≥B₀ are unsafe, where B₀=min_{w:m(w)=∞} C_x(w). B₀ is a valid eventual-unsafety bound, potentially not the **least** such bound due to preceding joined intervals.

If all words admit a prefix-compatible representative, let W₊={w:m(w)>C_x(w)}. If W₊ is empty, every budget is safe. Otherwise the **exact least permanently-safe budget** is

$$
\boxed{B_{\rm safe}^{\rm tail}=\max_{w\in W_+}m(w).}
$$

**Proof.** Each finite bad interval has greatest point m(w)−1; the greatest bad point over all words is max m(w)−1. Thus one larger budget is the least one after which all are safe. For every word |w|≤H and every candidate y, C_y(w)≤Hc_max, c_max=max_{a,z}c_a(z). Therefore B_safe^tail≤Hc_max. QED.

This sharpens BS4's generic finite-horizon stabilization threshold, without claiming any unbounded-horizon stabilization.

## BIS3 — H disconnected budget holes with one action (sharp)

Reuse the earlier BS2 family Ω={x,y,z}, A={a}, Y={y}, T_a(x)=x, T_a(y)=z, T_a(z)=z, all three labels equal and nonempty, with costs (q,q+d,q), q≥2 and 1≤d<q. For t≥1, C_x(a^t)=qt and m(a^t)=qt+d; the empty word has both costs zero. Therefore

$$
\boxed{\operatorname{BAD}_H=\bigcup_{t=1}^{H}[qt,qt+d-1]\cap\mathbb N.}
$$

These H intervals are pairwise separated, achieving the H-component unary upper bound whenever the empty-word label is covered. Every budget B≥qH+d is safe; this is the **exact least** permanently safe budget. At (q,d,H)=(2,1,8), the eight unsafe budgets are exactly 2,4,6,8,10,12,14,16, and safety holds from B=17 onward. BS4's general bound would be Hc_max=24. The infinite alternation in unbounded BS2 is therefore genuinely a horizon effect.

## Exact computational checks

The companion Python program constructs the interval certificate and compares it to an **independently written budget-first direct word/prefix replay**, using integer costs and bit-mask containment, never floating-point arithmetic.

- Complete finite class: all 27 transitions on three states for one action; all 64 two-bit named label assignments; all eight {0,1}-cost assignments. Fixed x=0, Y={1,2}, H=5. Exactly **13,824 models × 9 budgets (0..8) = 124,416 checks**, all matching.
- Separate deterministic sample: **4,096** four-state, two-action models with random seed 20261119, two-bit named labels, cost range {0,1,2}, nonempty candidate subsets, H=4. All **45,056** checks over budgets 0..10 matched.
- Directly checked the full 26-budget range B=0..25 for the H=8 sharpness witness. In the complete unary class, **6,312** models had an unbounded bad interval, and the component-count distribution was 0:5,781; 1:8,035; 2:8.

These are scope-typed finite arithmetic checks, **not** universal computational proof beyond the declared classes. BIS1–BIS3 have the direct mathematical proofs above. Source program: VERIFY_INTERVAL_SPECTRUM.py. Expected machine output: \`PASS_R5_INTERVAL_SPECTRUM 13824 124416 4096 45056 2 6312\`.

## Remaining scientific target

For the *real* frozen 256-state eight-error Bellman objective, reconstruct the typed action and feedback semantics, Port identity, positive/negative responses, adaptive policy-tree decisions and cost. Establish an exact observer/transition-factorization certificate **before** applying an interval compression or deleting an R5 source direction. For a multi-action fixed-word auxiliary class, consider reducing word enumeration with proven frontier dominance while retaining source and branch information. Only if the mapping is proved can budget-interval certificates be used to screen the nine-state hard classes. The previously reported bound **8335≤C₈*≤8343** is unchanged.

No formal Task CLAIM/RUN, Result, independent review, Working Truth or P000 promotion is asserted.