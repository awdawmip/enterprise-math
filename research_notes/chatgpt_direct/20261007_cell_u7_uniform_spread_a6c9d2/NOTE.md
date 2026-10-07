# U7 — uniform spreading closes the unbounded co-moving loophole

Event: EM-20261007-CELL-U7-UNIFORM-SPREAD-A6C9D2
Status: NEW_CONDITIONAL_THEOREM / ACTUAL_TYPED_BRC / UNREVIEWED / NOT_NATIVE_FORCE
Global read: awdawmip/chatgpt-global-knowledge@5384949209cbaffbfd8b5d34da90a63f26f36675.
Initial current EM read: 71b905027327eadf3417cddd6b4dcb54cc3eac71.
Researcher: EM-DIRECT-7A7883; activity RA-340F62216896447E8083980E.
Own public session: MCP-53fb0730eb0d40809d9a98fa23b855d3.
Logical conversation: chatgpt-heartbeat-cell-attraction-20261006-8b74f0 (self-chosen, not platform-attested).
Registration observed at fe7bd400805b593ecaf77b140c0a7b62fa55b3d0, activity blob50a498b6445623d38d21db995bac9a22e0866b7f. No Task/CLAIM/open/Result or review authority is inferred.

## 0. Exact advance and scope

U6 established finite-region escape/exposure bounds but explicitly left an unbounded moving cluster open. This unit does NOT repeat that argument or add attraction, reinjection, walls, timing, or a selection rule. It proves a stronger uniform bound for the unchanged U5 active/dormant circuit, independent of ALL choices of the occupied sets. The sets need not remain in a common finite region. Indeed the field theorem does not require them to have bounded cardinality.

For fixed 0<rho,epsilon<1 and finite initial total response M, there is an explicit finite C=C(rho,epsilon) such that, for every layout schedule and all n>=0,

    sup_(z,p) max{ F_n(z,p), D_n(z,p)/h } <= C*M/(n+1)^3,
    h=(1-rho)/epsilon.                                           (T1)

Here F,D denote TOTAL readouts summed over birth-sources only for this bound; full source-labelled CWM state remains in the circuit. Equivalently apply the bound to each source and sum. Consequences include: response in any uniformly finite collection of Cells tends to zero even if that collection moves arbitrarily; no positive-weight indefinitely moving trajectory remains under the existing finite-N, fixed-wait selector; and a storage-aware all-future position-law error bound without U6's exit stopping. These are not native-force claims or calibrated physics.

Sources consumed: U5@e077563ca390c1f964ad4d4e856c098c00f9f0b5; U6@f1bfcc952542706d87db4aec1c106f5de42a96aa. The new cross-line note research_notes/chatgpt_direct/20261007_residual_triad_interface_7c2e8a/NOTE.md at current EM was also read. It supplies conditional event-assembly diagnostics, NOT an instantiated native force law. Its distinction between action events and displacement is preserved; no U2 port triple is promoted to native TRIADIC_CLOSURE_E.

P000/X6 and separate time typing are unchanged. n is the declared circuit update index. Positive response mass, CWM count/dominant, mathematical comparison density, normalized selector weight and physical force/energy are different types. All infinite statements below concern this exact mathematical continuation. No proof is asserted for a new native incidence table that fails the checked hypotheses.

## 1. A common infinite reference measure, not a physical equilibrium

Write the inherited material scattering K(q,p): 1/3 if q=p, zero if q=-p, and 1/15 on the ten other-axis ports. At an empty Cell it is 1/12 on every port. Both tables have unit ROW and COLUMN sums. Column conservation alone would not suffice. The source's existing incidence audit already demonstrated why a different incidence can fail the row condition.

Let P_X scatter locally and then stream one native edge. Streaming is a permutation of Cell/port slots. Therefore P_X preserves the counting measure on Z^6 times twelve ports for every X, including infinite X. It is not necessary that P_X be symmetric, nor do different P_X need to commute.

The original U5 mass update is

    F'=rho P_X F+epsilon D,
    D'=(1-rho)F+(1-epsilon)D.                                  (1)

On E=Z^6 x {12 ports} x {A,D}, set reference weights mu_A=1, mu_D=h=(1-rho)/epsilon. Then T_X mu=mu for EVERY X: the active row reads rho+epsilon*h=1, and the dormant row reads (1-rho)+(1-epsilon)*h=h.

This reference measure has infinite total mass. It is a proof device, not a realizable finite-budget stationary field and not a counterexample to U6's absence of a finite-mass stationary state.

For density f=(F,D/h), let H_X f=mu^(-1)T_X(mu f). H_X is a positive row-stochastic operator preserving mu. It contracts weighted l1, l2 and linfinity norms. Define U=||f||_(2,mu)^2 and A=||f||_(1,mu). The weighted adjoint H_X* is likewise Markov and mu-preserving. It is used for duality only, not backwards physical evolution.

## 2. Exact Jensen loss and a layout-independent connected comparison graph

For a row-stochastic H preserving mu, expanding a finite weighted square gives

    ||f||_2^2-||Hf||_2^2
      = sum_y mu_y sum_(i<j) H(y,i)H(y,j)(f_i-f_j)^2.            (2)

All right-hand terms are nonnegative comparison observations. No signed difference is submitted to positive BRC as physical response. Finite support first suffices; monotone/local approximation extends the estimates to l1 inputs.

In H_X, the D row at (z,p) has input weights epsilon on A(z,p) and 1-epsilon on D(z,p). The A row has input weight 1-rho on D(z,p) and the streamed active inputs rho K. Hence the loss is at least

    c_v sum_(z,p)(f_A(z,p)-f_D(z,p))^2
    + c_e sum_(z,p,q != -p)(f_A(z,p)-f_D(z+d(q),-q))^2,        (3)
    c_v=(1-rho)(1-epsilon), c_e=rho(1-rho)/15 >0.

The bound uses exactly the edges nonzero in BOTH the empty and material tables. The extra bulk edge and all other Jensen pairs remain nonnegative and are simply not needed in this lower bound.

For H_X*, the corresponding graph is (3) with A and D exchanged in its second sum, with the SAME coefficients. This matters: one cannot assume that a forward smoothing bound automatically gives an adjoint bound. Both are certified here.

Let E_ref(f)=sum_(sector s,port p,axis i,z) mu_s (f_s(z+e_i,p)-f_s(z,p))^2. We show

    E_ref(f) <= C_J (||f||_2^2-||H_X f||_2^2),                (4)
    C_J=9216*mu_max/min(c_v,c_e),

and the same for H_X*. No layout-dependent constant occurs.

Explicit path proof: in the forward comparison graph, A(z,p) can connect to A(z,r) in two edges through D(z+d(a),-a), choosing a != -p,-r. For a spatial displacement +e_i, first change the input port to r != -e_i if needed, cross to D(z+e_i,-e_i), take its vertical edge, and change that A port back to p. This uses at most six comparison edges. For D endpoints add the two vertical edges, giving at most eight. For the adjoint graph swap sectors. These are COMPARISON paths between input slots, not a physical motion or a temporal response trajectory.

There are 2*12*6=144 reference templates per graph. For any translated graph edge, a path occurrence of a given template aligns with it for at most one translation. Cauchy--Schwarz along paths bounds its load by at most sum_templates(mu_s*L_template^2) <=144*64*mu_max=9216*mu_max. Dividing by the minimum positive coefficient in (3) proves (4). Every template and edge has been checked; the loose constant follows from the symbolic construction even without optimizing the finite table.

## 3. Six-dimensional Nash bound without trigonometry or a Fourier calculation

Let Q_l average translations over {0,...,l-1}^6 separately in every sector/port. Positive convolution gives

    ||Q_l f||_2^2 <= A^2/(mu_min*l^6).

A telescoping path for each translation, followed by Cauchy--Schwarz and translation-invariance, gives

    ||f-Q_l f||_2^2 <=36*l^2*E_ref(f).

Thus

    U <=72*l^2*E_ref(f)+2*A^2/(mu_min*l^6).                    (5)

For f not zero, U<=A^2/mu_min. Set R=(4A^2/(mu_min U))^(1/6)>=1 and l=ceil R<=2R. The second term in (5) is <=U/2. Rearrangement gives

    U^(4/3) <=576*4^(1/3)*mu_min^(-1/3)*A^(2/3)*E_ref(f)
             <= C_N*A^(2/3)*E_ref(f), C_N=1152/mu_min.        (6)

Here mu_min<=1. The displayed powers are symbolic comparison inequalities, not computations of native square roots or trigonometric values. The checker uses the equivalent cubed inequality U^4<=C_N^3 A^2 E_ref^3, with exact rational observations. The power three in T1 comes from the six-dimensional lattice-volume bound, not the integer quantity N being square or prime.

Nash/adjoint methods for time-inhomogeneous Markov chains have established prior art: L. Saloff-Coste and J. Zuniga, Merging for inhomogeneous finite Markov chains, part II: Nash and log-Sobolev inequalities, arXiv:1104.1560v1, Ann. Probab.39(3),1161-1203 (2011), DOI10.1214/10-AOP572, in particular Theorem2.3 and its proof. Official metadata and parsed PDF sections2.1-2.3 were consulted, not the entire paper; the screenshot endpoint failed. That paper's displayed setting is finite-state, whereas the above elementary cube proof directly handles our infinite lattice. No theorem is blindly transferred, no classical numerical solver is run, and no claim of inventing the general Nash method is made.

## 4. Noncommuting arbitrary schedules: uniform n^-3 density bound

Let a=(C_J C_N)^(-1). Apply (4)-(6) along ANY sequence of occupied sets. Mass A=M is constant for nonnegative density. Therefore

    U_n-U_(n+1) >= a*U_n^(4/3)/M^(2/3).

With V_n=U_n/M^2, convexity of t^(-1/3) gives V_(n+1)^(-1/3)>=V_n^(-1/3)+a/3 when V_(n+1)>0; a zero term makes every later term zero. Hence, for any interval of k>=1 steps,

    ||H_(interval) f||_2 <= (3/(a*k))^(3/2)||f||_1.            (7)

The same holds for every reversed sequence of adjoint operators, using their separately proved graph estimate. Split an n>=2 interval into floor(n/2) and ceil(n/2), both >=n/3. Duality and Cauchy--Schwarz give

    ||H_(interval)||_(l1->linfinity) <= (9/a)^3/n^3.

For n=0,1 use linfinity contraction and ||f||_infinity<=M/mu_min. A deliberately conservative rational constant valid for all n is

    C=max(8/mu_min,(18/a)^3).                                 (8)

This proves T1. The operators can change at every stage and do not need to commute. Since the estimate holds for EVERY fixed sequence, it also holds pathwise for schedules selected adaptively from the evolving field. There is no conditioning of a single response ray on an unrecorded future decision.

At rho=1/4,epsilon=1/8, the declared coarse C is 771837833825395905352477704192000. It is VERY loose, not a prediction of any practical stopping stage. Short-run tail bounds obtained from this constant can be trivial (one). The value of this estimate is its uniformity and summability, not a newly calibrated timescale. Finite template loads admit smaller constants; optimizing them is not necessary to close the present question.

## 5. Moving observation sets, selector activity, and full-future state accuracy

For ANY sets B_n of at most V Cells, allowed to move without bound,

    sum_(z in B_n,p)(F_n(z,p)+D_n(z,p))
        <=12*(1+h)*V*C*M/(n+1)^3 ->0.                        (9)

Thus even a fixed-radius observation neighborhood carried by a migrating finite cluster cannot retain a nonzero asymptotic response fraction in this circuit. No common containing box is assumed. If an observed region retains fraction eta>0 of M, its cardinality must grow at least eta*(n+1)^3/[12*(1+h)*C]. This is an asymptotic comparison, not a physical radius law.

Let N<infinity be the number of labelled materials, and reuse U3/U5's positive current-active request choice with constant kappa>0. A moved actor must have chosen a non-wait request. The sum of cross-source responses at all actors is no larger than the full active response there. On EVERY past history,

    E[number of moved actors at stage n | past]
        <=12*N*C*M/[kappa*(n+1)^3].                           (10)

Summing n>=1 gives finite expected total moves. Therefore the event of infinitely many moves has TRIAL measure zero. It follows that each finite group eventually stops at some random finite stage almost surely, even without assuming it remains bounded. This is not a deterministic stopping time, zero field, native stable force balance, or natural matter impossibility. Exceptional zero-measure histories are not excluded. An n>h tail certificate follows from sum_(n>h)(n+1)^(-3)<=1/[2(h+1)^2].

For two initial states with the same labelled material positions and source-wise augmented total contrast delta=||F-G||_1+||D-E||_1, couple the selector laws until the first positional disagreement. While their positions agree, absolute contrast is dominated by a positive field of mass delta propagated by that common sequence. Apply T1 pathwise and use the existing local normalization/identical-conflict-kernel bound. Summing first-disagreement probabilities gives

    TV(entire future labelled-position trajectory laws)
       <=min(1,18*N*C*delta/kappa).                           (11)

We used sum_(n>=1)n^(-3)<=3/2 conservatively. No exit stopping is needed. This repairs U6's remaining unbounded-observation restriction for this exact future language. It does not compare direct field observations, CWM count/dominant, all raw paths, arbitrary joint packet gates, old-command rearming, or native forces. Such observations have not been licensed for deletion.

## 6. Actual BRC certificates and limitations

New module uniform_spread.py imports unchanged lifecycle.py blob389bd51a2a71a62a4c533ef781920bef00783bc3, then the unchanged U4/U3/U2/BRC chain. Existing kernel functions/classes are not changed. The inherited BRC adapter removes only its two unused relative imports and checks function/class AST identity. Forward field evolution ACTUALLY calls U5 local_release_step; the proof adjoint is constructed from the same positive edge table and checked by weighted duality. Variance pairs carry positive BRC products, while norm differences remain comparison observations.

check_u7.py verifies all288 translation templates (two graphs, all24 fibres, all6 positive spatial edges),36 full finite-support Jensen cases across three parameter pairs and two layouts, exact row and column checks, cube-average certificates for sides2/3, and five-stage full source-labelled propagation under a declared translating layout. The latter is a CONTROLLED layout illustration, not an actual chosen material-motion history. No all-schedule simulation or infinite-trajectory enumeration is claimed.

Final counts/hashes and byte-identical same-author isolated replay are recorded in CHECKPOINT.json after actual execution. Development transcription/typing issues were fixed before the final executable; they are not structural residuals. Neither this checker nor a replay constitutes independent review. Proof estimates can be extremely loose and are not fitted to the finite samples.

## 7. What is now closed, and what remains genuinely missing

The fixed finite-budget U5 baseline does not sustain a finite local response packet, even by migrating without bound. Its active/dormant redistribution and default geometry cannot be promoted into a sustaining force law. Continued parameter sweeps inside this same class will not repair the proved obstruction.

A proposed new native material mechanism must therefore explicitly change at least one relevant premise: the common spatially uniform reference measure, the uniformly mixing transport graph, fixed positive storage/release timing, finite unsourced budget, or the present query/eligibility rule. Breaking a premise is NOT sufficient proof of confinement; the proposed mechanism still needs its own source-grounded native event law, signed triad legality, indivisible-action/readout bridge, third-action provenance, reaction, and position compatibility. Merely installing a forced return, a target shape, or a matching objective would be another uncalibrated candidate.

The independent native-interface gap remains OPEN. The cross-line triadic assembly is consumed at its stated TEST_ONLY strength, not treated as the missing force law. No prime formula, perfect-square shell, modified P000, mathematical admission or parent-objective completion is claimed. Preserve U1-U6 rather than redoing their proofs. The next productive unit is a source-grounded spatial retention/action interface outside the ruled-out class, not another waiting-rate adjustment.
