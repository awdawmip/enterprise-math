# Euler comparison transport with local edge backreaction

Status: PROVISIONAL MODEL THEOREMS AND EXACT TYPED-BRC CERTIFICATES; NOT FORMALLY ADMITTED.
Date: 2026-10-09 (Asia/Tokyo). Same-conversation continuation, not independent replication.
Global read snapshot: 9944ec5937a4024fbdad0c6de6d3f0bd6f33e5f0.
Source read snapshot: 2a563624c36515fdf38f93a7b78b62833c93ea6a.
Prior frontier: a9f23108d24e5f852e15863220a4e991bda989ca, research_notes/chatgpt_direct/20261008_EULER_CHANGING_FIELD_TEMPORAL_GLUE.md, blob 58f8e50fb50ad24e0bc8b73b1c6640c1f8723d2c.
Logical conversation: chatgpt-heartbeat-euler-20261004-layer-01; not platform-attested.
Research activity: UNVERIFIED / REGISTER_PENDING. No borrowed identity, CLAIM or mathematical acceptance.

## 1. Scope and executed reuse

The preceding unit allowed externally specified changing comparison fields and supplied their necessary cross-stage identification. This unit replaces a preselected pulse by a declared local feedback: read a traversed edge's current comparison bit, then toggle that edge. It proves the consequences and the limitation of that rule. It does NOT derive the rule from native forces, nor assert it is the unique physical feedback mechanism.

K4 vertices are sourced comparison contexts, not native X6 positions. Edge records, carried sheets, relative reference sheets, traversal counts, and channel triples are typed internal data. No spatial dimension, native 90-degree right angle, physical heartbeat interval, energy or quantum spin is introduced. P000 and the residual-fidelity contract are unchanged.

Previous archive SHA256: 7ffa695543abf0e5f7cf974c41e4685365b9a9b7e0a809a72be3e1603aaf83df; all 22 prior manifest entries verified. The unchanged brc_changing_field.py is SHA256 21f41dbdf594012130a6dc20712c9a847166861cda922f2052e9ee4321578658. The new extension imports it and its existing dependency chain. Prescribed edges execute its transport function with zero temporal link; equal nonbacktracking alternatives execute the unchanged brc_first_return.edge_children. Every spatial comparison uses the existing source transition_bit, every positive path uses existing CWM edge/serial/merge, and contact uses the unchanged brc_route_memory.contact. Only the post-read field toggle is new. Complete histories, source roots, channel data, positive weight and incoming neighbours are retained on explicit paths.

Current full brc_weighted.py blob: 3f205696709e847909958a153f8fe10d3f6b70f0; actual bundled bytes match. Current euler_fcc_chirality.py full blob: 6f8b147c094720c2749f620a40394c4d7b67a386; its already inspected dependency-closed excerpt is reused, not called the entire source module. The previous note remains unchanged at current source.

REUSE_EXECUTED / COMPOSE_APPLIED / EXTEND_EXISTING_TOOL. No new accepted BRC family. No pi, numerical trigonometry, numerical roots, matrix exponential, or alternate numerical world propagator. Bit/group/count formulas below certify actual sourced BRC transitions, not signed replacements for positive mass.

## 2. The smallest covariant local carrier strongly restricts feedback

Use two binary inputs: carried sheet s at the edge's departure vertex v, and comparison bit e on the undirected edge {v,w}. A static frame change at endpoints (g_v,g_w) sends input to (s+g_v,e+g_v+g_w), where addition in this note's bit formulas is XOR. An output (s',e') must transform to (s'+g_w,e'+g_v+g_w).

Assume a deterministic update with no further local data and no distinguished direction on the undirected edge. Equivariance forces exactly

s' = s+e+c,   e' = e+d,    c,d in F2.

Proof: the endpoint frame group acts transitively on the four inputs. The image of (0,0), say (c,d), determines all other images by taking g_v=s and g_w=s+e. All four resulting maps are bijective. Exhaustion of all 256 binary-input/binary-output functions confirms this classification. It is not merely a search over guessed reversible maps.

If an edge with e=0 is required to transmit the carried sheet unchanged, then c=0. Two rules remain: d=0 (the old static transport), or d=1 (read and toggle). Thus read-and-toggle is the only nonstatic option under THESE minimal interface and covariance assumptions. A richer field, directed incidence, delayed response or source-dependent law is outside this classification.

Choose the d=1 candidate:

(s,e) -> (s+e,e+1).

Its true inverse is (s',e')->(s'+e'+1,e'+1). Applying the SAME forward law while traversing back instead gives (s+1,e), not the identity. Four same-law uses restore both bits. Therefore local invertibility must not be conflated with automatic undoing by spatial retracing. Requiring both same-law retracing to be identity and this undirected two-bit covariance forces d=0; additional directional data can change that conclusion.

The two-bit integer r=2s+e satisfies r' = r+1 mod4. For the existing alpha ring alpha^4-alpha^2+1=0, put beta=alpha^3, so beta^2=-1. The declared readout beta^r updates by multiplication by beta. This is a finite algebraic representation, not a native spatial quarter-turn or a unique physical origin of i.

## 3. Local source of the previous mixed comparison parity

In a common temporal frame, traversing edge a at stage t reads e_t(a) and sets e_(t+1)=e_t+1_a. Other edge records do not change. Thus the preceding unit's mixed rectangle parity is now generated by the path itself:

Omega_t(a)=1 if a was just traversed, and 0 otherwise.

In arbitrary cross-stage frames with temporal bits tau_t(v), the covariant same law is

e_(t+1)(v,w)=e_t(v,w)+J_t(v,w)+tau_t(v)+tau_t(w),
s_(t+1)=s_t+e_t(v_t,v_(t+1))+tau_t(v_(t+1)),

where J_t indicates the traversed edge. Consequently Omega_t=J_t, independently of frame notation. This closes the local field update conditional on a selected edge; it does not derive the edge-selection grammar or temporal calibration.

For a triangular face f, let phi_t(f) be its spatial loop parity. Then

phi_(t+1)(f)+phi_t(f) = sum_(a in boundary f) J_t(a).

A single edge toggle changes exactly the two incident triangle parities. The XOR of all four K4 face parities stays zero. Thus in this candidate representation an isolated one-face change is not a legal output of the local edge update. This is a combinatorial consistency law, not an energy conservation or primitive force-balance theorem.

## 4. Exact transport memory for any path

Suppose edge a has been used n_a times during a transport segment, without an intervening sheet reset. On its successive uses the bits read are e_0(a), e_0(a)+1, e_0(a), ... . Summing them gives

e_T(a)=e_0(a)+(n_a mod2),
s_T+s_0 = sum_a n_a e_0(a) + sum_a binom(n_a,2)  (mod2).

The second term is a feedback contribution. A static-field holonomy would omit it.

Define p_a=n_a mod2 and q=sum_a binom(n_a,2) mod2. The endpoint transport action is

G_(p,q): (e,s) -> (e+p, s+e.p+q).

Equivalently q=(L-|p|)/2 mod2, where L=sum n_a and |p| is the number of odd traversal counts. This integer quotient is valid because L and |p| have equal parity.

If the final field is exactly the initial field, then p=0. Nevertheless

s_T+s_0=L/2 mod2.

Hence any closed path using every edge an even number of times and having L=2 mod4 restores the field but reverses the sheet. Two repetitions of the NB triangle 0,1,2,0 give L=6 and this effect for EVERY initial field. Four repetitions restore the sheet. A fixed-base temporal reference makes the returned-sheet comparison invariant under frame changes.

Composition has the explicit feedback term

(p,q) followed by (r,k) = (p+r, q+k+p.r).

This particular pure-transport action law is commutative; it is NOT the previously studied noncommutative contact-plus-transport law. For a closed K4 path, p has even incidence at every vertex. The cycle space has eight masks (empty, four triangles, three squares), and q has two values: sixteen endpoint transport actions. All sixteen were reached by genuine NB paths from a fixed base and incoming port. A finite exploration has 192 reachable (field,sheet,incoming,current) cores from the chosen flat seed. Distinct actions already produce distinct (field,sheet) outputs on the zero-field positive-sheet probe, so sixteen is minimal for THIS raw labelled action-output contract.

The pure-transport group is isomorphic to C4 x C2 x C2: take three independent triangular cycle generators; their squares are the same central sheet flip, and ratios with one generator have order two. This is a standard finite group structure, not a new general group discovery. Gauge-insensitive or phase-only observers may admit further quotients. Source/path-sensitive interventions or collisions inside a segment invalidate replacement by this endpoint transport summary unless separately proved.

## 5. A gauge-relative four-cycle around an actual triangle

Fix a simple comparison triangle and repeat it without resetting the field. Let f be its INITIAL face parity at the beginning of a lap. Each of the three edges is read once before toggling, so the returned sheet changes by f; toggling all three edges changes the next face parity by one.

Let s_rel compare the carried sheet to a retained base reference, with its temporal identification recorded. One lap induces

(s_rel,f) -> (s_rel+f,f+1).

Both f and the closed sheet comparison are invariant under changes of frame notation. Thus this is not only the frame-dependent single-edge counter of section2. With r=2s_rel+f, the relative algebraic readout w=beta^r satisfies

w_next=beta*w, beta^2=-1.

From (0,0) the states are
(0,0)->(0,1)->(1,0)->(1,1)->(0,0),
and readouts are
1,beta,-1,-beta,1.

After two laps the entire edge field has returned, but the relative sheet has not. This is a specific joint-state realization of a four-step Euler readout; it does not change the project's native 120-degree orthogonality.

Add the existing collision P^chi BEFORE each lap, leaving the field feedback unchanged. Starting from a field-channel unit and fair initial carried signs in a zero comparison field, the laboratory channel phase factors at completed laps are

1,-1/2,-1/2,-1/2,1,...

For every binary triple, both signs and all 64 initial fields, four such triangle laps return channels, sheet and labelled field. This is a joint endpoint return, not a return of elapsed time or audit history.

For a simple square in a zero field, the sheet stays unchanged on each lap, channel rotation has period three and raw edge-field bits have period two; six laps restore all labelled data. Three laps already restore the laboratory channel phase. The six-lap assertion concerns raw labelled field records; a coarser gauge-insensitive observer can identify more states. These prescribed-loop experiments test the same local update, not a claimed spontaneous preference for triangle or square trajectories.

## 6. Forward first-return law with an evolving field

Now choose each allowed NB next edge with fresh equal weight1/2, preserving the true incoming neighbour at every step. The path-selection law is the prior candidate NB rule; the field is no longer fixed and is not reset at a return. Each chosen edge reads the existing source bit before toggling it.

The first-return length law and mean are unchanged:

Pr(L=l)=2^(-(l-2)), l>=3; E[L]=4.

The returned field, sheet and incoming port MUST remain joint. Write B_l(i;j,h,p) for their length-resolved total mass, with p the final field change. The four surviving internal path skeletons repeat their internal directed triangle after three nonreturns. Adding six edges visits each internal edge twice. Therefore p and j are unchanged but q changes by three, reversing h:

B_(l+6)(i;j,h,p)=B_l(i;j,h+1,p)/64.

After twelve edges the same joint event recurs with weight1/4096. Thus lengths3..14, multiplied by4096/4095, give an exact infinite MASS closure. At cutoff20 the unreturned mass is2^-18. Infinite path count is not encoded as a finite CWM count; the closure preserves the specified mass interface, not original infinite multiplicities or maximum individual-path weights.

For a zero initial field, all closed K4 parity masks have sizes0,3,4. Section4 therefore implies

h=floor((L+1)/2) mod2.

Even transport parity occurs at L=0 or3 mod4. Summing the genuine return-length masses gives

p_even(zero initial field, read-toggle)=4/5.

For all-negative initial edges, the extra initial contribution is L mod2, so even transport occurs at L=0 or1 mod4 and

p_even(all-negative initial field, read-toggle)=2/5.

For comparison, the already-proved STATIC NB laws at those same initial fields give1 and1/3. The difference is endogenous field modification in this declared candidate, not a selected target persistence. After one return the actual field has generally changed, so repeatedly substituting either4/5 or2/5 into a constant-rate model is NOT authorized. The implementation retains the complete returned field/port/sheet and provides a joint mass-only macro adapter.

All 64 fields and all three true incoming ports were checked. The period-six sign reversal and the normalized mass closure are exact BRC certificates, not an extrapolation from an empirical return histogram.

## 7. Evidence and limitations

Final new checker: 58,138 exact assertions, including22 prior manifest assertions and one current CWM blob comparison. Coverage includes all256 local binary laws; all64 fields; both sheets and all six local undirected edges; static and independent cross-stage frame changes; every actual binary NB branch through nine edges for the transport identity; all16 closed residues and their256 products against every field; all1024 field/triple/sign probes for double triangle transport and four-contact return; joint first-return certificates for192 field/incoming cases through length20; full-state CWM versus explicit paths through eight edges; 512 recorded inverse-channel recoveries; and the gauge-relative triangle counter and beta observer.

Actual unchanged CWM calls: edge150441, propagate134290, recoalesce4478.
Actual old contact calls:4820.
Actual source calls: transition_bit99164, face_holonomy3072, gauge_action59392.
These are checks and function calls, not independent experiments or replication. Many checks are finite algebraic and gauge certificates.

New adapter SHA256: 5b310a371c99c92f19a8e1136310a4361b388ad2d1ec78ecc48320f219e2e68c.
New checker SHA256: 5a385cc12a2c4cf44055de575af55a92ce2b4617659daba2555c56bfee877fe9.
Final summary SHA256: 5e7b433c42482fb657330f875c2a5901c976d652c4a40b4d1794f51392bbea87.

A container invocation was unavailable; actual local execution used the available Python runtime without network access. An initial attempt to read an unextracted dependency found only the mounted note; the supplied archive was then safely extracted. The first complete checker reached reporting but failed on a wrong counter-module attribute; the reporting access was corrected to the existing function's globals. The preliminary58k-scale stage and final added triangle-observer checks are development/revalidation, not separate replication. The final standalone command is python -S check_edge_backreaction.py, Python3.10+ standard library. No prior scientific suite was rerun. A nonresearch startup warning is retained in the first log.

Literature scope: the official arXiv abstracts of Webb and Cohen, Self-Avoiding Modes of Motion in a Deterministic Lorentz Lattice Gas, arXiv:1404.3629, and Kumar and Mishra, Dynamics of particle moving in one dimensional Lorentz lattice gas, arXiv:1902.01037, establish prior context for scatterers changed by the paths that visit them. Their physical lattices and laws are not imported. No unread theorem or literature-wide novelty claim supplies the present finite proofs.

Own bounded control status request: bridge issue3506, status-20261009-euler-edge-backreaction-24. This manuscript does not infer activity authority from a status transport. Prior registration remains unverified; no old rejected registration, role, CLAIM, independent review or successful final guard is asserted. Scientific persistence is not mathematical admission.

Completed increment: constrained local binary feedback; generated mixed comparison change; exact quadratic traversal residue; gauge-relative four-state Euler observer; first-return joint sign/field kernel and derived4/5,2/5 weights. The remaining native obligation is to establish whether actual incoming relations realize this edge feedback or a richer rule, including the physical meaning of reversing an interaction. Merely matching covariance, a cycle length or an Euler readout does not derive a force law.
