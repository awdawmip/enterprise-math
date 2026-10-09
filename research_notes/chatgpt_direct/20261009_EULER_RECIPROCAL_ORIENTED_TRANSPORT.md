# Euler transport: reciprocal directions, signed winding and odd-cycle memory

Status: PROVISIONAL MODEL THEOREMS AND EXACT TYPED-BRC CERTIFICATES; NOT FORMALLY ADMITTED.
Date: 2026-10-09 (Asia/Tokyo). Same-conversation continuation; not independent replication.
Global read snapshot: a5016513f59f5b4d690eff09ff11e19551bf351f (verified in this turn, 2026-10-09 around 07:08 UTC).
Source read snapshot: eef565a6e15271ff6afc2688099f5fdae1139fde.
Prior frontier: 3f56aa79fef5dca840e7088589969d62be3340c0, research_notes/chatgpt_direct/20261009_EULER_LOCAL_EDGE_BACKREACTION.md, blob 1eeb8b8bff7afd91f66360bd5ab963a81811174c.
Logical conversation: chatgpt-heartbeat-euler-20261004-layer-01; not platform-attested.
Research activity: UNVERIFIED / REGISTER_PENDING. No borrowed role, CLAIM or acceptance.

## 1. Question and scope

The previous directionless read/toggle rule was locally invertible, but the same rule on a reversed spatial edge was NOT its inverse. This unit asks whether reciprocal directed transport can remove that immediate-retrace effect while retaining the joint four-state Euler readout around a triangle. The answer is yes, conditional on explicit directional comparison data. A general graph theorem then identifies exactly when the remaining fourth-order loop memory can occur.

This is a candidate extension of the existing comparison interface, not a derivation of a native force law. Each undirected comparison edge receives a DECLARED positive arrow. Traversal with the arrow and traversal against it are distinguished. Numbering vertices is a storage convention, not an intrinsic way of selecting arrows. Relabelling tests push forward arrows, fields, paths and endpoints together. The source undirected field alone does not determine these extra data.

The sourced K4 vertices are comparison contexts, not native X6 positions. Restricting commands to a connected subgraph below is a mathematical test of the transport interface, not replacement of the six-dimensional world. Bits, signed edge counts and cycle rank are internal/representation data, not additional spatial dimensions. No native 90-degree angle, physical time reversal, energy law, spin or quantum effect is inferred. P000, separate time, native 120-degree orthogonality and the residual-fidelity contract are unchanged.

Actual reuse: the prior attachment has SHA256 0746ee1c81a064f647eed20d531105aa2464fd02cfa5757caa3f6bcb2c13000a. All 32 prior manifest entries were checked. Its unchanged brc_edge_backreaction.py has SHA256 5b310a371c99c92f19a8e1136310a4361b388ad2d1ec78ecc48320f219e2e68c. The new adapter calls its prescribed/children operations, which perform the old sourced comparison read, old positive CWM serial/merge, and post-read toggle. A separately recorded unit-positive-weight inverse-direction correction is the only new transport action. The source full CWM blob remains 3f205696709e847909958a153f8fe10d3f6b70f0, and the bundled full bytes match. The source chirality full blob remains 6f8b147c094720c2749f620a40394c4d7b67a386; its previously inspected dependency-closed excerpt, not the full module, is executed unchanged. The existing three-channel contact is used unchanged in joint-loop tests.

REUSE_EXECUTED / COMPOSE_APPLIED / EXTEND_EXISTING_TOOL. No new admitted tool family. No numerical pi, trigonometry, roots, matrix exponential or alternative world propagator. Integer cycle/group formulas are proofs and certificates of the actually executed BRC actions; they are not positive populations. Explicit branches retain source root, weights, incoming/current vertices and chronological history.

## 2. Exact classification of reciprocal local pairs

Write bits additively over F2. Let s be the carried sheet, e the current edge record. The prior exhaustive equivariance theorem gives, for each fixed direction separately,

F_d(s,e) = (s+e+c_d, e+b_d).

Here d=0 means with the declared arrow and d=1 means against it. Requiring F_1 F_0 = F_0 F_1 = I is equivalent to

b_0=b_1=b,  c_0+c_1=b.

Indeed a composition has field increment b_0+b_1 and sheet increment b_0+c_0+c_1. There are exactly four reciprocal pairs. If forward zero-record transport is transparent (c_0=0), the choices are the static pair b=0, or the unique nonstatic reciprocal pair b=1:

F_0(s,e)=(s+e,e+1),
F_1(s,e)=(s+e+1,e+1)=F_0^{-1}(s,e).

Both retain the original post-read edge toggle. Backward traversal has an additional sheet correction. Requiring zero-record transparency in BOTH directions would exclude this nonstatic pair; that stronger requirement is not silently assumed.

Without a directional distinction the same map would have to serve in both directions. For a covariant directionless law F(s,e)=(s+e+c,e+b), one has F^2(s,e)=(s+b,e). Reciprocity therefore forces b=0. A nonstatic reciprocal law cannot arise from that directionless two-bit carrier alone.

The new directed rule is s'=s+e+d, e'=e+1. Locally r=2s+e mod4 changes by +1 with the arrow and -1 against it. This local r depends on the chosen frame and is not promoted to a closed, gauge-relative observation. Section 4 supplies the relative loop version.

## 3. Signed traversal counts repair the retracing problem

Fix the arrow data. For a path gamma let k_a be the signed number of traversals of edge a: positive with its arrow, negative against. Let p_a=k_a mod2 and

q(k)=sum_a binom(k_a,2) mod2,

where binom(k,2)=k(k-1)/2 is an integer for negative k as well. In pure transport, with no intervening sheet reset or channel collision,

e_T=e_0+p,
s_T+s_0=e_0.p+q(k) (mod2).

Proof: the forward action on edge a has fourth power identity and inverse equal to the backward action. Its kth power reads (e_a,s) as e_a+k, s+k e_a+binom(k,2), for every integer k. Actions on different edges commute on the joint edge/sheet state. Composing the integer powers proves the formula. Actual negative-net-count paths were checked, not only forward traversals.

For two segments with residues (p,q) and (r,t), chronological composition is

(p,q)*(r,t)=(p+r,q+t+p.r).

The inverse is (p,q+|p| mod2). Since k(reverse gamma)=-k(gamma), a path followed by its reversed path has zero signed counts and is exactly identity on field, sheet, channel (unchanged during transport) and spatial comparison endpoint. Inserting or deleting an adjacent edge/reverse-edge pair likewise has no transport effect.

This does NOT reverse elapsed time, delete provenance or recover the old incoming-neighbour record automatically. In the actual carrier, an out-and-back path returns with its last visited neighbour as the new incoming neighbour. Recovering that previous-control datum requires its retained history or an explicitly declared inverse controller. The inverse tests observe the transport output, not a false equality of all audit fields. Nor is immediate reversal silently made part of the old NB random grammar: prescribed reversal is a separate allowed inverse-control experiment; the forward equal-NB tests still exclude immediate reversal.

Comparison with the previous directionless law is explicit. With the same raw path and initial field, the two sheet residues differ by the parity of the number of traversals against the declared arrows. The old two-edge out-and-back sheet flip disappears in the reciprocal model.

If the field is restored, p=0 and k=2m. Then

s_T+s_0=sum_a m_a mod2.

This is signed winding information, not total distance travelled. The old rule L/2 cannot be reused: an out-and-back has L=2 but k=0, and now restores the sheet. Two traversals of the SAME oriented odd cycle have k=2c with sum c odd, and still reverse it.

## 4. Reciprocal reversal and a relative fourth-root Euler readout coexist

Fix a simple oriented triangle gamma and let D_gamma be the parity of the number of its edges traversed against their declared arrows. Let f be the XOR of the three CURRENT edge records at the beginning of a lap, and define

F_gamma=f+D_gamma.

Let s_rel compare the carried sheet at the base to a separately retained base reference. Static vertex-frame changes preserve f and this relative comparison, and arrows are transported with vertex relabellings. Thus the following observation is independent of those notational changes.

One forward lap reads each edge once and toggles all three, giving

(s_rel,F_gamma) -> (s_rel+F_gamma,F_gamma+1).

Reading the reversed triangle, while using the SAME forward-reference definition of F_gamma, gives

(s_rel,F_gamma) -> (s_rel+F_gamma+1,F_gamma+1),

which is its exact inverse. The reversal changes D by one because the triangle length is odd.

Set r=2s_rel+F_gamma mod4. In the already used alpha ring alpha^4-alpha^2+1=0, put beta=alpha^3, beta^2=-1, and w=beta^r. Actual forward laps induce w->beta w; actual reverse laps induce w->beta^-1 w. No scalar phase is inserted into the state update to enforce this result.

For arrows 0->1,1->2,2->0, an initially zero field and positive relative sheet give

(s_rel,F): (0,0),(0,1),(1,0),(1,1),(0,0),
w: 1,beta,-1,-beta,1.

Thus two same-oriented laps restore the whole raw field but reverse the sheet; four restore the transport core. A forward lap followed by the reversed lap restores the field/sheet in two laps. The two experiments have equal total edge count but different signed winding. This removes the previous retracing ambiguity WITHOUT eliminating the nontrivial four-cycle.

If the unchanged three-channel contact P^chi is inserted before each SAME-oriented triangle lap, four laps also restore its binary channels for all 64 fields, all eight triples and both sheets. This follows because the four collision exponents sum to zero: for initial F=0 they are chi,chi,-chi,-chi; for F=1 they are chi,-chi,-chi,chi. Reversing only a transport loop is not automatically an inverse of these interleaved collisions.

Beta can be represented by i in the selected external complex embedding. The construction identifies an exact joint-state four-cycle, not a native spatial quarter-turn or a unique physical source of the imaginary unit. A reverse geometric loop is also not a reversal of physical time.

## 5. General graph theorem: odd cycles are necessary and sufficient for fourth-order loop memory

Let G be any finite connected simple undirected comparison graph, with an explicit arrow on each edge and the same reciprocal rule. All statements in this section concern closed pure-transport paths, with arbitrary prescribed traversal/reversal allowed. No faces are filled: deleting a triangle is not an allowed path reduction merely because a drawn picture encloses it.

Let C=ker(partial:Z^E->Z^V) be the integral cycle lattice and b=|E|-|V|+1 its rank. Closed walks have signed count k in C, and every integer cycle can be realized by concatenating oriented cycles and connecting paths; those connecting paths cancel in signed counts.

The action map is phi(k)=(k mod2,q(k)) with the composition in section 3. Distinct (p,q) already have distinct outputs on the zero-field positive-sheet probe, so its image counts genuine field/sheet transport actions.

Its kernel has a simple exact form. A zero action must have k=2m with m in C, and then q(k)=sum m_a mod2. Hence

ker phi = {2m : m in C, sum_a m_a even}.

If G is bipartite, every cycle has even length, and sum m_a is even for every integer cycle. Then ker phi=2C, and

image phi is isomorphic to (C2)^b, with 2^b elements.

If G contains an odd cycle, m->sum m_a mod2 is a surjective homomorphism C->C2. The kernel above has index 2^(b+1). A fundamental cycle basis contains at least one odd generator. Its image has order four and square J=(0,1), the central sheet flip. Each other odd generator has the same square; dividing it by the chosen order-four generator produces an involution. Even generators are already involutions. Therefore

image phi is isomorphic to C4 x (C2)^(b-1), with 2^(b+1) elements.

This is a complete model-specific transport classification, not a new classification of finite abelian groups. An equivalent sharp criterion is:

A closed transport can restore every edge record while reversing the sheet IF AND ONLY IF G contains an odd cycle.

Necessity follows from the bipartite kernel calculation; sufficiency is two same-oriented laps of an odd cycle. On a tree b=0 all closed transports are identity. A single triangle gives C4; a single square gives C2; the sourced K4 has b=3 and gives C4 x C2 x C2, hence 16 actions. This matches the prior K4 action count but changes which paths represent identity: retraces now cancel. The previous enumeration is not claimed again as a new 16-element group discovery.

The implementation tests every connected labelled simple graph on vertex sets {0,1}, {0,1,2}, {0,1,2,3}: 1+4+38=43 graphs, realised as allowed-path restrictions inside the unchanged K4 interface. Graphs on more vertices are covered by the proof, not by an unperformed numerical experiment. These graph/cycle ranks are not counts of native spatial dimensions or primitive forces. In particular an odd cycle is not automatically P000 triadic stable balance.

## 6. Positive weights, safety of quotients and what is not restored

Each new directed step is a composition of the already executed positive BRC path action with a declared deterministic sheet correction of positive weight one. Existing roots, channels, field records, incoming/current vertices, history and CWM remain typed separately. Positive mass is never treated as a signed phase.

For the forward fresh equal-NB programme, every original path still has two alternatives of weight 1/2 per edge. From one unit path after n edges, CWM is (2^n,1,2^-n). Full-state histogram updates agree with explicit paths. No prior first-return probability or scalar persistence is imported into this new directed programme. Arrow/field/incoming correlations must be retained before deriving such a reduction.

The closed action summary may replace a completed pure-transport command word only for a future language that does not inspect erased intermediate paths. NB continuation still needs the genuine incoming neighbour; collisions require the retained channel/sign data, and history-sensitive controls require their own proof. Compressing a word to its action does not reduce all physical states to 16 or prove fixed bit cost.

Choosing different physical arrows while holding the original edge records fixed can change observations; it is a change of declared programme, not automatically a harmless relabelling. The tests establish covariance only when the complete data are transported under relabelling. Bare undirected source incidence supplies no deterministic preferred arrow: an endpoint swap exchanges the two choices. Deriving an actual directional relation from a native incoming channel remains open in this line.

## 7. Exact evidence and literature boundary

Final new suite: 78,237 exact assertions, including 32 prior-manifest checks and one current full CWM blob check. It covers the reciprocal classification, all 64 raw fields and both sheets on all 12 directed K4 edges, all 16 vertex-frame changes, 4,608 whole-data relabellings and their relative loop bit tests, 2,295 actual weighted path certificates, 1,152 whole-path reversal checks, all 1,024 field/sheet/triangle-arrow probes, 1,024 joint four-contact returns, all 43 connected small graphs, and the K4 action products on every initial field. Counts are not independent experiments, and this is not independent replication.

Actual old CWM calls in the final run: cwm_edge 357673, cwm_propagate 319202, cwm_recoalesce 6615. Old contact calls 4096; sourced transition_bit 168804 and gauge_action 51200. The new reciprocal edge wrapper was called 105796 times. No old scientific checker was rerun. The initial full run reached reporting but addressed a nonexistent source-counter name; it was corrected. A development PASS reported 69,021 assertions before the relabelling extension and initially selected the wrong, unrelated source-counter dictionary for its CWM summary. Final reporting reads the actual BRC call function's CALL_COUNTS. These were reporting defects, not physical residuals; logs are retained.

Run `python -S check_reciprocal_transport.py` with standard-library Python 3.10+ from the supplied directory. The package includes the unchanged dependency tree, proof, new adapter/checker, full finite witnesses and reproducibility hashes. Project publication stores this proof/frontier; it does not assert all attachment bytes were uploaded to Source or mathematically admitted.

Primary background checked at definition/abstract scope: Thomas Zaslavsky, Home Page of Signed, Gain, and Biased Graphs (author site), defines inverse labels on reversed edges; Nathan Reff, Spectral Properties of Complex Unit Gain Graphs, arXiv:1110.4554, official abstract, likewise states that inverse-orientation convention. This is established gain-graph practice. It is not evidence for this particular path-updated field, the odd-cycle theorem or a native physical law. No unread theorem and no literature-wide novelty claim are used.

Own bounded status request: private bridge 3515, status-20261009-euler-reciprocal-transport-25; its matching status reply was read. It grants no mathematical authority. The earlier activity remains unverified; no new CLAIM, independent review, formal Result or passed final guard is asserted. Old failed registration and safety-blocked contents were not replayed. No automation/index settings changed.

Completed increment: a reciprocal directional lift, actual inverse transport without erasing audit history, signed-winding residual, gauge-relative beta/beta^-1 triangle action, and the all-graph odd-cycle criterion. The remaining native obligation is to identify the actual directional comparison/incoming datum and test whether inverse traversal implements this reciprocal response. Covariance and the existence of a four-cycle do not select that law. Do not repeat the present transport/group proof as new research; any future contact-interleaved or field-dependent route-selection extension needs its own joint-state closure.
