# R762CK — Open X6 path area, parity obstruction and exact BRC repair

**Task:** RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142. **Scientific pin:** P000 at a72226e2430ffa4786321ac86e7f0c599d5f0389, V17 signed native paths at the same pin. **Predecessor:** R762CH, immutable PR #2575@1c860018c4399e1b7497192ef818e3567390d2e2 (closed-path pair-area); R762CJ, PR #2582@2ac8e3826d9ce1d77c057d82aafc2a71dac1546f (K4 observer repair). Independent mathematical review: NOT_REVIEWED.

## 1. Question and exact typing

R762CH uses the ordered pair-coordinate functional C_ij only for **closed** X6 words. A natural alternating extension to **open** signed-X6 words introduces a factor of two and a 2-torsion observer defect. Establish the exact transport, identify which finite histories are realized by V17 shortest paths, and determine the repair cost of losing that factor.

Let H=(d_1,...,d_m), where every d_t belongs to the P000 signed native primitive direction set {±e_1,...,±e_6}; choose a chart anchor of the affine X6 Cell torsor. Put z(H)=Σ_t d_t. For i≠j define the ordered two-step interaction

P_ij(H)=Σ_{1≤s<t≤m} d_{s,i}d_{t,j}

and for i<j define the antisymmetric **path diagnostic**

A_ij(H)=P_ij(H)-P_ji(H).

The fifteen A_ij form a formal alternating pair carrier; no two-dimensional native plane, extra spatial axis, Euclidean angle or TRIADIC_CLOSURE_E license is introduced. P_ij is an ordered source statistic and A_ij is its alternating readout. Positive BRC counts remain separate from signed force amplitudes.

## 2. Theorem A — exact open-path transport and integral normalization

For all primitive X6 paths H,K and all i<j,

(1) P_ij(H)+P_ji(H)=z_i(H)z_j(H);

(2) A_ij(H)=2P_ij(H)-z_i(H)z_j(H);

(3) P_ij(HK)=P_ij(H)+P_ij(K)+z_i(H)z_j(K);

(4) A_ij(HK)=A_ij(H)+A_ij(K)+z_i(H)z_j(K)-z_j(H)z_i(K).

Thus A mod q and z mod q determine P mod q for every odd q through the inverse of 2. For **even** q, A mod 2q and z mod 2q determine P mod q by exact integer division by 2; A mod q with z mod q is not generally sufficient.

**Proof.** Expand z_i z_j as a sum over two time indices. The same-time terms vanish because one primitive step has support on exactly one axis. The two strict orderings give P_ij+P_ji, proving (1); subtracting gives (2). Partition pairs (s,t) in HK into those internal to H, internal to K and crossing the H/K boundary. The crossing sum is z_i(H)z_j(K), proving (3); subtract its transpose to obtain (4). The divisibility in (2) follows in Z, not merely modulo q. For odd q, 2 has a modular inverse. For even q, an integer representative of A+z_i z_j modulo 2q has a well-defined even residue, whose half yields P modulo q. QED.

For a closed word z=0, P_ji=-P_ij and A_ij=2P_ij. In this case P_ij coincides exactly with R762CH's closed-loop C_ij. Consequently **reducing the alternating open-path diagnostic modulo q before converting to the closed-loop C loses 2-primary information whenever q is even**.

## 3. Theorem B — sharp q-adic BRC repair from alternating to ordered area

Fix q≥2 and E a set of d distinct unordered axis pairs (0≤d≤15). Use exactly the labeled closed B/L source family of R762CH: q independent four-step slots for each pair in E, with B_ij=(+e_i,-e_i,+e_j,-e_j) and L_ij=(+e_i,+e_j,-e_i,-e_j). Every history has the same endpoint, time and full signed-step histogram. Its ordered closed-loop residue C_E ranges independently over (Z/qZ)^d; the alternating observation is A_E=2C_E mod q.

Let g=gcd(2,q). The exact alternating-observer quotient contains (q/g)^d classes, and **every** nonempty A_E fibre contains g^d distinct ordered C_E states. The optimal extra fixed-length information restoring all C_E states is therefore

R_alt→ordered(q,E)=log_2(g^d) = {0 bits if q is odd; d bits if q is even}.

**Proof.** R762CH gives surjectivity of C_E over (Z/qZ)^d on the specified common coarse fibre. Multiplication by 2 on Z/qZ has kernel of size g and image of size q/g. Its product on d independent coordinates therefore has uniform fibres of size g^d. Any reconstruction needs at least log_2(g^d) fixed bits; record one binary kernel selector per coordinate when q is even (the two solutions differ by q/2), and no selector when q is odd. This attains the lower bound. The BRC source weights are positive and every C_E residue has at least one labeled source, so source multiplicity cannot eliminate either branch of an ambiguous fibre. QED.

For any even q set k=q/2. The two equal-length, equal-histogram closed paths B_ij^k and L_ij^k have C_ij residues 0 and k, respectively, but alternating residues A_ij=0 in both cases modulo q. This is an explicit obstruction, not merely a counting argument.

At q=2, all 15 independent closed-pair residues can be erased by reducing A modulo 2; recovering the R762CH C-observer then needs exactly 15 bits for E consisting of all 15 pairs. These bounds concern the specified pair-source family and its diagnostic observations, not authentic triadic event admission.

## 4. Theorem C — shortest six-axis path order, transitive tournament and exact observer loss

Fix signs s_i∈{+1,-1}, i=1,...,6, and target z=(s_1,...,s_6). V17's shortest signed-X6 paths to z have precisely six steps, one s_i e_i on each axis, and exactly 6!=720 ordered realizations. For a path corresponding to permutation π, let i≺π j denote that axis i occurs earlier than j. Then for each i<j,

P_ij(H_π)=s_i s_j · 1[i≺π j],
A_ij(H_π)=s_i s_j · (2·1[i≺π j]-1).

Hence the 15 signs A_ij/(s_i s_j) are precisely the edge orientations of a **transitive tournament** on six named axes. Exactly 720 of the 2^15 formally possible sign patterns are realizable, one for each total ordering. Each triangle's edge orientations must be acyclic, and an acyclic tournament uniquely determines the total order.

When q=2, A_ij mod 2 is 1 for every pair, independent of the order and of the signs. The alternating observer has one fibre of size 720; its minimum fixed-length exact repair is ceil(log_2 720)=**10 bits**. A lexicographic permutation rank 0,...,719 achieves the bound. For q≥3, +1 and -1 are distinct modulo q, and known endpoint signs recover all pair comparisons and thus π; the exact repair is **0 bits**. At q=2, retaining the raw ordered P_ij mod 2 also recovers every comparison without extra repair.

**Proof.** V17 gives m=Σ_i |s_i|=6 and 6! multinomial realizations. Each axis appears once, so exactly one of P_ij,P_ji has the nonzero product s_i s_j. The displayed identities follow. A set of pair comparisons comes from a total order iff its tournament has no directed cycle, equivalently no directed triangle: a shortest directed cycle in a tournament would otherwise contain a directed triangle. Each total order induces a different orientation and there are 720. Reduction modulo 2 maps both ±1 to 1. For q≥3 the two residues differ, and a topological ordering gives π. The bit bounds follow from exact fibre sizes. QED.

## 5. Scientific consequence and boundaries

This result separates three distinct objects: the full ordered signed source word, the open-path pair interaction P, and the alternating area diagnostic A. A source-safe quotient has to specify which one future admissible updates actually query. In particular, R762CH's abstract q^15 independent *closed-loop* residues cannot be transferred unchanged to shortest monotone six-axis paths: the latter carry only 720 realizable order patterns and strong triple-order constraints. Conversely, the alternating reduction modulo even q can erase information that the ordered closed-loop C actually retains.

**Next native dependency:** obtain the genuine TRIADIC_CLOSURE_E Cell/Port/Link event predicate and actual V29/V39 transport, identify whether its future guards use ordered interactions P, alternating A, other provenance, or none. Test event-factorization on the exact fibres above. These mathematical statements are proved for P000 signed path words, V17 shortest paths and the explicitly declared R762CH B/L source model; no conditional diagnostic is called a licensed native event.

## 6. Validation and audit

The accompanying R762CK_VERIFY.py performs exact integer computations, enumerating all 6!·2^6=46,080 shortest six-axis signed words and checking each of 15 pair comparisons: **691,200 pair-level checks**. It checks q=2,...,12 for d=3 the fibre counts ((q/g)^3) and maximum fibre size g^3, and q=2,4,6,8,10 for the explicit same-histogram closed-loop obstruction. R762CK_EVIDENCE.json records the results. These author-side checks are finite consistency verification; the proofs above give the general conclusions. Independent review remains NOT_REVIEWED.

**Reproducible sources:** [frozen P000 triadic definition](https://github.com/awdawmip/enterprise-math/blob/a72226e2430ffa4786321ac86e7f0c599d5f0389/definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md); [frozen V17 signed shortest-path BRC](https://github.com/awdawmip/enterprise-math/blob/a72226e2430ffa4786321ac86e7f0c599d5f0389/research_notes/X6_SIGNED_PATH_BRC_AND_PRIMITIVE_LINE_V17_20260905.md); [R762CH closed pair-area theorem](https://github.com/awdawmip/enterprise-math/blob/1c860018c4399e1b7497192ef818e3567390d2e2/research_notes/portable_direct/R762CH_PAIR_AREA_FRAME_TRANSPORT_THEOREM.md).
