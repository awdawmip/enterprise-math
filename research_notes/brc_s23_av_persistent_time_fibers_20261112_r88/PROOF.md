# R88 — Persistent source-time fibers and two-polarity certificate composition

**2026-11-12.** Evidence class: author-side exact theorem, executable finite tests and timing observations. Predecessor R87: `6c7908dd76cb4114e2c37c2f7f8d36b75e111305`; R86: `5b4f6fa4f442358fe721e9c2c0eb3b238f588845`. Frozen scientific reference `43ec6098b1330ae86d0a7863be336c5d97f6ef34` is unchanged. This is the *auxiliary rational circular-source model*, not an asserted native X6/BRC result.

## 1. Exact model, representation and observer

Let `I=[L,U]` be a nonempty rational closed interval. Fix integer observer `j`, rational `x` and integer labels `a,b`. Each source identity is an ordered pair `(t,branch)` of integers. Write `{q}=q-floor(q)`, `s_t(theta)={x+(t-j)theta}`, `A(theta)={a theta}`, `B(theta)={b theta}`. A time qualifies, `M_t(theta)`, when `s_t` lies in the directed half-open circular arc from `A` to `B`, with an empty arc at `A=B`. The observable winner is the lexicographically largest qualifying *identity* or `NONE`.

This observer can forget branch data **only inside the membership predicate**: `M_t` is constant on the fiber of identities at the same time. Identity-valued winner recovery and future delete/update operations still require all branch identities. Neither the whole source set nor the branch fiber is erased in the representation.

## 2. Persistent fiber quotient theorem R88.1

For any finite identity set `S`, put `T(S)={t: exists branch, (t,branch) in S}` and `B_S(t)={branch: (t,branch) in S}`. Define `b_S(t)=max B_S(t)` for nonempty fibers. Then for every real `theta in I`,

`W_S(theta) = max_{t in T(S), M_t(theta)} (t,b_S(t))`, with `max(empty)=NONE`.

**Proof.** Every source in a fixed time fiber has the same membership result. If the fiber qualifies, its unique maximal identity is `(t,b_S(t))`; otherwise the entire fiber is absent. Lexicographic maximization over the union of fibers is therefore equal to maximization over their qualifying representatives. This argument holds pointwise for every real parameter, including every arc endpoint and label coincidence. QED.

A persistent AVL whose key is `t` and whose node stores the **complete immutable set** `B_S(t)` therefore represents the same winner function under every future sequence of insertions, deletions and historical-version reads. An identity toggle changes only the corresponding leaf/fiber and the immutable AVL ancestor/rotation path; old roots retain their original complete fibers. At the ordinary unit-cost tree level the number of newly constructed AVL nodes is `O(log(|T|+1))`, excluding the cost of copying a branch fiber, integer bit costs and memory reclamation. Rebuilding a `frozenset` fiber of size `k` may cost `O(k)`; there is no universal logarithmic end-to-end promise.

## 3. Composing with R87.1 without merged global profiles

For a fixed query signature `sigma=(I,j,x,a,b,arc-convention)` and distinct time `t`, define exact polarities `P_t=exists theta in I: M_t(theta)` and `N_t=exists theta in I: not M_t(theta)`. The R77/R87 six integer-crossing families partition the interval into rational cuts and open gaps where `M_t` is constant. Checking every cut and one rational midpoint per gap yields a complete polarity verdict and a rational witness if the polarity holds.

Calculate the point winner `w0=W_S(L)` by descending through the time AVL and testing `M_t(L)` once per time until the first hit. If `w0=NONE`, the function is identically NONE precisely when every present time has `P_t=false`. If `w0=(t0,b0)`, it is identically `w0` precisely when `N_t0=false` and `P_t=false` for every present `t>t0`. If a condition fails, the corresponding rational witness and a fresh point winner at that witness produce an exact `CHANGES` certificate. This is the R87.1 argument applied to the complete branch-fiber representation from R88.1. No union of all source-time critical points is required on this path.

The per-time polarity cache key includes `sigma,t,polarity` and retains rational witness or an exact negative result. It can be reused across identity updates and historical versions; a version-level `STABLE(identity)` verdict cannot be reused solely because its set of source times is unchanged.

**Exact counterexample to time-only result caching.** At `I={1/4}`, `j=x=0`, `a=1,b=2`, the time-1 source qualifies. With identities `(1,1),(1,7)`, the winner is `(1,7)`. Deleting `(1,7)` leaves time support unchanged but makes the winner `(1,1)`. The old persistent root continues to return `(1,7)`. Thus time support is a sufficient quotient for the **membership-oracle cache**, but not for identity-valued winner output or branch deletion. This explicitly certifies the limited observer scope of the quotient.

## 4. Exact implementation and finite verification

`check_r88.py` implements a path-copy AVL with immutable time-fiber sets, ordered source query, rational exact polarity oracle, signature-keyed cache and an **independent full union-of-critical-cuts reference**. The reference compares every rational cut and interval midpoint with a direct sorted-identity scan. It verifies AVL heights, balance, counts, identity-set reconstruction, historical roots, actual rational change witnesses and identity ties.

A seeded run (`8820261112`, Python standard-library `Fraction`) performs 480 identity toggles and 960 direct independent whole-interval version comparisons, and includes a deliberate same-time branch deletion counterexample. It additionally checks top-stable champion cases with 33,129,513 source identities. The actual `verification.json` records the measured counters and one-run `perf_counter_ns` timings. These are **finite software tests**, not an independent mathematical review or a statistically powered wall-clock benchmark.

## 5. Costs, information accounting and next problem

For `m` distinct times and one fixed signature, the first full uncached query may require `O(m)` polarity calls; the single-time exact oracle can itself enumerate many integer crossings as coefficient magnitude grows. Across multiple version queries using the same signature, the *number of newly computed cached time/polarity pairs* is at most `2 * |union of distinct queried times|`; query traversals, point-winner scans, branch-fiber copy, cache lookups, exact rational bit lengths, persistent node allocations and history retention remain actual costs.

This data structure preserves time, branch multiplicity, the complete identity fiber and old root ancestry. Only the logically certified membership-oracle readout merges branches, with an exact decoding rule for the requested winner. This is the applicable BRC/observer-preservation lesson; it makes no claim of a new native BRC theorem.

**R89 target:** integrate the R71/R84 group-envelope exclusions into the persistent time-fiber index; test cross-version cache invalidation when query signature/interval changes, and measure complete workload costs including updates, cache storage, old-root retention and bit arithmetic against both R86 merged profiles and R83 temporary heaps. Derive a witness-backed crossover surface rather than universal speedup claims.

**Source/control note.** At 2026-11-12 07:00+08:00, source-native `em_session_start` returned `SESSION_ISSUANCE_QUOTA`; a lookup of the guessed key `RS-S23-AV` returned `NO_CURRENT_IMMUTABLE_PUBLICATION`. Thus this is an author-side research artifact, not an authenticated S23 Task CLAIM/Result/Review. A real Source session/activity checkpoint is pending a successful native issuance; no earlier researcher identity is reused.
