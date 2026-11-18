# Stage244–245 exact execution record and certificate index

**Classification:** author-side exact mathematical/computational evidence; not independently reviewed or accepted by native Source. Date 2026-10-28. Root model N=14 IID with P=(3,1,20)/24 and Q=(2,2,20)/24. Previously verified author frontier Stage243 commit 0c522c040132b11794adea98967f97a6f51506af.

## Actual local execution

Python standard library fractions.Fraction and arbitrary-precision integers, no floats in proof checks. Source programs are full and executable from their own directory, generating corresponding detailed JSON certificates. Files in this PR are exact source text and were verified against original executed local Git-blob identities, not represented as remote GitHub-side execution.

    python STAGE244_EXACT_REPRO.py
    STAGE244_EXACT_AUTHOR_PASS 16384 ordered_nodes 1441798
    ALPHA 136710455785/365699432448 VALUE 324682148605/45712429056 WIDTH 1765157155/11702381838336

    python STAGE245_EXACT_POLYTOPE.py
    STAGE245_EXACT_POLYTOPE_PASS 16 ties 27 candidates 419 DFS_nodes 403
    ALPHA 2/5 VALUE 24/5 WIDTH 47846585971/1828497162240

## Stage244 full proof certificate

Dual λP=96950297784/1765157155, λQ=104485552128/1765157155, H=57363048204634793377/1152708874580404224. 680 Bellman states, 14 two-action ties, 1226 strict positive action gaps, minimum gap 34069364/1765157155. 16384 deterministic action tables were exhausted; integer suffix DP matched unmerged integer weighted ordered-history DFS for all 1441798 visited history prefixes. Error-plane hull 4 vertices from 12280 distinct exact (D(eP−eQ),D eP) points.

Global supports:
lower A=(-2972925671028817920,6586558925383925760), B=(3250719450805043200,9253835406169866240).
upper C=(-3210930030792146944,6487730030792146944), E=(3268357523094110208,9264567553886257152).
The full support sign inequalities and exact eP=eQ hyperplane intersections are checked by executable integer determinant calculations, not numerical sampling.

Lower balanced witness: deterministic masks 5 and 16383, exact weights 620025530015/1187066101424 and 567040571409/1187066101424, α243=4372969427965/11702381838336, tP=V243=10415008236599/1462797729792, tP−tQ=1535520971813/2925595459584>0.
Upper witness: masks 0 and 16379, weights 194809289163/386195633047 and 191386343884/386195633047, α244=136710455785/365699432448, tP=V244=324682148605/45712429056, tP−tQ=47846585971/91424858112>0. All four endpoint masks also checked with a separate forward mass propagation algorithm.

## Stage245 full proof certificate

Dual λP=40, λQ=48, H=40. 680 Bellman states, 27 two-action ties, 1213 strict positive action gaps, minimum 296/6561. Exact 2D error-set convex/Minkowski induction covers all Bellman-optimal randomized policies, without iterating 134217728 deterministic corners. Root convex error polygon has 16 vertices, max intermediate polygon 16 vertices; total candidate combinations 419. Global supports:
lower (-3210930030792146944,6487730030792146944) to (3268357523094110208,9264567553886257152) (balanced α244);
upper (-3210930030792146944,6487730030792146944) to (21035720123168587776,21035720123168587776) (balanced α245=2/5).
Every root error hull vertex passed the exact support inequalities and tP+40eP+48eQ=40 check. Exact 4-observation origin trees were retained, and full-history DFS independently checked 403 visited ordered nodes for the four endpoint witness trees.

Lower balanced witness is the Stage244 upper witness, time advantage tP−tQ=47846585971/91424858112>0. Upper witness root vertex mixture weights 313456656384/361303242355 and 47846585971/361303242355 produces exactly eP=eQ=2/5 and tP=tQ=24/5. The latter is a boundary case, not a strict time-dominance certificate. Arbitrary *real* root mixing covers the entire stated α interval.

## Reproducibility, exact scope and pending gates

The complete Python scripts regenerate richer machine-readable JSON files automatically, including all tie states, exact hull/root vertices, endpoint weights and residuals. The local author archive additionally includes original JSON outputs, stdout and per-file SHA256 manifest. GitHub repository contains the reproducer, mathematical argument and this precise certificate index; **do not mistake this concise index for a remotely stored full generated JSON**.

Typed BRC observer use: separate positive integer P/Q branch masses and ordered provenance; only *declared* finite-IID four-observation sufficiency is proved. No native typed BRC execution or P000/X6 Cell correspondence. Gate status: CONTROL_QUOTA during attempted live-owner read; research_authority_granted=false; formal CLAIM, Source Result, independent Driver review and canonical scientific admission remain outstanding. Classify as AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED.
