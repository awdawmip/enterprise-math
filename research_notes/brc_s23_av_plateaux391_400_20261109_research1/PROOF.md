# S23/AV auxiliary capacity: exact finite certificates for plateaux 391–400

Date: 2026-11-09 (Asia/Shanghai). **Status: AUTHOR_SIDE_FINITE_EXACT_CERTIFICATE; independent mathematical review pending.** Frozen scientific input: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. The native Heartbeat X6/P000 ontology and the distinct six-source/ten-label bridge are unchanged.

## Statement and scope

In the frozen two-point iid auxiliary observer on labels (1,3,4), `P0=(1/2,1/4,1/4)` and `P1=(5/7,1/4,1/28)`. A prefix retains the joint counts of labels 1 and 4, with label 3 neutral. Let `T_h={10^j/7^s : 0<=j<=s<=h}`. `N(h)` is the least common padded prefix length with an attainable likelihood ratio strictly inside every open cell of the partition induced by `T_h`, including exterior cells.

Set `r=ln(7)/ln(10/7)`, `eps=79r-431`, `d=2074774-380295r`, `alpha=d/eps`, `a_i=floor(i*alpha)`, `V_i=380295*i+79*a_i`, `K_i=2074774*i+431*a_i`, `H_i=V_i+510`, `M_i=K_i+V_i-V_(i-1)-1`.

**Finite certificate theorem, conditional on the inherited correctness of the previously published exact critical-cell covering checker and global first-entry lower-bound theorem:** for every integer `391<=i<=400` and every integer `V_(i-1)+511<=h<=V_i+510`, one has `N(h)=M_i`.

Thus the newly covered contiguous range is `148333573<=h<=152136996`, i.e. **3,803,424 new integer horizons**. At its final endpoint, `N(152136996)=830390827`. The previous verified endpoint is `H_390=148333572`, `N(H_390)=809640501`.

## Proof and exact finite evidence

1. The published all-index scaled-gap first-entry theorem at immutable source commit `85b53d06d6ba775e516c566c1d79828b6ca9bb1f`, path `research_notes/brc_s23_av_scaled_gap_sturmian_jumps_20261108_research1/PROOF.md`, proves `N(V_(i-1)+511)>=M_i` for all integer `i>=2` in this auxiliary model.
2. The *unchanged* endpoint checker `research_notes/brc_s23_av_plateau20_20261108_r1/VERIFY_PLATEAUX20_200.py` (Git blob `261d7e22da0e62d667009cb50acfe77ac4e35c3f`, fetched from PR #1777) was reconstructed locally byte-for-byte; its local Git blob was computed and checked equal. It uses exact `Fraction` bounds from 45-term atanh expansions, determines `floor(i alpha)` by strict rational inequalities, enumerates admissible narrow displacements, checks the complete finite critical-cell partition against translated witness predicates, and checks the top 510 rows and both exterior cells. Completeness of this finite critical-cell reduction is an inherited proof obligation documented in `research_notes/brc_s23_av_plateau20_20261108_r1/PLATEAUX20_200.md`.
3. Actual calls to `check(i)` returned non-null complete tuples for every integer `391<=i<=400`. The finite exact run checked **758,786 feasible critical cells**, with no uncovered cell, mixed-sign blocker or failed strict rational comparison. Maximal cells for one endpoint: 77,467; maximal narrow displacement types: 122. Rows and witness counts are in `RUN_EVIDENCE.csv`.
4. The separate exact-integer audit `AUDIT_391_400.py` verified for all ten reported endpoints the strict alpha-floor bracketing, `H_i`, `M_i`, and contiguous interval joining. The audit emitted `PASS_10_EXACT_ENDPOINT_AND_FLOOR_AUDIT`.
5. Hence the checker yields `N(H_i)<=M_i` for the ten endpoints. Nondecreasing `N(h)` combined with the lower bound from (1) proves equality throughout each stated interval. Consecutive intervals join because the lower endpoint for `i+1` is `H_i+1`.

**Execution segmentation is important:** the separate `i=391` process completed with `PASS_SEGMENT 391 391`. A long process requested 392–400 and emitted complete successful rows for 392–398 before its 110-second limit; it did **not** emit an overall pass for 392–400. The remaining 399–400 were executed in a separate process and completed with `PASS_SEGMENT 399 400`. Together these preserve ten complete endpoint evaluations; no stopped computation is counted as a finished row.

## Meaning, limitations, next question

The result is a conditional author-side exact finite certificate. It is not formal checker acceptance, independent proof review, native six-axis/X6 dynamics, or a proof of arbitrary-index equality `N(H_i)=M_i`. The applied BRC interface is the branch/provenance-preserving joint-count likelihood observer; the label-3 padding quotient is justified for this auxiliary likelihood readout only, not future arbitrary native operations.

Next: check `i=401` in a bounded process; find a uniform all-index translated-witness covering invariant or an exact first uncovered cell; separately study the lawful observation bridge to the six-source ten-label mother model. No formal Task CLAIM or Owner authority is asserted by this research note.
