# R1/N14 observer-safe BRC: exact minimum finite-horizon monitor (N=4)

2026-10-26 — author mathematical proof and complete finite enumeration. External three-symbol positive-IID auxiliary model; no P000-native six-dimensional Cell theorem, independent Driver review, formal native CLAIM or Result is asserted.

## Frozen starting sources

GLOBAL_KNOWLEDGE_V1 main: 2e711e9f23ebe815597ac7b228679cdc8bcdeb63; loaded 00_BOOTSTRAP.md, OPERATING_MANUAL.md, P000_STARTUP.json (its canonical SHA-1 agrees with P000_REALITY_FOUNDATION.json blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc), ACTIVE worldview and applicable BRC/code/math policies. Enterprise Math source was read at main 7765e1f20df165c723f06d64ac6449efbe88df6c, including AGENTS.md, docs/PORTABLE_RESEARCH_PROTOCOL.md, and the preceding order-observer-monitor proof and NEXT_TASK. Prior result used: positive-IID law-independent monitor-safe BRC Markovization, only in its stated external finite-horizon setting. This is a new bounded-minimality result; it does not take over Stage171 optimization or its owner.

## Exact problem

Alphabet A={0,1,2}, horizon N=4. For each ordered word h of length 0 through 4 let

R(h)=(I[h contains substring 01], I[h contains substring 10], I[|h|>=2 and its last two letters agree]).

The third readout is zero for lengths 0 and 1. A randomized policy may stop and decide P or Q at any time including time zero. A deterministic, time-indexed monitor must allow current R(h) and all subsequent readouts under future letters to be computed without revisiting the discarded prefix.

## Theorem 1 — exact coarsest right-congruence monitor

For words h,h' of equal depth t define

h ==_t h'  iff  R(hz)=R(h'z) for EVERY suffix z in A^j and every 0<=j<=4-t.

This is the unique coarsest equivalence on depth-t ordered words compatible with every current/future readout and deterministic letter updates. The class [h]_t is a valid monitor state, with update rho_t([h],a)=[ha] and output R([h])=R(h).

Proof: taking the empty suffix gives equal present readouts. If h ==_t h', for any letter a and any remaining suffix z, az is an allowed suffix at time t; therefore R(haz)=R(h'az), proving update well-defined. Conversely, if any deterministic monitor gives h,h' the same state, their states and outputs remain the same after every common suffix. Therefore their readout vectors are equal for every suffix, so h ==_t h'. Thus any such monitor refines this quotient, proving minimality. QED.

Exact backward construction:
- at t=4 the signature of h is R(h);
- at t<4 the signature is (R(h), class(h0), class(h1), class(h2)) using already computed t+1 classes;
- group equal signatures, repeat back to t=0.

By backward induction, these signatures give exactly the suffix equivalence. No heuristic state merging is involved.

## Complete finite classification

| t | words 3^t | minimal pure-monitor classes | actual reachable (count,monitor) classes | max labels of count-aware monitor |
|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 | 1 |
| 1 | 3 | 3 | 3 | 1 |
| 2 | 9 | 8 | 9 | 2 |
| 3 | 27 | **14** | 27 | 6 |
| 4 | 81 | 8 | 43 | 6 |
| sum | 121 | 34 time-indexed | **83 joint states** | |

The horizon-4 readout realizes all eight triples. Depth 3 requires 14 classes because the remaining one-letter continuation can distinguish histories with identical present readouts. For example R(002)=R(020)=(0,0,0), while suffix 1 gives R(0021)=(0,0,0) but R(0201)=(1,0,0). At t=4 no future discrimination is needed, so eight classes suffice.

Independent complete verification used every one of the 121 prefixes, all 120 transitions in the raw prefix tree, all suffixes of lengths 0..4-t and all pairs within each depth. It built 150 explicit distinguishing suffix witnesses for every pair of DIFFERENT monitor classes at fixed depth (0+3+28+91+28). The locally executed complete certificate contains all representatives, class membership, transitions and 150 witnesses; PORTABLE_VERIFY.py generates this same classification on any Python 3.

For only the observer "has01", the time-indexed minimal sizes are 1,2,3,3,2; the usual three-state substring monitor suffices for all horizons. Requiring has01, has10 and last-two-equal together genuinely changes the peak requirement from 3 to 14 in this bounded test.

## A distinct, cheaper count-aware contract

If the Markov state already includes symbol counts k(h), the coarsest product-state relation is h ~=_t h' iff k(h)=k(h') AND h ==_t h'. Its depth-wise numbers are 1,3,9,27,43, summing to 83 reachable joint states. Inside a given count fiber, minimum observer labels equal the number of distinct future-readout profiles; reusing labels across DIFFERENT counts requires allowing rho to depend on (k,s,a), not s alone. The max labels required for any single count fiber at t=0..4 are 1,1,2,6,6. This is a DIFFERENT transition contract and must not be mislabeled as a 6-state pure-letter DFA. Proof: within equal-count fibers the same suffix-distinguishability lower bound applies, and appending a letter keeps both count and suffix-equivalence congruent. Across fibers the count already separates states. QED.

The pure monitor can merge distinct-count histories, e.g. 02 and 12 have the same future-readout profile through t=4. Hence pure-monitor counts and count-product counts need not be numerically comparable at each depth.

## Theorem 2 — exact two-law BRC observer preservation

Let P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). For any full-ordered-history randomized stop/decision policy with T<=4 and independent private coins, there exists one policy on (t,k,[h]_t) with the SAME joint terminal distribution of (T,k(T),R(H_T),decision) under P and Q, simultaneously.

Proof: at each product state x, sum the full-history pre-action surviving conditional masses u_h into F_x, and the masses for stop-P, stop-Q and continue into A_x,B_x,C_x, respectively. Set the replacement action probabilities to (A_x,B_x,C_x)/F_x whenever F_x>0. Since every observed letter has a uniquely determined next quotient state, the positive unweighted branch recursion is identical. Induction proves original and compressed flows agree at every product state. Under either positive IID law L, the likelihood of any ordered word with count k is lambda_L(k)=product_i L(i)^k_i, independent of its order. Multiplication by lambda_L(k) therefore gives equal P and Q terminal joint masses for each x and decision. Finally R(h) is a function of [h]_t, proving joint observer equality. QED.

This proof does not transfer to non-IID path likelihoods without extra conditions, preserve internal private-coin correlations, prove minimum arbitrary randomized sufficient representations, or imply P000 X6 state equivalence.

## Executed author's exact arithmetic check

The local author program independently enumerated direct suffix profiles and backward classes (PASS), built every pair witness (PASS), and checked every child transition (PASS). A second executed program propagated a nontrivial ordered-history-dependent rational stop/decision policy using fractions.Fraction and separately propagated aggregate monitor states. It checked the full 332 indexed terminal probabilities (two laws, two decisions, 83 nonzero product states) and both total probabilities equal to one (PASS). Exact policy metrics:
- error_P=10875077779/20639121408
- error_Q=607604449/1289945088
- E_P[T]=7478285/3981312
- E_Q[T]=2817205/1492992

These four fractions are one test policy; the all-policy assertion follows from the foregoing proof, not from finite test data. The local full source/certificate/archive provides the original executed byte evidence; the portable GitHub checker is separately saved for reproduction, not claimed to have executed remotely.

## Evidence and next

Full author evidence: PROOF.md, VERIFY.py, VERIFY_BRC.py, RESULT.json with all 150 witnesses, BRC_RESULT.json, stdout and SHA256SUMS.txt in archive EM_R1_N14_Observer_Minimal_N4_20261026.zip, locally tested with Python 3 Fraction. The locally bundled PROOF.md contains the expanded version of the argument. RESULT_SUMMARY.json gives compact readback fields.

Next: determine the sharp two-law path-dependent, non-IID criterion for a common law-independent compressed policy, with an exact rational failure or a ratio-aware monitor repair. Native owner query currently returned CONTROL_QUOTA; Site gateway is configured static-readonly with no research authority. This proof is an author-scoped research note pending independent review.