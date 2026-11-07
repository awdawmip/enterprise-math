# EC49EXG — Unique H8/M3/S4 BRC-key schedule, exact lower bound, and 144-edge witness

Date: 2026-11-03 (Asia/Shanghai). Classification: AUTHOR_FINITE_CLASSIFICATION / EXACT_INTEGER_TRIE_BOUND / EXACT_RATIONAL_WITNESS_PASS / MILP_OPTIMUM_REPORTED / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.
Parent: EC49EXF, existing Draft PR #1730. Frozen scientific pins: global \`773d538180bfb49e24cffeb35c3ee75eb0628e2e\`; enterprise-math \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`. Current behavioral rules, ACTIVE worldview, P000 and portable protocol were separately fetched from canonical main on 2026-11-03. No physical-dynamics or new P000 claim.

## Exact setting

The seven operation words are native signed-X6 primitive paths
a=(-1,-1), b=(-2,-2), c=(+1,+2,-1,-2), d=(+2,+1,-2,-1), e=(+3,+1,+1,-3), f=(+1,-1), g=(+2,-2).
The signed indices name native axes E1,E2,E3; native axes E4,E5,E6 are explicitly zero in THIS RESTRICTED INPUT FAMILY (no general three-dimensional layer identification). At each h=2,...,8, choose operation words of length h with native signed displacement (2,0,0,0,0,0), all sharing a complete six-axis positive count key p_h. Their stacked nine initial seam histories into five observer buckets N,A,B,AB,BA must have rank nine over Q. Keep ordered primitive steps, branch identities, transfer signatures, and symbolic strictly positive paired BRC monomials X_p=product_i x_i^(p_i), Y_p=product_i y_i^(p_i) typed separately. E is the number of nonempty signed primitive-step prefixes in the union; M counts different full p_h; S counts different transfer signatures.

Earlier EC49EXD/EC49EXF finite rank classifications establish that every full-rank fiber requires four signatures T4 (packed integers 1836687, 1867942, 1872656, 1873981) or two signatures T2 (1836425, 1866380). As h2 forces T4, S<=4 forces all four T4 at every horizon.

## Theorem 1 — unique three-key schedule

For H=8, M=3, S<=4, the sequence of six-axis positive BRC keys is unique:

| h | p_h (six components) |
|---|---|
| 2 | (3,1,1,0,0,0) |
| 3,4 | (4,2,1,0,0,0) |
| 5,6,7,8 | (6,4,1,0,0,0) |

Proof. A returning word has #b=0 and #e=#a+1. With w=#e, r=#c+#d, f=#f, g=#g, put u=r+2w+f and v=r+g. The length and key satisfy h=2w-1+r+f+g, p=(u,v,w,0,0,0). For each h<=8 enumerate the complete finite nonnegative integer solutions (w,r,f,g), every split r=#c+#d, all distinct multiset permutations, then calculate exact nine-state transfer signatures. Full T4-capable key counts for h=2,...,8 are (1,3,7,13,22,34,50), with all 340,064 h8 returning words included in the precursor C++ enumeration; Python verifies the T4-key counts independently. At h3 the only T4 keys are (3,2,1),(4,1,1),(4,2,1). The h2 key cannot cover h3 under T4. The key supporting h8 cannot cover h4, so the h3 key must cover h4; only (4,2,1) does. Intersection of h5,h6,h7,h8 T4-key sets excluding the first two keys is the singleton (6,4,1). Direct exhaustive pair enumeration gives exactly one feasible pair. Every horizon is consequently forced as shown. This is an exact finite classification, not a sampled search.

## Theorem 2 — certified interval and computed candidate optimum

Let E* be the least E at H8/M3/S<=4 in the stated finite model. Then

**140 <= E* <= 144.**

For the unique schedule the h2..h7 prefix subproblem has exact E7=128, established in the EC49EU third key-schedule case (full 20-color signed-prefix integer DP, independently crosschecked there). Let U be the union of ALL native signed prefixes of every permissible T4 word at h2..h7 with the unique keys, i.e. a superset of any truly paid predecessor prefixes. It contains exactly 11,116 distinct nonempty prefixes. Treat all U edges as free, and optimize the h8 fiber with key (6,4,1) to cover T4. There are 2,240 eligible words, 560 per required signature; their signed-native trie has 15,887 nodes. A four-color exact integer OR-mask trie DP, with each edge outside U charged one, gives minimum **12** new edges. Subtree induction proves the OR-mask recurrence enumerates all subsets of terminal words without double-charging shared prefixes. Therefore E8>=128+12=140, independently of predecessor path choices.

An explicit authentic native-X6 path family attains E=144; the ordered operation words are:

| h | Four selected words | New prefix edges | Cumulative E |
|---|---|---:|---:|
| 2 | ed, de, ec, ce | 28 | 28 |
| 3 | edd, ded, ecc, cec | 16 | 44 |
| 4 | edgf, degf, ecfg, cefg | 12 | 56 |
| 5 | edddd, deddd, ecccc, ceccc | 32 | 88 |
| 6 | edddgf, deddgf, ecccfg, ceccfg | 12 | 100 |
| 7 | edgffgd, degfgfd, ecfggfc, cefgfgc | 32 | 132 |
| 8 | edgffggf, degfgfgf, ecfggffg, cefgfgfg | 12 | 144 |

Exact rational Gaussian elimination independently verifies observer rank 9 at every horizon. Direct signed primitive-step reconstruction verifies full X6 displacement (2,0,0,0,0,0), unique per-h full six-count key, exactly M=3 and S=4, and 144 distinct native prefixes.

Separately, SciPy/HiGHS 1.8.0 solves the full joint 28-color 0–1 native-prefix tree MILP (23,887 nodes) and reports optimum additional cost 116 above the mandatory 28-edge baseline, dual bound 116, mip gap zero: **reported global MILP optimum E=144**. The solver run is a reproducible computational result. A stand-alone exact-integer global 28-color DP proof or independently checkable exhaustive integer optimality certificate would close the remaining four-edge mathematical certificate gap between the rigorous bound 140 and the solver's reported 144. No unconditional mathematical lower bound of 144 is asserted here.

## Reproduction and evidence

- \`VERIFY_EC49EXG.py\` (Python standard library only): complete key-fiber T4 classification h2..h8, 4-color exact integer OR-mask DP with every earlier eligible prefix free, exact rational observer-rank check and signed native path witness; **actual executed status PASS**, with counts [1,3,7,13,22,34,50], only one M3/S4 schedule, E in [140,144], rank nine and E=144.
- \`MILP_EC49EXG.py\` (SciPy/HiGHS): independently constructs the full 28-color signed-prefix tree integer program, **actual executed status PASS**, 23,887 nodes, optimizer E=144, returned matching primal/dual bound and zero reported gap.
- \`EC49EXG_EXECUTED.json\`: exact checker result and solver summary; \`NEXT_EC49EXH.md\`: next unit and explicit acceptance standard.

The prior H7 lower bound E7=128 is sourced from EC49EU's immutable \`EC49EU_M3S4_EXECUTED.json\` and proof at EC49EU/H7 M3 S4 on PR #1730. The H8 M3 S6 global E=112 theorem is the published EC49EXF precursor. Hence allowing two additional observer signatures reduces the known strictly finite model optimum from the current four-signature 144-edge witness to the certified six-signature 112-edge optimum; the difference 32 is a comparison of an upper witness and an exact optimum until E*=144 has independent integer certification.

## Source, authority and remaining scientific problem

GitHub authenticated user awdawmip has repository admin and push permission. Native Enterprise Math gateway v0.6.11 on 2026-11-03 reported research_authority_granted=false; owner/control-task read returned CONTROL_QUOTA (active jobs at limit 5/5). Active native owner was not authenticated and no CLAIM, Research Result or independent Driver review/admission is asserted. This is an author-side portable PR draft. P000, ACTIVE worldview, immutable scientific pins, source firewall and existing claims are unchanged.

Next EC49EXH: obtain a fully exact integer global certificate E>=144 for this unique schedule (or a smaller legitimate witness, if the MILP or model checker is corrected). Reuse the 28-color signed-prefix OR-mask DP with cutoff, or an independent exact integer branching certificate. In parallel test H8 M4 S<=6 for a smaller E and build the complete H8 Pareto frontier.