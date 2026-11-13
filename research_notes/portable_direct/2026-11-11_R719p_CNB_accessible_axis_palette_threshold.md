# R719P — Exact accessible-axis palette threshold for cyclic non-backtracking X6/BRC holonomy

Date: 2026-11-11 (Asia/Shanghai). Line: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`. Author-side independent mathematical research; not an admitted native Result/Review.

## Scientific sources and carrier

Keep the immutable P000 V5 science pin `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`. Use the separately sourced V17 shared-axis slot transport, blob `42b810a8f82c504833027da17884cc4fb2943e5b` from source `696c2e3d698105447b77c64ecee631b91e052dcc`, and the R718 CNB branch definition and verification, author source commit `9aa9bdd937a5d975762a807ae0eb6e938835ceb1`. V29 network event grammar is later candidate research (blob `6849ebd3fc776fb7da3b46627376490aba3dad99`); its directed Link/Port permissions are instantiated by a particular network, rather than universally fixed by that file.

Define a ROOTED, ordered, positive-count BRC carrier as all closed active-triad words `S=T_0,T_1,...,T_m=S` for `S={0,1,2}`, with consecutive distinct triads intersecting in two axes. The cyclic non-backtracking (CNB) condition is `T_{i-1} != T_{i+1}` modulo m, including the seam at S. Each transition retains the two shared axes in their three slots and puts the entering axis into the departing axis's slot; the final ordered frame at S is an element `h(W) in S_3`. Histograms count distinct ordered triad words, with each BRC branch having positive integer weight one. The observer is final based V17 holonomy at a fixed length m; its allowable future composition is the same slot transport. Do not quotient branch provenance or confuse a palette restriction with a native Cell-address restriction.

Let `P_q={0,1,2,...,2+q}`, `q in {0,1,2,3}`, be the *globally accessible axis palette*. Every active triad in the word must be a subset of P_q. This is an explicitly defined axis-availability / conditional port-admission experiment; native V29 alone does not instantiate such a palette as an automatic Link/Port permission.

## Theorem A: a single accessible spare axis leaves an exact parity residue

For `q=1` the active-triad graph `J(4,3)` is K4. A transition replaces a present axis by the *unique* missing axis. Adjoin the missing axis as a fourth ordered slot to the transported active frame. **Each transition is exactly one transposition of these four slots**, exchanging the departing axis with the missing axis. On return to S the fourth slot again contains axis 3, so the parity of the final S3 holonomy is

`sgn(h(W))=(-1)^m`.

Thus a fixed-length CNB observer on a globally four-axis palette sees at most three of the six S3 elements. This is a universal parity theorem (not a finite extrapolation). In particular, the full six-state cover of R718 cannot occur at a fixed m with only one accessible external axis.

Stronger, for q=1: at length 3 precisely all three transpositions appear; at length 4 precisely the two nonidentity 3-cycles appear; at length 5 there are no CNB rooted closed walks; for every **even m >= 6** precisely all three even elements appear, and for every **odd m >= 7** precisely all three odd elements appear.

Proof of unbounded support: the exact finite base cases m=6,8,10 have all three even elements; m=3,7,11 have all three odd elements. Every legal CNB word W can be extended by six steps while keeping its holonomy: let p be the axis of S missing at T_(m-1), and f the axis of S missing at T_1. Choose distinct a,b in S such that a != p and b != f; such a pair always exists. With the unique spare axis x=3, form the triangle `C_ab: S -> S-a+x -> S-b+x -> S` and append `C_ab C_ab`. The triangle swaps the slots containing axes a,b; two copies compose to identity. All internal turns and three seam conditions remain CNB since a!=b, a!=p, b!=f. The original W is a preserved prefix, giving an injection `N_{m+6}(h) >= N_m(h)`. Together with parity, the six residues modulo 6 represented by the cited finite bases give exactly the stated support. The m=5 empty case and the base supports are certified by the executable exact dynamic programming and an independent literal exhaustive DFS where applicable.

Therefore for q=1 and m even >=6 or m odd >=7 the exact **final-holonomy** repair cardinality is three, or `ceil(log2 3)=2` fixed binary bits. For m=4 it is two (1 bit); for m=5 there is no admissible branch. Information quantities are observer- and fixed-length-specific.

## Theorem B: two spare axes already recover all six states at every length m>=4

For q=2 (only five of the six native axes accessible), exhaustive exact small cases m=4,5,6 show *all six* S3 holonomies are reachable. Here is a complete six-witness set at m=4, indexed by final ordered frame (slashes separate successive active triads):
- `012`: `012/013/034/024/012`
- `021`: `012/013/014/024/012`
- `102`: `012/023/024/124/012`
- `120`: `012/013/023/123/012`
- `201`: `012/013/123/023/012`
- `210`: `012/013/014/124/012`

For any legal rooted CNB word W, choose `a in S` different from the missing root axis at its first and last neighbors (at most two forbidden a). Choose the two distinct accessible spare axes x=3, y=4. Append the triangle `S -> S-a+x -> S-a+y -> S`. It changes only one slot, temporarily to x and then y, before restoring a; its V17 holonomy is **identity**, and the CNB seams remain legal because a avoids both forbidden axes. Hence for every h, `N_{m+3}(h)>=N_m(h)`. The base six-state supports at m=4,5,6 propagate to every integer m>=4. Enlarging the palette to all six axes preserves those witnesses.

**Exact threshold** (within this declared global palette restriction): q=0 admits no positive-length Johnson-adjacent return; q=1 gives the parity-limited result; q>=2 admits all S3 values for every m>=4. Thus the minimum globally accessible native-axis count supporting the *full fixed-length six-state CNB holonomy cover for every m>=4* is **5**, i.e. precisely **two spare axes** outside the rooted active triad. The full six-state repair for the declared final-holonomy observer requires `ceil(log2 6)=3` bits at m>=4.

## Independent integer verification

File: `R719P_CNB_AXIS_PALETTE_VERIFY.js`; output: `R719P_CNB_AXIS_PALETTE_RESULTS.json`. Exact BigInt lifted-state dynamic programming tracks (previous triad, current triad, ordered frame, first neighbor) and counts all CNB branches; an independent literal depth-first complete path enumeration checks q=1 at m=3..8 and q=2/q=3 at m=3..6. Additional BigInt checks: q=1 m=3..17 obeys parity; q=1 support classification on m=6..17; q=2 all six m=4..12; q=3 exactly reproduces R718 m=3..6.

Selected counts (columns order: identity, each transposition, each 3-cycle): q=1 m=3 (0,2,0), m=4 (0,0,3), m=5 (0,0,0), m=6 (6,0,9), m=7 (0,14,0), m=8 (36,0,3); q=2 m=4 (12,16,6), m=5 (60,40,66), m=6 (270,248,324). Every finite count is exact nonnegative integer BRC path mass, not a signed cancellation.

Proof validity is by the permutation parity and explicit identity-cycle extension arguments, with exact complete small-base checks; infinite support is not inferred solely from finite tables. This is author-side evidence and is pending independent mathematical Review.

## Native-interface follow-up

Read actual deployed Link/Port declarations/permission instances and dependent-event constraints. Translate permitted active-triad moves into an exact labelled subgraph of J(6,3), retaining the V17 frame and V29 event ordering. Determine if it contains the rooted five-axis CNB witness family (sufficient) or only a globally four-axis palette (parity obstruction), then run the general constrained lifted automaton. A five-axis *palette* is not sufficient if its allowed directed transitions omit required witnesses. The actual V29 primitive event grammar alone does not supply that instance-specific directed graph.

BRC resolution: `COMPOSE_APPLIED` (R718 positive branch/path carrier with exact restricted-axis filter) and `REUSE_APPLIED` (V17 slot transport); preserve branch identity, multiplicity, order and frame until observer-safe quotient.
