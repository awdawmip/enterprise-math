# PREFIX-542 — Phase-only binomial transform for rooted BRC–gate counts

Date: 2026-11-06. Research line: RS-X6-NATIVE-ROTATION-DYNAMICS.
Frozen scientific input: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Predecessors: PREFIX-539 (local BRC cocycle), PREFIX-541 (tropical support).
Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / BENCHMARKED / UNREVIEWED / NOT_ADMITTED. Independent author-side mathematics; no native CLAIM or Result.

## Exact model and new statistic

Four STAR triples: (1,3,6),(1,4,5),(2,3,5),(2,4,6). The declared model has 48 directed signed phases, 144 legal phase edges, two independent INNER/OUTER bits for every transition, and fixed gate target T=(A,+L1,-L3). The initial previous bit b_0 is OUTER (=0). From each phase there are three successors.

For a fixed phase path i_0=s,i_1,...,i_d, define its first-axis BRC cancellation p=p_1 by the frozen endpoint formula, equivalently by the PREFIX-539 nonnegative local cocycle. Define k=#{t: 2<=t<=d and i_t=T}, the number of potential gate target-arrivals after the first transition. The first arrival t=1 is excluded because b_0=0. Let C_s(d;p,k) count unlabeled phase paths with those statistics, and P_s(d;q,z)=sum_{labeled histories} q^p z^H, where H is the number of actual consecutive-INNER gate events.

## Theorem 1: disjoint gate-pair binomial transform (all lengths)

For every fixed root s, d>=0 and formal q,z, the exact identity in Z[q,z] is

    P_s(d;q,z) = SUM_(p,k) C_s(d;p,k) q^p 2^(d-2k) (3+z)^k.

Proof: An actual gate at t>=2 occurs exactly when i_t=T and b_(t-1)=b_t=INNER. Target T has no self-edge, so target arrivals cannot occur in adjacent steps. Thus the two free branch bits allocated to distinct potential gate arrivals are disjoint. For each of k such pairs, precisely one of four choices triggers the event (weight z); three do not (weight 1). All remaining d-2k branch bits are freely chosen and contribute 2^(d-2k). BRC depends only on the underlying phase path. Multiply and sum over unlabeled phase paths. For d=0,1 there are no potential gate pairs, and the identity remains valid. QED.

In particular, 0<=k<=floor(d/2), each phase path has 2^d labels, and the total at q=z=1 equals 6^d.

## Theorem 2: invertibility, rooted classes, exact support

Define C_s(d;q,x)=SUM_(p,k) C_s(d;p,k)q^p x^k. Then

    P_s(d;q,z) = 2^d C_s(d;q,(3+z)/4)
    C_s(d;q,x) = 2^(-d) P_s(d;q,4x-3).

These are formal polynomial identities over Q. Consequently, two roots have the same full labeled BRC–gate polynomial at a depth iff they have the same phase-only (p,k) polynomial at that depth. The equivalence also holds for simultaneous equality at every depth. The 26 rooted full-length equivalence classes proved in PREFIX-533 can therefore be represented via the phase-only observer without re-proving the prior classification.

For every attainable p at fixed s,d, every k with C_s(d;p,k)>0 contributes all gate counts h=0,1,...,k with strictly positive coefficients. Thus the exact occupied fiber is

    {h: [q^p z^h]P_s(d;q,z)>0}
      = {0,...,max{k:C_s(d;p,k)>0}}.

This recovers the PREFIX-541 gate-support interval theorem. Under uniformly random independent INNER/OUTER bits conditioned on a fixed phase path, H is Binomial(k,1/4); the k trials use disjoint pairs.

## Explicit three-seed 48-phase recurrence

Let r=sigma(s) in {-1,0,+1}. For every directed edge i->j, use PREFIX-539's exact tau_r(i,j) in {0,1}. Initialize U^r_0(i;q,x)=1. For n>=0 define

    U^r_(n+1)(i;q,x)
      = SUM_(j in NEXT(i)) q^tau_r(i,j) x^[j=T] U^r_n(j;q,x).

For d>=1,

    C_s(d;q,x)
      = SUM_(j in NEXT(s)) q^tau_r(s,j) U^r_(d-1)(j;q,x),

and C_s(0;q,x)=1. The first transition intentionally has no potential-gate x marker; every subsequent target arrival does. Path decomposition and the exact additive BRC law prove the recurrence by induction. All 48 roots are extracted from three shared 48-component phase polynomial trajectories, one for each r. This is a sufficient observer-specific representation, not a claim of minimal dynamic state dimension.

## Executed finite certificate and implementation comparison

The self-contained Python standard-library certificate computes the 48-phase recurrence and binomial conversion, then compares all coefficients with two distinct methods: (i) the already published 49-coordinate rank-one reverse polynomial lift (PREFIX-537), and (ii) raw forward INNER/OUTER-labeled dynamic programming with the original endpoint BRC formula. For all 48 roots, at all depths 0 through 24 inclusive, the 1200 complete polynomial equalities pass. Each phase histogram totals 3^d; each labeled histogram totals 6^d. At depth 24, there are 1876 nonzero joint coefficients across the 48 roots, with 26 distinct rooted polynomials and maximum k=6. Root index 0 at depth 6 gives 14592+28800q+960qz+2176q^2+128q^2z.

An extended executed benchmark (local supplementary evidence) measured all roots and all depths 0..N including setup and full q,z output extraction, CPython/Linux, tracemalloc active, three repetitions:
- N=8: phase-only median 0.0766 s, traced peak 443315 bytes; rank-one 49 median 0.0408 s, 314648 bytes.
- N=16: phase-only median 0.3711 s, 1769407 bytes; rank-one 49 median 0.1841 s, 1126032 bytes.
- N=24: phase-only median 1.3417 s, 4692203 bytes; rank-one 49 median 1.0449 s, 2810000 bytes.

Measured timing spread was substantial. The rank-one 49 implementation is faster and smaller in this Python comparison. The new benefit is an exact positive-weight phase-only factorization, support certificate, and conditional binomial law, not an asserted speedup.

Run PREFIX542_exact_certificate.py (no external dependencies) to reproduce 1200 three-way coefficient checks. The detailed executed benchmark program and full output JSON are retained in the supplementary evidence package.

## Observer-safety and next question

This is an exact representation for the declared first-axis BRC count and gate count of fixed-depth paths. It is a many-to-one projection of native Cell identities and ordered INNER/OUTER paths, so arbitrary later Cell/provenance-sensitive operations remain on their native typed carrier. No generalized X6 rotation or physical time law is claimed.

Next PREFIX-543: derive gate factorial moments and conditional correlations at fixed BRC p from the phase potential-arrival polynomial; test update under alternate initial INNER-bit choices and whether a phase-only sufficient observer can accommodate them without rebuilding the native labeled path dynamics.
