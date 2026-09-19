# 心跳世界 BRC：条件分布重建、关联生成与可传播失配

Status: `SCOPED_PROOFS / EXECUTABLE_RESEARCH_CANDIDATE / NOT_FOUNDATION`  
Researcher: `EM-DIRECT-AD0416`  
Activity: `RA-37C0A30C7B1F5A338F03D186`  
Event: `heartbeat-brc-conditional-lift-20260920-AD0416`  
Read EM: `91c39a76eaa69f9cb4221125619d75be53cac03b`  
Read GLOBAL_KNOWLEDGE: `5d443f0c8241e73b6b1192dc00adb9c523711115`

<a id="section-1"></a>

## 1. Problem and semantic boundary

Continue the existing residue/environment/phase/mass research. The previous chain-rule expression
`P(r,e,phi)=P(r|e,phi)P(e|phi)P(phi)` is always valid (up to zero-probability conditioning conventions), but does not itself reduce parameters. Conditional independence, a sparse restricted family, or a proved observer quotient is required for actual reduction.

HEARTBEAT_WORLD remains native X6 signed relative spatial coordinates plus separately typed time. The six Boolean environmental bits below refer only to the six positive-axis channels, NOT all twelve signed neighbors. The example retains the first spatial coordinate residue mod4 exactly. All six coordinates remain present, and each motion is one signed native unit-axis step. No final nonnegative Cell-address codec, P000 change, physical clock calibration or semantic-memory performance is claimed.

<a id="section-2"></a>

## 2. Independence defect and a stability-changing witness

For a finite nonnegative joint mass table M with total T>0, row sums a_i and column sums b_j, product factorization is equivalent to `T M_ij = a_i b_j` for every entry. Necessity follows by summing the factors; sufficiency gives `M_ij=a_i b_j/T`. The zero table satisfies the polynomial equalities without defining a normalized probability distribution.

Start with two independent uniform bits and apply positive gain

```
G = [[3/2, 1/2], [1/2, 3/2]].
```

The resulting normalized joint table is `[[3/8,1/8],[1/8,3/8]]`. Both marginals remain uniform, but the product defect at (0,0) is 1/8. A hidden common bit creates a separate obstruction: the equal mixture of product point masses (0,0) and (1,1) becomes `diag(1/2,1/2)` after that common cause is forgotten. Conditional independence before mixing is not independence after mixing.

Include retention lambda=3/4. Holding the two bits fixed gives the four-state diagonal mass kernel `diag(9/8,3/8,3/8,9/8)`. From uniform initial mass,

`S_n = ((9/8)^n+(3/8)^n)/2`,

so the all-depth positive mass diverges. If, instead, an ACTUAL operation reselects both bits independently and uniformly AFTER EACH gain, the kernel is `W_ij=w_i/4` and uniform initial mass yields `(3/4)^n`, with total all-depth mass 4. Merely replacing the correlated distribution by its product marginals implements this different reset model; it is not an exact compression of the held-bit model. At n=2 the two totals are 45/64 and 9/16.

The existing exact recurrent-mass module was executed unchanged on both kernels, including a stable integer certificate and a divergence certificate. These weights are positive branch mass, not physical conserved mass or stochastic transition probabilities in every row.

<a id="section-3"></a>

## 3. Conditional reconstruction differs from a point quotient

Let pi map n micro-controls onto m retained classes. Set `P_ia=1{pi(i)=a}`. A fixed lift L is nonnegative, each row sums to one, and row a is supported on pi^-1(a). Thus `L P=I`. The implementation stores one conditional probability p_i per micro-control, `L_ai=p_i 1{pi(i)=a}`.

Admissible row measures are exactly `mu=alpha L`. The input guard computes alpha=mu P and checks reconstruction exactly; it never silently randomizes an invalid input.

The new certificate is

`L W_t = Q_t L`, with `Q_t=L W_t P`.

This is a LEFT intertwining, unlike the previous strong point quotient `W_t P=P Q_t`. The latter preserves coarse outputs from arbitrary micro-state starts. The new interface preserves a stipulated conditional distribution family and may pass when the strong quotient fails. Neither condition should be substituted for the other.

Multiplying and applying induction gives

`L W_0 ... W_(n-1) = Q_0 ... Q_(n-1) L`.

Therefore admissible distributions evolve exactly by alpha_(t+1)=alpha_t Q_t and can be reconstructed at each declared boundary. In a time-homogeneous stable case summing the nonnegative terms gives `L W*=Q* L`.

Stability scope matters. If each micro-control has positive conditional probability in its fiber, every point mass is dominated by a finite multiple of some lift row. Positivity and the identity above then make total-mass finiteness for all coarse starts equivalent to finiteness for all micro starts. Without full support, the lift can hide an unstable unrepresented state; the tests include `L=(1,0)`, `W=diag(1/2,2)`.

These are standard intertwining-style algebraic identities specialized to finite exact positive BRC, not a priority claim for Markov intertwining.

<a id="section-4"></a>

## 4. Affine-action mass certificate

Mass equality alone does not preserve dependence between spatial endpoints and micro-control. For each integer-coefficient affine map f, let W_f(i,j) be the TOTAL positive branch mass carrying that map, including multiplicity. The stronger certificate checks

`L W_f = Q_f L`

separately for every map in the supplied finite packet. This is coefficientwise equality of positive action-mass measures. It does NOT preserve how total mass splits into individual weights, or labeled path provenance.

For joint measures require the stronger initial condition

`mu_i(dx)=L_(pi(i),i) nu_(pi(i))(dx)`.

Thus micro-control and spatial position are independent conditional on retained control according to the specified template. The endpoint guard checks this, rather than merely checking the marginal micro-control distribution. Substitution proves

`mu'_j = sum_(a,f) (L W_f)_(a,j) f_*nu_a = sum_b L_(b,j) nu'_b`.

Induction yields exact joint endpoint mass measures at every allowed packet boundary. The implementation constructs a reduced ControlPacket from total mass per (source class, target class, affine map), reusing the existing affine BRC and moment_action. Consequently degree<=2 conditional moments propagate exactly, without implying complete path memory.

<a id="section-5"></a>

## 5. Concrete 256-to-28 six-phase model

Micro-control is `(r,e)` with r in Z/4 and e in {0,1}^6. Here r is REQUIRED to equal x_1 mod4. Retained control is `(r,k)` where k=sum e; 4*64=256 micro-controls become 4*7=28 conditional classes. Conditional on (r,k) AND spatial position, e is uniform over the C(6,k) masks with k occupied channels. The fixed lift therefore has entries 1/C(6,k) on each fiber.

At global time phase phi=t mod6, define sigma(r)=+1 on {0,3}, -1 on {1,2}, and

`g_phi(r,e)=1+(sigma(r)/2)*(e_phi-k/6)`.

It has conditional mean 1 but generally differs between masks in the same class. With retention lambda=3/4 and p_k=(k+1)/8, choose the +e_(phi+1) motion with relative weight p_k and the negative motion with weight 1-p_k. The positive branch replaces k by 6-k; the negative branch retains k. Both update r by the actual first-coordinate change, so no geometric residue is independently resampled. Finally the actual environment operation distributes the occupied channels uniformly among masks of the new count.

The last operation is a declared material/control redistribution, not a coordinate relabeling or an operation secretly performed by the compiler. Its physical implementation and cost are not established. The transport step is a native unit-axis move; the full block has a declared discrete clock duration, not an empirical time calibration. Removing redistribution yields a different model and fails the certificate in all six phases.

For each affine motion, the conditional average of g_phi is 1 and the new fine mask distribution is exactly its target lift row. This directly proves the coefficientwise certificate. All six phases were also checked on all finite fibers: 512 nonzero-target equalities per phase, 3,072 total. The six strong mass-partition tests all reject the same 28 classes; all phase-addressed raw row signatures together distinguish all 256 micro-controls.

The full joint endpoint distribution was explicitly expanded over six steps and matched against reduced execution followed by lift. All six motion axes were used. Spatial r=x_1 mod4 was checked for every reached point; conditional degree-two moments also agreed. Raw mass vectors and the lifted 28-class vectors agreed for 60 consecutive phase-varying steps.

Each reduced row has total mass 3/4. Reusing the prior ControlMassQuotient reduces the 28-state kernel further to the scalar 3/4 for MASS-ONLY observation; effect-valued merging to one class is rejected. Thus 28 is not a universal minimum or a necessary size for all observers.

Although some raw row masses are 17/16>1, all-depth mass is controlled. Put `h_phi(i)=1+3g_phi(i)`. Since each target lift averages every g to 1,

`W_phi h_(phi+1)=h_phi-1`.

The finite time-periodic positive potential proves stability directly. A frozen-phase integer certificate 4h_phi was checked on the full 256-state matrix by the existing recurrent verifier. The six-phase reduced cycle has exact potential 4096/3367. Counting every tick, an admissible unit input has all-depth mass 4; a raw point input has total `1+3g_initial(i)` under this reset model.

Storage qualification: 28 denotes dynamic control classes, not all memory. Tracking six-axis conditional second moments uses 28*28=784 rational slots rather than 256*28=7168. Full endpoint measures may require growing support. Lift templates, code, certificate construction, bit lengths and the redistribution itself have costs. No production speedup, minimal bit bound or Nollm semantic gain is asserted.

<a id="section-6"></a>

## 6. Retain a failed lift as an algebraic residual, not a false certificate

For any proposed lift define Q=LWP and E=LW-QL. The diagnostic returns E even when certification fails. E is signed bookkeeping and must not enter the positive BRC carrier as a branch weight.

An exact telescoping identity is

`L W^n - Q^n L = sum_(j=0)^(n-1) Q^j E W^(n-1-j)`.

It follows by expanding each summand; adjacent terms cancel. In a submultiplicative norm with q=||Q||, w=||W||, delta=||E||,

`||L W^n-Q^n L|| <= delta sum_j q^j w^(n-1-j)`.

If q,w<1 then `||L W*-Q*L|| <= delta/((1-q)(1-w))`, and exactly

`L W*-Q*L = Q* E W*`.

The row-sum norm example L=(1/2,1/2), W=diag(1/2,3/4) gives Q=5/8, E=(-1/16,1/16), exact all-depth discrepancy norm 1 and upper bound 4/3. Ten finite telescoping cases and the star identity were verified. This bound is sufficient, not necessary; noncontractive raw row norms do not imply instability, as the 256-state example shows. No unsafe lift is approved by this diagnostic.

<a id="section-7"></a>

## 7. Reuse, validation and literature

Executed byte-identical existing modules: brc_transport, brc_histogram, brc_control_port, brc_control_mass, brc_weighted_recurrent. Their Git blob hashes are in RESULTS.json. The new module extends T0 BRC with a different, restricted-initialization certificate; no new top-level family is created. The finite-control source and prior strong quotient do not implement this left-intertwining interface.

Thirteen new check groups pass (including the partial-redistribution continuation in section 9). Tests include random product tables, explicit common-cause and weight-selection defects, real-reset versus erased-correlation stability, mass/effect separation, every finite model phase/fiber, exact joint endpoints, 60-step evolution, integer stable and divergence certificates, residual propagation, zero-support counterexample, and invalid inputs/time binding. This is local verification, not independent review, Lean formalization, whole-project integration or a production memory benchmark.

External comparison (original author/research sources; abstracts/metadata inspected, not claimed full-text reviews):
- Rogers and Pitman, Markov Functions, Annals of Probability 9(4), 1981, DOI 10.1214/aop/1176994363. Publisher page access was insufficient for a full-text check.
- Jeffrey Kuan, Stochastic Fusion of Interacting Particle Systems and Duality Functions, arXiv:1908.02359. Rogers-Pitman-based stochastic fusion is explicitly described in its abstract.
- Xavier Boyen and Daphne Koller, Tractable Inference for Complex Stochastic Processes, UAI 1998; arXiv:1301.7362 is the later archive entry. This concerns controlled approximation of evolving belief states, not a guarantee that arbitrary product factorization stays exact.

All proof claims above stand on the displayed finite identities and stated assumptions, not on transferring conclusions from the external models.

<a id="section-8"></a>

## 8. Next exact frontier

The complete-redistribution example is deliberately favorable. Replace it by partial/local mixing or a memory-preserving environmental interaction and test how E accumulates, whether a finite expanded conditional template closes, and whether its real computational/communication cost is lower than the uncompressed baseline. Do not erase correlations or spatial residue consistency in order to obtain an apparent benefit.

<a id="section-9"></a>

## 9. Further continuation: partial redistribution and an exact threshold

The immediately following partial-mixing unit was executed, not left only as a suggestion. In the two-bit witness, after each gain retain the pair with probability 1-theta and redraw it independently with probability theta. Theta is an actual model parameter in [0,1], not an approximation knob of the observer. The four-state mass kernel is

`W_theta=diag(9/8,3/8,3/8,9/8)*((1-theta)I+theta J/4)`.

The existing strong mass quotient groups the two equal-bit states and the two unequal-bit states. This preserves the correlation class rather than assuming independence, and gives

```
Q_theta = [[(9/8)(1-theta/2), (9/8)theta/2],
           [(3/8)theta/2,     (3/8)(1-theta/2)]].
```

`det(I-Q_theta)=(21theta-5)/64`. For theta>5/21, the inverse produces positive potential

`h_equal=(40+48theta)/(21theta-5)`,
`h_unequal=(-8+48theta)/(21theta-5)`.

Hence the exact existing positive-potential criterion proves convergence. For theta<5/21 the first potential would be negative, contradicting finite positive all-depth mass; at equality I-Q is singular, also incompatible with a finite Neumann series. Therefore

`ALL_DEPTH_MASS_FINITE iff theta>5/21`.

For a uniform initial pair the total is `(16+48theta)/(21theta-5)` on the convergent side: 112 at theta=1/4, 80/11 at theta=1/2, and 4 at theta=1. The rational expression below the threshold is NOT an interpretation of a divergent positive series.

The global uniform one-class conditional lift remains invalid for every theta<1, but the two-class strong mass quotient works for every theta in [0,1]. Thus partial mixing need not force a full four-state expansion: retaining the one equal/unequal interaction distinction is sufficient for the declared mass observer. This is an exact parameterized diagnostic, not a universal physical threshold.

A thirteenth check group compared the exact two-state and four-state recurrent classifiers at 102 rational theta values, including the critical value. All agree. This strengthens the next frontier: locally mixed multi-axis environments should retain an explicitly verified correlation partition/template instead of assuming that incomplete redistribution has already erased dependencies.
