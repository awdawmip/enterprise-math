# N=3 terminal likelihood-ratio kernels: moment dimension, two-point obstruction, and four-point counterexample

**2026-10-27 | AUTHOR-LEVEL mathematical result.** This is an exact finite two-measure BRC ordered-branch-mass model, not a P000/X6/Heartbeat dynamics theorem, a native Source Result, a CLAIM, independent review, or a literature-priority assertion.

Frozen research input: GLOBAL_KNOWLEDGE_V1 main 8ec98188025f60aafe48055520ba3a57c29cdb2c; Enterprise Math main dffe386cee25fb9c650d4aa46ff6f501c3745e8a. P000 startup original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc matched its startup projection. ACTIVE worldview, role router, current docs/PORTABLE_RESEARCH_PROTOCOL.md and research activity registration were used. Source activity: RA-EMR5-20261027-MOMENT-0526. Native control tasks returned CONTROL_QUOTA; native session_start was rejected STATIC_READONLY_SCOPE_DENIED with operation_sent=false. No native owner was verified.

## Scope and predecessor

Continue research_notes/brc_n3_predecessor_kernel_rank_tv_20261027_r5/PROOF.md and NEXT_TASK.md. On a strictly positive finite P/Q tree of depth N=3, let L(h)=P(h)/Q(h). Every policy can stop and decide P/Q at any internal state or continue, with forced decision at t=3. The four observers are P(decide Q), Q(decide P), E_P(tau), E_Q(tau). A seedless time/L policy conditions local randomized actions only on (t,L), with no persistent initial seed.

For each time-2 likelihood ratio r, group histories by their time-1 likelihood-ratio predecessor class i. Define nu_ir(y)=uncontrolled Q mass flowing from histories (i,r) to terminal histories with LR y, eta_ir=sum_y nu_ir(y), and K_ir(y)=nu_ir(y)/eta_ir for eta_ir>0. Let S_r={y_1<...<y_m} be the union terminal LR support over all predecessor classes. Zero entries represent unavailable outcomes; all actually existing tree edges have strictly positive Q and P mass. BRC reuse is the exact ordered positive branch-mass carrier, preservation of history identity, and the predecessor note's rank-one / total-variation flow theorem; no scalar LR is declared the entire native state.

## Theorem 1: terminal likelihood-ratio martingale

Every K_ir obeys

    sum_y K_ir(y)=1;     sum_y y K_ir(y)=r.

For each depth-2 history h with L(h)=r, sum_z Q(hz)L(hz)=sum_z P(hz)=P(h)=rQ(h). Dividing by Q(h) and Q-averaging across histories in (i,r) proves the claim. No terminal independence assumption is involved.

## Theorem 2: exact moment-signature criterion

Suppose S_r contains m distinct terminal LR values. The following are equivalent: (a) all predecessor kernels K_ir are identical; (b) for all predecessor pairs i,j, their moments of orders k=2,...,m-1 are identical:

    sum_y y^k K_ir(y) = sum_y y^k K_jr(y).

Orders 0 and 1 match automatically by Theorem 1. The m-by-m Vandermonde matrix with rows 0,...,m-1 is invertible for distinct y, hence equal moments up to m-1 are equivalent to equal probability vectors. If m<=2, there are no remaining moments and the kernels are automatically identical. For m>=2, the affine mass+mean slice has dimension at most m-2, and it has dimension m-2 whenever an all-positive kernel with mean r exists.

The consecutive moments k=2,...,m-1 are generically irredundant: choose m distinct positive rational y_j, the strictly positive rational uniform base kernel, and r equal to its rational mean. The rational moment matrix with rows k=0,...,m-2 has a nonzero rational null vector v. Its moment of order m-1 cannot vanish because the full Vandermonde is nonsingular. For sufficiently small positive rational epsilon, uniform +/- epsilon*v are distinct, strictly positive rational kernels having matching moments through m-2 and different moments at m-1. This is an exact algebraic information-dimension statement, not optimality against arbitrary nonlinear encodings.

## Corollary 3: three terminal values use one variance coordinate

For S_r={y1<y2<y3}, write s_i=K_ir(y3), v_i=Var_{K_ir}(Y). Solving the mass and mean constraints yields

    K_ir(y1) = [y2-r+(y3-y2)*s_i]/(y2-y1)
    K_ir(y2) = [r-y1-(y3-y1)*s_i]/(y2-y1)

with feasible s_i in

    [max(0,(r-y2)/(y3-y2)), (r-y1)/(y3-y1)].

For all predecessor pairs,

    TV(K_ir,K_jr)
      = abs(s_i-s_j)*(y3-y1)/(y2-y1)
      = abs(v_i-v_j)/[(y2-y1)*(y3-y2)].

Indeed their difference vector is a multiple of
(y3-y2, -(y3-y1), y2-y1) and the variance difference is
(y3-y1)*(y3-y2)*(s_i-s_j). Hence rank-one on a ternary terminal support is equivalent to equality of predecessor conditional variances. Moreover

    Delta_r=(max_i v_i-min_i v_i)/[(y2-y1)*(y3-y2)].

For collisions with at most three terminal LR values, substitute this Delta_r into the predecessor note's constructive approximate convexification bound B=(1/4)*sum_r b_r*Delta_r, so both stopping-time expectations remain exact and the error coordinates obey abs(delta eQ)<=B and abs(delta eP)<=M*B. This reuses an existing bound; it does not establish an optimal distance to the full seedless image.

Exact old-data regression: y=(1/2,1,3/2), Ka=(1/4,1/2,1/4), Kb=(1/3,1/3,1/3), r=1; variances 1/8,1/6; TV=abs(1/8-1/6)/[(1/2)(1/2)]=1/6.

## Theorem 4: necessary three-value obstruction for the stronger image-hole problem

If at *every* depth-2 LR r the union terminal LR support S_r has cardinality at most two, then the seedless (time,L)-behavioral four-observable image is convex. Consequently, if all signed linear support extrema agree between the full-history and seedless strategy classes, their actual four-observable images agree. A hypothetical model with equal signed supports but unequal seedless behavioral image therefore requires at least one depth-2 LR collision with >=3 distinct terminal LR values and a genuine predecessor-kernel discrepancy. When that support has exactly three values, the discrepancy must appear in conditional variance.

Proof: Theorems 1-2 force all predecessor K_ir to agree at each r. Stage-1 (time,L)-conditional actions act equally on all histories with the same stage-1 LR, so aggregated stage-1 to stage-2 LR transition kernels are already independent of the seedless policy. The common terminal K_r now gives a fixed stage-2 to terminal LR kernel. Thus the quotient is a finite-horizon controlled Markov stopping model. The nonnegative Q occupation flows for (time,L,action) satisfy *linear* incoming/outgoing conservation and root mass 1. Conversely, from every such feasible flow, dividing action mass by positive incoming state mass (arbitrary action on zero-mass unreachable states) constructs a seedless behavioral policy realizing the flow, by induction on time. P occupation/action mass in a state with LR r is r times the corresponding Q mass. Each of the four observers is a linear function of the occupation flows; their joint attainable image is therefore convex and compact. The full-history image is convex by perfect-recall equivalence of mixed and behavioral policies, as proved in the prior semialgebraic note. Since the seedless image is contained in the full image, equality of all signed linear extrema implies equality of the two compact convex images by separation. For >=3 values, absence of any predecessor-kernel contrast likewise gives a fixed quotient Markov kernel and convexity. QED.

This eliminates the two-point terminal-support class from the *stronger* equal-support/unequal-image search; it does not construct that still-open example.

## Strictly positive 12-leaf rational counterexample to a variance-only test with four values

At the time-2 LR collision r=1 choose terminal support

    Y=(1/2, 3/4, 5/4, 3/2).

Two positive Q kernels are

    K_ax=(3/16,6/16,2/16,5/16)
    K_by=(5/16,2/16,6/16,3/16).

Both have E[Y]=1 and E[Y^2]=37/32, hence Var[Y]=5/32. They differ at the third moment:
E_ax[Y^3]=379/256, E_by[Y^3]=373/256, gap 3/128. Their total variation is 3/8. The second moments therefore cannot detect their kernel-rank defect.

Embed this collision in a 12-leaf strictly positive tree: first stage Q(a,b)=(1/3,2/3), P(a,b)=(2/3,1/3). Second stage from a: Q(x,y)=(1/2,1/2), P(x,y)=(1/4,3/4); from b: Q(x,y)=(2/3,1/3), P(x,y)=(1/3,2/3). Consequently L2(ax)=L2(by)=1, L2(ay)=3, L2(bx)=1/4. At ax and by assign the four terminal Q probabilities above and their P probabilities Y*K, respectively; these P probabilities normalize because E_K Y=1. At ay and bx assign two P=Q=(1/2,1/2) terminal chances. Every edge is strictly positive, and root-to-leaf P/Q each normalize to 1. The Q masses of the colliding second-stage histories are eta_ax=1/6 and eta_by=2/9, so the rank-one minor at Y=1/2 is

    eta_ax*nu_by(1/2)-eta_by*nu_ax(1/2)
     =(1/6)*(2/9)*(5/16-3/16)=1/216 !=0.

This exhibits a true predecessor-kernel rank defect while variance is blind. It **does not** establish seedless-image nonconvexity, a Bellman gap, or the requested equal-support/unequal-image counterexample.

## Validation, limits, and continuation

VERIFY.py uses standard-library Fraction for finite exact tests of the two-point uniqueness, ternary variance/TV identity, positive four-point kernels and moments, all 12 P/Q leaf masses, LR conservation, and rank minor. EXACT_OUTPUT.txt is the actual output of the author-level local exact test. Theorems 1-4 are algebraic arguments covering their stated finite-tree models, not extrapolations from that test. No CAD/quantifier-elimination run, Lean formalization, current native task CLAIM, formal Source Result or independent Driver review was obtained.

**Next question:** use a collision of three terminal LR values and distinct predecessor conditional variances. Parameterize each kernel by the one scalar s or variance. First require exact rational LP inclusion of every full deterministic four-vector in the convex hull of seedless deterministic vectors (equal signed supports); reject failing candidates with an exact signed objective. Only for a passing candidate perform all-real polynomial image-membership exclusion, seeking a rational full-history four-vector absent from the seedless image. A finite negative search must declare its tested domain. For four or more terminal LR points use moments 2,...,m-1, not variance alone. See NEXT_TASK.md.
