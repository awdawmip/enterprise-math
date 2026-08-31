# EXPLORATION_TRACE — R035 Project Arm

Researcher-ID: `EM-R035-6F2A91`  
Arm: `PROJECT`  
Task: `RS-R035-POLYGONAL-REFINEMENT-ENDPOINT-DYNAMICS`

This trace is chronological. It intentionally preserves false/narrowed routes instead of rewriting the run as if the final theorem decomposition had been known in advance.

## 2026-08-12T13:23+08:00 — task intake

Read the portable R035 package, verified its manifest hashes, and read the official taskbook at source commit `58346f6a473f681730f3ffc2f70ff2d5de899a14`. No mathematical project-history/tool-library search had yet been performed.

## 2026-08-12T13:23+08:00 — INITIAL_EXPLORATION_CHECKPOINT frozen

Before deliberate project-history, external-literature, or reasoning-tool search, froze `INITIAL_EXPLORATION_CHECKPOINT.md` with the actually present ideas:

- lower map `F(k)=L_s(rP_s(k))` plus an exact-hit endpoint bit;
- discriminant/basin-residual coordinate;
- ordered parent-child blocks and interval/gap support geometry;
- controls `r=1`, `s=4`, square/non-square `r`;
- uncertainty whether supports expand combinatorially or collapse to a short carrier.

## 2026-08-12T13:24+08:00 — first deliberate global/process search

Bootstrapped `GLOBAL_KNOWLEDGE_V1` at `main@efd0c162b651055d484138465f37bd7e483a5066` and read the Enterprise Math liveness/owner-isolation rules. This changed process discipline (remote-silent hot path, evidence separation, do not stop at soft blockers), not the R035 theorem decomposition.

## 2026-08-12T13:26+08:00 — exact oracle established

Implemented exact integer `P_s`, `L_s`, endpoint support, one-step and multi-step support, incidence, duplicate/recoalescence statistics, and actual-value/index bridge. Lower-index inversion used integer square root and exact inequalities only.

Early scans immediately killed the naive idea that set-support cardinality should simply double: distinct parent branches can hit the same child. This made parent incidence a first-class diagnostic observable without changing the frozen set semantics.

## 2026-08-12T13:29+08:00 — discriminant coordinate became structural

With `a=s-2`, `c=s-4`, found

`P(k+1)-P(k)=ak+1`

and the lattice discriminant coordinate

`z_k=2ak-c`, with `c^2+8aP(k)=z_k^2`.

For the lower map `F(k)=L_s(rP(k))`, derived the real inverse coordinate

`phi(k)=(c+sqrt(r z_k^2-(r-1)c^2))/(2a)`.

This turned the initial “residual coordinate” idea into a usable exact arithmetic coordinate and exposed the generalized Pell equality surface for exact hits.

## 2026-08-12T13:32+08:00 — universal lower-map jump bound

Proved, independently of finite scans,

`1 <= F(k+1)-F(k) <= r`.

This established strict order/injectivity of `F`: every parent has a distinct lower child and set-support cardinality can never decrease.

Because each parent block has width at most one, strict order also implied that only adjacent numerical parents can ever share a child, and any overlap is a simple two-parent event.

This yielded the exact finite-support accounting law

`|D(S)| = 2|S| - H - C`,

where `H` counts exact-hit unary parents and `C` counts duplicate-edge excess/recoalescence events.

## 2026-08-12T13:34+08:00 — interval conjecture attacked

A strong conjecture emerged naturally from low factors: perhaps singleton-root supports remain integer intervals. Direct attack found the earliest factor-5 failure in the triangular world:

`(s,r,k0)=(3,5,1): {1} -> {2,3} -> {5,7,8}`.

The global “all-r interval” claim was therefore killed. The surviving question became whether there is a sharp factor boundary rather than sporadic failure.

## 2026-08-12T13:36+08:00 — derivative lower bound and separated regime

For positive `k`, computed

`phi'(k)=r z_k/sqrt(r z_k^2-(r-1)c^2) >= sqrt(r)`.

Hence

`F(k+1)-F(k) >= floor(sqrt(r))`.

This immediately proved that for `r>=4`, positive adjacent parent blocks are disjoint. Together with the origin, `r>=4` has no parent-to-child recoalescence at all. The arithmetic had therefore produced a clean representation split: low factors can merge; `r>=4` is a separated forest.

## 2026-08-12T13:38+08:00 — r=2 and r=3 interval mechanism

For `r=2`, the general jump bound leaves jumps 1 or 2, and an exact-hit comparison forces the next jump to 1. Therefore every positive parent interval maps to an interval.

For `r=3`, parity-based lower estimates sharpened the jump upper bound to 2; exact-hit comparisons again force the neighboring block to close the potential gap. Therefore every positive parent interval maps to an interval.

At this stage the data suggested `r=4` might be the exact critical crossing rather than merely the first separated factor.

## 2026-08-12T13:40+08:00 — r=4 solved exactly

Found the identity

`P_s(2k)-4P_s(k)=(s-4)k`.

This yielded the exact child rule for positive `k`:

- `s=3`: `{2k,2k+1}`;
- `s=4`: `{2k}`;
- `s>=5`: `{2k-1,2k}`.

The full singleton orbit therefore has a closed dyadic interval/singleton form. At this point `r<=4` all had universal singleton interval dynamics, while `r>=4` had universal branch separation.

## 2026-08-12T13:42+08:00 — project-history search performed only after structure existed

Fetched existing `EnterpriseMath/Relation/BranchRecoalescence.lean`. It roots generic relation/direct-image/set-union/recoalescence semantics and confirmed that the R035 set semantics fits an existing project abstraction.

Direction change: the new R035 arithmetic statement for `r>=4` was recognized as stronger than generic exact recoalescence semantics: it is reverse-functionality/unique-parent genealogy. No old theorem supplied the polygonal factor threshold.

## 2026-08-12T13:44+08:00 — independent holdout and theorem narrowing

Built `experiments/r035_holdout.py` using monotone integer doubling/binary search for `L_s`, deliberately independent of the discriminant/isqrt closed form. On disjoint/larger parameter regions it completed `321,118` counted checks with no mismatch, including `n<=10^20`, `k<=10^8`, `s<=150`, `r<=200`, and the full taskbook one-step sanity window.

A proof statement was narrowed during this pass: the `r=2,3` interval-to-interval theorem must require a **positive** parent interval. The artificial interval `{0,1}` at `(s,r)=(3,3)` maps to `{0,2}`. Default singleton dynamics is unaffected because `k0=0` is fixed and positive roots never reach zero.

## 2026-08-12T13:46+08:00 — two sharp factor classifications

The factor-5 counterexample generalized uniformly. For every `r>=5`, choose `s=r+1`, `k0=1`. Then `S1={1,2}` but `rP_s(2)=r(r+1) >= P_s(4)=6r-2`, so parent 2's children start at index at least 4 while parent 1 again contributes `{1,2}`. Thus `S2` misses 3.

Therefore:

**Universal singleton-root interval dynamics for every `s,k0,t` holds iff `r<=4`.**

Separately, concrete triangular adjacent-parent overlaps were found for the two unresolved factors:

- `r=2`, parents `3,4` share child `5`;
- `r=3`, parents `8,9` share child `15`.

Combined with the `r>=4` proof and the `r=1` identity:

**Universal no-recoalescence across distinct parents holds iff `r=1` or `r>=4`.**

Thus `r=4` is the exact crossing of two independently defined properties.

## 2026-08-12T13:48+08:00 — square control and exact-hit arithmetic

For `s=4`, `P(k)=k^2` gives a complete control world:

- square `r=q^2`: unary scaling `{k}->{qk}`;
- nonsquare `r`: no positive exact hits, child block `{floor(sqrt(r)k), floor(sqrt(r)k)+1}`.

For nonsquare `r>=5`, branch separation plus no hits gives exact `|S_t|=2^t`.

Exact hits in general satisfy

`z_m^2-r z_k^2=(1-r)c^2`

with the polygonal congruence class modulo `2a`. Square `r` with `s!=4` reduces by factorization to finitely many positive hits; nonsquare compatible hits fall on generalized Pell orbits.

## 2026-08-12T13:49+08:00 — long-run jump alphabet

For `s!=4`, `r>1`, `phi'` decreases to `sqrt(r)`. With `q=floor(sqrt(r))`, the integer lower-map jump is eventually in `{q,q+1}`. For `s=4`, the same two-letter statement holds from the start (one letter if `r` is square).

Added integer-only `eventual_two_jump_start(s,r)` from a squared derivative inequality. A full Sturmian/generalized-Beatty identification for general `s!=4` was deliberately **not** promoted beyond the proven two-letter alphabet.

## 2026-08-12T13:52+08:00 — external prior-art rooting

Only after the independent arithmetic structure was present, searched public prior art.

1. Chahal–Griffin–Priddis, *When are Multiples of Polygonal Numbers again Polygonal Numbers?* (`arXiv:1806.07981`) materially overlaps the exact-hit subproblem. Direction change: the generalized-Pell fixed-multiple surface was downgraded from possible task-new mathematics to **ROOTED COMPONENT**. The support-dynamical threshold, recoalescence and carrier results remain R035-specific residue.
2. Rozikov–Sattarov–Usmonov (`arXiv:1503.07129`) is related deterministic floor-map prior art, not a solution to the nonlinear polygonal endpoint-support dynamics.
3. Allouche–Dekking (`arXiv:1809.03424`) roots Beatty/generalized-Beatty representation language; no general Sturmian theorem was imported into R035.

## 2026-08-12T13:55+08:00 — completion boundary reached

Final focused tests: 25 PASS. Independent holdout: 321,118 counted checks PASS. Evidence boundaries, killed/narrowed claims, prior-art rooting, exact theorem statements, open questions and machine summary completed.

Taskbook stopping conditions are satisfied. No extra data was added merely to make the result look prettier.

Final classification:

`POLYGONAL_ENDPOINT_DYNAMICS_STRUCTURE_FOUND / SHARP_FACTOR_BOUNDARIES_AND_EXACT_CARRIERS_FROZEN / PELL_COMPONENT_PRIOR_ART_ROOTED / NOT_CANONICAL`

`hard_block = NONE`

`CI_NOT_REQUIRED_FOR_RESEARCH`
