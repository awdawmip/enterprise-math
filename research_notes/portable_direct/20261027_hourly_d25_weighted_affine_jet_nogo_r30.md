# D25/LIFT R30 — uniform affine rank-jet obstruction after exact W/S source intertwining

Date: 2026-10-27 Asia/Hong_Kong. Own TASK_RESEARCH logical conversation: chatgpt-research-hourly-enterprise-math-20260923. Do not use control-maintenance chatgpt-hourly-enterprise-math-20260921 or the separate chatgpt-research-onhour-enterprise-math-20260923 Research lane. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen SCIENTIFIC Source pin c47e13e4aba0e006366f989d6334d443f6333ae3. D25/LIFT/JT2 stays OPEN.

**AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING / SYNC_DEBT**. This external finite-field result is not a native CLAIM/open/checkpoint, Result, independent review, original CM experiment or full supercongruence proof.

## Scope and inputs

Consume without recredit: R23's source-labelled low-half W/S defect plus W-high U_p; R25's invertible unweighted Hadamard kernel h_r and the p=13(mod24) one-index weighted S hole; R27's full inhomogeneous PF source intertwiner L_S H_m=K_m L_W including X^m; R28's finite Green inverse and source adjoint; R29's original S weight-zero valuation ladder. The independent on-hour lane's half-cutoff and E3 work is separate. The new question is whether the exact Hadamard source map, after transport, makes the **two genuinely different weighted output functionals** equal on every finite-field input by one affine rank-jet alpha+beta*theta. This is an all-input observer statement, not the original scalar equality on the actual hypergeometric solution.

For a prime p=6m+1, let V_m=F_p[X] of degree <m, theta=X*d/dX. Define (strict range 0<=r<m):

~~~
h_r=(4/3)_r*r! / ((11/12)_r*(17/12)_r), h_0=1.
W_r=(2r+1)*2^r.
S_r=(8r+13/3)*9^r*h_r.
W(f)=SUM_(r<m) W_r*f_r;   S(f)=SUM_(r<m) S_r*f_r.
~~~

These are the R25–R28 true W/S weighted port coefficients after transporting the S coefficients onto W's free carrier through H_m. The nonzero global constants C_m,D_m can be absorbed into an affine jet's parameters, without changing existence. Signed weights, W versus S provenance, strict cutoff, endpoint X^m, and original p-adic high/low origins remain distinct.

## Theorem A — universal failure of affine weighted observer transfer

For **every prime p=6m+1>=13** there are NO alpha,beta in F_p with

~~~
W(f)=SUM_(r<m) (alpha+beta*r)*S_r*f_r    for ALL f in V_m.       (A)
~~~

For p=13, m=2 and S_0=13/3=0 while W_0=1; this directly uses R25's source hole. For p>=19, m>=3, apply (A) to the three independent inputs 1,X,X^2. Exact rational coefficient data are:

~~~
(h_0,h_1,h_2)=(1,192/187,129024/124729).
(W_0,W_1,W_2)=(1,6,20).
(S_0,S_1,S_2)=(13/3,21312/187,212502528/124729).
det [ S_r | r*S_r | W_r ]_(r=0,1,2)
  = 2692858746624 / 23324323
  = 2^8 * 3 * 3506326493 / (11^2 * 17^2 * 23 * 29).             (B)
~~~

The denominator prime factors are 5 mod 6, and therefore p-units for every allowed p. The numerator's only prime factors are 2,3,3506326493. The final integer is **prime**, 5 mod 6: the accompanying executed exact checker exhausts every integer trial divisor 2<=d<=floor(sqrt(3506326493))=59214. Thus the determinant cannot vanish in any target F_p for p>=19. Equations (A) for three independent coefficients are inconsistent. QED.

At the exceptional smallest target p=7, m=1, S_0=2 and W_0=1 mod7; alpha=4 works on its one-coordinate carrier. Hence the >=13 hypothesis is sharp for this affine free-carrier claim.

Theorem A forbids only the specified low-order **global source-observer** equivalence; a nonlocal WZ certificate, low-half compensation, X^m boundary repair, higher-rank jets or the accidental equality on one actual f remain open.

## Theorem B — weighted post-Hadamard rank-jet order must grow

For primes p=19 mod24, all S_r (0<=r<m) are units by R25. Set R_r=W_r/S_r. Its exact recurrence, obtained from the already-proved h recurrence, is:

~~~
R_r/R_(r-1)
 = (2r+1)*(24r-11)*(12r-1)*(12r+5)
   / [216*r*(2r-1)*(3r+1)*(24r+13)]          (1<=r<m).             (C)
~~~

Let P_p in F_p[t] be the unique interpolating polynomial deg<m satisfying P_p(r)=R_r for every r<m. Its minimal degree d satisfies

~~~
max(0,m-5) <= d <= m-1.                                           (D)
~~~

In particular, a fixed-order polynomial in theta, independent of p, cannot transport the whole true weighted W observer onto the S observer for arbitrarily large primes p=19 mod24.

Proof: define

~~~
A(t)=216*t*(2t-1)*(3t+1)*(24t+13),
B(t)=(2t+1)*(24t-11)*(12t-1)*(12t+5).
Q(t)=A(t)*P_p(t)-B(t)*P_p(t-1).
~~~

(C) forces Q(1)=...=Q(m-1)=0. For degree d of nonzero P_p, the leading term of Q is (31104-6912)*lc(P_p)*t^(d+4)=24192*lc(P_p)*t^(d+4). Its coefficient is a p-unit for p>=19 (prime factors 2,3,7), so deg Q=d+4. If d<=m-6, then deg Q<=m-2 although Q has m-1 distinct roots, contradiction. Standard interpolation proves d<=m-1. The 0 lower bound is trivial because R_0=3/13 is nonzero in this residue class. QED.

For p=13 mod24, R25 already identified r_0=(p-13)/24 with S_(r0)=0 while W_(r0) is nonzero: no polynomial rank-jet on the S output alone, of ANY order, represents W on the entire free carrier. This is a consumed fact, not a newly credited theorem.

## Exact evidence, typed implications and continuation

The accompanying Python 3 standard-library verifier was ACTUALLY EXECUTED: complete integer trial division through 59214 for the fixed prime numerator; rational rederivation of (B); nonzero modular determinant for all 148 primes p<2000, p=1 mod6 with m>=3; and recurrence/interpolation-degree checks for every one of the 37 p=19 mod24 primes in that range. The all-prime statements rely on the algebra plus the finite exact primality certificate, not on prime sampling. Examples det(B) mod p: p=19:18, 37:9, 61:51, 181:14, 373:199, 733:238. Finite interpolation examples (p,m,d): (19,3,2), (43,7,6), (67,11,10), (211,35,34), (739,123,122); no universal assertion d=m-1 follows from this census.

**BRC COMPOSE_APPLIED / SOURCE-LABELLED OBSERVER AUDIT**: distinguish W/S coefficients, finite ranks, weighted moment jets, GF(p) projection, residuals and X^m cutoff. Even an invertible transport of PF source equations does not preserve the specified scalar observation under a finite low-order rank-jet. It is a typed external coefficient algebra, not a native Enterprise X6 spatial or P000 theorem; no worldview or frozen pin is changed.

2026-10-27 native status (v0.6.11) gave research_authority_granted=false. This host exposes native em_status but no callable recovery_status; historical **own** recovery bridge #6571 and canonical continuation #6572/#6573/#6574 remain read evidence, not Source authorization. The original R29 continuation request researchhourly-20261027-0829-continuation-r29 was rechecked by its unchanged request_id; receipt returned CONTROL_REQUEST_NOT_FOUND after its prior CONTROL_QUOTA. Source-native current winning CLAIM/open/checkpoint is not established; no session/Researcher mutation or maintenance-lane use occurred. Preserve the verified old Source checkpoint bytes/claims and both neutral staging archives; controller support enterprise-math#1558 owns the mismatch.

**Next precise research unit:** construct a truly nonlocal or source-augmented WZ/adjoint relation matching the exact p²-divided original low-half W/S difference to the genuinely W-sourced high-tail U_p (R23/R28), instead of equating the two weighted ports by a bounded jet. Retain p=13 mod24's missing weighted S port, p=19 mod24's low-half S valuation-two port, r=m source and distinct six fixed-z=2 Hasse J/E, positive infinity/high-high, left/right boundaries. Original native H0/B0, [X]U modp², semilinear Frobenius eta/kappa, p373 CM benchmarking and independent Driver review remain separately required. D25/LIFT/JT2 OPEN; no scheduler, phase, enablement or notification changes.
