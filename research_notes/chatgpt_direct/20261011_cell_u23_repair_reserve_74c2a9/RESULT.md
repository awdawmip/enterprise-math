# U23: reusable reserve and the order of first contact loss

Event: EM-20261011-CELL-U23-REPAIR-RESERVE-74C2A9
Status: CONDITIONAL_FINITE_CONTACT_THEOREMS / EXECUTED_TYPED_BRC / UNREVIEWED
Global read:2415716de586c52eb2615cc10604432998460ece
Source intake:3d174bc233263dd45efebc34e5704e7506991ba5
Predecessor: uploaded U22 OPERATIVE-RESIDUAL-6E91F4;25 manifest entries and seven dependency pins verified. This is new U23 research, not a retransmission of the earlier rejected U22 report. Activity registration remains unresolved; no old session, Task/CLAIM or native-force admission is assumed.

## New question and exact model

Keep the four bodies at(0,E1,E1+E2,E2) in X6 and the same initial active contacts AB,BC,CD. The remaining coordinates are explicitly0 in this finite preparation, not omitted axes. Every side is absent, A, or operative D; a present side retains one of two source cuts and consumes ONE identified record. A->D retains that record and operative path. D->0 releases it. Original U21 toggle and U22 source/path interpretation are reused unchanged.

Compare total available records B3 and B4. Capacity counts edge records, not materials. In B4 the fourth record can add AD, producing an alternate connected route before loss. All disconnected states fitting B remain allowed. Fixed geometry is a deliberate diagnostic: no claim about moving-body lifetime is made.

Unlike U22, capture and mode frequencies stay fixed; ONLY final release is thinned by epsilon. The new30-label trial law:

- share1/2: one of six pairs, flip an existing A/D with acceptance1/2;
- share1/4: one of twelve pair/cut labels, capture a missing adjacent D with probability x/(1+x) if a record is free;
- share1/4: one of twelve pair/cut labels, a matching D is released with probability epsilon/(1+x).

Here x=lambda=1/48 and0<epsilon<=1. The release is implemented as a separate Bernoulli(epsilon) then the old acceptance; all refusal alternatives remain. At accepted capture each free identity is chosen with probability1/(B-m). There is no connectedness filter or state-dependent deletion of waiting labels. These are candidate kinetics, not derived physical rates or native triadic forces.

For a present side the A/D flip probability is f=1/24. For each absent adjacent side the capture probability is b=1/1176. For a D side the full-release probability is epsilon*d with d=1/49.

## Finite reduction and exact all-time calculation

Full fixed-geometry states are625 at B4,369 at B3. Let(a,h) count A/D contacts. Before first loss of effective connectivity, a+h=3, or4 when B4. The nonwaiting count transitions are

 (a,h)->(a-1,h+1): a*f;
 (a,h)->(a+1,h-1): h*f;
 (a,h)->(a,h+1): (4-a-h)*b, provided a+h<B;
 (a,h)->(a,h-1): h*epsilon*d.

A drop from3 to2 is BREAK. All full states in the same fiber have identical target CWM, including free-token-choice multiplicity. Thus count/total/dominant first-loss observations compose exactly on4 or9 transient count states. This quotient is scoped to the fixed four-side uniform proposal grammar, not to arbitrary identity-sensitive or moving-state observations.

Actual all-time computations use the unchanged U22 pointed BRC algebra: transfer(W,M), serial(WV,MV+WN), positive loop closure C with pointed mass CMC, and positive state elimination. Every transient first-step mean equation is checked. No time cutoff, ordinary matrix inverse or fit supplies the all-time answer.

Rounded displays of E[first effective disconnection], SAME initial three-A tree:

 epsilon1/64:   B3=2106.6286,   B4=4915.2144;
 epsilon1/256:  B3=8378.6571,   B4=53063.9289;
 epsilon1/1024: B3=33466.6643,  B4=747418.6833;
 epsilon1/4096: B3=133818.6661, B4=11552997.6750.

Exact fractions are in paired results.json. At epsilon1/1024 the B4 mean number of successful captures before BREAK is28.4579105308, including initial creation of the fourth side, not only later repairs. Cap3 has no capture before first loss because the initial tree uses every record.

The initial full contact laws at B3/B4 already differ by TV1/1176: the fourth-edge birth becomes possible while all three original edges are still present. This effect is caused by a declared reserve state, not a change of body positions or cardinality.

## Exact lifetime powers and their positive certificates

As epsilon decreases to0,

 E T_3 = (98/3) epsilon^(-1)+O(1),
 E T_4 = (49/72) epsilon^(-2)+O(epsilon^(-1)),
 E T_4/E T_3 ~ 1/(48epsilon).

Proof. Regenerate at o_m=(m active,0 dormant), m3 or4, stopping an excursion on its first return or BREAK. Its mean length l and break probability p give E T=l/p. At epsilon0 the fixed effective graph's A/D mode population is uniform; the count state has Binomial(m,1/2) law. Therefore l(0)=2^m, and visits to dormant count j per return cycle have mean choose(m,j).

Cap3 requires one actual release. Its leading break coefficient is

 c1=d SUM_j choose(3,j)j=12d=12/49.

Cap4 requires two actual releases before repair. After the first loss, let g(j) be cumulative D-edge count up to repair at rate b, with3 remaining effective edges and j initially D. Mode flips remain f. The exact positive first-step solution is

 g(j)=j/(b+2f)+3f/[b(b+2f)].

It solves(b+3f)g(j)-(3-j)f*g(j+1)-j*f*g(j-1)=j, with boundary terms removed. Its Binomial(3,1/2) mean is3/(2b). Thus

 c2=d^2 SUM_(j=1..4) choose(4,j) j g(j-1)=48d^2/b=1152/49.

Mean cycles8 and16 divided by these coefficients yield98/3 and49/72. A three-edge start reaches the four-edge regeneration state in finite mean when epsilon0; its small-epsilon pre-arrival loss probability is O(epsilon), affecting only the lower order.

Why the coefficient sum covers the whole future: after killing return-to-base, the finite zero-release chain has a uniformly positive bounded-length repair/mode path to absorption from every transient state. Its survival tail is geometric, uniformly near epsilon0. The stopped path sums and moments are analytic there. No history with fewer than r=1 or2 actual deletions can break, so the first nonzero coefficient is the POSITIVE sum of exactly-r-deletion histories, with other factors evaluated at0. Corrections to waiting weights contribute only to higher order.

The code separately executes this coefficient construction with a deletion counter and original positive BRC recurrent closures. The computed coefficients12/49 and1152/49 are weights of marked history families, not probabilities;1152/49 exceeding1 is not normalized or treated as a physical probability. The result is not inferred from numerical epsilon sweeps.

## Finite-record transport and repeated reuse

Resource identities are not equal-weight hidden copies. For m contacts, uniform free-identity choice gives the reversible identity lift w_micro=w_graph/(B)_m, w_graph=(x/epsilon)^m. Each birth chooses1/(B-m), its inverse releases that exact ID, and weighted flows match. Summing identity assignments recovers w_graph. Giving every assignment the uncorrected graph weight would be a different ensemble.

All15666 allowed identity assignments and25592 identity-changing birth/inverse pairs are checked. These are identity states, not an asserted equilibrium sum over arbitrary free-record storage positions.

A resource transcript uses the same four records repeatedly. Create AD with the spare at A. Then BC switches to D, releases its ID at B, and captures with that same ID, restoring the cycle. Twenty such cycles are executed without adding any identity. Two successive genuine releases also produce a disconnected state, confirming no forced connectedness. Cross-use of released IDs includes real one-edge transfers between A and B.

Each capture delivers the selected free record along at most two native edges in this fixed geometry, then calls original ContactInventory.toggle. Every hop updates its position. Reservation/detachment and commit preserve disjoint free/held/bound identities. Proposals are padded to five declared work stages, including actual delivery, so this serialized timing does not bias the macro-proposal law. Concurrent losses during delivery and physical rates are outside this witness. Recycling records does not prove zero energetic work, inexhaustible support or a native three-force reaction.

## General finite-contact consequence and exact boundary

Let a finite connected available contact graph G have enough records for all its edges. Suppose absent edges have positive epsilon-independent repair paths, local A/D states communicate by fast operations, and each complete deletion has weight epsilon times a positive coefficient. Keep a fixed finite grammar, with no loss of repair eligibility or other disconnecting mechanism. If r is the fewest edges whose removal disconnects G, then from the fully repaired graph

 E T_disconnect = Theta(epsilon^(-r)).

Proof: regenerate at a fully repaired reference state. All nondeleted transitions give a uniform finite repair route, hence bounded stopped-excursion moments. Fewer than r deletions cannot disconnect. A selected minimal cut supplies a positive finite r-deletion path with no intervening repair or return. Thus the first nonzero positive deletion-order coefficient is r, and regeneration gives the result. At B3 the four-edge repaired state is unavailable, so the enough-resources hypothesis fails and the order is1 instead of2.

For every fixed positive epsilon in the present finite model, first disconnection still has probability1 and finite mean. Repair improves lifetime; it does not prove permanence. Complete deletion remains possible. This is a finite fixed-contact theorem, not a theorem that the full moving four-body process has the same exponent.

Because only detachment is slowed, equilibrium also changes: beta=4x/epsilon,

 Z_B=SUM_(m=0..B) choose(4,m)beta^m,
 connected mass=4beta^3 for B3, or4beta^3+beta^4 for B4.

This is not U22's unchanged-ratio clock rescaling. Both stationary connected shares tend to1 as epsilon0 while each positive-epsilon history eventually first disconnects. Occupancy, first-loss time and permanent connectivity are distinct.

## Execution and continuation

68124 assertions;4970 full row cases; complete stationary inflows; all4/9 mean first-step equations;12-trial source/cut versus count prefixes;625 inherited path bridges;15666 identity states;25592 identity flux pairs;104 explicit resource hop/binding phases. Actual BRC calls: edge81283, alternative354719, serial339446, recurrent587. Same-author isolated replay reproduced results and compressed trajectory bytes. No old full suite or independent review is counted.

Results SHA256:3982920270b38be6d3dd0624f94f807406a947fab8258bc8324b028346dc6b2d.
Raw trace SHA256:f6f4fe3d254954f3266c39f51dc91706362e64d03a4eba4386d47ab215a4ea20.
Compressed trace SHA256:33ee9c02e8c81c35d6da65d4a79100ad82731d2cf08d9febece0959a97682ec4.

Original seven-code chain: residual_contact6160eb24cda9ef576d2972ef45df8e16e9fe67a4; contact_network5f89fe162f230c5ce31c317bda17089935f1c7fc; mobile_junction37931d40d7a2edc36889366d4766c83319eef0e7; local_latent67408af5b977bed7295f7225cdd3f550c41b9729; connected_retention569e6171d0052fbfd41cf007b09a8327b339228b; packet_router7465f5aa16cbb8fba61ba4be80f8a6884b879c53; brc_weighted3f205696709e847909958a153f8fe10d3f6b70f0. Old scientific bodies unchanged. Full note, new code, dependencies and traces reside in cell_closure_u23_evidence.zip; Source report/results are scientific preservation, not an independently reviewed native implementation.

General attribution: Aldous/Fill author-hosted chapter2 section2 for occupation/return identities; Heidarzadeh/Sprintson/Singh arXiv1712.09666 official abstract for established cutset/repair reliability context. No general reliability-method invention or empirical-force inference is claimed.

Next: let released records and material/path states move, and check whether the fast positive repair route used by this proof survives. A sourced repair-window bound or an explicit moving/capacity counterexample is the next unit. Native material-field-support incidence/reaction remains to be established. The lifetime exponent here is a contact-topology/resource property, not a square-number or prime criterion.
