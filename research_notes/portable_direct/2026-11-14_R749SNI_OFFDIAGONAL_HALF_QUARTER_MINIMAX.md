# R749SNI — Exact non-diagonal Walsh minimax at (1/2,1/4)

Date: 2026-11-14. Status: author-side exact theorem and reproducible rational certificate, NOT_REVIEWED.
Frozen science: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Earlier exact frontiers: R749SNG at PR #2309, and R749SNH at PR #2319 (scientific commit f307cb07ef317d344860c6475e0a513e5e7bee08).
Scope: auxiliary four-bit Walsh source model; no native X6/V29/V39 signed-Port lift asserted.

## Theorem

Set G=(F_2)^4 and chi_m(x)=(-1)^popcount(m & x).
Retain B={3,5,6,7,9,10,11,12,13,14}. Let F_(t,s) be all probability laws on the 16 elements with moment m_3=t, moment m_12=s and the other eight B moments zero. Write TV(mu,q)=(1/2) sum_x |mu(x)-q(x)|. Define

rho(t,s) = min_{q in Delta(G)} max_{mu in F_(t,s)} TV(mu,q);
rho_cal(t,s) = min_{q in F_(t,s)} max_{mu in F_(t,s)} TV(mu,q).

For t=1/2, s=1/4,

  rho(1/2,1/4) = 13/32,
  rho_cal(1/2,1/4) = 5/12,
  rho_cal-rho = 1/96.

The fiber is nonempty and the assertions concern every compatible source law, not a sample.

## Exact source and decoder parametrizations

Abbreviate A=chi_3, D=chi_12, AD=chi_15, P=chi_1, AP=chi_2,
Q=chi_4, DQ=chi_8. These seven characters give the exact five-parameter fiber

  mu_(h,u,v,w,z)(x)
    = [1+(1/2) A+(1/4) D+h AD+u P+v AP+w Q+z DQ]/16 >= 0.

The 16 nonnegativity conditions are necessary and sufficient, with automatic sum 1. The zero-vector five-tuple is strictly feasible: each atom is at least 1/64. The feasible coefficient region is a bounded full-dimensional five-polytope.

Translations flipping P and/or Q independently, without changing A,D, preserve the fiber. Averaging any decoder over these translations does not enlarge its supremal TV loss, by convexity and symmetry. Consequently one may minimize over

  q_(tau,sigma,eta)(x) = [1+tau A+sigma D+eta AD]/16 >= 0.

For calibrated minimax, set tau=1/2 and sigma=1/4.

## Universal upper bounds

Two explicit centers are

  q_free = q_(3/8,5/16,-1/16),
  q_cal  = q_(1/2,1/4,-1/12).

Both are nonnegative probability laws, and q_cal belongs to F_(1/2,1/4).
For every compatible mu,

  TV(mu,q_free) <= 13/32;
  TV(mu,q_cal)  <= 5/12.

The complete exact certificate is the accompanying Python standard-library program. It enumerates all C(16,5)=4368 five-facet sets, finds 3008 nonsingular bases, 256 feasible bases and 42 distinct vertices. It checks both TV bounds with Fraction arithmetic at all 42 vertices (free equality at 14, calibrated equality at 6). Every vertex of a bounded full-dimensional five-polytope lies on five linearly independent supporting facets; all possibilities have been examined. TV against a fixed center is convex in mu, so the verified vertex maxima imply the upper bounds for every real law in the fiber.

## Universal lower bound for unrestricted decoders

Choose the genuinely compatible law Wf with (h,u,v,w,z) =
(0,-3/4,-1/2,-1/4,-1/4) and event

  Ef={3,5,7,9,11,13,14,15}.

All three character sums sum_Ef A, sum_Ef D, sum_Ef AD vanish. Therefore every invariant decoder has q(Ef)=1/2, while mu_Wf(Ef)=29/32. Since TV dominates every event difference,

  TV(mu_Wf,q_(tau,sigma,eta)) >= 29/32-1/2 = 13/32.

The averaging argument extends the lower bound to unrestricted decoders. Together with q_free this proves rho=13/32.

## Universal lower bound for calibrated decoders

Take two compatible source witnesses and events:

  W1=(3/4,-1/4,-1/4,0,0),
  E1={0,3,5,6,9,10,12,15};

  W2=(-1/4,-3/4,-3/4,0,0),
  E2={1,2,3,7,11,13,14,15}.

For every calibrated invariant decoder q_(1/2,1/4,eta), direct character summation gives

  L1 = mu_W1(E1)-q(E1) = 3/8-eta/2,
  L2 = mu_W2(E2)-q(E2) = 7/16+eta/4.

A nonnegative combination eliminates eta:

  (1/3) L1 + (2/3) L2 = 5/12.

The maximum of the two event differences dominates their convex combination, and TV dominates each event difference. Hence every calibrated decoder has worst-case TV at least 5/12. The center q_cal attains this bound. Thus rho_cal=5/12, with positive gap 1/96.

## Independent scope and next question

This is an exact special point in the auxiliary Walsh-source observation fiber and a new contrast with the earlier R749SNH point (1/2,1/3), where the gap was 1/240. The two results establish distinct positive calibration costs but do not by themselves determine an intervening two-variable transition curve. The next discriminating unit is to find a rationally certified segment in the line t=1/2, s in [1/4,1/3], including any breakpoints in the optimizing centers and dual event supports. Another independent task is an actual native signed-Port/future-observer correspondence satisfying the frozen P000 and joint-source constraints.

Reproduction: Python 3 standard library, run
python research_notes/portable_direct/R749SNI_OFFDIAGONAL_HALF_QUARTER_EXACT_CHECK.py
and compare stdout JSON against R749SNI_OFFDIAGONAL_HALF_QUARTER_RESULTS.json.
No floating-point numerical optimizer is used in the certificate. The earlier numerical exploratory LP is not part of the proof.
