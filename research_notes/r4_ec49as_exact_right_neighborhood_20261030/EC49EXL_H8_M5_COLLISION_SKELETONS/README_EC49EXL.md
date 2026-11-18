# EC49EXL — exact five-BRC-key collision skeletons for native X6 H8 (2026-11-03)

**Evidence status:** AUTHOR FINITE ENUMERATION / EXACT Q-RANK / INDEPENDENT HALL COUNT / UNREVIEWED / NOT ADMITTED.

## Frozen inputs and scope

Parent: EC49EXK, immutable author checkpoint \`7c61e357d28e4b81912b6cac38b96f2ff5427b16\`; frozen scientific pins: global \`773d538180bfb49e24cffeb35c3ee75eb0628e2e\`, Enterprise Math \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`. Current canonical-main behavioral policy is a separate overlay. P000 and the ACTIVE Heartbeat worldview remain unchanged.

The finite model is seven **native signed six-axis operation codes**
\`a=(-1,-1), b=(-2,-2), c=(1,2,-1,-2), d=(2,1,-2,-1), e=(3,1,1,-3), f=(1,-1), g=(2,-2)\`;
at horizons \`h=2,...,8\`, each operation word must return X6 displacement \`(2,0,0,0,0,0)\`. Each horizon's chosen words share one **complete six-axis positive symbolic BRC key**; its 9-history by 5-bucket transfer/incidence matrix has Q-rank 9. Exactly 5 distinct keys are used globally, and at most 6 distinct observation signatures. Ordered primitive paths and positive BRC multiplicities remain separate objects.

## Proposition A: complete finite rank-key criterion for h=2,...,8

If \`a,b,c,d,e,f,g\` denote operation multiplicities, X6 return forces \`b=0\` and \`e=a+1\`. Writing \`r=c+d\` gives \`h=2a+1+r+f+g\`. All such nonnegative integer tuples give returning primitive words upon permutation. Their full positive BRC keys are

\`(u,v,w,0,0,0)=(r+2(a+1)+f,r+g,a+1,0,0,0)\`.

Solving the counts in terms of the key:

\`r=u+v-h-1; a=w-1; f=h+1-v-2w; g=h+1-u\`.

For each h in the specified *finite* range and each legal key, the exact rank-9 property holds **iff** either:

* \`r>=1\`, with the four available signatures \`T4=(1836687,1867942,1872656,1873981)\`, which already span rank 9; or
* \`r=0, f>=1, g>=1\`, with signatures \`T2=(1836425,1866380)\`, which span rank 9.

The executed Python checker enumerates **all 411,368 legal returning words** at horizons 2,...,8, expands every signed primitive operation in order, computes the exact nine-history A/B transfer signature and performs exact rational row reduction over the whole fiber. It checks the iff criterion *for every full key*. This is a finite statement; no all-H extension is claimed.

| h | Returning words | Legal keys | Rank-9 keys | T2 keys | T4 keys |
|---|---:|---:|---:|---:|---:|
| 2 | 8 | 3 | 1 | 0 | 1 |
| 3 | 51 | 7 | 4 | 1 | 3 |
| 4 | 304 | 13 | 9 | 2 | 7 |
| 5 | 1,770 | 22 | 17 | 4 | 13 |
| 6 | 10,224 | 34 | 28 | 6 | 22 |
| 7 | 58,947 | 50 | 43 | 9 | 34 |
| 8 | 340,064 | 70 | 62 | 12 | 50 |

## Theorem B: exactly 40 of 140 five-key collision skeletons are realizable

A collision skeleton is a set partition of the **seven labelled horizons** \`{2,3,4,5,6,7,8}\` into five nonempty equality blocks; equal-block horizons share a complete BRC key, and distinct blocks have distinct keys. Exactly \`S(7,5)=140\` partitions exist.

For a block B, intersect the rank-9 eligible key sets at its horizons: \`K(B)=intersection(h in B, K_h)\`. The skeleton is realizable iff the five \`K(B)\` admit **five distinct representatives**. Necessity follows from the keys; sufficiency follows by using the corresponding T2 or T4 full-rank word witnesses at each horizon. Their combined observation signatures lie in the **same six-element** T2 union T4, so S<=6. Each witness preserves actual signed primitive ordering; no quota-only or count-only quotient is used as a final path.

An exact restricted-growth enumeration and integer bipartite matching certifies **40 realizable skeletons, 100 excluded**, among the 40: **32 consist of two repeated pairs, 8 consist of one repeated triple** (others singletons). Under local type choices T2/T4 with h2 forced to T4, **60/64** type profiles are possible; four profiles are impossible (the complete profiles are in the JSON evidence).

Independently, \`VERIFY_EC49EXL_INDEPENDENT.js\` generates all rank-eligible keys directly from the displayed integer equations (without replaying Python word enumeration), and verifies the five distinct-representative condition by **all 31 nonempty Hall subset inequalities**, yielding the same \`140/40/100/32/8/60\` counts.

A corollary: the h2 unique eligible key is \`(3,1,1,0,0,0)\`, which can coincide only with the h3 key, not with h4,...,h8.

## Reproduction and current frontier

Run \`python3 VERIFY_EC49EXL.py > EC49EXL_REGENERATED.json\` and \`node VERIFY_EC49EXL_INDEPENDENT.js > EC49EXL_INDEPENDENT_REGENERATED.json\` (standard-library Python and Node; all arithmetic integer/rational). \`EC49EXL_EXECUTED_SUMMARY.json\` records the executed outputs and all 40 realizable partition skeletons; local full raw audit also contains the 411,368-word run. This is exact finite computational proof at the declared model and range, with no external physical interpretation.

EC49EXK's **80-edge valid witness** and previously established **63<=E*<=80** bound for global H8/M5/S<=6 remain unchanged. This result classifies only BRC key **equality shapes**, *not* their best union-of-ordered-primitive-prefix cost. There may be feasible skeletons whose minimum E>80; computing them remains open.

Current service status: \`research_authority_granted=false\`; an actual Owner task query returned \`CONTROL_QUOTA\` (5/5). GitHub author-side preservation is **not** canonical CLAIM/Result/Driver review.

**Next EC49EXM:** run exact ordered-prefix OR-mask search first on 8 triple-collision skeletons, then on 32 double-pair skeletons, seeking E<80 witnesses or a certified lower bound over *all 40*. Preserve each full six-axis BRC key, complete signatures, native order and actual X6 return.