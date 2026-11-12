# R89 — Finite-box cover for phase-exclusion certificates across source versions

Date: 2026-11-12. Evidence: author-side exact proof plus executable finite Fraction verification. Predecessors: R84 (f141f6157e7539c6806f1af8ccbd164cce94b3ab), R87 (6c7908dd76cb4114e2c37c2f7f8d36b75e111305), R88 (a74395dcf54b4f437cfab0b7b2105ca3a1c259ad). Frozen scientific reference: 43ec6098b1330ae86d0a7863be336c5d97f6ef34. The model is the auxiliary rational circular-source model, with original P000/native X6 assumptions unmodified.

## Definition and complete-observer semantics

Fix x rational, observer j integer, original arc-label coefficients a,b integers, and a finite set E of (time,branch) integer identities. On a rational closed interval I=[L,U], put s_t(θ)={x+(t-j)θ}, A(θ)={aθ}, B(θ)={bθ}, with {y}=y−floor(y). Membership M_t(θ) holds exactly when s_t lies in the directed half-open circular arc starting at A and ending at B. If A=B the arc is empty. Winner W_E(θ) is the lexicographically largest qualifying identity or NONE. The membership oracle may quotient branches by time; the winner, deletion and historical version storage must retain all original branch identities.

R84 reuses one excluded group envelope when the new time range and query interval are each contained in that certificate. R89 considers a *finite union of separately proved phase-exclusion rectangles*, including covers in which no one rectangle contains the whole changed-group query.

## R89.1 — Exact anchored exclusion box, even away from the anchor

Choose a reduced rational anchor θ₀=p/q, q>0, a residue r mod q, an integer time range H=[lo,hi], and any rational closed interval J=[l,u]. For every integer time t≡r mod q,

s_t(θ) = { β+(t-j)(θ−θ₀) },   β={x+(r-j)θ₀}.

Proof: the two quantities inside fractional parts differ by the integer (t-r)θ₀, since t-r is divisible by q. This identity is global in θ; in particular θ₀ need not belong to J.

Suppose floor(aθ) and floor(bθ) are constant on J, respectively k_a,k_b, and aθ−k_a < bθ−k_b at both endpoints. The last inequality, being affine, then holds on all of J, so the original directed target is the nonwrapping interval [aθ−k_a,bθ−k_b) throughout J.

Define a closed source-lift enclosure S by adding β to the minimum and maximum of (t-j)(θ−θ₀) at the four corners (t,θ)∈{lo,hi}×{l,u}. This is valid for the entire real-time rectangle because a bilinear function reaches its extrema at corners. Define closed target enclosure Q=[min(a l−k_a,a u−k_a),max(b l−k_b,b u−k_b)]. If S is disjoint from Q+Z, then for every θ∈J and every present t≡r mod q in H, M_t(θ) is FALSE.

The finite integer-shift test is precisely:

ceil(min S − max Q) > floor(max S − min Q).

A successful test constructs a sound OUT certificate. Use of closed enclosures rejects some valid exclusions but cannot produce an invalid exclusion. The exact constructor must separately verify the label-floor and original ordering hypotheses.

## R89.2 — Multiple certified boxes imply whole-group exclusion

Let C_k=(J_k,H_k) be finitely many valid OUT boxes with identical observer, original labels, anchor and residue. A current group T of source times all congruent to r mod q has bounds lo=min T and hi=max T. If the rectangle I×[lo,hi] is contained in the union of the certified rectangles ⋃_k(J_k×H_k), then for every t∈T and every real θ∈I, M_t(θ) is FALSE.

Proof: fix an arbitrary present t and θ. By rectangle coverage there is a valid box containing both coordinates. R89.1 supplies the exact OUT result. Universal quantification gives the group assertion. This reasoning remains valid for any historical version whose group has a covered time range, with the identity and branch registry unchanged in meaning.

**Finite rational cover algorithm.** Clip each J_k to I; form all distinct clipped rational endpoints plus L,U. At every endpoint and one rational midpoint of each adjacent open gap, collect boxes active at that parameter. Sort their closed time intervals and merge overlapping or touching intervals; require that their union contains [lo,hi]. Between consecutive breakpoints the set of active boxes is constant. Therefore endpoint and midpoint checks are *equivalent* to exact rectangle coverage, including boundary points. For K boxes there are at most 4K+3 parameter atoms, with a straightforward loose O(K² log K) comparison bound. This conservatively covers a continuous time interval, even though only discrete congruent times are present.

## Strict worked example: the single envelope fails, a union passes

Choose θ₀=1/16, q=16, r=2, j=x=0, a=4, b=8, H=[-14,18], and I=[113/2000,137/2000]=[θ₀−3/500,θ₀+3/500]. Times -14, 2 and 18 are in the residue class, and β=1/8.

The full-box source-lift enclosure is S=[17/1000,233/1000]; its target enclosure is Q=[226/1000,548/1000]. Since they overlap on [226/1000,233/1000], the single R84-style full envelope does NOT certify exclusion.

Split I at θ₀. For J_left=[113/2000,1/16], the source enclosure is [17/1000,209/1000] and target enclosure [226/1000,500/1000]. For J_right=[1/16,137/2000], the source enclosure is [41/1000,233/1000] and target enclosure [250/1000,548/1000]. Each pair is disjoint, hence both are exact OUT certificates on the full H. Together they cover I×H. Alternatively subdivide H into [-14,2] and [2,18] to obtain four individually smaller valid boxes jointly covering both axes; none alone contains I×H.

Thus multi-box evidence proves exact all-real group exclusion even where the single coarse envelope test is inconclusive. The coarse test's rejection is not evidence of actual member qualification.

## R89.3 — Composition with the R87/R88 champion and provenance

At L compute exact identity-valued w₀=W_E(L). Group candidate distinct times above w₀ (or all times if w₀ is NONE) by anchor residue. A group satisfying R89.2 has P_t=FALSE for every contained time t, so all its positive-polarity calls may be skipped. Other candidate times use R77/R87's full integer-crossing polarity oracle. For an existing w₀, check the original negative polarity N_t₀. R87's maximality proof then gives exact STABLE_NONE, STABLE(identity), or CHANGES with two rational parameters and distinct directly verified winners.

These boxes can be reused across branch edits, retained historical time-fiber versions, time-envelope shrinking, covered query restrictions and union of compatible certificates. A new time outside the covered envelope, interval expansion, changed observer, changed phase labels, changed anchor or arc convention requires a fresh matching coverage check. The full identity fiber remains necessary for recovering the winner and arbitrary future branch operations.

## Executed exact verification

The self-contained standard-library Fraction program in check_r89.py creates each box by the mathematical test, performs the exact finite rectangle cover sweep, composes the result with the R87 champion, and compares it against an independent global R77 six-family critical-cut partition and direct full-identity winner scan, including all real interval gaps and boundary points. Random seed 8920261112. Reported counters are in verification.json.

Across 181 immutable historical identity snapshots, 360 varied interval/history queries plus 140 arbitrary signed-observer/label queries all matched the global full-interval reference (500 classifications). In the 360 matched mixed comparisons, the box-certificate path made 385 polarity-oracle calls versus 414 for its unaccelerated comparator (1,155 versus 1,242 source-oracle atoms). It generated 180 exact CHANGES cases and verified both returned witnesses by direct evaluation.

In a separate controlled family, 181 historical versions preserve time 5 as a qualified champion and time 18 as OUT while branch identities at times -14, 5, 18 are toggled without deleting the fixed champion. Across 360 distinct subinterval queries, covered-box reuse made 360 polarity-oracle calls versus 720 without the cover, and 1,080 versus 2,160 source-oracle atoms, with 360 certified group skips. Every query matched the independent whole-real reference.

The comparison baseline intentionally does not reuse per-time polarity answers across different query intervals; this measures oracle-work savings, not an end-to-end speedup. Cover scanning, cache maintenance, AVL path construction, bigint arithmetic and historical memory require matched benchmark measurement. The verification also checks invalid interval extension, invalid time-range enlargement, invalid observer-signature substitution and endpoint coverage. Finite tests support the implementation; the universal assertions above follow from the mathematical proofs.

## Unfinished R90 unit and control state

Integrate the certified box cover into the actual persistent R88 time-fiber AVL node/query path; measure whole-pipeline exact STABLE/CHANGES output costs, integer-bit sizes, retained memory and witness recovery against R86 merged profiles and R83 temporary heaps for shared workloads.

An actual Source-native em_session_start attempt in this run returned SESSION_ISSUANCE_QUOTA. No new Researcher-ID, Activity checkpoint, Task CLAIM, Result or independent Review was issued. This branch preserves a distinct author-side source, not a shared S23 Task authorization. Scientific input pin remains unchanged.