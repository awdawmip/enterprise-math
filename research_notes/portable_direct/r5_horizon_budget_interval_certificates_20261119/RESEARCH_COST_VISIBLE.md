# R5 — Cost-visible adaptive policies: exact trace theorem and budget-spectrum collapse

Date: 2026-11-19. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## Source and improvement

Predecessors: BIS1–BIS3, the exact finite-horizon witness-interval theorem at Enterprise Math commit 5bbb1bfe4997bc80159cadbb800fcd388d7d3655, and BAE1 full-feedback adaptive equivalence at 19f4fc516d90cb74322b732623d50c69c1f4af55. Those were **already published** before this run; the sibling RESEARCH.md is an independent replication/refinement of BIS, not a distinct priority claim for the interval theorem.

**New scope:** A policy sees both the exact feedback symbol O and the **running cumulative integer cost** at each decision point, and can choose an action or STOP. Its required matching trace records the chosen actions and O values; total cost is a feasibility condition, not itself required to be identical at the forced horizon. This explicit cost-visible extension is distinct from BAE1's policy, which sees only O.

Model: finite Ω, nonempty finite A, deterministic T_a, O:Ω→Σ, nonnegative integer c_a, original response x, nonempty candidate set Y, action horizon H≥0, budget B≥0. For a word w of length t let O_z(w_j) and C_z(w_j) be its exact prefix feedback and cumulative cost from z. The prefix j=0 is included and C_z(empty)=0.

Define CV_y^H(w) by:
(1) O_y(w_j)=O_x(w_j) for all 0≤j≤t;
(2) C_y(w_j)=C_x(w_j) for all 0≤j≤t if t<H, or for all 0≤j<t if t=H.

The distinction at t=H is essential: a policy has no decision after its mandatory horizon, so a difference in *final* cost cannot change its action trace. The final O is still explicitly part of the matching trace.

Define F_CV,H(B): for all words w with |w|≤H and C_x(w)≤B, there exists y∈Y with CV_y^H(w) and C_y(w)≤B.

Define A_CV,H(B): for **every** deterministic policy that chooses the next action or STOP from the observed history of O and cumulative costs, and whose actual source-x run ends within H actions and budget B, there exists one initial y∈Y such that running **that same policy** from y yields the same O/action trace, and the candidate run also ends within budget B.

## CVA1 — Exact cost-visible adaptive-wordwise equivalence

**Theorem.** A_CV,H(B) if and only if F_CV,H(B), for every fixed B≥0.

**Proof F⇒A.** Fix a policy π and the word w it executes from x. F gives a y with the same O values at all prefixes, the same cumulative costs at every decision prefix before the forced horizon, and an affordable total. At j=0 both histories coincide. Suppose the policy has followed w from both states up to a decision j<t. Since j<H, the O and C histories agree, so the deterministic π chooses the same next action at y. At the source stopping decision j=t<H, the histories agree too, so π chooses STOP from y. At t=H both runs must terminate by the horizon. The O/action traces and affordability therefore coincide.

**Proof A⇒F.** Fix any word w of length t≤H with C_x(w)≤B. Construct a policy that, at each decision j<t, follows action a_(j+1) only if its entire O/cumulative-cost decision history agrees with the specified source-x history of w; it chooses STOP if that history differs. If t<H, at its final decision j=t it chooses STOP exactly on the original source history and chooses some action in A otherwise; if t=H, STOP is forced. Thus from x it executes exactly w. Any y whose run has the same O/action trace must have coinciding O at every prefix and coinciding cost at every decision prefix (otherwise the policy diverges), and must finish within B. Hence it satisfies CV_y^H(w) and is affordable. Since w was arbitrary, F holds. QED.

In particular the condition does not erroneously force equality of terminal cumulative costs when |w|=H.

## CVA2 — Exact interval classification with a stronger compatibility relation

For each word w define m_CV(w)=min{C_y(w):y∈Y, CV_y^H(w)}, or +∞ if no candidate exists. Applying BIS1's elementary source-affordability argument with the new compatibility predicate yields

BAD_CV,H = union_{|w|≤H} [C_x(w),m_CV(w)−1]∩N,

with the same infinite-ray convention. For each **shorter word |w|<H**, the CV condition already requires C_y(w)=C_x(w), so its window is either empty (some candidate exists) or the **permanent unsafe ray** [C_x(w),∞) (none exists). The only budget-sensitive bounded windows can come from terminal words |w|=H.

This sharply separates observation incompatibility **before a decision** from a terminal affordability difference.

## CVA3 — At most one bad-budget component for a one-action cost-visible policy

**Theorem.** If A={a}, cost-visible adaptive matching up to any finite H has either an empty bad set, a single finite integer interval, or a single infinite integer ray. Thus SAFE_CV,H changes at most twice as B increases.

**Proof.** If any shorter prefix a^t, t<H, lacks a CV-compatible y, CVA2 gives [C_x(a^t),∞). Since all costs are nonnegative, C_x(a^H)≥C_x(a^t), so this ray contains the only possible terminal word a^H failure interval. All other shorter failure rays are nested because C_x(a^j) is nondecreasing. Their union is one ray. If all shorter words have a compatible y, each contributes no interval and at most the sole terminal word a^H contributes one finite interval or ray. H=0 is the same one-word terminal case. QED.

This is a stronger rigidity statement than the O-only unary system: in the earlier BS2/BIS3 construction, the latter can have **H disconnected budget holes**.

## CVA4 — Minimal cost-visibility separation and the previous periodic family

**Two-state, one-action example.** Ω={x,y}, Y={y}, T_a=identity, O(x)=O(y)=same symbol, c_a(x)=1 and c_a(y)=2, H=2 and B=4. For every word a^t with t≤2, both runs have equal O and C_y(a^t)=2t≤4, so the **O-only** wordwise property F_O,H(B) holds. However the policy “execute a once; then execute a again exactly when observed cumulative cost equals 1, otherwise STOP” yields source trace aa but candidate trace a. Therefore cost-visible adaptive matching fails. This example has the minimum possible number of response states when one state is deleted and a distinct alternative remains, uses strictly positive costs and a single action.

**Strengthened old-family classification.** In the BS2 family with costs (q,q+d,q), q≥2, 1≤d<q, and all O identical: at H=1 the only nonempty failure interval is [q,q+d−1]; at every H≥2 the first-action cumulative costs q and q+d disagree at a decision point, so the one-letter word yields the permanent ray [q,∞). Hence CVA1–3 yield SAFE_CV,H(B) iff B<q for H≥2. The unbounded O-only periodic pattern becomes a permanent unsafe tail in the cost-visible policy model.

## Verified finite evidence

VERIFY_COST_VISIBLE.py independently enumerates all depth-two deterministic policy maps over reachable O/cumulative-cost histories (including STOP) and separately computes the wordwise CV predicate. It tests 600 seeded random finite systems (2–3 states, 1–2 actions, 0/1 feedback values, transition costs 0..2) at budgets 0..4: **3,000 exact policy/wordwise decisions all agree**. Among those, 585 cases satisfy O-only fixed-word safety but fail cost-visible adaptive safety. The explicit 2-state example is checked separately.

Output: PASS_R5_COST_VISIBLE 3000 585. Random computation validates a finite sample; CVA1–4 rely on the direct proofs above.

## Native Bellman consequence and remaining work

A real error-budget Bellman controller can know its remaining budget. If it observes the **exact number of spent errors**, its semantics is closer to CVA1; if only the binary question “still under budget?” is visible, O-only BAE1 extends to that binary flag under nonnegative costs, because a source-feasible and candidate-feasible completed word has all prefixes affordable. These distinct information models give different safe state quotients.

The actual frozen R5 256-state Bellman feedback, budget readout, signed Port/source tracking, and decision history have not been mapped to this auxiliary deterministic model. Extract one genuine native policy interface before applying CVA3 as a state-pruning theorem. The source pin remains 435e77af0d180eac32bd1f9c4c464bc4010b7551; original bound 8335≤C8*≤8343 remains.

Formal CLAIM/RUN: not created; independent review: NOT_REVIEWED.
