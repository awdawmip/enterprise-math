# D25 — source-faithful signed joint-strip second-digit obstruction

2026-10-30 Asia/Hong_Kong. AUTHOR-SIDE / EXACT ALGEBRAIC DERIVATION / EXECUTED FINITE CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3, unchanged. Research conversation chatgpt-research-onhour-enterprise-math-20260923, NOT maintenance. No native CLAIM, authorized run, checkpoint, Result or independent review asserted by this note.

## Consumed original input and exact provenance

Let p=6m+1 be prime, p=13 or 19 (mod24). Define c_n=(1/6)_n(1/3)_n/(n!)^2, G_p(z)=sum_(n=0)^(p-1)c_n z^n, original A_p=sum_(n=0)^(p-1)(6n+1)binom(2n,n)^2 binom(3n,n)/216^n, and B_n=binom(m,n)binom(2m,n). All congruences are in p-local rationals, with explicitly invertible denominators.

Reuse the PROVED three-source c_n expansions from research_notes/portable_direct/20261030_onhour_d25_gauss_three_stratum_harmonic_jet_p3.md:

  0<=n<=m: c_n=B_n[1+pL_n+p²(L_n²-J_n)/2] (mod p³),
  m<n<=2m: c_n=pT_n(1+pK_n) (mod p³),
  2m<n<p: c_n=p²U_n (mod p³),

where

  L_n=-(H_m-H_(m-n))/6-(H_(2m)-H_(2m-n))/3;
  J_n=(H_m^(2)-H_(m-n)^(2))/36+(H_(2m)^(2)-H_(2m-n)^(2))/9;
  T_n=(-1)^(m+n)m!(n-m-1)!(2m)!/[6(2m-n)!(n!)²];
  K_n=(H_(n-m-1)-H_m)/6-(H_(2m)-H_(2m-n))/3;
  U_n=(-1)^m m!(2m)!(n-m-1)!(n-2m-1)!/[18(n!)²].

The consumed CM zero p|G_p(1/2), original first-digit A_p=p (mod p²), and source-aligned Clausen/reflected identity imply, writing h=G_p(1/2)/p, g=G_p'(1/2),

  (A_p-p)/p² = [6 h g+p(h²-R_p)-1]/p (mod p).

The frozen signed observer is NOT a fitted scalar:

  beta_i=B_i/2^i;
  C_1=1/10, C_(a+1)/C_a=36a²/((6a+5)(3a+2));
  R_p=2 sum_(i=1)^m beta_i sum_(a=1)^i (1+6(i-a))C_a (mod p).

Earlier PROVED high-tail reflection: F_p=sum_(n=2m+1)^(p-1) U_n 2^(-n)=sum_(a=1)^(4m) C_a (mod p), research_notes/portable_direct/20261030_onhour_d25_gauss_high_tail_frozen_C_reflection.md. It does NOT assert F_p=R_p; the sources and observers remain distinct. The earlier rational one-index Gosper obstruction and nonsingular rank-three C/S/T carrier are at research_notes/portable_direct/20261030_onhour_d25_frozen_R_gosper_obstruction_rank3_carrier.md.

## Theorem A — explicit four-port obstruction

Define the original-index p-local jets:

  V0=sum_(n=0)^m B_n 2^(-n);
  V1=sum_(n=0)^m B_n L_n 2^(-n)+sum_(n=m+1)^(2m) T_n 2^(-n);
  Y0=sum_(n=0)^m B_n (L_n²-J_n)/2 * 2^(-n);
  Y1=sum_(n=m+1)^(2m) T_n K_n 2^(-n);
  F=sum_(n=2m+1)^(p-1) U_n 2^(-n);
  W0=2 sum_(n=0)^m n B_n 2^(-n);
  W1=2 sum_(n=0)^m n B_n L_n 2^(-n)
       +2 sum_(n=m+1)^(2m) n T_n 2^(-n).

Let X=V0/p+V1 modulo p²; Y=Y0+Y1+F modulo p; Y_low=Y0+Y1. The CM input gives p|V0 and the source expansions imply h=X+pY (mod p²), g=W0+pW1 (mod p²). The first-digit input gives 6XW0=1 (mod p), hence K0=(6XW0-1)/p is p-integral modulo p.

For EVERY target prime p under the consumed source identities,

  (A_p-p)/p² = K0+6XW1+6YW0+X²-R_p (mod p).            (A)

Proof: substitute h=X+pY, g=W0+pW1 in 6hg+p(h²-R_p)-1 modulo p²; use h²=X² mod p, divide its p-divisible value by p, and consume the source-aligned original 216 relation. This does NOT prove the RHS vanishes universally.

## Theorem B — new bivariate signed two-strip joint carrier

Set

  J_p=2 sum_(i=1)^m beta_i [
      sum_(a=1)^i (6a-1)C_a
      +6i sum_(a=i+1)^(4m) C_a ] (mod p).                (B1)

Then exactly

  J_p=6 F W0-R_p (mod p),                               (B2)

and the original LIFT obstruction has the coupled FIVE-PORT representation

  (A_p-p)/p² = K0+6XW1+6Y_low W0+X²+J_p (mod p).        (B3)

Proof: W0=2 sum_i i beta_i and F=sum_(a=1)^(4m)C_a. Therefore
6 F W0-R_p=2 sum_i beta_i[6i sum_(a=1)^(4m)C_a-
sum_(a=1)^i(1+6(i-a))C_a].
Split the a-sum at a=i: the coefficient is 6a-1 for a<=i, 6i otherwise. This gives B1/B2; substitute Y=Y_low+F into A for B3. Every original signed index, branch and weight survives.

Equivalent a-first two-strip representation, useful for bivariate telescoping:

  J_p=2 sum_(a=1)^(4m) C_a [
        6 sum_(i=1)^(min(a-1,m)) i beta_i
        +(6a-1)sum_(i=a)^m beta_i ],

empty sums being zero. No nonunit denominator is inverted: C recurrence only through a=4m-1.

This is source-faithful algebraic research and a joint (i,a) carrier for an attempted creative telescoper; it does not establish a new Source-admitted Result, universal LIFT, or native X6/H0/B0 transfer.

## Executed evidence — original independent recurrence and 166 target primes

The executed standard-library Python file d25_four_port_jet_reduction_guard_20261030.py evaluates independently (i) original A216 ratio, (ii) original Gauss ratio, (iii) three harmonic-valuation strata, (iv) original frozen signed R triangular double sum, (v) original high-tail C and the bivariate J. Every prime p=13,19 (mod24), 13<=p<5000, was checked: 166 primes. All identities passed; no p in this finite range had a nonzero original second-digit residual. 161/166 had ALL FOUR addends in A nonzero, demonstrating that separately deleting source ports is incorrect in these finite witnesses. Finite coverage is not all-prime proof.

  p  | R_p | (Y0,Y1,F)    | (K0,6XW1,6Y_low W0,X²,J) | total mod p
  13 |   0 | (0,0,8)      | (1,12,0,4,9)             | 0
  19 |  12 | (3,18,10)    | (6,7,5,7,13)             | 0
  67 |  21 | (15,62,29)  | (3,22,43,36,30)         | 0
 373 | 196 | (197,212,252)| (127,227,188,203,1)    | 0

At p=373, original A_373=373 (mod 373³); signed R_373=196, F_373=252 and J_373=1 (mod373). The five nonzero outputs sum to 746=2*373. The p-adic source observer permits this scalar cancellation but not deletion of internal (i,a) branch identities.

## Remaining obligations, BRC and control status

BRC COMPOSE_APPLIED: declared carrier (p, original i,a indices, beta_i, C_a, valuation source 0/1/2, derivative/value and signed observer weights), with original A_p, R_p, F_p, J_p as separately typed readouts and allowed future composition. These arithmetic indices are NOT new spatial dimensions and do not identify ordinary Hesse/Gauss with a native H0/B0 operator.

Next precise mathematical obligation: directly prove or disprove the TWO target-class vanishing of B3 using an authentic *joint bivariate* finite WZ/CM transform/certificate connecting J_p to the four harmonic-jet ports, or supply a rigorously scoped no-go. Do NOT retry the proven impossible single-index rational Gosper ansatz or restate prior equivalent Hensel criteria as new target proofs.

Independent highest-priority native benchmark remains #1559 OPEN/PENDING_OWNER: fixed original-class p=373 H0/B0 divided-power [X]U modulo 139129, original module rank, real semilinear Frobenius/eta, signed odd Green/Hesse, kappa, and independent reproducible acceptance. This scalar arithmetic is NOT_RUN for that benchmark.

2026-10-30 15:02:50 UTC the Sites gateway returned research_authority_granted=false/write_relay_enabled=false, and native status/own checkpoint reported BACKEND_IDENTITY_CHECK_UNAVAILABLE, operation_sent=false. Existing own Research-lane bridge #6581 (2026-10-27) reported no local pending work and a historical service session but no execution authorization or claim; #6582 was REJECTED PREREQUISITE_NOT_SUCCEEDED. Those are historical, not current Source ownership. No role-bound mutation is attempted. The Site route requires a separately approved Site-bound backend client and secure credential; do not replay through another identity or maintenance lane. Source session/CLAIM/run/Result and checkpoint remain PENDING independent authorization/recovery. Frozen Source pin, P000 and original hourly scheduling/notifications are unchanged.
