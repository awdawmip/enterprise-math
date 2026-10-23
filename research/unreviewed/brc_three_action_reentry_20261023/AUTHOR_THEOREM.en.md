# Three-action reentry in the four-label auxiliary BRC occupancy observer

**Status: author-side exact counterexample, 2026-10-23; UNREVIEWED, NOT ADMITTED, NOT NATIVE X6.**

## 1. Previously established boundary and new experiment

The unreviewed two-action theorem at commit `3f9f112e83838e65c599b844bf26095e0f949ddd` applies to public words over **{0,2}**, not arbitrary future actions. We keep its four hidden labels `{0,1,2,3}`, the exactly-good occupancy sets `G={{0,1},{1,2},{1,3},{2,3}}`, and the two original independent positive-mass action laws:

`q_0(z)=(0,1+z,1-z,1)/3`, `q_2=(1,1,0,1)/3`, `0<=z<=1`.

Add just one action: **`q_3=(0,0,0,1)`**, a deterministic draw of the existing hidden label 3. No new hidden label, negative mass, signed amplitude or phase is introduced.

Let `D_t` be the set of distinct labels sampled by time `t`, `delta_t=Pr(D_t in G)`, `delta_0=0`, `Delta_t=delta_t-delta_(t-1)`, `M_t=max_{s<=t} delta_s`, and `R_t=sum_{j=2}^t max(0,Delta_j)-M_t`. Residual growth is strict if `R_t>R_(t-1)`.

## 2. Global-parameter reentry counterexample

For the exact public word `w=032020` (six actions), direct inclusion-exclusion gives these **polynomial identities**, valid for every real `0<=z<=1`:

```
delta_1 = 0
delta_2 = 2/3
delta_3 = (z+4)/9
delta_4 = (3*z^2+4*z+10)/27
delta_5 = (5*z^2+12*z+18)/81
delta_6 = (3*z^3+30*z^2+36*z+38)/243
```

The load-bearing exact occupancy law is, for every good pair `{i,j}`,

`Pr(D_t={i,j}) = product_s(q_(w_s,i)+q_(w_s,j)) - product_s(q_(w_s,i)) - product_s(q_(w_s,j))`.

Summing this disjoint partition over the four good pairs proves the six displayed expressions directly by integer polynomial expansion; the independent polynomial checker in the companion file verifies the coefficients.

For `0<=z<=1`, the expressions show `delta_t<2/3` for `3<=t<=6`; thus `M_t=2/3` for `2<=t<=6`, and every strictly positive occupancy increment after round 2 produces exactly the same positive increment in residual.

The four relevant occupancy increments are

```
Delta_3 = (z-2)/9                          <0
Delta_4 = (z+1)*(3*z-2)/27
Delta_5 = -4*(z*z+3)/81                     <0
Delta_6 = (3*z^3+15*z^2-16)/243.
```

Let `rho` be the unique root of `P(z)=3*z^3+15*z^2-16` in `(0,1)`. Uniqueness follows from `P'(z)=9*z^2+30*z>0` on `(0,1]`, plus `P(0)<0<P(1)`; exact rational substitutions give `947/1000<rho<948/1000`. In particular `rho>2/3`. Consequently **for every `rho<z<=1`, the residual strictly increases at exactly rounds 4 and 6, with a non-growing round 5 between**. The strict-growth-time set is `{4,6}`, not an interval. This is a new-action counterexample to extending the older two-action theorem without hypotheses on the allowed action family. It does not refute the theorem on its original `{0,2}` domain.

At the rational endpoint `z=1`, the exact auditable rows are:

| round | action | delta | Delta | M | R | residual gain |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2 | 3 | 2/3 | 2/3 | 2/3 | 0 | 0 |
| 3 | 2 | 5/9 | -1/9 | 2/3 | 0 | 0 |
| 4 | 0 | 17/27 | 2/27 | 2/3 | 2/27 | **2/27** |
| 5 | 2 | 35/81 | -16/81 | 2/3 | 2/27 | 0 |
| 6 | 0 | 107/243 | 2/243 | 2/3 | 20/243 | **2/243** |

## 3. Finite sharpness (explicitly restricted)

Fix `z=1`, the two original actions, the same good sets and the same residual definition. Let the one new action be any **deterministic** draw `q_3=e_j` of one of the four existing labels `j in {0,1,2,3}`. Exhaustive exact integer enumeration of **all words of lengths 1..5** (`4*(3+9+27+81+243)=1452` cases) finds no separated strict-growth episodes. At length 6 (another 2916 cases), exactly six words, all for `q_3=e_3`, have reentry: `032020, 032030, 223020, 223030, 302020, 302030`. Therefore six is the *minimum word length in this restricted deterministic one-action extension at the fixed parameter z=1*. No universal minimality over stochastic added actions or other parameters is asserted.

The verifier implements a 16-state occupied-label bitmask recurrence with **integer numerators / 3^t**, an independent good-pair inclusion-exclusion formula, exact polynomial arithmetic in z, and rational parameter checks. The two distinct occupancy implementations agree on all 4,368 words across labels and lengths 1..6. The six explicit polynomial coefficient arrays and 42 rational polynomial checks agree. Finite exhaustion certifies only the stated finite class; the continuum `z>rho` result follows from the explicit polynomial identities.

## 4. Research significance and next exact problem

The one-episode invariant requires hypotheses on **future public operations**, not just four-label hidden-state cardinality and nonnegative weights. This witness changes neither hidden labels nor the exact good-set observer; it only adds a deterministic operation. It is a typed positive-mass BRC counterexample inside an auxiliary model.

Next: characterize action families `Q` that guarantee no separated strict residual-growth episodes for all words; find necessary/sufficient testable inequalities on their inclusion-exclusion product vectors, or prove a scope-limited obstruction. Separately, the native P000 X6 embedding, three-dimensional slice and third-coordinate semantics, readout and permitted-future-operation preservation remain **unproved**.

## 5. Provenance, identity and status

- Previous author-only source: `awdawmip/enterprise-math@3f9f112e83838e65c599b844bf26095e0f949ddd`, `research/unreviewed/brc_one_growth_episode_20261023/ONE_EPISODE_AUTHOR_PROOF.en.md`.
- Pinned global source: `awdawmip/chatgpt-global-knowledge@674c44f8c3c194a82c63f0bba6da995d1d307ad3`; pinned EM main: `awdawmip/enterprise-math@1fbbbb3b9541952974f67e1c4c803047c79199f3`. Global P000 projection matches original blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`.
- BRC reuse: existing exact occupied-pair formula and 16-mask verifier, **EXTEND_EXISTING_TOOL** with action 3; positive rational branch masses, no signed cancellation.
- Authenticated GitHub actor `awdawmip` has GitHub repository write permission, but the native `em_control_tasks`/`em_control_dispatch` returned `CONTROL_QUOTA`, and `em_session_start` was denied `STATIC_READONLY_SCOPE_DENIED` with `operation_sent=false`. Thus no authoritative live Owner, formal research session, task CLAIM, Result admission, independence review or native X6 theorem is claimed. This is a readback-verifiable unreviewed author-side artifact only.
