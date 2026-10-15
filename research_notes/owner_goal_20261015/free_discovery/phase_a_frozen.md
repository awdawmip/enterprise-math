# FREE Phase-A frozen packet: pairwise path summaries and a finite cubic residual

Candidate-ID: FC-FREE-20261015-C94B7F-PAIRWISE-RESIDUAL
Researcher-ID: EM-FREE-333687
Activity-ID: RA-09A10D86AD7D405CE35FBD97
Mode: direct FREE_AXIOM_DISCOVERY; no formal Task, claim, Result, Working Truth, or axiom promotion.
Frozen at: 2026-10-15T15:18:39.827409+00:00 (local UTC creation observation).
Phase-A status: BLIND_CANDIDATE_FROZEN, with ANCHOR_EXPOSED disclosure below. This is a derived conditional exact obstruction, not a proposed world axiom.

## Self-generated question

In the native six-axis Cell space, is endpoint plus the complete signed native-step inventory plus all fifteen ordered pair cross-moments sufficient for a finite-resolution path observer under arbitrary future native-step appending? If not, can one prove a sharp finite residual cost in an explicit local model?

The question arose from the P000 requirement to preserve ordered composite native paths and the residual-fidelity requirement that a current readout need not be complete state. No downstream current-result or tool catalog was consulted before this packet was frozen.

## Mother substrate and semantic typing

P000 is a project premise, not external scientific consensus. Space is the fixed Heartbeat X6 affine torsor over Z^6. Choose a native Cell anchor c_*; z is a raw signed six-axis chart, not a public final Cell address. There is no native plane or distinguished global origin. Every path step is one of the twelve signed native-axis primitives. The examples use only E1,E2,E3, with all omitted relative components exactly zero; they are restricted paths inside X6. The theorem and allowed future steps cover all six axes.

Time is explicitly and separately typed: t=0,...,n orders path updates; it is a discrete process index, with no claim of a physical tick or calibration. The residual r belongs to the finite internal carrier Z/mZ over each Cell and is not an extra spatial axis.

Primitive dependencies read in Phase A:
- p000_reality_foundation.json
- definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json
- definitions/RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json
- definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json
- definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md
- definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json
- definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md, spatial type and adjacency/metric/observer portion only.

The dynamic law below is a newly declared conditional toy model, not asserted heartbeat physics. It has one deterministic branch. Boolean/positive weighted/signed amplitude carriers are not identified; no positive-mass cancellation or branch erasure occurs.

## Candidate statement (all m >= 2)

For a word w in the signed six-axis steps, start z_0=0 and let d_t=z_{t+1}-z_t. Define:
- signed inventory N_{i,s}: number of steps s e_i, for i=1,...,6 and s in {+,-};
- endpoint z_n;
- all fifteen pair cross-moments A_ij(w)=sum_t (z_t)_i (d_t)_j for 1 <= i < j <= 6;
- base summary B(w)=(z_n,N,A).

Declare the finite local update and final observer
r_0=0 in Z/mZ,
r_{t+1}=r_t+(z_t)_1 (z_t)_3 (d_t)_2 mod m,
Obs(w)=r_n.

Thus a step on axes other than E2 leaves r unchanged; a signed E2 step adds the signed product of the current E1/E3 raw coordinates.

Claim:
1. B is not sufficient for Obs, even for closed length-ten paths with identical signed inventories.
2. For every m>=2 there is a single B-fiber containing all m observation values. Therefore any exact augmentation of B that preserves Obs needs at least m residual labels on that fiber.
3. The one m-valued residual r is sufficient for Obs after every finite future word of arbitrary signed steps on all six axes. The uniform residual cost is sharply m states (ceil(log2 m) bits for a binary fixed-width implementation).

## Exact proof

Write a=+e1, b=+e2, c=+e3 and use superscript -1 for the reverse signed step. Set

u = a b a^-1 b^-1,
P = u c u^-1 c^-1
  = a b a^-1 b^-1 c b a b^-1 a^-1 c^-1,
Q = (a a^-1)^2 (b b^-1)^2 c c^-1.

Both are closed paths of length ten. Both have N1+=N1-=N2+=N2-=2 and N3+=N3-=1, all other signed counts zero.

For P, A12 on u is +1 and on u^-1 is -1, hence A12(P)=0. Each c or c^-1 step occurs with z1=z2=0, hence A13(P)=A23(P)=0. Other pair moments vanish because coordinates/steps on axes 4,5,6 vanish. For Q, each immediate axis retracing has zero pair moment, so A_ij(Q)=0 for every i<j. Thus B(P)=B(Q).

On u and on Q every E2 step has z1*z3=0. On the inverse u at z3=1, its first +b step has z1=0, while its -b step has z1=1. Therefore r(P)=-1 mod m, whereas r(Q)=0. This proves (1) for every m>=2.

For (2), for k=0,...,m-1 let
W_k = P^k Q^(m-1-k).

Closed words concatenate with additive signed inventories, additive A_ij, and additive r because each component restarts from z=0. Every W_k has endpoint 0, A=0, and signed inventory exactly (m-1) times the shared inventory of P,Q. Thus all W_k share one base summary, while r(W_k)=-k mod m runs through all m residues. Any exact encoding whose current output factors through B plus an added residual must distinguish these m paths. This lower bound already follows from the empty future word and therefore also holds under arbitrary future appending.

For (3), retain (B,r). On a step d=s e_j update z by z+d, the corresponding inventory count by +1, A_ij by z_i*d_j for every i<j (using the pre-step z), and r by z1*z3*d2 mod m. These updates depend only on the retained state and the new step. Induction on the length of every future word proves that Obs is exactly reproduced. The m-label upper bound matches (2).

## Immediate consequences and falsifiers

A full signed inventory and all pairwise path moments do not license erasing every higher joint path distinction. One explicitly typed finite scalar residual can be both necessary and sufficient in a bounded declared observer language.

Obvious falsifiers: a correct exact computation giving B(P)!=B(Q), r(P)=r(Q) for some m>=2, failure of the concatenation argument for closed words, or failure of the stated one-step retained-state update. The polynomial local update is a definition; its existence is not a claim that physical dynamics chooses it.

The theorem does not claim minimality for a richer observer or future-operation language. Native rotations, path reversal as an operation, path splicing at an arbitrary historical interior Cell, access to path provenance, and arbitrary nonlinear observables require a fresh lease. No general-purpose tool family or formal task is created.

## Source exposure and independence

The session was initialized with only the parent's bounded FREE assignment. Before freeze it read operating/identity/activity governance plus the mother substrate listed above. It did not read existing research tasks/returns, active routes, current-result router, current tool coverage, or other agents' proposed questions. Its only parent updates were bookkeeping and this already self-generated structural question.

However, the mandatory weighted global substrate file was read in full. That current file includes detailed downstream commitments, IDs and module pointers beyond the minimal branch-typing excerpt advertised by the FREE router. Those mandatory-file contents were exposed before question generation; they were not used to generate this deterministic native-path question. To avoid overstating pristine blindness, freeze blindness_status is ANCHOR_EXPOSED, not CLEAN. No fresh-ID independence claim is made. The full exposure should remain visible during review.

Required foundation_snapshot_ref: local repository files listed above; exact hashes are captured in freeze_manifest.json.
worldview_snapshot_ref: p000_reality_foundation.json and HEARTBEAT_WORLD_NATIVE_X6_TIME.json.
structural_motivation_without_active_route_reference: ordered primitive composite paths plus future-sensitive finite residuals.
semantic_layer: conditional deterministic internal-state path model over native X6.
created_at_or_content_hash: see freeze_manifest.json.

## Phase-B boundary

This file is the Phase-A freeze. After its immutable source publication/readback, current-result and tool-coverage lookup may begin. Phase-B findings will be written separately and will not rewrite this origin story.

