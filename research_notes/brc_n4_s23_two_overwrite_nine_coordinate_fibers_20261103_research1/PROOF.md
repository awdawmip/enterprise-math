# BRC N=4 / S23: complete nine-coordinate fibers of the overwrite-only two-view observer

Date: 2026-11-03 (Asia/Shanghai). Classification: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Exact model, frozen source and observation horizon

Frozen scientific input is awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. This continues the preceding overwrite-only exact-modulus proof in the same PR at aa6b8110d0e84a94b0911c4d203d21ae1d1527ef. The algebra retains the six separately labeled BRC stochastic sources and four ordered outcomes, without identifying them with the native X6/independent-time state.

For z=(z0,...,z10) in [0,1]^11, let

    A=(0,0,0,1,1,1), B=(2,2,3,2,2,4), C=(5,6,7,8,9,10).
    R(p,q,r)=(p,(1-p)q,(1-p)(1-q)r,(1-p)(1-q)(1-r)).
    M=((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),
       (0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20)).
    P_j(z)=sum_i (M_ji/20) R(z_Ai,z_Bi,z_Ci).

For mask m over indices 0,...,4, U_(m,beta) overwrites each selected coordinate with the known beta. In every pair F from {(3,31),(7,27),(11,23),(15,19)}, let N be the mask omitting bit 2 and E the mask containing bit 2. Observe only

    Psi_F(z)=(P(U_(N,beta_N)z), P(U_(E,beta_E)z))

for any fixed beta_N,beta_E in [0,1], with NO baseline observation. Each view still contains all six labeled mixed rows. Both views overwrite z0 and z1.

## Main theorem: necessary and sufficient fiber test, including endpoints

For each view v=(m_v,beta_v) in {N,E} and any q-index g in {2,3,4}, define q_v(g)=beta_v if g is covered by m_v, otherwise q_v(g)=z_g.

Define the set I_F(z) of invisible original coordinates by:

1. 0 and 1 always belong to I_F(z).
2. A middle coordinate g=2,3,4 belongs to I_F(z) if and only if NO view has beta_v<1 while g is NOT covered by m_v.
3. For each source i=0,...,5, the distinct downstream coordinate C_i belongs to I_F(z) if and only if NO view has both beta_v<1 and q_v(B_i)<1. Equivalently, for every view having beta_v<1, its mask omits B_i and z_Bi=1.

Then for every real z in [0,1]^11 and every fixed real beta_N,beta_E in [0,1],

    Psi_F^{-1}(Psi_F(z))
      = {w in [0,1]^11 : w_j=z_j for all j not in I_F(z)}.

Thus every complete 11D fiber is an axis-aligned closed cube of dimension |I_F(z)|. The projected fiber in coordinates z2,...,z10 is a closed cube of dimension |I_F(z)|-2. All declared free coordinates vary independently throughout [0,1]. The index set is constant across its own fiber.

In particular, for EVERY beta_N<1 and beta_E<1, the nine remaining coordinates z2,...,z10 are globally and uniquely identifiable, including all points with some middle gates equal to 1. The complete 11D observation fibers then have dimension exactly 2 (the original z0,z1).

## Endpoint classification for all four optimal pairs

Write t2=[z2=1], t3=[z3=1], t4=[z4=1]. Each entry is the exact remaining-nine-coordinate fiber dimension. N-only means beta_N<1,beta_E=1; E-only means beta_N=1,beta_E<1.

| Pair F | Both beta<1 | N-only | E-only | Both beta=1 |
| --- | ---: | --- | --- | ---: |
| (3,31) | 0 | 4t2+t3+t4 | 3 | 9 |
| (7,27) | 0 | 2+4t2 | 1+t3+t4 | 9 |
| (11,23) | 0 | 1+4t2+t4 | 2+t3 | 9 |
| (15,19) | 0 | 1+4t2+t3 | 2+t4 | 9 |

For example, F=(7,27), beta_N=1/2, beta_E=1, z2=1 has exactly six free remaining coordinates: z3,z4,z5,z6,z8,z9; the other remaining coordinates are fixed. For F=(3,31), beta_N=1,beta_E=0 the three middle coordinates are free while all six downstream coordinates are recovered. All endpoint numbers include beta=0 as an admissible open gate.

## Proof

The six-by-six source mixer M/20 is invertible (determinant 1/50). Its exact inverse acts separately on every outcome coordinate:

    R0=11P0-10P1, R1=10P1-9P0, R2=P2,
    R3=(9P3-5P4)/4, R4=(5P4-P3)/4, R5=P5.

For each view, this recovers all six ordered raw R rows. The first raw event is beta_v (both root coordinates overwritten). If beta_v<1 and the relevant middle g is not overwritten, its raw second event divided by 1-beta_v recovers z_g. These are exactly the middle indices not in I.

For each source i, whenever a view satisfies beta_v<1 and q_v(B_i)<1, its raw third event divided by (1-beta_v)(1-q_v(B_i)) recovers the original z_Ci. These are exactly the downstream indices not in I. All divisions have strictly positive denominators, including the beta=0 case. This proves necessity of fixing every index outside I.

Conversely, vary any coordinates inside I. A middle g inside I is never retained in a view with beta_v<1; therefore changing it cannot affect any nonconstant raw row. For a downstream coordinate C_i inside I, in every view either beta_v=1 (raw row fixed at its first outcome) or the retained middle gate is exactly z_Bi=1 (raw row stops at its second outcome). All these blockers stay fixed: if any beta_v<1 retains B_i, then B_i is a visible middle coordinate, so its value 1 cannot change; if none do, any varying B_i is always masked whenever the first gate is open. Therefore all six raw rows remain unchanged in both views. In particular I is constant on the fiber. This proves sufficiency and independent coordinate freedom.

For the table, note that each pair's N and E masks both contain bits 0,1; only N can retain z2; and for g=3,4 exactly one of the two views retains g. The downstream group sizes indexed by middle gate are 4 for g=2 (C=5,6,8,9), 1 for g=3 (C=7), and 1 for g=4 (C=10). Apply the two visibility tests to each active-view regime. Both open: each middle gate is exposed at least once, and each downstream coordinate has a view overwriting its middle gate at an open value, so dimension zero. With both closed, all nine remain free. The two mixed regimes give the displayed formulas. QED.

## Verification and precise scope

VERIFY.py uses only Python standard-library Fraction. It evaluates 288 exact finite gate-signatures (four pairs, three beta choices per view and eight upstream boundary signatures), 4,896 direct equality checks on independently varied fiber coordinates, 1,920 coordinate-separation checks, and 1,920 exact inverse reconstructions after source unmixing. Actual stdout is in RUN_EVIDENCE.json. The all-real conclusion comes from the algebraic proof, not finite enumeration. No independent mathematical review or native Result/CLAIM admission is asserted.

The theorem classifies the precise overwrite-only TWO-VIEW readout. It provides an exact future-observation-horizon criterion for latent information preservation; the algebraic mask operations have no asserted physical X6/Heartbeat evolution interpretation.

## Next unresolved mathematical problem

Quantify the sharp inverse stability modulus restricted to z2,...,z10 for beta_N,beta_E<1: determine inf_{z≠w, z0=z0',z1=z1'} d_F(z,w) / ||(z-w)_{2:10}||_infinity and its dependence on masks and betas, with explicit rational extremizers. Also determine the effect of discarding one or more of the six source labels. Keep the mother S23 decoder minimax question separate from this observer-invertibility tool result.
