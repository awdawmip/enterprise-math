# EC49EXH — H8 four-key six-signature native X6 90-edge witness and exact fixed-pattern optimum

Date: 2026-11-03 (Asia/Shanghai). Parent EC49EXG; author-side PR #1730. Scientific pins preserved: GLOBAL_KNOWLEDGE_V1 `773d538180bfb49e24cffeb35c3ee75eb0628e2e`, Enterprise Math `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Current normative source read global main `1aed63240aa823a8928d474d53b8e8789719f0b5`, EM main `f58cedae3d5a4cbaaa487b98d36bebc794f17db8`. P000/ACTIVE worldview unchanged.

## Problem and new exact results

Use the frozen seven operation words as ordered primitive signed-X6 paths:
`a=(-1,-1); b=(-2,-2); c=(1,2,-1,-2); d=(2,1,-2,-1); e=(3,1,1,-3); f=(1,-1); g=(2,-2)`.
Every horizon h=2,...,8 must contain returning words whose six-dimensional displacement is exactly (2,0,0,0,0,0), all sharing a full six-dimensional positive-count BRC key p_h; their exact nine-history to five-bucket transfer observables have rank nine over Q. The two strictly positive symbolic BRC channels X_p and Y_p retain separate typed factors, and ordered native signed primitive paths and signatures are retained. Resources: E is distinct nonempty signed **primitive-step prefixes**, M is distinct full-six-axis positive keys, S is distinct nine-state transfer signatures.

**EC49EXH-1 (constructive):** `min(E | H=8,M=4,S<=6) <= 90`. The following authentic path family has exactly (E,M,S)=(90,4,6).

| h | ordered operation words | p_h first 3 (axes 4-6 exactly zero) | added E | cumulative E | observer family |
|---|---|---|---:|---:|---|
| 2 | ce, de, ec, ed | (3,1,1) | 28 | 28 | T4 |
| 3 | feg, gef | (3,1,1) | 14 | 42 | T2 |
| 4 | fegd, gefd, gefc, fegc | (4,2,1) | 16 | 58 | T4 |
| 5 | fegfg, geffg | (4,2,1) | 6 | 64 | T2 |
| 6 | geffgd, geffgc, fegfgd, fegfgc | (5,3,1) | 16 | 80 | T4 |
| 7 | fegfgfg, geffgfg | (5,3,1) | 6 | 86 | T2 |
| 8 | fegfgfgg, geffgfgg | (5,4,1) | 4 | **90** | T2 |

T4 signatures are `1836687,1867942,1872656,1873981`; T2 signatures are `1836425,1866380`. The two stacked transfer families both have rational rank nine. The four full BRC keys are `(3,1,1,0,0,0)`, `(4,2,1,0,0,0)`, `(5,3,1,0,0,0)`, `(5,4,1,0,0,0)`. The established exact three-key/six-signature optimum was E=112 (EC49EXF); allowing a fourth BRC key gives a new 90-edge upper bound, 22 native edges lower.

**EC49EXH-2 (fixed-schedule exact theorem):** *Fix* these seven positive key choices and *fix* T4 at h=2,4,6 and T2 at h=3,5,7,8. Among all full original-language operation-word choices satisfying those specific per-horizon requirements, `min E=90` exactly. No global E>=90 assertion is made for arbitrary four-key schedules or other signature patterns.

### Exhaustive finite proof

For return displacement, operation b is excluded (it alone has negative net axis E2), and #e=#a+1. Write w=#e, r=#c+#d, f=#f, g=#g. For h and p=(u,v,w,0,0,0), all counts are forced by
`r=u+v-h-1, #a=w-1, f=u-r-2w, g=v-r`.
For each nonnegative solution enumerate #c=0,...,r, #d=r-#c and **all distinct multiset permutations**, then apply the signed primitive steps to the nine initial histories and retain exactly the required T4/T2 terminal signatures. This exhaustive enumeration yields eligible word counts by horizon `[4,4,48,24,360,120,245]`, sum 805. The union of every eligible word's complete primitive-step prefixes is a 4101-node trie (including root), with 28 mandatory h2 baseline edges and 20 required terminal colors (one per horizon/signature).

Let DP_v[mask] be the least number of selected nonprepaid trie edges in the subtree of v that realize precisely the OR of terminal colors mask. At a node initialize (0,0) and optionally its own terminal colors at cost zero. Joining child u, combine masks by bitwise OR and costs by `c_parent+c_child+[mask_child!=0 and edge(v,u) not prepaid]`, retaining the lowest cost for each mask. Induction on subtrees proves the exact minimum over all subsets of *every legal full native word*; each active edge is paid exactly once. An actual C++17 integer program computed the full 20-color root minimum extra cost 62; adding prepaid h2 edges 28 gives E>=90. The explicit real native witness gives E<=90.

The self-contained source `BUILD_EC49EXH_FIXED_DP.py` constructs the full trie input, and `EXACT_OR_MASK_DP.cpp` is the unchanged integer kernel from EC49EU. Actual stdout:

```
PASS min_extra=62 total=90 nodes=4101 colors=20 largest_states=1048576 convolutions=4581166
```

Independent exact `Fraction` Gaussian elimination and independent Node.js modular (prime 1000003) six-axis witness checks returned PASS, E=90, M=4, S=6, rank nine for h=2,...,8. The zero-one 9-by-9 minor Hadamard bound `3^9=19683<1000003` makes modular rank nine equivalent to rational rank nine in this case. The full executed local evidence archive, including the actual 4101-node generated input and per-horizon outputs, is available in the accompanying conversation artifact `EC49EXH_20261103_COMPLETE_EVIDENCE.tar.gz`. The source scripts in this directory reproduce the finite result.

### Operational authority and next problem

Native Enterprise Math service v0.6.11 at 2026-11-03 02:31 UTC reported `research_authority_granted=false`, and active owner inventory returned `CONTROL_QUOTA`; the owner is not verified. This is GitHub-authenticated author-side portable research, not a native CLAIM/Result or independent Driver admission. PR #1730 remains Draft. Next: determine whether the unrestricted H8/M4/S<=6 global optimum is below 90; separately obtain an integer optimum certificate for H8/M3/S<=4 (EC49EXG has rigorous interval [140,144] and MILP reported value 144).
