# D25 — Exact characteristic-p Green flux for Sun's d=3 and d=4 defects
2026-11-04 · TASK_RESEARCH author-side, UNREVIEWED / NOT_ADMITTED.
Logical lane: chatgpt-research-onhour-enterprise-math-20260923; maintenance lane distinct. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; immutable scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3.

## Exact global polynomial conservation theorem

For every p>=5 prime and d in {3,4}, retain the already proved original Sun finite-period notation: C=(d-1)/d², u=X(1-X), v=1-2X, F=sum_{k=0}^{p-1}(1/d)_k(1-1/d)_k/(k!)² X^k reduced mod p, E=(F_lift²-H(u))/p²=C X^p Q in F_p[X], with Q(0)=0, deg Q<=J<=p-2. The previous exact theorem gives T_C Q=2F-6(1-X)F', where

    T_C = u²D³+3uvD²+(v²-(2+4C)u)D-2Cv.

For arbitrary polynomials f,g define the symmetric concomitant

    B_C(f,g)=u²(fg''-f'g'+f''g)+uv(fg'+f'g)-4Cufg.

**New theorem (exact finite Green flux):**

    B_C(F²,Q) = 2(1-X^p)-2(1-X)F³  in F_p[X].       (G)

**Proof.** Formal integration by parts yields T_C^*=-T_C and the exact polynomial Lagrange identity D B_C(f,g)=f T_C g+g T_C f. The original truncated second-order hypergeometric equation makes T_C(F²)=0 mod p. Therefore D B_C(F²,Q)=F²(2F-6(1-X)F')=D[-2(1-X)F³]. Hence P=B_C(F²,Q)+2(1-X)F³ has zero derivative in F_p[X].

The previous checked finite-support theorem bounds deg F<=m and deg Q<=J, with 2m+J+2<=p in all cases p=3m+1,3m+2 (d=3) and p=4m+1,4m+3 (d=4). Thus deg P<=p, whence P=a+bX^p. At X=0 every B-term contains u and F(0)=1, giving a=2. At X=1 every B-term contains u and (1-X)=0, giving a+b=0. Thus b=-2 and (G) holds for every allowed prime. QED.

The Frobenius boundary term X^p and the two original source labels remain present. For p≡13,19 mod24 with s²=2, x_3=(2+s)/4, x_4=(3+2s)/6 and x_d^p=1-x_d, evaluation gives

    B_C(F_d²,Q_d)(x_d)=2x_d-2(1-x_d)F_d(x_d)³.

At a CM zero of the period modulo p this becomes 2x_d. The equality is an ordinary exact finite-field observer identity, not a calculation of the separate native H0/B0 Frobenius.

## Independent tests and continuation

A separate mod-p recurrence checker constructs c_k, Q via the new three-term Green transport and independently expands both sides of (G), validating every coefficient. 70 model-prime cases (all p=5..151 and p=373; d=3,4) passed. The X^p coefficient of P was -2 in both models, including residues 11 for p=13, 17 for p=19, 137 for p=139 and 371 for p=373. The preceding independent mod-p³ convolution checker already validated the Q recurrence against the original Sun defect for the same cases.

Next real science: seek an exact signed cross-model CM Green intertwiner using both (G) identities and the original weighted period-and-derivative observer, first testing p=13,19,139,373. Native fixed p=373 H0/B0 [X]U mod139129, module rank, semilinear Frobenius and independent replication remain pending under #1559 with no recorded executor. No native Research CLAIM/run/checkpoint/Result was established in this lane. Status: EXACT PROOF / FINITE EXACT CHECKED / AUTHOR PUBLISHED / UNREVIEWED / NOT_ADMITTED.
