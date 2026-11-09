# BRC-X6: a strictly positive 9-minimal policy with common denominator 24

Date: 2026-11-09. Evidence: AUTHOR_PROVED / EXACT_FINITE_CERTIFICATE / UNREVIEWED / NOT_ADMITTED. Frozen scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.

## Model, observer and main result

Use the original 96-port/576-labeled-action native kernel, all nine frozen roots, and the complete joint observation (next port, R1..R6, K), with four signed source ports (6,7,28,29), signs (+,-,-,+), and the 38 lawful deterministic four-source controls preserving all signed native atoms. A policy is a nonnegative convex mixture of those 38 native four-source action tuples; s(x) denotes the minimum number of distinct lawful pure policies needed for such a mixture.

Here is an explicitly **full-support** rational policy x. For each row the six displayed integer numerators have common denominator 24:

    source 6:   1  5  5  1  7  5
    source 7:   6  4  5  1  4  4
    source 28:  6  4  1  5  5  3
    source 29:  3  3  6  4  5  3

Every action probability is positive. The following nine lawful deterministic controls, in original 0-based action-label order, realize x exactly. Weights are integer numerators over 24:

    (0,0,2,2): 1       (1,0,3,2): 5       (2,2,4,4): 5
    (3,3,5,5): 1       (4,4,0,0): 3       (4,4,5,5): 1
    (4,5,0,1): 3       (5,1,1,3): 4       (5,5,5,5): 1

Each of these nine controls is among the 38 exact lawful controls for every frozen root. Signed joint atom balance is checked on the original native labeled edge kernel, not a scalar reduction. Hence s(x)<=9.

## Singleton-mass exact lower-bound lemma

For an arbitrary strictly positive four-row table with a=6 action cells per row and a representation by m positive deterministic terms, each row has at least max(0,2a-m)=max(0,12-m) **singleton cells** occupied by exactly one term. Indeed all six cells need at least one term, and each nonsingleton cell consumes at least two terms.

If the coefficient of one such singleton term equals rational mass v, this term has mass v in every one of the four source rows; thus it must fit into some cell of each row. Consequently v <= M := min_p max_a x[p,a].

Let c[p,v] be the count of cells in row p having mass v, and let t[v] be the number of terms whose coefficient is v and which occur as a singleton in at least one row. The following conditions are necessary:

    sum_v t[v] <= m;
    sum_v v*t[v] <= 1;
    for each row p: sum_v min(t[v],c[p,v]) >= max(0,12-m).

Only positive masses v<=M need be considered. Capping each t[v] at max_p c[p,v] preserves these necessary coverage inequalities and decreases both budgets. All comparisons and sums are exact. These conditions are a lower-bound relaxation, not a complete characterization of possible decompositions.

## Compact proof that s(x)>=9

For m<=8, each row requires at least four singleton cells. For the explicit x above, M=6/24; only singleton coefficient numerators v in {1,3,4,5,6} are eligible. Their original four-row multiplicities are:

    v=1: (2,1,1,0)
    v=3: (0,0,1,3)
    v=4: (0,3,1,1)
    v=5: (3,1,2,1)
    v=6: (0,1,1,1)

It therefore suffices to check the 384 integer count vectors

    t1=0..2, t3=0..3, t4=0..3, t5=0..3, t6=0..1.

Requiring t1+t3+t4+t5+t6 <=8 and the four coverage sums >=4 leaves exactly NINE possibilities. The smallest integer coefficient mass sum

    t1 + 3*t3 + 4*t4 + 5*t5 + 6*t6

is 25, attained at (t1,t3,t4,t5,t6)=(2,1,1,2,1). But the sum of all nine mixture weights is exactly 24/24=1. Any m<=8 decomposition would require singleton coefficients of total mass at least 25/24>1, an exact contradiction. Therefore s(x)>=9 and, with the explicit nine-term representation, **s(x)=9**.

This is a 5-bit **full-support** 9-minimal witness, compared with the earlier author-side 113-bit full-support positional-base witness (2026-11-09, commit bed52e2da16f13e98bc54c29ac1418093a117b28). The earlier 9-vertex simplex-face barycenter with denominator 9 has zero coordinates and is a different model input. No assertion is made that 24 is globally the smallest possible denominator for this input class.

## Verification and scope

The portable proof/certificate verifies all 9 frozen roots; 38 exact lawful pure controls; all 24 positive rational marginals; 384 possible singleton count vectors and all 9 survivors with minimum mass numerator 25. The primary verifier enumerates the finite count vectors directly; an independent integer dynamic-programming implementation obtains the same exact minimum 25, plus a rational-parameter relaxation check. Verification costs: finite 384-vector count search after the 24-cell projection and original root/action checks, rather than 38-choose-8 subset enumeration. This is a scoped witness and reusable residual-preserving lower-bound tool, not a claim of asymptotic improvement.

The mathematical proof and portable verification programs belong to this author-side evidence unit; native D25 H0/B0, Frobenius, CM, Source checkpoint and independent Driver review retain their own authority/status. No Source CLAIM, mathematical admission or inherited predecessor completion is asserted.

Next: strengthen the necessary mass histogram conditions using the legal four-action incidence tensor; benchmark exact sparse recovery and infeasibility on rational 6..13 cases with preprocessing, bit length and certificate checking costs.
