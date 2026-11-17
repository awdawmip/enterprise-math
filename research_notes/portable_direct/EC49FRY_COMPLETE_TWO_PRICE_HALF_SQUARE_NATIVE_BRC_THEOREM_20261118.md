# EC49FRY — exact full two-price half-square native BRC phase diagram (eight trees)

**Frozen scientific input:** \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\` (unaltered). **Date:** 2026-11-18. Continues EC49FRW #2663 and EC49FRX (#2666). **Mathematical status:** AUTHOR_PROVED / EXACT_FINITE_BELLMAN_AND_EIGHT_TREE_REPLAY / NOT_REVIEWED. Independent portable research, without a canonical task CLAIM.

## Exact statement

In original BRC class16943 keep all 141 complete named-response states, 310 original configurations and 228 original named *physical* observations. The prior is uniform on the 141 states. Each complete legal adaptive physical-observer decision tree T has total observer usages U(T), usages N32(T) of original observer 32, usages N34(T) of original observer 34 over all 141 state paths. All observers except 32 and 34 cost t>0; observers 32,34 cost (1-a)t and (1-b)t, respectively. For any real a,b in [0,1/2], all prices remain positive.

Let F(a,b):=141 V(a,b)/t, where V is the minimum expected observation cost over **all** complete legal adaptive native decision trees. Write M=max(a,b), m=min(a,b). Then, throughout the full real parameter square:

\`\`\`text
F(a,b) =
 296-141*M-11*m       if 0 <= m <= 1/4,
 297-141*M-15*m       if 1/4 <= m <= 1/3,
 304-141*M-36*m       if 1/3 <= m <= 2/5,
 306-141*M-41*m       if 2/5 <= m <= 1/2.
\`\`\`

All boundary formulas agree. Exactly eight affine fixed-complete-tree **cost types** are both sufficient and necessary to cover the entire square optimally. They are:

| Witness | (U,N32,N34) | Max path depth | Zone where strictly optimal |
|---|---|---|---|
| L32 | (296,141,11) | 3 | m in (0,1/4), a>b |
| L34 | (296,11,141) | 3 | m in (0,1/4), b>a |
| H32 | (297,141,15) | 3 | m in (1/4,1/3), a>b |
| H34 | (297,15,141) | 3 | m in (1/4,1/3), b>a |
| M32 | (304,141,36) | 4 | m in (1/3,2/5), a>b |
| M34 | (304,36,141) | 4 | m in (1/3,2/5), b>a |
| N32 | (306,141,41) | 4 | m in (2/5,1/2), a>b |
| N34 | (306,41,141) | 4 | m in (2/5,1/2), b>a |

At equality boundaries several tree types may tie. Distinct open-region gradients show eight is the minimal number of different affine cost types. Each listed full original physical-query tree has been replayed against 141/141 original states, with no query repeated on a state path. The four new M/N witnesses use depth 4.

## Thirteen exact unrestricted Bellman vertices

The exact native integer Bellman oracles enumerate all 228 original physical observers (not a compressed response-equivalence menu); 13 distinct parameter vertices were calculated. Results below are F=141V/t, not rounded:

| (a,b) | F |
|---|---|
| (0,0) | 296 |
| (1/2,0), (0,1/2) | 451/2 |
| (1/4,1/4) | 258 |
| (1/2,1/4), (1/4,1/2) | 891/4 |
| (1/3,1/3) | 245 |
| (1/2,1/3), (1/3,1/2) | 443/2 |
| (2/5,2/5) | 1166/5 |
| (1/2,2/5), (2/5,1/2) | 2191/10 |
| (1/2,1/2) | 215 |

Each original state subset S uses the exact recurrence

\`D(S) = min_{q informative among 228} ( |S| c_q + sum_{C in Pi_q(S)} D(C) )\`, with singleton D=0, original complete named-response fibers \`Pi_q\`, integer-scaled rational prices. All informative splits have strictly smaller state subsets and all prices in this theorem are positive; the finite recurrence is exhaustive across legal complete trees. Two independent raw parsers reconstruct consistent original 228 response vectors, but the Bellman minimizer is one implementation, not claimed as two independent solvers.

First seven vertex outputs were rechecked in one runtime batch; after a long batch runtime stalled, remaining six were rechecked as **separate successful subprocess calls**. Both logs and the exact 13-point reconciliation are preserved, so the interrupted long batch is not represented as a complete run. Additionally full trees N32,N34 were extracted at (1/2,9/20) and (9/20,1/2) respectively.

## Proof over every real parameter, and minimality

For each fixed legal complete tree Q, normalized total cost is the affine function \`f_Q(a,b)=U_Q-a*N32_Q-b*N34_Q\`. Hence the all-tree infimum \`F=inf_Q f_Q\` is a concave function on [0,1/2]^2.

For each one of the four closed bands in \`m=min(a,b)\` defined by endpoints 0,1/4,1/3,2/5,1/2, split on \`a>=b\` versus \`b>=a\`. This partitions the square into **eight convex cells**: six quadrilaterals and two triangles. On each cell choose the corresponding one of L32,L34,H32,H34,M32,M34,N32,N34. Its affine cost equals the globally optimal Bellman value at *all vertices of its cell*, by the finite 13-point certificate above and exact full native tree replay. For any interior point x which is a convex combination of its cell's vertices v_i, concavity yields

\`F(x) >= sum_i lambda_i F(v_i)=sum_i lambda_i f_Q(v_i)=f_Q(x)\`.

The feasible complete tree Q gives the opposite inequality \`F(x)<=f_Q(x)\`. Equality holds throughout each convex cell, hence for all real (a,b) in the full square. This is a universal all-tree proof within the declared finite original native BRC instance, not a numerical fit.

Eight open regions of strict optimality have eight pairwise distinct gradients \`(-141,-11),(-11,-141),(-141,-15),(-15,-141),(-141,-36),(-36,-141),(-141,-41),(-41,-141)\`. Every fixed complete tree has one affine gradient; equality to F throughout any such open region forces gradient equality. Fewer than eight affine fixed-tree types cannot cover all eight open regions. The eight named witness trees attain the lower bound.

## Reproducibility, immutable sources, and frontier

Exact source SHA256:
- \`source/frozen_original_master.txt\` = \`cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e\`.
- \`source/EC49FPG_PROFILE.csv\` = \`a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f\`.

The exact finite machine certificate and eight full-tree JSON witnesses are delivered in the separate 23-file self-contained evidence archive \`EC49FRY_FULL_TWO_PRICE_HALF_SQUARE_COMPLETE_EVIDENCE_20261118.tar.xz\` (218096 bytes, SHA256 \`0e4c8cb084ce301bc84483959cda9709cce4dbc55e5f8079bf0073ec5002473c\`). The archive contains original frozen source input, the two parsing modules, complete original 228-physical-query Bellman solver, original and new witness trees, the replay verifier, 13-anchor exact readback logs, source hashes, and this proof. Its 23 constituent files were re-opened and checked against their SHA256 manifest. The complete GitHub-verifiable theorem, verifier and machine index are committed alongside this text.

**Next frontier:** classify \`a,b>1/2\`, especially the positive-price region \`[1/2,1)^2\`, retaining all physical observer identities, and then joint nonuniform priors/root prices. For the zero-price endpoint a=1 or b=1, restrict to informative queries to preserve the strict-state-decrease recurrence. Formal Source read-only control request \`r4-ec49frx-20261118-0127-task-lookup-01\` concluded \`SUCCEEDED/NO_CANONICAL_PUBLICATION_DIRECTORY\` at Source \`c17863d7c88e4d9653fc89644b3278d7c546a5f1\`; owner projection remains unverified; no CLAIM, Result, Review or Activity was created. No credentials included.