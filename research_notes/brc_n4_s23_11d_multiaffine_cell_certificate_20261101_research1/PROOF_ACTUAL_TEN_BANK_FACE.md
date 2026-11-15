# BRC N=4 / S23 — sharp 9/14 worst error on an actual frozen ten-label bank face

Date: 2026-11-01. **Author-side exact mathematical proof plus executed rational certificate; UNREVIEWED / NOT_ADMITTED.** This theorem concerns one already frozen k=4 common encoder and ten fixed decoder kernels, restricted to a lawful two-parameter face of the eleven-parameter S23 model. It is not the eleven-dimensional or unrestricted ten-label minimax optimum.

## Frozen source, decoder and observer

Reuse exactly the six BRC latent sources, the six mixed preparations, four stopping times, M=M20/20 and S23 stopping law from the sibling PROOF.md. The k=4 deterministic encoder maps sources (AU0,AU1) to AU, AV to AV, (BU0,BU1) to BU, and BV to BV. The first nine fixed decoders from PR #1765 have four group rows AU AV BU BV, each pair ij denoting half mass at times i and j:

    label 1: 34 24 34 24       label 2: 34 23 34 34
    label 3: 34 34 34 23       label 4: 24 24 12 12
    label 5: 12 12 24 34       label 6: 12 13 23 24
    label 7: 23 34 12 13       label 8: 24 34 12 14
    label 9: 13 12 13 13

The tenth decoder group rows are
    AU=(1/2,0,1/4,1/4); AV=(1/2,0,1/2,0);
    BU=(1/2,0,0,1/2);   BV=(1/2,1/2,0,0).

The legally causal face is given by real s,t∈[0,1], a_A=s, a_B=t, b_U=b_AV=b_BV=0 and (c_AU0,c_AU1,c_AV,c_BU0,c_BU1,c_BV)=(0,1,1,1,0,1). Let p_i(s,t)=sum_x M_ix F_x(s,t) be the exact prepared stop-time law and q_li=(M E D_l)_i the frozen decoded law. The strategy label is selected after policy selection, before observation. Let

    G(s,t) = min_(l=1,...,10) max_(i=1,...,6) TV(p_i(s,t),q_li).

## Exact theorem — the whole real face has supremum 9/14

**sup_{(s,t)∈[0,1]²} G(s,t) = 9/14.**

**Upper bound (all real s,t).** The mixing matrix M is block-diagonal between the first three A preparations and last three B preparations. On this face, every A prepared law depends affinely on s alone and every B prepared law depends affinely on t alone. For fixed decoder l, its sublevel region at radius r is a Cartesian product A_l(r)×B_l(r) of two closed intervals (possibly empty).

Every individual TV constraint TV(p_i(z),q_li)≤r is exactly equivalent to 16 signed linear inequalities

    sum_(u=1,...,4) sigma_u (p_i(z)_u - q_li,u) ≤ 2r,
    sigma∈{-1,+1}⁴.

Thus both intervals arise by exact rational intersection of finitely many one-variable affine half-spaces; no stochastic endpoint approximation occurs. At r=9/14 their exact intervals for four of the ten frozen labels are

| Label | A interval for s | B interval for t |
| --- | --- | --- |
| 2 | [0,9/14] | [0,9/14] |
| 5 | [5/14,1] | [0,2/7] |
| 9 | [5/14,1] | [2/7,1] |
| 10 | [0,1] | [5/14,1] |

These four **fixed-label** product rectangles already cover the entire square: for s≥5/14 use label 5 when t≤2/7 and label 9 otherwise; for s≤5/14 use label 2 when t≤9/14 and label 10 otherwise. All boundaries are included and the two alternatives overlap where necessary. Therefore G(s,t)≤9/14 for every legal real pair.

**Sharp lower witness.** At the legal rational policy (s,t)=(2/3,2/7), the exact ten frozen label losses in order are

    (1, 2/3, 2/3, 1, 9/14, 1, 5/6, 17/20, 9/14, 5/7).

Hence G(2/3,2/7)=9/14; the upper bound is attained.

## Executed verification and independent methodological check

The sibling `VERIFY_TEN_BANK_FACE_COMPACT.py` imports the previously published exact S23 BRC mixing source `VERIFY.py`. It reconstructs all ten frozen decoder kernels and asserts stochasticity; intersects all 16 exact signed inequalities for each of six mixed preparations using Python Fraction; checks four full interval pairs and the real-square rectangle partition; and verifies all ten losses at the rational witness. Its actual stdout is `RUN_EVIDENCE_TEN_BANK_FACE_COMPACT.txt`. The universal statement follows from the affine/sign-inequality reduction and the covering argument, not from the finite vertex check. No independent review or formal verification is asserted.

An additional fully executed exploratory cross-check used the general multi-affine fixed-label cell theorem from sibling PROOF.md with a complete 16×16 rational partition. For this same frozen ten-bank face, `min_l max_vertex L_l` gives the legitimate but weaker continuum upper bound 21/32, while `max_vertex min_l L_l` on its 17×17 grid gives only 5/8. The four-rectangle certificate now establishes the sharper **exact** result 9/14, showing why finite grid maxima alone can miss an interior maximum.

This exact 2D face answer neither changes the unrestricted k=4/6,m=10 interval [1/2,2/3] nor solves the full 11-parameter fixed-bank supremum. BRC's six latent *statistical* sources are not the six P000 primitive spatial axes. S2 information-set transfer, native X6/independent-time fidelity and independent review retain separate obligations.
