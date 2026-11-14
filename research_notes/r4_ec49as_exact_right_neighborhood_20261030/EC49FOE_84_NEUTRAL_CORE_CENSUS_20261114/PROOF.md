# EC49FOE — 84 neutral BRC cache exchanges: exact forcing-core census

Date: 2026-11-14. Status: AUTHOR_PROVED / EXACT_FINITE_COMPUTATION / NOT_REVIEWED.
Parent: EC49FOD, PR #2368. Frozen scientific input pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. This is the native ordered signed-prefix rooted minimum-cover auxiliary problem; P000 and native X6 ontology are unchanged.

## Definitions

Native roots are (03,05,06,07). For configuration K, D_{K,r}(S) is the minimum rooted-prefix cover cost of demand set S at root r, reconstructed from the frozen 94-key, 178850-word dataset. Let R_{K,i} be the legal native roots of demand i.

Fix the same legal preassigned masks p=(0,5,138,8192) in that root order and the 18 unassigned labels
U=(4,5,6,8,9,10,11,12,14,15,16,17,18,19,20,21,22,23).

For T subset U, set
f_{K,p}(T) = min over all lawful disjoint root allocations T_r of T of sum_r D_{K,r}(S_r union T_r).
At threshold B=155, a forcing core is an inclusion-minimal T with f_{K,p}(T)>155. Define H_h=max_{|T|=h} f_{K,p}(T).

## Boundary-certificate theorem and proof

If f is monotone and H_{n-2}<=B for n=|U|, all strict forcing cores lie in layers n-1 or n. They are exactly (a) strict (n-1)-subsets, if any, and otherwise (b) U itself if f(U)>B. If f(U)<=B no strict core exists.

Proof: every smaller subset is contained in an (n-2)-subset and is non-strict by monotonicity. Every strict (n-1)-set is therefore minimal; U is minimal precisely when strict and all immediate deletions are non-strict. Rooted cover cost is monotone and a lawful larger assignment restricts to a lawful smaller assignment, hence f is monotone. This proves the theorem for any finite native rooted-cover instance satisfying its hypotheses.

## Exact 51-case / 84-edge result

The frozen FIRST_NEUTRAL_EDGES_EC49FNS.txt contains exactly 84 distinct single-key exchange edges with 51 distinct cache configurations. In the original exact 24-demand optimizer table, the endpoint triple (C, count, next_cost) agrees within all 84 edges: 78 edges (154,1,155), four (152,1,153), and two (144,1,145).

On every one of the 51 configurations, exact legal-root enumeration of all 153 size-16 subsets confirms H16<=155. The algorithm also checks all 18 size-17 deletions and U, i.e. 172 boundary subset-costs per configuration, 8,772 across all 51. It evaluates 1,084,428 actual legal-root assignment leaves in the rooted-cost solver, with exact integer arithmetic. The full 51-case subset lattice has 13,369,344 entries; boundary certification requires only the specified 8,772 subset-cost computations.

Complete finite classification:
- 39 configurations: f(U)=158, five minimal 17-cores U minus 4, 5, 6, 8, or 9.
- K=32296: f(U)=157, unique 17-core U minus 6.
- K=32279: f(U)=156, unique 18-core U itself.
- Remaining 10 configurations: f(U)<=155 and no strict core.

Exactly four of the 84 neutral edges change their strict obstruction hypergraph:
(32315,32279), (32318,32279), (32315,32296), (32318,32296).
The other 80 preserve the complete hypergraph. On this precisely enumerated family, core-hypergraph change is equivalent to a change of the rooted completion cost f(U).

The 32315↔32296 and 32318↔32296 exchanges give a sharper example: both endpoints have minimum forcing depth 17, but the core *sets* differ (five cores versus one). Thus the scalar minimum forcing depth h* does not determine the forcing-core hypergraph, even on a single neutral global-optimizer edge. On all four changing edges, the global 24-demand optimizer triple is identical at both endpoints. This displays the exact future-observer residual hidden by that global triple.

## Verification and provenance

Inputs: original signed-prefix master SHA256 cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e; frozen edge list and optimizer-table SHA256 recorded in EC49FOE_CERTIFICATE.json.gz.b64. Use the precise frozen source, not any later main data.

The exact Python verifier rebuilds rooted trie cost arrays from ordered signed words using the prior EC49FNY independent reference, validates common partial-mask legality, enumerates *all* legal root allocations for U and every 16/17-subset, checks all 84 original neutral optimizer triples and applies the proved boundary theorem. The complete 51-case certificate and input/source files are preserved in the companion evidence archive. Crosschecks: prior EC49FOD exhaustive five-case certificates agree in every full, H16, H17, deletion and minimal-core result; a separate top-down strict-core enumerator agrees where applied. Integer arithmetic, exact complete finite coverage, no approximate thresholds.

## Next

Derive a root-local perturbation or demand-overlap criterion predicting these four core changes from less than a complete 172-subset boundary census, and compare the fixed auxiliary masks with actual original DFS search nodes. This file records a scientific result, not a formal Task/CLAIM/Result or independent mathematical admission.