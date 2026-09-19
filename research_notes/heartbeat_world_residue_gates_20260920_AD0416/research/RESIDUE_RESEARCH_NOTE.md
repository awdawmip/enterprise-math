# Heartbeat World: local residue gates and guarded BRC transport

Researcher-ID: `EM-DIRECT-AD0416`
Research-Activity-ID: `RA-37C0A30C7B1F5A338F03D186`
Progress-Event-ID: `heartbeat-residue-gates-20260920-AD0416`
Session: `chat-local-reciprocal-ceec8bd1559acdf8c10ebc9b` (continuing local key, not a platform ID).
Status: `RESEARCH_CONSTRUCTION / SCOPED_PROOFS / EXECUTED_EXACT_CHECKS / NOT_FOUNDATION`.
Read EM: `999ed1daf4c36ddf22374681949da532eb801504`.
Read GLOBAL_KNOWLEDGE: `f0f19b02ddb0c7c894973f39230d3c41ce93f0df`.
User objective: advance Heartbeat World and extend BRC beyond the prior phase-conjugate baseline.

## 1. Exact scope and real reuse

Heartbeat World remains native six-dimensional discrete Cell space plus one separately typed time dimension. P000, the native X6 definition, the naming contract, final-address distinction and joint-observer constraint are unchanged. Work here is on signed relative displacements about a chosen Cell, not a final nonnegative address codec. A cyclic ordering of axes and a dyadic partition alignment are explicit research parameters; neither is an ontic origin or the whole native rotation group. The local rule is a permutation of positions, not a force-equilibrium claim or a two-body memory-binding rule.

The previous phase_algebra baseline proves that a readout-only pulse cannot manufacture material evolution. The new variable is an explicit position-dependent gate; it is not a renamed coordinate change. The old heartbeat_algebra, phase_algebra, brc_transport, brc_histogram and predictive_quotient files were reused unchanged and checked against current remote Git blobs. The standalone package retains the previously disclosed small prime-valuation dependency excerpt; it is not a full holonomy-module test. No Nollm runtime, LLM semantics or memory-store mutation occurred.

Tool resolution: T0 affine/histogram and T5 radix helpers REUSE_EXECUTED; T6 predictive partition REUSE_EXECUTED; source-/target-control and temporal ports COMPOSE_APPLIED. Guarded finite-control affine kernels and geometry gates are EXTEND_EXISTING_TOOL / DOMAIN_OPERATOR candidates within T0, not a new top-level family. Existing finite recurrent positive-mass BRC does not by itself provide joint coordinate moments behind congruence guards. This is a narrow extension of the earlier one-step conditional-moment boundary, not a claim of inventing Markov additive processes, block permutations or partition refinement.

## 2. A geometry-derived unit gate

Use zero-based indices i modulo6 in code; human axes are E_1,...,E_6. At width1 define

    c_i(x) = (x_i + x_(i+1)) mod2,
    G_i(x) = x + (-1)^c_i(x) e_i.

This is exactly an adjacent-pair exchange. Holding the other coordinates fixed, let a=x_(i+1) mod2 and write x_i=2h+a+epsilon with epsilon=0 or1. Replace epsilon by1-epsilon. Thus G_i is a bijection, G_i^2=id, and each execution moves exactly one primitive native step. Only the selected coordinate moves; the neighboring axis component selects the pairing alignment. There is no semantic index or nonlocal lookup.

For coarse width m, write x=mq+r componentwise, retain r, and apply the same gate to q. The lift is x -> x+m*(-1)^(q_i+q_(i+1))e_i. It costs m fine primitive steps, not one free jump. At m=2^d this is executed using the earlier exact6d-step analysis/synthesis functions. A fixed-width family preserves the fine remainders; unrestricted width changes need another control contract.

The gate depends on actual selected geometry. Under a change of coordinate anchor, the partition alignment must be transported too. Keeping the formula but silently changing the physical alignment is not a passive frame change. Using the existing frame program, F_(t+1) G_i F_t^-1 gives the same material gate;120 such checks were executed.

## 3. Equal-cost transport and noncommuting schedules

Let r=x mod2 and s_i=(-1)^(r_i+r_(i+1)). Execute F chronologically as G_0,G_1,...,G_5. Before G_i for i<5, its controlling next bit has not yet changed; at G_5, bit0 already changed. Therefore

    F(x)=x+v(r),
    v(r)=(s_0,s_1,s_2,s_3,s_4,-s_5).

One sweep complements all six parity bits. The s_i are invariant under that complement. Hence for every K>=0,

    F^K(x)=x+K v(r).

The reverse chronological word is F^-1, since each gate is involutive. Consequently three12-tick,12-fine-step programs give x+2v, x, and x-2v respectively: forward/forward, forward/reverse, reverse/reverse. At x=0 their increments are (2,2,2,2,2,-2),0, and its negative. A spatial return is not a return of absolute time.

For neighboring indices j=i+1, the four-gate chronological word i,j,i,j yields

    x -> x + 2 s_i e_i.

The other axis cancels but the ordered loop leaves a spatial correction. Nonadjacent gates commute. At0, words(0,1) and(1,0) give (1,1,0,0,0,0) and(-1,1,0,0,0,0). This is a genuine state-dependent order effect, not failure of scalar addition or multiplication.

There are32 velocity channels, each from two complementary parity vectors. All satisfy product_i v_i=-1. Uniform initial parity makes every nonempty proper sign product have expectation0, yet the sixfold product equals-1. The independent uniform64-sign ensemble has the same polynomial moments through degree5 but sixfold product expectation0. Thus pairwise or even five-way views can miss a specific joint six-axis constraint. This is an exact parity-code observation, not a physical chirality theorem or a claim that every six-axis model has this invariant.

## 4. Random order changes the transport regime without changing work

Choose one of all720 axis permutations uniformly for each complete six-step sweep, independently across sweeps. Every branch visits each axis exactly once and pays exactly6 fine steps. Intermediate queries must retain the selected order or unused-axis mask; the implemented macro packet has a six-tick source/target contract.

For fixed initial c, let s_i=(-1)^c_i. In an order sigma, the increment is

    W_i=s_i*xi_i,  xi_i=+1 if i precedes i+1, otherwise-1.

E[W_i]=0. Disjoint comparison pairs have zero correlation. For adjacent comparisons, enumeration of the six orders of three distinct axes gives E[xi_i xi_(i+1)]=-1/3. Therefore

    C_ii=1;
    C_i,j=-(s_i*s_j)/3 for cycle neighbors;
    C_i,j=0 otherwise.

This matrix is positive definite: C=D_s(I-A_cycle/3)D_s and |z^T A_cycle z|<=2||z||^2, so its eigenvalues lie in[1/3,5/3]. Each sweep complements parity and leaves c unchanged, so subsequent W are independent with the same conditional law. After K sweeps the displacement has mean0 and covariance K C. The centered root-mean-square displacement grows as sqrt(K), versus coherent F displacement proportional to K. This is an exact second-moment statement; full hitting probabilities, ergodicity and semantic coverage are not inferred.

All720 orders produce62 different endpoint increments, not62 equally weighted alternatives. Their multiplicities sum to720. Two sweeps represent518400 schedule paths and715 endpoints. The BRC histogram retains these counts. At K=60 (360 ticks and360 fine steps per path), the exact compressed result from0 has mass1, mean0, diagonal covariance60 and cycle-neighbor off-diagonal-20. The represented720^60 schedule paths were NOT enumerated; the one-sweep laws and finite-control recursion supply the calculation.

## 5. New BRC interface and exact finite-control closure

Let c(x) be a declared finite control. In control c, a branch has positive rational weight w, multiplicity n, integer affine effect x->Ax+b, and a certified destination control d. Denote the old EffectHistogram packet on c->d by K_cd. Serial and alternative composition are

    (K star L)_ce = sum_d K_cd star L_de,
    (K+L)_cd = K_cd+L_cd.

The inner star and plus are the executed original BRC operations, with their weight/action correlation preserved. Source and target time ports must also match. Associativity and distributivity follow by expanding finite sums and using the old laws; only compatible middle ports occur. Replacing these matched transitions by an unconditional Cartesian product changes the measure and is forbidden.

For the gate family take c_i=r_i XOR r_(i+1). Its image has32 states and its kernel over F2 is the single global-complement bit. A G_i update toggles c_(i-1) and c_i; its displacement depends only on c_i. Thus this is an all-finite-word control quotient for the gate family. Distinct controls differ in some c_i and are immediately distinguishable by that gate's displacement, proving32 is the minimum for all-six-gate displacement observations. This says nothing about deleting spatial dimensions or identifying different Cell positions.

For each control retain a homogeneous moment matrix

    M_c=sum_(x:c(x)=c) mu(x) [x;1][x;1]^T.

If H_a is a branch's homogeneous affine matrix, the exact update is

    M'_d=sum_(c,a:c->d) n_a*w_a*H_a M_c H_a^T.

Proof: on every control fiber, weight and affine action are fixed; substitute x'=Ax+b and collect each output fiber. All degree<=2 polynomial observations multiplied by any control indicator are linear functionals of these matrices. Their pullbacks remain in this same finite span. Hence equality of these summaries is preserved by any finite sequence of the declared kernels, even though the maps are globally non-affine. No Gaussian approximation occurs.

Six spatial coordinates require28 symmetric entries per control. The32-control version uses at most896 rational entries; this is a sufficient dimension, not a minimal total statistic or constant bit-memory theorem.96 half-firing gate ticks were computed exactly with all32 sectors active, representing2^96 positive history choices without enumerating them. Occupancy, nonlinear coordinate observations, arbitrary path labels and history-dependent branch probabilities remain outside this lease. Full labels must remain in a richer carrier when those observations are requested.

A small failure witness uses mu=(delta_-e1+delta_e1)/2 and nu=delta_-2e1/8+3delta_0/4+delta_2e1/8. Their global degree-two moments agree. G_0 sends their first-coordinate means to-1 and+1. Residue-conditioned moments distinguish and propagate them exactly. The correct repair is a finite controlling relation, not arbitrarily increasing global moment order.

`ResidueControl.target` proves affine descent, not merely samples it. For full low-bit parity, every integral A,b descends. For neighbor-XOR control at width1, descent holds exactly when A*(1,...,1) has constant parity, because this is preservation of the quotient kernel. At width>1 the implemented contract narrows to translations by width multiples. Other operations reject rather than silently assume safety.

## 6. Actual expansion heartbeat: a boundary and a new exact interaction

The original material A_2 does NOT preserve the32-control quotient: x=0 and x=(1,...,1) have the same c, but c(A_2 x) differs. The unchanged T6 compiler gives (32,32,32,32) for gates alone and (32,64,64,64) after admitting A_2. The64-parity interface handles arbitrary integral affine actions, including expansion, using1792 possible moment entries. Arbitrary floor contractions still do not descend through fixed low-bit parity; retain finer digits or prove another quotient.

Now actually execute, at tick i, A_2 followed by G_i, for i=0,...,5. For any signed integer x, write epsilon=x_0 mod2. The exact complete-sweep rule is

    X_6=2x-2*epsilon*e_5  (zero-based e_5 = human E_6).

Proof: after A_2 the first five injected directions follow the rotating coordinate and have signs s,-s,s,-s,s where s=(-1)^epsilon. The sixth has sign-1, because its successor coordinate is even. The net transported injection is(s-1)e_5=-2epsilon e_5; the underlying six heartbeats give2x.

All output coordinates are even, but the full map is injective onto2Z^6. Given y, recover x_0=y_0/2 and then x_5=y_5/2+(x_0 mod2); other coordinates are y_i/2. Thus a one-class low-bit observer is NOT destruction of64 material identities. Subsequent identical sweeps have epsilon0 and simply double; for K>=1, X_(6K)=2^K(x-epsilon e_5). This particular schedule transfers one bit once and then locks; it is not a claim of perpetual novel interaction.

600 signed inputs verified the formula. Starting with64 equally weighted parity points, actual64-control kernels preserve64 distinct output points but leave one parity class. The output mean is(1,1,1,1,1,0); Cov(X_1,X_6)=-1 and Var(X_6)=2. An erased low-bit distinction became a retained cross-axis positional relationship. Expansion's full-field work/physical cost is not set to zero; only the six injected primitive steps are counted explicitly.

## 7. Verification, persistence and limits

14 new check groups PASS, seed20260920: five complete source blob matches;93750 signed local involution/unit-cost cases;800 exact prior radix-lift checks;64 initial parity classes and joint-product checks;384 adjacent and1152 nonadjacent order checks; original T6 refinement;12 guarded composition triples and12 old moment-action cross-checks;10 independent path enumerations at depth7 with7620 generated labels; moment-failure repair;23040 order/control cases plus two-sweep weighted convolution;60-sweep compressed transport;96-tick recurrent moments;120 original frame checks;14 invalid-input rejections;600 active-heartbeat identities. Mathematical claims above have explicit proofs; finite counts are reproducibility checks, not an independent referee. A streaming container launch was unavailable; ordinary foreground execution completed. No failed test is hidden behind a claimed pass.

No complete EM/Nollm test suite, independent mathematical review, Lean, physical clock calibration, semantic memory benchmark, global full-field coverage theorem or production modification. The world's naming/coordinate constraints were consumed, not modified. The method addendum marks an executable research candidate and does not promote it to Foundation.

Primary comparison: Arrighi-Nesme arXiv:1201.5529 (reversible block representations); Costa-de Melo arXiv:1905.10391 (coarse graining partitioned CA); Ben-Ari et al. arXiv:1911.05716 (finite-memory additive functionals). This turn inspected their primary abstract/metadata pages only. They contextualize known mechanisms, not prove this model's formulas or establish novelty. The gate is one prescribed geometric environment, not yet interacting memory items.

## 8. Smallest next question

Allow a bounded palette of genuinely changing contact widths while preserving actual primitive work and the joint residue carrier. Locate the first required control refinement beyond32/64 and compare exact support/occupancy with the moment-only observer. Do not restart the prior coordinate-only, velocity-census or5/7 probes. No background execution is implied.
