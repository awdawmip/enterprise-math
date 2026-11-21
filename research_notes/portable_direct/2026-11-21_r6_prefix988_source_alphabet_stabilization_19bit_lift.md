# PREFIX-988 — Source-alphabet stabilization and exact 19-bit lift for periodic signed-source observers

Date: 2026-11-21 (Asia/Shanghai)
Status: AUTHOR_ANALYTIC_PROOF / EXACT_INTEGER_CHECKED / NOT_REVIEWED
Predecessor: PREFIX-987, minimal deterministic future named-source language carrier.
Scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json (frozen P000 V5).
Role: independent portable continuation of the auxiliary signed-source bit-flip observer; not an authenticated CLAIM or an assertion about native Heartbeat X6 evolution.

## Exact setting

Let p>=2 and let w=(c_0,...,c_{L-1}) be a nonempty finite periodic word of **nonzero integers**. Its named sources at phase q are a=(q,i,j,s), with 0<=i<p, 1<=j<p, s in {-1,+1}, satisfying

    c_q = 2^i - s 2^j.

A source a is legal at an odd p-bit state x exactly when bit_j(x)=(1-s)/2; applying it flips bit j, leaves all other bits unchanged, and advances phase q to q+1 mod L. Labels contain q,i,j,s, so source identity is not discarded. Nonnegative letter weights u_a depend only on this named source, not on spectator bits or unrecorded history.

Let M=max_q |c_q|, k=floor(log2 M), and p_0=k+2. Let A_p(w) denote the full named-source alphabet, U_p(w) its union of nonzero flip ports, and G_p(w) the compact phase/active-bit automaton. Let F_{p,n} be the total weight of all legal n-step named-source paths from **all** 2^(p-1) odd p-bit initial states, with each original start counted once.

## Theorem 988.1 (uniform source stabilization)

For every p>=p_0, A_p(w), U_p(w), and the phase/active-bit transition graph G_p(w) are independent of p. Consequently the minimal deterministic right-language quotient for the named alphabet, as defined in PREFIX-987, is also independent of p. Writing U=U_{p_0}(w), m=|U|, and a_n for the total n-step weight summed over all 2^m active-bit initial configurations at phase 0, one has the **exact** formula

    F_{p,n} = 2^(p-1-m) a_n     for all p>=p_0, n>=0.

This holds simultaneously for every nonnegative, source-factorized choice of letter weights. The spectator factor is a multiplicity of starting states, not a source-path weight or a new native dimension. The formula applies to raw named paths and to the PREFIX-987 deterministic future-language quotient with initial class masses aggregated.

**Proof.** For any nonzero c=2^i-s2^j, if i!=j then

    |c| = |2^i - s2^j| >= 2^(max(i,j)-1).

Indeed, among two unequal powers of two the least nonzero difference occurs for adjacent exponents; a sum is larger. If i=j, nonzero c requires s=-1 and |c|=2^(i+1), so the same lower bound holds. Thus every source satisfies

    2^(max(i,j)-1) <= |c| <= M,
    max(i,j) <= 1+floor(log2 M) = p_0-1.

Increasing p beyond p_0 therefore adds no source labels. The same source ports and legality rules give exactly the same compact phase/active-bit graph. A legal step alters only a port in U; every bit outside U and the fixed odd bit 0 remains unchanged. For each active-bit start there are exactly 2^(p-1-m) independent spectator assignments. Each assignment admits the identical collection of named words with identical source-factorized products. Summing these contributions establishes the formula for every n. The right-language equivalence on the identical compact automaton is identical, which proves quotient stabilization. QED.

## Corollary 988.2 (a sharp uniform threshold)

The bound p_0=floor(log2 M)+2 cannot be uniformly lowered as a function of M alone. For M=2^k, k>=1, the residual c=2^k admits the source (i=k+1,j=k,s=+1), available at width p=k+2 but absent at p=k+1. For M=1, c=-1 similarly admits (i=0,j=1,s=+1) only when p>=2. This demonstrates sharpness for every M that is a power of two, not that every individual word reaches its bound.

## Exact 19-bit results

The same active state graphs previously examined at small width give the following results when the initial distribution is **all** 2^18 odd 19-bit integers; phase is fixed at 0. N_n counts named paths with every letter weight 1. M_n uses u_a=2 for s=+1 and u_a=3 for s=-1.

| Four-stage w | p0 | Active flip ports | Compact states | Minimal named-language classes | Spectator factor at p=19 | N8 | N18 | N19 | M8 |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| (6,24,6,-3) | 6 | {1,2,3,4} | 64 | 57 | 16,384 | 1,572,864 | 22,020,096 | 33,030,144 | 2,165,833,728 |
| (6,24,8,40) | 7 | {1,2,3,4,5} | 128 | 108 | 8,192 | 688,128 | 98,304 | 0 | 1,496,973,312 |
| (4,-1,3,-7) | 4 | {1,2,3} | 32 | 17 | 32,768 | 0 | 0 | 0 | 0 |

For the first word, M19=1,039,110,965,821,440. For the other two words, M19=0. Counts include multiplicities from the original odd starts, not only one representative per active configuration. These data extend PREFIX-987 without redoing or changing its small-width theorem.

## Exact replication and limits

The bundled Python 3 standard-library checker enumerates every source (i,j,s), builds the compact deterministic named-source graph, computes its right-language quotient, and computes path counts by exact-integer backward DP. It compares the entire compact alphabet and transition structure at **every p from p0 through 19**, and independently performs direct forward DP over **all original odd integer states** at p0,p0+1,p0+2 where <=8, for n=0..10 under both weight assignments. It checks sharpness witnesses for k=1..13 and M=1. The universal part is the analytic proof above; the calculations verify stated instances, not arbitrary native BRC operations.

Files:
- research_notes/portable_direct/PREFIX988_R6_STABILIZATION_CHECK.py
- research_notes/portable_direct/PREFIX988_R6_EXACT_RESULTS.json

## Research boundary, value, and next unit

This is an auxiliary source-observer theorem. No claim is made that the bit-flip state is an X6 Cell, that spectator bits encode actual spatial dimensions, or that arbitrary BRC weights factor over named letters. The declared observer and its future named paths are preserved exactly; source letters, sign, port, order and multiplicity are retained. The P000 joint relation constraint remains binding for any future native correspondence.

Next: classify which concrete typed BRC operators have weights constant on the SOURCE-987 quotient fibers. Where they do not, construct the smallest observer-specific memory refinement that preserves the actual weighted futures, and test a typed native Cell/Link/Port lifting on a small pinned instance. The mother question B_fix,odd(32) in {19,20} remains open.

Provenance: PREFIX-987 science source in enterprise-math/research_notes/portable_direct/2026-11-21_r6_prefix987_weighted_named_source_carrier.md. Historical contributor EM-DIRECT-FBEA5D and activity RA-3FB2D033BE6048D8712FF056 are preserved as prior provenance; current formal Task execution authority was not obtained.