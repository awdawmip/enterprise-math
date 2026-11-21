# R762IB — Six-axis parity-core theorem and three exact obstruction orbits

Date: 2026-11-21. Status: AUTHOR_PROVED / EXHAUSTIVE_EXACT_COMPUTATION / NOT_REVIEWED.

Scientific input: frozen six-axis composite Port candidate of \`RS-X6-TRIADIC-CLOSURE-DYNAMICS\`, \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. Prior exact lattice \`L\`: R762IA@87ae1942f29bab7be629c3fbbe3c5503281e90a2. Current norms from \`docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context\`. This note proves statements about the *composite support/sign observer*, retaining support multiplicity, Port admissibility as a separate predicate, and P000 primitive \`TRIADIC_CLOSURE_E\` as a separate lift.

## Definitions

Let X={0,1,2,3,4,5}, T=all 20 three-subsets of X in lexicographic order and h_S=sum_{i in S}e_i in Z^6. A finite support multiset n=(n_S) has m=sum n_S events and H=sum n_S h_S. It is signable when the individual occurrence signs eps_t in {-1,+1} can be chosen with sum eps_t h_{S_t}=0; denote its positive signability count by C(n)>0.

Define q_S=floor(n_S/2) and parity core delta_S=n_S mod 2, with odd-core support O={S:delta_S=1}. Define the 2-overlap graph G2(O) whose vertices are the *distinct* supports in O; two supports are adjacent exactly when they share two axes. This graph is a **test only for signability**; it is not the original 15-Port walk graph. The original event identities, order, endpoints and signs must remain available for Port realization.

## IB1 — Exact integral-span congruence removes a false obstruction route

R762IA proved L=span_Z{h_S}={x in Z^6:sum_i x_i=0 mod 3}. For *any* n, with m=sum n_S and H=sum n_S h_S:

    H in 2L   <=>   every H_i is even.

Indeed H in 2L has even coordinates. Conversely H_i all even implies sum_i H_i=3m is even, hence m is even. Then sum_i (H_i/2)=3m/2 is divisible by 3, so H/2 in L. Consequently a proposed even-coordinate H outside 2L **cannot occur** for this candidate model.

This does *not* make H even sufficient for C(n)>0: the lattice condition forgets the individual occurrence multiplicity bounds. The exact signability criterion is that there exist integers 0<=k_S<=n_S with sum_S k_S h_S=H/2.

## IB2 — Parity-core reduction for arbitrary multiplicities

If C(delta)>0 then C(n)>0. Proof: for each S, assign the 2q_S extra occurrences in q_S cancelling (+,-) pairs, and use a fixed zero-sum signing of the remaining delta_S occurrences. This gives a constructive zero-sum signing of all n events. Equivalently, if C(n)=0 then C(delta)=0. This is one-way; a bad core may become signable after even multiplicity additions.

## IB3 — Complete finite six-axis parity-core classification

The six axis-incidence equations on 20 triple indicators have GF(2)-rank 6. Thus exactly 2^(20-6)=16,384 parity cores (including empty) have even coordinate degree. All these cores have even support weight m because each triple has three axes.

Exhaustive exact enumeration of *all 16,384 cores*, with independent C++ and Python checkers, gives:

| Core weight m | Even-coordinate cores | Unsignable cores | G2-connected cores | Unsignable and G2-connected |
|--:|--:|--:|--:|--:|
| 0 | 1 | 0 | n/a | 0 |
| 2 | 0 | 0 | 0 | 0 |
| 4 | 165 | 30 | 90 | 0 |
| 6 | 1,200 | 180 | 1,020 | 0 |
| 8 | 3,930 | 0 | 3,915 | 0 |
| 10 | 5,792 | 20 | 5,772 | 0 |
| 12 | 3,930 | 0 | 3,930 | 0 |
| 14 | 1,200 | 0 | 1,200 | 0 |
| 16 | 165 | 0 | 165 | 0 |
| 18 | 0 | 0 | 0 | 0 |
| 20 | 1 | 0 | 1 | 0 |

The 230 unsignable nonempty cores form exactly **three orbits under permutation of the six axes**. With triples written as three digit labels, representatives are:

- **weight 4, orbit size 30**: 024, 035, 125, 134 (all six axis degrees 2).
- **weight 6, orbit size 180**: 012, 015, 025, 034, 123, 124 (axis degrees 4,4,4,2,2,2).
- **weight 10, orbit size 20**: 012, 013, 014, 025, 035, 045, 125, 135, 145, 234 (axis degrees 6,6,4,4,4,6).

Orbit sizes are calculated by applying all 720 axis permutations to each exact representative and checking that the resulting 30+180+20 masks equal the full computed unsignable set. Each representative is verified to fail the exact half-incidence subset sum; all other even-coordinate core masks pass.

**Universal corollaries for arbitrary finite n.** If H is coordinate-even and delta=0, or G2(O) is connected, then C(n)>0. A nonsignable n can have only a parity core in one of the three displayed orbits; in particular its odd-core support count lies in {4,6,10}, and its odd-core 2-overlap graph is disconnected. The corollary does not assume or imply Port connectivity.

## Reproducibility and meaning

\`R762IB_CHECK.py\`: independent nullspace-basis enumeration of all 16,384 GF(2) cores; exact (non-floating) meet-in-the-middle six-coordinate subset-sum signability; exact G2 connectivity; complete S6 orbit enumeration. Local run output matched the table and the three orbit sizes.

\`R762IB_SCAN.cpp\`: independently scans all 2^20 distinct support masks and checks the six degree parities, exact six-coordinate meet-in-the-middle and G2 connectivity; compiled as \`g++ -O3 -std=c++17\` and run locally. Its per-weight counts agree with Python exactly. The C++ checker does not compute Port walks. Both checkers are finite exhaustive certificates for the **specific six-axis universe**, not a symbolic all-dimensional theorem.

The IB2 implication is a mathematical proof for every finite multiset over this fixed universe; IB3's entire core table is certified by the executable exhaustive search. The result strengthens the single-histogram signability route, but leaves open whether there exists n with H even, C(n)=0 and N_p(n)>0 for a genuinely legal closed Port walk. Such a witness, if it exists, must have one of the three odd cores but can include even-multiplicity bridge supports. Candidate composite calculations are not primitive P000 TRIADIC_CLOSURE_E dynamics.

## Next experiment

Enumerate even-multiplicity extensions of exactly the three odd-core orbits. First test C(n)=0 using bounded integer incidence, then test actual closed Port realizability N_p(n)>0 by source-preserving event/Port dynamic programming (Eulerian connectivity, not merely G2). Preserve the first precise witness or a certified covered range. Do not regenerate R762IA's aggregate local-limit calculation; do not use H outside 2L as a proposed even-H obstruction. Independent review and native Activity/PROGRESS remain separate from these Source files.
