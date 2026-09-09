# Residual-driven inner refinement: a certified third finite Navier–Stokes correction

Record-ID: FINDING-EM-PDE-ADAPTIVE-INNER-20260909
Status: TESTING / ORDINARY_PROOFS_AND_EXACT_FINITE_CHECKS / NOT_INDEPENDENTLY_REVIEWED
Researcher-ID: EM-DIRECT-F00A51
Research-Activity-ID: RA-076944AE1950A916ACC95399
Date: 2026-09-09
Session: local-ns-jitter-901c9f34161ce0f1 (locally assigned, not a platform-authenticated ID).
Read authority: global 9a284373b128dfb6a03f49996bc22cf9e53e632b; EM 141f8e547192b6ae9448c614664cc5023eca3ecd. Unique-create target refreshed at EM 79024a66e2c5f9d89d72d2cee1b0697ae3ffc0bd.

## 0. Scope and recovery

Continue the user's explicit NS/BRC question under unchanged P000. The PDE is classical incompressible, unforced, normalized 2pi-periodic 3D NS with real, divergence-free, mean-zero data. A3/FCC directions are the inherited effective carrier, not a construction of complete native X6 dynamics. No arbitrary-data regularity, historical priority, accepted tool admission or Foundation promotion is claimed.

The previous inexact-Newton work has already been published at research_notes/ns-inexact-newton-error-ledger-20260909.md, blob 0e0ac50c2055ba6e3a3f8e7e47658fc05806e43f. Its seventh activity event exists; do not duplicate it under an older pending path. The parent's full causal inverse and global ball are in research_notes/ns-causal-inverse-newton-basin-20260909.md, blob 32678f3cc52733af6b2ebe81dfbd390b91e41f0b.

This note constructs ONE further finite outer correction with THREE successively tested inner refinement levels. The first two fail a specified linear-defect tolerance; the third passes. The resulting full-time trajectory error is below 5e-9. This is improved approximation of the same previously certified solution, NOT an enlargement of the regular initial-data class.

## 1. Inherited analytic interface

Set nu=1, Lambda=(-Delta)^(1/2), B(f,g)=P((f.grad)g), N(f,g)=-B(f,g), and H=partial_t+Lambda^2. Use

||w||_X^2=sup_(t>=0)[||w(t)||_(Hdot^1/2)^2+(3/4)int_0^t||w(s)||_(Hdot^3/2)^2 ds],
Y=L2([0,infinity);Hdot^-1/2).

The parent proves the all-mode bounds

||G_v||_(Y->X)<=L=33/10,
||G_v B(f,g)||_X<=alpha||f||_X||g||_X, alpha=128/5,
||B(f,g)||_Y<=C_B||f||_X||g||_X, C_B=194/25.

The last bound follows from C*=9503/1000 and C_B^2*(3/2)>C*^2. The known solution u is in the parent ball ||u-v||_X<=r*=7/1000. For a current reference U with ||U-v||_X<=s and alpha(s+r*)<1, the parent exact residual identity gives

||u-U||_X <= L ||R(U)||_Y/[1-alpha(s+r*)],
R(U)=H U-N(U,U).                                           (1)

No old error is reset to zero by (1). It recertifies distance to the same already-certified full solution.

For any zero-trace correction h, define its FULL linear defect e=D_U h+R(U), D_U=H-N(U,.)-N(.,U). Then

R(U+h)=e-N(h,h).                                           (2)

The sign in (2) is consistent with N=-B; the norm bound is ||e||_Y+C_B||h||_X^2. Out-of-core modes and unenumerated higher products must not be dropped.

## 2. The initial field and recovered two-step reference

Let A=1/10. At positive wavevectors (1,1,0),(1,0,1),(0,1,1),(2,-2,0), use unit positive-helicity coefficients h_+(k)=(e+i k cross e/|k|)/sqrt(2), where e is the unit axis corresponding to the zero component of k. Add conjugate negative coefficients. The first three frequencies have rank three. Initial support has eight modes and two radii; nonlinearity and opposite-helicity generation are nonzero.

For unit amplitude let v1 be its heat flow and define

n2=N(v1,v1), H v2=n2, v2(0)=0;
n3=N(v1,v2)+N(v2,v1), H v3=n3, v3(0)=0.

The recovered reference is U2=A v1+A^2 v2+A^3 v3. Define

n4=N(v1,v3)+N(v3,v1)+N(v2,v2),
n5=N(v2,v3)+N(v3,v2), n6=N(v3,v3).

Its exact full residual is

R(U2)=-A^4 n4-A^5 n5-A^6 n6.                               (3)

The parent certifies ||U2-v||_X<=2599/500000 and ||u-U2||_X<19/1000000, with v=A v1. These facts are consumed, not rediscovered.

## 3. Inner refinement keeps the missing terms, not just the order label

Write T_i h=N(v_i,h)+N(h,v_i). Construct zero-initial-value heat responses

H w4=n4,
H w5=g5:=n5+T_1 w4,
H w6=g6:=n6+T_2 w4+T_1 w5.                                (4)

For m=4,5,6, use d_m=sum_(j=4)^m A^j w_j. These are finite APPROXIMATE causal linear solves at the FIXED reference U2; none is relabeled as an exact Jacobian inverse.

Define k6=n6+T_2 w4, m7a=T_3 w4+T_2 w5, m7=T_1 w6+m7a. Direct expansion of D_(U2) d_m+R(U2) gives

e4=-A^5 g5-A^6 k6-A^7 T_3 w4,
e5=-A^6 g6-A^7 m7a-A^8 T_3 w5,
e6=-A^7 m7-A^8(T_2 w6+T_3 w5)-A^9 T_3 w6.                (5)

Every amplitude order is present in (5). Heat rates, time-polynomial powers, output frequencies, complex phases and polarizations are retained inside its coefficients. We do not infer that truncating at a higher order must improve the result; each candidate is checked against the same complete-defect tolerance.

## 4. Exact packet computation and all-mode remainder bounds

The unchanged current coefficient backend is research_notes/ns-inexact-newton-error-ledger-20260909/exact_packets.py, SHA256 0ffab938427c4827700876fbd9f9c371a59d07aa89edefd5a6447071ec48d25d. Its exact coefficient field is Q(sqrt(2),i).

Measured packet counts are

v1:8, v2:20, v3:196;
n4:804, w4:948;
g5:4060, w5:4406;
g6:13834, w6:14456;
m7a:32402, m7:41838.

The complete m7 has 1064 output frequencies. It is a computed finite source, not a truncation of a presumed infinite solution.

For any finite source F, its exact Y Gram is

sum_(k!=0) |k|^-1 sum_(r,m),(s,n) Re< F_(k,r,m),F_(k,s,n)> (m+n)!/(r+s)^(m+n+1). (6)

Every same-output cross term in (6) is retained. Final scalar norm comparisons use outward rational square-root intervals; decimal displays below are not proof inputs.

Computed norm readouts:

||n4||_Y = 0.0379237856307507909...,
||g5||_Y = 0.0131664881354398207...,
||k6||_Y = 0.00027495682135857016...,
||g6||_Y = 0.004909974680703672...,
||m7a||_Y = 0.00013596306947201396...,
||m7||_Y = 0.0018234712277439443... .

Rigorous convenient upper bounds are

b2:=||A^2 v2||_X <=507/100000,
b3:=||A^3 v3||_X <=16/125000,
b4:=||A^4 w4||_X <9481/2500000000,
b5:=||A^5 w5||_X <26333/200000000000,
b6:=||A^6 w6||_X <491/100000000000.                          (7)

For (7), the zero-trace forced heat energy inequality gives ||H^(-1)F||_X<=||F||_Y; its use is valid because 3/4<=nu=1. Thus b4,b5,b6 are obtained directly from (4),(6), not from time samples.

The unenumerated eighth- and ninth-order terms in e6 have full Y bounds

T8=2 C_B(b2 b6+b3 b5)=6.479106464e-10,
T9=2 C_B b3 b6=9.7540096e-12.                              (8)

The measured seventh-order source satisfies

A^7||m7||_Y <1.82348e-10.

Consequently

||e6||_Y <52500791/62500000000000000
           =8.40012656e-10 <1e-9.                         (9)

All possible frequencies in (8) are covered by the bilinear bound; their contribution is positive and explicitly budgeted, not declared zero.

## 5. An actually executed tolerance-based stopping decision

Set the target linear-defect norm to 1e-9. Apply (5) and the exact Grams, with triangle and reverse-triangle inequalities for the unenumerated remainder. The resulting certified decisions are

m=4: 1.2e-7 <||e4||_Y<1.4e-7 : REFINE;
m=5: 4.6e-9 <||e5||_Y<5.2e-9 : REFINE;
m=6: ||e6||_Y<8.40012656e-10 : ACCEPT.                     (10)

Thus the program tests genuinely different achieved accuracies. The first two candidates actually exceed the target, not merely fail an overly weak upper-bound test. This is one implemented inner refinement policy: cancel the lowest remaining amplitude-order source, then certify ALL remaining orders. It is not an optimal spatial-basis selector or a universal inner solver.

The target is stricter than the inherited sufficient quadratic forcing budget

(256/33)*(19/1000000)^2 =2.800484848...e-9.

Hence the accepted finite third outer correction meets that quadratic-accuracy requirement. Merely repeating the earlier fixed three-percent tolerance would not establish this.

## 6. The new full-time approximation error

Set h=d6 and U3=U2+h. From (7),

||h||_X <157159/40000000000=3.928975e-6,
||U3-v||_X <208077159/40000000000=0.005201928975.

Equation (2), with the entire self-interaction included, yields

||R(U3)||_Y <19196051394257/20000000000000000000000
              =9.5980256971285e-10.                       (11)

Applying (1) gives

||u-U3||_X <211156565336827/45842041216000000000000
             =4.606177206...e-9 <5e-9.                    (12)

In particular the EXACT full NS solution satisfies

sup_(t>=0)[||u(t)-U3(t)||_(Hdot^1/2)^2+(3/4)int_0^t||u-U3||_(Hdot^3/2)^2 ds] <=(5e-9)^2. (13)

This is a critical trajectory bound over all time and all Fourier modes, not a pointwise velocity error. The established initial-data class is unchanged. Subsequent initial-value solutions or a fourth outer Newton step are not claimed to have been computed.

If the next outer step uses the inherited quadratic ledger with E=5e-9, its sufficient future forcing budget is (256/33)*(5e-9)^2. This is a prospective test, not an executed result.

## 7. Arithmetic optimization and BRC reuse

To make larger coherent sources practical, the new implementation accumulates convolution in integers after extracting common coefficient denominators. The Leray output is formed using (|k|^2 I-k k^T) with a final denominator |k|^2 D_A D_B. This is exactly the inherited convection/projection law. It does not alter coefficients, introduce floating point arithmetic or discard outputs.

The Gram implementation similarly extracts common coefficient and heat-kernel denominators separately at each output, accumulates integer numerators, and only then forms exact fractions. Cross-rate and cross-time-power terms remain present. For final irrational weights 1/|k| it uses outward rational intervals and outward rounding to a common rational grid, avoiding denominator growth without losing enclosure.

Lower-degree convolution and Gram outputs were checked against the unchanged source implementation. All five used forced-heat equations and their zero traces are checked. Larger expressions were constructed in staged executions and checked by exact coefficient identities and outward scalar bounds. The accompanying verifier reconstructs the same finite calculation; computational optimization is an extension of the existing result-specific tool, not a new accepted BRC family.

Reuse: T0_BRC and T6_OPERATION_SAFE_QUOTIENT are REUSE_APPLIED; the parent's exact backend and full causal inverse are REUSE_EXECUTED / REUSE_APPLIED; integer accumulation, residual-based stopping and the full third correction are EXTEND_EXISTING_TOOL. Primitive six-axis/120-degree semantics are not modified. A3 support is an initial structure, not an invariant Fourier cutoff.

## 8. Attribution and remaining problem

General inexact Newton forcing and residual control are established: Dembo–Eisenstat–Steihaug (1982), DOI 10.1137/0719025; Eisenstat–Walker (1996), DOI 10.1137/0917003. A posteriori NS validation: Morosi–Pizzocchero, arXiv:1104.3832. Space-time least-squares formulations in natural dual norms also predate this note; see Hinze–Kahle–Stahl, DOI 10.1002/pamm.70037. These are context, not independent verification or priority for the present constants.

Next useful work is selective graph-residual refinement and phase-sensitive inverse bounds that reduce cost or enlarge the initial-data basin. The present success does NOT show that every initial datum reaches a certified basin, nor that increasing amplitude order always converges. No arbitrary-data NS/MHD global regularity theorem is claimed.
