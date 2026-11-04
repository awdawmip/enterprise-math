# D25 — Constant-memory signed Sun first-jet transport at the CM observers

2026-11-05 · TASK_RESEARCH author-side exact algorithm / finite exact check · UNREVIEWED / NOT_ADMITTED.
Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, immutable scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Lane chatgpt-research-onhour-enterprise-math-20260923 (not maintenance).

## Specific unfinished scientific subunit

The immediately preceding CM-zero Green reciprocity [20261105_onhour_d25_cm_zero_green_reciprocity_first_jet.md] eliminates the Q **value** but rigorously shows its scalar flux does not determine the Q' needed by the true signed weighted observer. The existing *original* inhomogeneous Green transport still determines Q uniquely. This unit evaluates Q' without constructing Q as a stored polynomial, while retaining d=3 and d=4 and all signed field components.

For p≡13 or 19 (mod 24), d∈{3,4}, C=(d-1)/d², c_0=1 and
    (j+1)² c_(j+1)=(j(j+1)+C)c_j (mod p).
Take J_3=(p//3)-1 when p mod3=1 and p//3 otherwise; J_4=2(p//4)-1 when p mod4=1 and 2(p//4)+1 otherwise. The previous *proved* Green recurrence states q_0=q_(-1)=0 and
    (j+1)³ q_(j+1)
       = (2-6C/(j+1))c_j
         +(2j+1)(j(j+1)+2C)q_j
         -j(j²-1+4C)q_(j-1) (mod p).
All inverses used have j+1<p and are units for the displayed ranges.

**Streaming value-and-first-jet theorem.** Fix the original x_3=(2+s)/4, x_4=(3+2s)/6, s²=2. Maintain only (c_j,q_(j-1),q_j,t=x^j,V,D) in F_p²; after generating q_(j+1), update
    D <- D + (j+1)q_(j+1)t;
    t <- t*x;
    V <- V + q_(j+1)t.
At the end, by exact finite-sum identities, V=Q_d(x), D=Q'_d(x); hence
    E_d(x)=C(1-x)V,    E'_d(x)=C(1-x)D.
The previous Green reciprocity also independently certifies E_d(x) from F_d'(x), but the **derivative** is computed here from the true source transport.

Proof: induction on j gives c_j and the two most recent q's from the published recurrence, t=x^j, V=sum_(i=1)^j q_i x^i and D=sum_(i=1)^j i q_i x^(i-1). The displayed update yields the invariant at j+1. At J, the previously proved support theorem makes these full Q value and ordinary derivative. Multiplication by C x^p=C(1-x) is performed only **after** differentiation, preserving the Frobenius/derivative order. QED.

For fixed p and either d, the stream uses O(J) finite-field arithmetic operations and **O(1) auxiliary field elements**. Modular inverse via pow has a nonconstant bit-operation cost; no sublinear bit-complexity claim is made. The prime search in the test runner is a separate operation. The algorithm consumes the original input recurrence and does not claim to run the p373 native H0/B0 divided-power experiment.

## Finite evidence and first live-use evaluation

The independent Python exact checker evaluates the streaming first jet for **166 target primes p<=5000**, two original models each (**332 cases**). All tests complete with zero failures. Earlier independent full original p³ convolution values are consumed as regression witnesses for the derivative; the new checker does not substitute finite checks for an all-prime cross-model proof.

| p | (E3,E3') | (E4,E4') | signed S_def |
|---:|---|---|---|
| 13 | (6,11+5s) | (1,12+4s) | 12+3s |
| 19 | (18,4+2s) | (17,5+7s) | 6+18s |
| 139 | (138,3+53s) | (122,50+73s) | 16+75s |
| 373 | (132,287+249s) | (137,371+268s) | 227+371s |

Here S_def = -E3+E4+(3s/4)E3'-(s/6)E4'. All four signs and extension components agree with the previous preserved p³ witnesses, including the nontrivial s components. These are the exact discriminating values for future cross-model candidate identities.

BRC resolution=COMPOSE_APPLIED: distinct coefficient/valuation provenance (d=3,d=4), signed extension field amplitudes, and operation order (derivative then Frobenius) are retained; value-only CM Green flux is used only within its proven observer fiber. Full native-X6 bridge is not claimed.

## Frontier and next action

Mother: Delta_p-R_p=0 mod p (p≡13,19 mod24); current algebraic route W_p-V_p=0 mod p³. The remaining precise proof obligation is a general identity connecting the **streamed signed Q' combination** to the *p-adic period square/derivative* contribution at the two original CM points. The existing recurrence gives exact target values; now test hypotheses at 13,19,139,373 before pursuing a terminating Green/WZ certificate.

The original native p=373 H0/B0 same-original-class [X]U mod139129, rank, semilinear Frobenius and independent replication remain issue #1559 PENDING_OWNER, NOT_EXECUTED. Historical request onhour-d25-20261104-1702-continuation-read FAILED/SOURCE_TREE_SIZE_LIMIT was not reissued. No native Source Research CLAIM, open run, canonical checkpoint or formal Result is asserted. Past staging provenance remains independent. GitHub author-side only, UNREVIEWED / NOT_ADMITTED.