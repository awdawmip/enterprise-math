# Direction-preserving critical lattice bound and removal of the fixed-alpha NS certificate obstruction

Record-ID: FINDING-EM-PDE-ANGULAR-LATTICE-CERTIFICATE-20260910
Status: TESTING / ORDINARY_PROOF_AND_EXACT_FINITE_ARITHMETIC / NOT_INDEPENDENTLY_REVIEWED
Researcher-ID: EM-DIRECT-F00A51
Research-Activity-ID: RA-076944AE1950A916ACC95399
Session: local-ns-jitter-901c9f34161ce0f1 (inherited locally assigned conversation-continuation key, not a platform-authenticated identity)
Date: 2026-09-10
Read authority: GLOBAL_KNOWLEDGE c71e803f61e038ea8576b91d28d492bfc793c901; enterprise-math 16c8daad1e0f3db5c3399d5a085ccbd70f9d4476.

## 0. Exact task and scope

Continue the specified NS/BRC research from the previous dictionary-independent fixed-majorant obstruction. Do not repeat dictionary optimization: the unfinished unit is a smaller valid nonlinear-feedback bound. P000 and native 120-degree orthogonality remain unchanged. All PDE statements here concern the classical normalized torus T3=(R/2pi Z)^3, mean-zero real solenoidal velocity, nu>0. The A3 frequency carrier and six-channel representation are not a derivation of full native X6 dynamics.

This note proves a valid critical bilinear constant 7.605, replacing the preceding valid but weaker 9.503. It then reuses the unchanged all-mode causal-inverse and trajectory-contraction theorems to certify the previously obstructed amplitude 0.16 and a uniform interval of the fixed shape through amplitude 1/6. No arbitrary-data regularity, optimal constant, historical priority, or mathematical admission is claimed.

Inherited sources:
- research_notes/brc-critical-lattice-gram-newton-20260909.md: scalar lattice proof and C*=9.503.
- its certify_lattice_constant.py: Git blob 4551bd83edab7453bda993582eed098cb8073519; fetched by exact blob and executed unchanged.
- research_notes/ns-causal-inverse-newton-basin-20260909.md: all-mode inverse and running-energy trajectory product.
- research_notes/ns-orthogonal-response-barrier-20260910.md: Git blob 49ad4bb583d5b40d2d6378911245c1928b769f05, SHA256 5e9958c00594078257e2cf09f6c9caea2e0cd75954b38685d8b78ef2ac0c2964.
- its certify_joint.py: SHA256 a16b817cdc5cc46f96d447094c18fef14be8252b118e2d0435795970a9a81139.

General Fourier/Sobolev constant estimation and a posteriori PDE validation predate this work. Primary context: Morosi-Pizzocchero, arXiv:1007.4412 (a different, higher-order Sobolev inequality), arXiv:0709.1670 and arXiv:1104.3832. Those works do not independently verify the critical constant or example in this note.

## 1. Angular lattice-Gram theorem

Use normalized Fourier norms ||h||_s^2=sum_(k!=0)|k|^(2s)|hhat(k)|^2 and B(f,g)=P((f.grad)g). The first argument f is divergence free. Both arguments have zero mean. The second argument may also be divergence free, as in NS, but this is not needed for the estimate.

THEOREM. For f,g in Hdot^1,

||B(f,g)||_(-1/2) <= (1521/200)||f||_1||g||_1.                 (1)

The constant is valid, not sharp. It is independent of Fourier cutoffs and of the special A3 example.

For p+q=k, incompressibility yields fhat(p).q=fhat(p).k=fhat(p).P_p k. Hence

|fhat(p).q| <= |fhat(p)| |P_p k|,
|P_p k|^2=|p cross k|^2/|p|^2.

Set F_p=|p||fhat(p)| and G_q=|q||ghat(q)|. The Leray projection has norm at most one. Cauchy-Schwarz at each output k gives

|k|^-1 |Bhat(k)|^2 <= S_ang(k) sum_(p+q=k) F_p^2 G_q^2,

S_ang(k)=1/|k| sum_(p!=0,k) |p cross k|^2/(|p|^4|k-p|^2).   (2)

Summation in k leaves ||F||_2^2||G||_2^2. Thus it suffices to prove sup S_ang(k)<7.605^2. The earlier scalar majorant replaced |P_p k| by |k| before forming this Gram. This note keeps the direction dependence longer.

This is not an assertion that every interaction near 120 degrees vanishes: the angular factor in (2) is between p and the OUTPUT k. The separate equal-shell helical cancellation is not being used or silently extended here.

## 2. Exact near field, including both singular centers

Let K=|k| and P6={p in Z3:0<|p|<6}. Write a=|p|^2, b=|k-p|^2 and c=|p cross k|^2. The union |p|<6 or |k-p|<6 is bounded by

M6(k)=1/K sum_(p in P6,p!=k) c(a+b)/(a^2 b^2).              (3)

Overlap is counted twice; this only increases the nonnegative bound. The summand is the sum of the original term and its p <-> k-p image.

The unchanged scalar parent enumerates 894 points in P6 and 277 octahedral representative outputs 0<=k1<=k2<=k3, 0<|k|<13. For every representative, the new checker evaluates the rational numerator A(k)=K M6(k) and verifies

A(k)^2 < (19383/1000)^2 |k|^2.                              (4)

No floating point is used for acceptance. The largest near-field representative is (1,1,1), with display value 19.38218502849, below 19.383.

For K>=13, octahedral symmetry gives the exact moment laws

sum_(P6) sin^2(angle(p,k))/|p|^2=(2/3)A6,
sum_(P6) sin^2(angle(p,k))=(2/3)*894,
A6=sum_(P6)|p|^-2=67048852231/1012647636.

Since |k-p|>K-6,

M6(k) <= (2/3)[A6 K/(K-6)^2 + 894 K/(K-6)^4]
       <= 598671535129/40077477594 <19.383.                  (5)

Both functions of K decrease for K>6. The checker verifies the tensor moment identities by exact rational arithmetic. Equations (4)-(5) cover every integer output, not a sampled range.

## 3. Exact continuum angular moments

For m=0,1,2 define

I_m(k)=integral_R3 sin^m(angle(x,k))/(|x|^2|k-x|^2) dx.

Align polar coordinates with k, put mu=cos(theta), and scale radial distance by K. For -1<mu<1,

integral_0^infinity dr/(r^2+1-2r mu)
=(pi/2+arcsin(mu))/sqrt(1-mu^2).

The arcsin term is odd in mu. Consequently

I_m(k)=(pi^2/K) integral_-1^1 (1-mu^2)^((m-1)/2) dmu.

In particular,

I_0=pi^3/K, I_1=2pi^2/K, I_2=pi^3/(2K).                   (6)

All integrals are finite. Singular endpoints are understood through the integrable polar formulas. I_1 is evaluated exactly, not replaced by sqrt(I_0 I_2). That last improvement lowers an intermediate valid constant 7.682 to 7.605.

## 4. Analytic infinite-tail certificate with direction error retained

In the remaining sum, |p|>=6 and |k-p|>=6. For x in the unit cube Q_p around p, put delta=sqrt(3)/2 and a0=1+delta/6. Then

1/(|p|^2|k-p|^2) <= a0^4/(|x|^2|k-x|^2).                  (7)

Writing r=|p| and s=|x|, the normalized-direction difference obeys

|p/r-x/s|^2=[|p-x|^2-(r-s)^2]/(rs)
<=delta^2/[6(6-delta)].                                    (8)

Thus, with epsilon=delta/sqrt(6(6-delta)),

sin(angle(p,k)) <= sin(angle(x,k))+epsilon.

Integrate over each disjoint unit cube and enlarge the domain to R3. Using (6),

S_ang,far(k)
<= a0^4 K[I_2+2epsilon I_1+epsilon^2 I_0]
= a0^4[pi^3(1/2+epsilon^2)+4epsilon pi^2].                 (9)

The finite checker uses only rational upper parameters

delta <1351/1560,
epsilon <1561/10000,
pi <355/113.

The epsilon inequality is checked by squaring positive quantities. The pi bound is the same classical rational upper bound used by the parent. The resulting bound is

far <38.448262270190,
near+far <57.831262270190 <(1521/200)^2=57.836025.            (10)

This proves (1). The exact rational difference is stored in output/angular_constant.json. A simpler intermediate proof discarding far-field direction information gives C=8.518; using Cauchy-Schwarz only on I_1 gives C=7.682. Both intermediate inequalities are also checked.

## 5. Reuse of the full nonlinear trajectory theorem

For nu=1 set c=3/4 and

||h||_X^2=sup_t[||h(t)||_(1/2)^2+c integral_0^t ||h||_(3/2)^2],
Y=L2_t Hdot^-1/2.

The inherited running-energy identity gives

||B(f,g)||_Y <= C_ang/sqrt(2c) ||f||_X||g||_X.               (11)

If the unchanged all-mode linear inverse has bound ||G_v||<=L, the feedback bound becomes

alpha=L C_ang/sqrt(3/2).                                   (12)

The linear inverse itself does not become smaller merely because (1) improved. Its existing bound is kept. Only the bilinear factor in (12) is changed.

Let h0=G_v g be the exact first linear correction and let eta>=||h0||_X. The complete NS error satisfies w=h0-G_v B(w,w). If

eta+alpha r^2<r, 2alpha r<1,                               (13)

it has a unique fixed point in that trajectory ball. This includes all generated modes and all nonlinear feedback. The parent local/Prodi-Serrin continuation argument then gives smoothness for smooth data. T=infinity is allowed under the globally bounded reference/inverse assumptions verified in the example.

## 6. Executed A3 examples and the old obstruction

Use positive wavevectors k1=(1,1,0), k2=(1,0,1), k3=(0,1,1), k4=(2,-2,0), conjugates at negatives, and

h_+(k)=[e+i(k cross e)/|k|]/sqrt(2),

where e is the unit coordinate vector at the zero coordinate of k. Give each positive coefficient the same real amplitude a. This is exactly the inherited rank-three, two-shell shape. It is not a single-shell heat solution. Let v be its heat reference.

Reuse the explicit unit responses p2,p3 and trial d=a^2 p2+a^3 p3. Their supports are disjoint by the parent's integer-relation proof. The new checker re-executes the exact full-output packet operations and verifies that cross pairing is zero. With w0=3271/10000 and q0=16/125,

U(a)=sqrt(w0^2 a^4+q0^2 a^6),
||e||_Y=a^4 sqrt(c4),
eta <= U(a)+L(a)a^4 sqrt(c4).                              (14)

The exact radical c4=0.0014408187275118617... is recomputed from all outputs, not read as a floating-point assumption. Each trial has 216 packets; its complete linear defect has 772 packets at 144 frequencies. The parent time-maximum certificate is executed unchanged to verify w0; no time sampling is used.

A. a=4/25=0.16:
L=200630557/50000000=4.01261114 (unchanged),
alpha=311451679/12500000=24.91613432,
eta=84899757/10^10=0.0084899757,
r=13/1000.

Exact checks:
r-eta-alpha r^2=3739969999/12500000000000>0,
2alpha r=4048871827/6250000000<1.

Therefore ||u-v||_X<=0.013 for the full global NS solution. The old alpha0=31.13451998 and old exact-response lower bound ell=0.0082681778 still satisfy 4alpha0 ell>1. Nothing in that old conditional obstruction is retracted: its fixed-alpha hypothesis has deliberately changed. Relative to C_old=9.503 the valid constant decreased by 146/731, about 19.97264 percent, more than the parent's necessary 2.884617 percent target.

B. a=1/6:
L=2675157/625000=4.2802512,
alpha=2657803363/10^8=26.57803363,
eta=92307779/10^10=0.0092307779,
r=9/500=0.018.

Exact checks:
r-eta-alpha r^2=3948480097/25000000000000>0,
2alpha r=23920230267/25000000000<1.

Thus this endpoint is also globally certified. For a>=0 the reference envelope b_a=(a M(v_unit)-1/4)_+, its integral, L(a), and the right side of (14) are all nondecreasing. The endpoint constants therefore certify EVERY amplitude in [0,1/6], with the common radius 0.018 and the appropriate reference v_a. This interval extension is a proved monotonicity argument, not interpolation between two successful samples.

At 0.16 and 1/6 the corresponding smooth real solenoidal zero-mean off-family initial perturbations can have critical norm up to 430497/10^10 and 213039/10^10 respectively. The checker uses less than half the inclusion margin and the unchanged homogeneous response bound sqrt(3/4)L. Such perturbations need not lie on A3 lines or have one helicity. These remain small neighborhoods, not arbitrary data.

## 7. BRC typing, reuse, and limits

Carrier: labeled input frequencies (p,q), output k, complex vector amplitudes and divergence-free constraints. Retained observer: transverse projection P_p k. The weighted Gram is formed only after applying this identity; the later absolute-value majorant does not claim to preserve all phase cancellations. The old replacement |P_p k|<=|k| was safe but lossy. The new observer proves a quantitatively smaller upper bound.

REUSE_EXECUTED: canonical scalar lattice checker, exact_packets.py SHA256 0ffab938427c4827700876fbd9f9c371a59d07aa89edefd5a6447071ec48d25d, parent joint-response, temporal and inverse certificate functions. REUSE_APPLIED: T0_BRC, T6 operation-safe observer boundary, all-mode inverse and running-energy contraction. EXTEND_EXISTING_TOOL: angular near/tail Gram and fixed-alpha obstruction removal. No new top-level accepted family or Foundation change.

All numerical acceptance uses exact fractions and outward rational intervals. Decimal displays are not proof oracles. The infinite lattice tail and full nonlinear feedback are analytic dependencies, never extrapolated from a finite PDE simulation. No external independent review or proof-assistant formalization is claimed.

Next useful unresolved unit: preserve output Leray/polarization information in a matrix-valued Gram, or certify a sharper directional nonlinear-feedback operator. The remaining slack is in the bound, not automatically in NS dynamics. No claim is made that successive improvements of constants will prove arbitrary-data global regularity.
