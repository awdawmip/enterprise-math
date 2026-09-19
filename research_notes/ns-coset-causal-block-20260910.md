# Fourier-coset causal bounds and a two-block Navier--Stokes certificate

Record-ID: FINDING-EM-PDE-COSET-CAUSAL-BLOCK-20260910
Status: TESTING / ORDINARY_DERIVATION_AND_EXACT_RATIONAL_CHECKS / NOT_INDEPENDENTLY_REVIEWED
Researcher-ID: EM-DIRECT-F00A51
Research-Activity-ID: RA-076944AE1950A916ACC95399
Continuation key: local-ns-jitter-901c9f34161ce0f1 (locally assigned, not a platform identity)
Date: 2026-09-10
Read pins: global bd9a613d2a546a7d3f500db7b124834e581df4db; project 4fffe9f6353242ce5c7c514325da8b9a63c18f8b.

## 0. Recovery, scope, and dependencies

Current GitHub checkpoint 14 already contains symmetric convection, C_s=909/200=4.545, and the specified family through a/nu=0.19. The older chat's ordered-polarization 6.45 report is not the source frontier. Checkpoints 12--14 are already represented: no duplicate backfill is required.

Precise parent: research_notes/ns-symmetric-polarization-20260910.md at 88d18007c15f02e4581b14381220e64da570d57e, blob 0fc2e6cc7304526baa91dd4acc0e1642a02618b9, SHA256 d1f898271a9b8694767b951dab00c9af78785df85c9c19b84d81c7eba84d29da. Its manifest is at 782a53f8919eca955f720541665cff1fcae45e2f. The explicit Hermitian block bound is research_notes/ns-spectral-reference-20260909.md, blob e1b8d70548245a34ed18b34718f6bf404e2386a1. The causal inverse, running-energy product, and smooth continuation statements are inherited analytic dependencies, not independently re-proved or promoted here.

P000 is unchanged. The mathematics concerns the normalized classical three-torus, not a derivation of all native X6 dynamics. Fourier parity below is NOT helicity, force count, a physical two-force equilibrium, or a claim of two spatial dimensions. It is an additive frequency label retained alongside full complex Fourier data. No arbitrary-data NS regularity, best threshold, or historical novelty is claimed. The new work is coset-resolved use of the background spectral gap and a coupled nonlinear certificate, not a new general invention of symmetry decomposition or contraction mappings.

## 1. Exact additive label and invariant linear sectors

On T3=(R/2pi Z)^3 define chi(k)=k1+k2+k3 modulo 2. Let P_E and P_O retain respectively even and odd chi. Equivalently, with tau u(x)=u(x+pi(1,1,1)), P_E=(I+tau)/2, P_O=(I-tau)/2. These are orthogonal Fourier projections on every Sobolev space and commute with Lambda=(-Delta)^(1/2), heat, and Leray projection.

For B(f,g)=P((f.grad)g) and Bs=(B+B^op)/2,

  Bs(E,E) subset E, Bs(O,O) subset E, Bs(E,O) subset O.       (1)

This follows from chi(p+q)=chi(p)+chi(q), retaining every convolution output. The zero mode of convection of solenoidal mean-zero fields is zero, so it causes no exception.

All four positive frequencies of the fixed A3 field Phi,

  (1,1,0), (1,0,1), (0,1,1), (2,-2,0),

have even chi. Hence the heat reference v=a exp(-t Lambda^2)Phi is even. Its full linearization D_v=partial_t+Lambda^2+2Bs(v,.) preserves both sectors. Its exact causal inverse therefore decomposes into G_E and G_O. This is an invariant decomposition, not a modification or decimation of NS.

The two minimal nonzero radii differ:

  rho_E=sqrt(2), rho_O=1.                                  (2)

Indeed radius-one integer vectors have odd sum, while (1,1,0) is even. Exact finite checks accompany this elementary all-lattice proof.

## 2. All-mode causal inverse uses each sector's actual gap

The parent gives, for all input/output radii >=rho,

  ||S_v|| <= M_rho(v),
  M_rho(v)=sum_(p!=0)|p|[1/2+sqrt(1+|p|/rho)]|vhat(p)|.     (3)

This follows by symmetrizing the unbounded transport part before taking block norms. We apply the same proved law, not a new eigenvalue assumption. On sector j the viscously shifted form obeys

  <z,S_v z>-(1/4)||Lambda z||^2 <= b_j(t)||z||^2,
  b_j(t)=(M_(rho_j)(v(t))-rho_j^2/4)_+.                    (4)

Define c=3/4, Y=L2_t Hdot^-1/2, and

  ||h||_X^2=sup_t[||h(t)||_Hdot^1/2^2+c int_0^t||h||_Hdot^3/2^2].

For the zero-initial problem D_v h=g in sector j, the parent energy argument gives

  ||G_j g||_X <= L_j ||g||_Y,
  L_j=exp(int_0^infinity b_j)/sqrt(c).                      (5)

For nonzero initial error delta_j and zero forcing, the corresponding bound is sqrt(c)L_j||delta_j||_Hdot^1/2. Galerkin limits inside each invariant sector give existence and uniqueness exactly as in the parent. No finite-matrix extrapolation or normality assumption is used.

For the fixed two-shell reference,

  M_(rho_j)(v)=a[m_A(j)e^(-2t)+m_B(j)e^(-8t)].

In the even sector m_A=6sqrt(2)[1/2+sqrt(2)], m_B=4sqrt(2)[1/2+sqrt(3)], and the subtraction in (4) is 1/2. In the odd sector m_A=6sqrt(2)[1/2+sqrt(1+sqrt(2))], m_B=4sqrt(2)[1/2+sqrt(1+2sqrt(2))], and the subtraction is 1/4.

Each positive-part growth envelope has at most one zero. The checker brackets it by rational bisection with outward radical/exponential intervals and integrates the exponential envelope analytically. These bounds cover all time and all frequencies.

## 3. Two nonlinear radii, including symmetry-breaking perturbations

The inherited symmetric bilinear estimate is

  ||Bs(f,g)||_Y <= C_B ||f||_X||g||_X,
  C_B=(909/200)/sqrt(3/2).                                 (6)

Both inputs must be solenoidal. Define alpha_E=L_E C_B and alpha_O=L_O C_B, or rigorous larger bounds.

Write u=v+e+o with e even and o odd. The exact fixed point is

  e=h_E-G_E[Bs(e,e)+Bs(o,o)],
  o=h_O-2G_O Bs(e,o).                                     (7)

Here h_E includes the even reference residual and the even initial perturbation; h_O is the odd homogeneous initial response. Odd-odd feedback is present in (7) and in every inequality below. If the initial datum is exactly even, h_O=0 and o=0 is invariant; this is a consequence of (7), not an imposed deletion for mixed data.

Suppose ||h_E||_X<=eta_E, ||h_O||_X<=eta_O. A product ball with radii r_E,r_O is invariant if

  eta_E+alpha_E(r_E^2+r_O^2)<=r_E,
  eta_O+2alpha_O r_E r_O<=r_O.                              (8)

The componentwise Lipschitz matrix is

  M=[[2alpha_E r_E,2alpha_E r_O],
     [2alpha_O r_O,2alpha_O r_E]].                          (9)

It is enough to find positive weights w_E,w_O with Mw<=q w, q<1. Banach contraction then applies in the weighted maximum metric. This test is different from replacing both inverse constants and both radii by their common maxima. It preserves the exact finite interaction table.

Because Fourier sectors are orthogonal at each time,

  ||e+o||_X^2 <= r_E^2+r_O^2.                              (10)

The constructed full solution inherits bounded Hdot^1/2 and integrable Hdot^3/2 dissipation. Together with the prescribed smooth heat reference, interpolation gives the standard L4_t L6_x continuation control. With smooth data the resulting full periodic unforced solution is globally smooth, subject to the stated inherited local/continuation interfaces.

## 4. Finite abelian grading interface

More generally let chi:Z3->G be an additive map to a finite abelian group, and take a background in the neutral class. The linearization preserves each coset, while Bs sends classes h,l to h+l. Given certified L_g, the same argument gives

  r_g >= eta_g+alpha_g sum_(h+l=g)r_h r_l,
  M_(g,h)=2alpha_g r_(g-h), alpha_g=L_g C_B.                (11)

A positive weighted contraction Mw<=q w, q<1, proves a full solution in the componentwise ball. Reality must be preserved through conjugate classes g and -g. Empty sectors can be omitted. Finite grading by itself gives no all-data radius or uniform bound; its value is avoiding an unjustified collapse of distinct propagation budgets.

This is the reusable BRC interface: retain the output class, the full signed/complex data within that class, and the convolution law until the componentwise estimates are formed. The class alone is not a complete dynamical state. No probabilistic independence, cancellation between positive masses, or extra physical degrees of freedom is asserted.

## 5. Executed mixed-sector certificate at a=0.20

Phi is the inherited real eight-mode field: at each positive k choose e0 at the zero coordinate and h_+(k)=[e0+i(k cross e0)/|k|]/sqrt(2); negative coefficients are conjugates. Three input directions are independent. The two shells are nonlinear together and generate new frequencies and helicities.

The unchanged backend constructs unit responses p2,p3 and the complete defect K3. Reuse

  d=a^2p2+a^3p3,
  D_vd-g=-a^4K3,
  ||p2||_X<0.3271, ||p3||_X<0.128,
  ||K3||_Y^2=0.0014408187275118617... .

The two responses have disjoint Fourier supports. Thus

  eta_base <= sqrt((0.3271 a^2)^2+(0.128 a^3)^2)
               +L_E a^4||K3||_Y.                         (12)

All inputs, responses and this defect are even. Rebuilt correction: 216 packets. Complete defect: 772 packets and 144 outputs. The odd test field used by the checker has nonzero odd-odd output and verifies (7) with all convolution modes retained.

At a=1/5, adopt rational bounds

  L_E=3919/1000=3.919, L_O=741/125=5.928,
  alpha_E=291/20=14.55, alpha_O=2201/100=22.01,
  eta_base=13363/1000000=0.013363.

The computed bound in (12) is <0.013362022337. For arbitrary smooth real mean-zero solenoidal delta with ||delta||_Hdot^1/2<=1/10000, both projected initial norms are <=1/10000. Choose

  r_E=1/50=0.02, r_O=1/200=0.005.

After including the two homogeneous initial responses, exact rational intervals prove that the two margins in (8) exceed respectively

  0.00011385464425 and 0.00008462014063.

Weights (w_E,w_O)=(1,2) yield row contraction bounds

  q_E=873/1000, q_O=19809/20000=0.99045<1.                 (13)

Consequently this entire initial perturbation ball is certified. It is not restricted to even parity, A3 support, finite Fourier data or one helicity.

Endpoint domination is valid because the positive-part envelopes, L_j(a), and powers a^2,a^3,a^4 in (12) are nondecreasing for a>=0. Restore viscosity by u(t)=nu U(nu t). The theorem covers

  u0=a Phi+delta, 0<=a/nu<=1/5,
  ||delta||_Hdot^1/2<=nu/10000,

and the two sector trajectory bounds scale to r_E nu and r_O nu. In particular

  sup_t[||u-v||_Hdot^1/2^2+(3nu/4)int_0^t||u-v||_Hdot^3/2^2]
     <=(17/40000)nu^2.                                   (14)

This norm is not a pointwise velocity error.

## 6. Why a single common amplification factor loses this certificate

At a=0.20 evaluate the explicit d at the rational time t0=17/100, including its partial accumulated dissipation. The parent exact exponential-polynomial integration routine gives

  ||G_E g||_X >= ||d||_(X,t0)-L_E||D_vd-g||_Y > 0.012843.

This single-time calculation is a lower bound only, not an all-time upper estimate. If one insists on the shared scalar feedback alpha_O=22.01, then

  4alpha_O||G_Eg||_X > 28267443/25000000=1.13069772>1.     (15)

Thus that fixed scalar majorant cannot pass for any candidate dictionary. The new two-sector certificate succeeds because the actual large first response is in the less amplified even sector; only the smaller odd error uses the larger inverse. The scalar obstruction remains true within its declared scope. It is neither a blow-up statement nor a lower bound on the best possible exact inverse.

## 7. A larger symmetry-preserving family, with a different perturbation condition

At a=213/1000, use

  L_E=547/125=4.376, alpha_E=406/25=16.24,
  eta_base=7617/500000=0.015234,
  r_E=29/1000=0.029.

For EVEN-sublattice perturbations with norm <=1/100000 the exact maintained-ball margin exceeds 0.00007026272833 and the contraction factor is

  2alpha_E r_E=5887/6250=0.94192<1.

Hence the invariant-even family covers all 0<=a/nu<=0.213 with even perturbations of norm <=nu/100000. Its trajectory radius is 0.029nu. This result MUST NOT be combined with (14) to claim arbitrary perturbations at 0.213. Symmetry-breaking stability at that larger endpoint is not certified by this run.

## 8. Execution, limitations, and next unit

REUSE_EXECUTED unchanged: exact_packets.py SHA256 0ffab938427c4827700876fbd9f9c371a59d07aa89edefd5a6447071ec48d25d; certify_joint.py SHA256 a16b817cdc5cc46f96d447094c18fef14be8252b118e2d0435795970a9a81139; its pinned goal/greedy dependencies. REUSE_APPLIED: canonical checkpoint 14 symmetric constant, critical causal inverse, background block law (3), and continuation. EXTEND_EXISTING_TOOL: coset-dependent growth bounds, matrix majorant, and certified symmetry-breaking neighborhood.

Checks executed: 15,376 integer character sums; exact Fourier even/odd nonlinear and linearized identities; a nonzero odd-odd feedback witness; inherited zero traces/reality/divergence and temporal maxima; complete residual Gram; rational growth-zero brackets; two-block and scalar ball margins; a scalar-obstruction lower bound; clean-directory rerun. No PDE time/space sampling or assumed background process. Numerical output is not independent peer review or proof-assistant verification.

Next unit: sharpen the odd-sector propagator (the largest contraction row is 0.99045), or subdivide admissible frequency classes further while retaining their exact interaction graph. No finite group partition alone establishes arbitrary-data NS regularity. The source/persistence status is provenance only, not Foundation, Working Truth or theorem admission.

Method context checked: Morosi--Pizzocchero, arXiv:1104.3832; Morosi--Pizzocchero, arXiv:0709.1670 (established a posteriori approximate-solution and semilinear control methods). These references do not independently verify this note's constants or examples.
