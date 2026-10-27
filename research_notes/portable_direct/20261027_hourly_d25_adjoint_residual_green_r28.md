# D25/LIFT R28 — Exact finite Green inverse, adjoint source identity, and a sharp endpoint-only W/S no-go

Date 2026-10-27, Asia/Hong_Kong. This is continued *portable author research* of the independent TASK_RESEARCH lane chatgpt-research-hourly-enterprise-math-20260923 (not the control-maintenance conversation). Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7; frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. Mother D25/LIFT/JT2 OPEN.

Evidence: **AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY**. Not Source CLAIM/open/checkpoint, a native original-class Frobenius experiment, an all-prime W=S proof, a Result, or independent review.

## Specific new unit after R27

Consume without recredit the R23–R26 p²-reflected W/S source facts and R27's complete polynomial identity L_S H_m=K_m L_W. R27 transported ALL Picard–Fuchs source coefficients, including X^m. The new question is whether endpoint data is genuinely *necessary and sufficient* to reconstruct every finite-field input and to express the two distinct genuine rank-jet observers through source residuals. This gives a sharp test for any proposed endpoint-free WZ/adjoint shortcut, without ruling out compensating original low-half terms.

Let p=6m+1>=7, R=F_p, V_m=R[X]_(degree<m) and G_m=X*R[X]_(degree<=m). Write

~~~
L_W = theta*(theta+1/6)*(theta+1/3) - X*(theta+2/3)^3,
theta=X*d/dX.
a_0=1; a_r=((2/3)_r)^3 / ((7/6)_r*(4/3)_r*r!), 0<=r<m.
A_t=t*(t+1/6)*(t+1/3),  1<=t<m,
c=a_(m-1)/8 in R^x.
~~~

All a_r, A_t and c are nonzero in the actual strict finite field range; r=m is a singular UNEXTENDED coefficient of a, not an admissible additional input.

## Theorem 1 — full-source finite Green inversion, including the endpoint

The map L_W:V_m -> G_m is an R-linear ISOMORPHISM. If g=L_W f and z_r=f_r/a_r, then its exact inverse is

~~~
z_(m-1)=g_m/c,
z_r=g_m/c - SUM_(t=r+1..m-1) g_t/(A_t*a_t)  (0<=r<m-1),
f_r=a_r*z_r.                                             [1]
~~~

**Proof.** For 1<=t<m, the defining homogeneous recurrence of a gives

~~~
g_t=A_t*f_t - (t-1/3)^3*f_(t-1)
   =A_t*a_t*(z_t-z_(t-1)).
~~~

At t=m, truncation f_m=0 and the exact R24 endpoint valuation show

~~~
g_m=-(m-1/3)^3*f_(m-1)=(a_(m-1)/8)*z_(m-1)=c*z_(m-1).
~~~

The displayed inverse follows by backward finite telescoping; conversely these formulas reconstruct a unique f for every g in G_m. All denominators are units. At m=1 the interior sum is empty and the argument still applies. QED.

Using R27's exact invertible H_m and K_m, the distinct operator L_S is likewise an isomorphism on its truncated polynomial carrier, and its Green inverse is

~~~
                     (L_S)^(-1) = H_m*(L_W)^(-1)*(K_m)^(-1).    [2]
~~~

The S source is neither suppressed nor a new native-physics dimension; (2) is the exact source-coordinate change permitted by R27.

## Theorem 2 — full source-to-observer adjoint identity

For ANY source-labelled finite-field observation weights v_0,...,v_(m-1), define L_v(f)=SUM_(r<m)v_r f_r and the exact prefix moments

~~~
Q=SUM_(r=0..m-1) v_r*a_r,
Q_(t-1)=SUM_(r=0..t-1) v_r*a_r    (1<=t<m).
~~~

Then for every f in V_m with g=L_W f,

~~~
L_v(f) = (Q/c)*g_m
         - SUM_(t=1..m-1) [Q_(t-1)/(A_t*a_t)]*g_t.       [3]
~~~

Every summand records its original residual index; the X^m endpoint is never silently discarded.

**Proof.** Insert [1] into SUM v_r*a_r*z_r and reverse the finite double sum. The endpoint has coefficient Q/c and each interior residual g_t appears exactly for original ranks r<t, with coefficient -Q_(t-1)/(A_t*a_t). All terms are exact in R. Uniqueness of the adjoint representation follows from the isomorphism in Theorem 1. QED.

### Exact factorization/no-go criterion for endpoint-free observers

Let pi:G_m -> G_m/(R*X^m) retain only residual ranks 1,...,m-1. Then

~~~
ker(pi*L_W)=R*(SUM_(r<m)a_r X^r),  rank(pi*L_W)=m-1.
~~~

Consequently, L_v factors through the endpoint-deleted residual pi*L_W **if and only if Q=0**. If Q!=0, exactly one additional R scalar, g_m, repairs the loss; (3) constructs the unique linear repair, and an endpoint-free linear observer cannot reproduce L_v on the declared free input carrier. This does not ban nonlinear/nonlocal telescopers or extra genuine original sources.

**Proof.** The interior homogeneous recursion forces f_r=f_0*a_r, so the kernel is precisely the indicated one-dimensional span. A functional on V_m factors through a surjective linear quotient exactly when it annihilates its kernel. Here L_v(a)=Q. If Q!=0, [3] supplies the missing single scalar; rank-nullity proves minimality. QED.

## Genuine W/S observation port and exact p=181 obstruction

R24/R25's genuine weighted source totals, NOT the full original W/S p³ sums, are

~~~
U_p=C_m*SUM_(r<m)(2r+1)*2^r*a_r,
M_p=D_m*SUM_(r<m)(8r+13/3)*9^r*b_r,
b_r=h_r*a_r,
C_m=3*216^(2m)*((2m)!)^5/(4m+1)!,
D_m=2*2304^(2m)*((2m)!)^4/(2m+2)!.
~~~

For their free-carrier difference functional define

~~~
v_r=C_m*(2r+1)*2^r - D_m*(8r+13/3)*9^r*h_r.
Q=U_p-M_p.
~~~

Theorem 2 implies a **sharp equivalence**: a linear adjoint transfer from the *interior PF residuals alone* can represent the difference functional precisely when U_p=M_p in F_p. If U_p!=M_p, the unique transfer MUST include the original cutoff source with coefficient (U_p-M_p)/c. This is a quantified limitation of a specified proposed source interface, not of the original W=S conjecture.

Executed exact factorial/Pochhammer arithmetic gives:

~~~
p    m     U_p    M_p    U-M     endpoint coefficient (U-M)/c
13    2     10      7      3           9
19    3      9      3      6          17
37    6     20     20      0           0
181  30    152      0    152          55
373  62    266     92    174         341
733 122     67    174    626         210
~~~

At p=181, both the original R22 S-only aggregate T_181=0 and R25 S-mid M_181=0 occur, but U_181=152!=0. The explicit endpoint coefficient 55!=0 proves no universal endpoint-free *linear PF residual representation* can be valid across all target primes. It does NOT refute a full W/S bridge containing an exact low-half compensator; the open target is an all-prime p³ equality of DIFFERENT scalar series.

## Executed finite check and source limits

Standalone Python 3 standard-library checker: research_notes/portable_direct/20261027_hourly_d25_adjoint_residual_green_r28_check.py. Executed **PASS on all 148 primes p<2000, p=1(mod6)**. For three independently specified polynomial inputs at each prime it reconstructs ALL coefficients through the inverse [1], independently evaluates the exact adjoint [3], and compares the two true R24/R25 weighted-port sums; arithmetic is integer/Fraction modulo p. The all-prime theorems follow from the finite algebraic proofs above, not from finite enumeration. No native original-class experiment or independent review was run.

**BRC COMPOSE_APPLIED / OBSERVER-FACTORIZATION TEST.** The explicit carrier is V_m with W/S source tags, inverse residual G_m, strict r cutoff, true x^m source, field weights, exact prime valuations inherited from R23 and original k↔j indexing. The future operation includes PF, Hadamard, weighted readouts and the pi quotient. Theorem 2 proves the exact condition under which pi is safe for a *specified* observer, and a minimal scalar repair otherwise. No claim about native Enterprise X6 geometry or protected P000/worldview is made.

**NEXT precise action.** Use [3] as a source-aware WZ/adjoint design equation for the *genuine LOW-HALF p²-divided scalar discrepancy* in R23, and determine whether its independently declared low-half source produces exactly the missing endpoint Q/c. Preserve the p=181 exceptional S total and p=13(mod24) lost individual S port, separate six Hasse channels, positive-infinity/high-high terms, and original native H0/B0 + [X]U modp² + semilinear eta/kappa obligations. No inference that this PF finite-field certificate itself solves LIFT or realizes a native execution. This semantic unit awaits native registration/publication: REGISTER_PENDING / SYNC_DEBT, as current direct continuation was rejected by CONTROL_QUOTA and the original request readback was CONTROL_REQUEST_NOT_FOUND. Control support enterprise-math#1558 remains responsible; old session, staging and maintenance conversation unchanged. D25/LIFT/JT2 stays OPEN.
