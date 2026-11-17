# PREFIX-862 — Full named BRC transition recovery at information-theoretically near-optimal peak width

Date: 2026-11-17. Scientific status: AUTHOR_PROVED / EXACT_INTEGER_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
Dependencies: PREFIX-861 (shared-GCD CRT observer, its exact checker and result table), PREFIX-850 (projective order). Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Scope: auxiliary named binary BRC source observer; native X6 Cell/Link/Port event admission and future-operation compatibility are separate.

## Stronger recovery theorem

For p named binary sources x in {0,1}^p, an allowed heartbeat transition is a no-op or exactly one bit flip. There are exactly T_p=2^p(p+1) **distinct ordered source-state transitions** (x_before,x_after). Both observations are taken at consecutive heartbeats, and the initial state is completely unknown.

Let g=3^(1+ceil(log_3 p)), choose the least positive odd a such that g a(a+2)>=2^p, and set q1=ga, q2=g(a+2), as in PREFIX-861.

**Theorem 862-A.** The pair of residue readouts (U_before mod q1,U_after mod q2) identifies the *entire ordered transition*, not merely its terminal state. In particular it identifies the initial complete p-bit source vector, final complete p-bit source vector, whether a flip occurred, the named flipped index and its signed direction.

**Proof.** The residue difference modulo g uniquely identifies the signed increment delta in E={0,±2^i:0<=i<p}, by PREFIX-861-B. Generalized CRT with q1,q2 recovers U_after uniquely in [0,2^p), since lcm(q1,q2)=g a(a+2)>=2^p. Set U_before=U_after-delta. Both integers are exact and their p-bit expansions recover both named source vectors. The bit index and sign are encoded by delta (delta=0 is no-op). Distinct legal ordered transitions therefore cannot yield the same observed pair. QED.

## Sharp information lower bound and bounded additive upper bound

Let B_peak(p) be the infimum of the maximum raw port width over all two-round observers required to distinguish **all** T_p transitions, with no uncounted side channel. A second-round modulus can even be chosen deterministically from the first observation: a depth-two decision tree with at most 2^B outcomes at each round has at most 2^(2B) leaves.

**Theorem 862-B.** For every p>=1,
  B_peak(p) >= ceil((p+log_2(p+1))/2).
For p>=5, the specific PREFIX-861 odd-modulus construction satisfies
  B_constructed(p) <= ceil((p+log_2 p)/2)+4
and hence
  0 <= B_constructed(p)-B_peak(p) <= 4.
In particular its peak width is p/2+(1/2)log_2 p+O(1), and this order is optimal up to an additive constant **for full transition recovery**.

**Proof.** Counting the T_p different transitions forces at least T_p distinct two-read transcripts. Thus 2^(2B)>=T_p and the lower bound follows. For the upper bound, put N=2^p. PREFIX-861 proves q2<sqrt(gN)+4g. For p>=5 we have g<=N and g<9p, so q2<5sqrt(gN)<15sqrt(pN); since sqrt(pN)>1, q2+1<16sqrt(pN). Its raw width is therefore
  ceil(log_2(q2+1)) <= ceil((p+log_2 p)/2)+4.
The lower bound is at least ceil((p+log_2 p)/2), proving an additive gap at most four bits. QED.

The result concerns *worst-case raw peak width*. A two-round state observer optimized only for final state can require fewer transcripts than full transition recovery; the lower bound T_p applies specifically to the latter stronger objective. It also does not claim every observation pair is used, or that a future sequence of physical updates factors through this two-read observation.

## Exact finite checks

The already-published PREFIX-861 independent direct-transition enumerator checks that, for every 1<=p<=12, all N(p+1) legal ordered transitions map to DISTINCT pairs. The committed JSON reports exact equality between trajectories and distinct_output_pairs, for example:
p=8: 2304/2304; p=9: 5120/5120; p=11: 24576/24576; p=12: 53248/53248.
Arithmetic conditions h(g)>=p, gcd(q1,q2)=g and g a(a+2)>=N are checked for p=1..18.

The corresponding peak-width gaps to the counting lower bound for p=5..18 are
p:   5  6  7  8  9 10 11 12 13 14 15 16 17 18
gap: 3  2  3  2  1  2  2  2  2  2  1  1  1  1
so the finite observed maximum gap on that range is three bits. The universal four-bit guarantee follows from the proof and covers every p>=5.

Source evidence: awdawmip/enterprise-math@727d6ca2dee6f707e3dd3cabba600d2c21b12bc8, research_notes/portable_direct/PREFIX861_R6_COMMON_GCD_BALANCED_PORT_CHECK.py and PREFIX861_R6_COMMON_GCD_BALANCED_PORT_RESULTS.json, plus the PREFIX-861 proof.

## Next scientific question

Find a family of odd q1,q2 with smaller peak-width constant or prove a structural restriction beyond the counting bound. Distinguish transition recovery from terminal-only recovery, and test whether the requisite retained provenance/time memory can be embedded into an authorized native X6 event observer.
