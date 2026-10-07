# Incidence regularity is the exact equal-channel emission condition

Task: RS-U2-NATIVE-OCCUPANCY-BRIDGE-20261007 / TP2-E49C20B8D0A6569355F6.
Researcher: EM-DIRECT-FA0C27. Status: proved conditional finite BRC derivation; not native incidence admission, not independent review, not a material successor law.

## Frozen carrier and question

Use the U2 response-packet carrier at `fe9ce58293ac77b72092512620e8670ca9be2d78:research_notes/chatgpt_direct/20261007_cell_closure_u2_7f21d8/packet_router.py`, with the unchanged weighted-BRC blob `3f205696709e847909958a153f8fe10d3f6b70f0`. Signed ports are the twelve native X6 directions, with source, anchor and joint packet identity retained before the declared unary mass readout. A packet has three distinct axes, equal leg shares, and a positive response budget. This does not identify response with primitive force quanta.

The old permissive default has 160 signed triples and 40 incident triples at each port. The new question is what survives when a future supplied native-incidence relation replaces that default. The theorem below is conditional on a **single coherent finite hypergraph** H of distinct three-port tuples, with every port in at least one tuple, and the specific U2 uniform choice among tuples incident to the incoming port. Arbitrary incoming-dependent families are more general and need not satisfy this theorem's reciprocity assumption. No native legality of H is inferred from its syntax.

Write d(p)=|{h in H:p in h}| and n(p,q)=|{h in H:p,q in h}|, including n(p,p)=d(p). The permitted BRC operations choose an incident h with serial weight 1/d(p), then a leg q in h with serial weight 1/3. Recoalescence is only for the source-blind unary port mass observer, while the original joint packet labels remain available for richer future operations. Therefore

    K_H(q,p) = n(p,q)/(3 d(p)).                         (1)

Each column sums to one, K_H(p,p)=1/3, and K_H(-p,p)=0. These are exact sums of positive BRC branches; no signed-amplitude cancellation or classical propagator is used. The actual finite check in `incidence_check.py` invokes the unchanged pinned kernel and preserves the explicit source/port tags. The all-H result below is proved symbolically, not established by enumerating examples.

## Theorem and proof

Let two ports be connected when a chain of triples of H joins them. For the circuit above, the following are equivalent:

1. Equal input budget 1/12 at each incoming port emits exactly 1/12 at every outgoing port.
2. Every row sum r(q)=sum_p K_H(q,p) is one.
3. d(p) is constant within each incidence-connected component.

Also, the positive degree weights are stationary and obey a reciprocal identity:

    sum_p K_H(q,p)d(p) = d(q),
    K_H(q,p)d(p) = K_H(p,q)d(q) = n(p,q)/3.             (2)

Stationarity here concerns only the local incoming-to-outgoing port kernel, before spatial travel and the reversal of the next incoming-port label. It asserts neither stationary material occupancy nor a stationary full field.

Proof of (2): each of the d(q) triples incident to q supplies three terms of weight 1/3. Symmetry of n gives reciprocity. The equivalence of (1) and (2) in the list is simply the readout of the equal input branches. If d is constant on a component, each incident triple contributes 3/d to sum_p n(p,q)/d(p), so r(q)=1.

Conversely suppose every r(q)=1, and let x(p)=1/d(p). Rearranging that equation yields

    x(q) = (1/(3 d(q))) sum_(h contains q) sum_(p in h) x(p).    (3)

On any finite component choose q where x is maximal. The right side is an average of 3 d(q) values, each no larger than x(q), and all have positive weight. Equality forces every port sharing a triple with q to have the same maximum. Repeating along connecting triples makes x constant on that component. Thus d is constant there. This is a finite positive-branch maximum argument; no spectral, continuum, force-balance or time-evolution premise is added.

Different disconnected components may have different degrees. Global equal degree is sufficient but is not necessary. If incidence is state-dependent, weighted nonuniformly, contains repeated hyperedges, or depends on source/anchor history, use its actual typed branch weights and rederive the condition; the unweighted theorem must not be transferred silently.

## Consequence for the two-unit bridge

At a material a, let r_a(q) be its row sum and use the original equal twelve-channel source injection, rho=12 lambda with 0<lambda<1/12. Every material uses the same attenuation rho, conservative anchored equal-three-leg scattering, and no intervening gate or storage delay. Its first emission in direction q is lambda r_a(q), not generally lambda. At an empty neighboring Cell the returning edge weighs lambda. At an occupied neighbor with any such anchored kernel the returning edge weighs rho/3=4 lambda. Consequently its exact own-source, two-edge response is

    R_a^(2) = lambda^2 [12 + 3 sum_(q: a+direction(q) occupied) r_a(q)].   (4)

The neighbor's kernel may differ; its anchored diagonal 1/3 is sufficient for this particular coefficient. Formula (4) sums the actual outward/return path weights, without deleting self response or cross-source state. It is a fixed-layout diagnostic coefficient; it does not solve material occupancy.

For a single specified occupied-neighbor set B, the old formula (12+3|B|)lambda^2 holds exactly iff sum_(q in B) r_a(q)=|B|. Uniform rows are necessary and sufficient for that old formula to hold for **every** neighbor set, since singleton sets test every row separately. In the task's adjacent pair c,c+E1, only r_A(+1)=1 and r_B(-1)=1 are needed for the two old coefficients individually. If one fixed coherent H is used at both materials for every signed pair orientation, and each source-labelled coefficient must individually equal the old value, the theorem gives the exact regularity condition. Observing only the sum of the two own-return coefficients is weaker: for an orientation q it requires only r(q)+r(-q)=2. Such a source-blind aggregate cannot by itself certify the two separate source responses.

Thus nonempty legal incidence by itself would not license transfer of U2's default two-edge formula. A later native-incidence supply must either establish the required balance condition, or use its actual r_a in (4). Full signed-permutation covariance of a fixed port kernel would imply equal rows by transitivity, but such covariance cannot be assumed merely from six native axes or from P000. P000 is unchanged.

## Concrete conditional counterexample and limits

The five triples are

    {+1,+2,+3}, {-1,-2,-3}, {+4,+5,+6}, {-4,-5,-6}, {+1,+4,+5}.

All twelve incoming ports have a nonempty anchored family; every triple has three distinct axes. The positive component has degrees (2,1,1,2,2,1), while each negative component here has degree 1. The row sums in signed-port order (+1,-1,+2,-2,...,+6,-6) are

    (4/3,1,5/6,1,5/6,1,7/6,1,7/6,1,2/3,1).

For the adjacent pair with this same circuit at both sites and lambda=1/48, (4) predicts (1/144,5/768), whereas substituting neighbor count alone would give (5/768,5/768). See `incidence_check.json` for the actual BRC verification and operation counts. This counterexample falsifies the **transfer of a default-circuit formula to arbitrary syntactically anchored incidence**. It is not a second lawful native completion and does not prove native nonuniqueness. It does not claim autonomous P/Q-buffer reachability, indivisible-quantum realization, force asymmetry, physical instability, or material motion.

The preserved all-depth field bound needs positivity, fixed linear propagation, total column weight rho<1 and finite injection; it does not require uniform rows. Storage/reaction or evolving occupancy can change those hypotheses, so they require their own joint-state propagation and error statement. The exact missing native interface remains the incidence-to-action realization plus reaction/storage-to-occupancy successor relation in `INTERFACE_CERTIFICATE.md`.

Method harvest: compose the existing U2 packet lift with T0 weighted-BRC CWM and a finite hypergraph counting/maximum argument. No new top-level tool family or literature-wide novelty is claimed. Proof authorship is this nonblind task execution; temporary collaborators and inherited source exposure do not constitute independent formal review.
