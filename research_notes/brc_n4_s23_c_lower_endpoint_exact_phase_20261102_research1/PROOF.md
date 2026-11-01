# Exact lower-c endpoint phase transition: BRC N4/S23

**Date:** 2026-11-02. **Status:** AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED. Frozen scientific source: Enterprise Math commit 43ec6098b1330ae86d0a7863be336c5d97f6ef34, asymmetric six-source positive S23 model. This continues the two-endpoint result at 84bc9c68d9de5303b179e253e14de0ce3dabc239. All parameters below are real unless explicitly rational.

## Definitions and theorem

Preserve labeled positive sources AU0, AU1, AV, BU0, BU1, BV with four-stop law

    F(a,b,c) = (a, (1-a)b, (1-a)(1-b)c, (1-a)(1-b)(1-c)).

Preserve the original mixing matrix (rows of 20M):

    (10,10, 0, 0, 0, 0)
    ( 9,11, 0, 0, 0, 0)
    ( 0, 0,20, 0, 0, 0)
    ( 0, 0, 0,10,10, 0)
    ( 0, 0, 0, 2,18, 0)
    ( 0, 0, 0, 0, 0,20).

Freeze a_B=1/4, b_AV=0, b_BV=1/3, and c_AU0=c_AU1=c_BU0=c_BU1=c_BV=1/2. Controls (a,b,c)=(a_A,b_U,c_AV) share the SAME b_U across A and B sources. Define

    Q_tau = [1/2,7/8] x [1/8,1/2] x [1/2-tau,7/8],  0<=tau<=1/8.

Write P(theta) for all six mixed four-stop rows and D(P,Q)=max_i TV(P_i,Q_i), TV(p,q)=sum_j |p_j-q_j|/2. The lawful Chebyshev radius R_L minimizes the maximum D-risk over centers P(z) with z in Q_tau. The hull radius R_H permits one joint center from conv(P(Q_tau)), NOT independently chosen row centers.

Under precisely these freezes, AU0=AU1 and BU0=BU1, with identical third/fourth tail atoms; grouping those two atoms is TV-exact. The reduced three-atom rows (source labels still retained) are

    AU=(a,(1-a)b,(1-a)(1-b));
    AV=(a,(1-a)c,(1-a)(1-c));
    BU=(1/4,3b/4,3(1-b)/4); BV is constant.

For any two probability triples, TV equals the maximum absolute singleton-coordinate discrepancy.

**Exact theorem (full real continuum):** Set

    r0 = (sqrt(43)-5)/8,
    H(tau) = 3/16+tau/6,
    tau_* = 6(r0-3/16) = (6sqrt(43)-39)/8.

For every real tau in [0,1/8],

    R_H(tau) = H(tau),
    R_L(tau) = max(r0,H(tau)),
    R_L(tau)-R_H(tau) = max((2sqrt(43)-13)/16 - tau/6, 0).

Thus the strict gap lasts exactly until tau_* (~0.0430788932265), and is zero for tau_*<=tau<=1/8. At tau=1/8 both radii equal 5/24.

## Universal lower bounds

For any joint hull or lawful center whose AV row is a probability triple (v1,v2,v3) and whose risk is <=r, each vi must be at least the maximum observed value of coordinate i minus r. The three maxima on Q_tau are

    7/8, 7/16, 1/4+tau/2.

Since the center coordinates sum to 1, 3r >= (7/8+7/16+1/4+tau/2)-1 = 9/16+tau/2, hence r>=H(tau).

For any lawful center (x,y,z), three attainable observer-event inequalities are

    r >= 7/8-x,
    r >= 7/16-(1-x)(1-y),
    r >= (3/4)(1/2-y).

The first and third yield 1-x<=1/8+r and 1-y<=1/2+4r/3. The second therefore forces

    (1/8+r)(1/2+4r/3) >= 7/16-r,
    32r^2+40r-9 >= 0.

For nonnegative r the left polynomial is strictly increasing and its unique positive zero is r0. Thus R_L(tau)>=max(r0,H(tau)).

## Joint convex center matching H(tau)

For each tau choose four nonnegative weights summing to one:

    w1=4/9+16tau/27, w2=1/18-4tau/27,
    w3=2/9-16tau/27, w4=5/18+4tau/27,

and the legal third-stage control

    c_H = (1/4-tau/6)/(5/16+tau/6).

Use the SAME weights and control on all six rows:

    C_H = w1 P(1/2,1/8,c_H) + w2 P(1/2,1/2,c_H)
        + w3 P(7/8,1/8,c_H) + w4 P(7/8,1/2,c_H).

For 0<=tau<=1/8 all weights are nonnegative and c_H lies in [1/2-tau,7/8]. The resulting reduced centers are

    C_H,AU=(11/16-tau/6, 1/16, 1/4+tau/6);
    C_H,AV=(11/16-tau/6, 1/4-tau/6, 1/16+tau/3);
    C_H,BU=(1/4,3/16,9/16),  C_H,BV=fixed.

The coordinate ranges of the complete real parameter box are:
AU: first [1/2,7/8], second [1/64,1/4], tail [1/16,7/16].
AV: first [1/2,7/8], second [1/16-tau/8,7/16], third [1/64,1/4+tau/2].
BU: first fixed 1/4, second [3/32,3/8], tail [3/8,21/32].
Direct endpoint subtraction from the displayed centers gives maximum coordinate difference <=H(tau) in every row; in AV the upper second/third differences equal H(tau), in AU the lower tail difference equals H(tau). BU risk <=3/16 and BV risk=0. For probability triples coordinate L-infinity equals TV, so this SINGLE JOINT mixture attains H(tau). Thus R_H(tau)=H(tau).

## Lawful center matching max(r0,H(tau))

Let r=max(r0,H(tau)) and select the single causal tuple

    x=7/8-r,
    y=1/2-4r/3,
    z=(7/16-r)/(1/8+r).

Since 3/16<r<=5/24<1/4, x is in [1/2,7/8], y in [1/8,1/2], and 1/2<=z<=7/8; thus z also lies in [1/2-tau,7/8]. Put s=1-x=1/8+r. The AU second and grouped-tail centers are respectively

    sy=1/16+r/3-4r^2/3,
    s(1-y)=1/16+2r/3+4r^2/3.

For AU, the first-atom error is <=r. The second center satisfies

    1/4-r <= sy <= r+1/64.

The left inequality follows by the monotone expression sy+r-1/4 = -3/16+4r/3-4r^2/3, which starts at 1/64 for r=3/16 and increases through r=5/24. The right follows since sy<=s/2<=1/6<r. Thus the AU second-coordinate error across [1/64,1/4] is <=r. For the AU tail, the upper deviation 7/16-s(1-y)<=r is precisely 32r^2+40r-9>=0; the lower deviation s(1-y)-1/16=(2r+4r^2)/3<=r uses r<=1/4.

For AV, the reduced center is

    (x, 7/16-r, 2r-5/16).

Its first-coordinate error is <=r; the second upper error is exactly r and its lower error 3/8-r+tau/8<=r follows from r>=H(tau)>=3/16+tau/16. The third upper error is 9/16+tau/2-2r<=r from r>=H(tau); the lower error is 2r-21/64<=r for r<1/4. The BU second center is 3y/4=3/8-r; deviations from [3/32,3/8] are at most max(r,9/32-r)=r, since r>=3/16. BV is fixed. These coordinate intervals cover ALL real theta in Q_tau, hence the full six-row risk is <=r. Its AV first-atom witness at a=7/8 attains r, establishing R_L(tau)=max(r0,H(tau)).

Finally r0>3/16 follows from 2sqrt(43)>13; H(tau) is increasing and meets r0 exactly once, at tau_* in (0,1/8). The gap formula follows.

## Exact verification and interpretation

VERIFY.py actually executes Python stdlib Fraction and isqrt checks on 65 rational boxes tau=j/512 (j=0..64), 520 vertices, 6240 original four-stop mixed-row center TV comparisons. For the one irrational parameter it supplies exact rational polynomial-sign and 2^100 isqrt enclosures with radius width 1/(8*2^100); see actual stdout RUN_EVIDENCE.json. The all-real theorem is the preceding analytic proof; the finite test verifies arithmetic, source mixing, formulas and claimed sample coverage.

This is a model-internal positive-source BRC/S23 observer theorem. P000 X6 Cell, native three-dimensional slice, independent time and source/projection fidelity remain distinct obligations. The full eleven-control ten-label minimax interval [1/2,2/3] for k=4,6 has not changed. No native CLAIM/Result or independent mathematical review is asserted.
