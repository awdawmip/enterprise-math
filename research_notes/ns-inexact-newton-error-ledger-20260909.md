# 可验证的非精确 Newton 误差账本与两次完整 Fourier 修正

Record-ID: `FINDING-EM-PDE-INEXACT-NEWTON-ERROR-LEDGER-20260909`
Status: `TESTING / ORDINARY_PROOFS_AND_EXACT_FINITE_CHECKS / NOT_INDEPENDENTLY_REVIEWED`
Date: `2026-09-09`
Researcher-ID: `EM-DIRECT-F00A51`
Research-Activity-ID: `RA-076944AE1950A916ACC95399`
Session: `local-ns-jitter-901c9f34161ce0f1` (locally assigned; not a platform-authenticated session identifier).
Read authority: global `d89ea926ecc7db875336eecd0ab14d84a9540099`; EM `d40aa672623d6fc82af4cbb60964e6a628267e62`.
Parent: `research_notes/ns-causal-inverse-newton-basin-20260909.md`, current blob `32678f3cc52733af6b2ebe81dfbd390b91e41f0b`; immutable original commit `c26297984a9178e45235ca9226b673af8cd7805e`.

## 0. Scope and advance

The exact user-selected question is to continue the NS/BRC residual program by replacing ideal exact linearized solves with finite, certified inexact solves. P000 is unchanged. The PDE is the classical unforced incompressible NS equation on the normalized 2pi-periodic three-torus, for real, zero-mean divergence-free fields and viscosity nu>0. Its effective A3/FCC representation is not a derivation of complete native X6 dynamics. No arbitrary-data regularity or accepted Foundation promotion is claimed.

The parent supplies a full causal inverse and an explicit global contraction ball. This note adds a graph-residual error ledger, a quantitative inexact continuation rule, an amplitude-only pruning obstruction, and TWO ACTUALLY EXECUTED finite inexact updates for the parent's rank-three A3 datum. Subsequent high-precision adaptive PDE updates have NOT been executed. The sharper numbers below concern accuracy around this already-certified solution, not an automatically larger set of regular initial data.

Inexact Newton methods and forcing terms are established: Dembo–Eisenstat–Steihaug (1982), DOI 10.1137/0719025; Eisenstat–Walker (1996), DOI 10.1137/0917003. A posteriori NS validation: Morosi–Pizzocchero, arXiv:1104.3832. Validated parabolic integration: van den Berg–Breden–Sheombarsing, arXiv:2305.08221. These give attribution, not independent verification of this note. The contribution here is the explicit composition with the parent's critical causal norm and exact output/rate/power/phase packets.

## 1. Fixed reference and inherited bounds

Write B(f,g)=P((f.grad)g), N(f,g)=-B(f,g), Lambda=(-Delta)^(1/2), and

R(U)=U_t+nu Lambda^2 U+B(U,U).

Fix the parent's smooth reference v, with v(0)=u0. Put c=3nu/4 and

||w||_X^2=sup_(t>=0)[||w(t)||_(Hdot^1/2)^2+c int_0^t ||w(s)||_(Hdot^3/2)^2 ds],
Y=L2([0,infinity);Hdot^-1/2).

Use the full causal inverse G_v of

D_v h=h_t+nu Lambda^2h+B(v,h)+B(h,v), h(0)=0.

The parent proves all-mode bounds

||G_v g||_X<=L||g||_Y,
||Q(f,g)||_X<=alpha||f||_X||g||_X, Q=G_v B.

Bounds L and alpha may be independently rounded up; one need not reset alpha to the product of two separately rounded bounds. The parent also certifies a true full NS solution u=v+w_* with ||w_*||_X<=r_*. Its fixed-point equation is

w_*=h0-Q(w_*,w_*), h0=-G_v R(v).

The associated preconditioned residual is

F(w)=w-h0+Q(w,w)=G_v R(v+w).

All candidate corrections have zero initial value. Nonzero initial-data/discretization mismatches would require the parent's separate initial-trace term and may not be reset to zero.

## 2. Exact inexact-step identities

Let U_n=v+w_n be a finite reference and h_n a finite approximate correction. Define the FULL linear defect

e_n=D_(U_n)h_n+f_n, f_n=R(U_n), h_n(0)=0.

Set U_(n+1)=U_n+h_n. Bilinearity gives exactly

f_(n+1)=e_n+B(h_n,h_n).                                      (IN1)

There is no hidden truncation in this identity. In particular, measuring only a projected linear residual is insufficient: e_n includes outputs outside the numerical core as well as any time-approximation defect.

If eps_n>=||e_n||_Y and s_n>=||w_n||_X with 2alpha s_n<1, the full causal inverse at U_n exists and

||G_(U_n)||_(Y->X)<=L/(1-2alpha s_n).                       (IN2)

Proof: D_(U_n)=D_v+B(w_n,.)+B(.,w_n); precondition by G_v. The perturbation has X operator norm <=2alpha s_n, hence a convergent Neumann inverse. This is not an inference from a truncated spectrum.

Let E_n>=||U_n-u||_X. Put E=U_n-u. Quadratic expansion yields

D_(U_n)E=f_n+B(E,E).

Adding the inexact equation proves

D_(U_n)(E+h_n)=B(E,E)+e_n.

After preconditioning and (IN2),

||U_(n+1)-u||_X <= [alpha E_n^2+L eps_n]/(1-2alpha s_n).   (IN3)

Thus a valid next radius is the right side of (IN3). This estimate includes the true infinite response to the finite linear defect.

If eps_n<=theta_n||f_n||_Y, (IN1)-(IN2) also give the conventional residual recurrence

||f_(n+1)||_Y <= theta_n||f_n||_Y
 + C_B [L/(1-2alpha s_n)]^2(1+theta_n)^2||f_n||_Y^2,

where C_B is any valid X x X -> Y product bound from the parent. Fixed nonzero theta normally provides a linear forcing floor in this bound; quadratic convergence requires forcing accuracy to improve. No constant-3-percent forcing is relabeled as quadratic convergence.

## 3. Residual-based recertification of the current reference

An actual residual often yields a sharper error radius than accumulated step estimates. Since F(w_*)=0,

F(w_n)=E+Q(E,w_n)+Q(w_*,E), E=w_n-w_*.

Therefore, when alpha(s_n+r_*)<1,

||U_n-u||_X <= L||f_n||_Y/[1-alpha(s_n+r_*)].              (IN4)

This does not erase old error; it bounds the same already-certified solution using its full equation residual and the parent ball. A failed test is not evidence of singularity.

## 4. Quantitative inexact convergence within the known basin

Suppose E_start bounds the error at a certified starting reference and

R=r_*+E_start, d=1-2alpha R>0.

If each later finite solve is checked to satisfy

eps_n<=mu E_n^2,

then (IN3) gives

E_(n+1)<=K E_n^2, K=(alpha+L mu)/d.                       (IN5)

If K E_start<1, induction keeps E_n nonincreasing and ||w_n||_X<=R. Thus every next inverse is valid, and

E_n <= K^(-1)(K E_start)^(2^n)

for the chosen scalar radii. This is convergence with verified inexact solves, not with imagined exact solves.

In the numerical parent basin, L=33/10, alpha=128/5, r_*=7/1000. After the two updates below take E_start=1/50000. Then

1-2alpha(r_*+E_start)>16/25.

Choosing mu=alpha/L=256/33 gives the simple sufficient rules

eps_n <= (256/33) E_n^2,
E_(n+1) <= 80 E_n^2.                                     (IN6)

For example the successive conditional radius bounds begin 2e-5, 3.2e-8, 8.192e-14. They are consequences IF those future linear defects are certified; they are NOT reported as executed PDE iterates. Only the first two finite updates were run in this note.

Within an already-certified smooth reference neighborhood there is no mathematical obstruction to arbitrarily accurate finite linear solves: the inverse belongs to the parabolic graph space h_t in Y, h in L2 Hdot^3/2, with the prescribed trace. Finite Fourier fields with continuous piecewise-polynomial time coefficients are dense in that graph space (truncate time using vanishing energy at infinity, then truncate Fourier modes, smooth in time, and approximate the finite scalar components). D_U is continuous there under the parent's product bound. This gives existence of finite approximants with arbitrarily small defect, not a universal complexity bound or success guarantee outside the certified basin.

## 5. The two actual updates

Use nu=1 and the exact parent's eight-mode initial field with amplitude A=1/10 and unit positive-helicity coefficients on

(1,1,0), (1,0,1), (0,1,1), (2,-2,0)

plus conjugate negative frequencies. The first three vectors have rank three. The initial two radii are sqrt(2) and 2sqrt(2). All initial directions are A3/FCC, but later outputs are NOT restricted to them.

For unit amplitude let v1 be its heat flow and define

n2=N(v1,v1), (partial_t+Lambda^2)v2=n2, v2(0)=0;
n3=N(v1,v2)+N(v2,v1), (partial_t+Lambda^2)v3=n3, v3(0)=0.

The actually computed references and corrections are

U0=A v1,
h0=A^2 v2, U1=U0+h0,
h1=A^3 v3, U2=U1+h1.

These are finite inexact Newton steps, not exact Jacobian inversions. Their FULL measured linear forcing ratios below are both less than 3 percent.

Let

n22=N(v2,v2),
n4=N(v1,v3)+N(v3,v1)+n22,
n5=N(v2,v3)+N(v3,v2), n6=N(v3,v3).

Exact all-output computations verify

f0=-A^2 n2,
e0=-A^3 n3,
f1=-A^3 n3-A^4 n22,
e1=-A^4 n4-A^5 n5,
f2=-A^4 n4-A^5 n5-A^6 n6.                                (IN7)

The native exact packet key is (output k, positive heat rate sigma, integer time power m); complex vector coefficients carry phase and polarization. There are 8, 20 and 196 packets in v1,v2,v3; 804,1822,7138 in n4,n5,n6. After combining identical keys the complete f2 has 8284 packets.

All same-output/rate amplitudes are combined BEFORE squaring. For packets a_(k,sigma,m)t^m exp(-sigma t), the exact Y Gram uses

|k|^-1 (m+n)!/(sigma+tau)^(m+n+1).

Coefficients in this example lie in Q(sqrt(2),i). The executable specializes that coefficient arithmetic exactly, and checks the convolution/heat results against the unchanged inherited implementation. It does not approximate sqrt(2) in packet algebra. Only final norms use outward RATIONAL square-root bounds, verified by integer squaring.

Verified norm enclosures (decimal displays are rounded descriptions; JSON stores rational intervals):

||f0||_Y approximately 0.005067883922537555;
||e0||_Y approximately 0.0001274332982397244;
||f1||_Y approximately 0.0001274334759901937;
||e1||_Y approximately 0.000003792390596155351;
||A^6 n6||_Y <0.0000000003015193570561871.

The last full residual is bounded by

||f2||_Y <= ||e1||_Y+||A^6n6||_Y
 <0.000003792692115512408.

The e1 and degree-six Grams are exact separately; this last inequality uses triangle rather than evaluating their remaining cross-generation Gram. No term is set to zero. The full residual identity itself is independently checked against R(U2).

Rational interval arithmetic proves both

||e0||_Y < (3/100)||f0||_Y,
||e1||_Y < (3/100)||f1||_Y.

The parent's heat-response estimate gives

||U1-v||_X <=507/100000,
||U2-v||_X <=507/100000+16/125000=2599/500000.

Use rigorous residual bounds

||f1||_Y <51/400000,
||f2||_Y <381/100000000.

With the inherited L,alpha,r_*, formula (IN4) and exact rational comparison prove

||u-U1||_X <61/100000=0.00061,
||u-U2||_X <19/1000000=0.000019.                          (IN8)

These are full-time critical trajectory errors, not pointwise velocities, not sampled time errors, and not just low-mode discrepancies. The parent's heat-reference bound was 0.007. The new references are more accurate around the same certified solution; no claim is made that this alone expands the initial-data class.

## 6. Safe compression needs the graph residual, not the visible amplitude

If an approximate correction h is compressed to h-delta, its linear defect changes by exactly

e_new=e-D_U delta.

The admissibility test must therefore control the FULL norm of this new defect, or conservatively ||e||_Y+||D_U delta||_Y. Small ||delta||_X alone does not suffice.

An explicit heat-packet obstruction uses any nonzero solenoidal A3 single-shell phi with Lambda^2 phi=2phi. At nu=1 set, for integer N>=2,

delta_N(t)=N^(-1)(exp(-2t)-exp(-N^4t)) phi.

It has zero initial trace and ||delta_N||_X=O(N^-1). Nevertheless, even for the zero background,

D_0 delta_N=(N^4-2)N^-1 exp(-N^4t) phi,

||D_0 delta_N||_Y^2=(N^4-2)^2/(2N^6) ||phi||_(Hdot^-1/2)^2,

which diverges as N^2. Thus discarding a tiny-amplitude packet can erase a large linear equation error. Output, heat rate and time power remain operationally necessary coordinates. This is not a PDE singularity; it is a counterexample to an unsafe compression rule.

## 7. BRC reuse and remaining work

REUSE_EXECUTED: the parent's exact Fourier convection/Leray and forced heat implementation, SHA256 ac6a0a34994c85832bde55e38e195e9552df308906f1a4c4460d3dbdafb1db59, used unchanged as an oracle.
EXTEND_EXISTING_TOOL: exact coefficient-ring specialization for performance, full inexact linear-defect measurement, and scalar error ledger. The extension matches the inherited finite operations before larger calculations.
COMPOSE_APPLIED: the all-mode causal inverse and certified ball with standard inexact Newton error propagation.
NOT_APPLICABLE: replacing signed/complex branches with positive masses before coherent summation; pretending finite retained modes are the complete dynamics.

In the effective six-channel representation Phi=N^T/sqrt(2), NN^T=2I, the inherited compatible-subspace embedding is an isometry and commutes with Lambda, so these norm statements lift without creating extra independent velocity coordinates. All intermediate classical Fourier outputs are retained; the root directions are initial structure, not an invariant truncation.

Next: implement an adaptive inner solver/pruner that certifies (IN6) at every subsequent step, selecting packet refinements by their graph-residual contribution. The two measured 3-percent steps are a verified prototype, not a full high-precision nonlinear integration engine. Extending the initial-data basin, proving all-data global regularity, and historical novelty remain separate unsolved obligations.
