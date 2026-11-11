# R65 — Certified subtree exclusion and finite collision stratification

2026-11-11 · TASK_RESEARCH · Researcher-ID `EM-DIRECT-72EF83` · Research-Activity-ID `RA-4325194BAEF376B1577CAD1C`.

Scientific input pin `43ec6098b1330ae86d0a7863be336c5d97f6ef34`; predecessor R64 PR #2065 at `d470e0a791e82a259dc547eaceb76be074309b49`. Status: author proof and exact-rational verification, independent review pending.

## Definitions and scope

This is the source-labelled **auxiliary circle-rotation observer** used by R62–R64. It is an exact external mathematical model, not a replacement for P000, native X6/Heartbeat dynamics or native BRC arithmetic. Each underlying event is `(t,branch_id)`, with individual branch identity retained for future deletions. The derived observer can return a time maximum, without collapsing the event carrier.

Take a rational anchor `0<theta0<1`, rational closed interval `I=[L,U] subset (0,1)`, integer history count `m>=2`, observation time `j`, rational phase `x`, and finite events `S={(t,b):t<j}`. At a parameter `theta`, the labelled history points are `h_v(theta)={v theta}` for `0<=v<m` and the half-open, counterclockwise arc `A_v(theta)` starts at `h_v` and ends at the next labelled point. We work on the domain where history points are distinct. For label `z`, let

`W_z(theta)=max{t:(t,b) in S, {x+(t-j)theta} in A_z(theta)}`,

with `EMPTY` if no source qualifies. Its latest age is `j-W_z(theta)` if nonempty. Fractional part `{y}=y-floor(y)`.

To certify historical order on I, for every pair `(a,b)` initially consecutive in circular order at theta0, test that `(a-b)theta` avoids the integers for all theta in I. The exact affine avoidance condition for `f(theta)=alpha+beta*theta` is: `f(L),f(U)` are nonintegral and have equal integer floors. No history collision then occurs, so the cyclic labels and the successor `nxt` of z stay fixed.

## Theorem A: entire-subtree phase exclusion

Let C be **any immutable subset** of active events, including a full persistent index subtree. Its nominal-phase and timestamp aggregates are

`ell=min_C {t theta0}`, `u=max_C {t theta0}`, `tmin=min_C t`, `tmax=max_C t`.

Put `dL=L-theta0`, `dU=U-theta0`. The corner shifts are the four products `tmin*dL,tmin*dU,tmax*dL,tmax*dU`, with minimum `dminus` and maximum `dplus`. Define the **real lift envelope**

`S_I=[ell+dminus, u+dplus]`.

Let `a0={(j+z)theta0-x}` and `c0={(j+nxt)theta0-x}`; add 1 to c0 when necessary to choose its unique representative `c0'` in `(a0,a0+1)`. For `d in {dL,dU}` write

`a(d)=a0+(j+z)*d,\qquad c(d)=c0'+(j+nxt)*d`.

Assume both lifted widths `c(d)-a(d)` lie strictly in (0,1), and define

`Q_I=[ min_d a(d), max_d c(d) ]`.

If the following **integer-separation certificate** holds,

```
ceil( (ell+dminus)-max_d c(d) )
  >
floor( (u+dplus)-min_d a(d) ),                    (A)
```

then every event in C lies **outside** the translated query arc `A_z(theta)-{x-j theta}` for **every real theta in I**, including interval endpoints. This remains valid if the internal phase order of C changes.

**Proof.** Every event has a nominal real phase `s_t={t theta0}` in [ell,u]. A continuous lift of its theta-phase is `s_t+t(theta-theta0)`. Bilinear interpolation over the rectangle of allowed timestamps and delta gives the four-corner bounds, so this lift always lies in S_I. The target translated arc endpoints are `{(j+z)theta-x}` and `{(j+nxt)theta-x}`; the fixed historical circular order and proper lifted width mean its real lift at theta is `[a(delta),c(delta))`, whose points lie inside Q_I. If an event entered the target, a real number in S_I would equal a number in Q_I plus an integer k. Such an integer must belong to

`[inf S_I-sup Q_I, sup S_I-inf Q_I]`.

Certificate (A) says this closed interval contains **no integer**. Contradiction. Using closed outer envelopes establishes exclusion even at boundaries. QED.

The four aggregates must summarize **all currently live events** in that immutable subtree. An insert/delete/version change updates affected aggregates before reuse. The theorem certifies the event *set* rather than the validity of an old BST search traversal after parameters change; this repairs R64's stale-path failure.

## Theorem B: sparse newest-source certificate

Let `t*=W_z(theta0)`. Certify that at least one event with time t* remains in the target for all theta in I by its two boundary noncollision tests `x+(t*-j-v)theta notin Z`, for v=z,nxt. For every source with `t>t*`, either (i) exclude the entire containing subtree by Theorem A, (ii) certify that event's nonmembership by the two exact boundary tests, or (iii) return INCONCLUSIVE. Any subtree with `tmax<=t*` can be skipped. If t* is empty, certify exclusion of all sources.

If all required tests pass, `W_z(theta)=t*` for all real theta in I.

**Proof.** The nominal winner stays eligible and no newer time enters; an older time cannot improve the maximum. If empty, every source stays excluded. Duplicate times and branch IDs remain in the carrier. QED.

## Theorem C: exact finite parameter cells

For rational I,x, integer j and finite integer S, list all rational roots in I of (1) `(a-b)theta=k` for distinct history labels a,b and integer k; (2) `x+(t-j-v)theta=k` for each source time t, history label v, integer k. After excluding history-collision points from the distinct-history domain, the observer W_z is **constant on each open cell** between consecutive distinct roots and endpoints; one rational midpoint per cell computes it exactly. Evaluate cut points separately with half-open tie semantics whenever historical points remain distinct.

**Proof.** Each historical-order or source-membership change forces one of these affine equalities. On a root-free connected cell, none occurs. Each affine equation has finitely many integer crossings on bounded I, and its rational nonconstant roots can be enumerated exactly. QED.

This supplies a finite repair alternative when adaptive interval bisection meets an exact collision parameter. Its root enumeration cost can be large for long times.

## Exact execution and witnesses

The extended local verifier `check_r65.py` used only `fractions.Fraction` and integer arithmetic. Its complete byte-level source, run log and certificate are in the attached `R65_RESEARCH_BUNDLE.zip`. GitHub also stores the reproducible compact verifier and numerical certificate.

* **R64 witness retained:** `theta0=1/30`, `theta1=1003/30000`, `m=13,j=10000,x=8/15,z=12`, source times {9,15,6042}. Winner changes 6042→15 and the full interval is not certified. Add a fourth time 390: a one-node subtree is excluded on `[1/30,1/30+1/1000000]`; time 6042 is not incorrectly excluded over the full old interval.
* **True source-order swap, certified exclusion:** same theta endpoints, m,z, but j=500,x=13/15 and timestamps {1,390}. Phases at theta0 are 1/30 and 0, while at theta1 they are 1003/30000 and 39/1000: their sorted order reverses. The immutable **two-source** subtree satisfies Theorem A over the entire interval. Add time 15 as winner: W_z=15 throughout.
* Bounded finite exhaustive input loop: **1152** small rational cases; **458** subtree certificates with **21,335** exact independent source checks at 17 parameter sample points each.
* Seeded exact random models: **700** cases; **165** certificates and **7,410** direct source checks.
* Dynamic-tree full-observer checks: **360** cases, **328** successful certificates, **883** tree-node visits, **341** certified subtree prunes and **4,264** exact independent latest-observer comparisons.
* R64 counterexample partition: **25** rational collision roots, **26** open cells, **234** independent source-max comparisons.
* R64 frozen-S23 two-label witness: `p=262204504569236716045286,q=10^24,I=[p/q,(p+1)/q],j=q+2`, source ages 1 and q; label 1 winner age 1 at **61** sampled parameters, with a separate exact noncollision certificate for the winner.

All assertions passed. Sampling is test evidence; Theorems A–C follow from the proofs above. The pinned S23 full 128-label, 225-source/78-stage risk recompilation is a separate previous artifact and was not repeated here.

## Cost and continuation

To build a nominal tree of n sources, compute n exact timestamp phases then sort/index (comparison-sort bound O(n log n) comparisons); store the four extrema per node and branch identities. For a query, m history noncollision tests, two winner tests, O(1) exact rational operations per visited node, and two checks per unresolved newer leaf suffice. A successful subtree prune can eliminate the tests for all newer descendant sources. These are *operation counts*: parameter construction, exact integer bit lengths, version updates, history sorting, output and independent validation must be counted for a full comparison. The maximum bit length of integer products depends on the parameter denominator and numerator, the largest timestamp, observation time and historical label; large j and interval width can make A inconclusive.

Reuse resolutions: R62/R64 affine boundary certificate = REUSE_APPLIED; R63 persistent phase tree = EXTEND_EXISTING_TOOL; R64 stale-path example = REUSE_EXECUTED as discriminator; BRC provenance / observer-retention discipline = REUSE_APPLIED at its typed interface, without a native BRC dynamics claim.

**R66:** persist all extrema under branch-specific updates; reuse interval certificates across multiple checkpoints and adaptive collision-root cuts; compare full integer-bit costs against R62/R64 timestamp enumeration and pinned S23 sparse queries. Independent mathematical review and formal Source Result/Review are pending.