# N14 Stage135 — exact first scientific unit (DUAL_CANDIDATE_ONLY)

**External auxiliary iid model, not native P000/X6.** For N=14, ternary P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), consider arbitrary literal-ordered-history randomized stopping/decisions and V14(alpha)=inf max(tP,tQ) with P(declare Q),Q(declare P)<=alpha.

## Verified predecessor (AUTHOR-level)

Stage134 exact endpoint alpha134=36703016772992738695/105616844785075617792, V134=656399729826573779227/52808422392537808896. Its dual is (K,L)=(48012912/81457,45307624/81457); ties B=(11,0,1) Q/C and G=(9,3,3) Q/C. At the endpoint G has Q-stop probability 1, while B remains mixed at w=29128806260109437/81438720000000000.

Full exact proof and runnable author checkers: research_notes/n14_aux_iid_affine_134_20261026/{PROOF_STAGE134.md,VERIFY_STAGE134.py,INDEPENDENT_ORDERED_STAGE134.py}. These are not an independently admitted Result.

## New exact dual candidate

Move along K(t)=K134-t, L(t)=L134-(112/129)t. First newly vanishing strict action gap candidate:

t=301004945493984/17079934306375,
K135=119895901488/209680375,
L135=113419128664/209680375.

A separate full 680-state exact Fraction check at this candidate found 1238 strictly positive gaps; the only two ties are B=(11,0,1), declare Q vs continue, and new A=(7,3,0), declare P vs continue. Other gaps are strictly positive, minimum=8101984967/271745766000. Root dual value=1222494294337487125572330743/3063040058209052550758400.

**Candidate only.** This does not establish any Stage135 primal feasible interval, right endpoint, or sharpness.

## First executable independent unit

1. Recompute Bellman choices from the exact candidate dual with rational arithmetic. Count real FIRST-HIT literal histories for A and B along strict choices, retaining separate P and Q positive weights, order and stopping depth until observers (eP,eQ,tP,tQ).
2. Determine descendant cone relationship. Since A has 3 zeros and B has 0, A cannot precede B; B has deeper stopping depth and cannot precede A. Verify actual first-hit and conditioned suffix moments, not just count-level combinatorics.
3. At A let u be probability of immediately deciding P; at B let w be probability of immediately deciding Q. Compute four deterministic corner observer vectors independently (bottom-up exact Fraction plus top-down integer prefix DFS); verify any cross term is zero.
4. Solve exact eP=eQ, identify the full legal real randomized interval, test tP>=tQ (or handle switching max), and prove equality with the universal Bellman bound. Characterize right endpoint and prove sharpness for *all literal ordered-history policies*, including prefix-dependent coins.
5. If full real interval is obstructed, publish the precise exact obstruction or narrower independently proved lemma instead of promoting a dual candidate as a theorem.

Preserve the fixed mathematical evidence distinction: author computation != independent Research Driver acceptance; no native P000 transfer; active owner/CLAIM remain unverified because native control dispatch returned CONTROL_QUOTA. For future formal task ownership, consume the actual source packet and follow the current native protocol.
