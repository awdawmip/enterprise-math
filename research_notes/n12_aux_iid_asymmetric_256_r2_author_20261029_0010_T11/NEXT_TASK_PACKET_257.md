# Stage257 — Maximal N=12 asymmetric Bellman contact face and TV adjacency

Status: NEXT_AUTHOR_TASK, not an admitted Source Task/CLAIM/Result. Scientific parent: Stage255 exact TV face, immutable commit 6c399579c9e744aa9be5eb519aa059d2ffbd1618; Stage256 now solves a distinct non-TV rational cap pair and proves a positive-area all-real affine subregion in the same Draft PR #1571.

## Frozen model and exact inputs

P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), N=12; arbitrary fully ordered-history randomized sequential stop/declare policy, four observers eP,eQ,tP,tQ, minimize max(tP,tQ) under separate caps.

Stage256 exact dual: thetaP=0, thetaQ=1,
Kp=644972544/8007455, Kq=418575732/8007455,
root H=30134718329/576536760. It has 455 count states, 11 Bellman ties: P/C at (0,0,k) for k=2,...,11, and Q/C at (0,1,2); 808 strictly positive alternative-action gaps.

Exact newly solved cap pair a=6788660051/34828517376, b=572868317/967458816 yields V12=3625356966401597/645573577789440. It is strictly outside the Stage255 TV region since 2a+b<1. A lawful two-coin policy at A=(0,0,8) and B=(0,1,2) attains this value, with x=2942214371765387/4197658050781250 and y=478956919/600559125. Its error projection is an invertible parallelogram of exact nonzero area 52470725634765625/202170937101722320896, and the same exact dual attains all real caps inside. This is not proven maximal.

## Next precise question

Determine the FULL maximal primal-contact error polygon or polytope for the Stage256 support, rather than restricting to the two selected randomizations. Explicitly handle dependencies among the pure all-2 tie states and the B tie. For example, stopping at k=2 on the pure-2 path can prevent some histories from reaching B, so 11 randomizations do not automatically give a simple independent product of affine terms.

Enumerate the 2^11=2048 possible deterministic tie action assignments with rational source mass and four observers, or prove a smaller exact convex hull recursion with complete coverage. Determine which error-plane points can be attained by a maximizing-time strategy with tQ>=tP; time Q does not follow solely from an error-plane projection. Give maximal exact vertices and edges and prove all-real iff contact if justified. Identify whether this support touches the Stage255 TV affine contact region directly or if other supports intervene. A new cap point or rational no-go with dual certificate should accompany the geometry.

## Acceptance and authority

Exact rational proof/certificate with complete finite tie domain, all four observables and guaranteed source labels; independent unmerged ordered P/Q mass DFS for at least a new vertex or sufficient exact algebraic alternative. No floating-only universal assertion; no silent global extrapolation from the author-side two-coin subregion. Preserve P000 ACTIVE six-native-X6, three-dimensional-slice and separately typed time semantics as an unchanged internal starting frame, no asserted physical transfer.

Inputs: Enterprise Math Draft PR #1571, research_notes/n12_aux_iid_asymmetric_256_r2_author_20261029_0010_T11/{PROOF_STAGE256.md,STAGE256_ASYMMETRIC_EXACT.py,EXACT_RUN_STAGE256.txt}. Global read pin main@243041d5d4e2c6bc8b78be63668669b0f1d26dce; Enterprise Math main@bc0a149e03ba2632a8ba79042361b50ad3ab471a; P000 original Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. Native owner was unconfirmed (CONTROL_QUOTA), status research_authority_granted=false and CODE_REVIEW_REQUIRED. Output remains AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED until separately authorized Source lifecycle and independent Driver review.
