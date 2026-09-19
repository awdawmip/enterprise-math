# Transverse tensor Gram and centered-cell critical NS bound

Record-ID: FINDING-EM-PDE-TENSOR-CELL-GRAM-20260910
Status: TESTING / ORDINARY_PROOFS_AND_EXACT_RATIONAL_CHECKS / NOT_INDEPENDENTLY_REVIEWED
Researcher-ID: EM-DIRECT-F00A51
Research-Activity-ID: RA-076944AE1950A916ACC95399
Continuation key: local-ns-jitter-901c9f34161ce0f1 (locally assigned, not platform-authenticated)
Date: 2026-09-10
Read pins: global 8403fde645780487edb8fa23a15c587e279175a3; enterprise-math 4fdfe0c561d8828c0eb5b28b0de653dc440b0d46.

## 0. Recovery and scope

The current twelfth checkpoint is research_notes/ns-angular-lattice-certificate-20260910/checkpoint.md, blob 582fddf1c5c8318999f126fb8092eea2f5c6d172. Its proof, research_notes/ns-angular-lattice-certificate-20260910.md, blob 049fed81b930c56d1f4dd2e43a9ddaad4405aa04, establishes C=7.605 and a specified A3 family through amplitude 1/6. This is consumed, not rerun as a new discovery. The older uploaded 7.95 package separately contains a valid disjoint-near checker, reused for that narrower input only.

P000 remains unchanged. Native 120-degree orthogonality is not replaced by the Euclidean scalar products below. The claims concern the classical three-dimensional carrier, not full native X6 dynamics. No arbitrary-data regularity, sharp constant, historical priority, independent review, or Foundation admission is claimed. General explicit Fourier constants and approximate-solution validation are established; primary context is Morosi--Pizzocchero arXiv:1007.4412 (a different higher-order inequality) and arXiv:1104.3832. They are context, not independent validation of this note.

## 1. Two-input transverse tensor

On normalized T3=(R/2pi Z)^3 use ||f||_s^2=sum_(k!=0)|k|^(2s)|fhat(k)|^2. Both inputs f,g are mean zero and divergence free. Write B(f,g)=P((f.grad)g), P_k=I-kk^T/|k|^2. For p+q=k and any complex unit z perpendicular to k,

|z*Bhat(k)| <= sum |P_p k| |P_q z| |fhat(p)| |ghat(q)|.

With F_p=|p||fhat(p)| and G_q=|q||ghat(q)|, Cauchy--Schwarz gives

|k|^-1 |z*Bhat(k)|^2 <= (z*M(k)z) sum_(p+q=k)F_p^2G_q^2,

M(k)=(1/|k|)sum_(p!=0,k) [|p cross k|^2/(|p|^4|q|^2)] P_k P_q P_k.

Thus

||B(f,g)||_-1/2^2 <= [sup_k lambda_max M(k)] ||f||_1^2||g||_1^2.

The real symmetric PSD matrix M(k) annihilates k. Its real maximum eigenvalue also controls complex z by separating real and imaginary parts. The zero output vanishes by incompressibility. The sum over nonzero outputs is bounded by the full product of input sums. The second solenoidal condition is essential to the improved tensor bound; the previous scalar reduction replaced |P_q z| by |z|.

## 2. Centered-cell numerator identity

Let e,t be orthogonal real unit vectors, k=K e, A=I-ee^T, C=I-tt^T. Then A,C commute, AC is PSD, and ACk=0. Average xi over the unit cube [-1/2,1/2]^3; this is a deterministic integral, not a physical stochastic model. E xi=0, E xi xi^T=I/12, and all odd total moments vanish.

For p+q=k, a=p^TAp and b=q^TCq, exact expansion gives

E[((p+xi)^TA(p+xi))((q-xi)^TC(q-xi))]
=ab+[tr(A)b+tr(C)a-4p^TACq]/12+E[(xi^TAxi)(xi^TCxi)]
=ab+[tr(A)b+tr(C)a+4p^TACp]/12+E[(xi^TAxi)(xi^TCxi)] >= ab.

All extra terms on the second line are nonnegative. This is NOT an assertion about arbitrary products of positive quadratics: commutation and ACk=0 supply the sign. For a single PSD quadratic, E[(p+xi)^TA(p+xi)]=p^TAp+tr(A)/12. Eighteen rationally rotated polynomial cases are checked independently; the expansion is the general proof.

## 3. Exact continuum integral and R3 corollary

For unit real t perpendicular to k define

F_(k,t)(x)=|k|[x^TAx][(k-x)^TC(k-x)]/(|x|^4|k-x|^4).

Then integral_R3 F_(k,t)(x) dx=3pi^3/8.

Proof: the C=I term is pi^3/2, from K integral sin^2(angle(x,k))/(|x|^2|k-x|^2). In polar coordinates the radial integral is (pi/2+arcsin mu)/sqrt(1-mu^2); the odd arcsin contribution vanishes. The subtracted term, with k=K e3 and t=e1, has numerator (x1^2+x2^2)x1^2. Use

1/(a^2b^2)=6 integral_0^1 s(1-s)/[sa+(1-s)b]^4 ds.

Translation along k preserves this numerator. Its spherical average is (4/15)|y|^4, while integral_R3 |y|^4/(|y|^2+m^2)^4 dy=5pi^2/(8m) and Beta(3/2,3/2)=pi/8. The subtracted term, including K, is pi^3/8. All terms are finite, with nonnegative integration justified before subtraction.

For the unitary Fourier transform on R3, the convolution prefactor squared is (2pi)^-3. Therefore, for Schwartz solenoidal f,g and by homogeneous Sobolev completion,

||P((f.grad)g)||_(Hdot^-1/2(R3)) <= (sqrt(3)/8)||f||_Hdot^1||g||_Hdot^1.

If only f is solenoidal, the same scalar angular calculation gives 1/4 instead. Neither constant is claimed sharp or historically new. This is a bilinear estimate, NOT an R3 global NS theorem; the torus spectral gap and its prior inverse certificate do not transfer unchanged.

## 4. Infinite lattice tail

For Q_p=p+[-1/2,1/2]^3 and |p|,|k-p|>=6, set delta=sqrt(3)/2 and h=1+delta/6. For every x in Q_p,

|x|^4|k-x|^4 <= h^8 |p|^4|k-p|^4.

Combining this denominator bound with the A,C numerator-average identity gives

F_(k,t)(p) <= h^8 integral_(Q_p)F_(k,t)(x)dx.

The numerator is averaged before comparison; a pointwise directional-error bound is not substituted for it. Summing disjoint cubes and enlarging to R3 proves

M_far(k) <= h^8(3pi^3/8)P_k.

Using rational upper bounds delta<1351/1560 and pi<355/113 gives far<34.19120138830904. The pi bound is independently checked through Machin's identity and alternating rational series in the reused checker. This covers ALL remaining input pairs and outputs.

The single-quadratic identity similarly gives a scalar far bound h^6*pi^3/2<34.813265040935. With the disjoint scalar near bound <10 it yields C=6.695 when only the first input is solenoidal.

## 5. Exact near transverse matrices

Partition near pairs disjointly: |p|<6, then |q|<6 with |p|>=6. Relabel the second part. For a=|p|^2, b=|k-p|^2, c=|p cross k|^2, |k| times the near matrix is

T(k)=P_k sum_(0<|p|<6,p!=k) [c/(a^2b)P_(k-p)+1_(b>=36)c/(ab^2)P_p] P_k.

There are 894 near lattice points. For 0<|k|<17, signed coordinate permutations reduce checking to 571 classes 0<=k1<=k2<=k3. Matrix conjugation under these symmetries preserves eigenvalues. Entries are rational; symmetry and T(k)k=0 are checked exactly.

Let n=|k|^2, t=tr T, D=2tr(T^2)-t^2. The largest transverse eigenvalue of T is (t+sqrt(D))/2. For beta=737/100 the checker verifies

D>=0, t>=0, 4beta^2n>t^2,
J=4beta^2n+t^2-D>0,
J^2>16beta^2nt^2.

Positive-side squaring proves lambda_max(T)/|k|<7.37. No floating eigenvalue is an acceptance oracle. The largest diagnostic value is 7.368577261737 at (1,2,2).

For K=|k|>=17, scalar domination and the exact cubic moment identities give

lambda_max M_near <= (2/3)[A6 K/(K-6)^2+894 K/(K-6)^4]
<= (2/3)[17A6/121+894*17/14641] <6.893652<7.37,

where A6=67048852231/1012647636. Both radial factors decrease for K>6. Thus all outputs are covered.

Consequently sup_k lambda_max M(k)<7.37+34.19120138830904<(6447/1000)^2. By density,

||P((f.grad)g)||_(Hdot^-1/2(T3)) <= 6.447 ||f||_Hdot^1||g||_Hdot^1

for mean-zero solenoidal f,g. There is no A3, helicity, amplitude, or cutoff restriction. This reduces the canonical 7.605 by 386/2535, using a second solenoidal condition already satisfied by NS velocities. It is not an optimal constant claim.

## 6. Full periodic NS family

Reuse the established all-mode inverse, temporal response bounds and critical contraction. For nu=1,

||h||_X^2=sup_t[||h(t)||_Hdot^1/2^2+(3/4)integral_0^t||h||_Hdot^3/2^2],
Y=L2_t Hdot^-1/2, C_B=6.447/sqrt(3/2), alpha>=L C_B.

The inverse bound L itself is unchanged. All bilinear inputs and outputs are solenoidal. A finite zero-initial d with complete defect e=D_vd-g gives eta>=||G_vg||_X whenever eta>=||d||_X+L||e||_Y. The complete error is w=G_vg-G_v B(w,w). Conditions eta+alpha*r^2<r and 2alpha*r<1 give a full invariant contraction ball; the inherited critical-space continuation argument yields smoothness for smooth data.

Use the fixed shape Phi with positive frequencies (1,1,0),(1,0,1),(0,1,1),(2,-2,0) and conjugates. At positive k, h_+(k)=(e+i(k cross e)/|k|)/sqrt(2), with e the coordinate unit vector at the zero coordinate. Let v=a exp(-t Lambda^2)Phi. Reuse d=a^2p2+a^3p3. Their supports are disjoint, so

||d||_X <= sqrt[(0.3271a^2)^2+(0.128a^3)^2],
||D_vd-g||_Y=a^4 sqrt(c4), c4=0.0014408187275118617... .

The exact radical c4 is recomputed from complete outputs. The correction has 216 packets; its full linear defect has 772 packets and 144 output frequencies. No mode or opposite helicity is removed.

At a=7/40=0.175 rational outward bounds give

L=4.64133868, alpha=24.4317908, eta=0.0102061332.

For r=1/50,

r-eta-alpha*r^2=0.00002115048>0,
2alpha*r=0.977271632<1.

An arbitrary smooth, real, mean-zero solenoidal initial perturbation of norm <=10^-6 adds at most sqrt(3/4)L*10^-6 to eta, smaller than the inclusion margin. No A3 or helicity restriction is placed on this perturbation.

The reference growth envelope b_a=(aM(v_unit)-1/4)_+, its integral, L(a), and the displayed powers of a are nondecreasing for a>=0. Endpoint bounds therefore certify the WHOLE interval, not sampled interpolation. Exact viscosity scaling u(t,x)=nu U(nu t,x) yields for every nu>0:

0<=a/nu<=7/40, ||delta u0||_Hdot^1/2<=nu/10^6
=> a global smooth full periodic NS solution, with

sup_t[||u(t)-a exp(-nu t Lambda^2)Phi||_Hdot^1/2^2
 +(3nu/4)integral_0^t||u(s)-a exp(-nu s Lambda^2)Phi||_Hdot^3/2^2 ds] <=(nu/50)^2.

Additional executed tests at a=0.16 and 1/6 give radii 0.012 and 0.014. These improve certificates for already-certified data. None of these statements is an arbitrary-data theorem.

## 7. BRC and reproducibility

Retain ordered input pairs, output k, complex polarization, and the solenoidal projection before forming the tensor Gram. For causal responses retain rate, time power, conjugacy and zero trace. A positive matrix Gram does not imply off-diagonal negativity or automatic dissipation. Cell averaging here is exact integration, not a physical jitter model.

REUSE_APPLIED: T0_BRC, operation-safe observer boundary, all-mode inverse and running-energy contraction. REUSE_EXECUTED unchanged: exact_packets.py SHA256 0ffab938427c4827700876fbd9f9c371a59d07aa89edefd5a6447071ec48d25d; certify_joint.py SHA256 a16b817cdc5cc46f96d447094c18fef14be8252b118e2d0435795970a9a81139; supplied disjoint-near checker SHA256 40d41ab035fd4be7b6c271f3cb0144c9a4c2042e4268940c96613c240de89a50. EXTEND_EXISTING_TOOL: matrix Gram and centered-cell tail, not a new accepted Foundation family.

Executed checks: 571 exact near matrices, inherited 487-class scalar near check, analytic large-output and far bounds, beta/gamma normalization, 18 rotated cell identities, full causal defects, and three contraction balls. All numerical acceptance is rational or outward interval arithmetic. Infinite tails are analytic, not PDE sampling. Independent peer review and proof-assistant validation remain undone.

Next unresolved unit: sharpen the phase-sensitive background inverse or the uniform denominator distortion, with a quantitative diagnosis of which term limits the expanded family. Repeated constant improvements alone do not prove arbitrary-data global regularity.
