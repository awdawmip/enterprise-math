# Euler sector conservation: arbitrary paths, mobile carriers and a shared-field readout

Status: PROVISIONAL MODEL THEOREMS AND EXACT TYPED-BRC CERTIFICATES.
Date: 2026-10-09 (Asia/Tokyo). Same-conversation continuation, not independent replication.
Global read snapshot: b818f2b256acdfe4bf0a568020adb460361fd09c.
Source read snapshot: 3d45d737420e57008d24e87da283c4d41ba8594f.
Prior frontier: d2bd8c1edff31fa3c6a37fe3bd40edd9a9740462, research_notes/chatgpt_direct/20261009_EULER_MULTICYCLE_CONDITIONAL_OBSERVER.md, blob 8ac5d08d471771cb2263475fe9787a79c8576465.
Logical conversation: chatgpt-heartbeat-euler-20261004-layer-01; not platform-attested.
Current local activity: RA-347DF236B3CD57BBC455B432; researcher handle EM-DIRECT-9C64E4. These are bookkeeping, not a task CLAIM or mathematical admission.

## 1. Objective, operations and actual reuse

The previous three-loop result preserves eta2=F2+F1 and eta3=F3+F1. This unit determines whether that is an artifact of selecting three triangles. It admits arbitrary prescribed edge paths, the existing field-neutral contacts, state-dependent choices of the same edges, and explicitly scheduled coexisting carriers sharing the same field. The local reciprocal read/toggle rule is unchanged. The new result proves a conservation law for this entire action family and exhibits subsystem sector transfer using that law.

Use source edge order 01,02,03,12,13,23, arrow bits (0,1,0,0,0,0), and rooted triangles 0120,0130,0230. On a chosen directed edge a, the carried sheet bit updates by s'=s+e_a+d_a and the edge record by e'_a=e_a+1, over F2; d_a indicates traversal against its declared arrow. These are the existing sourced BRC operations, not a new propagation law. Contacts change the three-channel record but not the field or comparison position. The formulas below do not assume that an action-selection policy is independent of the field, sheet or past history.

The K4 vertices are comparison contexts, not native X6 positions. Bit incidence, cycle rank, occupancy parity and the label called Q below are relation data, not spatial axes, charge, force, energy or calibrated heartbeat time. The two coexisting carriers are not two alternative BRC branches or a claim of primitive two-force balance. Their scheduling is a declared sequential control, not a derived simultaneous interaction.

The prior ZIP SHA256 is 163914e0aa236d95800ead742eeef60901e1639fad0c1c4b21bfdf1f30d17114. All 31 manifest entries were checked. Seventeen Python dependency modules were copied unchanged; no preceding scientific checker was run. The new adapter imports brc_multicycle and actually calls its existing reciprocal transport, contact, phase and CWM operations. A shared world has ONE edge field and ONE positive branch weight; selecting one carrier updates that field for every carrier. The other carrier is not given an independent copy of the field.

Current full brc_weighted.py remains Git blob 3f205696709e847909958a153f8fe10d3f6b70f0; bundled full bytes match. The executed source chirality excerpt remains tied to full-module blob 6f8b147c094720c2749f620a40394c4d7b67a386. Graph incidence and F2 computations are certificates of executed BRC rows, not an alternative world propagator. No numerical pi, trigonometry, roots or matrix exponential is executed.

## 2. The two old sector bits survive EVERY closed path

Write c1,c2,c3 for the three binary triangle edge masks. Then
c1+c2=(0,1,1,1,1,0),
c1+c3=(1,0,1,1,0,1).
The first is the cut between {0,1} and {2,3}; the second is the cut between {0,2} and {1,3}. Let their vertex potentials, anchored to zero at vertex0, be
h2=(0,0,1,1), h3=(0,1,0,1).
Thus c1+ci=delta hi, where (delta h)(u,v)=h(u)+h(v).

For ANY path from v to w, let p_a be the parity of its number of uses of edge a. Directions affect the sheet update, but not whether the edge is toggled. The field changes by p. Its boundary is partial p=1_v+1_w. Consequently
eta_i(final)+eta_i(initial)
=(c1+ci).p=(delta hi).p=hi(v)+hi(w).

In particular eta2 and eta3 are unchanged on every closed path. Intermediate contacts do not affect this equation because they do not change the field or position. It also holds path by path under arbitrary feedback choices among the same edge/contact operations, and therefore under normalized positive BRC mixtures. Adding a square, the fourth triangle, repeated edges, longer routes, or an incoming-memory controller cannot change these sectors at a return. This is a theorem under the fixed local rule, not a restriction on researching other rules.

For an open path define the vertex code
q(0)=(0,0), q(1)=(0,1), q(2)=(1,0), q(3)=(1,1).
The complete local relation is
eta(final)+eta(initial)=q(v)+q(w).
Therefore the dressed pair Q=eta(e)+q(current) is constant on every step. This repairs the apparent sector changes observed while a carrier is away from its base. Q is an exact bit invariant, not a physical electric charge.

## 3. Several carriers: conservation belongs to the joint system

Let n_v be the parity of the number of coexisting carriers at vertex v in ONE complete world. This is computed from actual integer occupancy before any average over alternative worlds. Define
D=partial e+n.
When a carrier traverses edge a, e changes by 1_a and n changes by partial 1_a. Hence D'=D. A contact leaves both unchanged. Any sequential schedule of any number of such carriers preserves D, even if selection depends on the full current state.

Under a change of local frame g, e becomes e+delta g. Thus D changes by Delta g, where Delta=partial delta is the graph Laplacian over F2. D itself is a raw-frame record. If h satisfies Delta h=0, however,
Q_h=h.D=(delta h).e+h.n
is gauge invariant and is conserved. If frames change between stages with identification tau, the covariant field rule is e'=e+J+delta tau and n'=n+partial J, so D'=D+Delta tau; the same Q_h remains conserved.

For K4, Delta is the all-ones 4x4 binary matrix. Its kernel consists of the even-weight vertex potentials. Modulo the constant potential there are two independent choices, h2 and h3 above. Up to the fixed arrow offsets, their conserved values are exactly
Q_total=eta(e)+sum_carriers q(position).
Thus another carrier may change the field sector seen by a fixed probe, while its own change of endpoint supplies the compensating label. If the total vertex occupancy parity returns, the field sectors return as well. Individual carrier names need not return for this statement; it concerns occupancy parity.

This gives a source diagnostic. For arbitrary recorded field and occupancy changes, put B=partial(delta e)+delta n. Then delta Q_h=h.B. Under the stated local rule B=0 in a common frame. An independently imposed edge edit, carrier creation/removal, reset or a different local law can give a nonzero value. A changed coarse readout alone does not establish which source occurred.

## 4. Exact shared-field write/read/erase witness

Use the existing field tuple with F1=F2=F3=0: in the declared edge order its raw records are (0,0,0,0,1,0). A probe and a writer both start at base0, each with channel triple (0,0,1) and positive sheet. The complete world has one BRC branch of weight1, not two alternative branches.

The writer traverses 0->3 using the OLD reciprocal edge rule. Now F=(0,1,1), eta=(1,1), while the probe remains at0. The writer's vertex code becomes (1,1), so Q_total is still (0,0). The probe's channel, sheet and first-triangle F1 are unchanged: even its previous single-loop four-moment record is identical before and after this write.

Reuse the previous selector witness. Let V be chronological U2,U1^-1 and apply to the probe
W: V,C,V^-1,C^-1.
The preceding theorem proves, and the present actual joint execution checks, that W is identity on channels when eta2=0 and acts as C when eta2=1; its complete raw field and probe sheet are restored. C^-1 is still TWO actual old contacts.

Without the writer excursion, the probe output is omega^2=-alpha^2. With the write it is 1. Finally send the writer back 3->0. This is the genuine inverse of its edge traversal. All field records, both comparison positions and both sheets return to the initial values; the writer's channel also returns unchanged. The probe retains channel (1,0,0) and phase1. Q_total stayed (0,0) throughout.

This is a controlled write/read/erase composition, not spontaneous scheduling, a nondisturbing measurement of the full state or spatial nonlocality. The probe was deliberately changed, incoming records and audit history remain, and the comparison graph has not been calibrated as native space. The result shows how a subsystem sector can be accessed through a shared field without violating the joint conservation law or inventing an independent field-flip operation.

## 5. General graph theorem: the protected field labels are bicycles

Let G be any finite connected simple graph with the same read/toggle field update. Work over F2 with edge space E and vertex space V. Let
C=ker partial (cycle space),
B=im delta (cut space),
R=C intersect B (bicycle space).
The terminology and the relation to based conservative vertex colorings are established graph theory; the correspondence to this BRC field update is proved here.

A linear field label r.e is insensitive to all local frame changes iff r is orthogonal to B, equivalently r in C. It is preserved by every closed transport iff r is orthogonal to C, equivalently r in B. Therefore the frame-independent linear labels preserved by ALL closed transports are exactly r in R.

This is also a COMPLETE classification of arbitrary field-sector labels, not just a list of linear examples. A closed transport adds an element of C, and every binary cycle mask can be realised by a based closed walk: connect its constituent cycles to the base using out-and-back paths. A frame change adds an element of B. Thus the equivalence classes are the cosets of C+B in E. Since (C+B)^perp=R, a basis of R separates all such classes. If nu=dim R, there are exactly 2^nu classes. This counts field classes after identifying frame notation; it does not count every labelled field/sheet/channel state or every control history.

Let b=|E|-|V|+1, choose a binary cycle basis c1,...,cb, and put H_ij=ci.cj. The radical of this pairing is R, so
nu=b-rank_F2(H).
Also delta maps ker Delta onto R with kernel consisting of constant vertex potentials. Hence
nu=dim ker_F2(Delta)-1.
Every r in R has r=delta h with Delta h=0. Its mobile extension is r.e+h.n, exactly the conserved joint quantity in section3. These equations are incidence/transport identities, not continuum field equations.

Examples:
- a tree: b=0, nu=0, one frame-independent field sector;
- one triangle: b=1, nu=0, one sector;
- one square: b=1, nu=1, two sectors;
- K4: b=3, H is the all-ones 3x3 matrix, nu=2, four sectors.
The old odd-cycle theorem is a DIFFERENT invariant: triangles support fourth-order sheet return, while squares do not. Here squares protect a field label, while triangles alone do not. Therefore the source of an i-type joint cycle and the source of conserved field-sector labels are not interchangeable. Neither changes P000's native space or identifies an odd graph cycle with primitive triadic force balance.

## 6. What this proves about disappearance and prediction

For the same closed local operations, longer paths and more complicated field-dependent routing do not mix the four K4 field sectors. Each positive branch stays in its sector when its carrier returns, and sector mass is conserved in a normalized full output. It is still possible for a channel phase to vanish, because a phase average does not equal sector mass. Open transport exchanges the field label with endpoint data; it is not automatic destruction of the label.

Q_total is a conservation certificate, NOT by itself a complete predictor. The write witness has the same total label and the same probe single-loop moments before and after writing, yet later probe outputs differ. Predicting such shared-field controls needs the relevant joint environment/position information, not only the conserved values. The previous 4/8/16 conditional observer theorem remains valid in its stated closed-control domain. A moving carrier/controller must be included or newly proved reducible.

A source supported on one K4 edge has sector syndrome q(u)+q(v): edges01/23 give(0,1),02/13 give(1,0),03/12 give(1,1). A legitimate carrier traversal supplies precisely the matching endpoint term. An unrecorded field-only reset does not. This is a useful distinction between representation loss and an actual change of the local rule; it is not an empirical claim of charge creation.

## 7. Exact execution and remaining native question

Final checker: 40,750 assertions, including19 dependency/source integrity checks. A separate build audit verified all31 prior manifest entries. It covers all64 raw K4 fields, both sheets, all directed edges, frame and cross-stage changes; 1,093 arbitrary prescribed prefixes including274 closed prefixes; four field-dependent positive NB policies through8 edges; all43 connected labelled simple graphs on2,3,4 vertices with complete bicycle/cut/cycle orbit checks and actual old BRC loop/open-edge rows; all64 fields and all16 two-carrier position pairs under each carrier's available step; and the complete write/read/erase witness. Larger graphs are covered by proof, not unperformed execution.

The field-dependent NB test uses probabilities1/3 and2/3 whose assignment depends on the current field. At each level all branches preserve the same corrected label and have CWM=(2^n,1,(2/3)^n). These are actual positive branch updates. Shared-world tests keep one global CWM weight, not the product of independent carrier populations.

The first full check completed its assertions but failed while reporting a nonexistent counter attribute. Reporting was corrected to the existing source_call function's actual COUNTS dictionary. The final40,750 check includes one stronger old-observer comparison added after a40,749 development pass; these runs are not independent replication. Logs preserve the reporting defect. No old scientific suite was rerun.

Run python -S check_sector_charges.py with standard-library Python3.10+. The package contains seventeen unchanged dependencies, new joint-state adapter/checker, graph certificates, the complete witness, logs and hashes. The source manuscript stores the proof/frontier; executable package publication is stated separately.

Primary background: Lamey, Silver and Williams, Vertex-Colored Graphs, Bicycle Spaces and Mahler Measure, arXiv:1408.6570v3 (official abstract checked), identifies based conservative colorings with bicycle space. We supply the finite incidence proofs above; this citation is not evidence that its authors studied the present BRC law or physical Heartbeat World.

The current activity uses a locally assigned continuation key and researcher handle under the source connector-only metadata protocol, not a ChatGPT server session or a clean independent context. Previous service-session failures and contribution provenance are not erased; no privileged service operation is rerouted or claimed successful. Activity/checkpoint publication does not grant a formal Task, CLAIM, Working Truth or mathematical acceptance.

Completed increment: all-path sector conservation, mobile and multi-carrier compensation, general bicycle classification, and actual shared-field write/read/erase. The remaining native obligation is to identify the actual incoming carriers, their comparison incidence and local scheduling, and determine whether their complete update has the proved matched field/endpoint change. The current theorem gives a testable condition; it does not derive that native correspondence by naming a conserved bit. A useful next unit is a minimal joint observer for moving-writer controls rather than repeating the old closed-loop classification.
