# PREFIX-989 — Positive branch-history refinement of the named-source residual carrier

Date: 2026-11-21 (Asia/Shanghai)
Status: AUTHOR_ANALYTIC_PROOF / EXACT_INTEGER_CHECKED / NOT_REVIEWED
Line: independent portable research; immediate predecessor PREFIX-988.
Frozen scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json (P000 V5).
Observed control Source main at start: 697ae262c71abea056fee9584c1df3ecc8489d21.
Historical contributor: EM-DIRECT-FBEA5D; historical Activity RA-3FB2D033BE6048D8712FF056. Neither provenance nor this research note grants a current CLAIM or current-session Activity mutation authority.

## Question

PREFIX-987 proves minimal deterministic right-language compression for the auxiliary four-stage signed-source bit-flip observer when nonnegative weights factor solely through the named source letter. PREFIX-988 proves that its source alphabet stabilizes in the bit width. The next exact question is whether a positive branch weight depending on the *previous source port* can be retained without extra state.

We keep the previous model exactly. A letter a=(q,i,j,s) is enabled at phase q and odd p-bit x if c_q=2^i-s2^j, 0<=i<p, 1<=j<p, s in {+1,-1}, and bit_j(x)=(1-s)/2. It flips bit j and advances q modulo L. Let U be the active nonzero flip ports, m=|U|. Spectator bits never change. The enhanced state is z=(q,b,h), where b records the active bits and h is the *previous* selected port, with h=0 (the start sentinel) before the first step. On named letter a, the successor is (q+1,b xor e_j,j). Choose a strictly positive rational (or integer) local mass g(h,a); its value may depend on the prior port h. Legal word mass is the ordered product of these transition masses. For the empty word its mass is 1.

## Theorem 989.1 — exact finite weighted Nerode quotient

For an arbitrary finite deterministic partial labeled graph with strictly positive rational edge weights, define f_z(alpha) as the mass of the unique path spelling the finite named word alpha from z, or zero if the word is illegal; set f_z(empty)=1. Define z≡z' iff f_z(alpha)=f_z'(alpha) for every finite named word alpha.

Then (i) z≡z' implies equal sets of enabled named letters and *equal immediate weights* for every common enabled letter; (ii) the corresponding a-successors are equivalent; (iii) the quotient is a well-defined deterministic weighted labeled graph and exactly retains each legal named word's mass, its path count and every resulting finite positive-weight histogram for an arbitrary initial distribution; (iv) it has the minimum number of classes among deterministic quotients which preserve, state-by-state, the entire weighted named-word series with the original labels and empty-word normalization.

Proof. For a letter a, f_z(a) is zero if disabled, and is g_z(a)>0 if enabled. Equality of all f values therefore implies simultaneous enablement and equal nonzero edge weights. For any continuation beta, f_z(a beta)=g_z(a) f_delta(z,a)(beta). Division by the common positive weight gives equality of the successors' entire weighted future series. Thus the relation is a right congruence compatible with edge weights. Induction on the word length proves exact path-weight retention; aggregating the start multiplicities yields counts, mass and the histogram N[Q_{>0}]. Any deterministic quotient that merges unequal series loses the value of some named word, proving minimality in the stated category. On a finite graph, stable partition refinement using signatures of (named label, immediate weight, successor class) computes this quotient, because inequivalent states have a finite distinguishing word. QED.

Strict positivity matters: zero-weight enabled paths can be invisible to this mass series. If Boolean named support is also an observer, its support bit must be retained separately. This matches the typed distinction between R023 Boolean support and positive Weighted-BRC.

## Theorem 989.2 — finite memory and width-stability inheritance

Suppose a local mass depends only on the last k named letters, or a finite deterministic history automaton H whose update is driven by the current named letter. The exact positive weighted observer is realized on S×H, using its transition-weighted right-language quotient. In particular, for last-port memory, |H|<=m+1, so the full phase/bit/history carrier has at most L*2^m*(m+1) states before quotienting. For a finite history automaton of size r the corresponding bound is L*2^m*r.

If M=max_q |c_q| and all c_q≠0, PREFIX-988 gives p0=floor(log2 M)+2. For p>=p0 the source alphabet and active ports are unchanged; if the history update and weights depend only on the named letters and their finite history, the augmented graph and its minimal weighted quotient are independent of p as well. For a start distribution uniform over all odd p-bit integers, with h=0 and phase zero, the total n-step mass and each exact histogram multiplicity are multiplied by 2^(p-1-m) relative to the active-bit model. The theorem is about a finite explicitly typed positive branch observer; identifying it with a specific native X6/BRC operator requires an additional type-preserving map.

Proof. The transition on (q,b,h) is deterministic for each label and stays within a finite set. Its weight g(h,a) and next history are available from the augmented state. Apply Theorem 989.1. For p>=p0, PREFIX-988 gives identical labels/ports. Every untouched bit outside U and the fixed odd bit zero is a spectator, with exactly 2^(p-1-m) assignments per active start. This multiplicity changes none of the named path weights. QED.

## Concrete counterexample: the PREFIX-987 quotient is insufficient for a history-sensitive weight

Take p=6, w=(6,24,6,-3), initial odd integer x=1 and phase 0, with h=0. The following two *different legal seven-step named paths* both reach exactly the same phase q=3 and integer x=3, but end with different previous ports. Each entry is (phase,i,j,sign).

Path A:
(0,3,1,+1), (1,5,3,+1), (2,2,1,-1), (3,0,2,+1), (0,1,2,-1), (1,4,3,-1), (2,3,1,+1). Final h=1.

Path B:
(0,3,1,+1), (1,5,3,+1), (2,2,1,-1), (3,0,2,+1), (0,3,1,+1), (1,4,3,-1), (2,1,2,-1). Final h=2.

The same next named source (3,0,2,+1) is legal from both. Set g(h,a)=1 for h=0, 2 for h=1, 3 for h=2, 5 for h=3, 7 for h=4, and 11 for h=5, independent of a for this explicit test. The common next named source has conditional mass 2 after path A but 3 after path B. The two states are indistinguishable in the old (phase, active-bit) carrier and in its unweighted right-language quotient, yet have different weighted futures. Last-port memory is therefore genuinely necessary to represent this specific positive mass rule. No assertion is made that every native BRC weight has this dependence.

## Exact reproducible calculations

The companion standard-library Python checker independently computes (1) backward exact-integer dynamic programming on the reachable augmented graph, (2) exact stable weighted partition refinement and quotient dynamic programming, (3) independent forward exact-integer propagation, and (4) the full length-eight histogram N[Q_{>0}]. It verifies each source alphabet from p0 to 19. All initial active-bit states at phase 0 with h=0 are included. Counts and masses in the table below are before the spectator multiplier.

| Residual word | Stable p0 | Active ports | Reachable augmented states | Minimal weighted classes | N8 | Mass8 | N19 | Mass19 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| (6,24,6,-3) | 6 | 1,2,3,4 | 96 | 89 | 96 | 276480 | 2016 | 1763596800000 |
| (6,24,8,40) | 7 | 1,2,3,4,5 | 188 | 163 | 84 | 1901600 | 0 | 0 |

For all 19-bit odd starts the first row has (N8,Mass8)=(1572864,4529848320) and (N19,Mass19)=(33030144,28894769971200000); the second has (688128,15577907200) at step 8 and zero at step 19. The first row length-eight exact positive histogram for active starts is 1800×16, 2520×16, 2700×32, 3780×32; its total count is 96 and its total mass is 276480. These values can be checked without floating point.

Code: research_notes/portable_direct/PREFIX989_R6_HISTORY_WEIGHTED_NERODE.py.
Result certificate: research_notes/portable_direct/PREFIX989_R6_EXACT_RESULTS.json.
Coverage: equality of backward/quotient recurrences n=0..24; equality with independent forward dynamic programming n=0..16; exact histogram-moment consistency n=8; identical named-source alphabets p=p0..19. This finite testing validates the two explicit families; the universal result follows from the analytic argument above. Mathematical review remains NOT_REVIEWED.

## BRC and native-model boundary; next research frontier

The branch-mass histogram belongs to the foundation's finite positive-rational N[Q_{>0}] carrier. Theorem 989.1 retains the stronger entire weighted named-word observer, and so implies preservation of that histogram. The same source sequence and sign are still labeled; no signed cancellation is inferred from positive masses. The model's binary flip ports are auxiliary observation indices, not X6 spatial axes or Cell identities.

Next determine, for a concrete Source-typed native BRC operator, whether its transition mass is constant on each old PREFIX-987 right-language fiber. If yes, the old quotient suffices for that declared weight; if not, identify the smallest finite history/state refinement preserving its actual permitted operations, phase and joint observation. Only after that test a typed Cell/Link/Port correspondence and BRC composition, keeping the frozen P000 joint-observer preservation rule. The mother question B_fix,odd(32)∈{19,20} remains open.
