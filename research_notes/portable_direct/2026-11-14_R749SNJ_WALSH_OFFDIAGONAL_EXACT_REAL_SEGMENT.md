# R749SNJ — Exact off-diagonal Walsh minimax on a real interval

Date: 2026-11-14. Frozen scientific pin: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Status: author-side exact rational proof and fully reproducible all-real-parameter certificate; NOT_REVIEWED. Continues R749SNI (the left endpoint), R749SNH (the right endpoint), and R749SNG's diagonal results. This is an auxiliary finite Walsh observation model; no native signed-Port/X6/V29/V39 correspondence is asserted.

## Statement

Let G=(F_2)^4, chi_m(x)=(-1)^popcount(m&x), retain moments indexed by B={3,5,6,7,9,10,11,12,13,14}, and fix m3=t=1/2, m12=s, with all other eight retained moments equal to zero. Let F_(t,s) be the exact fiber of compatible probability laws. For total variation TV(mu,q)=sum_x |mu(x)-q(x)|/2, define

  rho(t,s)     = min_(q probability law) max_(mu in F_(t,s)) TV(mu,q),
  rho_cal(t,s) = min_(q in F_(t,s)) max_(mu in F_(t,s)) TV(mu,q).

For EVERY REAL s in [1/4,1/3],

  rho(1/2,s) = 7/16 - s/8,

and

  rho_cal(1/2,s) =
    { 1/2 - s/3  if 1/4 <= s <= 3/10,
    { 2/5        if 3/10 <= s <= 1/3.

Thus the exact calibration penalty is

  { 1/16 - (5/24)s     if 1/4 <= s <= 3/10,
  { s/8 - 3/80        if 3/10 <= s <= 1/3.

It is strictly positive except at s=3/10, where rho=rho_cal=2/5. At the endpoints the penalty equals 1/96 (s=1/4) and 1/240 (s=1/3). NOTE: The first penalty expression is equivalently (3-10s)/48; the second is (10s-3)/80.

## Exact fiber and symmetry reduction

Write A=chi3, D=chi12, AD=chi15, P=chi1, AP=chi2, Q=chi4, DQ=chi8. Every fiber law has the unique five-parameter form

  mu_(s,h,u,v,w,z)(x)
   = [1+(1/2)A+sD+hAD+uP+vAP+wQ+zDQ]/16,

subject to sixteen nonnegative masses. The fiber is nonempty and full-dimensional in (h,u,v,w,z) for the stated s. Translational averaging over independent P/Q sign flips reduces all unrestricted minimax decoders, without changing the value, to

  q_(tau,sigma,eta)(x)=[1+tau A+sigma D+eta AD]/16.

Calibrated symmetric decoders have tau=1/2, sigma=s.

## Explicit affine centers proving the upper bounds

For the unrestricted problem, for the WHOLE interval choose

  tau(s)=(5/2)s-1/4,
  sigma(s)=3/8-s/4,
  eta(s)=(5/4)s-3/8.

For calibrated decoders use

  eta_L(s)=(5/3)s-1/2 on [1/4,3/10],
  eta_R(s)=s-3/10 on [3/10,1/3].

Each resulting decoder is a nonnegative probability law, and the calibrated decoders lie in their exact fibers. The accompanying exact checker verifies the TV inequality over every source distribution in each continuous parameter segment, using the following finite joint-polytope argument.

Introduce six joint variables (s,h,u,v,w,z), impose 16 atom inequalities and two interval endpoint inequalities s>=lo, s<=hi. Each is a bounded full-dimensional six-polytope. Every vertex is the unique solution of six independent tight inequalities. For each interval, enumerate ALL C(18,6)=18564 potential active-facet combinations using integer Bareiss elimination with an interval-specific exact common-denominator scaling. For a fixed affine decoder q(s), the function TV(mu_(s,coeff),q(s))-r(s) is convex on the joint polytope because mu, q, r are affine. Its maximum occurs at a vertex; therefore verifying <=0 at every joint vertex establishes the upper bound for EVERY REAL s in the interval.

The exact run found:
- Free segment [1/4,1/3]: 9536 nonsingular, 496 feasible bases, 86 different joint vertices, 30 tight, zero failures.
- Calibrated left [1/4,3/10]: 9536 nonsingular, 496 feasible bases, 86 different joint vertices, 22 tight, zero failures.
- Calibrated right [3/10,1/3]: 9536 nonsingular, 432 feasible bases, 88 different joint vertices, 24 tight, zero failures.

The accompanying standard-library Python checker uses Fraction throughout. The preceding floating-point exploratory LP selected candidates but is not relied on in the proof.

## Universal affine witness families and lower bounds

Let E_f={3,5,7,9,11,13,14,15}. For every s in [1/4,1/3], choose the feasible source coefficient family

  W_f(s)=(h,u,v,w,z)=(0,s-1,-1/2,-s,-s).

All sums of A,D,AD over E_f vanish, so q(E_f)=1/2 for every invariant decoder q. Exact substitution yields

  mu_Wf(E_f)-q(E_f)=7/16-s/8.

The masses of W_f(s) are affine in s and nonnegative at both endpoints, hence nonnegative throughout the interval. This proves the unrestricted minimax lower bound.

For calibrated lower bounds use two feasible affine source families

  W_+(s)=(s+1/2,s-1/2,s-1/2,0,0),
  W_-(s)=(s-1/2,s-1,s-1,1/2-2s,1/2-2s).

They are probability laws throughout [1/4,1/3]; checking the atom inequalities at the two endpoints suffices by affinity.

On the LEFT segment set
  E_+={0,3,5,6,9,10,12,15},
  E_-={1,2,3,7,11,13,14,15}.

For every calibrated invariant q_(1/2,s,eta),

  L_+ = mu_W+(E_+)-q(E_+)=(1+2s-2eta)/4,
  L_- = mu_W-(E_-)-q(E_-)=(5-6s+2eta)/8.

Their nonnegative convex combination is

  (1/3)L_+ + (2/3)L_- = 1/2-s/3.

On the RIGHT segment keep E_+ above, and take
  E_3={3,7,11,13,14,15} for W_-.

Then
  L_3=mu_W-(E_3)-q(E_3)=(7-2s+2eta)/16,
  L_+=mu_W+(E_+)-q(E_+)=(1+2s-2eta)/4,

and

  (4/5)L_3+(1/5)L_+=2/5.

TV dominates every event difference, and a maximum dominates each convex combination. This proves both calibrated lower bounds. The finite joint-polytope certificates above prove their matching upper bounds.

## Continuation, evidence and research boundary

This result supplies a complete continuous parameter segment containing two earlier certified special points and a new exact zero-penalty transition at s=3/10. It does not imply zero loss from deleting all unretained source information: even at the crossing the optimal prediction error is 2/5. The next natural unit is the neighboring non-diagonal two-dimensional region, especially the location of the s=3/10 transition curve when t varies, or a certified native future-observer mapping.

Reproduce with:
  python research_notes/portable_direct/R749SNJ_WALSH_OFFDIAGONAL_REAL_SEGMENT_EXACT_CHECK.py

Compare stdout JSON with R749SNJ_WALSH_OFFDIAGONAL_REAL_SEGMENT_RESULTS.json. Scientific proof status is author-side exact, independent review NOT_REVIEWED. P000, true native X6 dimensions and source/future observer distinctions remain intact.
