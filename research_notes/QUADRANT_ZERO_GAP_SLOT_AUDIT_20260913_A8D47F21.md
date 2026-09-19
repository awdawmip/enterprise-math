# Inactive-zero directional slots and gap-crossing address audit

Progress-Event-ID: quadrant-zero-gap-slots-20260913-a8d47f21
Research-Activity-ID: RA-20260912-gap-origin-a8d47f21
Researcher-ID: EM-CHAT-A8D47F21
Session: local-chat-gap-origin-a8d47f21 (local key, not platform-authenticated)
Status: CONDITIONAL_EXACT_PROOFS_AND_EXPERIMENTAL_BRIDGE; NOT_FOUNDATION; NOT_WORKING_TRUTH
Source snapshot: awdawmip/enterprise-math@f0108147c41766eb610da0805af1aefc8ef2e92c.
User proposal: put unrelated quadrant coordinates at zero so crossing a displayed axis is a simple transfer between slots.

## 1. Scope and existing interfaces

Treat zeros as inactive signed-direction address slots, not as deletion of nonzero hidden native coordinates. Six native coordinates may use twelve nonnegative slots; these are not twelve independent spatial axes. A full quadrant-block representation is also possible but needs one canonical active block and consistent frame/identity metadata; allocating a separate coordinate set per orthant is not necessary.

The existing X6 definition blob d5afee11cea0ace14a11f984e6374a95d399a953 is unchanged. Reuse its signed unit transitions, displacement metric and BRC laws. Consume the prior V2 multiframe/edge-identity proofs rather than restarting them. The exact V2 adapter blob c3f97db8286081077407e33c442e7a5a9d43ced3 and geometry backend blob a1a8dc4d1ca53fde2ca00d9b944c1b8aa346a152 were hash-verified and executed unchanged from the prior supplied bundle. The new experimental SlotAddress type is distinct from V2 Address: existing positive-only version-2 digits are not silently changed to allow zero.

## 2. Centered slots versus a gap between integer Cells

Centered scheme: E0(z)=(max(z,0),max(-z,0)), D0(p,m)=p-m. Require p,m nonnegative integers and p*m=0. This is a bijection onto that constrained set. Indeed D0E0(z)=z; conversely disjointness forces exactly the positive and negative parts. The pair (0,0) represents the actual old chart-zero coordinate, not a display-only origin.

For arbitrary nonnegative accumulators, N(p,m)=(p-c,m-c), c=min(p,m), uniquely normalizes their difference. Transported endpoint addition N(p+r,m+s) is associative by decoding. This is an operation on endpoint/coordinate representations, not a license to erase actual path steps or branch history. Centered crossing 1 -> 0 -> -1 has two old primitive steps.

For the user's gap-reference plus both-nearest-labels-1 preference, use a different scheme. Put the address cut between the old integers 0 and 1; no physical point or edge is added. Any auxiliary cut strictly in this interval induces the same discrete partition. Define

Eg(z)=(z,0) for z>=1; Eg(z)=(0,1-z) for z<=0.
Dg(p,m)=p-m+1_{m>0}.

The valid set has p*m=0 and p+m>=1. On the positive side p>=1 and Dg=p; on the negative side m>=1 and Dg=1-m. These are disjoint sets of integers covering Z. Thus DgEg=id and EgDg=id. The old zero Cell is preserved as negative-side label 1; an all-zero display marker is invalid. This is a discrete address convention, not a claim that a planar carrier develops physical holes or that every first-layer Cell has distance 1 to a point.

## 3. Exact crossing rule and distances

Decreasing the native integer by one gives:
(p,0)->(p-1,0) if p>1;
(1,0)->(0,1);
(0,m)->(0,m+1) if m>=1.
Increasing reverses these cases. Decode proves Dg(Ts(a))=Dg(a)+s, hence the operations are mutual inverses and preserve all existing signed translation compositions. Changing two storage fields at the cut is one native edge, not two independent twelve-dimensional steps.

Example: (2,0)->(1,0)->(0,1)->(0,2) decodes to 2->1->0->-1, exactly three old steps. Across sides, positive label p and negative label m are separated by p+m-1 steps; on the same side the distance is the absolute label difference. The tempting p+m formula belongs to the centered scheme, not this gapped scheme.

In six coordinates apply Dg in each registered frame, then use native differences Delta_i. Native squared distance is sum Delta_i^2 and N_min=sum |Delta_i|. Raw slot arithmetic is not the metric: (1,0) and (0,1) have raw slot L1 distance 2 but native distance 1. The required cross-side correction is an encoding effect, not a changed physical metric.

A simultaneous two-axis crossing is still two native steps with two ordered shortest realizations, not one primitive diagonal. Pure re-framing is different again: if the Cell does not move, the aggregate decoded key must remain unchanged, using the existing V2 frame conversion.

## 4. Information and BRC boundaries

REUSE_APPLIED: native B_min(Delta)=N_min! / product |Delta_i|!, labeled-walk transport and V2 multiframe alias normalization. REUSE_EXECUTED: unchanged V2 positive/signed codec, frame validation, move/displacement adapter and geometry.l1_distance. EXTEND_EXISTING_TOOL: directional-slot presentation adapter, not a new BRC family.

The coordinate map is injective, so each old labeled walk has exactly one encoded walk in a fixed frame. Edge identities, directions, order and weights remain attached. Empty history and a forward/backward two-step history can share an endpoint; normalizing slots never identifies those histories. Positive weights are not a signed/phase-cancellation model.

Do not zero genuinely nonzero omitted coordinates. The projection identity for carrier vectors u1+u2+u3=0 is not the native identity e1+e2=-e3. Native triples (1,1,0) and (0,0,-1) have the same carrier coordinates but differ by (1,1,1), whose native squared length is 3. Common depth and other required coordinates remain available. Unknown or unobserved is not zero.

## 5. New exact tests actually executed

Python integer/Fraction tests PASS:
- 402 one-axis roundtrips across centered/gapped schemes;
- 202 gapped step/inverse checks and 10,201 one-axis metric pairs;
- 1,331 centered-normalization associativity probes;
- 4,374 V2/slot roundtrips on 729 six-axis Cells across three frames and two schemes;
- 26,244 gapped native move/inverse checks through the unchanged V2 adapter;
- 3,819 mixed-frame displacement/metric pairs;
- all 22,621 twelve-direction words of lengths 0..4, with exact endpoint-wise weight histograms;
- 1,289 shortest-path multinomial checks;
- 9 invalid/mixed-type rejection cases;
- explicit two-axis corner, old-zero preservation, projected-state collision and raw-slot-distance witnesses.

These are new bridge regressions, not a replay of the V2 suite, an exhaustive repository test or a Lean build. The general claims follow from the displayed inverse and transition identities, not from finite sampling.

Chat supplement files: slot_codec.py SHA256 7cde1b86566ad4383e1444868faf5ce2a3cad563eeaa1001150d879a2a1eaa04; check_slots.py SHA256 c08e2732f8d099598122b6ab6357ebaccfd9a1ca0db0df10ea19a80dcec195db; results.json SHA256 36be922b3fed69c9eb2f0f0355e57bb12a9098bb85e5077c6a73122ee29e9035. This note preserves the complete mathematical frontier; the executable supplement is supplied with Chat and is not claimed to be production source.

## 6. Decision boundary

Recommend the gapped signed-side scheme as an experimental presentation matching the user's stated goal. Zero may mean inactive slot; the opposite active slot retains the complete coordinate. New obligations: declare the cut and scheme/version, prove codec inverses (done conditionally here), test boundary switches and inverse updates (done in prototype), use decoded distances, retain frame/edge identity, and prevent physical-history cancellation. Unchanged native Cell population, adjacency, distance and path/BRC theorems do not need to be restarted. Final layer membership, production migration, full tests and Lean remain separate and unperformed. No P000, Foundation, Working Truth, worldview, production code, physical origin, units or time rule is changed.

Standard background checked: official mathlib4 Mathlib.Algebra.Order.Group.PosPart, especially posPart_sub_negPart and posPart_negPart_injective. This supports centered sign-part representation; the gap-shift formula above is explicitly derived here, not attributed to an executed Lean certificate.
