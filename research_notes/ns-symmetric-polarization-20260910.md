# Symmetric convection Gram: exchange cancellation, an all-mode constant, and a larger causal NS basin

Record-ID: FINDING-EM-PDE-SYMMETRIC-POLARIZATION-20260910
Status: TESTING / ORDINARY_DERIVATION_AND_EXACT_FINITE_CHECKS / NOT_INDEPENDENTLY_REVIEWED
Researcher-ID: EM-DIRECT-F00A51
Research-Activity-ID: RA-076944AE1950A916ACC95399
Continuation key: local-ns-jitter-901c9f34161ce0f1 (local, not platform-authenticated)
Date: 2026-09-10
Global read: 71fbb87fbbece9d82aef6f8e4240a1f4fb886783
Project read: c10a23e6eae0e53d9104dd78a69fec3c29ab1321

## 0. Recovered frontier, scope, and actual new work

Current remote activity already contains checkpoints 12 and 13 under DIFFERENT paths from the older pending local bundles. They must not be duplicated. Checkpoint 12 is `research_notes/ns-angular-lattice-certificate-20260910/checkpoint.md` at 307757948f8dc1ec224094881af15b9295ac19f8. Checkpoint 13 is `research_notes/ns-tensor-cell-gram-20260910/verification_manifest.json` at 97a7f095e4136b3fe81bb9b874b0ef6bee492c5f. The latter establishes the ordered two-solenoidal-input constant 6.447, the R3 constant sqrt(3)/8, and the specified family through 7/40. The chat's older 6.695/0.172 report is not substituted for this verified frontier.

An initial local independent implementation reproduced the transverse tensor with a slightly looser 6.45 enclosure. This was identified as DUPLICATE_REPRODUCTION, not a new result. The present NEW step symmetrizes the two input roles before forming the Gram. It proves a bound for Bs=(B+B^op)/2, not a smaller bound for ordered B. It then uses the exact identity Bs(w,w)=B(w,w) in the nonlinear fixed point.

P000, native 120-degree orthogonality and primitive triadic closure are unchanged. These calculations concern the classical normalized T3 carrier and a separately normalized Euclidean R3 estimate, not a derived full native X6 dynamics. No arbitrary-data global regularity, optimal constant, historical priority, or Foundation admission is claimed. General Fourier explicit estimates, symmetrization, Gram bounds, and a posteriori contraction are established mathematics; the numbers and composed certificate below are result-specific, pending independent review.

## 1. The operation that can safely forget ordered input roles

On normalized T3=(R/2pi Z)^3 let B(f,g)=P((f.grad)g), P_k=I-kk^T/|k|^2, and ||f||_s^2=sum_{k!=0}|k|^(2s)|fhat(k)|^2. Both f and g have zero mean and are solenoidal. Define

    Bs(f,g)=(B(f,g)+B(g,f))/2.

For any w and any direction h,

    Bs(w,w)=B(w,w),
    D[B(w,w)]h=2 Bs(w,h).

Thus the full NS quadratic map and its derivative factor through symmetrization. Ordered B(f,g) for arbitrary distinct f,g does not factor through it. Nor is the lower constant automatically valid for every multi-field system such as MHD.

Fix k=p+q, K=|k|, n=K^2, a=|p|^2, b=|q|^2, c=|p cross k|^2, and t=P_k p. The symmetrized frequency map on the input tensor product is

    T_(p,q)(A tensor C)= [ (A.k) P_k C + (C.k) P_k A ]/2,
    A in p^perp, C in q^perp.

Tensor products here are only a Hilbert-space bookkeeping device for the actual Fourier amplitudes; inputs at different p are not assumed probabilistically independent. The exact 3x3 operator Gram is

    T T* = [c(a+b) P_k - 2(c+(p.k)(q.k)) t t^T]/(4ab).       (1)

One derivation writes T=(T1+T2)/2. Then

    T1T1*=|P_p k|^2 P_k P_q P_k,
    T2T2*=|P_q k|^2 P_k P_p P_k,
    T1T2*=(P_k P_q k)(P_k P_p k)^T.

Since P_k P_q k=((q.k)/b)t and P_k P_p k=-((p.k)/a)t, the two mixed terms have the signed coefficient in (1). Their signs are not discarded.

With F_p=|p| fhat(p), G_q=|q| ghat(q), each weighted convolution is a sum of T_(p,q)(F_p tensor G_q)/(sqrt(K)|p||q|). Cauchy--Schwarz in the direct sum gives

    ||Bs(f,g)||_-1/2^2 <= [sup_k lambda_max Ms(k)] ||f||_1^2||g||_1^2,
    Ms(k)=sum_(p!=0,k) [c(a+b)P_k-2(c+(p.k)(q.k))tt^T]/(4K a^2 b^2). (2)

Ms is PSD and annihilates k. Real symmetric form estimates control complex test polarizations by splitting real and imaginary parts. This is a bound after the true symmetrized convolution; it does not replace each physical branch by a positive independent mass.

## 2. The exact continuum exchange cancellation

Let M be the parent's ordered tensor. Summing over the full symmetric domain p<->q gives

    Ms_cont(k)= M_cont(k)/2 - J(k)/2,
    J(k)=(1/K) integral (p.k)(q.k)(P_k p)(P_k p)^T/(|p|^4|q|^4) dp.

The parent establishes M_cont=(3pi^3/8)P_k. We prove J=0, rather than simply bounding its absolute value. Scaling/rotation reduce to k=e3. For a transverse test e1, the needed scalar integral is

    integral p3(1-p3) p1^2/(|p|^4|e3-p|^4) dp.

It is absolutely integrable. Use

    1/(A^2 B^2)=6 integral_0^1 s(1-s)/[sA+(1-s)B]^4 ds.

After translation p=y+(1-s)e3, put D=s(1-s). Odd terms vanish, leaving numerator (D-y3^2)y1^2. The two radial identities are

    integral y1^2/(|y|^2+D)^4 dy = (pi^2/24) D^(-3/2),
    integral y1^2 y3^2/(|y|^2+D)^4 dy = (pi^2/24) D^(-1/2).

Their difference with the factor D is exactly zero for every 0<s<1. Off-diagonal transverse terms vanish by reflection. Therefore

    Ms_cont(k)=(3pi^3/16)P_k.                                (3)

For reference, the ordered tensor follows from the angular scalar integral pi^3/2 minus the transverse penalty pi^3/8. These values can be rechecked from the same Feynman formula: spherical averages of rho^4 and rho^2 x1^2 are 8r^4/15 and 4r^4/15, and Beta(3/2,3/2)=pi/8.

With unitary Fourier transform on R3, the squared convolution normalization is (2pi)^(-3). Hence, first on solenoidal Schwartz fields and then by homogeneous Sobolev completion,

    ||Bs(f,g)||_(Hdot^-1/2(R3)) <= (sqrt(6)/16)||f||_Hdot^1||g||_Hdot^1. (4)

This improves the parent's ordered upper constant by sqrt(2) for the SYMMETRIC operator. It is not a sharp-constant claim or an R3 global regularity theorem. It must not be inserted numerically into normalized torus formulas.

## 3. A positive sum-of-squares cell comparison for the symmetric numerator

Fix real unit output z perpendicular to k. Take the orthonormal frame (z,b,e) with e=k/K, b=e cross z. Write p=X z+Y b+Z e. The numerator in (2), tested against z, is K^2 times

    Q=2(X^2+Y^2)Y^2 + X^2(2Z-K)^2 + Y^2[Z^2+(K-Z)^2]
     =2(XY)^2+2(Y^2)^2+[X(2Z-K)]^2+(YZ)^2+[Y(K-Z)]^2.       (5)

It is manifestly nonnegative. Average h over the centered standard unit cube, in the ORIGINAL lattice orientation, so E h=0 and E hh^T=I/12. For each product of two affine linear factors in orthogonal directions in (5), its cube mean is its center value; Jensen implies that its squared mean is no larger than its mean square. For Y^2, its mean is Y(p)^2+1/12, which is nonnegative and at least its center value. Thus

    Q(p) <= integral_(p+[-1/2,1/2]^3) Q(x) dx.               (6)

This is valid for arbitrarily oriented frames: only the cube's isotropic SECOND moments are used, not rotational invariance of fourth moments. The signed mixed terms in (1) are never individually assumed nonnegative; they are regrouped exactly into (5) BEFORE averaging.

If |p|,|k-p|>=6, put h6=1+sqrt(3)/12. The denominator satisfies

    |x|^4|k-x|^4 <= h6^8 |p|^4|k-p|^4

on the cell. Combining (6), positive denominators, disjoint cells, and (3) gives the all-output tail bound

    Ms_far(k) <= h6^8 (3pi^3/16) P_k.                        (7)

The exponent eight is explicitly paid. Rational bounds sqrt(3)<1351/780 and pi<355/113 give

    far < 17.09560069415452.

The latter pi bound is rechecked by the inherited Machin/alternating-series code. This is not a finite-tail truncation.

## 4. Exact finite transverse matrices, plus all large outputs

Partition near pairs disjointly: |p|<6; then |q|<6 with |p|>=6. Because the summand (2) is symmetric under p<->q, relabel the second part. Iterate the 894 p with 0<|p|<6 and use multiplicity m=1+1_(|k-p|^2>=36). Then |k| times the near form, in any transverse integer directions u,z, is computed from

    R=sum m*c*(a+b)/(4a^2b^2),
    Hij=sum 2m*(c+(p.k)(q.k))*(p.ui)*(p.uj)/(4a^2b^2),
    N_ij=R(ui.uj)-Hij.                                     (8)

All entries are rational. For 0<|k|<24, signed coordinate permutation symmetry reduces the check to 1490 classes. Use two nonzero orthogonal integer vectors u,z perpendicular to k (z=k cross u). For a rational lower enclosure KL<=|k|, certify that

    diag((71/20)KL*|u|^2,(71/20)KL*|z|^2)-N

has positive diagonal entries and positive determinant. Increasing KL to the exact |k| preserves positivity. All 1490 tests pass, proving the near bound 71/20=3.55 on these outputs. Floating readouts, used only AFTER the exact acceptance, have maximum 3.546519422344686 at (0,2,2).

For |k|>=24, symmetrization obeys TT* <=(T1T1*+T2T2*)/2. The near region is invariant under input exchange, so its sum is bounded by the parent's ordered near tensor, hence by the scalar angular near bound

    (2/3)[A6 K/(K-6)^2+894 K/(K-6)^4],
    A6=67048852231/1012647636.

Both factors decrease for K>6. At K=24 the value is <3.405961<3.55. This covers EVERY remaining output, not a sample of large frequencies.

Combining near and far,

    sup_k lambda_max Ms(k) < 3.55+17.09560069415452
                            < (909/200)^2=20.657025.

Therefore

    ||Bs(f,g)||_(Hdot^-1/2(T3)) <= 4.545 ||f||_Hdot^1||g||_Hdot^1. (9)

Both inputs must be zero-mean solenoidal. No A3 support, helicity, amplitude or output cutoff restriction is present. Ordered B retains the parent's 6.447 bound; (9) is not falsely substituted for ordered mixed-field terms.

## 5. High-frequency limit and what this proof does not remove

The matrix kernel in (2) is homogeneous of degree -3 in (k,p). Thus its lattice sum is a scaled Riemann sum. Matrix domination by the exchange-average of the parent's ordered positive kernels controls both singular neighborhoods and infinity uniformly in the direction k/|k|. On a compact set away from them, ordinary uniform Riemann-sum convergence applies. The parent's bounds give O(epsilon)+O(epsilon^3) near the two endpoints and O(1/R) at infinity. Consequently

    ||Ms(k)-(3pi^3/16)P_k||_op -> 0 as |k|->infinity.        (10)

This is an ANALYTIC limit, not proved by the finite near-field computations. It identifies the positive floor of this particular symmetrized Gram relaxation, not a lower bound on the optimal PDE operator norm and not a dynamics or blow-up assertion. Further input compatibility/phase cancellation may lie outside the relaxed tensor estimate.

## 6. Full nonlinear fixed point: why the new constant is legitimate

Keep the parent's ALL-MODE causal inverse G_v and its bound L unchanged. For nu=1,

    ||h||_X^2=sup_t[||h(t)||_Hdot^1/2^2+(3/4) integral_0^t||h||_Hdot^3/2^2],
    Y=L2_t Hdot^-1/2.

The running-energy product argument gives

    ||Bs(f,g)||_Y <= C_Bs ||f||_X||g||_X,
    C_Bs=(909/200)/sqrt(3/2).

This follows by applying (9), interpolating ||f||_1^2<=sqrt(H(f)D(f)), and using the parent integral inequality integral H(f)D(f)<=||f||_X^4/(2c), c=3/4.

With h0=G_vg, the EXACT error equation is

    w=h0-G_v Bs(w,w).

Its Lipschitz estimate uses Bs(f,f)-Bs(g,g)=Bs(f-g,f+g), so a ball has contraction factor <=2alpha*r with alpha>=L*C_Bs. Neither the background inverse nor its numerical growth estimate is replaced by an unproved symmetric shortcut. No Fourier modes are decimated.

## 7. Executed A3 endpoint, interval, and arbitrary small perturbations

Use the inherited real solenoidal field Phi with positive frequencies (1,1,0),(1,0,1),(0,1,1),(2,-2,0), plus conjugates, and h_+(k)=(e0+i(k cross e0)/|k|)/sqrt(2), where e0 is the coordinate direction at the zero coordinate of k. The frequency rank is three. The reference is v=a exp(-t Lambda^2)Phi.

Reuse d=a^2p2+a^3p3 with disjoint supports, ||p2||_X<0.3271, ||p3||_X<0.128, and complete defect e=-a^4K3 with ||K3||_Y^2=0.0014408187275118617... . These packets are rebuilt exactly using the unchanged backend. The correction has 216 packets; the defect has 772 packets and 144 frequency outputs. Initial traces, reality, divergence, the heat equations, the full defect, and finite-packet symmetrization are checked.

At a=19/100, rational enclosure gives Lraw<5.37352442. Use

    L=43/8=5.375,
    alpha=20 > L*C_Bs,
    eta=1211/100000=0.01211,
    r=3/125=0.024.

The computed upper bound U(d)+L||e||_Y is <0.01210679030854. Exact inequalities are

    r-eta-alpha*r^2=37/100000=0.00037>0,
    2alpha*r=24/25<1,
    4alpha*eta=0.9688<1.

An arbitrary smooth, real, mean-zero solenoidal initial perturbation with ||delta||_1/2<=1/20000 adds at most sqrt(3/4)L/20000. The remaining inclusion margin is >0.00013725567. No A3, Fourier-finiteness or helicity assumption is imposed on delta.

All bounds L(a), a^2, a^3, a^4 are nondecreasing for a>=0, so the ENDPOINT certificates cover the entire interval, not sampled interpolation. Under the explicitly inherited inverse and smooth-solution continuation interfaces, for every nu>0,

    u0=a Phi+delta,
    0<=a/nu<=19/100,
    ||delta||_Hdot^1/2<=nu/20000

has a global smooth FULL periodic unforced NS solution, with

    sup_t[||u(t)-a exp(-nu t Lambda^2)Phi||_Hdot^1/2^2
      +(3nu/4)integral_0^t||u(s)-a exp(-nu s Lambda^2)Phi||_Hdot^3/2^2]
      <=(3nu/125)^2.                                       (11)

The viscosity scaling is u(t)=nu U(nu t). The larger radius pertains to a larger family and is not an accuracy comparison for the earlier smaller datum. This is a restricted certificate, NOT an arbitrary-data theorem. The numerical proof status of inherited inputs remains TESTING.

## 8. Typed BRC reuse, tests, and next unfinished step

REUSE_EXECUTED: canonical exact_packets.py SHA256 0ffab938427c4827700876fbd9f9c371a59d07aa89edefd5a6447071ec48d25d; certify_joint.py SHA256 a16b817cdc5cc46f96d447094c18fef14be8252b118e2d0435795970a9a81139; archived angular checker SHA256 40d41ab035fd4be7b6c271f3cb0144c9a4c2042e4268940c96613c240de89a50, now also present under canonical checkpoint 13. Exact finite packet phases are retained. Tensor multiplication, Leray projection, and ordered-input exchange are performed before norms.

REUSE_APPLIED: canonical checkpoint 13, causal inverse, running-energy product, initial perturbation bound, and nonlinear contraction. EXTEND_EXISTING_TOOL: operation-safe symmetrization of the quadratic map, exact signed exchange integral, symmetric SOS cell comparison, and its explicit all-mode constant. No new accepted toolbox family or Foundation promotion.

Symmetrization is licensed for B(w,w) and its derivatives; it is NOT an equivalence for arbitrary ordered B(f,g), an arbitrary MHD component, or hidden branch operations. Positive Gram matrices do not create global dynamical dissipation. The continuous limit is a property of the majorant, not a blow-up test.

Actual checks: unchanged parent scalar near checker; 1490 rational transverse matrices; all-large-output bound; exact Gram identity; positive SOS polynomial; radial/Beta identities; complete finite Fourier responses and nonlinear margins; clean-directory reruns. High precision/float diagnostic values are not proof oracles. No PDE time/space simulation or finite-to-infinite extrapolation is used.

Next smallest unit: certify a sharper background propagator or exploit coupled frequency compatibility beyond independent tensor relaxation; repeated scalar constant optimization alone cannot prove all-data regularity. The existing high-frequency positive limit makes that boundary explicit.

Primary context checked on 2026-09-10: Morosi--Pizzocchero, arXiv:1007.4412 (different higher-order explicit inequalities); Morosi--Pernici--Pizzocchero, arXiv:1511.00533 (related tame inequalities); Morosi--Pizzocchero, arXiv:1104.3832 (a posteriori approximate-solution control). These contextual sources do not verify our endpoint constants or establish historical novelty.
