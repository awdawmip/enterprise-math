# Routing memory, transported orientation and equal-mean Euler dynamics

Status: PROVISIONAL MODEL THEOREMS AND EXACT BRC CERTIFICATES / NOT FORMALLY ADMITTED.
Date: 2026-10-05. Same-conversation continuation, not independent replication.
Global read snapshot: awdawmip/chatgpt-global-knowledge@fdf96684806fbe8becfb4a01e8b9a60994d541ee.
Source read snapshot: awdawmip/enterprise-math@21cbdf36e88c4dd06a4d9e3c25332a1a23baecd5.
Previous scientific frontier: 09d35689b0460e3639837bb00b52d93f34a37098, research_notes/chatgpt_direct/20261005_SYNCHRONOUS_SYMMETRY_BRC_LIMIT.md, blob 67181fc496aeb6f35327cf0c751b2805ed379230.
Logical conversation: chatgpt-heartbeat-euler-20261004-layer-01; not platform-attested.

## Scope and executed reuse

This unit changes the temporal relation between already-defined routing choices, not the collision permutations or the native spatial dimension. P(a,b,f)=(f,a,b), its inverse, the shared-field synchronous maps F_+ and F_-, and positive CWM operations are reused unchanged. C12 incidence ports are not X6 coordinates. K4 slice-comparison paths, contact count, synchronous update count and physical time are distinct types. No native force, primitive three-action equilibrium, field origin, clock, distance, spin or energy law is inferred.

The previous conversation archive euler_simultaneous_evidence.zip has SHA256 31bc2fb0026855350ed0f4b95757dd25a0f0821e5c3b4db2dd200cb5e08942ed. All 45 entries of its manifest were checked. Unchanged brc_simultaneous.py has SHA256 819a4e1d2d4358408f0b158b8497a1c098dfa53a65aaaba57940963fe651def5. Its dependency chain actually executes the existing positive CWM bodies from brc_weighted.py, blob 3f205696709e847909958a153f8fe10d3f6b70f0, and the previously pinned finite incidence successor. No old research suite was rerun as new science.

The relevant additional source is src/enterprise_math/euler_fcc_chirality.py, full source blob 6f8b147c094720c2749f620a40394c4d7b67a386. Its unchanged dependency-closed functions transition_bit, face_holonomy, gauge_action and normalization helpers were executed from inspected excerpts at lines 25..107, 132..160 and 245..273. The local excerpt adds an importable header/imports and omits unused definitions; it is not claimed byte-identical to the entire source module. That source explicitly does not derive overlap bits from bare FCC incidence. No whole-repository absence claim follows from a keyword search.

Reuse classifications: REUSE_EXECUTED for the CWM/collision/incidence kernels and inspected chirality functions; COMPOSE_APPLIED for contact followed by source orientation transport; EXTEND_EXISTING_TOOL for retained routing memory. This is a scenario extension and certificate, not an accepted new tool family. P000, the ACTIVE residual-fidelity worldview and scoped BRC-only arithmetic were applied. No numerical pi, classical trigonometry, numerical square root, ordinary propagator, matrix exponential or Taylor/Pade/Cayley computation is used.

## 1. Symmetry does not imply independent re-selection

Let chi be the routing sign, +1 or -1. The local update applies P^chi. Interchanging the two recipient roles conjugates P to P^-1 and must transform chi to -chi.

A time-homogeneous two-sign transition respecting this exchange symmetry has the general form

Pr(chi_next=chi)=p, Pr(chi_next=-chi)=1-p,

where 0<=p<=1. We use rational p for the exact positive BRC implementation. Symmetry leaves p undetermined. From an initially fair sign, every single-time sign marginal remains fair, including p=0 and p=1. Fair marginals do not imply independent choices.

For p=1 the initial sign is retained forever. For p=0 it alternates deterministically. For p=1/2 each next sign is fair and independent of the current sign. These are different programs even though their first contact has identical channel endpoint weights.

At every actual branch we retain (three binary channels, next sign, positive CWM, source root, complete choice/history record). Zero-weight alternatives are skipped. Contact applies the unchanged cyclic function, then the supported p/(1-p) edges execute cwm_edge and cwm_propagate. Alternatives use cwm_recoalesce. No fractional bit or negative positive-weight branch is created.

## 2. Exact local memory law

Use the previous alpha with alpha^4-alpha^2+1=0, and omega=alpha^4. The channel observer is zeta=a+omega*b+omega^2*f, evaluated after positive path transport.

Let u_r and v_r be its weighted sums conditional on the next routing sign + and -, without normalizing those subpopulations. Routing followed by the sign transition gives

u_next=p*omega*u+(1-p)*omega^2*v,
v_next=(1-p)*omega*u+p*omega^2*v.

Consequently zeta_r=u_r+v_r satisfies

zeta_(r+2)=-p*zeta_(r+1)+(1-2p)*zeta_r.

Proof: the displayed two-component transformation has trace -p and determinant 2p-1. Expanding its degree-two polynomial gives zero; applying the identity to u+v gives the recurrence. The array is a proved observer interface, not an alternative numerical state propagator.

For a fixed initial channel state with an independent fair initial sign, zeta_1=-zeta_0/2. Writing zeta_r=c_r*zeta_0:

p=1: c_r=1 for r divisible by3, otherwise -1/2.
p=0: c_r=1 for even r, otherwise -1/2.
p=1/2: c_r=(-1/2)^r.

Thus the one-contact average is the same, but retaining, reversing, or refreshing the routing choice gives three-period echo, two-period echo, or decay.

For every 0<p<1, the unit-count joint channel/sign chain has six states and both supported routing transitions. It is irreducible: arbitrary future choices reach every channel/sign state. Positive closed walks of lengths2 and3 through the same state make it aperiodic. Its column sums equal its row sums, both one, so uniform1/6 is stationary. The standard finite-chain theorem then yields joint convergence and vanishing channel difference modes. At p=0 or1 the chain instead splits into deterministic cycles. This statement is model-local and does not derive the parameter or independent branching from native dynamics.

The general role of correlated increments and retained memory is established prior art; see Cenac, Chauvin, Herrmann and Vallois, Persistent random walks, variable length Markov chains and piecewise deterministic Markov processes, arXiv:1208.3358. The new result here is the concrete BRC correspondence, witnesses and source-family composition, not a new general stochastic-process theory.

## 3. Exact uniformity can be a crossing, not equilibrium

Choose p=2/3, begin at (a,b,f)=(0,0,1), and give the initial sign fair weights. After two contacts the joint channel/sign masses are

                 sign+     sign-
A occupied        1/9       2/9
B occupied        2/9       1/9
field occupied    1/6       1/6.

The three channel marginals are exactly (1/3,1/3,1/3), both sign marginals are1/2, and zeta_2=0. Nevertheless the next channel marginals are (5/18,5/18,4/9), with zeta_3=omega^2/6 !=0.

The different joint preparation assigning1/6 to each of the six states has the same channel and sign marginals but remains stationary. Therefore even exact channel uniformity plus an exactly fair routing marginal is not sufficient for equilibrium. Replacing their joint distribution by a product would erase the operative channel/sign correlation. This is a positive classical correlation example, not quantum entanglement.

## 4. What actual incoming information would have to supply

For an input-relation set X with recipient-exchange involution R, an orientation selector chi:X->{+1,-1} satisfying chi(Rx)=-chi(x) exists if and only if R has no fixed point on X. Necessity follows at a fixed point; sufficiency assigns opposite signs to the two members of each orbit. The selection is not automatically canonical.

More generally, for a finite group of allowed relabellings G and a sign character epsilon, a selector with chi(gx)=epsilon(g)chi(x) exists on an orbit exactly when every stabilizer element of x has epsilon=+1. Choosing a representative proves sufficiency and an odd stabilizer proves obstruction.

An explicitly supplied orientation of three distinct incoming ports supplies the required antisymmetric sign. The candidate collision P^chi is then recipient-equivariant by RPR=P^-1. Using arbitrary numeric port names as an ordered frame would add data, not derive physical orientation. Coincident/indistinguishable input ports do not satisfy this construction. No native incoming-channel contract identifying the collision sign with the source slice-sheet variable is proved here.

## 5. Existing source orientation transport yields memory, not fresh randomness

The exact chirality source transports a sheet bit s along a comparison edge i->j by

s_j=s_i XOR e_ij.

Set chi=(-1)^s. Along a closed comparison path gamma, the final sign is

chi_after=(-1)^h_gamma*chi_before,

where h_gamma is the XOR of the traversed edge bits. Vertex gauge changes add endpoint bits that cancel around the closed path; h_gamma is gauge invariant.

Compose one collision P^chi with this declared closed-path transport. If h_gamma=0, repeated contacts keep the same sign and three contacts restore the channel state. If h_gamma=1, successive signs alternate, and two contacts restore the channel state because P^-chi P^chi=I. In both cases the sheet also returns at the stated contact count.

This composition was executed for all64 edge assignments, all4 source triangular faces, both initial signs and all8 channel triples. An initially fair sheet still has a fair sign at every return, yet its temporal choices are fully correlated. It is not equivalent to independently redrawing the sign, which multiplies the local channel observer by-1/2 on each contact.

This is an exact bridge between existing finite interfaces under a stated identification and a prescribed comparison path. It does not identify those paths with actual incoming native trajectories, prove the physical sign choice, or derive gate incidence from K4 chirality. The source itself preserves that distinction.

## 6. Exact closure term when route memory is omitted

Write A_+ and A_- for pushforward by the unchanged synchronous shared-field maps F_+ and F_-. A persistent-routing joint distribution consists of positive measures mu_+,mu_-. Define the signed readout coordinates

mu=mu_++mu_-, nu=mu_+-mu_-,
K=(A_++A_-)/2, L=(A_+-A_-)/2.

Direct composition gives

mu_next=K*mu+L*nu,
nu_next=L*mu+K*nu.

The old fresh-choice endpoint dynamics is K*mu. It is exact when a fresh fair sign independent of the CURRENT full world is supplied at each choice, or when L*nu happens to vanish. A fair sign marginal only implies total(nu)=0; it does not remove L*nu. An initially independent fair sign gives nu_0=0, but generally nu_1=L*mu_0 is already nonzero.

These signed quantities are observer/certificate differences, not negative BRC populations. Atomic-column identities were checked against actual existing BRC updates. The unclosed term now has a specified cause: world/routing correlation.

## 7. Same global one-step kernel, same time average, different long-term dynamics

For the SAME previous Q=1 shared-field rules, compare:

Fresh program: use the existing independent equal alternative at each shared-gate contact.
Persistent program: choose chi fairly ONCE in the initial preparation, retain it, and always apply F_chi.

For every one of1152 bare Q=1 states the programs have equal one-step endpoint mass distributions. They do not have equal full latent states, route histories or generally equal path counts.

Each fixed F_chi is a permutation with726 fixed states,12 cycles of length18 and6 cycles of length35. On an anchored35-state component, a field-only unit is released into one object, completes an excursion in17 updates, is handed directly to the other object for another17 updates, and is deposited back into the field on update35. Reversing chi swaps which identity travels first. The two fixed routes traverse the same35-state component in different orders.

Begin at one odd anchor g with both objects idle at g and f_g=1. For both preparations the symmetric phase samples agree at updates0..17. At update18:

Z_persistent=(alpha^g+alpha^(g+1))/2,
Z_fresh=(3alpha^g+alpha^(g+1))/4.

Thus Z_fresh-Z_persistent=(alpha^g-alpha^(g+1))/4 !=0. The fresh process has a deposit branch on this encounter; persistent routing has retained the correlation that enforces direct handoff.

The persistent symmetric phase has exact period35, with no convergence from this preparation. Its value alpha^g occurs three times in a35-block, ruling out periods1,5,7. Only two initial BRC alternatives are needed, with total1 and maximum weight1/2; histories still grow and are not erased.

Yet its finite35-sample TIME AVERAGE is exactly17alpha^g/35, because each fixed route visits every state in the anchored component once. This is the SAME value as the previous fresh program's limiting ensemble phase, whose convergence remains valid under that program's independent-choice assumption.

The distinction is decisive: equality of a first-step kernel and of a long-term/time average does not establish equality of the processes. A35-point temporal averaging operation is not the instantaneous dyadic-weight evolution used in the earlier nonattainment theorem, so there is no contradiction with that theorem.

## 8. Finite evidence and limits

Final suite: 66,506 exact assertions, including45 prior-manifest integrity checks. New coverage includes all8 channel triples at7 persistence parameters through7 recorded contacts; retained inverse histories; exact local recurrence and typed joint quotient; the p=2/3 uniform-but-not-stationary witness; all64 edge assignments,4 faces,2 signs and8 channel triples; all16 gauge transformations; all1152 Q=1 states for both FIXED routes; equality of one-step endpoint kernels; and all6 anchored persistent/fresh comparisons through70 updates.

Actual existing CWM calls: cwm_edge117354, cwm_propagate111216, cwm_recoalesce51188. Existing incidence successor calls:3600. Inspected chirality-source calls: transition_bit30720, face_holonomy1088, gauge_action1024. These are assertion/call counts, not independent experiments or a whole-repository test.

The first run passed the same scientific assertions but wrote null for an unavailable counter alias. The reporting field was changed to read the actual call function's module globals; the final run revalidated the unchanged scientific code. Both logs remain in the attachment. This is a reporting correction, not a second independent replication or a physical residual.

Run python check_route_memory.py with Python3.10+ and the standard library from the conversation evidence directory. Full new code, the inspected excerpt, unchanged dependencies, traces, manifest and hashes are supplied there. This Source note preserves the proofs and validation frontier; it does not assert that every attachment byte is stored in the project source or formally admitted.

Primary finite-chain background: QuantEcon, Markov Chains: Irreducibility and Ergodicity, https://intro.quantecon.org/markov_chains_II.html. No external numerical propagator was run.

## Actual control and continuation

Current own status request is private bridge#2748, status-20261005-euler-routing-memory-17. It still exposes service-local session MCP-74124c48a87440a6b56f5f440f7e9493 tied to the earlier failed registration request. This pointer does not establish Source-bound authority. No duplicate registration, replay of the earlier rejected prerequisite, CLAIM, formal run, activity checkpoint admission or final-guard success is asserted. REGISTER_PENDING remains explicit. The new scientific packet is not a retry of any earlier safety-blocked note or verification sidecar.

Completed new unit: temporal routing-memory law; uniform-marginal non-equilibrium witness; conditional source-holonomy composition; fixed-route35-cycle classification; exact global first discrepancy and equal-average/different-dynamics witness. Do not rederive those or the earlier local symmetry obstruction as new progress.

The smallest native gap is now two coupled obligations: supply an actual incoming-channel/field relation that selects or transports chi equivariantly, AND establish its temporal memory law. A one-contact fair split alone supplies neither independence nor the previously derived convergence. The local source orientation transport offers an exact candidate type, not a native collision theorem. The original physical Euler/heartbeat bridge remains open.
