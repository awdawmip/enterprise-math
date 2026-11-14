# R675｜共享 Cell 双环 X6 模型的类型化半周交换协变与作用刚性

Status: AUTHOR-SIDE EXACT SYMBOLIC PROOF / DRIVER UNREVIEWED
Date: 2026-11-10 (Asia/Shanghai)
Parent Task: RS-X6-GLOBAL-TRIADIC-FIELD-NETWORK-LAW
Researcher-ID: EM-X6-0AE6CE
Research-Activity-ID: RA-6EDF1FA3D29E7A06B9855639
Frozen scientific frontier: R462 @ 18783e01e3646c72b7aab3b16d3f565e83e6446f
Predecessor: R674 @ 7e85d3b0fe3543e28c91894c174090102babb6db

## 1. Exact model and observer

Keep the R674 seven-Cell, eight-oriented-edge graph inside the full signed six-axis X6 affine Cell torsor. A chosen Cell o is a **relative chart anchor** (no global origin). Let E1,...,E6 be the six native coordinate steps, with the other axes retained even when the finite subgraph does not use them.

C_A: o → o+E1 → o+E1+E2 → o+E2 → o.
C_B: o → o+E3 → o+E3+E4 → o+E4 → o.

At each Cell x, keep the complete nonnegative V29 ledger L_x=(M_x,Rin_x,Rout_x) with port labels P={0,1,2,3}. Each of the four edges of C_A transfers (0→0); each edge of C_B transfers (2→2), under the declared H_diag={(p,p):p∈P}. The V29 primitive TRANSFER increments exactly one source Rout and one target Rin. PASS increments a specified M entry. The time-ordered event history is separately typed; it is not a seventh spatial axis.

The previously explicit **auxiliary** completed-cycle coupling appends the V17 block
A: 012→013→023→012, h ← h a, a=(0,2,1),
or
B: 012→013→123→012, h ← h b, b=(2,1,0),
where h∈S3, e=(0,1,2), and (p q)[i]=p[q[i]]. This is the R674 model assumption. No autonomous V27 scheduler or physical BRC evolution is assumed.

Full typed state S consists of all L_x, current h at the shared Cell o, and the phase of any partially executed block if atomic events are allowed. The complete-block subsystem is the domain of the principal theorem. We keep the full relation/branch provenance while comparing observers.

## 2. The order-two typed relabeling

Define four separate, explicitly typed actions:

(1) Native X6 axis skeleton: σ_X=(E1 E3)(E2 E4), leaving E5,E6 fixed. Apply σ_X to relative Cell displacements, and to every directed edge, preserving edge direction and event order.

(2) V29 port names: σ_P=(0 2), leaving 1 and 3 fixed. On all ledger entries, send M_x[p,q] to M_{σ_X x}[σ_P p,σ_P q], and similarly Rin/Rout. Since H_diag is the diagonal relation, it is invariant under simultaneous source/target port permutation.

(3) V17 four active-label names: τ=(0 1), leaving 2 and 3 fixed. It sends the entire A triple sequence to B, and B to A (triples treated as labeled sets).

(4) The base-triple 012 slot coordinate change c=(1,0,2)∈S3. Send the terminal shared frame h to c h c^{-1}; here c^{-1}=c.

Let R be the joint action. It is an involution R²=id and sends a complete cycle label A↔B. On event words define ρ by exchanging A and B without reversing their temporal positions.

## 3. Exact theorem: event-level covariance

**Theorem R675-A.** For every allowed V29 PASS or TRANSFER primitive event e on the declared typed graph, R T_e = T_{R e} R, where e is relabeled in space and ports. For every completed R674 loop event A or B, R T_A=T_B R and R T_B=T_A R. Consequently, for every finite complete-block word w∈{A,B}*, every initial typed state S in the complete-block subsystem, and the corresponding transformed initial state R S,

R(T_w(S)) = T_{ρ(w)}(R S).

**Proof.** The graph action sends the successive directed edges of C_A to those of C_B, with their order unchanged, and vice versa. For PASS at x,p→q the only newly incremented ledger entry is M_x[p,q]. Applying R before/after the increment produces the same unit increment in M_{σ_X x}[σ_P p,σ_P q]. The two TRANSFER increments have the same property for source Rout and target Rin; the allowed connection/port type remains allowed because H_diag is permutation invariant. Hence all V29 event maps commute with R in their typed form. Every local sum, u, Ω and global scalar Q transforms covariantly; the original exact conservation ΔQ=0 is preserved.

At the V17 level τ sends each triple along A to its counterpart along B:
012↦012, 013↦013, 023↦123, 012↦012.
Likewise τ sends B back to A. On the returned base triple 012 the induced change of ordered slot coordinates is c. Direct composition of the named swaps gives c a c^{-1}=b and c b c^{-1}=a. For h←h a we therefore have
c(h a)c^{-1}=(c h c^{-1})(c a c^{-1})=(c h c^{-1}) b,
and similarly for B. This proves the completed-block update identities. Induction over the length of w proves the word identity. QED.

**Scope of event level.** The V29 atomic-event identity holds for arbitrary nonnegative initial ledgers. The V17 part proves identity for the declared *completed V17 blocks*, with a base-triple frame; a separate varying-triple slot-coordinate map would be needed to restate it as a fixed-c formula at every internal V17 microstep.

## 4. Rigidity and failure of an untyped relabel

**Theorem R675-B (forced action on the used interfaces).** Assume a relabeling exchanges the two *directed* four-edge cycles, preserves o, uses an S6 permutation of six native positive axes, a uniform S4 port permutation, the original two V17 named triple sequences, and an inner S3 frame action. Then:
- E1↔E3 and E2↔E4 are forced; the unused E5,E6 may be fixed or exchanged.
- The port permutation must exchange ports 0↔2; ports 1,3 may be fixed or exchanged.
- The V17 active-label permutation is exactly τ=(0 1) if it exchanges these specified A,B triple sequences.
- The unique S3 inner conjugator exchanging a and b is c=(1,0,2).

**Proof.** From o, the only outgoing loop edges terminate at o+E1 and o+E3; the only incoming loop edges originate at o+E2 and o+E4. The oriented successor relation forces an exchange of outgoing axes E1,E3 and incoming axes E2,E4 when the cycles are exchanged. E5,E6 are unused. The A-event incidence occurs at port 0 and the B-event incidence at port 2; typed event matching forces their exchange. The first two triple sets 012 and 013 are fixed under A↔B, so {0,1} is preserved as a set while labels 2 and 3 are fixed; mapping 023 to 123 forces 0↔1. Finally a,b are distinct transpositions generating S3. If two inner conjugators both interchange them, their ratio centralizes both, hence centralizes S3; the center of S3 is trivial. The exhibited c exists and is unique. QED.

**Counterexamples.** A geometry-only loop exchange with fixed ports sends the first A TRANSFER to a B-edge event at port 0, whereas the B law requires port 2, so its Rout/Rin entries differ. A port-corrected spatial swap that fixes h sends the A output a to a while the B output is b≠a. Thus both a typed port action and the frame action are needed to attain this particular symmetry.

## 5. Holonomy fiber and scientific inference

At zero ledger and h=e, AB and BA give the same final *complete* V29 ledger and distinct holonomies ab=(1,2,0), ba=(2,0,1) (R674). The new typed rotation exchanges these complete histories and transforms their outputs by c(ab)c^{-1}=ba. The existing noncommutative memory is therefore **compatible with**, rather than an obstruction to, the declared order-two native-axis symmetry.

The result establishes a specific nontrivial covariance of a declared finite X6 subnetwork and its V29/V17 completed-block action. It does not select actual V27 autonomous events, provide a general S6 or full physical rotation action, or supply V39 cycle-current dynamics. The native/BRC-only arithmetic method is respected here by a symbolic typed group-and-incidence proof: no numerical native residual, π/trigonometric expansion, non-BRC physical simulation, or BRC execution is claimed.

## 6. Next discriminating research question

Define the V27 selector on the shared Cell using actual allowed source/port/direction constraints. Ask whether the scheduler itself is equivariant under R: for state S with enabled event set E(S), does E(RS)=R E(S)? If true, compose it with R675-A to obtain covariance of the **autonomously selected** law. If false, exhibit the smallest enabled-set mismatch and either preserve a typed direction-context state or construct a symmetry-compatible selector. Next incorporate the exact V39 j update, so any proposed quotient of (L,h,j,scheduler) is tested against future legality as well as current observables.

## Sources and evidence status

- R674 exact committed author proof: enterprise-math@7e85d3b0fe3543e28c91894c174090102babb6db, research_notes/r674_v29_shared_cell_double_loop_20261109_emr3/R674_PROOF.zh-CN.md.
- V29 original event law: enterprise-math@b62110008321d9147212cb89f2627ff613c2550d, research_notes/X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md.
- Frozen scientific frontier preserved: R462@18783e01e3646c72b7aab3b16d3f565e83e6446f.
- Proof status: complete deductive argument within the R674 declared model. No native BRC numerical execution or independent Driver acceptance.
