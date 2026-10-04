# Dynamic field exchange and shared-memory Euler return: 35 versus 70

Status: PROVISIONAL MODEL THEOREMS AND EXACT BRC CERTIFICATES / NOT FORMALLY ADMITTED.
This is same-conversation authored continuation, not independent replication.
Global read snapshot: awdawmip/chatgpt-global-knowledge@f7abd42860a51586b9a7a9207e623d7dd651b0d6.
Source read snapshot: awdawmip/enterprise-math@c6315b96fcc3403bbfcc1363c2de3c768b0f7ae4.
Prior unit: research_notes/chatgpt_direct/20261005_LOCAL_GATE_SWITCH_13_CYCLE.md, blob c52391051e5bed0acd4ef652df785c4f9a921343.
Logical conversation: chatgpt-heartbeat-euler-20261004-layer-01, not platform-attested.

## Scope, types and executed reuse

The twelve ports n in Z/12 are the existing Cell/gate incidence labels, NOT X6 coordinates. G={1,3,5,7,9,11} are six gate sites; the six field bits below are internal data at these sites, not additional spatial axes. P000, six native spatial dimensions, separate time and three-dimensional slice typing are unchanged. Reversibility, a binary exchange law, multiple occupancy and the two-tracer alternation clock are explicit candidate assumptions, not derived native force or primitive triadic balance. Update count is not calibrated physical time. The conserved internal count Q is not positive BRC mass or energy.

The previous conversation archive euler_local_switch_evidence.zip was recovered and hashed: f0f71904d083a23ea75cd6c8468b9f28bf5c6e5ca3181d9feb171d2d25152600. All 21 entries of its recorded manifest matched. Unchanged brc_local_switch.py SHA256 dd76f8e750d6115f505ccb59b4babb87f93a908448aedf84f8e9d4639b59baf1 loads unchanged brc_autonomous.py SHA256 d8268e8723cd314ad28df1af51d0014ff48db7329035f4632b8867f8da421224 and its byte-pinned incidence/CWM adapter. Actual positive CWM source blob: 3f205696709e847909958a153f8fe10d3f6b70f0. The pinned incidence excerpt derives from euler_rotation_refinement.py blob 55e12f7ffb68a5b241f5d6323f5fde118de2716a. Existing CWM bodies and incidence successor are executed, not reimplemented as a numeric reference. REUSE_EXECUTED / EXTEND_EXISTING_TOOL; no new accepted family.

No pi expansion, classical trigonometry, numerical root, matrix exponential, Taylor/Padé/Cayley or non-BRC reference evolution was used. Positive path weights, root/choice identity, joint fields and audit histories are distinct from signed algebraic observers. This is new field work, not a retry of previously safety-blocked notes, journal payloads or verification sidecars.

## 1. Local conservative binary exchange

For two bits (b,f), a bijection preserving b+f must fix 00 and 11 and permute the two weight-one states. Exactly two maps qualify: identity and SWAP. Nontrivial exchange within this deliberately restricted class is therefore uniquely (b,f)->(f,b). This does not force all physical laws into this class.

A single tracer has state (n,b,f_1,f_3,f_5,f_7,f_9,f_11). At its current gate g exchange b with f_g; at a Cell leave both unchanged. Write c for the resulting mode and f' for the resulting field. Then stream by the existing incidence rule:

F(n,b,f)=(n+c mod12,c,f').

The inverse first sets n=m-c mod12 and then undoes the same SWAP at that port. Thus F is bijective, changes no remote field, and conserves Q=b+sum_g f_g. Each actual positive BRC weight is independently unchanged. Zero mode and all-zero field cannot produce motion in this model.

## 2. Exact Euler/field accounting

Keep alpha^4-alpha^2+1=0 and the previously chosen primitive twelfth-root embedding. For a positive joint population let A and B be the idle and moving phase sums, Z=A+B, and R=sum_paths w sum_g f_g alpha^g. Define

J=sum_paths w 1[n in G]*(f_n-b)*alpha^n.

Collision gives (A,B,R)->(A-J,B+J,R-J). In particular B+R is invariant DURING collision. Streaming then gives

Z_next=A+alpha*B+(alpha-1)*J,
B_next=alpha*(B+J), R_next=R-J.

These identities follow by actual serial/alternative BRC laws. J is a signed observer of local joint occupancy, not negative mass. It need not be determined by separate tracer and field marginals. The field has no autonomous inter-site transport here; this is not an energy or native-force identity.

## 3. Single-tracer invariant sectors: dynamic does not necessarily mean new feedback

A mode-zero tracer is fixed unless it is at a gate g with f_g=1. On the remaining active states define the background h as f when b=1, and as f with the current gate bit set to zero when b=0. Directly checking the SWAP cases proves h is constant on every active orbit.

For fixed h, a gate with h_g=1 is passed immediately. At a gate with h_g=0 the tracer deposits its mode, waits one update, then retrieves it and restores the field to zero. Projection to (n,b) is an exact conjugacy with the active cycle of the PREVIOUS static-switch model using M_h={g:h_g=0}. The inverse restores f=h on moving states and f_g=1 on the idle active-gate state. It is not just period matching.

Each of 64 backgrounds gives one cycle of length 18-|h|. The complete 1536-state system has 576 fixed states and cycle counts 1,6,15,20,15,6,1 at lengths 12,13,14,15,16,17,18. On an active orbit Q=1+|h|. Thus an isolated tracer's apparently dynamic field reduces to a static invariant background plus one temporary deposit. This limitation is retained rather than presented as a new self-organizing field theory.

## 4. Equal full marginals and current zero phase, different future

Let e_g denote a field with its sole one at gate g. Compare positive preparations with two alternatives of weight 1/2, all initial tracer modes zero:

P: (n=1,f=e_1), (n=7,f=e_5).
P':(n=1,f=e_5), (n=7,f=e_1).

Their complete tracer marginals match, their complete six-bit field marginals match, and CWM=(2,1,1/2) and Q=1 branchwise match. Both have initial phase (alpha+alpha^7)/2=0. In P the first tracer acquires the local bit and moves to 2, while the other remains at 7. In P' neither tracer encounters the bit and both states are fixed. Hence

Z_1(P)=(alpha^2-alpha)/2 != 0; Z_k(P')=0 for all k.

The active alternative of P is in the 18-cycle with empty background. This is a positive classical joint-correlation witness, not quantum entanglement. Factoring the two marginals loses the deciding relation. More generally, equal tracer states cannot be affected by field differences until contact with a differing gate: an induction on the local rule proves the statement. This is incidence-graph locality, not a measured X6 signal speed.

## 5. Two tracers share ONE field

A complete two-tracer state is (n_A,n_B,b_A,b_B,f,tau), tau in {A,B}. At each micro-update the indicated tracer exchanges its mode with its current gate field and streams; the other tracer is unchanged; then tau flips. Inversion reverses tau, stream and collision. Q=b_A+b_B+sum f_g is conserved.

The Q=1 sector has exactly 12^2*8*2=2304 states: the unit is in A, B or one of six field sites. This is a closed carrier, not a minimality claim for phase-only observers. A BRC alternative carries the whole world and one shared field; it is incorrect to give the two physical tracers independent field copies.

With both tracers at gate g, initial modes (1,0), empty field and A's turn, the local mode/field triple obeys

(1,0,0) --A--> (0,0,1) --B--> (0,1,0).

After the first micro-update both remain at g. After the second, B is at g+1 with mode1 and A remains idle at g. Another object has read the deposit before its original owner could retrieve it. The prescribed order matters; reversing the scheduler changes the result. The rule does not claim simultaneous-collision or native occupancy physics.

## 6. Complete two-tracer Q=1 cycle theorem

All 2304 states form 726 cycles of length2, 12 cycles of length36, and 6 cycles of length70.

If the field unit is at a gate occupied by neither tracer, both modes stay zero and only tau alternates. The number of choices is 144*6-72-72+6=726.

Otherwise a tracer can acquire or carries the unit. If the other idle tracer is at an even Cell port, it never accesses a gate field. The moving tracer follows an 18-own-update loop, interleaved with the idle tracer's turns: one 36-cycle for each of 2 moving identities and 6 stationary Cell ports, totalling12.

If the idle tracer is at an odd gate g, the moving tracer hands the unit to it whenever it returns. This common gate anchor stays fixed. Start from s_g=(g,g,1,0,zero-field,A-turn). A deposits at update1; B receives and advances at update2. B makes 12 forward moves and five other-gate dwells in 17 of its turns, reaching g again at update34. Update35 is A's idle hold. Therefore F^35(s_g)=R(s_g), where R swaps tracer labels AND the scheduler bit. The rule commutes with R, so F^70(s_g)=s_g. Restoring the original labelled mode requires two complete excursions, and no earlier full return occurs. There is exactly one such cycle at each of six anchor gates.

The cases exhaust the sector, and 726*2+12*36+6*70=2304.

## 7. An Euler circle with period35 above a labelled period70

For the declared symmetric phase observer Z=(alpha^(n_A)+alpha^(n_B))/2, one tracer stays at anchor g on a 70-cycle. Writing m for the other position gives

Z=(alpha^g+alpha^m)/2,
Z-alpha^g/2=alpha^m/2.

The external readout therefore stays on the same circle centered at alpha^g/2 of radius1/2, with twelve geometric positions and a nonuniform update schedule. No native plane or seventieth-root spatial phase is introduced.

Since F^35=R on this orbit and Z is label-symmetric, Z_(t+35)=Z_t while the full labelled state needs70. The phase period is exactly35: within a canonical 35-block Z=alpha^g occurs exactly three times, at indices0,1,34. A smaller period would divide35 and force this count to be divisible by5 or7. Exact traces verify this for every anchor.

The difference between a state and its label-exchanged partner is invisible for every future symmetric phase observation because F commutes with R. A label-sensitive observer distinguishes it. Thus genuine field-mediated transfer still leaves observer-dependent hidden information. This is not quantum entanglement.

## 8. Executed validation and reproducibility

FieldPath extends the unchanged source-backed ModePath with fields. Collision executes the old positive BRC move core, and stream executes the unchanged advance function. PairWorld uses one positive CWM per JOINT alternative; every event invokes actual cwm_edge/cwm_propagate and the existing incidence successor. Root/choice/history survive. Alternative summaries call cwm_recoalesce. A histogram over the FULL joint state is future-sufficient for the declared history-blind operations by determinism and CWM distributivity; the product of marginals is not. The implemented single-tracer joint CWM quotient was checked against explicit paths through20 updates. No fixed-bit or general algorithmic speedup is claimed.

Final new suite: 42,047 assertions, including21 dependency-manifest checks; all1536 single-tracer states; inverse, count conservation, locality, phase/field flux, CWM and provenance; all64 active background conjugacies; equal-marginal echo; all2304 two-tracer Q=1 states; complete cycle classification; all2304 label-exchange covariance cases; exact35/70 return and phase minimality at six anchors. Existing CWM calls: cwm_edge25192, cwm_propagate20336, cwm_recoalesce6895. Incidence successor3121. Checks/calls are not independent experiments.

An earlier37,288-check development stage preceded the35/70 theorem and new checks. It is retained, not counted as a second replication. The first shell redirection failed because its log directory did not yet exist, before Python ran; that administrative launch error was corrected. Prior research suites were not replayed.

Full conversation NOTE.md:16504 bytes, SHA256 c2362799b7a03dfdb6442bc98b88301a30afcc63db22f0f5d1d37c2cb4f62891.
New brc_dynamic_field.py:7785 bytes, SHA256 a848479916af2ef92dc239bde0eafe0dc7b0ba2fd22a2761c9f9e4c0cb358dc8.
New check_dynamic_field.py:11455 bytes, SHA256 f09ab353790a2a4d69d6c056b772246307bb3d965dd7562cc3ab61f45db6bcec.
Final evidence/summary.json:421580 bytes, SHA256 b5089bb69a7a8275f11adad7bc4d16dc65f05f19711643a76e5d6c7057e0f2f4.
Run python check_dynamic_field.py in the conversation archive using standard-library Python3.10+. This Source note preserves the proof and validation frontier; it does not assert that all complete execution bytes were uploaded to Source or independently admitted.

## 9. Boundaries and next scientific unit

General prior art: Fredkin and Toffoli, Conservative logic, Int.J.Theor.Phys.21,219-253(1982), DOI10.1007/BF01857727; Margolus, Finite-State Classical Mechanics, arXiv:1807.04437. Primary-source abstracts were read for attribution only. The general reversible/conservative design principle is not a new discovery. No literature-wide novelty, physical equivalence, native field origin, primitive force, calibrated time/distance/energy or quantum mechanism is claimed.

New unit completed: a local dynamic field contract, exact conservation/inverse, single-tracer reduction, positive joint-correlation witness, two-tracer transfer, full Q=1 cycle classification and35/70 observer/state-return distinction. Next: a native-authorized occupancy and collision rule supporting symmetric simultaneous interaction without inserting the present alternation clock, with the same joint-state and conservation obligations. Additional units or field transport remain model extensions not executed here.

Current control is unresolved, not absent: status#2739 exposes service-local session MCP-74124c48a87440a6b56f5f440f7e9493 linked to earlier failed registration session-20261005-euler-local-switch-12. Its Source record at current pinned head returned404. Targeted reconcile#2740 returned NOT_RECONCILABLE. Source-bound registration/activity remains UNVERIFIED/REGISTER_PENDING. No old identity, CLAIM, formal run, independent approval or successful final gate is borrowed. Earlier blocked publications and activity sidecars were not retried. This source note is scientific continuity, not formal admission.
