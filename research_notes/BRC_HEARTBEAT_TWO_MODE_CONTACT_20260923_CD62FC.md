# Heartbeat47 — Two-mode BRC contact, hidden entanglement and collision-word holonomy

Event-ID: brc-heartbeat-two-mode-contact-20260923-CD62FC
Status: SCOPED_CONSTITUTIVE_CANDIDATE / SAME_AUTHOR_PROOF_AND_EXECUTION / NOT_ADMITTED
Researcher: EM-DIRECT-CD62FC; activity RA-3DCC056A140F662E2BF11D00.
Prior contributions EM-DIRECT-6EF011 and EM-DIRECT-92DA92 retained. Session request brc47-session-20260923-f3841, Issue1117, published registration f0b30607e9abd6d578c0fee9d3bfc8aeb53a06d7; no formal Task, CLAIM or run.
Global read c4f8c3dd8081ee79825538919561e5ae129817a1; project read74b3e7bf54e648f4b8c113f9623b2963755dc05a; parent standalone03018865d6517f0dc883ae604b4e1c114746d5cd.

## Scope and actual execution

Continue two interacting localized collective modes, not a rigid rod or prescribed angle. A/B are distinguishable directed-native-port amplitudes. Coincidence is allowed. No energy, calibrated force, Gauss-source/field identification, physical time calibration, zero-temperature result or Shor acceleration is supplied. P000 and heartbeat definitions are unchanged. No trigonometric, matrix-exponential, Taylor, Pade, Cayley or classical high-precision computation is used.

Reuse unchanged Stage45 Branch/phase_cover/core_power and Stage46 coin/phase_power/face_vector/pair_observer/character. The underlying canonical module is bc7babbb9e890f6d5a7094430a5fbdccf66c77ad:src/enterprise_math/brc_weighted_recurrent.py, Git blob4e6b3132580e3cd70a20a0d8bd4d28792b961afb. The frozen run records35 actual canonical power calls. Tensor composition and quadratic/quartic readouts are new scoped maps with correspondence proofs, not a claim that fractions or a class name automatically constitute BRC.

## Coupling and tensor correspondence

Inherit T[(u,v)->(v,w)]=2/degree(v)-[w=u]. Let Pi select pairs whose port heads are the same Cell, V=I-2Pi, and U=(T tensor T)V. T and V are unitary; so is U. Contact changes a sign, not position. Identical-port coincidence is a different control, not the Cell observation.

Retain M(i,j,p)>=0 with p in Z2. Contact toggles p at coincidence. The A step is M'(i',j,p')=sum M(i,j,p)K(i,i',q), p'=p XOR q, where K is the returned canonical positive BRC phase transfer. The B step is analogous. Expanding these sums gives exactly the phase lift of joint branches of weight w_A*w_B and phase p_A XOR p_B XOR contact. A/B factoring is computational and commutes, not two physical time slices. Induction covers every finite control sequence.

Read amplitude A_ij=M0-M1 and probability (M0^2+M1^2-2M0M1)/Z. Reduced state rho_A[i,k]=sum_j A_ij*A_kj/Z and purity=sum rho_A[i,k]^2 are ordered pair/four-path observers. No normalization repair is applied. Original branch graph, labels and control sequence remain available; phase totals alone do not answer future individual-word history queries. Nine bounded full-word computations agree with the complete phase masses of factored propagation.

## Protected interaction geometry

Take two chord-free even cycles meeting at exactly one junction o. Every other cycle vertex has degree2; arbitrary exterior edges may attach at o. The executed four/four graph consists of native squares in opposite E1/E2 sectors, plus an actual outgoing edge from o to (0,0,1,0,0,0). It has8 Cells,9 edges,18 ports and324 joint states. The exterior edge remains active. Nonjunction extra-neighbour couplings are absent by explicit model choice; this is not a uniform full-Z6 graph.

For a cycle of length a, restrict the Stage46 stationary circulation f to its two incoming ports at o, calling that e0. Its input sum is zero. At o the coin maps this to minus itself and emits no exterior amplitude, regardless of junction degree. At all other degree2 vertices the components advance along their two native paths. Hence e_r=T^r e0, r=0..a-1, have disjoint two-port supports, Gram2I, sum f, and T e_r=e_(r+1 mod a). Only e0 arrives at o.

Therefore K=span{e_r tensor e_s} is invariant for free transport and every applied/omitted contact. In normalized encoded notation the exact BRC law is

    |r,s> -> (-1)^[r=0 and s=0] |r+1 mod a,s+1 mod b>.

No angle or time function is evaluated. Full BRC versus reduced BRC intertwiners are checked on every encoded basis for lengths4/4,4/6,4/8, including the outlet. This is an exact restricted operator identity, not a finite-time leakage estimate or a whole-graph reduction.

## Position can remain unchanged while the whole state changes

Initially choose the product f_A tensor f_B, raw norm64. On two four-cycles all complete joint port probabilities remain unchanged for every update; coincidence stays1/16 and same-or-neighbour stays5/16. The two modes stay on their assigned loops. Yet the reduced purity of A at updates0..8 is

    1,23/32,1/2,11/32,1/4,11/32,1/2,23/32,1.

At update4 the encoded coefficient table is (J4-2I4)/4. The exact identity (J4-2I4)^2=4I4 gives rho_A=I4/4: the joint pure state is maximally entangled over four modes. On K, U^4=I-2sum_r|r,r><r,r|, U^8=I. Thus position-label return after4 is not state return. The initial prepared state returns after8; this is not an all-state whole-exterior recurrence claim.

A specified coherent analyzer C4=(J4-2I4)/2 on A gives equal-mode-label probability1 after contact, versus1/4 for the identical no-contact product. This is an actual BRC logical readout, not same-Cell counting and not an implemented free physical analyzer.

For the full-rank preparation (1-eta)|psi><psi|+eta I324/324, target fidelity after4 is1-eta+eta/324. At eta1/100 it is32077/32400. Any separable state has fidelity at most1/4 with this rank-four maximally entangled target, by the Schmidt Cauchy-Schwarz bound and convexity. Hence this particular mixed state is still entangled; local mixed-state purity by itself is not used as that proof.

## Nonideal controls and preparation

Containment in K holds for every deterministic sequence of applied/omitted contact signs, without independent-error assumptions. It does not cover arbitrary coin changes or newly attached nonjunction couplings.

For a separate model of independent missed contacts with probability delta during four updates, enumerate all16 histories and compute their weights through a31-state positive BRC control-word tree. The target fidelity is exactly1-15delta/16+3delta^2/16. For delta1/4 it is199/256, still above the separable bound1/4. For0<=delta<1 the witness remains positive; delta1 gives the original product at the common cycle return. These classical control outcomes are mixed as density matrices, not coherently summed.

For raw preparation psi+epsilon*h, norm(psi)^2=64 and unit h outside K and the assigned-loop port rectangle, all-time exterior probability is at mostepsilon^2/(64+epsilon^2). This follows from the reducing invariant subspace and unitarity for each permitted control step. At epsilon1/100000000 the bound is1/640000000000000001. This is a proof-derived preparation bound, not a simulated arbitrary-control-error trajectory.

## Arithmetic collision history

Let g=gcd(a,b), l=lcm(a,b). In l simultaneous shifts a label pair meets(0,0) once exactly when r=s mod g. Thus

    U^l|r,s>=(-1)^[r=s mod g]|r,s>, U^(2l)|K=I.

For uniform independent encoded inputs, grouping residue classes gives coefficient matrix(J_g-2I_g)/g. Its nonzero Schmidt weights are(g-2)^2/g^2 and4/g^2 repeatedg-1 times, omitting zeros. The exact reduced purity is((g-2)^4+16(g-1))/g^4.

Executed BRC cases:4/4,4/6,4/8,6/6,6/8,6/12,8/12,10/10. Four/six returns a product (purity1) after its common period12; four/eight has purity1/4 after common period8. Specified cycle lengths are inputs. This is a BRC ordered-word congruence law, not extraction of an unknown modular order or a Shor speedup. The class count is not native spatial dimension.

## Counterexample to automatic stability under contact

On the inherited two-plaquette strip with six Cells and14 ports, the cycles share an edge rather than only one vertex. The same initial product and same contact law retain all joint probabilities after one update but purity_A becomes1/2. After two updates assigned-loop retention is65/81, coincidence is59/216 and same-or-neighbour35/54; the matched no-contact case remains at1,1/8,1/2 respectively. One-particle-per-loop in either assignment is68/81, a distinct event. Thus contact can increase proximity while disrupting previous localization. Neither observation alone establishes a mobile bound object.

## Verification and limits

Command python -S -m stage47.run:436 named finite checks,35 canonical BRC power calls,three full interacting cases with9 stored states each,nine full bounded word checks,three full encoded-basis intertwiners,eight congruence cases,16 missed-contact histories. Replays compare all scientific fields and preserve frozen timing records. No conventional numerical reference or independent researcher/Lean verification. All1046 inherited manifest files remain unchanged.

Relevant existing work is Ahlbrecht et al.arXiv1105.1051v1, official title Bound Molecules in an Interacting Quantum Walk (official abstract read); journal title Molecular binding in interacting quantum walks, NJP14,073050(2012). Dedicated query Issue1123/request4866a641-3374-4122-909f-c094f15f7db1 returned confirmed NO_HIT for the journal-title phrase, one provider call, zero bridge-model calls. That is not absence of the known paper under its other title. No full-text or exhaustive novelty claim is made.

The outcome is a candidate phase-history/entanglement mechanism with exact BRC evidence, not self-assembly, mechanical binding, persistent macroscopic size, infinite instantaneous signaling or energy/temperature physics. Next: couple a genuine active native neighbourhood/source field or implement a movable protected interface, retaining separation, contact history and complete joint observation. Formal task admission and activity aggregate integration remain distinct from source and bundle publication.
