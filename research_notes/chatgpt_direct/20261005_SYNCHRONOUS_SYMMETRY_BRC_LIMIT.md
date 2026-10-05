# Symmetric synchronous collision: obstruction, BRC lift and nonattained Euler limit

Status: PROVISIONAL MODEL THEOREMS AND EXACT FINITE CERTIFICATES / NOT FORMALLY ADMITTED.
Date: 2026-10-05. Same-conversation authored continuation; not independent replication.
Global read snapshot: 8b9131c904cb01db6150badcdb35ef7dfe99845d.
Source read snapshot: dd9b44fafe3e6a02c5c6c8ba825e1f130a05bfe5.
Prior frontier: a155bb2c856256d1df260eaa72eedb229fca1e23, research_notes/chatgpt_direct/20261005_DYNAMIC_FIELD_SHARED_MEMORY_35_70.md, blob ef825d14d411a4dec390a3d5e1d16daf6d3af7a8.

## Scope and actual reuse

The previous model imposed alternating A/B updates. This NEW unit removes that scheduler and studies collision at a shared gate followed by synchronous streaming. It does not replace or republish earlier safety-blocked notes, journals or verification sidecars.

Ports in Z/12 are source Cell/gate incidence labels, not X6 positions. Odd ports are gate sites. Object modes and six field bits are internal data, not new spatial dimensions. P000, six native space axes, separate time and three-dimensional slice typing are unchanged. Co-occupancy, collision/stream ordering and the new branching law are candidate assumptions, not native simultaneous forces or primitive triadic balance.

Recovered prior archive SHA256: 7103fb0c174347d46e28179befee65e5ac80e58e4d5ceb12e89f58f147e9101e. All33 entries of its manifest match. Its unchanged brc_dynamic_field.py, SHA256 a848479916af2ef92dc239bde0eafe0dc7b0ba2fd22a2761c9f9e4c0cb358dc8, supplies the existing positive CWM core and incidence adapter. Source brc_weighted.py blob3f205696709e847909958a153f8fe10d3f6b70f0 matches current Source. The incidence excerpt remains pinned to euler_rotation_refinement.py blob55e12f7ffb68a5b241f5d6323f5fde118de2716a. Existing cwm_edge, cwm_propagate, cwm_recoalesce and successor bodies are actually executed. The old alternating pair-step is NOT used as the new update. New World has no turn variable.

REUSE_EXECUTED / EXTEND_EXISTING_TOOL; no new accepted tool family or literature-wide novelty. No numerical pi, trigonometry, roots, matrix exponential, Taylor/Pade/Cayley or non-BRC reference evolution. Graph and rational certificates audit BRC-generated rows, not alternative state propagation. Every explicit path retains a root, choice sequence, positive CWM and operation history.

## 1. Complete local deterministic obstruction

At one shared gate, suppose the only local data are (a,b,f) in {0,1}^3. The field bit is invariant under object renaming R(a,b,f)=(b,a,f). A deterministic collision C is required to be bijective, preserve a+b+f, and commute with R.

There are exactly FOUR such collisions, and all keep f unchanged.

Proof: sectors of total0 and3 are fixed singletons. In sector1, R swaps100/010 and fixes001. A commuting permutation must fix the unique R-fixed state001, and can only keep or swap100/010. In sector2, R swaps011/101 and fixes110; again there are two choices. The choices are independent, giving four maps, each with f'=f. These exhaust all3!*3!=36 count-conserving permutations.

Even dropping bijectivity does not let the exactly symmetric state001 deterministically select a receiver: an R-fixed output with total1 must still be001. Thus nontrivial neutral symmetric release is impossible on this bare carrier. Distinct incident directions, extra channels, a different conservation law or other local information are outside the theorem. This is not a no-go for native physics.

## 2. Relational routing bit and positive symmetric alternatives

Define P(a,b,f)=(f,a,b); P^-1(a,b,f)=(b,f,a). Then P^3=I, both preserve total, and RPR=P^-1. Neither oriented choice alone is invariant under R.

One relational binary bit chi suffices for a reversible extension:

G(x,chi)=(P^chi x,chi), R_tilde(x,chi)=(Rx,-chi).

G commutes with R_tilde; its inverse uses P^-chi. No routing distinction is insufficient by section1. The extra bit transforms under object relabelling; it is not a scalar field, an extra spatial dimension or physical spin. A single fixed value is not a free symmetric initialization.

A different, explicitly declared BRC program retains both alternatives:

K[x]=(1/2)[Px] plus (1/2)[P^-1 x].

Its endpoint kernel commutes with R. For001 its outputs are100 and010, each positive weight1/2. These are two alternative complete states, not two simultaneously excited receivers or fractional bits. Repeated K assumes a fresh independent equal-weight split at each contact; this is not a derived fundamental random law. A fixed chi across contacts is a different program.

## 3. Exact local channel-phase relaxation, with recovery boundary

For unit-count channel histogram v=(v_A,v_B,v_f),

K v=((v_B+v_f)/2,(v_A+v_f)/2,(v_A+v_B)/2).

Let E=(I+P+P^2)/3. Then K=E-(I-E)/2, E^2=E, hence

K^r v=E v+(-1/2)^r(I-E)v.

For v=(0,0,1), v_A=v_B=(1-(-1/2)^r)/3 and v_f=(1+2(-1/2)^r)/3. The same identity holds for bit expectations in the other conserved sectors.

For the existing alpha^4-alpha^2+1=0 and omega=alpha^4, the LOCAL CHANNEL observer zeta=v_A+omega*v_B+omega^2*v_f satisfies zeta_next=-zeta/2. Deterministic oriented routing multiplies it by omega or omega^2. This local repeated-contact experiment does not stream objects and is not the port-phase observer Z.

After r local BRC splits, CWM=(2^r,1,2^-r). Inverting each retained branch word restores the original triple. The marginal linear inverse K^-1=3E-2I has diagonal-1 and off-diagonal1. Thus the exact histogram is algebraically invertible, but no universally positive stochastic inverse exists; difference-mode errors amplify by2^r under inversion. Do not call this universal information destruction or physical dissipation.

## 4. Scheduler-free synchronous shared-field update

A complete branch carries (n_A,n_B,b_A,b_B,f), with ONE shared field. At each gate use pre-stream occupancy: none -> identity; one object -> previous mode/field SWAP; two objects -> P or P^-1 on(b_A,b_B,f_g). Different gate sites have disjoint local data and commute. Then both objects stream by their new modes, using the existing successor.

For fixed chi, collision is a permutation at fixed positions, and streaming has inverse n_i=m_i-b_i. Therefore F_chi is a bijection on all12^2*2^8=36864 bare states. It conserves Q=b_A+b_B+sum f_g and positive BRC weight. Its inverse undoes both streams, then local collisions. Label exchange conjugates F_+ to F_-. Their equal-weight endpoint kernel is normalized, symmetric under object relabelling, and doubly stochastic on every conserved sector.

Outside same-gate contention the two routes coincide and the implementation uses one path. At contention both choices remain distinct paths even if their endpoints coincide. Endpoint mass, path count and full histories are not interchangeable.

This removes an alternating object scheduler, not the assumption of synchronous collision/stream stages. No physical simultaneous collision or clock has been derived.

Example: at g=1 with both modes0 and f_1=1, the outputs have ports(2,1),modes(1,0) or ports(1,2),modes(0,1), zero field, each weight1/2. Both have symmetric phase(alpha^2+alpha)/2; label-specific phase distinguishes them. Total positive weight remains1.

## 5. Complete Q=1 component theorem

There are12^2*8=1152 bare Q=1 states. They partition into:

726 fixed states: field unit at g with neither object at g; count6*11^2.
12 deterministic18-cycles: idle object at one of six even Cell ports; choose moving identity in two ways.
6 closed strongly connected35-state components: one for each odd anchor g.

Each anchor component has17 states with A moving/depositing while B stays at g,17 with roles reversed, and one state with both idle at g and f_g=1. For each moving identity the17 states are12 moving positions plus5 deposits at gates other than g. No transient states remain;726+12*18+6*35=1152.

The two alternatives at a common arrival permit direct handoff or deposit and later reception. Every state in one anchor component reaches every other. Positive-weight closed walks of lengths18 and35 through the same arrival state have gcd1, proving aperiodicity. Here35 is a STATE COUNT, not a fixed Markov return period. The exact graph also has all-to-all reachability in306 steps and fails that property at305.

Since the kernel is an average of two permutations and the component is closed, uniform1/35 is stationary. Irreducibility and aperiodicity imply convergence from every normalized initial histogram in that component. The other fixed/18-cycle components do not acquire this convergence claim. This is the standard finite Markov theorem applied to a normalized BRC endpoint kernel, not physical randomness inferred from data.

A self-contained conservative bound: every306-step transition has weight at least2^-306. Set eta=35/2^306. Separating an eta fraction of the uniform kernel in each block gives TV(mu_t,uniform) <= (1-eta)^floor(t/306). This is a VERY weak sufficient bound, not an optimized mixing-time estimate. No numerical eigenvalues are used.

## 6. The Euler circle and its interior limiting mean

Every branch in an anchor-g component has one object at g and another at m. Thus

z=(alpha^g+alpha^m)/2, z-alpha^g/2=alpha^m/2.

The branch readouts remain on the same twelve-position external circle of radius1/2 centered at alpha^g/2. A positive average of different readouts need not remain on the circle; no native plane is introduced.

Over the17 states for one moving identity, the moving-port phase sum is

sum_(all12ports)alpha^n + sum_(five gates other than g)alpha^h = -alpha^g.

Both the full port sum and all-six-gate sum vanish. The35-state symmetric phase sum is18alpha^g-alpha^g=17alpha^g. Consequently

Z_limit=(17/35)alpha^g.

The stationary internal counts are E[b_A]=E[b_B]=12/35 and E[sum f_g]=11/35, preserving Q=1. Positive BRC mass stays1. Branchwise squared distance from the circle center stays1/4 even when the mean moves inside. These are not physical energy partitions or dissipation laws.

## 7. Convergence without finite exact equality

Start from ONE deterministic joint state of unit weight in an anchor component. Every finite endpoint weight is dyadic because transitions only multiply by1 or1/2 and add. A symmetric phase coefficient at time t has denominator dividing2^(t+1). But alpha^g has a coefficient +/-1 and the corresponding limiting coefficient is +/-17/35, not dyadic.

Therefore Z_t != (17/35)alpha^g for EVERY finite t, despite convergence. For one nonzero limiting coefficient,

|Z_t,j-Z_limit,j| >= 1/(35*2^(t+1)).

This weak lower bound is consistent with convergence. It is specific to the single-state/dyadic preparation; initializing the non-dyadic stationary distribution is excluded and would give equality immediately. It does not imply all natural residuals are nonzero.

Finite-resolution replacement can therefore be justified while finite exact equality cannot. Under this fixed future kernel, each coefficient deviation is bounded by twice TV distance. Path-sensitive inversion using recorded routing choices is a different operation class, and is not covered by the history-blind approximation.

## 8. Actual verification and artifacts

Final suite passed523869 assertions, including33 dependency-integrity checks; all36 conservative local permutations and their4 symmetric survivors; all16 local triple/choice-bit cases; all8 local triples through8 contacts; all36864 global states under both fixed choices with inverse, charge, locality, CWM and covariance; all1152 Q=1 branch rows; all744 closed components, exact coprime return paths and six306-step support certificates; explicit-path/joint-CWM agreement through80 updates; inverse recovery of all162 final labelled branches.

Actual source calls: cwm_edge524444, cwm_propagate485070, cwm_recoalesce12871; incidence successor232956. These are assertions/calls, not independent experiments. The first checker finished its science assertions but failed on a wrong attribute name while collecting call counters. Only the reporting field was fixed; model/dependencies unchanged. Failure preserved; final checker rerun is not independent replication. Prior scientific suites were consumed, not replayed as new work.

Full local NOTE.md:17139 bytes, SHA256 cebb68f90be350be832cbe410168d93af28c40fb5fca2aff5571011bf5905bb2.
New brc_simultaneous.py:5582 bytes, SHA256819a4e1d2d4358408f0b158b8497a1c098dfa53a65aaaba57940963fe651def5.
New check_simultaneous.py:11953 bytes, SHA25604126a18466cbee08b518787ac3c1e3eed525415d53a25771e0c1c2ef94db4b8.
Final evidence/summary.json SHA256ab3f72a4a8c3562c23cb05f5a0abecac48cb812f0fff02608e0d4fa85c8138d2.
Run python check_simultaneous.py in the conversation evidence package, Python3.10+, standard library. This Source note preserves the new proofs and validation frontier, not the complete attachment bytes or formal admission.

Primary background: Margolus, Finite-State Classical Mechanics, arXiv:1807.04437 (abstract for general context); QuantEcon, Finite Markov Chains, https://julia.quantecon.org/introduction_dynamics/finite_markov.html (finite-chain convergence). No literature-wide novelty claim.

## 9. Actual control and next unit

Current status#2743, status-20261005-euler-synchronous-15, still exposes service-local pointer MCP-74124c48a87440a6b56f5f440f7e9493 tied to earlier FAILED registration. Its Source session record at current dd9b44f returned404. The earlier failed reconcile is not repeated. Source-bound identity/activity remains UNVERIFIED/REGISTER_PENDING; no old identity, CLAIM, formal run, independent review, theorem acceptance or successful final gate is asserted.

Completed: deterministic symmetry obstruction, minimal relational routing extension, symmetric positive collision, exact-1/2 channel relaxation, synchronous shared-field transport, complete Q=1 component theorem, limiting phase and all-finite nonattainment. Earlier35/70 alternating results remain valid within their old contract.

Next: determine whether actual native incoming-channel or triadic-incidence information can supply the relational routing distinction, or prove that a specified branching/extra-field state is required. Equal split weights, independent resampling, multiple occupancy and synchronous collision/stream stages remain assumptions; naming a bit chirality does not derive its native origin. No native force, calibrated time/distance/energy, quantum mechanism or speedup is established.
