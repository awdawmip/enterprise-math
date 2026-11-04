# PREFIX-480 — Exact weighted X6 BRC observation-fiber transfer and future-safe suffix state

Date: 2026-11-04 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED. Work type: independent author-side Source research; no live native CLAIM, Result or review is asserted.

## Input and declared observer

Continuation: PREFIX-479, `awdawmip/enterprise-math@58a59c803081ca65ef516b24091ef0af1a9bf929`; frozen scientific model/source pin `f42f2906d77f24085c123f3ccfe9667d41caa96d`. P000 native six-axis basis and joint-observer preservation remain unchanged. This paper uses only the exact *restricted positive-weight BRC ordered-path model* already declared in PREFIX-479, not a native physics or signed-amplitude assertion.

Normal steps: the ten signed directions `aAbBcCdDeE` on native axes E2..E6; special direction `x=+E1` can be used at position 1 or immediately after a fixed ordinary gate word `w` of length k>=1. An ordinary step is always legal. KMP state q=0..k is the longest ordinary suffix since the latest x which is a prefix of w; after x it resets to 0. Time in this paper is the discrete ordered path-step index, not a physical heartbeat duration.

For each path let s be the x count. For native axis i in {a,b,c,d,e}, let (u_i,v_i) be positive/negative directional counts, y_i=u_i-v_i and p_i=min(u_i,v_i). Declare the base BRC observation

    O=(s,y_a,y_b,y_c,y_d,y_e,V,W)
    V=p_b+2*p_d+p_e,  W=p_c+p_e.

This is the exact observer used by PREFIX-478/PREFIX-479 finite X6 checks. Path identities, count multiplicity, total positive mass, per-path weight histograms, and history q are kept as separate typed data. Native positive step weights: (6,1,12,1,18,1,24,1,36,1), x weight 1.

## Theorem 1: BRC right-action closure for every signed native step

For each ordinary axis i, set c_i=coefficient of p_i in V (0,1,0,2,1) and d_i=coefficient of p_i in W (0,0,1,0,1). For step +i, define

    delta_i=1_{y_i<0};   y_i' = y_i+1,
    V'=V+c_i*delta_i; W'=W+d_i*delta_i.

For step -i, use

    delta_i=1_{y_i>0};   y_i' = y_i-1,
    V'=V+c_i*delta_i; W'=W+d_i*delta_i.

All other y_j and s are unchanged. The x step increments s and leaves the remaining seven O coordinates unchanged. Call these maps T_c.

For **all** native raw Parikh-count vectors a and all 11 declared append directions c,

    O(a+e_c) = T_c(O(a)).                           (RIGHT-ACTION)

In particular, if O(a)=O(b) then for any finite identical continuation c_1...c_h, the resulting base BRC observations stay equal. This holds independently of the unrecorded individual p_i and the chosen gate word.

**Proof.** Increasing u_i by one increases min(u_i,v_i) exactly when u_i<v_i, i.e. y_i<0. Increasing v_i by one increases that minimum exactly when v_i<u_i, i.e. y_i>0. All increments therefore depend only on y_i and the declared linear coefficients. Iterating the one-step identity proves the arbitrary common-continuation statement. The distinguished x contributes only to s. QED.

This is an *observer-specific* continuation certificate, not a claim that raw directional Parikh counts or branch identities can be reconstructed. Example: raw count vectors for aA+dD and bbBB both have n=4 and O=(0,0,0,0,0,0,2,0); the certificate holds under every next direction, though their discarded raw counts and native step weights differ.

## Theorem 2: exact ordered-path multiplicity, histogram and moment transfer on (O,q)

For a fixed gate w, let Δ_w(q,c) be its exact KMP transition on ordinary letter c. For each n and reachable (O,q), define the *full positive path-weight histogram*

    H[n,O,q] = sum_{legal ordered paths P: len(P)=n,O(P)=O,q(P)=q} e_{weight(P)},

where e_r is the basis element of the finite-support semiring N[Q_{>0}^{multiplicative}] and each path contributes once (including distinct paths with identical weight). The initial histogram at (n,O,q)=(0,0,0) is e_1. For every ordinary c with positive rational weight lambda_c, transfer the entire bin to (T_c(O),Delta_w(q,c)), multiplying the histogram's weight labels by lambda_c. Transfer x of weight chi to (T_x(O),0) iff n=0 or q=k.

Then for every n>=0 and every fixed gate w, the recurrence returns **exactly** the raw legal-path histogram on every BRC/KMP observation fiber. It requires no full raw-Parikh vector and no full ordered-path enumeration.

**Proof.** Every legal path has a unique last letter and legal predecessor, including the exceptional initial x rule. By Theorem 1 its output O depends only on the predecessor O and appended letter. The KMP update and x legality similarly depend on q and n, while multiplying its path weight by the known positive rational lambda_c. Partitioning paths by their unique predecessor gives precisely the histogram recurrence. Induction on n proves all coefficients. QED.

Three exact projections are C=sum_r H[r], M1=sum_r r*H[r], and M2=sum_r r^2*H[r]. Thus the vector (C,M1,M2) also evolves exactly under each step by

    (C,M1,M2) -> (C, lambda_c*M1, lambda_c^2*M2),

with addition on collision. All fixed nonnegative integer moments have the analogous transfer. An exact histogram must be retained if its full weight shape matters; the three-moment projection is licensed only for the three declared outputs.

Complexity for computing fixed (C,M1,M2) through length N is O(11*sum_{n<N} F_n(w)) big-integer additions/multiplications, where F_n(w) is the actual number of reachable BRC/KMP fibers at that layer. This is an arithmetic-operation count; precise bit cost depends on weight magnitudes and n. Histogram mode costs additional work proportional to its occupied weight labels. The result is an exact finite positive BRC transfer engine; it is not a runtime claim about the project's complete native heartbeat.

## Corollary: lift of PREFIX-479 to the full observable

PREFIX-479's commuting multivariate renewal/KMP formula may use one independent commutative monomial per ordinary direction (plus a separate x marker). Coefficients then count ordered paths for every *raw Parikh vector and suffix state*. Summing these coefficients over the finite preimage of O gives the exact (O,q) path multiplicities; replacing each step marker by its native positive weight yields the exact weighted masses. Theorem 2 is a direct observer-state implementation of this pushforward without enumerating the raw Parikh vectors. This repairs the possible information loss from projecting to unqualified total-only renewal coefficients: q and O are retained as explicit fibers.

For a future legal-operation/query interface consisting of arbitrary sequences of native single-step append choices, KMP legality, final O and any of C, M1, M2 or the complete positive-weight histogram, the joint retained state (n,O,q,H) is sufficient. Source identity and non-commuting path observables require their own typed carrier when requested.

## Exact anagram witness at n=4 and large-N check

The words aab and aba have k=3 and the same ordinary weight product, so PREFIX-479 proves equality of *global* total ordered-path counts, positive masses, all positive moments, and special-step counts, for every n. Their resolved BRC/KMP fibers differ.

At n=4, in the fiber O=(0,0,0,0,0,0,0,0), q=1:

    gate aab: C=2, M1=72, M2=2592; paths aAAa, AaAa (weight 36 each).
    gate aba: C=3, M1=108, M2=3888; same two paths plus AAaa (weight 36).

This is an exact finite witness of history-sensitive path mass, despite equal global total masses and matching base BRC support. In particular, removing q does not preserve the declared gate-conditioned future operations.

At n=8:

    word  B_n    F_n    C_total      M1_total           M2_total
    aab   33295  58496  110054001    10936007142504414  1033374017182766350949291334
    aba   33295  58498  110054001    10936007142504414  1033374017182766350949291334

The different F_n distinguish the tagged support; equal global C/M1/M2 are exactly consistent with PREFIX-479.

## Executed checks and scope

The published JavaScript BigInt certificate is `research_notes/portable_direct/prefix480_brc_fiber_certificate.js`; its actual output is `research_notes/portable_direct/PREFIX480_EXACT_JS_EXECUTION.log`, ending ALL_CHECKS_PASS. It performs exact compressed (O,q) positive-weight moment DP for aab and aba at every n=0..8, including the witness and all global totals.

An **independently written/executed Python standard-library** local cross-check separately evolves every eleven-direction raw Parikh vector together with q, projects it to O, and compares the *entire* per-fiber (C,M1,M2) dictionaries against direct BRC transfer at all n=0..8. It independently enumerates all legal ordered paths at n=0..4 and checks all positive-weight histograms at n=0..5 (including all keys and their moments). For the two explicit raw-count collision vectors it checks all 11 single-step right-actions. Its log ends ALL_CHECKS_PASS. Local file paths in this execution: `/mnt/data/prefix480_brc_fiber_certificate.py` and `/mnt/data/PREFIX480_EXACT_EXECUTION.log`; these are supplementary independent evidence and are not represented as a GitHub published file.

The universal theorems follow from the displayed one-step identities and exact path partition; finite checks target implementation mistakes. All computations use arbitrary-precision integer counts and positive integer weights. Signed amplitude cancellation, arbitrary provenance queries and native physical-time attribution are separate observer classes.

## Next unresolved question (PREFIX-481)

Can the **exact** full histogram H[n,O,q] be compressed for a declared positive-weight future interface by a finite collection of moments, a rational generating family, or a smaller coalescence-aware weight-label dictionary? Compare the actual histograms and their moment jets for witness fibers from aab/aba at n>=4, find a minimal finite fiber pair sharing their first r moments but differing at moment r+1, and test whether proposed projection is stable under arbitrary future gate operations. Retain q, signed native axes, source identity where required, and the fixed frozen scientific pin.

## Authority/read-write status

Project source authorization observed during this run: GitHub authenticated login awdawmip with admin permission; latest applicable global bootstrap/manual read from canonical main, project portable/continuation/method rules, P000/ACTIVE and frozen pin. The native Sites identity is static read-only (research_authority_granted=false); bounded control task query returned CONTROL_QUOTA, so active owner is unconfirmed and no new CLAIM, Result, Review or Admission is claimed. This is author-side scientific evidence publication only.
