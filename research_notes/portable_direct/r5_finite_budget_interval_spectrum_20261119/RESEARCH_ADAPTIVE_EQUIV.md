# R5 — Full-feedback equality-prefix bridge to adaptive policies

Date: 2026-11-19. **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**. Supplement to BIS1–BIS3 in the same research branch. Frozen scientific input remains **435e77af0d180eac32bd1f9c4c464bc4010b7551**, unchanged.

## Exact scoped question

Let Ω be a finite set of response states, A a finite action alphabet, each T_a:Ω→Ω deterministic, c_a:Ω→ℕ a nonnegative integer cost, and O:Ω→Σ the **complete discrete feedback** available to a decision policy. Fix original x, nonempty finite candidate Y and horizon H≥0.

For an action word w let E_y(w) mean **exact equality** O(T_{w_j}x)=O(T_{w_j}y) at every prefix j including the empty prefix. The wordwise full-feedback replacement property at budget B is

$$
F_H(B):\ \forall w\in A^{\le H},\quad C_x(w)\le B
\ \Rightarrow\ \exists y\in Y:\ E_y(w)\land C_y(w)\le B.
$$

A deterministic adaptive policy π can select its next action or STOP from the observed history (up to H actions). For each starting state it generates one definite trace. Define A_H(B): for **every** such π whose run from x costs at most B, there is a **single initial candidate y for that policy** whose run under π has the same entire observation/action trace and whose total cost is at most B. Distinct policies may use distinct candidates. Cost is tested for feasibility; the policy does not branch on an invisible running cost unless that cost is explicitly added to the feedback O.

## BAE1: Full-feedback wordwise and adaptive equivalence

**Theorem.** Under the preceding deterministic, observation-complete and finite-horizon hypotheses,

$$
\boxed{A_H(B)\ \Longleftrightarrow\ F_H(B).}
$$

**F⇒A:** Fix π and its realized run from x. Let w be its action word; |w|≤H and C_x(w)≤B. F supplies a candidate y such that all prefix feedback along w is identical and C_y(w)≤B. By induction on steps, π sees the same initial feedback from x and y, hence chooses the same first action; after each action it receives the same feedback again and must make the same next decision, including STOP. Therefore π's entire y-trace follows w, equals the x-trace, and remains affordable.

**A⇒F:** For any w, select the deterministic policy that ignores observations and executes precisely w then STOP. Its action trace is w from every state. A supplies y with the identical observation trace and C_y(w)≤B whenever C_x(w)≤B. That is E_y(w), establishing F for all words. QED.

**Interval consequence:** BIS1 applies directly with the exact-feedback replacement cost
m_eq(w)=min{C_y(w):y∈Y and E_y(w)} (empty minimum +∞). Thus the finite union of bad-budget intervals [C_x(w),m_eq(w)−1] is also an exact all-budgets certificate for **every deterministic observation-only adaptive policy** up to the stated horizon. It does not require enumerating each policy tree to compute the certificate, once the word family is enumerated.

## BAE2: Inclusion-only observation is insufficient

Let two response states have complete observable labels O(x)={p} and O(y)={p,q}, with identity transitions and all costs zero. Positive-label inclusion O(x)⊆O(y) holds at every prefix of every word. However exact feedback already differs at the empty prefix, allowing an adaptive policy to choose a different first action on the extra observed label q. Consequently positive-prefix containment alone cannot replace exact full-feedback equality for this policy class. An observer-specific quotient may be valid only after its own exact semantics/preservation proof.

## Reproducible precision and source

The companion independent Python test enumerates both **all fixed words** (length≤2) and **all deterministic observation-only policies** of depth 0, 1 and 2, with binary observation alphabet and two actions. Policies choose the first action based on the initial observation, and the second based on the initial and first-post-action observations.

- Exhaustive class: 16 pairs of two-state action transformations × 4 binary full-observation assignments × 16 binary cost assignments = **1,024 finite systems**. With B=0,1,2 this yields **3,072 matching fixed-word/adaptive decisions**.
- Separate seed-20261119 sample: **2,048** three-state two-action systems with two alternative representatives, **6,144** budget decisions, all matching.
- Positive containment versus full-feedback inequality checked with labels 1 and 3 (set masks).
- Exact integer/Boolean arithmetic; the computational domain is the declared finite subset. The universal theorem is proved above, not extrapolated from samples.

Expected output: \`PASS_R5_ADAPTIVE_EQUIVALENCE 1024 3072 2048 6144\`. Verifier file: VERIFY_ADAPTIVE_EQUIV.py. Result certificate: RESULT_ADAPTIVE_EQUIV.json.

## Native bridge obligation

The actual 256-state R5/Bellman system may include negative feedback, signed Port/source identity, cost-aware adaptive decisions, shared counterfactual branches and other observations that O does not yet encode. One must pin its genuine decision/observation semantics and verify those are wholly represented by O; otherwise this theorem is **not** a native R5 compression, and the existing bound **8335≤C₈*≤8343** remains unchanged. P000/Heartbeat World six-dimensional spatial basis, independent time and joint-relation retention are unchanged.

This is new scoped mathematical evidence, **not** formal CLAIM/RUN, Result, independent review or P000 promotion.