# R5 — Exact two-coordinate coherent Set controller as a weighted cube cover

Date: 2026-11-16. Frozen scientific input commit: 435e77af0d180eac32bd1f9c4c464bc4010b7551 (not rebased). Role: author-side portable research, independently reviewed: NOT_REVIEWED. Historical R5 provenance: EM-DIRECT-B78E55 / RA-33C87C2B703418F0706695E9 (not a new native CLAIM). This is an auxiliary exact source-labelled integer repair model, not native X6 or BRC-native dynamics.

## Problem and conventions

Let T be a finite set of immutable tail coordinates, J a finite set of d named controllable bits, and A={0,1}^J. A raw state is (t,a). A command Set_i(b) changes only controllable coordinate i to b. Let Y denote fixed typed output source libraries and G(t,a,y) their snapshot-correctness predicate (which can incorporate an integer resource slack). A deterministic Moore controller has finite internal states Q, fixed state outputs o:Q->Y, total initialization for each raw state and internally defined updates f_(i,b). Correctness means every permitted initialization is output-correct after every finite command sequence. No online tail input is supplied.

A controller is internally reset-coherent if, for each i, f_(i,b) composed after f_(i,c) equals f_(i,b), and all operations for different i commute. No assertion is made that unrestricted internally noncommutative controllers are coherent.

For S subset J and a source table y:{0,1}^S -> Y, define its eligible tail set

C(S,y)={t in T : for every a in A, G(t,a,y(a restricted to S))}.

Its cost is 2^|S| (number of internal states in its canonical orbit). Define W_J as the minimum total cost among finite families of these tables whose eligible tail sets cover T.

## Theorem — Exact internally coherent controller minimum

For every finite T,J and snapshot feasibility relation G for which the displayed covering problem is feasible, the minimum number of internal states of an internally reset-coherent correct deterministic Moore controller is exactly W_J. Transient internal states, overlapping initial belief supports and arbitrary output labels do not decrease this minimum within the coherent class.

**Lower bound.** For q in Q and a in A, apply once every coordinate reset Set_i(a_i) in any order, and denote its internal image p_a(q). Commutativity makes the order immaterial. The reset absorption laws imply f_(i,b)(p_a(q))=p_(a with coordinate i set to b)(q). Hence the image O(q)={p_a(q):a in A} is a closed orbit.

If O(q) and O(q') intersect, choose their common state z. Applying the full reset to assignment c to z gives p_c(q)=p_c(q') for every c, so the orbits coincide. Thus distinct full-reset image orbits are disjoint.

Define a~b iff p_a(q)=p_b(q). This is an equivalence relation stable under every coordinate reset. If a~b and a_i differs from b_i, apply resets for all other coordinates to arbitrary values; this proves that changing bit i alone never changes the image, regardless of other coordinates. Let F be the set of such forgotten coordinates and S=J\F. Conversely, bits in F can be changed one at a time without changing the image. If two assignments differing in an S-bit had equal images, the same argument would make that bit forgotten, a contradiction. It follows that O(q) contains exactly 2^|S| distinct states and is canonically indexed by assignments restricted to S.

For every fixed tail t select an initial controller state q for any one raw assignment. Execute the full-reset word for each a. It produces p_a(q), and correctness yields G(t,a,o(p_a(q))) for all a. Therefore t lies in the eligible set of the table of state outputs on O(q). The disjoint orbits covering all tails contribute total cost no greater than |Q|. Thus W_J<=|Q|.

**Upper bound.** For each table (S,y) of a covering family, build a disjoint internal component with 2^|S| states indexed by b in {0,1}^S. Give state b output y(b), and let Set_i(c) replace bit i in b if i is in S, otherwise leave the state unchanged. All required absorption and commutation identities hold. Initialize each raw state (t,a) in any component whose eligible set contains t, at state a|S. After every command word the internal index remains the restriction of the true controlled assignment, and outputs are feasible by the definition of C(S,y). The state count is exactly the cover cost, proving the reverse inequality.

## Exact genuine-source ring specialization

Use the inherited frozen cycle-of-triangles canonical source library L(r). For k>=3, u and r are k-bit masks and

q_k(u) = sum over i mod k of u_i*u_(i+1).

A canonical genuine source centre r serves raw old state u within additive slack s=2 exactly when (u AND NOT r)=0 and 0<=q_k(r)-q_k(u)<=2. The inherited common-source canonicalization theorem allows every fixed typed source library serving a set of raw snapshots to be replaced with a canonical L(r) without losing that set of obligations or raising its source cost. Therefore W_J for this particular model may be enumerated with r ranging over all 2^k masks. J={0,1}; the tail consists of the other k-2 bits, and raw mask is u=(t<<2)|a.

For each S subset {0,1}, enumerate all feasible output-centre tables for its 2^|S| states. Compress tables with exactly the same covered-tail bitset (at the same cost), then retain the cheapest representative of each bitset across S. A complete exact subset DP over covered tails proves the optimum for k=3..6. Empty-cover tables may be discarded since they cannot help cover T. No floating-point arithmetic or MILP solver enters these four lower bounds.

| k | Raw masks | Tails | Distinct nonempty eligible bitsets | Exact coherent state minimum |
|---|---:|---:|---:|---:|
| 3 | 8 | 2 | 3 | 3 |
| 4 | 16 | 4 | 7 | 4 |
| 5 | 32 | 8 | 19 | 7 |
| 6 | 64 | 16 | 41 | 11 |

The k=6 11-state witness comprises the following seven disjoint components; S below uses the literal two controlled coordinates (indices 0,1), and all decimal masks encode the covered tail set:

| S | Ordered genuine source centres for assignments on S | State count | Covered-tail bitset |
|---|---|---:|---:|
| {0,1} | 60,61,62,63 | 4 | 59520 |
| empty | 51 | 1 | 4096 |
| empty | 43 | 1 | 1285 |
| {1} | 37,39 | 2 | 514 |
| empty | 27 | 1 | 85 |
| empty | 23 | 1 | 51 |
| empty | 15 | 1 | 8 |

The union of these tail bitsets is all 16 tails (65535). The companion standard-library verifier checks all source-centre membership obligations and the complete finite table family; the symbolic theorem supplies correctness for arbitrary operation words.

For k=5, the coherent optimum 7 equals the already established static lower bound 7, so the unrestricted two-control optimum is also 7. For k=6, the inherited static lower bound is 10, and the coherent class requires exactly 11. The unrestricted controller minimum for k=6 is hence 10 or 11; whether an internally noncoherent 10-state realization exists remains open.

Additional local SciPy/HiGHS exploratory calculations on the same derived candidate family found coherent optima 19,29,51 for k=7,8,9 respectively (95,206,451 distinct eligible bitsets; zero reported gap and exact integer checks of selected witness tables). These larger finite lower values retain solver-dependent status; the standard-library exhaustive certificate currently covers k<=6 only. The original Python exploratory program and full outputs are separate local work products, not asserted as remotely preserved by this note.

## Reproduction, provenance and next problem

Run the companion VERIFY_R5_TWO_CONTROL_CUBE_EXACT.py with Python standard library. It re-enumerates all exact source-centre table masks, computes full 2^|T| subset-DP optima and independently checks each selected component across all four named assignments. The paired output summary is EXACT_R5_TWO_CONTROL_CUBE_EVIDENCE.json. Declared status: AUTHOR_PROVED / EXACT_FINITE_EXHAUSTIVE(k=3..6) / NOT_REVIEWED.

Source chain: research_notes/portable_direct/r5_one_bit_cycle_collapse_20261116/R5_ONE_BIT_ALTERNATING_CYCLE_COLLAPSE_THEOREM.md at 10b745c967702d59d183909548f372f6c2111bf9; research_notes/portable_direct/r5_single_reset_pair_loop_20261116/R5_SINGLE_RESET_PAIRED_LOOP_THEOREM.md at fdca33bd777759d4162a71e8f9cc920fd1b70281.

Next targeted question: for k=6,J={0,1},s=2 construct and verify an unrestricted internally noncoherent ten-state controller, or derive an additional transition-order invariant proving eleven states necessary without coherence. Independently, obtain non-solver certificates for k=7..9 and investigate whether any general multi-bit collapse comparable to the proven one-bit alternating-cycle theorem holds.

Control/source boundary: no formal Task/CLAIM/Result/Review is inferred from this file. The relevant control query at 2026-11-16 04:43 UTC reports no execution authorization. P000 and the ACTIVE worldview are left unchanged.
