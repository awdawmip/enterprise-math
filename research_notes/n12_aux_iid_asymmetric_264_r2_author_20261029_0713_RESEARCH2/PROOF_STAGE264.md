# Stage264 — exact Bellman adjacency, portable author mathematical proof

Status: **AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED**. Research identity: local EM-RESEARCH2-STAGE264-20261029-0713, not a native Source session or CLAIM. Scientific reads: GLOBAL_KNOWLEDGE_V1 main@d659eb0978f58efec56ab3e3013e39de5538aff0, Enterprise Math main@5fa950a7d2f6e75cf091f5fd60e85dcf4a4a574a, Stage263 commit 211ede8a7e3baa82b41f092fb9a84e9644086a45, P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Read ACTIVE Heartbeat/X6 and residual-faithful joint-observer constraints. This is an EXTERNAL finite IID auxiliary model, not native P000 dynamics.

## 1. Statement

Let P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), N=12, alphabet {0,1,2}. Policies may stop/declare P or Q or continue (when fewer than 12 observations), randomized on arbitrary complete ordered histories. Four observers are eP=Pr_P(wrong Q), eQ=Pr_Q(wrong P), tP=E_P(stop time), tQ=E_Q(stop time). At real caps (a,b), V12(a,b) is the minimum max(tP,tQ) subject to eP≤a,eQ≤b.

**Theorem 264A.** For a=595553513081/6449725440000 and b=2918481415/3869835264, V12(a,b)=16927184206983443/3094860441600000 ≈ 5.46944992396243.

**Theorem 264B (all real iff).** LambdaP=1357504/15355, lambdaQ=859212/15355, H=14999620027/268651080. Define four exact four-observer vectors (eP,eQ,tP,tQ):
- G5: (668435839/7739670528,2229900905/2902376448,1450753471/322486272,1259213767/241864704).
- H5: (3750849409/46438023168,13498546055/17414258688,8819755201/1934917632,7717391977/1451188224).
- H6: (1420974803/15479341056,4343298685/5804752896,3244810067/644972544,2829330659/483729408).
- G6: (1524881053/15479341056,4295642435/5804752896,3198716317/644972544,2764486909/483729408).

Write pi for projection onto (eP,eQ), R264=conv{pi(G5),pi(H5),pi(H6),pi(G6)}. For EVERY REAL (a,b) in [0,1]^2:
V12(a,b)=H−lambdaP*a−lambdaQ*b **if and only if** (a,b) lies in R264.
R264 is a strictly convex quadrilateral of exact area 206182861328125/2495937495082991616. It and the prior Stage263 region R263 meet in their entire common G5–G6 edge and have disjoint interiors.

## 2. Global Bellman bound (exact)

For an ordered word with count s=(i,j,k), r(s)=Q(word)/P(word)=(2/3)^i*2^j. Since every P word has positive probability, normalize the dual remaining cost by the P probability of the particular word. For |s|=12 set D(s)=min{lambdaQ*r(s),lambdaP}; for |s|<12 use
D(s)=min{lambdaQ*r(s) [declare P], lambdaP [declare Q], r(s)+Σ_z P(z)*D(s+unit_z) [continue]}.
Exact Fraction backward induction covers 455 states and 1274 actions. Root D(0,0,0)=H. Precisely 817 nonminimal actions have strictly positive gaps; minimum 250/27639. There are exactly two ties, at (0,0,5): P/continue, and (0,1,8): Q/continue.

For all arbitrary complete-history randomized policies, tQ+lambdaP*eP+lambdaQ*eQ≥H, because each history costs at least its Bellman minimum. With max(tP,tQ)≥tQ and both multipliers strictly positive, the bound V12(a,b)≥H−lambdaP*a−lambdaQ*b holds for all feasible error caps.

## 3. Source-faithful four-observer sufficiency

At any count state sum the P mass of all *ordered* histories arriving there and taking each action. Because the Q/P ratio r(s) depends only on the count, replacing history-dependent action probabilities with their conditional P-mass weighted average at that state preserves both sources' aggregated action masses, future transition masses and all four declared observers by induction on time. No ordered-path multiplicity is erased from those positive sums. This is an exact finite-horizon four-observer Markovization theorem, not a general provenance collapse, native X6 equivalence or new world axiom.

Equality in Bellman requires every reached action be minimizing. Only the two tie states can vary. Time strictly increases at every continuation, hence each count state occurs at most once on a path. Pre-sample independent Bernoulli actions at those two states: every randomized Markov equality policy is a convex mixture of the four deterministic tie policies. Thus every equality four-observer vector is in conv{G5,H5,H6,G6}; every convex combination is achievable. All four have tQ>tP and tQ+lambdaP*eP+lambdaQ*eQ=H.

The executable Fraction certificate computes those policies via count-state P/Q rational mass propagation and separately by an **unmerged** full ordered-history P/Q DFS: 616+661+664+718=2659 nodes, 411+441+443+479=1774 terminal branches. P and Q terminal masses both equal exactly 1 in each policy. Four observer values agree under both algorithms. No finite floating fit is used for the theorem.

## 4. Matching primal and whole-region iff

Choose at the root G5,H5,G6 with strictly positive weights
(16990664034839/37487792968750,705855264768/18743896484375,30536669447/59980468750).
Their exact sum is one. Their mixed observer vector is
(a264,b264,19540937843174179/4126480588800000,16927184206983443/3094860441600000).
Here tQ−tP=591724083257/806215680000>0. Exact substitution gives H−lambdaP*a264−lambdaQ*b264=tQ=max(tP,tQ), proving Theorem 264A.

Every (a,b)∈R264 is realized as the exact error pair by a convex mixture of all four policies. Such a mixture has tQ>tP and Bellman equality, so it attains the global lower bound. Conversely, equality at an arbitrary (a,b) requires both errors to equal their caps (positive lambdas), and all realized actions to satisfy Bellman equality; the sufficient-state theorem puts its error pair into the exact four-vertex hull. This proves the all-real iff.

Consecutive signed turns of (G5,H5,H6,G6) equal (93719482421875/1247968747541495808,18743896484375/207994791256915968,18743896484375/207994791256915968,93719482421875/1247968747541495808), all positive. The shoelace formula gives the exact area above. Both new H vertices lie strictly on the negative side of oriented G5→G6, whereas Stage263 F5 and F6 lie on the positive side. Both regions are convex, share G5,G6 exactly, and intersect only along that complete edge. At this target orient(G5,G6,(a264,b264))=−262655/92876046336, strictly outside R263.

## 5. Evidence and next result

Actually executed independently constructed exact stdlib program STAGE264_EXACT_FACE.py; stdout in STAGE264_EXECUTED_STDOUT.txt ends STAGE264_EXACT_ALL_REAL_FACE_PASS. The full author working source (with extra four-vector assertions) had local SHA256 b6c72ff894ccd0a71b75ddbabcc28455ae30559af35767cd4a2837bc8d830bb3; the compact posted certificate was also executed locally and yields the included stdout. SciPy HiGHS floats were candidate-discovery ONLY.

BRC resolution: REUSE_APPLIED — positive Q-rational P/Q labeled branch masses and explicit four-observer conditional sufficiency; no signed cancellation, unbounded inference, or X6 physical transfer. Original native status: research_authority_granted=false and live Owner query CONTROL_QUOTA; formal CLAIM, Source Result, independent Driver review, activity checkpoint binding and mathematical admission require their separately authorized routes. Activity registration remains REGISTER_PENDING, not invented as succeeded.

**Stage265 target:** across H5–H6 take (a,b)=(2501401941677/29023764480000,13264221055/17414258688), with exact orient(H5,H6,target)=−46865/17414258688. Exploratory float LP indicates V≈5.592547390568753 and possible lambdas 6216128/68615,3900924/68615 (UNPROVED). Next certify exact dual/primal, full-real neighboring region and ordered-path counts.
