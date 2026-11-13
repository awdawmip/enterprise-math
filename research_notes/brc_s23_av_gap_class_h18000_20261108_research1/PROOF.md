# S23/AV: exact horizon-18000 saturation by 55 translated gap classes

Date: 2026-11-08 (Asia/Shanghai). Status: AUTHOR_SIDE_EXACT_FINITE_CERTIFICATE; independent mathematical review pending.
Scientific input: immutable awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Predecessor lower theorem: research_notes/brc_s23_av_unimodular_first_entry_20261108_r1/FULL_SATURATION.md at immutable commit 85b53d06d6ba775e516c566c1d79828b6ca9bb1f.
Predecessor H=5000: research_notes/brc_s23_av_gap_class_h5000_20261108_r1/PROOF.md at immutable commit 83ec2f3dd0dfc5e24aa89578a927612b5a7c270c.

## Statement

For the explicitly defined two-point i.i.d. S23/AV auxiliary likelihood-sign observer with label laws P0=(1/2,1/4,1/4) and P1=(5/7,1/4,1/28), let T_h={10^i/7^s : 0<=i<=s<=h} and N(h) be the least common prefix length such that every open likelihood-ratio threshold cell from T_h has an attainable prefix ratio. Label 3 has unit likelihood ratio and permits padding. Then:

  N(h) = 2,455,069   for all integers 510 <= h <= 18,000.

This adds 13,000 horizons beyond H=5000 and replaces the old 29 displacement classes at H=5000 with a complete exact 55-class H=18000 certificate. The one exceptional class (79,431) covers 152,976,286 bounded cells with the existing witness (K,L)=(2074774,380295). All other 54 classes have maximum certified prefix length <=98,718. There are 162,027,001 distinct thresholds and 162,027,002 open cells.

## Mathematics

Put r=ln7/ln(10/7) and define E(k,ell)=k-r ell. Under the reflected log coordinate the threshold (v,j), with v,j>=0 and v+j<=H, has value t(v,j)=r v-j. A prefix with label-1 count k, label-4 count ell enters a gap between t(vL,jL)<t(vR,jR) iff

  0 < (k+jL)-r(ell+vL) < r(vR-vL)-(jR-jL).

Let dv=vR-vL and dj=jR-jL. Partition all actual adjacent threshold pairs by (dv,dj); for each class C let V=max_C vL, J=max_C jL, S=min_C(vL+jL). Any nonnegative integers K,L with

  K>=J, L>=V, K+L<=N+S,
  0<K-rL<r dv-dj

give a prefix witness (k,ell)=(K-jL,L-vL) of length <=N in every cell of C. This is an exact class-translation lemma; it requires no independence or stochastic approximation.

For the certificate take H=18000, N=2455069, Q=10^26 and the certified rational enclosure

  545569623581288298975349314 / Q < r <
  545569623581288298975349315 / Q.

The enclosure follows by 45 terms of the rational series 2 atanh(z)=2 sum_{j>=0} z^(2j+1)/(2j+1), with positive tail at most 2z^(91)/(91(1-z^2)), at z=1/3,1/9,1/15 and ln7=3 ln2-ln(8/7), ln(10/7)=ln(5/4)+ln(8/7). CHECK_CERT.py verifies the rational bounds independently via Python Fraction. Put LO and HI for the two integer numerators.

The C++ verifier constructs ALL M=(H+1)(H+2)/2=162027001 integer pairs (v,j). It sorts with the integer key R*v - 10^12*j, where R=5455696235812; the exact enclosure proves R/10^12 <= r < (R+1)/10^12. Then **every** consecutive key-sorted pair is validated in its true order by the strict adverse inequality

  (LO if dv>=0 else HI)*dv > Q*dj.

Positive strict inequalities at all consecutive pairs prove that the entire sorted order is the actual threshold order. This is an exhaustive finite proof of adjacency, not a floating-point guess. It yields 162027000 bounded cells, partitioned into 55 classes, with class counts summing exactly to 162027000.

The verifier checks for each class the sufficient integer conditions

  K*Q > HI*L,
  (K+dj)*Q < LO*(L+dv),
  K>=J, L>=V, K+L<=N+S.

The displacement (dv,dj)=(79,431) uses the existing exact unimodular witness (K,L)=(2074774,380295) with K+L=N and S=0; its class count is 152976286. Each other class uses the least K>rL at searched L, with all inequalities verified by integers; its maximum bound K+L-S is 98718. The extra outer-left interval (-infinity,-H) receives (k,ell)=(0,3300) because r*3300>H; the outer-right interval (rH,infinity) receives (k,ell)=(98203,0) because 98203>rH. Both lengths are <N. Padding by label 3 reaches common prefix n=N.

Thus N(18000)<=2455069. The predecessor exact theorem establishes N(510)=2455069, and T_h inclusions imply monotonicity, so N(510)<=N(h)<=N(18000) for 510<=h<=18000. Equality follows.

## Actual execution / reproducibility

Source VERIFY_GAP_CLASS.cpp was compiled with g++ 14.2.0:
  g++ -O3 -std=c++17 -Wall -Wextra -o verify VERIFY_GAP_CLASS.cpp
  ./verify 18000 > RUN_H18000.txt
Execution output: PASS_S23_AV_GAP_CLASS_UPPER H=18000 MAX_CERTIFIED_LENGTH=2455069 CLASSES=55 ELAPSED_SECONDS=32.2222.
The full 58-line transcript is RUN_H18000.txt; Python Fraction independent witness check is CHECK_CERT.py, which passed rational log bounds, all 55 emitted class witnesses, and both outer cells. The independent script does not reconstruct the threshold ordering: the exhaustive adjacent-pair scan is performed by the C++ verifier.
Local actual source SHA256=5f246053863d2c78eda0a54a3ee329d24aceb59ad78829cc68e2b931fe0372d5; log SHA256=2197797fff2bda105d1be2824df00dcf37ea51d372e72714f57964e8b860b7e3; independent script SHA256=c7637b87d81849ec661ce611d9de6e8e014ba8d0f6c87a01e86dc7f25e1dcff5. Re-running on another compiler/environment is a suitable independent computational audit.

## BRC observer scope and unresolved work

The branch carrier is the pair of joint counts (label 1 and label 4), with label 3 retained for padding. Future operation scope: the likelihood sign under up to h additional observations. This observer calculation is conditional on the declared S23/AV laws; no six-source, ten-label mother-model map or native X6 dynamical claim is asserted. The full-parameter four-observation minimax quantity delta_4 remains an independent problem.

Next useful unit: classify the 55 adjacent-gap displacement families symbolically and derive a uniform large-H guarantee without sorting O(H^2) thresholds; use the nonexception maximal certified length 98718 and the (79,431) near-resonance class to find the first H where the uniform class lift fails or an unseen narrower gap appears. Retain provenance and avoid assuming observations for H>18000 were enumerated.
