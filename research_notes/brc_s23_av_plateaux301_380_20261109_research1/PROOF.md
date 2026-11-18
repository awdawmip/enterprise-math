# S23/AV auxiliary capacity: exact plateaux 301–380

Date 2026-11-09 (Asia/Shanghai); AUTHOR_SIDE_FINITE_EXACT_CERTIFICATE; independent review pending.
Scientific input remains frozen: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Predecessor: research_notes/brc_s23_av_plateaux269_300_20261109_research1/PROOF.md at fac950d87c2a89c51c16224ae7af787e400e24a6.

## Precisely scoped theorem

For the frozen two-point iid auxiliary experiment on labels (1,3,4), the laws are P0=(1/2,1/4,1/4), P1=(5/7,1/4,1/28). Keep joint counts (#1,#4) and label-3 neutral padding. Let N(h) be the least padded prefix length whose attainable likelihood ratios intersect every open cell, including exterior cells, induced by T_h={10^j/7^s:0<=j<=s<=h}.

Put r=ln(7)/ln(10/7), epsilon=79r-431, d=2074774-380295r, alpha=d/epsilon, a_i=floor(i alpha), a_0=0; V_i=380295i+79a_i; K_i=2074774i+431a_i; H_i=V_i+510; M_i=K_i+V_i-V_(i-1)-1.

**For every integer 301<=i<=380 and every integer V_(i-1)+511<=h<=V_i+510, N(h)=M_i.**

The inherited i=300 endpoint H_300=114102835 has M_300=622887919. Newly checked contiguous horizons are 114102836<=h<=144530148 (30,427,313 integers). The terminal endpoint is H_380=144530148, N(H_380)=788890175.

## Proof: inherited general lower bound plus 80 finite exact upper certificates

The all-index scaled-gap first-entry theorem in research_notes/brc_s23_av_scaled_gap_sturmian_jumps_20261108_research1/PROOF.md, frozen at commit 85b53d06d6ba775e516c566c1d79828b6ca9bb1f, gives N(V_(i-1)+511)>=M_i for i>=2.

For each i=301..380 we executed the unchanged source checker at research_notes/brc_s23_av_plateau20_20261108_r1/VERIFY_PLATEAUX20_200.py, Git blob 261d7e22da0e62d667009cb50acfe77ac4e35c3f (3983 bytes). Its inherited soundness argument in PLATEAUX20_200.md and the 201–220 proof establishes a finite critical-cell reduction: strict 45-term Fraction logarithm bounds; complete embedded narrow-gap directions; partition of feasible integer endpoint triples (v,j,v+j); existence of length<=M_i translated integer-prefix witnesses for all feasible cells; top-510-row and exterior witnesses. Each check(i) returned a certificate with no uncovered cell, mixed-sign category or exact-bound assertion failure. Strict integer alpha-floor brackets a_i*EU < i*DL < i*DU < (a_i+1)*EL were checked at every i.

The 80 actual per-index rows in RUN_EVIDENCE.csv certify a total of 4,518,903 feasible critical cells, maximum 69,928 in one check, and maximum 116 narrow-gap displacement classes. One initial local 301–350 run was interrupted after it completed 301..321; five further bounded segments completed 322..334, 335..347, 348..360, 361..372 and 373..380. The 80 completed rows were sorted and checked for contiguous unique indices. No untested index was promoted to a result.

For each i, the lower equality at the interval start, the upper inequality at H_i, and monotonicity of N(h) imply the asserted equality for all integer h in that interval. Adjacent intervals concatenate because H_i+1=V_i+511.

The resulting mathematical statement is conditional on the inherited exact checker soundness and lower-bound theorem, and remains author-side until independent verification. The statistical two-point auxiliary observer is a typed external model; transfer to the six-source ten-label mother problem and native P000/X6 requires its own lawful observation bridge.

## Reproduction and next question

VERIFY_301_380.py calls the same upstream checker with a Git blob check; run it in bounded slices using --start 301 --end 310, etc. RUN_EVIDENCE.csv preserves all 80 observed results. Next test i=381 onward and preserve an exact first failing critical cell if any; concurrently seek an all-index translated-witness sufficiency theorem that handles growth of narrow-gap direction families, and analyze bit complexity of check(i).
