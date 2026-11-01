# EC49DI — Affine-collinear BRC weights: an exact rank defect and sharp delayed saturation

**Date:** 2026-11-01. **Status:** AUTHOR_ANALYTIC_PROOF / EXACT_NATIVE_X6_FINITE_AUDIT_PASS / PORTABLE_DRAFT / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED. No claim of independent Driver review or admitted theorem.

## Source and authority pins

Verified frozen GLOBAL_KNOWLEDGE_V1 main `f383e0c92a4a001a76c01505b8fc6fd87e48120f`; Enterprise Math main `f3473b69221a29e7021ee1503b92765fe9936a7c`. Read normative entrances, P000, ACTIVE worldview and native joint-observer constraints, BRC priorities and portable research protocol. Predecessor EC49DH is PR #1730 commit `7d7cc8b2f5cda0cfcfdbc6baee233f46f58877a2`. Gateway 0.6.11 reports research_authority_granted=false, executor_binding_configured=false, UPSTREAM_CODE_REVIEW_REQUIRED, quota 5/5; owner inventory returned CONTROL_QUOTA. No CLAIM, Result or independent review. P000 and protected worldview unchanged.

## Typed native six-axis model

Primitive prefixes are ordered signed steps `±E1,...,±E6`, fixed even length n and endpoint `D=(2s,2v,0,0,0,0)`, where v>=0, |s|+v<=h. Returning futures comprise exactly h or 1..h **whole** operations: a=(-1,-1), b=(-2,-2), c=(1,2,-1,-2), d=(2,1,-2,-1), e=(3,1,1,-3). Observe the final joint adjacent-subword tags A=(+1,+2), B=(+2,+1) on the **whole concatenated prefix and suffix**, including the seam. Independently read positive integer/rational BRC products W_x, W_y and unweighted count for each future word and final tag. Negative primitive weights are one. We do NOT treat positive BRC mass as signed amplitude or use a lower-dimensional native plane.

Take strictly positive `x_j`, `a,b>0`, affine-collinear `y_j=a*x_j+b`, and specifically `x_1=x_2=c`, with at least one `q>=3` satisfying `x_q=d!=c`. Rational weights give Q-ranks and positive real weights give R-ranks.

## Theorem A: exact extreme-return-fiber staircase for every h>=1

Fix `D=(-2h,0,0,0,0,0)` and `n=2h+2m`, m>=0. Its **only** complete returning suffix in both future languages is `e^h`, since only e has maximal positive E1 displacement per whole operation (+2), and the suffix is A/B-safe across the seam. The total positive primitive count is exactly m.

Let labels tau be none, A only, B only, both. Minimum positive letters are respectively `L_tau=(0,2,2,3)`. Their exact rank contributions are

```
r_tau(m)= 0 if m<L_tau, else min(3,m-L_tau+1).
R(m) = sum_tau r_tau(m).
```

Consequently `R(0..5)=[1,2,5,8,11,12]`, and `R(m)=12` for m>=5. In particular **R(4)=11 at n=2h+8**: a genuine rank defect of one, not merely a failed selected certificate. Its first 12-dimensional length is **2h+10**.

**Proof (upper).** The signed length/endpoint identity gives exactly m positives. Each tag needs L_tau positive letters. When m=L_tau, all mandatory positive letters lie in E1/E2, both with x=c and y=ac+b, so the tag's (Wx,Wy,1) vector has rank at most one. When m=L_tau+1, at most one exceptional positive letter has any different weight, and all triples lie on the affine line `(X0*x_j,Y0*(a*x_j+b),1)`, hence have rank <=2. For the both tag, disjoint A and B pairs using four positives also have only E1/E2 weights, so they cannot escape this line. Three is the universal three-channel upper bound.

**Proof (constructive lower).** Set `G_j=(+Ej,-Ej)`. For the four tags use cores `()`, `(1,2)`, `(2,1)`, `(1,2,1)`. For each tag core length L and `g=m-L>=0`, and `t=0,...,g`, prepend `G_1^t G_q^(g-t)`, then append negative-only compensating steps `(-E1)^(2h + positive E1 count of core) (-E2)^(positive E2 count of core)`. Every constructed prefix is an **actual signed-six-axis primitive word** with correct length, exact six-dimensional endpoint and joint tag, with no new seam. After e^h, its weight rows have factors `(X0*c^t*d^(g-t), Y0*(ac+b)^t*(ad+b)^(g-t), 1)`. At g=0 their rank is one; at g=1 two distinct rows have rank two. At g>=2 choose t=0,1,2; after removing nonzero common factors the determinant is

```
det [[d^2,(ad+b)^2,1],
     [c*d,(ac+b)*(ad+b),1],
     [c^2,(ac+b)^2,1]]
   = -a*b*(c-d)^3 != 0.
```

For g>2 factors `d^(g-2)` and `(ad+b)^(g-2)` are nonzero. Different tags occupy disjoint observed output columns; sum their ranks. This proves the exact staircase **for all h,m**, not by finite extrapolation.

## Theorem B: two-gate tensorization, full all-fibre rank at n=2h+10

Suppose the unweighted final-tag future observer on native prefixes of length n0 and a fixed return fibre/language has rank r, with r witness prefixes `p_j`. For each p_j prepend the three **ordered primitive gate pairs** `G_q G_q`, `G_1 G_q`, `G_1 G_1` (four native steps); endpoint, future responses and all A/B tags—including seams—stay unchanged. Each resulting three-row block has channel coefficient matrix exactly the invertible matrix above. Its inverse isolates the three disjoint x, y and count response channels: `W_x(p_j) diag(W_x(u)) T(p_j)`, `W_y(p_j) diag(W_y(u)) T(p_j)`, and `T(p_j)`. All positive weights and suffix diagonals are invertible, so their spans have dimension r each. Thus the 3r constructed rows reach rank **3r**, which is the universal upper bound by channel-wise factorization through the unweighted tag response space.

The predecessor **EC49DE author-side six-feature/basis proof** constructs r independent unweighted prefixes at n0=2h+6 for all h>=2 and all returning fibres. Its A/B history representation uses four tag flags and the two seam-sensitive `A absent & last +E1`, `B absent & last +E2` flags. Complete operations end in negative letters and have no additional unrepresented seam state. Exact-h suffix counts obey `N_b=v, N_e-N_a=-s`, `h=|s|+v+2t+N_c+N_d`; the resulting unweighted ranks are r=4 on boundary delta=h-|s|-v=0, r=5 on positive odd delta in exact mode, r=6 on positive even delta in exact mode, and r=6 on all positive delta in cumulative mode. For delta>0, a tag-free length-2h base plus six signed six-step zero-endpoint motifs at length 2h+6 yield a six-feature unimodular basis (det=-1); on mixed positive boundary four explicitly tag-distinguishing prefixes suffice. The native explicit bases and motifs appear in EC49DE_TAG_EARLIEST.md and are rebuilt by the verifier here. This predecessor is **author-side unreviewed**, not an admitted theorem.

Consequently at n=2h+10 the exact and cumulative future three-channel observer reaches its formal maximum on *every* fibre. Theorem A independently proves genuine failure at n=2h+8 on the extreme fibre, and shorter lengths also fail. Therefore, **conditional only on the EC49DE author-side full unweighted tag basis**,

```
n_sat(h) = 2h+10 for every integer h>=2
dim O_exact(h) = 3(11h²+15h+8)/2
dim O_cumulative(h) = 18h²+24h+12.
```

The dimensions are ranks of finite-future positive-BRC additive observations, NOT spatial dimensions or physical claims.

## Precise classification scope, and still-open case

- If all x_j are equal, y_j are also equal. On fixed length/endpoint the x/y masses are scalar count multiples; rank is only r, and earlier unweighted tag saturation is n=2h+6.
- If x1=x2 but x nonconstant, full three-channel rank exists yet needs **2h+10**, as proved above.
- If x1!=x2, the same general two-gate argument bounds the first saturation between **2h+8 and 2h+10**. It remains unknown whether all such positive affine parameters reach rank 3r at 2h+8 on every fibre.

This is a sharp true-rank obstruction for one positive affine parameter stratum, not a complete classification of all six-axis weight spaces.

## Actually executed exact finite verification and reproduction

`VERIFY_EC49DI.py` reconstructs true signed X6 words, six-component return, every complete future-operation word, final A/B tags including seams and positive integer Wx/Wy, and certifies nonzero modular ranks over **1,000,003** and **1,000,033**, with no floats. Exact positive test: x=(2,2,5,2,2,2), a=2,b=1, y=(5,5,11,5,5,5). Gate determinant =54.

Actual command: `python3 VERIFY_EC49DI.py --maxh 6`; returned PASS. For h=2..6, m=0..5, 60 two-prime extreme-rank checks matched [1,2,5,8,11,12]. All **135 endpoint fibres** at h=2..6, both exact and cumulative languages, attained the predicted full 3r by n=2h+10: **270 fibre-language instances, 540 two-prime modular checks**, max rank 18 and at most 883 complete suffixes before reaching it. `EXECUTED_SUMMARY_EC49DI.json` records authentic summary, the original full 81-kB per-fibre JSON and unchanged executed source are also preserved as a downloadable local archive `EnterpriseMath_EC49DI_20261101_FULL_EVIDENCE.tar.xz`. Local run evidence SHA256 for executable source `c3df9b4a2354e84789e245a1a178c7157116dc222e9bdebdae2477876a736bba`; full per-fibre report `6f567831ac9963e92a5754739d3c12f012a83f20377f8f10a3c06b6041d2b1da`; command log `fb4d8ff4527f98f8ea0dce03941ef82b54a0a4a39d8cb0a2700b462c0e5b9b83`. Finite audit does not replace analytic all-h proof and does not establish independent acceptance.

Prior-art framing: Balle et al., *Optimal Spectral-Norm Approximate Minimization of Weighted Finite Automata*, ICALP 2021, DOI 10.4230/LIPIcs.ICALP.2021.118, supplies general weighted-automata/Hankel-rank context, not this project-specific theorem.

## Next EC49DJ

For positive affine y=a*x+b, a,b>0 and x1!=x2, classify when genuine three-channel rank saturates by 2h+8, versus requires 2h+10. Seek smallest explicit full native X6 returning fibre with rank deficit at 2h+8, or a uniform determinant proving none. Independently adversarial-audit EC49DE's six-feature representation, final A/B seams, and the tensorization basis. No canonical Task machine publication/CLAIM or Foundation admission is inferred.
