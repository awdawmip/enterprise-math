# X6 native-time cut observers III: exact causal phase-fiber theorem and a one-link winding-recovery threshold

Date: 2026-11-19 (Asia/Shanghai). Scope: author-side *conditional finite event model*. Research line: RS-X6-NATIVE-TIME-DYNAMICS, publication TP2-91D4A7C2F63805BE21A3; prior researcher provenance EM-DIRECT-403AAA, activity RA-3CCFD886BD2BFF49E8A49CB9. **This independent GitHub preservation does not assert a renewed live CLAIM or mathematical acceptance.** Frozen scientific input pin awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. P000 retains six native spatial Cell coordinates and time as a separate trace/order coordinate, not a spatial axis.

## Sources and exact question

Extend two saved author-side conditional results:
- [2026-11-12 cut-lattice/C12 winding study](https://github.com/awdawmip/enterprise-math/blob/f115d6abf67f4dd41fe8a4d89367a0b1d1caa55f/research_notes/portable_direct/2026-11-12_x6_time_cut_lattice_and_C12_winding_residual_r2.md) established the independent-chain k-ideal polynomial and C12 (0,12)/(12,0) alias.
- [2026-11-12 single causal crosslink study](https://github.com/awdawmip/enterprise-math/blob/c8a44eeb585f83be41a161f1492caae07f8066f6/research_notes/portable_direct/2026-11-12_x6_time_one_causal_crosslink_cut_polynomial_r2.md) gave the cut polynomial subtraction for one hypothetical A_r < B_s edge with local lengths at most 11.

Let A_1<...<A_a and B_1<...<B_b be two distinguishable event chains (a,b>=1). Optionally add one cross-edge A_r < B_s with 1<=r<=a and 1<=s<=b, and take its transitive closure. Each local deterministic decorated component has exact event-return period p (V1R: p=12). This internal period alone is neither physical elapsed duration nor an admission of a physical cross-Cell event. A kth-cut ideal has completed local counts (i,j), k=i+j.

Observe (k, phi_A, phi_B), where the local fully decorated phases are determined exactly by i mod p and j mod p. The target observer is *exact source-allocation cut reconstruction* within the specified finite event model; the future alphabet comprises append A/B subject to the declared causal guard.

## Theorem 1. Exact causal cut-support interval

For every k=0,...,a+b, put

    U(k) = min(a,k)
    L0(k) = max(0,k-b)
    L(k) = L0(k)                              if no cross-edge;
    L(k) = max(L0(k), min(r,k-s+1))            if A_r < B_s
    W(k) = U(k)-L(k)+1.

The set of legal k-prefix ideals is exactly

    I_k = {(i,k-i): L(k)<=i<=U(k)},     |I_k|=W(k).

**Proof.** A pair of chain prefixes (i,j) must satisfy 0<=i<=a, 0<=j<=b and i+j=k. The cross-edge forbids j>=s unless i>=r, so the legal condition is i>=r OR i>=k-s+1. Its union is the single upper ray i>=min(r,k-s+1). Intersect with the original interval. Every legal ideal extends to some linear extension of the finite event poset, and a two-chain-plus-one-forward-edge poset is acyclic. QED.

This refines the earlier coefficient formula into an exact contiguous diagonal fiber; no serial-word enumeration is needed.

## Theorem 2. Exact phase fibers and minimal additional information

At fixed k and A-phase residue q in {0,...,p-1}, the B-phase is determined by (k-q) mod p. The exact phase-fiber size is

    F(k,q) = floor((U(k)-q)/p) - floor((L(k)-1-q)/p).

The largest possible phase fiber has size

    M(k) = ceil(W(k)/p).

Thus the minimum *worst-case* fixed-length extra bits needed to reconstruct the exact source-allocation cut from k and both complete local phases is

    b(k) = ceil(log_2 M(k)), with b(k)=0 when M(k)=1.

In particular the phase/count observer is injective on the k-cut support **iff** W(k)<=p.

**Proof.** Because each component has exact period p, two local progress counts yield the same complete local phase exactly when congruent mod p. With k fixed, only A-count i varies over the W consecutive integers in [L,U]. Counting their residue-q members gives the floor-difference formula. The maximum occupancy of a residue class among W consecutive integers is ceil(W/p). A code identifying an arbitrary member of its largest class needs at least ceil(log2 M) bits, attained by indexing that class. W>p supplies a congruent pair i,i+p; W<=p supplies none. QED.

**Typed BRC observer correspondence.** Use a finite labelled-branch carrier with ordered event words over {A,B}, full typed counts, and guarded append operators. Boolean BRC support projects each branch family to its set of reached (i,j) ideals. This projection commutes with future append A/B *for this declared support observer* because both enablement and successor support depend only on current (i,j), not on omitted order. It is therefore a valid exact future-safe quotient at this scope. Labelled event words/multiplicity are retained for provenance-sensitive observers; collapsing them has not been proved safe there. The second projection (k,i mod p,j mod p) may merge several supports, and the theorem calculates its exact fibers. No positive BRC mass is substituted for signed amplitude; no numerical native residual, physical period or pi/trigonometric quantity is inferred.

## Theorem 3. A single cross-edge recovers all phase winding for two p-step chains

Suppose a=b=p and 1<=r,s<=p. For any cross-edge A_r < B_s, the observer (k,phi_A,phi_B) is injective on *every* k=0,...,2p: M(k)=1 and b(k)=0. Without the cross-edge, the sole phase collision across all k is at k=p: ideals (0,p) and (p,0) share both initial phases and the total count; it requires one extra bit.

**Proof.** If two distinct count pairs (i,j),(i',j') in [0,p]^2 have equal k and both local phases, then i-i' and j-j' are multiples of p, sum zero, and nonzero. The only possibility, up to order, is the pair (0,p),(p,0), at k=p. But (0,p) violates every A_r<B_s (because B_s is present while A_r is absent), whereas (p,0) remains legal. No collision survives. Without an edge both are legal. QED.

**Sharp horizon boundary/counterexample.** With p=12,a=24,b=12,r=2,s=1 and k=24, both (12,12) and (24,0) satisfy the causal edge. Both have (k,phi_A,phi_B)=(24,0,0), so a single edge does not generally remove winding ambiguity after longer horizons. Here the phase-zero fiber requires precisely one extra bit.

## Reproducible finite validation

Companion exact Python verifier: [x6_causal_cut_phase_fiber_brc_verify.py](x6_causal_cut_phase_fiber_brc_verify.py). It constructs actual labelled branch-word supports and checks that the Boolean-support quotient commutes with all allowed future updates in its finite domain. Larger C12 models use the exact declared support operator whose quotient-safety was proved. Its output is [x6_causal_cut_phase_fiber_brc_results.json](x6_causal_cut_phase_fiber_brc_results.json). Reproduce with:

    python3 x6_causal_cut_phase_fiber_brc_verify.py

Executed locally: PASS. Complete labelled-word checks for all a,b in 1..5; r=1..a,s=1..b; p in {2,3,4,5}: **900 exact cases**, each at every possible k. Complete support-level checks for all 144 edge choices r,s=1..12 with a=b=p=12 at all k=0..24. No-edge C12 maximum phase fiber at k=12 is 2. The longer-horizon counterexample is exactly {(12,12),(24,0)}. For a=b=3,r=s=2 the observed cut-state histogram [1,2,2,2,2,2,1] agrees with the prior crosslink polynomial.

Executed local checker SHA256: f096bac6aa88f43466632792918e3c5a26cd06386f56b67fd93b54016c15b2fb. Output JSON SHA256: 14e50b171a2de90ccdc1c217225c320af7e3c7ca21ea766921c6f9c76d447882. These are bounded tests; the arbitrary-parameter claims are supported by the proofs, not extrapolated from the finite tests.

## Contribution, exact limitations, next question

The phase/source residual at a kth-cut is controlled exactly by causal interval width W(k), rather than event total or local C12 phase alone. The smallest nontrivial two-Cell causal edge can remove the sole collision within one local period, but longer horizons demonstrably retain winding/source memory. This is an observer-typed conditional finite mathematical result, **not** a new native Cell/Link/Port/force permission, an accepted foundation theorem, or a calibrated physical clock.

Next: determine an actual native admissible dependency/permission predicate for two V1R Cell/Link/Port updates, then test whether its support/future language is faithfully represented by one cross-edge or requires extra source-bearing state. For three chains or several edges, analyze phase fibers of noncontiguous cuts, where the present width-only formula can fail. Activity/PROGRESS association, formal Result and current OWNER/CLAIM remain distinct protected Source operations.
