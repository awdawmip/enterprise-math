# PREFIX-529 — A 51-state phase-resolving BRC–`aAc` transducer and a sharp one-bit memory witness

**Date:** 2026-11-06 (Asia/Shanghai). **Research line:** `RS-X6-NATIVE-ROTATION-DYNAMICS`.
**Scientific input (frozen):** `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`, as carried by PREFIX-518/522/525–528.
**Author evidence:** exact constructive proof below, independently reconstructed literal-word enumeration through four macrosteps, and integer weighted dynamic programming through nine macrosteps.
**Status:** `AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED`.

## 1. Question and declared observation

PREFIX-528 gives a sharp **degree-22 scalar aggregate** recurrence for the `(p_1,H)` histogram, with `H` the literal `aAc` gate count. A scalar aggregate recurrence does not automatically supply the memory needed to continue an individual history. We ask for the *smallest phase-explicit finite controller* that retains exact `H` updates under every **legal labelled future macrostep** while recovering **all six** native signed-axis BRC pair counts with additive visit counters and known endpoints.

Keep separate: the finite control state; the additive accumulators `(K_1,...,K_6,H)`; the initial phase needed for endpoint correction; and the native microstep/Cell provenance record when a later observer requests intermediate Cells or branch identity. Our state-minimality statement concerns the phase-explicit *finite controller*, not arbitrary encoded states or a full source archive.

## 2. Exact finite model and prior lemma

Let the four candidate STARs be `A={L1,L3,L6}`, `B={L1,L4,L5}`, `C={L2,L3,L5}`, `D={L2,L4,L6}`. A signed directed phase is `(j,p,c)`, where `j` is a STAR and `p,c` are two different signed axes of opposite sign in that STAR. There are 48 phases. Every phase has three admissible next phases and three incoming next-phase predecessors.

For an edge `s -> r`, with current signed axis `c_s` and next signed axis `c_r`, the original two separately labelled native microstep realizations are:

- `INNER`: `(-c_s,c_r)`;
- `OUTER`: `(c_r,-c_s)`.

They have the **same signed multiset** but different order/intermediate Cell. In the fixed chart `+L1=a`, `-L1=A`, `+/-L3=c`, other directions `_`, let `H(w)` count literal `aAc` occurrences in the concatenated native word. PREFIX-522's local gate lemma (also checked directly in the attached program) says that an event is completed at macrostep `r` precisely when the **previous and present branch labels are both INNER** and the new directed phase equals

`T=(A,+L1,-L3)`, encoded in zero-based STAR notation as `(0,1,-3)`.

The exact predecessor set is

`Pred(T) = {(A,-L6,+L1), (B,-L4,+L1), (B,-L5,+L1)}`,

so `|Pred(T)|=3`. These are combinatorial STAR-phase identities, not an assertion about the unknown full native rotation law.

## 3. The 51-state theorem

**Theorem (exact gate-control quotient).** Define the controller state space

`Q = {(s,*) : s not in Pred(T)} ∪ {(s,I),(s,O) : s in Pred(T)}`.

It has `45 + 2*3 = 51` elements. At initialization the controller is `(s,O)` if `s∈Pred(T)` and `(s,*)` otherwise (the `O` tag here means *no previous INNER*, including the empty prefix). For each legal macro transition `s -> r` with supplied branch `b∈{I,O}`, emit

`ΔH = 1_{s∈Pred(T)} 1_{memory=I} 1_{b=I} 1_{r=T}`

and update memory to `b` when `r∈Pred(T)`, or `*` otherwise. Accumulate the emitted `ΔH`.

For every initial phase, every finite branch-labelled admissible history, and every admissible future suffix, this transducer recovers the exact literal `aAc` count. The original phase-plus-last-branch presentation has 96 finite controller states and 576 labelled outgoing transitions; the quotient has 51 states and 306 such transitions (each state has six labelled choices). Both counts refer to finite *control* metadata, separate from the integer generating-function coefficient arithmetic and explicit raw Cell/source logs.

**Proof.** The prior local gate lemma shows that the only influence of the previously selected branch on a future event is at the **immediately next** macrostep. If the present phase `s∉Pred(T)`, no legal next phase equals `T`, so either previous label produces `ΔH=0` for every next legal labelled edge. Once that edge is taken, the new previous label is just its supplied branch `b`. Hence the old label is safely erased at exactly these 45 phases. At each `s∈Pred(T)`, the update above reproduces the local lemma. Induction on the length of the future suffix gives exactness for all finite histories and suffixes. The state and edge counts follow from the three predecessors and six labelled edges per state. ∎

## 4. Sharp conditional minimality and a shortest continuation counterexample

**Theorem (phase-resolving lower bound).** Within deterministic controllers whose finite state exposes the **current directed phase** and whose other accumulator variables preserve exactly the declared running BRC visits and `H`, every phase `s∈Pred(T)` requires **two distinguishable branch-memory categories**. Every `s∉Pred(T)` requires only one. Consequently 51 is the exact minimum number of phase-resolving *control categories* for this observer and future-operation language. This is not a general automaton-state lower bound after suppressing or changing the phase observer.

**Proof (lower bound).** Every directed phase has at least one incoming admissible edge. Fix any `s∈Pred(T)` and any predecessor phase `a -> s`. Take one-edge histories with the **same** initial phase and endpoint `s`, one INNER and one OUTER. Their two signed primitive steps are the same multiset. Thus all six `K_a`, all six BRC pair counts, and the initial/final phases agree; both have `H=0`, because a one-macrostep history has only two native steps. The legal common suffix `s -> T`, labelled INNER, produces a new gate event for the first history and none for the second. They are distinguishable by one legal common future operation, so the finite controller must retain two categories at this phase. Distinct current phases are distinct because the current phase itself belongs to the stipulated observer. At other phases the sufficiency proof shows that the previous branch is unnecessary. ∎

**Explicit shortest witness.** Choose

`a=(A,+L3,-L6)`, `s=(A,-L6,+L1)`, `T=(A,+L1,-L3)`.

The one-macrostep alternatives `a -> s` are:

- `u=INNER = (+L6,+L1)` with colors `_a`;
- `v=OUTER = (+L1,+L6)` with colors `a_`.

Both have `H=0`, six-axis `p=(0,0,0,0,0,0)`, exactly the same signed-axis multiplicities, and the same start and end phase. Append the **same** legal `s -> T` INNER branch `x=(-L1,-L3)`. Then

`ux=(+L6,+L1,-L1,-L3)`, colors `_aAc`, so `H(ux)=1`;

`vx=(+L1,+L6,-L1,-L3)`, colors `a_Ac`, so `H(vx)=0`.

Both augmented histories still have the same six-axis BRC pair vector `(1,0,0,0,0,0)` and terminal phase `T`. This is a **length-one prefix, length-one shared suffix** witness; no nonempty gate is possible in an empty prefix. It is a concrete obstruction to using the current `(p_1,H)` (or even the full six-axis BRC vector, `H`, and terminal phase) as a future-complete state without the conditional branch bit.

## 5. Six-axis BRC exact transfer, with source semantics preserved

For axis `a`, define `σ_a(s)=sign(c_s)` when `|c_s|=a`, else `0`. For an edge `s -> r`, both choices visit axes `|c_s|` and `|c_r|` once, independently of their INNER/OUTER order. Let `K_a(w)` count all visits to unsigned axis `a` in the concatenated primitive word. The native signed-axis pair-cancellation observer is

`p_a(w) = min(N_a^+(w),N_a^-(w))`.

The endpoint telescope from PREFIX-525 gives for any valid path from `s_0` to `s_d`:

`N_a^-(w) - N_a^+(w) = σ_a(s_0) - σ_a(s_d)` and

`p_a(w) = [ K_a(w) - |σ_a(s_d)-σ_a(s_0)| ]/2`.

Thus the 51-state controller plus the **six additive** visit counters, `H`, initial phase and current phase is exact for the joint declared observer `(p_1,...,p_6,H,current phase)` and all legal labelled futures. The transfer increment is `ΔK_a = 1_{|c_s|=a}+1_{|c_r|=a}`. Induction establishes exactness at every depth.

For a simultaneous generating function, give each phase-labelled edge the weight

`z^{ΔH} · ∏_{a=1}^6 x_a^{1_{|c_s|=a}+1_{|c_r|=a}}`.

Let `M(x,z)` be the corresponding 51-by-51 transition matrix (row destination, column origin), summing distinct labelled edges rather than merging their multiplicity. For each starting phase `s`, initialize the unique empty-history controller state as `v_s` and define the terminal readout at current phase `r` by `R_s(r)=∏_a x_a^{-|σ_a(r)-σ_a(s)|}`. Then the exact formal Laurent-polynomial identity

`Σ_{|w|=d} z^{H(w)} ∏_a q_a^{p_a(w)} = [ Σ_{s∈S} R_s^T M(x,z)^d v_s ]_{x_a^2=q_a}`

holds for every integer `d≥0`. Every resulting monomial exponent of `x_a` is even and nonnegative by the signed-pair identity. The bracket indicates this **verified even-exponent substitution**, not arbitrary square-root numerical evaluation. This is an exact full six-axis signed-BRC/gate construction. Source histories remain separately available when intermediate Cell or provenance queries are part of the observer.

## 6. Exact certificate and resource accounting

`PREFIX529_fiber_minimality_certificate.py` builds all 48 signed directed phases and their three outgoing edges from the four STAR definitions. It finds the exact three predecessors of `T`, checks the gate-memory distinguishing condition at all 48 phases, and verifies the explicit shortest witness. It directly enumerates **74,640** histories through depth four, reconstructs their native signed microsteps and literal words, independently checks `H` and **all six** BRC pair counts, and matches the 51-state incremental updates. It then compares independently written 96-state and 51-state integer weighted DPs for the `(p_1,H)` histogram through depth nine. Both produce identical coefficient dictionaries at each depth. Verdict: `ALL_CHECKS_PASS`.

The control-only arithmetic budget is 51 rather than 96 states and 306 rather than 576 labelled transitions (a **46.875% decrease** in both counts). At depth nine, the implemented dynamic programming has 7,111 reachable keys in the compressed representation versus 13,380 in the original `(start,phase,branch,K_1,H)` representation. This is a measured dictionary-key count, not a benchmark of wall time or a claim that dense multivariate polynomial arithmetic is cheap. Generating full six-axis coefficient dictionaries increases polynomial size; the exact matrix identity still holds without such enumeration. The sharp scalar order 22 of PREFIX-528 and the 51 phase-resolving finite-control categories solve different reduction problems.

The certificate is exact-integer/finite-combinatorial. The universal conclusions above follow from the specified transition law and induction, not by extrapolation from the exhaustive depth-four scan.

## 7. Method reuse, scope, next discriminating question

**BRC method:** typed signed-axis pair observer with retained raw INNER/OUTER paths, source branch identity and six-axis visit/endpoint relation; observer-preserving state quotient under every legal labelled macro suffix. Reuse: `PREFIX-525` endpoint BRC identity and `PREFIX-522` local `aAc` gate criterion; both re-derived on native literal words for the finite certificate. **No conventional trigonometric or physical-residual computation was used.**

**Next unit (PREFIX-530):** compare the 51-state full-six-axis transfer with the 48-dimensional order-two rank-one update from PREFIX-525, retaining input label multiplicity and all six visits; derive an explicit linear-system equivalence or construct a smallest witness where a purported further quotient loses a future observable. Separately compute sparse multivariate coefficient growth and end-to-end integer-bit cost before any performance claim. The broader goal of native arbitrary-three-axis `C6` generation and full native rotation selection remains open and has not been redefined by the four-STAR candidate calculation.

**Source references:** `research_notes/portable_direct/2026-11-06_prefix528_generic_joint_brc_gate_minimal_denominator.md`; `PREFIX527_exact_certificate.py`; PREFIX-522/525 results, all at their original commits; frozen native input commit above. P000 / ACTIVE world and current applicable method/portable protocols govern interpretation. All conclusions refer to this explicitly declared candidate four-STAR language.
