# R5 — Exact bad-budget interval certificates for finite-horizon common-source observers

Date: 2026-11-19. Status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**.

## Frozen science and provenance

**Research priority correction (current canonical-main readback, 2026-11-19):** BIS1–BIS3 already published the interval-union theorem, exact tail threshold and sharp unary holes at immutable commits 5bbb1bfe4997bc80159cadbb800fcd388d7d3655 and 19f4fc516d90cb74322b732623d50c69c1f4af55. HBC1–HBC4 here are an **independent replication and explicit boundary/transition presentation**, not priority claims. The new result in this branch is RESEARCH_COST_VISIBLE.md (CVA1–CVA4), which treats policies observing cumulative cost at each decision point and proves a distinct cost-visible equivalence and unary rigidity.

Continuation: BS1–BS4 at commit aea9c4b067520428a3489040690b1f5cb1d96a12, path research_notes/portable_direct/r5_budget_spectrum_20261119/RESEARCH.md.

Ancestor frozen scientific commit: 435e77af0d180eac32bd1f9c4c464bc4010b7551.
Earlier 256-state center-table SHA-256: 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b.
The previous computed inequality remains 8335 <= C8* <= 8343.

This is an exact theorem for the previously frozen **finite deterministic auxiliary positive-prefix observer**, not a native 256-state Bellman, negative-feedback, adaptive-branch or named-Port transfer. No P000/ACTIVE-worldview changes or BRC/Heartbeat arithmetic execution.

## Model

Let Ω be a finite set, A a nonempty finite action alphabet, T_a:Ω→Ω deterministic, L:Ω→2^[n] a named positive-support mask, and c_a:Ω→N a nonnegative integer cost. Fix x∈Ω, nonempty Y⊆Ω\{x}, finite horizon H≥0.

For a word w=a_1…a_t, T_{w_j}z is its state after the first j letters, and C_z(w)=Σ_{j=1}^t c_{a_j}(T_{w_{j-1}}z). The empty prefix j=0 is included. Set

D(w)={y∈Y : ∀j=0,…,t, L(T_{w_j}x)⊆L(T_{w_j}y)}.

Let m(w)=min_{y∈D(w)}C_y(w), taking m(w)=+∞ if D(w)=∅.

At budget B∈N, SAFE_H(B) means

∀w (|w|≤H and C_x(w)≤B ⇒ ∃y∈D(w): C_y(w)≤B).

A surviving representative must be the same initial response y for the whole prefix history of a fixed word; it can depend on the completed word.

## HBC1: Exact failure interval theorem

**Theorem.** Put I_w=[C_x(w),m(w)-1]∩N, with m(w)=+∞ giving [C_x(w),∞), and regard I_w as empty when m(w)≤C_x(w). Then

BAD_H={B∈N: ¬SAFE_H(B)}=⋃_{|w|≤H} I_w.

**Proof.** For fixed w the source is feasible iff B≥C_x(w). A compatible survivor is feasible iff B≥m(w); no such survivor exists when m(w)=∞. Therefore w witnesses failure precisely for C_x(w)≤B<m(w). Negate the universal quantifier over w and take the union. QED.

The equality also holds for unbounded words as a countable union; finite H gives an effective finite certificate.

## HBC2: Canonical connected certificate and breakpoints

**Theorem.** For finite H, discard empty intervals, order by left endpoint, then merge intersecting or consecutive integer intervals. The resulting list is the unique family of maximal connected integer components of BAD_H. SAFE_H is constant between consecutive component boundaries. Every budget verdict switch occurs at a threshold C_x(w) or finite m(w) for some |w|≤H.

**Proof.** Finite integer interval unions have unique maximal connected components. Membership in I_w can change only at its left endpoint or the first integer after its right endpoint, respectively C_x(w) and m(w). A union cannot change at any other point. QED.

To certify each merged component, retain a covering subfamily of **original** word intervals and the corresponding exact source/alternative costs. One arbitrary word per merged component is not in general enough to cover the whole component.

With N_H=Σ_{j=0}^H |A|^j, at most N_H nonempty failure intervals and at most N_H bad components exist. If at least one initial y has L(x)⊆L(y), the empty word contributes no interval and the bounds improve to N_H−1. There are at most twice as many adjacent-budget Boolean verdict transitions as components, with an infinite terminal component contributing only an entry transition.

An exact tree traversal computes cost vectors and prefix-compatibility flags for all words once; interval union then classifies **all budgets together** rather than separately running the budgeted observer for each B.

## HBC3: Sharp one-action horizon switching theorem

**Theorem.** If A={a}, Y={y} and the empty prefix is safe, then at horizon H the bad-budget set has ≤H connected components and SAFE_H has ≤2H adjacent-budget verdict transitions. For every H≥1, these bounds are attained using 3 states, one action, strictly positive integer costs and all labels identical and nonempty.

**Proof.** Only the H nonempty words a^1,…,a^H can produce nonempty intervals. Each interval creates at most one connected component, with at most two transitions. For equality take Ω={x,y,z}, T_a(x)=x, T_a(y)=z, T_a(z)=z, L≡{1}, and costs q,q+d,q at x,y,z, for integers q≥2, 1≤d<q. Then C_x(a^t)=qt and C_y(a^t)=qt+d, giving I_{a^t}=[qt,qt+d−1]. These H intervals are pairwise separated because d<q, so precisely H components and 2H changes occur. QED.

For q=2,d=1,H=8: BAD_8={2,4,6,8,10,12,14,16}; SAFE_8 holds at 0,1, all odd budgets and all B≥17. By contrast BS2's **unbounded** model has infinitely many unsafe positive even budgets.

## HBC4: Exact terminal stabilization

Let c_max=max_{z,a}c_a(z). For every B≥Hc_max every response can execute every word of length ≤H, hence SAFE_H(B) iff D(w)≠∅ for all |w|≤H. If one D(w) is empty, the associated interval has an infinite right tail and large-budget status is unsafe. If all are nonempty, all I_w end before Hc_max and large-budget status is safe.

The exact earliest budget after which the verdict is constant is 0 if BAD_H is empty; otherwise, for the **last** merged component, its right endpoint plus 1 if finite, or its left endpoint if unbounded. The uniform Hc_max bound is safe but need not be sharp. This refines predecessor BS4 from eventual stabilization to an explicit optimal finite certificate of the entire budget spectrum.

## Reproducible verification

VERIFY_INTERVAL_CERTIFICATES.py independently (i) enumerates all fixed words and computes each interval from exact prefix compatibility and minimal compatible cost and (ii) directly checks the original SAFE_H quantifiers separately for each tested budget. Using fixed PRNG seed 20261119 it compared 1,800 independent random systems of 2–5 states, 1–3 actions, 0≤H≤4, costs 0..3 and support bitmasks 0..7, yielding **25,263** matching budget verdict comparisons. Separately it covered q=2..9, 1≤d<q, H=0..8: 324 family/horizon instances and 14,364 exact budget checks against the closed intervals. Result: PASS_R5_HORIZON_INTERVALS. The assertions verify finite cases; HBC1–HBC4 are supported by the separate symbolic proofs.

## Native connection and next scientific frontier

The frozen R5 256-state Bellman system may use adversarial/negative observation, adaptive query choices, explicit Port-source coupling and action-dependent branching. Its correct observer quantifiers, physical cost semantics and source residual must be read and mapped before applying HBC certificates to native state elimination. An "eight-error" task name alone does not prove the corresponding action horizon equals H=8. Next: extract one fully sourced, actual native Bellman branch/cost/Port trace and test the theorem's exact deterministic fixed-word hypothesis, or obtain an explicit state repair when it fails.

Formal CLAIM/RUN: none created by this theorem. Activity attachment and independent review are separate processes. Review: NOT_REVIEWED.
