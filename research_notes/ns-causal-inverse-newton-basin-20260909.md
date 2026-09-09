# 因果线性化逆、临界轨道范数与可验证 Newton 收敛区域

Record-ID: `FINDING-EM-PDE-CAUSAL-INVERSE-NEWTON-BASIN-20260909`
Status: `TESTING / ORDINARY_PROOFS_AND_EXACT_FINITE_CERTIFICATE / NOT_INDEPENDENTLY_REVIEWED`
Researcher-ID: `EM-DIRECT-F00A51`
Research-Activity-ID: `RA-076944AE1950A916ACC95399`
Date: `2026-09-09`
Authority snapshots: global `202e522ea31357275ece35d7ddb9d9ffe3e1d99c`; EM `562df4628f1896bd0faca3706efbacdb78f189d0`.
Session: `local-ns-jitter-901c9f34161ce0f1` (locally assigned, not an authenticated platform ID).

## 0. Scope, question and attribution

Continue the user's selected NS/BRC research, under unchanged P000. All PDE assertions below concern the classical normalized torus T3=(R/2pi Z)^3, mean-zero real divergence-free fields and nu>0. The A3/FCC directions are the existing carrier for the native 120-degree project geometry; this is not a construction of the full native X6 dynamics. No claim of arbitrary-data regularity, mathematical acceptance, or historical priority is made.

The unfinished parent unit was a verified causal linearized inverse and a neighborhood in which successive Newton steps actually converge, rather than merely lower a residual. This note supplies an analytic all-mode inverse bound, a sharper trajectory product estimate, a quantitative contraction/Newton basin, and an explicit rank-three A3 example. A finite first response is used to certify the exact infinite-dimensional inverse response, not substituted for it.

Exact parents:
- `research_notes/brc-critical-lattice-gram-newton-20260909.md`, blob `cb6cddfd4b9a263b85ecc90f6b3bb194582e0a47`: C*=9503/1000 and Newton residual identity.
- `research_notes/ns-spectral-reference-20260909.md`, blob `e1b8d70548245a34ed18b34718f6bf404e2386a1`: Hermitian all-frequency growth bound.
- `research_notes/ns-jitter-initial-data-certificate-20260909.md`, blob `db3a72e6203398e3a876b31a0285679a21e6e131`: exact two-shell A3 heat residual.

General approximate-solution validation and Newton-Kantorovich theory predate this note. Primary context: Morosi-Pizzocchero, arXiv:1104.3832; van den Berg-Breden-Sheombarsing, arXiv:2305.08221; van den Berg-Breden, arXiv:2601.05146. The latter two concern rigorous parabolic integration, not an independent verification of this note's critical NS constants. The new result-specific composition is the running-energy norm, the full causal inverse, the coherent finite-response defect and the checked A3 convergence ball.

## 1. Norms and the inherited analytic inputs

Write Lambda=(-Delta)^(1/2), B(f,g)=P((f.grad)g), N(u)=-B(u,u). Set

H(w)=||w||_(Hdot^1/2)^2, D(w)=||w||_(Hdot^3/2)^2.

On the normalized torus the parent lattice proof gives

||B(f,g)||_(Hdot^-1/2) <= C* ||f||_(Hdot^1)||g||_(Hdot^1), C*=9503/1000. (1)

The inherited exact lattice checker was run unchanged in this turn. This checks its finite near field; the parent's cube/Riesz proof supplies the remaining infinite tail.

Let v be a prescribed locally smooth reference, bounded in Hdot^1/2 and square-integrable in Hdot^3/2 over [0,T], where T may be infinity. Let S_v be the Hermitian part of the critical linearized growth operator. Assume a verified nonnegative b(t) satisfies

<z,S_v(t)z> <= (nu/4)||Lambda z||_2^2+b(t)||z||_2^2,   int_0^T b(t)dt = B_T < infinity. (2)

This is a quadratic-form statement on ALL solenoidal Fourier modes. It may be obtained from the parent's finite-core/analytic-tail certificate or from

b(t)=M(v(t)),
M(v)=sum_(p!=0) |p|[1/2+sqrt(1+|p|)]|vhat(p)|. (3)

For clarity, M uses the smallest nonzero torus radius 1; no unchanged R3 formula is claimed.

## 2. Running-energy space and a factor sqrt(2) improvement

Put c=3nu/4. Define a Banach trajectory norm

||w||_X^2 = sup_(0<=t<=T) [H(w(t))+c int_0^t D(w(s))ds]. (4)

X consists of C_t Hdot^1/2 intersect L2_t Hdot^3/2 trajectories. At infinity use the supremum over finite t. This is a norm: at each t the expression is a squared norm in a direct-sum Hilbert space, and taking its square-root supremum preserves the triangle inequality. It is equivalent to the usual intersection norm and is complete. Let Y=L2_t Hdot^-1/2.

For E=||w||_X and q(t)=int_0^t D(w), (4) gives H(w(t))<=E^2-cq(t). Consequently

int_0^T H(w)D(w)dt <= E^2 q(T)-(c/2)q(T)^2 <= E^4/(2c). (5)

The last inequality is exactly (cq(T)-E^2)^2>=0. Thus the instantaneous critical mass and already accumulated dissipation cannot both independently use the full norm budget.

By (1), interpolation ||f||_1^2<=sqrt(H(f)D(f)), and Cauchy-Schwarz in time,

||B(f,g)||_Y^2
 <= C*^2 int sqrt(H(f)D(f)H(g)D(g))dt
 <= (C*^2/(2c))||f||_X^2||g||_X^2.

Therefore

boxed: ||B(f,g)||_Y <= C_B ||f||_X||g||_X,  C_B=C*/sqrt(2c). (6)

Bounding sup H and int D separately gives C*/sqrt(c); (6) improves that particular trajectory bound by sqrt(2). This is a proved norm-level factor, not a claim about a universal optimal NS constant.

## 3. Full causal inverse, with no small-background assumption

Define

D_v h = h_t+nu Lambda^2h+B(v,h)+B(h,v). (7)

For h(0)=0 let G_v g solve D_v h=g. Pairing with Lambda h and applying (2) gives

H'(h)/2+c D(h) <= b H(h)+||g||_-1/2 sqrt(D(h)).

Young yields

H'(h)+cD(h) <= 2bH(h)+||g||_-1/2^2/c. (8)

An integrating factor gives, for each t,

H(h(t))+c int_0^t exp(2 int_s^t b)D(h(s))ds
 <= exp(2 int_0^t b)H(h(0))+(1/c)int_0^t exp(2 int_s^t b)||g(s)||_-1/2^2ds. (9)

Since b>=0, all weights on the left are at least one. Therefore

boxed: ||G_v g||_X <= L||g||_Y, L=exp(B_T)/sqrt(c). (10)

With nonzero initial datum delta, the analogous solution obeys

||h||_X <= exp(B_T) sqrt(||delta||_1/2^2+||g||_Y^2/c). (11)

These estimates are uniform in a Fourier cutoff. Existence is not assumed: solve the finite linear Galerkin equations with the prescribed v, apply (8)-(10), and pass to a weakly convergent subsequence on each finite time interval. The linear coefficients are known and locally smooth. The bilinear estimate (6) bounds B(v,h),B(h,v) in Y, and h_t lies in L2 Hdot^-1/2. The Hilbert-triple continuity theorem supplies h in C Hdot^1/2; uniqueness follows from (8) with zero data. Consistency gives the solution on [0,infinity) when the stated global bounds hold. Thus (10) is an actual causal inverse, not a formal finite matrix inversion.

No commuting-time-matrices, diagonalizability, or pointwise spectral-stability assumption is used. A large reference is allowed, but its actual certified integral B_T enters L.

### Finite computation can certify the entire inverse tail

For any finite approximate response h_tilde with correct zero initial data define its FULL linear defect

e = D_v h_tilde-g.

Then exactly h_tilde-G_vg=G_ve, and

boxed: ||h_tilde-G_vg||_X <= L||e||_Y. (12)

If v and h_tilde are finite Fourier/exponential-polynomial packets, e includes all out-of-core products. It has finite computable support although the exact inverse need not. Repeated feedback into arbitrarily high modes is controlled by (10), not discarded. For a reference of Fourier radius P and an approximate response of radius L0, immediate convolution outputs through L0+P must be included. Time-discretization and source-tail defects must also be included when present.

## 4. A quantitative nonlinear basin and Newton convergence

Let f_v=v_t+nu Lambda^2v+B(v,v), and delta=u0-v(0). Let h0 be the EXACT linear response D_v h0=-f_v, h0(0)=delta. Choose a certified eta>=||h0||_X. It can be obtained from (11) or more sharply from (12) plus a finite response norm.

Put Q_v(f,g)=G_v B(f,g). From (6),(10),

||Q_v(f,g)||_X <= alpha||f||_X||g||_X,
alpha=L C_B=C*exp(B_T)/(sqrt(2)c). (13)

The complete error equation is equivalent to

w=h0-Q_v(w,w). (14)

No nonlinear terms have been omitted. If

boxed: 4alpha eta<1, (15)

let r_-=(1-sqrt(1-4alpha eta))/(2alpha), with the continuous trivial interpretation when alpha=0. The map in (14) maps the closed ball of radius r_- into itself and has Lipschitz constant 2alpha r_-<1. Hence it has a unique fixed point in that ball. More generally any r with eta+alpha r^2<=r and 2alpha r<1 is a valid certified ball.

The fixed point solves the FULL NS equation. It belongs to X together with v, hence int ||u||_6^4 <= C sup H(u) int D(u)<infinity. For smooth initial data the classical Prodi-Serrin continuation interface gives smoothness up to every finite endpoint, and globally if T=infinity. This is a restricted a posteriori sufficient theorem, not an all-initial-data statement.

### Exact Newton iterations really converge in this region

Set F(w)=w-h0+Q_v(w,w), w0=0, and

w_(n+1)=w_n-[I+Q_v(w_n,.)+Q_v(.,w_n)]^(-1)F(w_n). (16)

The inverse is a Neumann inverse whenever 2alpha||w_n||_X<1. To avoid assuming that the iterates stay in the ball, use the scalar majorant

phi(t)=eta-t+alpha t^2, t0=0,
t_(n+1)=t_n+phi(t_n)/(1-2alpha t_n). (17)

For (15), t_n increases to r_-. The exact quadratic remainder

F(w+d)-F(w)-DF(w)d=Q_v(d,d)

proves inductively ||w_n||<=t_n and ||w_(n+1)-w_n||<=t_(n+1)-t_n. Hence every inverse in (16) exists and Newton converges. If r is any above certified ball and w* the fixed point, then

boxed: ||w_(n+1)-w*||_X <= alpha/(1-2alpha r) * ||w_n-w*||_X^2. (18)

Moreover each updated causal inverse is controlled without restarting the proof:

||G_(v+w_n)||_(Y->X) <= L/(1-2alpha r). (19)

Thus the inverse-neighborhood hypothesis left open in the parent is supplied in this explicit basin. The theorem concerns exact Newton operations; implementing each operation requires a validated linear solve or an inexact-Newton error analysis. The present executable does NOT pretend to have run an infinite-dimensional Newton solver.

## 5. Fully checked rank-three A3 example on an infinite time interval

Set nu=1 and amplitude a=1/10. Use positive wavevectors

k1=(1,1,0), k2=(1,0,1), k3=(0,1,1), k4=(2,-2,0).

For each k select the coordinate unit vector e(k) at its zero coordinate and define the unit positive curl eigenvector

h_+(k)=[e(k)+i k cross e(k)/|k|]/sqrt(2).

Set uhat0(kj)=a h_+(kj), uhat0(-kj)=conj(uhat0(kj)), and all other coefficients zero. The four directions are A3/FCC root lines; the first three span rank three. Every initial coefficient has positive helicity, but no preserved-helicity assumption is made for the full solution.

Let v1 be the unit-amplitude heat flow. At actual amplitude a the reference is v=a v1. Define unit packets

n2=N(v1), (partial_t+Lambda^2)v2=n2, v2(0)=0,
n3=-B(v1,v2)-B(v2,v1).

Exact unchanged inherited Fourier convolution yields 8 initial packets, 12 n2 packets, 20 v2 packets, and 130 n3 packets. All complex interference and resonant t^m factors are retained. The previous known coefficient is rechecked:

cR=int ||n2||_-1/2^2
 =3sqrt(14)/245+7sqrt(10)/250+sqrt(6)/20
 =0.2568344745231463... . (20)

The new exact linear-defect action is

c3=int ||n3||_-1/2^2
 =17sqrt(42)/202836480+13sqrt(34)/84272400+sqrt(26)/346112+11/43200
  +9449sqrt(10)/17280000+757223sqrt(14)/1452124800
  +321119sqrt(6)/316108800+325286597sqrt(2)/46942156800
 =0.0162392455002545489998521307687... . (21)

The full reference residual is f_v=-a^2 n2. Take h_tilde=a^2 v2. Its COMPLETE linearized defect is

D_v h_tilde+f_v=-a^3 n3. (22)

This is not the nonlinear residual of v+h_tilde; the additional quadratic term B(h_tilde,h_tilde) is handled by (14), not silently omitted.

The pure heat energy estimate and c=3/4<=1 imply

||h_tilde||_X <= a^2 sqrt(cR),
||h0-h_tilde||_X <= L a^3 sqrt(c3). (23)

Therefore eta may be taken as a^2 sqrt(cR)+L a^3 sqrt(c3), rather than L a^2 sqrt(cR).

### Fully rational certificate

From (3), with mA=6sqrt(2)[1/2+sqrt(1+sqrt(2))] and mB=4sqrt(2)[1/2+sqrt(1+2sqrt(2))],

B_infinity=a(mA/2+mB/8)<523/500,
exp(B_infinity)<57/20.

Exact square-root enclosures and a positive Taylor remainder for exp prove

sqrt(cR)<507/1000,
sqrt(c3)<16/125,
L<33/10,
alpha<128/5,
eta<11/2000. (24)

Choose the rational ball r=7/1000. Then

4*(128/5)*(11/2000)=352/625<1,
r-11/2000-(128/5)r^2=307/1250000>0,
2*(128/5)r=224/625<1. (25)

Consequently this smooth initial datum has a global full NS solution and

boxed: sup_t [||u(t)-v(t)||_1/2^2+(3/4)int_0^t||u-v||_3/2^2ds] <= (7/1000)^2. (26)

The reference is not an exact NS flow: (20)>0, and the inherited nonlinear source contains opposite-helicity output. Thus this is not a single-shell heat solution or a helical-decimated equation.

The fixed-point contraction factor on this ball is <=224/625=0.3584. Exact Newton convergence follows from Section 4. The checker computes six scalar majorant values; it does not compute six full PDE Newton iterates.

### What improves and what is NOT claimed

Using only the raw bound eta_raw=L a^2 sqrt(cR), the corresponding quantity 4alpha eta_raw is >82731/50000>1 (decimal about 1.696). That sufficient contraction test fails. The finite coherent first-response estimate (23) succeeds with (25). Hence the computational preconditioning makes a real difference in THIS inverse-norm contraction test. This is not a claim that every earlier NS criterion fails for the example, or that these data are historically new global solutions.

The all-time error estimate improves from a formal 'linear solve assumed' to an actual certified inverse plus a nonlinear convergence region. No proof is given that arbitrary initial data can be brought into this region.

## 6. BRC typing and transferable content

Retain output frequency, parent identity, generator rate, time-polynomial degree, helical/polarization labels and complex amplitude until coherent sums and Gram integration are complete. The common (k,rate,power) observation is safe for the declared linear heat/product operations, not a license to erase hidden provenance for all future dynamics.

REUSE_APPLIED: T0_BRC and T6_OPERATION_SAFE_QUOTIENT at their typed observer boundaries; parent spectral quadratic-form and exact residual identities.
REUSE_EXECUTED: unchanged `inherited_fourier.py`, SHA256 `ac6a0a34994c85832bde55e38e195e9552df308906f1a4c4460d3dbdafb1db59`; unchanged prior lattice and Newton algebra checkers.
EXTEND_EXISTING_TOOL: critical reference certification -> causal inverse defect certification -> Newton basin. No new top-level accepted toolbox family or Foundation promotion is claimed.

The Banach-space part transfers to any system with the verified bilinear inequality, the quadratic-form bound and the appropriate local/continuation theorem. Equal-diffusivity MHD has the inherited direct-sum interface, but this turn does not newly certify a numerical MHD example. Neither Gram positivity nor a local descent step alone implies arbitrary-data convergence.

## 7. Verified frontier and next exact unit

Completed: all-mode causal inverse existence/bound; error certificate for a finite linear response including out-of-core products; running-energy product improvement; uniform Newton inverse neighborhood; explicit global A3 ball with exact rational margins.

Remaining: an implementable inexact Newton scheme whose discretization residuals are certified at every step, and sharper phase-sensitive inverse bounds extending the certifiable region. Window gluing must carry the actual error, not reset it. The arbitrary-data NS problem remains unclosed; this note supplies one rigorous convergence basin, not a universal algorithm.

Primary context checked on 2026-09-09:
- https://arxiv.org/abs/1104.3832 (established a posteriori NS control).
- https://arxiv.org/abs/2305.08221 (validated parabolic integration, Newton-Kantorovich).
- https://arxiv.org/abs/2601.05146 (2026 rigorous integration using approximate linearization).
