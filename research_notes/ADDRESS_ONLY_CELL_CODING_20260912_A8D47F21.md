# Address-only Cell coding with nonoperational reference axes and origin

Progress-Event-ID: address-only-cell-coding-20260912-a8d47f21
Research-Activity-ID: RA-20260912-gap-origin-a8d47f21
Researcher-ID: EM-CHAT-A8D47F21
Session: local-chat-gap-origin-a8d47f21 (locally assigned, not a platform ID)
Status: EXACT_CONDITIONAL_DERIVATION_AND_FINITE_REGRESSION; NOT_FOUNDATION; NOT_WORKING_TRUTH
Control/source snapshot: awdawmip/enterprise-math@df15bdb05ecf2c591bac847fbecda6e5162b23d6.
Native mathematical input reused at d63e2915f3b54a3e6271f8050245d499153a6446: definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md and definitions/ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.md.
Prior conditional audit consumed: research_notes/RECESSED_ORIGIN_UNIT_LAYER_AUDIT_20260912_A8D47F21.md at befbe745553305a4b589393e3410fa8e7d04423f.

## 1. User clarification and scope correction

User: if the goal is Cell coordinate coding, with the number axes and origin not participating in operations?

Interpret the proposed external/gap origin as a reference/display object, not a Cell, graph vertex, path endpoint, scalar zero of a new algebra, metric source, or physical extra dimension. No radial equal-distance condition or recession-depth equation is needed for address-only coding. The previous Euclidean equal-distance and apex-shortcut calculations remain conditional facts but their extra hypotheses are not part of this clarified goal. Do not delete the Cell formerly carrying the coordinate label zero. A numeral zero in displacement algebra and a drawn reference origin are different types.

The distinction is semantic: not drawing/using axis lines is not enough if software still treats address digits as ordinary lengths or arithmetic operands. In that case the numeric encoding is operational and its interfaces must be transported. Primitive direction labels and relative incidence are not removed merely because drawn axes are nonoperational.

## 2. Exact transport theorem

Let C be the Cell set with all required typed relations and decorations. Choose an injective encoding E:C->A and use only its valid image A_valid=E(C). Let D:A_valid->C be its inverse, so DE=id_C and ED=id_A_valid.

For an existing k-ary Cell operation F define

F_enc(a1,...,ak)=E(F(D(a1),...,D(ak))).

Partial operations retain their transported domains. Scalar observers are transported without inventing Cell-valued outputs: f_enc(a1,...,ak)=f(D(a1),...,D(ak)). A relation R is transported by R_enc(E(P1),...,E(Pk)) iff R(P1,...,Pk).

Induction on expressions gives evaluation_enc(E(inputs))=E(evaluation(inputs)) for Cell-valued expressions, and unchanged scalar values. Injectivity then preserves exactly the original typed identities. Codes need not be closed under ordinary addition/multiplication: no such code operation was declared. This is a change of representation, not evidence that a new numeric formula is correct.

For primitive labeled transitions T_i^s, set T_enc=E T_i^s D. A labeled walk P0,...,Pn maps bijectively to E(P0),...,E(Pn), preserving n, each direction/port and every transported weight. Inverse D supplies the inverse walk map. Thus graph shortest lengths and multiplicities are unchanged. Existing native component distances must be decoded or separately transported; they are not ordinary differences between arbitrary code integers. Other Cell decorations must also remain available if future operations need them.

## 3. Unit first layer without an origin vertex

Fix any nonempty first-layer Cell set S1 in the connected native unit-step graph G. Define

L(P)=1+min_{Q in S1} d_G(Q,P).

The minimum exists because the candidate distances form a nonempty subset of nonnegative integers. L(P)=1 iff P in S1. For adjacent P,Q, |L(P)-L(Q)|<=1 by the triangle inequality and minimization. Same-layer edges are permitted. This adds only an observer, no edges and no new state O. Infinite S1 is allowed; layer 1 does not assert common metric distance 1 from one point.

A code can be (frame_id,L(P),j(P)), with j injective within each layer and a reversible lookup. The frame field is metadata, not an operand. Distinct Cells in layer 1 have different full codes, for example (1,1),(1,2),(1,3). There is no zero-th Cell requirement. Layer/direction alone must not be presumed unique without proving injectivity.

Concrete positive-integer implementation from a retained signed d-coordinate chart: f(n)=2n+1 for n>=0, f(n)=-2n for n<0. Its inverse is (a-1)/2 for positive odd a and -a/2 for positive even a. E(x)=(L(x),f(x1),...,f(xd)) is injective, has no zero fields, and rejects the all-zero display marker. Layer is checked against the decoded address. The chart is encoding metadata, not an ontic origin. This implementation is illustrative, not a forced choice of S1 or production schema. Label subtraction fails as displacement already at f(1)-f(0)=2, whereas 1-0=1.

## 4. BRC applicability and information-loss witness

REUSE_APPLIED: native X6/signed-slice N_min(z)=sum |z_i| and B_min(z)=N_min(z)!/product |z_i|!. The walk bijection applies these exact laws without re-proving a changed path system. Alternative branches and serial compositions retain their labels; positive rational weights are transported rather than averaged. This is not a signed/phase-cancellation claim.

A layer-only observer is not operation-safe. In the raw three-axis example S1={0,e1,e1+e2}, both 0 and e1 have L=1, but applying +e1 gives L(e1)=1 and L(2e1)=2. Hence there is no deterministic map on the scalar layer alone that represents this primitive transition on all states. Retain the within-layer identity and transition relation.

Current min-zero source observations also need their common-depth repair. Replacing min-zero r by min-one r+1 is fine only if the original depth is retained when native identity/metric is needed. Tuples (0,0,0) and (1,1,1) both have min-one residual (1,1,1) but are different Cells. More code fields do not automatically mean additional spatial axes.

## 5. Exact finite regression actually executed

A 125-vertex induced cube {-2,...,2}^3 with the S1 above was encoded and decoded. PASS: all roundtrips and code uniqueness; 600 directed labeled edges; 15,625 ordered endpoint pairs for identical shortest distances, shortest-path counts and decoded displacements. Counts also match the native multinomial formula. Positive-rational weighted walk distributions match exactly at each length 0 through 6 (seven layers). The zero display marker is rejected. The scalar-layer and numeric-label-subtraction counterexamples are checked.

These are finite regression tests supplementing the general proof, not full-repository tests, Lean compilation, or formal theorem admission. The Python verifier and results accompany the Chat artifact. No P000, native Cell set, primitive adjacency, distance, time, worldview, Foundation, or Working Truth change was made.

## 6. Disposition and next boundary

For the clarified address-only goal, gap/external/visually recessed origins are legitimate nonoperational display choices. Recommend a reversible address layer separated from the signed relational/operation layer. Existing invariant mathematics is transported; code decoders, numeral-assuming formulas, frame changes, invalid-code checks and multi-chart consistency require interface tests. A production adoption still specifies S1 and the within-layer address rule; neither unspecified choice blocks this conditional answer.

Standard reference: Mathlib.Combinatorics.SimpleGraph.Maps (graph isomorphism / induced relabeling) and Mathlib.Combinatorics.SimpleGraph.Walk.Maps (walk map, length_map, map_append, reverse_map), official mathlib4 documentation retrieved 2026-09-12. These references support standard mathematics only, not physical claims or project-specific theorem admission.
