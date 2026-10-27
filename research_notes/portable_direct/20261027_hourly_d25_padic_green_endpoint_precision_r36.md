# D25/LIFT R36 — Integral p-adic finite Green lift and sharp endpoint-precision law

Date: 2026-10-27 (Asia/Hong_Kong). Author-side portable mathematics of TASK_RESEARCH lane chatgpt-research-hourly-enterprise-math-20260923. Maintenance lane chatgpt-hourly-enterprise-math-20260921 is separate. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, parent D25/LIFT/JT2 OPEN. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 retained separately from mutable control.

Evidence: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. This is an all-digit extension of earlier R27/R28 finite-field results and a new p=37 second-digit obstruction, not a duplicate claim of the mod-p theorems. No native CLAIM/open, Source checkpoint, original H0/B0 experiment, formal Result, Driver review or acceptance.

## Consumed facts and declared carrier

R27 proves the W/S full Picard–Fuchs source intertwiner over F_p, including the cutoff coefficient; R28 proves a finite-field Green inverse and endpoint adjoint. R34/R35 provide a genuine W/S same-index p-adic unit transfer but leave the unchanged-input cross-index WZ bridge open. This unit asks for the higher-precision integral source map and a proved endpoint information rule.

Fix any prime p=6m+1>=7. Let O=Z_(p), V_m=O[X] of degree <m and G_m=X O[X] of degree <=m. Use theta=X d/dX and R27's original operators

~~~
L_W=theta(theta+1/6)(theta+1/3)-X(theta+2/3)^3,
L_S=theta(theta-1/12)(theta+1/6)(theta+5/12)-X(theta+1)(theta+2/3)^3,
a_r=((2/3)_r)^3/((7/6)_r(4/3)_r r!),
h_r=(4/3)_r r!/((11/12)_r(17/12)_r)     (0<=r<m),
A_t=t(t+1/6)(t+1/3)                    (1<=t<m).
~~~

All these strict-rank a_r, h_r, A_t are p-units; integer denominators are p-units. No singular r=m a_m or h_m is introduced. Retain W/S labels, rank, finite-boundary port and p-adic precision in the BRC carrier.

## Theorem A: full integral W/S source transport

Define H_m(f)_r=h_r f_r (0<=r<m) and K_m(g)_t=t h_(t-1) g_t (1<=t<=m). Then

~~~
                      L_S H_m = K_m L_W                 (A)
~~~

holds exactly over O and therefore modulo every p^N, including X^m. Both H_m and K_m are invertible over O.

Proof: for t<m the defining exact rational recurrence is
(t-1/12)(t+5/12)h_t=t(t+1/3)h_(t-1).
Compare independently the f_t and f_(t-1) coefficients in each source. For t=m the f_m terms vanish by truncation, and the remaining f_(m-1) coefficients have precisely the ratio m h_(m-1). Every diagonal factor is a p-unit. This establishes the integral lift without inferring the open W/S scalar congruence.

## Theorem B: exact p-adic Green inverse with corrected endpoint

For f=sum_{r<m}f_r X^r, g=L_W f and z_r=f_r/a_r, exact rational algebra gives

~~~
g_t=A_t a_t(z_t-z_(t-1))                  (1<=t<m),
g_m=c_p z_(m-1),
c_p=-(m-1/3)^3 a_(m-1)
   =(a_(m-1)/8)(1-p/3)^3   in O^x.       (B1)
~~~

The endpoint factor is c_p, not R28's mod-p representative a_(m-1)/8. Thus L_W:V_m->G_m is an O-linear isomorphism, with

~~~
z_(m-1)=g_m/c_p,
z_r=g_m/c_p-sum_{t=r+1..m-1}g_t/(A_t a_t),   f_r=a_r z_r. (B2)
~~~

Given p-integral observation weights v_r and prefixes
Q=sum_{r<m}v_r a_r, Q_(t-1)=sum_{r<t}v_r a_r,
the full-source adjoint is

~~~
ell_v(f)=(Q/c_p)g_m
        -sum_{t=1..m-1} Q_(t-1)g_t/(A_t a_t).             (B3)
~~~

Proof: the exact a_r Pochhammer recurrence gives every interior B1 identity. At t=m, f_m=0 yields the displayed c_p. Backward telescoping proves B2. Substitute B2 into ell_v(f) and interchange finite sums for B3. The required lift of the endpoint inverse is

~~~
1/c_p=(8/a_(m-1))(1-p/3)^(-3)
     =(8/a_(m-1))[1+p+2p^2/3]        (mod p^3).         (B4)
~~~

## Theorem C: sharp minimal endpoint digits for declared observers

Suppose every interior residual g_1,...,g_(m-1) is retained modulo p^N, N>=1, and g_m is separately coarsened. Set t=min(N,v_p(Q)), with v_p(0)=infinity. For ell_v(f) modulo p^N on ALL inputs, the necessary and sufficient endpoint information is exactly g_m modulo p^(N-t); t=N means no endpoint digit. For finitely many declared future observers ell_(v^(j)), the exponent is

~~~
                   N-min_j min(N,v_p(Q_j)),
      Q_j=sum_{r<m}v^(j)_r a_r.                         (C)
~~~

Sufficiency follows from B3 and v_p(c_p)=0. Necessity holds for arbitrary (even nonlinear) output reconstruction: B2 makes g_m independent of all interior g_t. Choose two actual inputs with identical interiors but endpoint values separated by p^s. When s<N-t their observed values differ by a nonzero multiple of p^(s+t) modulo p^N. The least Q_j valuation proves the family formula. This proves a scoped BRC observer-factorization test rather than a generic right to discard source data.

## Genuine p=37 source certificate: safe mod 37, unsafe mod 37^2

Use exactly R28's original finite-field W-high/S-mid weights, now lifted to O:

~~~
v_r=C_m(2r+1)2^r-D_m(8r+13/3)9^r h_r,
C_m=3*216^(2m)*((2m)!)^5/(4m+1)!,
D_m=2*2304^(2m)*((2m)!)^4/(2m+2)!,
Q=ell_v(a)=U_p-M_p.
~~~

For p=37, m=6, direct rational evaluation reduced modulo 37^2=1369 gives

~~~
C_m=62; D_m=240; a_5=762; h_5=1045;
U_37=1056; M_37=1019; Q=37;
c_37=678; Q/c_37=1258=37*34;
m*h_5=794; [X^6]L_S H_m(a)=315.
~~~

For the unchanged homogeneous input f=a all five interior W sources are EXACTLY zero and g_6=c_37=678 mod1369. But ell_v(a)=37 mod1369, while zero input has the same interior residuals and observation 0. Hence an endpoint-free reconstruction (of any functional form) works at this first digit but fails at the second. The minimal repair for this scalar observer at p^2 is ONE digit of the genuine endpoint. The S endpoint agrees independently: 794*678=315 mod1369. No input-modifying observer, extra native dimension, or unproved cross-index WZ cancellation is used.

## Verification, limitations, and continuation

A Python 3 standard-library exact modular checker evaluated all 80 primes 7<=p<1000, p=1(mod6), at modulus p^3, with three independent deterministic input families per prime. It checked the complete L_S H_m=K_m L_W source (including X^m), Green inverse, and full adjoint. Independent Fraction/factorial computations were compared at p=7,13,19,37,43,67,181. Every check passed. The universal statements follow from the displayed algebra, not finite enumeration.

BRC COMPOSE_APPLIED: source label, arithmetic rank, exact p-valuation, unit jet, observer/future-operation family, cutoff boundary and declared p^N observation are separately retained. Auxiliary rank is not a native Enterprise X6 axis; P000 and ACTIVE worldview remain unchanged.

The immediate next executable scientific unit is the family of rank-jet observers ell_v(theta^j f). For the p=37 exception find the first j for which Q_j=sum r^j v_r a_r becomes nonzero modulo 37 and give the resulting sharp source-information certificate. Then investigate the genuine unchanged-input R23 low-half p^2-divided W/S discrepancy using B3 at p-adic precision, together with R34/R35 and the R28 endpoint. Preserve p=181, the p=13(mod24) distinct S port, six fixed-z=2 Hasse J/E ports and infinity/high-high sources. Original-class H0/B0, [X]U mod p^2, eta/kappa, native p373 experiment and independent Driver review remain distinct mother-target obligations.