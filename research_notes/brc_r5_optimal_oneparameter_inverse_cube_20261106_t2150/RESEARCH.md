# R5 — Exact optimal one-parameter LR inverse section and a larger four-observer cube

**Research date:** 2026-11-06 (Asia/Shanghai). **Scope:** frozen strictly-positive four-stage delta=1/4 P/Q-BRC likelihood-ratio tree. **Status:** AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

**Frozen science:** account GLOBAL a01383f825ef9d43b4b754254303298c64041568; Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. Current policy was read independently from the contemporary canonical-main snapshots. The fixed finite stochastic tree is an auxiliary typed observer; it is not asserted to be the native Heartbeat X6 dynamics.

## Theorem 1 — all-real LR inverse cube and its exact family optimum

Use the observations W=(e_P,e_Q,T_P,T_Q), e_Q=Q(declare P), e_P=P(declare Q). Set

W_*=(161801/180000, 6499/18000, 267/80, 137/40).

The entire **closed real** four-dimensional cube

    ||W-W_*||_infinity <= h_* = 145/495224

is achieved by explicit legal seedless likelihood-ratio (LR) randomized policies. The choice

    g=u_0=1,  u_1=v_*=57197/61903,  X_2=0

works uniformly for all W in that cube, with the same common likelihood-ratio continuation probabilities at matching time-3 nodes and declarations only at stopped ratios a=1/10, b=1/2.

Compared with the previously proved half-radius h_old=93519/349275680, the exact improvement factor is

    h_*/h_old = 6330621700/5789106657 = 1.0935403465... .

Moreover, among **fixed-v affine inverse sections of the exact form below** with g=u_0=1, u_1=v constant throughout the cube, X_2=0 and only the two declaration keys a and b, the largest possible centered cube half-radius is precisely h_* and is attained uniquely at v=v_*. This is an optimality theorem for the stated restricted section family, not for all seedless LR strategies or all target-adaptive choices of v.

## Model and inverse formulas

The frozen time-3 Q kernels are

    q_3[0]=(13/20, 1/5, 3/20),  q_3[1]=(1/40, 9/20, 21/40)

with time-2 ratios (3/4,5/4), time-3 ratios (1/2,1,3/2), and time-4 stopped ratios (1/10,1,19/10). The time-4 Q kernels at center j=1 are (47/180,43/90,47/180) and (67/162,14/81,67/162), and at j=0,2 are the positive outer rows used in the predecessor proof; the source verifier explicitly checks all six time-4 rows and their likelihood-ratio conditional means.

For any v in [12/13,1] put

    V_0=(26+v)/80, V_1=(8+18v)/80, V_2=(6+21v)/80,
    k(v)=(94+335v)/(90(4+9v)),
    X_0^*=(10v-3)/40, X_1^*=(4-3v)/4, X_2=0.

For arbitrary target W, define d_p=e_P-e_P^*, d_q=e_Q-e_Q^*, s_p=T_P-T_P^*, s_q=T_Q-T_Q^*. The exact inverse is

    X_0=X_0^*+2(s_q-s_p),
    X_1=X_1^*+2s_p-s_q, X_2=0,
    ell_a=1787/9000+(5/2)d_p+(5/4)d_q,
    ell_b=13/80-(5/2)d_p-d_q/4.

At time 3, for each j, set the shared LR continuation probability z_j=X_j/V_j and history Q-flow x_ij=(u_i/2)q_3[i,j]z_j. All V_j are positive. At the two declaration keys set probability of declaring P to ell_a/M_a and ell_b/M_b; at all other keys declare Q, with

    M_a=(509/900)X_0+k(v)X_1,   M_b=V_0-X_0.

Because alpha=47/180, beta=67/162 and the two central incoming capacities are A=u_0/10 and B=9u_1/40, pooled LR continuation gives J=(alpha A+beta B)X_1/(A+B)=k(v)X_1. Thus the displayed M_a,M_b are the exact stopped Q masses, not hypothetical free parameters.

The exact observer identities are

    T_Q=2+(1+v)/2+X_0+X_1,
    T_P=2+(3+5v)/8+X_0/2+X_1,
    e_Q=ell_a+ell_b,
    e_P=1-ell_a/10-ell_b/2.

Substitution yields exactly W for every real target; the center identities hold for every v in the declared family.

## Eight all-real feasibility certificates

For fixed v, legality is precisely ensured by eight affine constraints

    X_0>=0, V_0-X_0>=0, X_1>=0, V_1-X_1>=0,
    ell_a>=0, ell_b>=0, M_a-ell_a>=0, M_b-ell_b>=0.

The other frozen stopping masses are nonnegative because 0<=X_j<=V_j and the positive Q kernels redistribute each continued parent mass; the seven-bin Q histogram normalizes to one and has LR first moment one. As functions of the perturbation (d_p,d_q,s_p,s_q), the respective l1 norms of coefficient vectors are

    4, 4, 3, 3, 15/4, 11/4, L(v), 27/4,
    L(v)=5411/900-3k(v).

Indeed 0<k(v)<509/900, so |2k-1018/900|+|1018/900-k|=2(1018/900)-3k. At v=v_* the exact center slack-to-norm radii, in the same order, are

    386261/9904480,
    894153/19808960,
    76021/742836,
    145/495224,
    1787/33750,
    13/220,
    145/495224,
    44707/16713810.

All are >=h_*; the fourth and seventh equal h_*. An affine f with center f_* and coefficient vector c satisfies f>=f_*-h_*||c||_1 on the entire closed real cube, proving every legal constraint for all real W simultaneously. The binding corner is (d_p,d_q,s_p,s_q)=(h_*,h_*,h_*,-h_*), at which X_1=V_1 and ell_a=M_a.

## Theorem 2 — exact optimality in this family

For a fixed permitted v, the X_1<=V_1 constraint forces any centered cube half-radius to obey

    h <= H_C(v)=(13v-12)/40.

The small-ratio declaration capacity ell_a<=M_a forces

    h <= H_L(v)=(M_a^* - 1787/9000)/L(v)
                =-(10938v^2-9617v-580)/(104(2973v+1448)).

The first bound is strictly increasing in v, while the second is strictly decreasing throughout [12/13,1], since

    H_L'(v)=-(16259337v^2+15838224v-6100538)/(52(2973v+1448)^2)<0.

Their exact difference factors as

    H_C(v)-H_L(v)
      =(9v+4)(61903v-57197)/(520(2973v+1448)).

Therefore their unique crossing in the permitted interval is v_*=57197/61903, where both equal h_*=145/495224. For v below that crossing, H_C(v)<h_*; for v above it, H_L(v)<h_*. This proves the all-real family upper bound, and the eight-slack certificate shows it is attained. QED.

## Exact executable evidence, information scope and remaining question

The published VERIFY.py uses only standard-library fractions.Fraction and itertools. It checks all positive time-3/time-4 Q rows and exact conditional LR moments; all eight rational slack radii; both binding equalities; complete seven-bin stopped Q mass normalization and first moment; 16 closed cube corners plus 625 rational grid targets; the explicit recovered time/error observations and shared LR continuation. Exact stdout is in EXACT_OUTPUT.txt. Finite tests are additional checks; Theorem 1's all-real claim follows from the affine inequalities, and Theorem 2 from the exact monotone envelope.

BRC reuse: seven-bin positive rational stopped-mass histogram and central provenance residual J, with explicit observer loss in the four-coordinate projection. Resolution: REUSE_APPLIED (frozen kernels and predecessor LR section); REUSE_EXECUTED (independent exact Fraction checker). The original R5 mother objective of full four-observer FULL_HIST versus seedless LR image comparison remains open; the five-observer mass separation established previously remains valid.

**Next unit:** allow one additional independent flow variable (X_2>0 or nonconstant g/u_0) or a third declaration key; optimize a new rigorous all-real inverse region at W_*, then compare its geometry with rational FULL_HIST interior witnesses. Separately continue the exact global seven-variable K(W) and quadratic F zero/sign decision outside the proved repair cube. Formal active owner, CLAIM and independent mathematical review were not established in this author-side computation.
