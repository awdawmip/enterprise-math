# Euler controller memory: reference-completed orientation and incoming state

Status: PROVISIONAL MODEL THEOREMS AND EXACT TYPED-BRC CERTIFICATES; not independently reviewed or formally admitted.
Date: 2026-10-10 Asia/Tokyo (execution clock 2026-10-09 UTC).
Global read snapshot: cfa5ceb7a48aae08b1e4c10a877327947d8ebe8e.
Source read snapshot: a297578f23b36d9e1cc4fe38389681a104213973.
Prior proof: 139e5020f71ac304b6a95cc6d6f1cf046ce306e9, research_notes/chatgpt_direct/20261009_EULER_MOVING_WRITER_MINIMAL_OBSERVER.md, Git blob cc713e88213743d224952c55470800f720333028.
Activity reused: RA-347DF236B3CD57BBC455B432; local handle EM-DIRECT-9C64E4. Same conversation and exposed mathematical context, not independent replication.

## 1. Question and actual reuse

The previous observer omitted the writer's sheet and incoming vertex because its controllers read only the current endpoint. This unit specifies controllers that use those additional relations, identifies the required frame-independent state, and proves exact finite predictive closures. The reciprocal edge law, probe contact, shared field and rooted probe loops remain unchanged. The additional controls are declared comparison-model programs, not derived native force or scheduling laws.

One positive world contains a probe, a writer and ONE shared field/weight. At command boundaries the probe is at comparison base 0. The old unit-channel observer is (j,s,F,w), where j is the probe channel in Z3, s its base-relative sheet, F=(F1,F2,F3) the corrected bits of loops 0120,0130,0230, and w the writer node. Six raw edge records e and the writer raw sheet t remain present in explicit worlds. Arrow bits in edge order 01,02,03,12,13,23 are (0,1,0,0,0,0). A writer traversal a->b uses the existing law t'=t+e_ab+d(a,b), e'_ab=e_ab+1 over F2, with d(b,a)=d(a,b)+1. Contacts act on probe channels only.

The prior ZIP SHA256 is 7e243c48cbc42e64acf5de547dfb71e830f4405d81cc8dcf01ced44d12be061d. All 43 manifest entries were verified. Nineteen Python dependency modules were copied unchanged; no prior scientific checker was run. New execute calls brc_mobile_observer.execute, brc_sector_charges.world_edge, the old comparison read, reciprocal correction, contact, and positive CWM edge/propagate/recoalesce. New holds use the existing unit-weight CWM operation and record their reason. Full brc_weighted.py matches current Git blob 3f205696709e847909958a153f8fe10d3f6b70f0.

Comparison vertices, sheets, controller memory and dimensions of observation spaces are not native X6 axes, physical time, charge or energy. P000 and its residual-fidelity scope are unchanged. Operations use exact typed BRC; finite transition/rank certificates certify those executed rows. No trigonometry, numerical roots, matrix exponential or substitute world propagator is used.

## 2. A raw remote sheet is not a frame-independent decision variable

Fix the base reference: g(0)=0. A change of local sheet notation sends

e_ab -> e_ab+g(a)+g(b),  t -> t+g(w),  s -> s.

Thus a decision such as "move when raw writer sheet t=0" changes when only the notation at w is changed. Three loop bits F are invariant under this change, but they do not repair a bare t. Actual counterexample: probe j=field,s=0,F=000, writer at1 with raw positive sheet. Apply the bare-sign version of M13, then U2,C. Its phase is omega. Merely change the frame with g=(0,1,0,0), and the same bare-sign rule gives phase1. These inputs are frame-equivalent; the controller is not.

Define the reference-link completion

L_0(e)=0;
L_w(e)=e_0w+d(w,0) for w!=0;
theta=t+L_w(e).

All bit additions are XOR. theta is invariant under every root-fixed frame change. It equals the carried sheet that the old rule would yield on a direct return to the base; reading this formula does not itself perform that return or erase its future backreaction. This is a declared endpoint/reference-link controller input, not an unexplained absolute orientation.

Raw t and F together still do not determine theta: replace e by e+delta g with g(w)=1 but keep raw t fixed. F and t agree between these two preparations while theta differs. Those two full preparations are NOT gauge-equivalent because the carried writer sheet was deliberately not transformed.

## 3. The completion is an exact orbit coordinate, not an arbitrary hidden variable

For a fixed writer position, two raw fields have the same three F bits iff their difference is delta g for a unique g with g(0)=0. Proof: the three rooted triangles form a cycle basis of K4, so their common kernel is the three-dimensional cut space; the rooted potential is unique. Equality of theta then forces t'=t+g(w). Equality of probe s and j already fixes the remaining observed variables.

Consequently (j,s,F,w,theta) exactly classifies the root-fixed frame orbits of the raw core (j,s,e,w,t). Each class contains eight raw representatives. There are384 such atomic classes, or128 phase modes after leaving j to the channel-phase readout. With an incoming vertex a!=w included, there are1152 classes, or384 phase modes. Writer channel and complete path/source history remain in the full BRC world but are outside this controller input/observer scope.

Any frame-equivariant update of this same core, returning the probe to its base at the command boundary, descends to these orbit coordinates. This statement does not cover a controller querying omitted provenance, a new field component, an unrecorded clock, or the probe mid-loop.

## 4. Exact update rules for the completed sheet

The old probe loop Ui and inverse give

s' = s+Fi (+1 for the inverse),   F'=F+111,   w'=w,
theta' = theta + 1{w!=0 and w is a non-base vertex of gamma_i}.

The writer's raw sheet is unchanged during this probe operation. Its completed sheet can nevertheless change because the shared reference edge changes. Thus a parked carrier can retain its local sign while its orientation relative to the base changes. This is comparison-field dependence, not an assertion of instantaneous spatial interaction.

For an old writer move a->b:
- if one endpoint is 0, theta'=theta;
- if a,b!=0, let i label the rooted triangle through {a,b}. Then theta'=theta+Fi+1{a<b}, with Fi read BEFORE the move.

The field still changes by the old face mask b_ab, and w becomes b. In edge order01,02,03,12,13,23 the masks are110,101,011,100,010,001. The formulas follow by substituting the old reciprocal read/toggle law into theta; they were verified against all raw fields. Holds and probe contacts leave theta fixed.

Define H_0b, for b=1,2,3: if theta=0, apply the old endpoint gate M_0b; otherwise perform a recorded unit-weight hold. The radial move preserves theta, so H_0b is involutive on transport core data. It need not restore incoming history. All three H gates are root-fixed-frame equivariant.

## 5. An exact old-observer failure and its repair

Take two unit-weight worlds with identical old data j=field,s=0,F=000,w=0, but theta=0 versus theta=1. The old64 conditional phase record and total conserved label agree. Apply H03,U2,C. The theta0 writer moves to3 and changes F to011; U2 then flips the probe sheet and C sends its field unit to B. The theta1 writer holds; U2 preserves the probe sheet and C sends the unit to A. Outputs are respectively omega and1.

In the alpha basis, omega=-1+alpha^2, so the coefficient infinity distance is2. Any predictor receiving only the identical old record incurs error at least1 on one member of this pair. The discrepancy is omitted relational information, not numerical precision. Every actual world keeps its Q and positive weight.

The exact quotient for old commands plus the three H gates is (j,s,F,w,theta). Different old coordinates are separated by old controls. If only theta differs, a radial H incident to w changes a face in one input only; that probe loop followed by C separates the pair. At most three commands are needed. All384 classes are necessary among partitions refining exact probe-channel observation.

The prior invariant Q=(F2+F1,F3+F1)+q(w), q(0)=00,q(1)=01,q(2)=10,q(3)=11, remains unchanged. At one jointly known fixed Q, w is recovered from F. This leaves96 atomic states and32 phase modes. The reversible completed-sheet controls have exactly four96-state orbits, one for each Q.

## 6. Incoming dependence is a separate, finite memory requirement

Add N_ab: when the writer is at one endpoint of {a,b}, take the existing reciprocal move only if its destination is NOT the recorded previous vertex; otherwise hold. This is an explicit no-immediate-retrace gate, not a replacement of all prior controls by a nonbacktracking policy. On a move the previous vertex becomes the old current vertex; on a hold it remains unchanged.

Two worlds with j=field,s=0,F=000,w=0,theta=0 and previous=3 versus previous=1 have identical completed-sheet records. Under N03,U2,C they give respectively1 andomega. The first is blocked, the second moves. Thus theta alone does not encode incoming eligibility.

The enlarged quotient is (j,s,F,w,theta,a), a!=w. It is sufficient by the stated rows and minimal: old distinctions use the previous witnesses; if only a differs, choose N on the edge to one of the incoming vertices, followed by a changed face's Ui and C. Every pair of the1152 states has a witness of at most three commands. At fixed Q the count is288.

Only the most recent incoming vertex is required, not the whole past. A useful exact-erasure example has w0 and previous1 versus previous2; both N03 moves produce the SAME enlarged quotient with previous0. Their former distinction is no longer effective under this controller language, although audit histories are not erased. N gates can therefore be many-to-one on predictive states; they are not claimed involutive.

## 7. Minimal linear phase records and executable certificates

For each joint mode m=(s,F,w,theta), or m=(s,F,w,theta,a), retain

v_m = sum_{worlds in m} positive_world_weight * probe_channel_phase.

These are unnormalized Q(omega)-valued readouts, not positive masses. Non-contact commands send a contribution to its exact target mode. Distinct sources are ADDED when N merges modes. C multiplies by omega at s0 and omega^2 at s1. Thus the recurrence predicts every future phase after any common command word or common normalized positive mixture.

Dimensions:
- previous endpoint-only family:64 modes,16 at fixed Q (consumed prior result);
- completed-sheet gates:128 modes,32 at fixed Q;
- also incoming gates:384 modes,96 at fixed Q.

The new linear dimensions are minimal over Q(omega), not lower bounds for arbitrary nonlinear scalar encodings. A closure search composed ONLY actual BRC atomic rows to obtain128 and384 controlled scalar phase probes. Their square matrices contain third roots of unity. Under the ring homomorphism omega->2 in F7, determinants are5 and2, respectively, hence their exact determinants in Q(omega) are nonzero. Maximum word lengths are6 and7. Every fixed-Q column restriction has full rank32 or96. The restricted-rank certificate does not claim an optimal control length.

The standard-library verifier checks every163840 entry by exact action-row composition, plus8192 entries by fresh explicit BRC execution, then verifies the ranks. These are controls on identically prepared copies, not passive time samples of one changed run. Invertible128/384 probe matrices and linearity prove minimality on the span of differences of positive preparations. Equal channel mass in A/B/field inside each mode gives a nonempty positive all-future-zero example.

Precisely: all future allowed phase observations vanish iff EVERY v_m vanishes. Present cancellation sum v_m=0 is weaker. Full positive path count, total and dominant weight require the384/1152-bin CWM quotient, not the phase moments alone.

## 8. Why merely reading a hidden variable need not force a new state

For an existing quotient q, a stochastic controller pi(u|X) factors exactly through it iff, for every pair q(X)=q(Y) and every retained target z,

sum_{u:q(T_u X)=z} pi(u|X) = sum_{u:q(T_u Y)=z} pi(u|Y).

The current observation must also factor through q. This is equality of the induced transition, not a requirement that the underlying command labels themselves be identical. It proves sufficiency by induction and necessity for a well-defined quotient transition. H and N violate this condition on the older quotients in sections5 and6, while the completed quotients satisfy it.

A rule reading additional probe-channel data may require a different linear observer even when its atomic state is finite. The present phase closure uses controllers whose routing/holding does not depend on probe channel j. No universal permission to reuse128/384 moments for arbitrary later feedback is asserted.

## 9. All-future initial-compression bound

Each initial mode under a deterministic word has one final mode and one multiplier in {1,omega,omega^2}; N may merge different initial modes but does not split one. Their alpha-coefficient infinity norms are at most2. Therefore

sup_words ||Delta Z||_infinity <= 2 sum_m ||Delta v_m||_infinity.

For per-mode initial error epsilon this is256epsilon or64epsilon at fixed Q for the completed-sheet family;768epsilon or192epsilon at fixed Q with incoming gates. Common normalized mixtures preserve the bound. It is independent of word length with exact subsequent updates. Fresh roundoff, wrong-Q preparation, noisy probe inversion or a changed controller language have separate error obligations. Fixed slot count does not imply fixed rational bit complexity or runtime speedup.

## 10. Exact evidence and current frontier

Final main checker:802309 assertions, including21 source/dependency/prior-proof integrity assertions. Most are the662976 finite pair-separation witnesses, not independent experiments. It checks all1152 atoms under23 actual commands; all64 raw fields, both carrier sheets and four writer positions; all root-fixed frame changes and H covariance; complete rooted frame orbits; inverse/core and genuine merge examples; unchanged positive weights, phase recurrence and explicit branch accounting through five commands. The completed-sheet graph has four96-state orbits.

The separate rank verifier passes172042 assertions. Combined total974351, with no claim of statistical significance from a large assertion count. A build audit additionally verified43 prior ZIP entries. No prior scientific suite was executed.

Final main-run old CWM calls: edge318755, propagate264271, recoalesce1456. The logged counter file is authoritative if expanded; source transition/contact counters and rank direct-replay counters are separately scoped. A syntax parenthesis error and a reference to a nonexistent ONE constant occurred in development; both are preserved in logs and corrected. They are implementation defects, not mathematical residuals. Final check scripts both exit0.

Run python -S check_controller_memory.py and python -S check_rank_certificate.py with standard-library Python3.10+. The optional certificate search script uses NumPy only for finite mod7 elimination; scientific world rows still come from the sourced BRC. The delivered selected certificates and their standard-library verifier do not require NumPy or network access. Executable dependencies, proofs, witnesses, matrices and checksums are in the conversation evidence package; publication of this manuscript alone does not assert all package bytes are stored remotely.

Primary background checked at official abstract scope: Petreczky, Bako and van Schuppen, Realization theory of discrete-time linear switched systems, arXiv:1103.1343v2, for established observability/rank/minimal realization context. Reference-completed observables have existing gauge-theory analogues; no continuum field equation or literature-wide novelty claim is imported. All model-specific statements above have their own finite derivation/certificate.

Completed unit: reference-completed writer orientation; exact rooted-frame orbit quotient; sheet- and incoming-controlled counterexamples; minimal384/1152 atomic and128/384 linear observers; fixed-Q reductions; genuine forgetting of obsolete incoming data; exact all-word error bounds. The next native question is which incident/link relation actually supplies the controller and whether its timing can be implemented by justified local operations. A distinct useful mathematical continuation is to study passive/noisy observation under one autonomous controller, rather than equating controlled-copy observability with measurements from one trajectory.

The activity is the same previously verified local registration. Current snapshots and immutable readbacks are tracked separately from formal task ownership, independent review and mathematical admission. No background or asynchronous execution is implied.
