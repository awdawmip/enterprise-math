# Farey-epoch rank/select thresholds: complete finite-horizon risk block generator

Date: 2026-11-09. Researcher-ID: EM-DIRECT-FD1019; Activity: RA-DD03CA86D224EBB832D7AB70.
Research mode: author-side TASK_RESEARCH, independent review pending.
Frozen scientific source: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Immediate predecessor: research_notes/brc_s23_av_farey_gap_risk_20261109_research1_r13/PROOF.md at commit 3a400274da36724d74e7e10818fc77a2013103a3.
Source policy: current main@7c03e2a71d3594575febed0aa45153da8e88941b at initial read; P000 locked; the present result concerns the external auxiliary irrational-circle observer, not an X6 physical dynamics claim.

## Question

With an initial history of m distinct cuts t_i={i theta} (0<=i<m), and n>=m available cuts, calculate all maximal constant intervals of the risk

    R_theta(m,n-m) = 1 - sum_{historical arcs I} M(I;n),

where M(I;n) denotes the greatest length of an n-cut subarc inside the historical arc I. Theta is irrational with 0<theta<1. This risk is the uniform-initial-phase Bayes error of predicting the whole future symbolic block in the previously defined 79-bin auxiliary observer.

The earlier Farey three-gap direct evaluator computes a single n. This note generates candidate change points for all n in an interval without visiting each n.

## Theorem: three event thresholds per historical arc and Farey epoch

Let a/b<theta<c/d be consecutive Farey fractions of order n-1, with bc-ad=1, and define

    U=b*theta-a,  V=c-d*theta,  W=U+V.

The three circular successor-gap types for cuts 0,...,n-1 have respective starting-index ranges

    U: [0,n-b),    V: [d,n),    W: [n-b,d).

During a Farey epoch these four integers a,b,c,d and the positive gap lengths U,V,W are fixed, while n varies over a consecutive interval contained in

    max(b,d)+1 <= n <= b+d.

For a historical arc I, let S_I = {i>=0 : {i theta} belongs to I}. Write

    u_I=min S_I,
    v_I(d)=min(S_I intersect [d,infinity)),
    w_I(d)=max(S_I intersect [0,d)), when this set is nonempty.

The first two minima exist because each historical arc has positive length and irrational rotation is dense; u_I is at most m-1, since the arc includes its initial left endpoint.

Within this epoch the three gap-type presence predicates are EXACTLY

    U present iff n >= b+u_I+1;
    V present iff n >= v_I(d)+1;
    W present iff w_I(d) exists and n < b+w_I(d)+1.

Proof: U-start indices are 0<=i<n-b, whose intersection with S_I is nonempty precisely when the least member u_I is smaller than n-b. V-start indices satisfy d<=i<n, so the least such member is v_I(d). W-start indices satisfy n-b<=i<d, so a member exists precisely when the greatest member below d is at least n-b. This gives the three displayed thresholds. All gap lengths are fixed within the epoch, and M(I;n) is the greatest available type length. Hence M(I;n), and thus R, can change only at one of the three thresholds. QED.

**Consequences.** Each epoch has at most 3m candidate internal change points, in addition to its initial boundary. At any resulting open integer block, R is a single affine expression A+B*theta, because every selected maximum belongs to {U,V,W}. Unchanged adjacent affine blocks are merged. This is a theorem for every irrational theta and every m>=2; no S23 specificity is needed for the theorem.

## Rank/select algorithm and accounting

For a fixed epoch, determine u_I from the first m historical indices. Determine v_I(d) and w_I(d) via rank/select on the ordered set S_I, requiring at most two binary searches per historical arc if a direct select primitive is unavailable. The prior exact arc-count formula calculates the number of S_I indices in any integer range [A,B] from two Euclidean floor sums. Each rank request is logarithmic in the rational enclosure denominator; binary search uses O(log n) such requests. With E Farey epochs through n<=N, this gives an arithmetic-operation construction in O(m log m + E*m*log N*log Q + E*m^2*log Q), with Q a certified rational enclosure denominator; output size itself may be O(E*m). A sharper bound is possible with incremental maximum maintenance. All bit-complexity, input conversion, precision certification and output listing are extra costs. E is dependent on theta's partial quotients and is NOT automatically O(log N) uniformly in theta.

The included executable finite verifier chooses a different, scan-based rank/select realization: exact residue classification for every index 0<=i<N at BOTH certified rational endpoints, followed by bisect operations on per-arc sorted index vectors. It costs O(N log m) preprocessing comparisons plus at most O(E*m^2*log N) simple operations for candidate risk recomputation, and O(N) index storage. It is a complete finite certificate for the stated N, not a benchmark of the non-enumerating implementation.

Information carrier: the labelled phase-cut family, type-specific start-index ranges, historical arc labels and affine gap maxima. The single aggregate number of n-cuts is not a sufficient future-risk state; this reuses the predecessor's Farey/BRC-labelled observer without conflating it with native X6.

## Frozen S23/AV exact certificate through two million future steps

Here theta = 79*(2074774-380295*r)/(79*r-431)-46, r=ln(7)/ln(10/7). A separate 160-term rational logarithm-series enclosure in the included code proves

    262204504569236716045286 / 10^24
       < theta <
    262204504569236716045287 / 10^24.

**Why the finite endpoint check certifies the entire real interval.** For every phase index i<N and every historical cut index p<m, the function (i-p)*theta crosses an integer at most once between LO and HI, because abs(i-p)*(HI-LO)<2000128/10^24<1. An arc assignment can change only at such a crossing. Agreement of the two endpoint assignments therefore certifies each i's historical-arc membership throughout the interval. The same bound fixes each phase relation to the zero cut. The Farey mediant signs and all affine gap-max comparisons are separately fixed at both rational endpoints, so their chosen cells and winners are likewise stable. This covers the exact irrational theta, not merely the rational midpoint.

Take m=128 and N=2,000,128 (L=2,000,000). An exact two-endpoint enumeration of the N phase memberships gives:

    Farey epochs: 29
    distinct candidate thresholds: 6577
    maximal constant risk blocks: 3426
    R(128,2000000) = -21156991 + 80688896*theta
                    approximately 0.9999186661803596.

At n=1,000,128 (L=1,000,000), the old exact certificate is recovered:

    R(128,1000000) = -5169279 + 19714688*theta.

The exact maximal constant interval containing n=1,000,128 runs from n=630,382 THROUGH n=1,106,579. The first strict increase after the million-step horizon occurs at

    n=1,106,580, equivalently L=1,106,452.

Its exact increment is

    Delta R = 165289 - 630382*theta > 0.

At that point the risk is -5003990+19084306*theta. The finite enumeration also reproduces the earlier n=200128 and n=322177 certificates, and its full version independently cross-checks 11 selected n values against the predecessor's Euclidean floor-sum Farey-gap evaluator. The run evidence and fully reproducible standalone code accompany this note.

Verifier command from this directory:

    python VERIFY_PUBLICATION.py

This prints PASS_S23_AV_FAREY_EVENT_GENERATOR_2M and generates BLOCKS_2M.tsv (3427 lines including header). Its complete locally generated TSV has SHA-256 f9dd46e0e9e70b8871717b9d24a7f3361c4228f8894bef00d50458086cebb548. The version of the compact executable embedded here was run successfully and produced RUN_EVIDENCE.txt. A separate expanded implementation was checked with 11 independent Euclidean floor-sum endpoints.

## Prior art and limitations actually relevant to the claim

The three-gap theorem is classical: e.g., D. Taha, "The Three Gap Theorem, Interval Exchange Transformations, and Zippered Rectangles" (2017), https://arxiv.org/abs/1708.04380; H. Zhang, "The frequency problem of the three gap theorem" (2024), https://arxiv.org/abs/2403.07674. This note claims a checked event-threshold reduction and exact S23/AV finite certificates, not novelty for the three-gap theorem itself. Proof status: author-derived theorem, with finite rational certificate and independently checked endpoints; independent mathematical review and theorem adoption remain pending.

Next exact question: implement non-enumerating floor-sum select for all event positions through L=10^12, compare bit and output costs (including nearly rational slopes), and compute an output-sensitive maximal-block generator. Keep the 413th S23/AV capacity plateau as a distinct geometric research branch.
