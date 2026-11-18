# EC49FEH — Exact 94-edge optimum for the EC49FDN five-key inventory

Date: 2026-11-08. Status: author-side exact finite theorem, independently cross-checked; mathematical admission pending. Frozen science pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Predecessor: EC49FEG at commit 24c6151e4dd69f1f3552bdf07299bd865cd85d1b, with the earlier EC49FDN rank-2200 witness.

## Theorem

In the original six-operator signed native-X6 word grammar and nine-state observation automaton, fix the following exact full positive-BRC-key inventory:

K = {(3,1,1), (3,2,1), (4,3,1), (4,4,1), (5,5,1)}.

For horizons H2,...,H9, impose native endpoint +2E1 on each word, path quotas (4,2,2,4,2,2,4,2), and all four rank-nine observation clauses 18,20,33,40. A word may use **any** member of K, independently of the other words and horizons, and any legal ordering of its primitive operations.

**Exact finite optimum: min C_native(W) = 94 distinct nonempty ordered signed-X6 path prefixes.**

This is stronger than optimizing EC49FDN's originally specified single-key-per-horizon assignment: it includes all possible within-window mixing, especially H5 mixing the BRC keys (4,3,1) and (4,4,1). The explicit 22-word EC49FDN witness attains 94.

## Definitions and complete enumeration

Six signed primitive operation words, each retaining ordered native-axis steps, are:

- a = (-1,-1)
- c = (+1,+2,-1,-2)
- d = (+2,+1,-2,-1)
- e = (+3,+1,+1,-3)
- f = (+1,-1)
- g = (+2,-2).

Here signed integer ±i means a signed unit step on native axis Ei; it is not a position or a final Cell address. The complete BRC key (x,y,z) counts all **positive** native steps on E1,E2,E3, preserving key identity; the prefix cost uses the *full ordered signed* native sequence, not its endpoint or positive histogram. The nine-state transition and signature tables are exact literals in the certificate.

For an operation word of length h, endpoint +2E1 and full key (x,y,z), write r = number of c and d symbols combined. The necessary operator counts are

a = z-1; c+d = r = x+y-h-1; e = z;
f = h+1-y-2z; g = h+1-x.

The executable proof enumerates every nonnegative such multiset, every c/d split, and every word permutation under the original nine-state automaton. All returned candidates satisfy the actual endpoint and key by direct recomputation.

The four rank-nine clauses have signatures: 16 covers 18 and 20; 32 covers 33 and 40; each of 1,2,4,8 covers exactly one of the four clauses. Therefore any quota-two horizon must contain 16 and 32. All candidate words in the quota-four horizons H2,H5,H8 of this particular key inventory have only 1,2,4,8, so these horizons must contain exactly one of each. This yields 22 mandatory horizon/signature groups.

The candidate-key table further forces:
H2,H3 -> (3,1,1);
H4 -> (3,2,1);
H6 -> (4,3,1);
H7 -> (4,4,1);
H8,H9 -> (5,5,1).
H5 is the only mixed-key window and may choose words from (4,3,1) or (4,4,1) independently, including mixtures. No restriction on their ordering or sharing is imposed.

## Proof: complete four-case depthwise lower bound

All four H2 words are forced: ce, ec, de, ed. For H3, the 16/32 pair has precisely four possibilities:

(feg, gef), (feg, gfe), (fge, gef), (fge, gfe).

Every such early H2/H3 set E has |E| = 42 distinct nonempty native step prefixes. For each of the 16 compulsory late horizon/signature groups g in H4..H9, let P_g be the **entire** pool of signed native paths from every allowed key in K.

At each positive native depth d, keep only the groups all of whose candidate paths reach depth d. Every selected late path of such a group must have one prefix node of depth d. Regard all nodes of E as free and find the exact minimum m_d(E) of additional depth-d prefix nodes that cover all groups left uncovered by free nodes. The precise set-cover instance has one label for every active (horizon,signature) group and one candidate covering subset for each possible depth-d path prefix. Redundant subsets are removed only when dominated by supersets. A recursive bit-mask dynamic program exhaustively evaluates the minimum for every possible remaining-label mask.

For any legal complete system W whose early path set is E, every relevant depth-d selected-prefix set covers the corresponding groups, so it uses at least m_d(E) prefixes outside E. Different depths are disjoint. Optimizing each depth independently is a relaxation of choosing consistent complete paths, therefore

C_native(W) >= |E| + sum_{d >= 1} m_d(E).

The calculation is exact finite integer combinatorics. **For all four early variants**, the depth d = 1,...,20 vector is

[0,0,0,0,0,0,0,0,2,2,4,6,6,6,2,2,4,6,6,6].

Its sum is 52. Thus C_native(W) >= 42 + 52 = 94 for every complete admissible word family. The explicit EC49FDN 22-word system reaches 94. This proves the theorem.

## Reproduction and verification

The adjacent Git text artifact EC49FEH_evidence.tar.xz.b64 contains a lossless encoded archive with:
EC49FEH_EXACT_CERT.py (self-contained Python standard-library exact enumerator and bitmask DP);
EC49FEH_CERT.json (executed output, complete word candidate counts, all four depth vectors, and the 22-word witness);
EC49FEH_INDEPENDENT_CHECK.py (independent SciPy/HiGHS MILP formulation of each depth's set cover);
EC49FEH_INDEPENDENT_CHECK.json (80/80 matching solved instances, 4 variants × 20 depths, solver gap 0);
EC49FEH_MANIFEST.json (source hashes and output provenance).

Decode the archive with: base64 -d EC49FEH_evidence.tar.xz.b64 | tar -xJf -

Execute the exact proof: python EC49FEH_EXACT_CERT.py > EC49FEH_CERT.json

Execute the second solver check in a SciPy environment:
python EC49FEH_INDEPENDENT_CHECK.py > EC49FEH_INDEPENDENT_CHECK.json

The mathematical lower bound is certified by the exhaustive integer DP. The MILP results are a separate cross-check; MILP optimality alone would not replace the exact enumeration proof. The witness is directly re-expanded to all native signed steps and checked against the true five keys, endpoint and observation signatures.

The project P000 and active discrete six-spatial-axis worldview are preserved. This is a finite ordered-path and positive-key theorem, not a physical heartbeat propagation or signed-phase cancellation claim.

## Next EC49FEI

Retain the 22-path quotas and the nine-state clauses, then change **one complete BRC key** of K at a time while allowing all legal placements. First apply this exact per-depth cover filter; a lower bound >=94 excludes that inventory for the <=93 target, whereas a bound <=93 identifies a concrete family requiring a joint-path optimization. In parallel, test changes in H7 path count and signatures if the mother problem allows that coordinate.

Research provenance: GitHub author-side artifact only. Native researcher identity/CLAIM, active owner and independent Driver acceptance require separate current authenticated receipts.
